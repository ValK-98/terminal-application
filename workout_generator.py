import workout_database
import random


def WorkoutGenerator(workout_days):
    for session in range(workout_days):
        # Shuffle the workouts list to randomize exercise selection for each session
        random.shuffle(workout_database.workouts)

        workout_plan = []
        body_parts_in_session = set()

        while len(workout_plan) < 4:
            for workout in workout_database.workouts:
                body_part = workout["body_part"]
                if body_part not in body_parts_in_session:
                    workout_plan.append(workout)
                    body_parts_in_session.add(body_part)

                if len(workout_plan) == 4:
                    break  # Exit the inner loop if we have 4 exercises

        print(f"Session {session + 1}:")
        for exercise in workout_plan:
            print(f"  {exercise['name']} ({exercise['body_part']})")
        print()

        # Decrease the remaining workout days
        workout_days -= 1

        if workout_days == 0:
            break
