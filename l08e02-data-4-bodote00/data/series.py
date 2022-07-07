import csv
import operator
import pathlib
from data.index import Index

class Series:
    """Class Series contains sequence of values indexed by an instance of Index class."""

    def __init__(self, values, index=None):
        """Creates instance of Series class -> (Constructor). Taken arguments: "values", which is list of values (in sequence), and "index" (optional), which is an index, by that sequence is indexed.
            If "values" is an empty list, or if values length does not equal length of labels of given index, ValueError is raised.""" 

        if not values:
            raise ValueError(f"List of values must contain at least 1 value.")

        if not index:
            index = Index(range(len(values)))

        if index and len(values) != len(index.labels):
            raise ValueError(f"Values must have same length as labels of index. Values of length: {len(values)} and index.labels of length: {len(index.labels)} were given.")
        
        self.values = values
        self.index = index

    def __len__(self):
        return len(self.values)

    def __repr__(self):
        repr = [f"{key}\t{val}" for key, val in zip(self.index.labels, self.values)]
        return "\n".join(repr)

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return self._apply_operator(other, operator.add)

    def __sub__(self, other):
        return self._apply_operator(other, operator.sub)

    def __mul__(self, other):
        return self._apply_operator(other, operator.mul)

    def __mod__(self, other):
        return self._apply_operator(other, operator.mod)

    def __truediv__(self, other):
        return self._apply_operator(other, operator.truediv)

    def __floordiv__(self, other):
        return self._apply_operator(other, operator.floordiv)

    def __pow__(self, other):
        return self._apply_operator(other, operator.pow)

    def __round__(self, percision):
        def _round(val):
            return round(val, percision)
        return self.apply(_round)

    def __iter__(self):
        yield from self.values

    def __getitem__(self, key):
        try:
            return self.values[self.index.get_loc(key)]
        except ValueError as error:
            raise KeyError(f"Key {key} does not exist in class Series.")

    @classmethod
    def from_csv(cls, input_text, separator=","):
        """Creates Series class from csv string."""

        if not isinstance(input_text, pathlib.Path):
            raise ValueError(f"Input_string is not an instance of pathlib.Path")
        
        with input_text.open("r") as file:
            csv_reader = list(csv.reader(file, delimiter=separator))

        return cls(Series(csv_reader[1]), Index(csv_reader[0]))

    @property
    def shape(self):
        """Calculates shape of Series object, and returns tuple, that represents shape of Series object."""

        return (len(self), )

    def _apply_operator(self, other, operator):
        """New Series object with modified values list, which is based on given operator."""

        if not isinstance(other, Series):
            return NotImplemented

        modified_list = []
        for value_1, value_2 in zip(self.values, other.values):
            modified_list.append(operator(value_1, value_2))
        
        return Series(modified_list, index=self.index)

    def get(self, key):
        """Checks if Series.index contains defined key, if contains, corresponding value from values is returned. If does not, None is returned."""

        try:
            return self.values[self.index.get_loc(key)]
        except KeyError as error:
            return None

    def sum(self):
        """Does sum of all values in Series.values. Returns summation of all the values in Series.values."""

        return sum(self.values)

    def max(self):
        """Finds max value in Series.values, and also returns it."""

        return max(self.values)

    def min(self):
        """Finds min value in Series.values, and also returns it."""

        return min(self.values)

    def mean(self):
        """Computes arithmetic mean of values in Series.values, and also returns them."""

        return sum(self.values) / len(self.values)

    def apply(self, func):
        """Creates new Series object with values, which are made by applying given function on every single value in the original Series.values. 
        Index of created Series instance is same as the original.
        Returns new Series object that has modified values."""

        modified_list = []
        for value in self.values:
            modified_list.append(func(value))

        return Series(modified_list, index=self.index)

    def abs(self):
        """Creates new Series object with values. That values are absolute values of the original values. 
        Index of created Series instance is the same as the original one.
        New Series object (with modified values) is returned here."""

        return self.apply(abs)

    def items(self):
        """Supports iteration through couples(key, value). Returns zip iterator."""
        return zip(self.index.labels, self.values)