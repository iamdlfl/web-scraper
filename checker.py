import csv

with open("results.txt", "r") as myfile:
    names = [name.split(',')[0] for name in myfile.readlines() if name != "\n"]

while "\n" in names:
    names.remove("\n")

our_faculty_names = []
with open("info.csv", "r") as mycsv:
    reader = csv.reader(mycsv, delimiter=",")
    for line in reader:
        our_faculty_names.append(line[14])

our_faculty_names.pop(0)

for name in our_faculty_names:
    last, first = name.split(',')
    last = last.strip()
    first = first.strip()
    if last.strip() in str(names):
        print(f'Found {last}, {first}')