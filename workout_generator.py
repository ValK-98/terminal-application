# Import necessary modules
import workout_database
import random

# Function to get a random exercise from a given list
def get_random_exercise(exercise_list):
    random.shuffle(exercise_list)
    return exercise_list.pop()

# Function to generate a workout plan for the specified number of days
def generate_workout(workout_days):
    # Get the unique body parts from the exercise database
    body_parts = set(exercise["body_part"] for exercise in workout_database.workouts)
    
    # Separate exercises into compound and accessory categories
    compound_exercises = [exercise for exercise in workout_database.workouts if exercise["type"] == "compound"]
    accessory_exercises = [exercise for exercise in workout_database.workouts if exercise["type"] == "accessory"]
    
    # Initialize a set to keep track of used compound exercises and a dictionary to count body parts
    used_compound_exercises = set()
    body_part_counts = {part: 0 for part in body_parts}
    
    # Calculate the number of compound exercises to assign per body part
    even_body_part_count = len(compound_exercises) // len(body_parts)

    # Loop through each workout day
    for day in range(1, workout_days + 1):
        workout_plan = []

        # Generate a workout plan with 4 exercises for the current day if more than 1 day is chosen
        if workout_days > 1:
            while len(workout_plan) < 4:
                if compound_exercises:
                    # Get a random compound exercise
                    compound_exercise = get_random_exercise(compound_exercises)
                    # Check if the exercise hasn't been used and body part count is within the limit
                    if (
                        compound_exercise["name"] not in used_compound_exercises
                        and body_part_counts[compound_exercise["body_part"]] < even_body_part_count
                    ):
                        workout_plan.append(compound_exercise)
                        used_compound_exercises.add(compound_exercise["name"])
                        body_part_counts[compound_exercise["body_part"]] += 1
                else:
                    # If not, add an accessory exercise
                    accessory_exercise = get_random_exercise(accessory_exercises)
                    workout_plan.append(accessory_exercise)
        else:
            # If only 1 day is chosen, include only compound exercises
            while len(workout_plan) < 4:
                if compound_exercises:
                    compound_exercise = get_random_exercise(compound_exercises)
                    workout_plan.append(compound_exercise)

        # Print the workout plan for the current day
        print(f"Day {day}:")
        for exercise in workout_plan:
            print(f"  {exercise['name']} ({exercise['body_part']})")
        print()
