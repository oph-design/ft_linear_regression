def main():
    """calculate price by mileage"""
    theta0 = 0
    theta1 = 0
    mileage = "zero"
    while mileage.isdigit() is False:
        mileage = input("Please enter the desired mileage as a number: ")
    res = theta0 + int(mileage) * theta1
    print(f"Your calculated price is: {res}$")


if __name__ == "__main__":
    main()
