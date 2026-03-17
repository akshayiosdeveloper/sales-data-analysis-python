import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
def load_data(path):
    df = pd.read_csv(path)
    return df

def analyze_data(df):
    total_sales = df["sales"].sum()
    avg_profit = np.mean(df["profit"])
    
    region_sales = df.groupby("region")["sales"].sum()

    return total_sales, avg_profit, region_sales
    
def top_products(df):
    top = df.groupby("product")["sales"].sum().sort_values(ascending=False).head(5)
    return top   
def plot_region_sales(region_sales):
    region_sales.plot(kind="bar")
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.savefig("sales_by_region.png") 
    plt.show()
    
def run_analysis(path):
    df = load_data(path)
    
    total, avg, region = analyze_data(df)

    print("Total Sales:", total)
    print("Average Profit:", avg)
    print("\nSales by Region:\n", region)
    topproducts_info = top_products(df)
    print("Top products:",topproducts_info)
    # plot for region_sales
    plot_region_sales(region)
    # plot for top product
    plot_top_products(topproducts_info)

def plot_top_products(top_products):
    top_products.plot(kind="bar")
    plt.title("Top 5 Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Sales")

    plt.savefig("top_products.png")
    plt.show()    