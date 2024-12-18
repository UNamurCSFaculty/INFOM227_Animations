from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from small.ast import SmallType


class SmallTypeWrapper:
    def __init__(self, type: SmallType | None):
        self.type = type


class FunctionSymbolTable:
    def __init__(
        self,
        root: RootSymbolTable,
        wrapped_parameters: dict[str, SmallTypeWrapper],
        wrapped_return_type: SmallTypeWrapper,
    ):
        self.root = root
        self._variables: dict[str, SmallTypeWrapper] = wrapped_parameters.copy()
        self._wrapped_parameters = wrapped_parameters
        self._wrapped_return_type = wrapped_return_type

    def use(self, variable: str, type: SmallType) -> None:
        wrapped_type = self._variables.get(variable)

        if wrapped_type is None:
            self._variables[variable] = SmallTypeWrapper(type)
        elif wrapped_type.type is None:
            wrapped_type.type = type
        elif wrapped_type.type != type:
            raise ValueError(
                f"{variable} was previously used as type {wrapped_type.type}"
            )

    def return_(self, type: SmallType) -> None:
        if self._wrapped_return_type.type is None:
            self._wrapped_return_type.type = type
        elif self._wrapped_return_type.type != type:
            raise ValueError(
                f"Function previously returned type {self._wrapped_return_type.type}"
            )

    def get(self, variable: str) -> SmallType:
        wrapped_type = self._variables.get(variable)

        if wrapped_type is None:
            raise ValueError(
                f"Variable {variable} has never been used in this function"
            )

        return wrapped_type.type

    def variables(self) -> frozenset[str]:
        return frozenset(self._variables.keys())


class RootSymbolTable:
    def __init__(self):
        self._functions: dict[
            str,
            tuple[dict[str, SmallTypeWrapper], SmallTypeWrapper],
        ] = {}

    def declare_function(
        self,
        name: str,
        parameters: tuple[str, ...],
    ) -> FunctionSymbolTable:
        if name in self._functions:
            raise ValueError(f"Function {name} already declared")

        wrapped_parameters = {
            argument: SmallTypeWrapper(None) for argument in parameters
        }
        wrapped_return_type = SmallTypeWrapper(None)

        function_symbol_table = FunctionSymbolTable(
            self, wrapped_parameters, wrapped_return_type
        )

        self._functions[name] = (
            wrapped_parameters,
            wrapped_return_type,
        )

        return function_symbol_table

    def call(self, name: str, argument_types: tuple[SmallType]) -> None:
        function = self._functions.get(name)

        if function is None:
            raise ValueError(f"Function {name} not declared")

        current_arguments_types, _ = function

        if len(argument_types) != len(current_arguments_types):
            raise ValueError(
                f"Function {name} called with wrong number of arguments, expected {len(current_arguments_types)} got {len(argument_types)}"
            )

        for position, (current_argument_type, argument_type) in enumerate(
            zip(current_arguments_types.values(), argument_types, strict=True)
        ):
            if current_argument_type.type is None:
                current_argument_type.type = argument_type
            elif current_argument_type.type != argument_type:
                raise ValueError(
                    f"Function {name} called with wrong argument type: {argument_type} at position {position}"
                )

    def return_function(self, name: str, return_type: SmallType) -> None:
        function = self._functions.get(name)

        if function is None:
            raise ValueError(f"Function {name} not declared")

        _, current_return_type = function

        if current_return_type.type is None:
            current_return_type.type = return_type
        elif current_return_type.type != return_type:
            raise ValueError(
                f"Function {name} returned with wrong return type: {return_type}"
            )
