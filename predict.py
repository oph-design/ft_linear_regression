import pandas as pd
import os.path


def main():
    """calculate price by mileage"""
    C = 0
    M = 0
    mileage = "zero"
    if os.path.isfile("coefs.csv"):
        data = pd.read_csv("coefs.csv")
        C = float(data.at[0, 'theta0'])
        M = float(data.at[0, 'theta1'])
    while mileage.isdigit() is False:
        mileage = input("Please enter the desired mileage as a number: ")
    res = C + float(mileage) * M 
    print(f"Your calculated price is: {res}")


if __name__ == "__main__":
    main()
