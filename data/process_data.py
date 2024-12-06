import pandas as pd
import numpy as np

def process_data(competitor_prices, inventory_levels, demand):
    data = {
        'competitor_prices': competitor_prices,
        'inventory_levels': inventory_levels,
        'demand': demand
    }
    df = pd.DataFrame(data)
    df['avg_competitor_price'] = df['competitor_prices'].mean()
    df['optimal_price'] = df.apply(lambda row: row['avg_competitor_price'] * (1 + (row['demand'] / row['inventory_levels'])), axis=1)
    return df

# Example usage
demand = [100, 150, 200, 250, 300]  # Example demand data
competitor_prices = [19.99, 24.99, 29.99, 34.99, 39.99]  # Example competitor prices
inventory_levels = [50, 40, 30, 20, 10]  # Example inventory levels
df = process_data(competitor_prices, inventory_levels, demand)
print(df)
