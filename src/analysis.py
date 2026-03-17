import pandas as pd
import numpy as np
#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
def load_data(path):
    df = pd.read_csv(path)
    return df

def analyze_data(df):
    total_sales = df["sales"].sum()
    avg_profit = np.mean(df["profit"])
    
    region_sales = df.groupby("region")["sales"].sum()

    return total_sales, avg_profit, region_sales
    
    
def plot_region_sales(region_sales):
    region_sales.plot(kind="bar")
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.show()
    
def run_analysis(path):
    df = load_data(path)
    
    total, avg, region = analyze_data(df)

    print("Total Sales:", total)
    print("Average Profit:", avg)
    print("\nSales by Region:\n", region)

    plot_region_sales(region)