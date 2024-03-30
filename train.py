from enum import Enum
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

M: float = 0.0
C: float = 0.0
L: float = 0.0001
Iterations: int = 1000


def plot_data(x, y):
    """plots the data from the csv"""
    plt.scatter(x, y)
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title("price per mileage")
    plt.show()


def calc_loss(x, y, var) -> float:
    """calculates loss dependent on the variable"""
    sum: float = 0.0
    for i in x:
        predicted_price = C + M * x[i]
        error = y[i] - predicted_price
        if var is True:
            error *= y[i]
        sum += error
    return (-2 / len(x)) * sum


def train_model(x, y):
    """trains the model with gradient descent"""
    for i in range(Iterations):
        global C, M
        loss_m = calc_loss(x, y, True)
        loss_c = calc_loss(x, y, False)
        C -= L * loss_c
        M -= L * loss_m
        print(f"c: {C} loss: {loss_c} m:{M} loss: {loss_m}")
        time.sleep(1)


def main():
    """main function"""
    data = pd.read_csv("data.csv")
    x = np.array(data.get("km"))
    y = np.array(data.get("price"))
    # plot_data(x, y)
    train_model(x, y)
    print(f"final formular: price = {C} + {M} * mileage")


if __name__ == "__main__":
    main()
