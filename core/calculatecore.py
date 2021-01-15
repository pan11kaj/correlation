import plotly.express as px;
import csv;
import numpy as np;
def data_src(src):
    present_days = []
    percent = []
    with open(src) as f:
        read = csv.DictReader(f)
        for row in read:
            present_days.append(float(row["Days Present"]))
            percent.append(float(row["Marks In Percentage"]))
    return{"a":present_days,"b":percent}
def calculatecorr(source):
    correlation = np.corrcoef(source["a"],source["b"])
    print("the student percentage and days present correlation is  ->",+correlation[0,1])

def resultis():
    s = "marks.csv"
    src = data_src(s)
    calculatecorr(src)
resultis()