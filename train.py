from enum import Enum
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

m: float = 0.0
c: float = 0.0
L: float = 0.0001


def plot_data(data: pd.DataFrame):
    """plots the data from the csv"""
    x = np.array(data.get("km"))
    y = np.array(data.get("price"))
    plt.scatter(x, y)
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title("price per mileage")
    plt.show()


def predict_price(mileage: float) -> float:
    """predict function for the price"""
    return c + m * mileage


def calc_error(mileage: float, price: float, var: bool) -> float:
    """calculates single error based on the varibale"""
    if var is True:
        return mileage * (price - predict_price(mileage))
    return price - predict_price(mileage)


def calc_loss(data: pd.DataFrame, var: bool) -> float:
    """calculates loss dependent on the variable"""
    sum: float = 0.0
    for index, row in data.iterrows():
        sum += calc_error(float(row["km"]), float(row["price"]), var)
    return -2 * float(len(data)) * sum


def train_model(data: pd.DataFrame):
    """trains the model with gradient descent"""
    loss_c = calc_loss(data, False)
    loss_m = calc_loss(data, True)
    for i in range(1000):
        global c, m
        c -= L * loss_c
        m -= L * loss_m
        loss_m = calc_loss(data, False)
        loss_c = calc_loss(data, True)
        print(f"c: {c} loss: {loss_c} m:{m} loss: {loss_m}")
        time.sleep(1)


def main():
    """main function"""
    data = pd.read_csv("data.csv")
    print(len(data))
    # print(data.describe())
    # plot_data(data)
    train_model(data)
    print(f"final formular: price = {c} + {m} * mileage")


if __name__ == "__main__":
    main()
