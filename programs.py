from __future__ import annotations

from small import *

if_in_while = Function(
    "if_in_while",
    (),
    frozenset({"x", "y", "z"}),
    (
        Assignment(
            1,
            Variable("y"),
            IntBinaryExpression(IntConstant(5), IntBinaryOperator.MUL, IntConstant(2)),
        ),
        While(
            2,
            IntComparisonExpression(
                Variable("x"), IntComparisonOperator.GT, IntConstant(0)
            ),
            (
                IfElse(
                    3,
                    Variable("b"),
                    (
                        Assignment(
                            4,
                            Variable("y"),
                            IntBinaryExpression(
                                Variable("x"), IntBinaryOperator.SUB, IntConstant(2)
                            ),
                        ),
                    ),
                    (
                        Assignment(
                            5,
                            Variable("y"),
                            IntBinaryExpression(
                                Variable("x"), IntBinaryOperator.ADD, IntConstant(2)
                            ),
                        ),
                    ),
                ),
            ),
        ),
        Return(6, Variable("y")),
    ),
)

simple_if = Function(
    "simple_if",
    ("a",),
    frozenset({"b", "c"}),
    (
        Assignment(
            2,
            Variable("b"),
            IntBinaryExpression(IntConstant(5), IntBinaryOperator.ADD, IntConstant(-5)),
        ),
        IfElse(
            3,
            IntComparisonExpression(
                Variable("b"), IntComparisonOperator.GT, IntConstant(0)
            ),
            (
                Assignment(
                    4,
                    Variable("c"),
                    IntBinaryExpression(
                        Variable("a"), IntBinaryOperator.ADD, IntConstant(2)
                    ),
                ),
            ),
            (
                Assignment(
                    6,
                    Variable("c"),
                    IntBinaryExpression(
                        Variable("b"), IntBinaryOperator.MUL, IntConstant(2)
                    ),
                ),
            ),
        ),
        Return(8, Variable("c")),
    ),
)

sum_function = Function(
    "sum",
    ("x",),
    frozenset({"i", "sum"}),
    (
        Assignment(
            2,
            Variable("i"),
            IntConstant(0),
        ),
        Assignment(
            3,
            Variable("sum"),
            IntConstant(0),
        ),
        While(
            4,
            IntComparisonExpression(
                Variable("i"), IntComparisonOperator.LT, Variable("x")
            ),
            (
                Assignment(
                    5,
                    Variable("sum"),
                    IntBinaryExpression(
                        Variable("sum"), IntBinaryOperator.ADD, Variable("i")
                    ),
                ),
                Assignment(
                    6,
                    Variable("i"),
                    IntBinaryExpression(
                        Variable("i"), IntBinaryOperator.ADD, IntConstant(1)
                    ),
                ),
            ),
        ),
        Return(8, Variable("sum")),
    ),
)

nested_if = Function(
    "nested_if",
    (),
    frozenset({"y", "x", "b"}),
    (
        Assignment(
            1,
            Variable("y"),
            IntBinaryExpression(IntConstant(5), IntBinaryOperator.MUL, IntConstant(2)),
        ),
        IfElse(
            2,
            Variable("b"),
            (
                IfElse(
                    3,
                    IntComparisonExpression(
                        Variable("b"), IntComparisonOperator.GT, IntConstant(0)
                    ),
                    (
                        Assignment(
                            4,
                            Variable("y"),
                            IntBinaryExpression(
                                Variable("x"), IntBinaryOperator.SUB, IntConstant(2)
                            ),
                        ),
                    ),
                    (
                        Assignment(
                            5,
                            Variable("y"),
                            IntBinaryExpression(
                                IntConstant(2), IntBinaryOperator.ADD, Variable("x")
                            ),
                        ),
                    ),
                ),
            ),
            (),
        ),
        Return(6, Variable("y")),
    ),
)
