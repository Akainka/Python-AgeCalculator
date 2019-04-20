# AgeCalculator

# TO DO:
# # SHOW AN ERROR IF AGE IS NEGATIVE


def AgeCalculator():
    while True:
        year = input("Enter a present year: ")
        try:
            year = int(year)
            break
        except ValueError:
            print("Only integers allowed")
    while True:
        birth = input("Enter the year of your birth: ")
        try:
            birth = int(birth)
            break
        except ValueError:
            print("Only integers allowed")
    age = year - birth
    print(f"You are {age} years old.")
AgeCalculator()
