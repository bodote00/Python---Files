import csv
import pathlib
from data.index import Index
from data.series import Series

class DataFrame:
    """Class that represents table of data."""

    def __init__(self, values, columns=None):
        """Creates object that represents data table, which contains columns (or at least one column). Each column must be indexed by instance of Index.
            Taken arguments are: "values", which is instances list of Series (representing columns), and (optional) "Columns", which is Index, thet indexes columns.
            ValueError are raised if "values" and "index" are not the same length, or if "values" does not contain at least 1 element."""

        if not values:
            raise ValueError("Values list must cointain at least 1 element.")

        if columns is None:
            columns = Index(range(len(values)))
        elif columns and len(values) != len(columns.labels):
            raise ValueError(f"Values must have same length as index. Values of length: {len(values)} and index of length: {len(columns.labels)} were given, and are NOT the same length.")

        self.values = values
        self.columns = columns

    def __len__(self):
        return len(self.columns)

    def __repr__(self):
        return f"DataFrame{repr(self.shape)}"

    def __str__(self):
        return self.__repr__()
    
    def __iter__(self):
        yield from self.columns
    
    @property
    def shape(self):
        """Calculates shape of DataFrame object, and also returns tuple, that represents DataFrame object shape."""

        return (len(self.values[0]), len(self.columns))


    @classmethod
    def from_csv(self, input_file, separator=","):
        """Creates class Dataframe from csv string. Takes string (DataFrame), which have to be made out of (optional) separator. Default value of separator is set to ",". Returns new DataFrame made from csv string."""

        if not isinstance(input_file, pathlib.Path):
            raise ValueError(f"Input_string is not an instance of pathlib.Path")


        with input_file.open("r") as file:
            csv_reader = list(csv.reader(file, delimiter=separator))

        _list = list(zip(*csv_reader[1:]))

        values = [Series(value, Index([iter for iter in _list[0]])) for value in _list[1:]]

        return self(values, Index(csv_reader[0][1:]))
        
    
    def items(self):
        """Supports iteration through couples(key, value). Returns zip iterator."""
        return zip(self.columns, self.values)

    def index(self):
        """Returns the first "Series" instance in DataFrame.values"""
        return self.values[0].index

    def get(self, key):
        """If DataFrame.columns does not contain given key, None is returned. If does, corresponding column (type Series) is returned."""

        try:
            return self.values[self.columns.get_loc(key)]
        except KeyError as error:
            return None