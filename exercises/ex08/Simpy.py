"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730468022"


class Simpy:
    """Simpy object."""
    
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Initialize a new Simpy object."""
        self.values = values
    
    def __str__(self) -> str:
        """Representation of a Simpy as a string."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill out values array by mutating object called on."""
        fill: list[float] = []
        i: int = 0
        while i < times:
            self.values.append(value)
            fill.append(value)
            i += 1
        self.values = fill

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        # Start an empty values list
        self.values = []
        # Be sure step is not 0.0 by asserting
        assert step != 0.0
        # When step is positive:
        if step > 0.0:
            # Add next value to values list
            next_value: float = start
            # While next value is less than stop value
            while next_value < stop:
                # Add next value to values list
                self.values.append(next_value)
                # Update next value by adding the step to it
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step
   
    def sum(self) -> float:
        """Delegate this algo to the built-in sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overlad for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float): 
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> float:
        """Operator overload for exponents."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for ==."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        else:
            assert len(self.values) == len(rhs.value)
            i: float = 0
            while i < len(self.values):
                result.append(self.value[i] == rhs.value[i])
                i += 1
        return result
   
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for greater than."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: float = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result 
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription notation with get item operator overload."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            i = 0
            result: list = []
            for values in self:
                if rhs[i]:
                    result.append(values)
                i += 1
        return Simpy(result)