import workout_generator
import user_inputs


# Get the number of workout days from the user

workout_days = user_inputs.get_valid_workout_days()

# Generate and display the workout plan

workout_generator.generate_workout(workout_days)