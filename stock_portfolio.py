# Stock Portfolio Tracker - Task 2

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")

# Take input from user
n = int(input("Enter number of stocks you want to add: "))

for i in range(n):
    stock_name = input("Enter stock name (e.g., AAPL): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("❌ Stock not found in price list!")

# Calculate total investment
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Save to file
choice = input("Do you want to save result? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock}: {quantity} × {price} = {investment}\n")
        file.write(f"\nTotal Investment: {total_investment}")
    
    print("✅ Data saved to portfolio.txt")