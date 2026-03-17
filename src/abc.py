if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("../data/sales_data.csv")

    region_sales = df.groupby("region")["sales"].sum()

    region_sales.plot(kind="bar")

    import matplotlib.pyplot as plt
    plt.show()