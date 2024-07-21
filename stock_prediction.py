from __future__ import division
from math import sqrt
import heapq

def printTransactions(money, k, d, names, owned, prices):
    def mean(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        average = mean(nums)
        return sqrt(sum([(x - average) ** 2 for x in nums]) / len(nums))

    def info(price):
        # Simplified and improved info function
        cc = sum(1 for i in range(1, 5) if price[i] > price[i - 1])
        sigma = sd(price)
        mu = mean(price)
        c1, c2, c3 = mean(price[0:3]), mean(price[1:4]), mean(price[2:5])
        
        # Return a metric to decide buying or selling
        return (price[-1] - price[-2]) / price[-2]
    
    res = []
    drop = []
    
    for i in range(k):
        cur_info = info(prices[i])
        if cur_info > 0 and owned[i] > 0:
            res.append((names[i], 'SELL', str(owned[i])))
        elif cur_info < 0:
            heapq.heappush(drop, (cur_info, i, names[i]))
    
    while money > 0.0 and drop:
        rate, idx, n = heapq.heappop(drop)
        amount = int(money / prices[idx][-1])
        if amount > 0:
            res.append((n, 'BUY', str(amount)))
            money -= amount * prices[idx][-1]
    
    print(len(res))
    for r in res:
        print(' '.join(r))
    
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    m, k, d = map(float, data[0].strip().split())
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for i in range(1, k + 1):
        temp = data[i].strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(x) for x in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)
