import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Load and clean the data
trades = pd.read_csv( '/home/poppie/Documents/25_kot/01_01_2007-29_04_2025.csv', low_memory=False)
trades['opening_time_utc'] = pd.to_datetime(trades['opening_time_utc'], errors='coerce')
trades['closing_time_utc'] = pd.to_datetime(trades['closing_time_utc'], errors='coerce')
trades['profit_usd'] = pd.to_numeric(trades['profit_usd'], errors='coerce')

# Drop rows with missing critical data
trades = trades.dropna(subset=['opening_time_utc', 'closing_time_utc', 'profit_usd', 'type', 'symbol'])

# Extract time-based features
trades['open_hour'] = trades['opening_time_utc'].dt.hour
trades['open_day'] = trades['opening_time_utc'].dt.dayofweek  # 0 = Monday, 6 = Sunday
trades['close_hour'] = trades['closing_time_utc'].dt.hour
trades['close_day'] = trades['closing_time_utc'].dt.dayofweek

# Calculate key metrics
total_trades = len(trades)
total_profit = trades['profit_usd'].sum()
avg_profit_per_trade = trades['profit_usd'].mean()
winning_trades = len(trades[trades['profit_usd'] > 0])
losing_trades = len(trades[trades['profit_usd'] < 0])
win_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0
max_profit = trades['profit_usd'].max()
max_loss = trades['profit_usd'].min()

# Print summary report
print(f"Trade History Analysis Report")
print(f"----------------------------")
print(f"Total Trades: {total_trades}")
print(f"Total Profit (USD): {total_profit:.2f}")
print(f"Average Profit per Trade (USD): {avg_profit_per_trade:.2f}")
print(f"Winning Trades: {winning_trades} ({win_rate:.2f}%)")
print(f"Losing Trades: {losing_trades}")
print(f"Maximum Profit (USD): {max_profit:.2f}")
print(f"Maximum Loss (USD): {max_loss:.2f}")

# Most Profitable Time to Open Trades (Hourly)
profit_by_open_hour = trades.groupby('open_hour')['profit_usd'].mean().reset_index()
most_profitable_open_hour = profit_by_open_hour.loc[profit_by_open_hour['profit_usd'].idxmax()]['open_hour']
print(f"Most Profitable Hour to Open Trades (UTC): {int(most_profitable_open_hour)} (Avg Profit: {profit_by_open_hour['profit_usd'].max():.2f} USD)")

# Worst Time to Open Trades (Leading to Losses, Hourly)
loss_by_open_hour = trades[trades['profit_usd'] < 0].groupby('open_hour')['profit_usd'].mean().reset_index()
worst_open_hour = loss_by_open_hour.loc[loss_by_open_hour['profit_usd'].idxmin()]['open_hour'] if not loss_by_open_hour.empty else None
if worst_open_hour is not None:
    print(f"Worst Hour to Open Trades (UTC, Leading to Losses): {int(worst_open_hour)} (Avg Loss: {loss_by_open_hour['profit_usd'].min():.2f} USD)")

# Most Profitable Time to Close Trades (Hourly)
profit_by_close_hour = trades.groupby('close_hour')['profit_usd'].mean().reset_index()
most_profitable_close_hour = profit_by_close_hour.loc[profit_by_close_hour['profit_usd'].idxmax()]['close_hour']
print(f"Most Profitable Hour to Close Trades (UTC): {int(most_profitable_close_hour)} (Avg Profit: {profit_by_close_hour['profit_usd'].max():.2f} USD)")

# Worst Time to Close Trades (Leading to Losses, Hourly)
loss_by_close_hour = trades[trades['profit_usd'] < 0].groupby('close_hour')['profit_usd'].mean().reset_index()
worst_close_hour = loss_by_close_hour.loc[loss_by_close_hour['profit_usd'].idxmin()]['close_hour'] if not loss_by_close_hour.empty else None
if worst_close_hour is not None:
    print(f"Worst Hour to Close Trades (UTC, Leading to Losses): {int(worst_close_hour)} (Avg Loss: {loss_by_close_hour['profit_usd'].min():.2f} USD)")

# Visualize data silently (save plots, no print statements)
plt.figure(figsize=(10, 5))
sns.barplot(x='open_hour', y='profit_usd', data=profit_by_open_hour, color='green')
plt.xlabel('Opening Hour (UTC)')
plt.ylabel('Average Profit (USD)')
plt.title('Average Profit by Opening Hour')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('profit_by_open_hour.png')
plt.close()

plt.figure(figsize=(10, 5))
if not loss_by_open_hour.empty:
    sns.barplot(x='open_hour', y='profit_usd', data=loss_by_open_hour, color='red')
    plt.xlabel('Opening Hour (UTC)')
    plt.ylabel('Average Loss (USD)')
    plt.title('Average Loss by Opening Hour')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('loss_by_open_hour.png')
plt.close()

plt.figure(figsize=(10, 5))
sns.barplot(x='close_hour', y='profit_usd', data=profit_by_close_hour, color='green')
plt.xlabel('Closing Hour (UTC)')
plt.ylabel('Average Profit (USD)')
plt.title('Average Profit by Closing Hour')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('profit_by_close_hour.png')
plt.close()

plt.figure(figsize=(10, 5))
if not loss_by_close_hour.empty:
    sns.barplot(x='close_hour', y='profit_usd', data=loss_by_close_hour, color='red')
    plt.xlabel('Closing Hour (UTC)')
    plt.ylabel('Average Loss (USD)')
    plt.title('Average Loss by Closing Hour')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('loss_by_close_hour.png')
plt.close()

trades['type'] = trades['type'].astype('category')
valid_data = trades.dropna(subset=['type', 'profit_usd'])
if not valid_data.empty:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='type', y='profit_usd', data=valid_data)
    plt.xlabel('Trade Type')
    plt.ylabel('Profit/Loss (USD)')
    plt.title('Profit Distribution by Trade Type')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    plt.savefig('profit_by_trade_type.png')
plt.close()

valid_data = trades.dropna(subset=['opening_time_utc', 'profit_usd'])
if not valid_data.empty:
    plt.figure(figsize=(10, 5))
    plt.scatter(valid_data['opening_time_utc'], valid_data['profit_usd'], alpha=0.5, color='blue')
    plt.xlabel('Opening Time (UTC)')
    plt.ylabel('Profit/Loss (USD)')
    plt.title('Profit/Loss vs. Opening Time')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    plt.savefig('profit_vs_opening_time.png')
plt.close()

print("Visualization plots have been saved as PNG files in the current directory.")
