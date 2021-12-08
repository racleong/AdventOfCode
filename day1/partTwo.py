import pandas as pd

df = pd.read_excel('/home/rachel/AdventOfCode/day1/data.xlsx')
col_one = df['A'].tolist()

def slidingWindow(col_one, k, counter):
    n = len(col_one)

    #Checks array is greater than sliding window
    if n < k:
        print("invalid")
        return -1

    #calculate sum of first window of size k
    window_sumA = sum(col_one[:k])

    #calculate sum of remaining windows
    #remove first element of previous window and add
    #last element of current window
    #window B then becomes window A
    for i in range(n - k):
        window_sumB = window_sumA - col_one[i] + col_one[i+k]
        if window_sumB > window_sumA:
            counter += 1
            window_sumA = window_sumB
        else:
            window_sumA = window_sumB
            continue
    return counter

print(slidingWindow(col_one,3,0))


