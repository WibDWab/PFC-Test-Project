### Elite Hacker Code####
import constants
import csv

def getEGirls():
    with open('egirls.csv', mode='r') as egirlsCsv:
        csvReader = csv.reader(egirlsCsv)
        egirls = [{"name": row[0], "fucked": int(row[1])} for row in csvReader]
    return egirls

egirlList = getEGirls()

for girl in egirlList:
    if girl["fucked"] == 1:
        print(f"{girl['name']}? Yeah I fucked her.")

print(f"{constants.GUY_WHO_FUCKS_MEN} is gay.")
