import pandas  as pd
import matplotlib.pyplot as plt
import os
# Step 1: Define the file path

file_path = 'C:/Users/user/Downloads/company_sales_data(2).csv'

df = pd.read_csv(file_path)

# Step 3a: Line plot for Total Profit
plt.figure(figsize=(10, 5))
plt.plot(df['month_number'], df['total_profit'], marker='o', color='green')
plt.title('Company Profit per Month')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.grid(True)
plt.xticks(df['month_number'])
plt.tight_layout()
plt.show()

# Step 3b: Subplot for Bathing Soap and Facewash Sales
plt.figure(figsize=(12, 6))

# Subplot 1: Bathing Soap
plt.subplot(2, 1, 1)
plt.plot(df['month_number'], df['bathingsoap'], marker='o', color='blue')
plt.title('Sales of Bathing Soap per Month')
plt.ylabel('Units Sold')
plt.grid(True)

# Subplot 2: Facewash
plt.subplot(2, 1, 2)
plt.plot(df['month_number'], df['facewash'], marker='o', color='orange')
plt.title('Sales of Facewash per Month')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.grid(True)

plt.tight_layout()
plt.show()
