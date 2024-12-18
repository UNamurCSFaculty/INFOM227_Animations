from __future__ import annotations

from enum import StrEnum
from functools import total_ordering
from typing import Any, Iterable

from manim import *
from manim_dataflow_analysis import *

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


class IntervalAnalysisScene(
    AbstractAnalysisScene[IntervalAnalysisValue, BoolExpression]
):
    title = "Interval Analysis"

    sorting_function = sorted

    lattice = IntervalAnalysisLattice(15)
