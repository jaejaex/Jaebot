

from webbrowser import get


def writedata(values: list ,filename: str):
    file = open(filename,"a")
    for val in values:
        file.write(str(val) + ',')
    file.write("\n")

writedata([1,1,1,1,1,1,1],"data.csv")