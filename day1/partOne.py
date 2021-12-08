import pandas as pd

df = pd.read_excel('/home/rachel/AdventOfCode/day1/data.xlsx')

col_one = df['A'].tolist()

i = 0
counter = 0

while i < len(col_one):
    if i == 0:
        i += 1
        continue
    elif col_one[i] > col_one[i-1]:
        i += 1
        counter += 1
    else:
        i += 1

print("part 1: " + counter)





