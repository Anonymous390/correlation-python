import plotly.express as px
import csv
import numpy as np

def display_data(path):
    with open(path) as f:
        csv_reader = csv.DictReader(f)
        fig = px.scatter(csv_reader, x="Days Present", y="Marks In Percentage")
    fig.show()

def get_data_source(data_path):
    temp = []
    ice = []

    with open(data_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            temp.append(float(i["Days Present"]))
            ice.append(float(i["Marks In Percentage"]))
        return {"x": temp, "y": ice}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(f"The correlation between the data set is {correlation[0][1]} {correlation[1][0]}")

def main():
    data_path = "student.csv"
    display_data(data_path)
    data_source = get_data_source(data_path)
    findCorrelation(data_source)

main()