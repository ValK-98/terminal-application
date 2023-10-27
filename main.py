from workout_generator import WorkoutGenerator
from workout_displayer import WorkoutDisplayer
import user_inputs


def main():
    try:
        # Get the user's goal type ("muscle gain" or "strength gain")
        goal_type = user_inputs.get_goal_type()

        # Get the number of workout days from the user
        workout_days = user_inputs.get_valid_workout_days()

        # Create an instance of WorkoutGenerator
        generator = WorkoutGenerator()
        workout_schedule = generator.generate_workout(workout_days, goal_type)

        # Display and give option to modify the workout plan
        displayer = WorkoutDisplayer()
        displayer.modify_workout_plan(workout_schedule)

        # Uncomment the line below if you want to print the workout_schedule
        # print(workout_schedule)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
