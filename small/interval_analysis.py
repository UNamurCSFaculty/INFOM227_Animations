from __future__ import annotations

from enum import StrEnum
from functools import cached_property, total_ordering
from typing import Any, Iterable

from manim_dataflow_analysis import *

from small import read_string
from small.ast import *


@total_ordering
class IntervalExtremum(StrEnum):
    TOP = "⊤"
    BOTTOM = "⊥"

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, IntervalExtremum):
            return self == IntervalExtremum.BOTTOM and other == IntervalExtremum.TOP
        elif isinstance(other, (FloatIntervalValue, BoolIntervalValue)):
            return False
        else:
            return NotImplemented


@total_ordering
@dataclass(frozen=True, order=False)
class FloatIntervalValue:
    low: float
    high: float

    def __str__(self):
        return f"[{self.low}, {self.high}]"

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, IntervalExtremum):
            return True
        elif isinstance(other, FloatIntervalValue):
            return self.low < other.low or (
                self.low == other.low and self.high < other.high
            )
        elif isinstance(other, BoolIntervalValue):
            return False
        else:
            return NotImplemented


@total_ordering
@dataclass(frozen=True, order=False)
class BoolIntervalValue:
    low: bool
    high: bool

    def __str__(self):
        return f"[{self.low}, {self.high}]"

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, IntervalExtremum):
            return False
        elif isinstance(other, BoolIntervalValue):
            return self.low < other.low or (
                self.low == other.low and self.high < other.high
            )
        elif isinstance(other, FloatIntervalValue):
            return True
        else:
            return NotImplemented


IntervalAnalysisValue = IntervalExtremum | FloatIntervalValue | BoolIntervalValue


class IntervalAnalysisLattice(Lattice[IntervalAnalysisValue]):
    def __init__(self, interval_size: int = 500):
        self._interval_size = interval_size

    def top(self) -> IntervalAnalysisValue:
        return IntervalExtremum.TOP

    def bottom(self) -> IntervalAnalysisValue:
        return IntervalExtremum.BOTTOM

    def successors(
        self, value: IntervalAnalysisValue
    ) -> Iterable[IntervalAnalysisValue]:
        match value:
            case IntervalExtremum.TOP:
                return
            case IntervalExtremum.BOTTOM:
                yield BoolIntervalValue(True, True)
                yield BoolIntervalValue(False, False)
                yield FloatIntervalValue(0, 0)
                for i in range(1, self._interval_size + 1):
                    yield FloatIntervalValue(i, i)
                    yield FloatIntervalValue(-i, -i)
            case BoolIntervalValue(False, True):
                yield self.top()
            case BoolIntervalValue(False, False) | BoolIntervalValue(True, True):
                yield BoolIntervalValue(False, True)
            case FloatIntervalValue(low, high):
                if low == float("-inf") and high == float("inf"):
                    yield self.top()
                    return

                if low == -self._interval_size:
                    yield FloatIntervalValue(float("-inf"), high)
                elif low == float("inf"):
                    yield FloatIntervalValue(self._interval_size, high)
                elif low != float("-inf"):
                    yield FloatIntervalValue(low - 1, high)

                if high == self._interval_size:
                    yield FloatIntervalValue(low, float("inf"))
                elif high == float("-inf"):
                    yield FloatIntervalValue(low, -self._interval_size)
                elif high != float("inf"):
                    yield FloatIntervalValue(low, high + 1)

    def is_descendant(
        self, value: IntervalAnalysisValue, descendant: IntervalAnalysisValue
    ) -> bool:
        if value == descendant:
            return False

        match (value, descendant):
            case (IntervalExtremum.BOTTOM, _) | (_, IntervalExtremum.TOP):
                return True
            case (
                BoolIntervalValue(including_low, including_high),
                BoolIntervalValue(included_low, included_high),
            ):
                return included_low <= including_low and including_high <= included_high
            case (
                FloatIntervalValue(including_low, including_high),
                FloatIntervalValue(included_low, included_high),
            ):
                return included_low <= including_low and including_high <= included_high
            case _:
                return False

    def predecessors(
        self, value: IntervalAnalysisValue
    ) -> Iterable[IntervalAnalysisValue]:
        match value:
            case IntervalExtremum.TOP:
                yield BoolIntervalValue(False, True)
                yield FloatIntervalValue(float("-inf"), float("inf"))
            case IntervalExtremum.BOTTOM:
                return
            case BoolIntervalValue(False, False) | BoolIntervalValue(True, True):
                yield self.bottom()
            case BoolIntervalValue(False, True):
                yield BoolIntervalValue(False, False)
                yield BoolIntervalValue(True, True)
            case FloatIntervalValue(low, high):
                if low == high:
                    yield self.bottom()
                    return

                if low == float("-inf"):
                    yield FloatIntervalValue(-self._interval_size, high)
                else:
                    yield FloatIntervalValue(low + 1, high)

                if high == float("inf"):
                    yield FloatIntervalValue(low, self._interval_size)
                else:
                    yield FloatIntervalValue(low, high - 1)

    def is_ancestor(
        self, value: IntervalAnalysisValue, ancestor: IntervalAnalysisValue
    ) -> bool:
        if value == ancestor:
            return False

        match (value, ancestor):
            case (IntervalExtremum.TOP, _) | (_, IntervalExtremum.BOTTOM):
                return True
            case (
                BoolIntervalValue(including_low, including_high),
                BoolIntervalValue(included_low, included_high),
            ):
                return including_low <= included_low and included_high <= including_high
            case (
                FloatIntervalValue(including_low, including_high),
                FloatIntervalValue(included_low, included_high),
            ):
                return including_low <= included_low and included_high <= including_high
            case _:
                return False

    def join(
        self, value1: IntervalAnalysisValue, value2: IntervalAnalysisValue
    ) -> IntervalAnalysisValue:
        if value1 == value2:
            return value1

        match (value1, value2):
            case (IntervalExtremum.BOTTOM, value) | (value, IntervalExtremum.BOTTOM):
                return value
            case (FloatIntervalValue(low1, high1), FloatIntervalValue(low2, high2)):
                return FloatIntervalValue(min(low1, low2), max(high1, high2))
            case (BoolIntervalValue(low1, high1), BoolIntervalValue(low2, high2)):
                return BoolIntervalValue(min(low1, low2), max(high1, high2))
            case _:
                return self.top()

    def meet(
        self, value1: IntervalAnalysisValue, value2: IntervalAnalysisValue
    ) -> IntervalAnalysisValue:
        if value1 == value2:
            return value1

        match (value1, value2):
            case (IntervalExtremum.TOP, value) | (value, IntervalExtremum.TOP):
                return value
            case (FloatIntervalValue(low1, high1), FloatIntervalValue(low2, high2)):
                return FloatIntervalValue(max(low1, low2), min(high1, high2))
            case (BoolIntervalValue(low1, high1), BoolIntervalValue(low2, high2)):
                return BoolIntervalValue(max(low1, low2), min(high1, high2))
            case _:
                return self.bottom()


class IntervalAnalysisWideningOperator(WideningOperator[IntervalAnalysisValue]):
    instances = [
        (
            r"W(\bot, l_{new})",
            r"l_{new}",
        ),
        (
            r"W([a, b], [c, d])",
            r"[if\ a \leq c\ then\ a\ else\ -\infty,\ if\ b \geq d\ then\ b\ else\ +\infty]",
        ),
        (
            r"W(last, new)",
            r"last \sqcup new",
        ),
    ]

    def __init__(self, lattice: IntervalAnalysisLattice):
        self._lattice = lattice

    def apply(
        self, last_value: IntervalAnalysisValue, new_value: IntervalAnalysisValue
    ) -> tuple[IntervalAnalysisValue, int]:
        match (last_value, new_value):
            case (IntervalExtremum.BOTTOM, l_new):
                return l_new, 0
            case (FloatIntervalValue(a, b), FloatIntervalValue(c, d)):
                return (
                    FloatIntervalValue(
                        a if a <= c else float("-inf"),
                        b if b >= d else float("inf"),
                    ),
                    1,
                )
            case _:
                return self._lattice.join(last_value, new_value), 2


class IntervalAnalysisFlowFunction(FlowFunction[IntervalAnalysisValue]):
    instances = [
        (
            r"f [[ x = c ]] (\phi)",
            r"\phi[x \mapsto [c, c]]",
            r"c \in \mathbb{Z}",
        ),
        (
            r"f [[ x = y ]] (\phi)",
            r"\phi[x \mapsto \phi(y)]",
            r"y \in < Var >",
        ),
        (
            r"f [[ x = c + d ]] (\phi)",
            r"\phi[x \mapsto [c + d, c + d]]",
            r"c \in \mathbb{Z} \wedge d \in \mathbb{Z}",
        ),
        (
            r"f [[ x = y + c ]] (\phi)",
            r"\phi[x \mapsto [\phi(y).low +_\infty c, \phi(y).high +_\infty c]]",
            r"c \in \mathbb{Z}",
        ),
        (
            r"f [[ x = y + c ]] (\phi)",
            r"\phi[x \mapsto \top]",
            r"",
        ),
        (
            r"f [[ x = c + y ]] (\phi)",
            r"\phi[x \mapsto f [[ x = y + c ]] (\phi)]",
            None,
        ),
        (
            r"f [[ x = y + z ]] (\phi)",
            r"\phi[x \mapsto \top]",
            r"\phi(y).low +_\infty \phi(z).low = ?",
        ),
        (
            r"f [[ x = y + z ]] (\phi)",
            r"\phi[x \mapsto \top]",
            r"\phi(y).high +_\infty \phi(z).high = ?",
        ),
        (
            r"f [[ x = y + z ]] (\phi)",
            r"\phi[x \mapsto \top]",
            r"\phi(y).low +_\infty \phi(z).low = +\infty \wedge \phi(y).high +_\infty \phi(z).high = -\infty",
        ),
        (
            r"f [[ x = y + z ]] (\phi)",
            r"\phi[x \mapsto [\phi(y).low +_\infty \phi(z).low, \phi(y).high +_\infty \phi(z).high]]",
            r"",
        ),
        (
            r"f [[ x = y * z ]] (\phi)",
            r"\phi[x \mapsto \top]",
            r"\phi(y).low *_\infty \phi(z).low = ?",
        ),
        (
            r"f [[ x = y * z ]] (\phi)",
            r"\phi[x \mapsto \top]",
            r"\phi(y).high *_\infty \phi(z).high = ?",
        ),
        (
            r"f [[ x = y * z ]] (\phi)",
            r"\phi[x \mapsto \top]",
            r"\phi(y).low *_\infty \phi(z).low = +\infty \wedge \phi(y).high *_\infty \phi(z).high = -\infty",
        ),
        (
            r"f [[ x = y * z ]] (\phi)",
            r"\phi[x \mapsto [\phi(y).low *_\infty \phi(z).low, \phi(y).high *_\infty \phi(z).high]]",
            r"\phi(y).low \geq 0 \wedge \phi(z).low \geq 0 \wedge \phi(y).high \geq 0 \wedge \phi(z).high \geq 0",
        ),
        (
            r"f [[ x = E ]] (\phi)",
            r"\phi[x \mapsto \top]",
            r"\text{E is any other case}",
        ),
    ]

    def get_variables(
        self,
        statement: AstStatement,
        abstract_environment: AbstractEnvironment[IntervalAnalysisValue],
    ) -> tuple[dict[str, IntervalAnalysisValue], int]:
        match statement:
            case Assignment(_, Variable(x), IntConstant(c)):
                return {x: FloatIntervalValue(c, c)}, 0
            case Assignment(_, Variable(x), Variable(y)):
                return {x: abstract_environment[y]}, 1
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(
                    IntConstant(c), IntBinaryOperator.ADD, IntConstant(d)
                ),
            ):
                return {x: FloatIntervalValue(c + d, c + d)}, 2
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, IntConstant(c)),
            ) if isinstance(y_value := abstract_environment[y], FloatIntervalValue):
                return {x: FloatIntervalValue(y_value.low + c, y_value.high + c)}, 3
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, IntConstant(c)),
            ):
                return {x: IntervalExtremum.TOP}, 4
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
                return variables, 5
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, Variable(z)),
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(z_value := abstract_environment[z], FloatIntervalValue)
                and y_value.low + z_value.low == float("nan")
            ):
                return {x: IntervalExtremum.TOP}, 6
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, Variable(z)),
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(z_value := abstract_environment[z], FloatIntervalValue)
                and y_value.high + z_value.high == float("nan")
            ):
                return {x: IntervalExtremum.TOP}, 7
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, Variable(z)),
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(z_value := abstract_environment[z], FloatIntervalValue)
                and y_value.low + z_value.low == float("inf")
                and y_value.high + z_value.high == float("-inf")
            ):
                return {x: IntervalExtremum.TOP}, 8
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.ADD, Variable(z)),
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(z_value := abstract_environment[z], FloatIntervalValue)
            ):
                return {
                    x: FloatIntervalValue(
                        y_value.low + z_value.low,
                        y_value.high + z_value.high,
                    )
                }, 9
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.MUL, Variable(z)),
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(z_value := abstract_environment[z], FloatIntervalValue)
                and y_value.low * z_value.low == float("nan")
            ):
                return {x: IntervalExtremum.TOP}, 10
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.MUL, Variable(z)),
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(z_value := abstract_environment[z], FloatIntervalValue)
                and y_value.high * z_value.high == float("nan")
            ):
                return {x: IntervalExtremum.TOP}, 11
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.MUL, Variable(z)),
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(z_value := abstract_environment[z], FloatIntervalValue)
                and y_value.low * z_value.low == float("inf")
                and y_value.high * z_value.high == float("-inf")
            ):
                return {x: IntervalExtremum.TOP}, 12
            case Assignment(
                _,
                Variable(x),
                IntBinaryExpression(Variable(y), IntBinaryOperator.MUL, Variable(z)),
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(z_value := abstract_environment[z], FloatIntervalValue)
                and y_value.low >= 0
                and y_value.high >= 0
                and z_value.low >= 0
                and z_value.high >= 0
            ):
                return {
                    x: FloatIntervalValue(
                        y_value.low * z_value.low,
                        y_value.high * z_value.high,
                    )
                }, 13
            case Assignment(_, Variable(x), _):
                return {x: IntervalExtremum.TOP}, 14
            case _:
                raise ValueError(f"Unsupported statement: {statement}")


class IntervalAnalysisControlFlowFunction(ControlFlowFunction[IntervalAnalysisValue]):
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

    flow_function = IntervalAnalysisFlowFunction()

    def get_variables(
        self,
        program_point: ProgramPoint,
        abstract_environment: AbstractEnvironment[IntervalAnalysisValue],
    ) -> tuple[dict[str, IntervalAnalysisValue], int | tuple[int, int]]:
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


class IntervalAnalysisConditionUpdateFunction(
    ConditionUpdateFunction[IntervalAnalysisValue, BoolExpression]
):
    instances = [
        (
            r"cg[[ y < c ]] (\phi)",
            r"\phi[y \mapsto [-\infty, c - 1]]",
            r"c \in \mathbb{Z}",
        ),
        (
            r"cg[[ c < y ]] (\phi)",
            r"cg[[ y > c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y < x ]] (\phi)",
            r"\phi[y \mapsto [-\infty, \phi(x).low - 1], x \mapsto [\phi(y).high + 1, +\infty]]",
            None,
        ),
        (
            r"cg[[ y > c ]] (\phi)",
            r"\phi[y \mapsto [c + 1, +\infty]]",
            r"c \in \mathbb{Z}",
        ),
        (
            r"cg[[ c > y ]] (\phi)",
            r"cg[[ y < c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y > x ]] (\phi)",
            r"\phi[y \mapsto [\phi(x).high + 1, +\infty], x \mapsto [-\infty, \phi(y).low - 1]]",
            None,
        ),
        (
            r"cg[[ y <= c ]] (\phi)",
            r"\phi[y \mapsto [-\infty, c]]",
            r"c \in \mathbb{Z}",
        ),
        (
            r"cg[[ c <= y ]] (\phi)",
            r"cg[[ y >= c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y <= x ]] (\phi)",
            r"\phi[y \mapsto [-\infty, \phi(x).low], x \mapsto [\phi(y).high, +\infty]]",
            None,
        ),
        (
            r"cg[[ y >= c ]] (\phi)",
            r"\phi[y \mapsto [c, \infty]]",
            r"c \in \mathbb{Z}",
        ),
        (
            r"cg[[ c >= y ]] (\phi)",
            r"cg[[ y <= c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y >= x ]] (\phi)",
            r"\phi[y \mapsto [\phi(x).high, +\infty], x \mapsto [-\infty, \phi(y).low]]",
            None,
        ),
        (
            r"cg[[ y == c ]] (\phi)",
            r"\phi[y \mapsto [c, c]]",
            r"c \in \mathbb{Z}",
        ),
        (
            r"cg[[ c == y ]] (\phi)",
            r"cg[[ y == c ]] (\phi)",
            None,
        ),
        (
            r"cg[[ y == x ]] (\phi)",
            r"\phi[y \mapsto \phi(y), x \mapsto \phi(y)]",
            r"\phi(y) \neq \bot \wedge \phi(x) = \bot",
        ),
        (
            r"cg[[ y == x ]] (\phi)",
            r"\phi[y \mapsto \phi(x), x \mapsto \phi(x)]",
            r"\phi(y) = \bot \wedge \phi(x) \neq \bot",
        ),
        (
            r"cg[[ False ]] (\phi)",
            r"\bot",
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
        abstract_environment: AbstractEnvironment[IntervalAnalysisValue],
    ) -> tuple[dict[str, IntervalAnalysisValue] | None, int]:
        match condition:
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.LT, IntConstant(c)
            ):
                return {y: FloatIntervalValue(float("-inf"), c - 1)}, 0
            case IntComparisonExpression(
                IntConstant(c), IntComparisonOperator.LT, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), IntComparisonOperator.GT, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 1
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.LT, Variable(x)
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(x_value := abstract_environment[x], FloatIntervalValue)
            ):
                return {
                    y: FloatIntervalValue(float("-inf"), x_value.low - 1),
                    x: FloatIntervalValue(y_value.high + 1, float("inf")),
                }, 2
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GT, IntConstant(c)
            ):
                return {y: FloatIntervalValue(c + 1, float("inf"))}, 3
            case IntComparisonExpression(
                IntConstant(c), IntComparisonOperator.GT, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), IntComparisonOperator.LT, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 4
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GT, Variable(x)
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(x_value := abstract_environment[x], FloatIntervalValue)
            ):
                return {
                    y: FloatIntervalValue(x_value.high + 1, float("inf")),
                    x: FloatIntervalValue(float("-inf"), y_value.low - 1),
                }, 5
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.LTE, IntConstant(c)
            ):
                return {y: FloatIntervalValue(float("-inf"), c)}, 6
            case IntComparisonExpression(
                IntConstant(c), IntComparisonOperator.LTE, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), IntComparisonOperator.GTE, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 7
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.LTE, Variable(x)
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(x_value := abstract_environment[x], FloatIntervalValue)
            ):
                return {
                    y: FloatIntervalValue(float("-inf"), x_value.low),
                    x: FloatIntervalValue(y_value.high, float("inf")),
                }, 8
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GTE, IntConstant(c)
            ):
                return {y: FloatIntervalValue(c, float("inf"))}, 9
            case IntComparisonExpression(
                IntConstant(c), IntComparisonOperator.GTE, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), IntComparisonOperator.LTE, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 10
            case IntComparisonExpression(
                Variable(y), IntComparisonOperator.GTE, Variable(x)
            ) if (
                isinstance(y_value := abstract_environment[y], FloatIntervalValue)
                and isinstance(x_value := abstract_environment[x], FloatIntervalValue)
            ):
                return {
                    y: FloatIntervalValue(x_value.high, float("inf")),
                    x: FloatIntervalValue(float("-inf"), y_value.low),
                }, 11
            case IntComparisonExpression(
                Variable(y), EqualityOperator.EQ, IntConstant(c)
            ):
                return {y: FloatIntervalValue(c, c)}, 12
            case IntComparisonExpression(
                IntConstant(c), EqualityOperator.EQ, Variable(y)
            ):
                variables, _ = self.get_variables(
                    IntComparisonExpression(
                        Variable(y), EqualityOperator.EQ, IntConstant(c)
                    ),
                    abstract_environment,
                )
                return variables, 13
            case IntComparisonExpression(
                Variable(y), EqualityOperator.EQ, Variable(x)
            ) if (
                abstract_environment[y] != IntervalExtremum.BOTTOM
                and abstract_environment[x] == IntervalExtremum.BOTTOM
            ):
                return {y: abstract_environment[y], x: abstract_environment[y]}, 14
            case IntComparisonExpression(
                Variable(y), EqualityOperator.EQ, Variable(x)
            ) if (
                abstract_environment[y] == IntervalExtremum.BOTTOM
                and abstract_environment[x] != IntervalExtremum.BOTTOM
            ):
                return {y: abstract_environment[x], x: abstract_environment[x]}, 15
            case BoolConstant(False):
                return None, 16
            case _:
                return {}, 17


class AbstractIntervalAnalysisScene(
    AbstractAnalysisScene[IntervalAnalysisValue, BoolExpression]
):
    title = "Interval Analysis"

    sorting_function = sorted  # type: ignore

    program_string: str

    @cached_property
    def program(self) -> AstFunction:  # type: ignore
        return read_string(self.program_string)[0]

    lattice = IntervalAnalysisLattice()

    widening_operator = IntervalAnalysisWideningOperator(lattice)

    control_flow_function = IntervalAnalysisControlFlowFunction()

    condition_update_function = IntervalAnalysisConditionUpdateFunction()
