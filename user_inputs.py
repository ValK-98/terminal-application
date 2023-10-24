# Function to get the user's goal type
def get_goal_type():
    while True:
        goal_type = input("Choose your goal type (muscle gain/strength gain): ").lower()
        if goal_type in ["muscle gain", "strength gain"]:
            return goal_type
        else:
            print("Please choose 'muscle gain' or 'strength gain'.")

# Function to get a valid number of workout days from the user
def get_valid_workout_days():
    while True:
        try:
            workout_days = int(input("Enter the number of workout days (1-5): "))
            if 1 <= workout_days <= 5:
                return workout_days
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer between 1 and 5.")