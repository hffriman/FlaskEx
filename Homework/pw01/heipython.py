# Source: "Python Web Service from Idea to Production" by Tero Karvinen

# Help for Round function:
# --> https://www.tutorialspoint.com/How-to-round-down-to-round-down-to-2-decimals-a-float-using-Python

# Help for calculating BMI:
# --> https://www.foreverclub.fi/mita-painoindeksi-paljastaa


import sys

name = sys.argv[1]
weight = int(sys.argv[2])
height = int(sys.argv[3])
bmi = round((weight / (height * height) * 10000),2)

print(f"Hi {name}, your BMI is {bmi}")
