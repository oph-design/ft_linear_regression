import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """calculates theta0 and theta1"""
    data = pd.read_csv("data.csv")
    print(data.describe())
    x = np.array(data.get("km"))
    y = np.array(data.get("price"))
    plt.scatter(x, y)
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title("price / mileage")
    plt.show()


if __name__ == "__main__":
    main()
