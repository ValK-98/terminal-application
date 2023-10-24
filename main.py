import workout_generator


# Get the number of workout days from the user

workout_days = workout_generator.get_valid_workout_days()

# Generate and display the workout plan

workout_generator.generate_workout(workout_days)