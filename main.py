#from src.analysis import load_data, analyze_data, plot_region_sales

# df = load_data("data/sales_data.csv")

# total, avg, region = analyze_data(df)

# print("Total Sales:", total)
# print("Average Profit:", avg)
# print("\nSales by Region:\n", region)
# plot_region_sales(region)

from src.analysis import run_analysis

if __name__ == "__main__":
    run_analysis("data/sales_data.csv")