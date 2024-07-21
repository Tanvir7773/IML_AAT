class StockTrader:
    def __init__(self):
        self.money = 100.0
        self.portfolio = {}
        self.price_history = {}

    def read_input(self):
        import sys
        input = sys.stdin.read
        data = input().strip().split('\n')
        
        m, k, d = map(float, data[0].split())
        stocks = []
        
        for i in range(1, int(k) + 1):
            line = data[i].split()
            name = line[0]
            owned = int(line[1])
            prices = list(map(float, line[2:]))
            stocks.append((name, owned, prices))
        
        return m, k, d, stocks

    def decide_transactions(self, m, k, d, stocks):
        transactions = []
        
        for name, owned, prices in stocks:
            if name not in self.price_history:
                self.price_history[name] = prices
            else:
                self.price_history[name] = self.price_history[name][1:] + [prices[-1]]
            
            sma = sum(prices) / len(prices)
            current_price = prices[-1]
            
            if current_price < sma and self.money >= current_price:
                shares_to_buy = int(self.money // current_price)
                self.money -= shares_to_buy * current_price
                self.portfolio[name] = self.portfolio.get(name, 0) + shares_to_buy
                transactions.append((name, "BUY", shares_to_buy))
            elif current_price > sma and owned > 0:
                self.money += owned * current_price
                transactions.append((name, "SELL", owned))
                self.portfolio[name] = 0

        return transactions

    def play_turn(self):
        m, k, d, stocks = self.read_input()
        transactions = self.decide_transactions(m, k, d, stocks)
        
        print(len(transactions))
        for t in transactions:
            print(t[0], t[1], t[2])

if __name__ == "__main__":
    trader = StockTrader()
    trader.play_turn()
