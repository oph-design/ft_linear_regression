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


def calc_loss(x, y, length, slope) -> float:
    """calculates loss dependent on the variable"""
    prediction = C + M * x
    if slope is False:
        return (2 / length) * sum(prediction - y)
    return (2 / length) * sum(x * (prediction - y))


def train_model(x, y):
    """trains the model with gradient descent"""
    global C, M
    length = len(x)
    for i in range(Iterations):
        loss_c = calc_loss(x, y, length, False)
        loss_m = calc_loss(x, y, length, True)
        if i % 100 == 0:
            print(f"c: {C} loss: {loss_c} m:{M} loss: {loss_m}")
        C = C - L * loss_c
        M = M - L * loss_m


def normed(arr):
    """normes array to 0 1 scale"""
    span = np.max(arr) - np.min(arr)
    return (arr - np.min(arr)) / span


def denorm_coefs(x, y):
    """transforms coefficiants to original scale"""
    global M, C
    spanx = np.max(x) - np.min(x)
    spany = np.max(y) - np.min(y)
    M = spany * M / spanx
    C = np.min(y) + spany * C + M * (1 - np.min(x))


def main():
    """main function"""
    data = pd.read_csv("data.csv")
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]
    train_model(normed(x), normed(y))
    denorm_coefs(x, y)
    plot_data(x, y)


if __name__ == "__main__":
    main()
