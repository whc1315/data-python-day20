import math
open_file = open("CupcakeInvoices.csv")

for line in open_file:
    print(line)

for line in open_file:
    line = line.strip('\n').split(',')
    print(line[2])

line_total = 0

for line in open_file:
    line = line.strip('\n').split(',')
    line_total = line_total + (float(line[4]) * float(line[3]))
print(round(line_total, 2))

open_file.close()
