from workout_generator import WorkoutGenerator
from workout_generator import WorkoutDisplayer
import user_inputs


try:
    # Get the user's goal type ("muscle gain" or "strength gain")
    goal_type = user_inputs.get_goal_type()

    # Get the number of workout days from the user
    workout_days = user_inputs.get_valid_workout_days()

    # Create an instance of WorkoutGenerator
    generator = WorkoutGenerator()
    workout_schedule = generator.generate_workout(workout_days, goal_type)

    #Display the workout plan
    displayer = WorkoutDisplayer()
    displayer.display_workout_schedule(workout_schedule)


    # print(workout_schedule)

except Exception as e:
    print(f"An error occurred: {e}")
