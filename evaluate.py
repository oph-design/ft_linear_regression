import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path


def plot_data(x, y, predict):
    """plots the data from the csv"""
    plt.scatter(x, y)
    plt.plot(x, predict, color="g")
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title("Regression Graph")
    plt.show()


def main():
    """calculate price by mileage"""
    C = 0
    M = 0
    data = pd.read_csv("data.csv")
    if os.path.isfile("coefs.csv"):
        coefs = pd.read_csv("coefs.csv")
        C = float(coefs.at[0, "theta0"])
        M = float(coefs.at[0, "theta1"])
    x = np.array(data.get("km"))
    y = np.array(data.get("price"))
    predictions = C + M * x
    SSres = sum(np.power(y - predictions, 2))
    SStot = sum(np.power(y - np.mean(y), 2))
    r = 1 - (SSres / SStot)
    plot_data(x, y, predictions)
    print(f"The R Squared is: {r}")


if __name__ == "__main__":
    main()
