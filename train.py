import sys
import numpy as np
from utils import load_data
import matplotlib.pyplot as plt


M: float = 0.0
C: float = 0.0
L: float = 0.1


def plot_data(x, y, title, pause):
    """plots the data from the csv"""
    plt.scatter(x, y)
    predict = C + M * x
    plt.plot(x, predict, color="g")
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title(title)
    plt.draw()
    plt.pause(pause)
    plt.clf()


def calc_loss(x, y, length, slope) -> float:
    """calculates loss dependent on the variable"""
    prediction = C + M * x
    if slope is False:
        return (2 / length) * sum(prediction - y)
    return (2 / length) * sum(x * (prediction - y))


def train_model(x, y, iterations):
    """trains the model with gradient descent"""
    global C, M
    length = len(x)
    plot_data(x, y, "Graph at Start", 1)
    for i in range(iterations):
        loss_c = calc_loss(x, y, length, False)
        loss_m = calc_loss(x, y, length, True)
        # print(f"!Update! theta0 = {C} theta1 = {M}")
        plot_data(x, y, f"Graph Progression Epoch:{i}", 0.01)
        C = C - L * loss_c
        M = M - L * loss_m


def normed(arr):
    """norms array to 0 1 scale"""
    span = np.max(arr) - np.min(arr)
    return (arr - np.min(arr)) / span


def denorm_coefs(x, y):
    """transforms coefficiants to original scale"""
    global M, C
    spanx = np.max(x) - np.min(x)
    spany = np.max(y) - np.min(y)
    M = spany * M / spanx
    C = spany * C + M * (1 - np.min(x)) + np.min(y)


def write_result():
    """writes coefficiants to file"""
    file = open("coefs.csv", "w")
    file.write("theta0,theta1\n")
    file.write(f"{C},{M}\n")
    file.close()


def main():
    """main function"""
    plt.ion()
    iterations = 500
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        iterations = int(sys.argv[1])
    data = load_data("data.csv", "km", "price")
    x = np.array(data.get("km"))
    y = np.array(data.get("price"))
    train_model(normed(x), normed(y), iterations)
    denorm_coefs(x, y)
    plot_data(x, y, "Final Result", 3)
    write_result()


if __name__ == "__main__":
    main()
