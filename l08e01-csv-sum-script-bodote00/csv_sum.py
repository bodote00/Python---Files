import pathlib
import csv

loaded_csv = pathlib.Path.cwd().joinpath("data").glob("*/*.csv")

summation_of_values_on_line = 0

for file in loaded_csv:
    with file.open("r") as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            line = [int(value) for value in line]
            summation_of_values_on_line += sum(line)
print(summation_of_values_on_line)
