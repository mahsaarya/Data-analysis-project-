import yfinance as yf
import pandas as pd

# دانلود داده‌ها
data = yf.download("BTC-USD", start="2014-01-01", end="2022-12-31", interval="1d")

# استخراج روزهای هفته
data['weekday'] = data.index.weekday

# داده‌های دوشنبه و چهارشنبه
mondays = data[data['weekday'] == 0]
wednesdays = data[data['weekday'] == 2]

# نمایش تعداد روزهای دوشنبه و چهارشنبه
print(f"تعداد روزهای دوشنبه: {len(mondays)}")
print(f"تعداد روزهای چهارشنبه: {len(wednesdays)}")

# ترکیب داده‌ها
transactions = pd.merge(
    mondays[['Open']],
    wednesdays[['Close']],
    left_index=True,
    right_index=True,
    suffixes=['_buy', '_sell']
)

# نمایش تعداد معاملات و چند ردیف از داده‌ها
print(f"تعداد معاملات ممکن: {len(transactions)}")
print(transactions.head())