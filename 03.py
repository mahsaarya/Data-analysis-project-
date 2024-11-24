import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

initial_capital = 1000
capital = initial_capital

data = yf.download("BTC-USD", start="2014-01-01", end="2022-12-31", interval="1d")

data["weekday"] = data.index.weekday

mondays = data[data["weekday"] == 0]
wednesdays = data[data["weekday"] == 2]

transactions = pd.merge(
    mondays[["Open"]],
    wednesdays[["Close"]],
    left_index=True,
    right_index=True,
    suffixes=["_buy", "_sell"]
)

capital_history = []

for index, row in transactions.iterrows():
    capital_history.append(capital)

    btc_bought = capital / row["Open_buy"]

    capital = btc_bought * row["Close_sell"]

capital_history.append(capital)

profit_or_loss = capital - initial_capital

print(f"سرمایه نهایی: {capital:.2f} دلار")
if profit_or_loss > 0:
    print(f"شما سود کردید: {profit_or_loss:.2f} دلار")
else:
    print(f"شما ضرر کردید: {profit_or_loss:.2f} دلار")

plt.figure(figsize=(10, 6))
plt.plot(capital_history, marker="o", linestyle="-", color="blue", label="Capital over Time")
plt.axhline(y=initial_capital, color="red", linestyle="--", label="Initial Capital")
plt.title("Investment Capital Over Time", fontsize=16)
plt.xlabel("Transaction Index", fontsize=12)
plt.ylabel("Capital (USD)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
