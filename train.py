import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

M: float = 0.0
C: float = 0.0
L: float = 0.1
Iterations: int = 1000


def plot_data(x, y):
    """plots the data from the csv"""
    plt.scatter(x, y)
    predict = C + M * x
    plt.plot(x, predict, color="g")
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title("price per mileage")
    plt.show()


def calc_loss(x, y, length, var) -> float:
    """calculates loss dependent on the variable"""
    sum: float = 0.0
    for i in range(length):
        predicted_price = C + M * x[i]
        error = predicted_price - y[i]
        if var is True:
            error = error * x[i]
        sum = sum + error
    return (2 / length) * sum


def train_model(x, y):
    """trains the model with gradient descent"""
    length = len(x)
    for i in range(Iterations):
        global C, M
        loss_c = calc_loss(x, y, length, False)
        loss_m = calc_loss(x, y, length, True)
        if i % 100 == 0:
            print(f"c: {C} loss: {loss_c} m:{M} loss: {loss_m}")
        C = C - L * loss_c
        M = M - L * loss_m


def norm_data(arr):
    span = np.max(arr) - np.min(arr)
    return (arr - np.min(arr)) / span


def main():
    """main function"""
    data = pd.read_csv("data.csv")
    x = norm_data(data.iloc[:, 0])
    y = norm_data(data.iloc[:, 1])
    train_model(x, y)
    plot_data(x, y)
    print(f"final formular: price = {C} + {M} * mileage")


if __name__ == "__main__":
    main()
