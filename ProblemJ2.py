# The first line of input contains a positive integer N, where 1 ≤ N ≤ 100, representing the
# number of bids collected at the silent auction. Each of the next N pairs of lines contains a
# person’s name on one line, and the amount of their bid, in dollars, on the next line. Each
# bid is a positive integer less than 2000. The order of the input is the order in which bids
# were placed.

N = int(input())


#First bid + setting as max
name = input()
bid = int(input())
maxName = name
maxBid = bid

for x in range(0,N - 1):
    name = input()
    bid = int(input())
    if bid > maxBid:
        maxBid = bid
        maxName = name

print(maxName)


