import numpy as np
from utils import load_data
import matplotlib.pyplot as plt


def plot_data(x, y, predict, r):
    """plots the data from the csv"""
    plt.scatter(x, y)
    plt.plot(x, predict, color="g")
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title("Regression Graph")
    plt.suptitle(f"R Squared value for this Model: {r}")
    plt.show()


def main():
    """calculates R squared"""
    data = load_data("data.csv", "km", "price")
    x = np.array(data.get("km"))
    y = np.array(data.get("price"))
    coefs = load_data("coefs.csv", "theta0", "theta1")
    C = float(coefs.at[0, "theta0"])
    M = float(coefs.at[0, "theta1"])
    predictions = C + M * x
    SSres = sum(np.power(y - predictions, 2))
    SStot = sum(np.power(y - np.mean(y), 2))
    r = 1 - (SSres / SStot)
    plot_data(x, y, predictions, r)
    print(f"The R Squared is: {r}")


if __name__ == "__main__":
    main()
