from utils import load_data


def main():
    """calculate price by mileage"""
    mileage = "zero"
    data = load_data("coefs.csv", "theta0", "theta1")
    C = float(data.at[0, "theta0"])
    M = float(data.at[0, "theta1"])
    while mileage.isdigit() is False:
        mileage = input("Please enter the desired mileage as a number: ")
    res = C + float(mileage) * M
    print(f"Your calculated price is: {res}")


if __name__ == "__main__":
    main()
