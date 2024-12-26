from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

import networkx as nx
from manim_dataflow_analysis import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from small.ast.symbol_table import FunctionSymbolTable

# Types


class SmallType(StrEnum):
    INT = "int"
    BOOL = "bool"


# Expressions


@dataclass(frozen=True)
class Variable:
    name: str

    def neg(self) -> BoolExpression:
        return BoolNotExpression(self)

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return symbol_table.get(self.name)

    def __str__(self) -> str:
        return self.name


@dataclass(frozen=True)
class IntConstant:
    value: int

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.INT

    def __str__(self) -> str:
        return str(self.value)


class IntBinaryOperator(StrEnum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"


@dataclass(frozen=True)
class IntBinaryExpression:
    left: IntExpression
    operator: IntBinaryOperator
    right: IntExpression

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.INT

    def __str__(self) -> str:
        return f"{self.left} {self.operator} {self.right}"


IntExpression = Variable | IntConstant | IntBinaryExpression


class IntComparisonOperator(StrEnum):
    LT = "<"
    GT = ">"
    LTE = "<="
    GTE = ">="

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> IntComparisonOperator:
        match self:
            case IntComparisonOperator.LT:
                return IntComparisonOperator.GTE
            case IntComparisonOperator.GT:
                return IntComparisonOperator.LTE
            case IntComparisonOperator.LTE:
                return IntComparisonOperator.GT
            case IntComparisonOperator.GTE:
                return IntComparisonOperator.LT


class EqualityOperator(StrEnum):
    EQ = "=="
    NEQ = "!="

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> EqualityOperator:
        match self:
            case EqualityOperator.EQ:
                return EqualityOperator.NEQ
            case EqualityOperator.NEQ:
                return EqualityOperator.EQ


class BoolComparisonOperator(StrEnum):
    AND = "and"
    OR = "or"

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> BoolComparisonOperator:
        match self:
            case BoolComparisonOperator.AND:
                return BoolComparisonOperator.OR
            case BoolComparisonOperator.OR:
                return BoolComparisonOperator.AND


@dataclass(frozen=True)
class BoolConstant:
    value: bool

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> BoolExpression:
        return BoolConstant(not self.value)

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class IntComparisonExpression:
    left: IntExpression
    operator: IntComparisonOperator
    right: IntExpression

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> BoolExpression:
        return IntComparisonExpression(self.left, self.operator.neg(), self.right)

    def __str__(self) -> str:
        return f"{self.left} {self.operator} {self.right}"


@dataclass(frozen=True)
class IntEqualComparisonExpression:
    value1: IntExpression
    operator: EqualityOperator
    value2: IntExpression

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> BoolExpression:
        return IntEqualComparisonExpression(
            self.value1, self.operator.neg(), self.value2
        )

    def __str__(self) -> str:
        return f"{self.value1} {self.operator} {self.value2}"


@dataclass(frozen=True)
class BoolComparisonExpression:
    value1: BoolExpression
    operator: BoolComparisonOperator
    value2: BoolExpression

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> BoolExpression:
        return BoolComparisonExpression(self.value1, self.operator.neg(), self.value2)

    def __str__(self) -> str:
        return f"{self.value1} {self.operator} {self.value2}"


@dataclass(frozen=True)
class BoolNotExpression:
    value: BoolExpression

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> BoolExpression:
        return self.value

    def __str__(self) -> str:
        return f"!{self.value}"


@dataclass(frozen=True)
class BoolEqualComparisonExpression:
    value1: BoolExpression
    operator: EqualityOperator
    value2: BoolExpression

    def type(self, symbol_table: FunctionSymbolTable) -> SmallType:
        return SmallType.BOOL

    def neg(self) -> BoolExpression:
        return BoolEqualComparisonExpression(
            self.value1, self.operator.neg(), self.value2
        )

    def __str__(self) -> str:
        return f"{self.value1} {self.operator} {self.value2}"


BoolExpression = (
    Variable
    | BoolConstant
    | BoolNotExpression
    | IntComparisonExpression
    | IntEqualComparisonExpression
    | BoolEqualComparisonExpression
)


Expression = IntExpression | BoolExpression


@dataclass(frozen=True)
class FunctionCall:
    name: str
    arguments: tuple[Expression, ...]

    def __str__(self) -> str:
        return f"{self.name}({', '.join(str(arg) for arg in self.arguments)})"


# Statements


def sequence_cfg(
    statements: tuple[Statement, ...],
    previous_statements: list[tuple[Statement, BoolExpression, int | None]],
) -> tuple[
    list[tuple[Statement, BoolExpression, int | None]], nx.DiGraph[ProgramPoint]
]:
    graph: nx.DiGraph[ProgramPoint] = nx.DiGraph()

    for statement in statements:
        for previous_statement, condition, edge_case in previous_statements:
            graph.add_edge(
                ProgramPoint(previous_statement.line_number, previous_statement),
                ProgramPoint(statement.line_number, statement),
                case=edge_case,
                condition=condition,
            )

        previous_statements, statement_graph = statement.to_cfg()

        graph = nx.compose(graph, statement_graph)

    return previous_statements, graph


@dataclass(frozen=True)
class Assignment(AstStatement):
    line_number: int
    variable: Variable
    value: Expression | FunctionCall

    @property
    def header(self) -> str:
        return f"{self.variable} = {self.value}"

    def to_cfg(
        self,
    ) -> tuple[list[tuple[Statement, BoolExpression, int | None]], nx.DiGraph]:
        return [(self, BoolConstant(True), None)], nx.DiGraph()

    def __str__(self) -> str:
        return f"{self.header};"


@dataclass(frozen=True)
class IfElse(AstStatement):
    line_number: int
    condition: BoolExpression
    if_body: tuple[Statement, ...]
    else_body: tuple[Statement, ...]

    @property
    def header(self) -> str:
        return f"if ({self.condition})"

    def to_cfg(
        self,
    ) -> tuple[list[tuple[Statement, BoolExpression, int | None]], nx.DiGraph]:
        if_next_statements, if_graph = sequence_cfg(
            self.if_body,
            [(self, self.condition, True)],
        )
        else_next_statements, else_graph = sequence_cfg(
            self.else_body,
            [(self, self.condition.neg(), False)],
        )

        next_statements = if_next_statements + else_next_statements
        graph = nx.compose(if_graph, else_graph)

        return next_statements, graph

    def __str__(self) -> str:
        return "%s {\n\t%s\n} else {\n\t%s\n}" % (
            self.header,
            "\n\t".join(
                str(statement).replace("\n", "\n\t") for statement in self.if_body
            ),
            "\n\t".join(
                str(statement).replace("\n", "\n\t") for statement in self.else_body
            ),
        )


@dataclass(frozen=True)
class While(AstStatement):
    line_number: int
    condition: BoolExpression
    body: tuple[Statement, ...]

    @property
    def header(self) -> str:
        return f"while ({self.condition})"

    def to_cfg(
        self,
    ) -> tuple[list[tuple[Statement, BoolExpression, int | None]], nx.DiGraph]:
        previous_statements, graph = sequence_cfg(
            self.body, [(self, self.condition, True)]
        )

        for previous_statement, condition, edge_case in previous_statements:
            graph.add_edge(
                ProgramPoint(previous_statement.line_number, previous_statement),
                ProgramPoint(self.line_number, self),
                case=edge_case,
                condition=condition,
            )

        return [(self, self.condition.neg(), False)], graph

    def __str__(self) -> str:
        return "%s {\n\t%s\n}" % (
            self.header,
            "\n\t".join(
                str(statement).replace("\n", "\n\t") for statement in self.body
            ),
        )


@dataclass(frozen=True)
class Return(AstStatement):
    line_number: int
    value: Expression

    @property
    def header(self) -> str:
        return f"return {self.value}"

    def to_cfg(
        self,
    ) -> tuple[list[tuple[Statement, BoolExpression, int | None]], nx.DiGraph]:
        return [(self, BoolConstant(True), None)], nx.DiGraph()

    def __str__(self) -> str:
        return f"{self.header};"


Statement = Assignment | IfElse | While


# Program


@dataclass(frozen=True)
class Function(AstFunction):
    line_number: int = 1
    name: str = "main"
    parameters: tuple[str, ...] = ()
    variables: frozenset[str] = frozenset()
    body: tuple[Statement, ...] = ()
    function_code: str | None = None

    def to_cfg(self) -> tuple[ProgramPoint, nx.DiGraph[ProgramPoint]]:
        _, graph = sequence_cfg(self.body, [])
        return ProgramPoint(self.body[0].line_number, self.body[0]), graph

    def __str__(self) -> str:
        if self.function_code is not None:
            return self.function_code
        else:
            return "function %s(%s) {\n\t%s\n}" % (
                self.name,
                ", ".join(self.parameters),
                "\n\t".join(
                    str(statement).replace("\n", "\n\t") for statement in self.body
                ),
            )
