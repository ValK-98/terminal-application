import workout_generator
import user_inputs

# Get the user's goal type ("muscle gain" or "strength gain")
goal_type = user_inputs.get_goal_type()

# Get the number of workout days from the user
workout_days = user_inputs.get_valid_workout_days()

# Generate and display the workout plan
workout_generator.generate_workout(workout_days, goal_type)
