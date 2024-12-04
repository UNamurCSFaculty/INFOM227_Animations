from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from manim import *
from manim_dataflow_analysis.condition_update_function import ConditionUpdateFunction
from manim_dataflow_analysis.flow_function import ControlFlowFunction, FlowFunction
from manim_dataflow_analysis.lattice import FiniteSizeLattice
from manim_dataflow_analysis.scene import AbstractAnalysisScene

from programs import *
from small import *

if TYPE_CHECKING:
    from manim_dataflow_analysis.abstract_environment import AbstractEnvironment


class ZeroAnalysisValue(StrEnum):
    U = "U"
    Z = "Z"
    NZ = "NZ"
    BOTTOM = "BOTTOM"


class ZeroAnalysisFlowFunction(FlowFunction[ZeroAnalysisValue]):
    instances = [
        (
            r"f [[ x = c ]] (\phi)",
            r"\phi[x \mapsto Z]",
            r"c = 0",
        ),
        (
            r"f [[ x = c ]] (\phi)",
            r"\phi[x \mapsto NZ]",
            r"c \in \mathbb{Z}_0 \cup \{True, False\}",
        ),
        (
            r"f [[ x = y ]] (\phi)",
            r"\phi[x \mapsto \phi(y)]",
            r"y \in < Var >",
        ),
        (
            r"f [[ x = c + d ]] (\phi)",
            r"\phi[x \mapsto Z]",
            r"c = -d",
        ),
        (
            r"f [[ x = c + d ]] (\phi)",
            r"\phi[x \mapsto U]",
            r"",
        ),
        (
            r"f [[ x = y + z ]] (\phi)",
            r"\phi[x \mapsto Z]",
            r"\phi(y) = \phi(z) = Z",
        ),
        (
            r"f [[ x = y + z ]] (\phi)",
            r"\phi[x \mapsto U]",
            r"",
        ),
        (
            r"f [[ x = y + c ]] (\phi)",
            r"\phi[x \mapsto Z]",
            r"\phi(y) = Z \wedge c = 0",
        ),
        (
            r"f [[ x = y + c ]] (\phi)",
            r"\phi[x \mapsto NZ]",
            r"\phi(y) = Z \wedge c \neq 0",
        ),
        (
            r"f [[ x = y + c ]] (\phi)",
            r"\phi[x \mapsto NZ]",
            r"\phi(y) = NZ \wedge c = 0",
        ),
        (
            r"f [[ x = y + c ]] (\phi)",
            r"\phi[x \mapsto U]",
            r"",
        ),
        (
            r"f [[ x = c + y ]] (\phi)",
            r"f [[ x = y + c ]] (\phi)",
            None,
        ),
        (
            r"f [[ x = E ]] (\phi)",
            r"\phi[x \mapsto U]",
            r"\text{E is any other case}",
        ),
    ]

    def get_variables(
        self,
        statement: AstStatement,
        abstract_environment: AbstractEnvironment[ZeroAnalysisValue],
    ) -> tuple[dict[str, ZeroAnalysisValue], int]:
        match statement:
            case Assignment(_, Variable(x), IntConstant(c)) if c == 0:
                return {x: ZeroAnalysisValue.Z}, 0
            case Assignment(_, Variable(x), IntConstant(c)) | Assignment(
                _, Variable(x), BoolConstant(c)
            ):
                return {x: ZeroAnalysisValue.NZ}, 1
            case Assignment(_, Variable(x), Variable(y)):
                return {x: abstract_environment[y]}, 2
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(
                    IntConstant(c), IntBinaryOperator.ADD, IntConstant(d)
                ),
            ) if c == -d:
                return {x: ZeroAnalysisValue.Z}, 3
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(
                    IntConstant(_), IntBinaryOperator.ADD, IntConstant(_)
                ),
            ):
                return {x: ZeroAnalysisValue.U}, 4
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, Variable(z)),
            ) if abstract_environment[
                y
            ] == ZeroAnalysisValue.Z and abstract_environment[
                z
            ] == ZeroAnalysisValue.Z:
                return {x: ZeroAnalysisValue.Z}, 5
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(_), IntBinaryOperator.ADD, Variable(_)),
            ):
                return {x: ZeroAnalysisValue.U}, 6
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, IntConstant(c)),
            ) if abstract_environment[y] == ZeroAnalysisValue.Z and c == 0:
                return {x: ZeroAnalysisValue.Z}, 7
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, IntConstant(c)),
            ) if abstract_environment[y] == ZeroAnalysisValue.Z and c != 0:
                return {x: ZeroAnalysisValue.NZ}, 8
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, IntConstant(c)),
            ) if abstract_environment[y] == ZeroAnalysisValue.NZ and c == 0:
                return {x: ZeroAnalysisValue.NZ}, 9
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, IntConstant(c)),
            ):
                return {x: ZeroAnalysisValue.U}, 10
            case Assignment(
                i,
                Variable(x),
                IntBinaryExpression(IntConstant(c), IntBinaryOperator.ADD, Variable(y)),
            ):
                variables, _ = self.get_variables(
                    Assignment(
                        i,
                        Variable(x),
                        IntBinaryExpression(
                            Variable(y), IntBinaryOperator.ADD, IntConstant(c)
                        ),
                    ),
                    abstract_environment,
                )
                return (
                    variables,
                    11,
                )
            case Assignment(_, Variable(x), _):
                return {x: ZeroAnalysisValue.U}, 12
            case _:
                raise ValueError(f"Unsupported statement: {statement}")


class ZeroAnalysisControlFlowFunction(ControlFlowFunction[ZeroAnalysisValue]):
    instances = [
        (
            r"fg [[ p ]] (\phi)",
            r"f [[ P[p] ]] (\phi)",
            r"P[p] \equiv x = E",
        ),
        (
            r"fg [[ p ]] (\phi)",
            r"\phi",
            r"P[p] \equiv \text{while (E)} \lor P[p] \equiv \text{if (E)} \lor P[p] \equiv \text{return E}",  # noqa: E501
        ),
    ]

    flow_function = ZeroAnalysisFlowFunction()

    def get_variables(
        self,
        program_point: ProgramPoint,
        abstract_environment: AbstractEnvironment[ZeroAnalysisValue],
    ) -> tuple[dict[str, ZeroAnalysisValue], int | tuple[int, int]]:
        match program_point:
            case ProgramPoint(_, Assignment(i, Variable(x), expression)):
                variables, instance_id = self.flow_function.get_variables(
                    Assignment(i, Variable(x), expression), abstract_environment
                )
                return variables, (0, instance_id)
            case (
                ProgramPoint(_, While(_, _, _))
                | ProgramPoint(_, IfElse(_, _, _, _))
                | ProgramPoint(_, Return(_, _))
            ):
                return {}, 1
            case _:
                raise ValueError(f"Unsupported program point: {program_point}")


class ZeroAnalysisConditionUpdateFunction(
    ConditionUpdateFunction[ZeroAnalysisValue, BoolExpression]
):
    instances = [
        (
            r"cg[[ y < c ]] (\phi)",
            r"\phi[y \mapsto NZ]",
            r"c \leq 0",
        ),
        (
            r"cg[[ y < c ]] (\phi)",
            r"\phi[y \mapsto U]",
            r"c > 0",
        ),
        (
            r"cg[[ c < y ]] (\phi)",
            r"cg[[ y > c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y > c ]] (\phi)",
            r"\phi[y \mapsto NZ]",
            r"c \geq 0",
        ),
        (
            r"cg[[ y > c ]] (\phi)",
            r"\phi[y \mapsto U]",
            r"c < 0",
        ),
        (
            r"cg[[ c > y ]] (\phi)",
            r"cg[[ y < c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y <= c ]] (\phi)",
            r"\phi[y \mapsto NZ]",
            r"c < 0",
        ),
        (
            r"cg[[ y <= c ]] (\phi)",
            r"\phi[y \mapsto U]",
            r"c \geq 0",
        ),
        (
            r"cg[[ c <= y ]] (\phi)",
            r"cg[[ y >= c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y >= c ]] (\phi)",
            r"\phi[y \mapsto NZ]",
            r"c > 0",
        ),
        (
            r"cg[[ y >= c ]] (\phi)",
            r"\phi[y \mapsto NZ]",
            r"c > 0",
        ),
        (
            r"cg[[ y >= c ]] (\phi)",
            r"\phi[y \mapsto U]",
            r"c \leq 0",
        ),
        (
            r"cg[[ c >= y ]] (\phi)",
            r"cg[[ y <= c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y == c ]] (\phi)",
            r"\phi[y \mapsto Z]",
            r"c = 0",
        ),
        (
            r"cg[[ y == c ]] (\phi)",
            r"\phi[y \mapsto NZ]",
            r"c \neq 0",
        ),
        (
            r"cg[[ c == y ]] (\phi)",
            r"cg[[ y == c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y\ != c ]] (\phi)",
            r"\phi[y \mapsto NZ]",
            r"c = 0",
        ),
        (
            r"cg[[ y\ != c ]] (\phi)",
            r"\phi[y \mapsto U]",
            r"c \neq 0",
        ),
        (
            r"cg[[ c\ != y ]] (\phi)",
            r"cg[[ y\ != c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ E ]] (\phi)",
            r"\phi",
            r"\text{E is not defined in the other instances}",
        ),
    ]

    def get_variables(
        self,
        condition: BoolExpression,
        abstract_environment: AbstractEnvironment[ZeroAnalysisValue],
    ) -> tuple[dict[str, ZeroAnalysisValue], int]:
        match condition:
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.LT, IntConstant(c)
            ) if c <= 0:
                return {y: ZeroAnalysisValue.NZ}, 0
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.LT, IntConstant(c)
            ) if c > 0:
                return {y: ZeroAnalysisValue.U}, 1
            case IntComparisonExpression(
                IntConstant(c), IntComparisonOperator.LT, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), IntComparisonOperator.GT, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 2
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GT, IntConstant(c)
            ) if c >= 0:
                return {y: ZeroAnalysisValue.NZ}, 3
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GT, IntConstant(c)
            ) if c < 0:
                return {y: ZeroAnalysisValue.U}, 4
            case IntComparisonExpression(
                IntConstant(c), IntComparisonOperator.GT, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), IntComparisonOperator.LT, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 5
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.LTE, IntConstant(c)
            ) if c < 0:
                return {y: ZeroAnalysisValue.NZ}, 6
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.LTE, IntConstant(c)
            ) if c >= 0:
                return {y: ZeroAnalysisValue.U}, 7
            case IntComparisonExpression(
                IntConstant(c), IntComparisonOperator.LTE, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), IntComparisonOperator.GTE, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 8
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GTE, IntConstant(c)
            ) if c > 0:
                return {y: ZeroAnalysisValue.NZ}, 9
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GTE, IntConstant(c)
            ) if c >= 0:
                return {y: ZeroAnalysisValue.NZ}, 10
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GTE, IntConstant(c)
            ) if c < 0:
                return {y: ZeroAnalysisValue.U}, 11
            case IntComparisonExpression(
                IntConstant(c), IntComparisonOperator.GTE, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), IntComparisonOperator.LTE, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 12
            case IntEqualComparisonExpression(
                Variable(y), EqualityOperator.EQ, IntConstant(c)
            ) if c == 0:
                return {y: ZeroAnalysisValue.Z}, 13
            case IntEqualComparisonExpression(
                Variable(y), EqualityOperator.EQ, IntConstant(c)
            ) if c != 0:
                return {y: ZeroAnalysisValue.NZ}, 14
            case IntEqualComparisonExpression(
                IntConstant(c), EqualityOperator.EQ, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntEqualComparisonExpression(
                        Variable(y), EqualityOperator.EQ, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 15
            case IntEqualComparisonExpression(
                Variable(y), EqualityOperator.NEQ, IntConstant(c)
            ) if c == 0:
                return {y: ZeroAnalysisValue.NZ}, 16
            case IntEqualComparisonExpression(
                Variable(y), EqualityOperator.NEQ, IntConstant(c)
            ) if c != 0:
                return {y: ZeroAnalysisValue.U}, 17
            case IntEqualComparisonExpression(
                IntConstant(c), EqualityOperator.NEQ, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntEqualComparisonExpression(
                        Variable(y), EqualityOperator.NEQ, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 18
            case _:
                return {}, 19


class ZeroAnalysisScene(AbstractAnalysisScene[ZeroAnalysisValue, BoolExpression]):
    title = "Zero Analysis example"

    program = simple_if

    lattice = FiniteSizeLattice(
        (ZeroAnalysisValue.BOTTOM, ZeroAnalysisValue.Z),
        (ZeroAnalysisValue.BOTTOM, ZeroAnalysisValue.NZ),
        (ZeroAnalysisValue.Z, ZeroAnalysisValue.U),
        (ZeroAnalysisValue.NZ, ZeroAnalysisValue.U),
    )

    control_flow_function = ZeroAnalysisControlFlowFunction()

    condition_update_function = ZeroAnalysisConditionUpdateFunction()
