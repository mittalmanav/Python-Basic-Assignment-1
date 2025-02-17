# Write a Python script which reads a csv file and Visualizes a table with proper indentations and borders. (make sure to don’t use any table making module or package)	
# Example : CSV file like this
# Name,Age,Department
# Alice,30,HR
# Bob,25,Engineering
# Charlie,35,Marketing
# Diana,28,Sales

import csv
def read_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def print_table(data):

    col_widths = [max(len(row[i]) for row in data) for i in range(len(data[0]))]
    horizontal_border = "+".join("-" * (width + 2) for width in col_widths)
    horizontal_border = f"+{horizontal_border}+"
    print(horizontal_border)
    for i, row in enumerate(data):
        row_text = " | ".join(row[j].ljust(col_widths[j]) for j in range(len(row)))
        print(f"| {row_text} |")
        if i == 0: 
            print(horizontal_border)
    print(horizontal_border)
filename = "/home/manav/Desktop/python/Python-Basic-Assignment-1/data.csv"

data = read_csv(filename)
print_table(data)
