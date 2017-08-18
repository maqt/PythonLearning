import csv

with open('test.csv', newline='') as f:
    content = f.read()
    for line in content[0]:
        print(line, end='')
