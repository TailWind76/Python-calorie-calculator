def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

def calculate_daily_calories(bmr, activity_level):
    activity_factors = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    return bmr * activity_factors[activity_level]

def main():
    print("Welcome to the Advanced Calorie Calculator!")
    while True:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))
        age = int(input("Enter your age in years: "))
        gender = input("Enter your gender (male/female): ").lower()
        activity_level = input("Enter your activity level "
                               "(sedentary/lightly active/moderately active/very active/extra active): ").lower()
        goal = input("Enter your goal (lose weight/gain weight/maintain weight): ").lower()

        bmr = calculate_bmr(weight, height, age, gender)
        daily_calories = calculate_daily_calories(bmr, activity_level)

        if goal == 'lose weight':
            daily_calories -= 500
        elif goal == 'gain weight':
            daily_calories += 500

        print(f"\nYour daily calorie intake should be approximately {daily_calories:.2f} calories.\n")

        choice = input("Do you want to calculate again? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("Thank you for using the Advanced Calorie Calculator!")

if __name__ == "__main__":
    main()
