def get_goal_type():
    """Prompt the user to choose a goal type and return the chosen goal."""
    while True:
        goal_type = input(
            "Choose your goal type (muscle gain/strength gain) or type 'exit' to quit: "
        ).lower()

        if goal_type in ["muscle gain", "strength gain"]:
            return goal_type
        elif goal_type == "exit":
            print("Exiting the program. Goodbye!")
            exit(0)
        else:
            print("Please choose 'muscle gain' or 'strength gain'.")


def get_valid_workout_days():
    """Prompt the user to specify the number of workout days and return the chosen number."""
    while True:
        response = input(
            "Enter the number of workout days (1-5) or type 'exit' to quit: "
        )

        if response == "exit":
            print("Exiting the program. Goodbye!")
            exit(0)
        try:
            workout_days = int(response)
            if 1 <= workout_days <= 5:
                return workout_days
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer between 1 and 5.")
