import csv

with open("results.txt", "r") as myfile:
    names = [name for name in myfile.readlines()]

while "\n" in names:
    names.remove("\n")

our_faculty_names = []
with open("info.csv", "r") as mycsv:
    reader = csv.reader(mycsv, delimiter=",")
    for line in reader:
        our_faculty_names.append(line[14])

print(our_faculty_names)