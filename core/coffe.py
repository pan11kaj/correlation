import csv;
import numpy as np;

def get_data():
    sleep_time = []
    take_coffe = []
    with open("coffeee.csv") as f:
        read_data = csv.DictReader(f)
        for rows in read_data:
            sleep_time.append(float(rows['Coffee in ml']))
            take_coffe.append(float(rows["s"]))
    return{"p":sleep_time,"q":take_coffe}
def calculate(src):
    correlation = np.corrcoef(src["p"],src["q"])
    print("coffe and sleeping correlation is ->",correlation[0,1])
def finalresult():
    source = get_data()
    calculate(source)
finalresult()