import workout_database
import random
from sets_reps_generator import SetsRepsGenerator

class WorkoutGenerator:
    def __init__(self):
        self.body_parts = set(exercise["body_part"] for exercise in workout_database.workouts)
        self.compound_exercises = [exercise for exercise in workout_database.workouts if exercise["type"] == "compound"]
        self.accessory_exercises = [exercise for exercise in workout_database.workouts if exercise["type"] == "accessory"]

    def get_random_exercise(self, exercise_list):
        random.shuffle(exercise_list)
        return exercise_list.pop() if exercise_list else None

    def generate_workout(self, workout_days, goal_type):
        used_compound_exercises = set()
        body_part_counts = {part: 0 for part in self.body_parts}
        even_body_part_count = len(self.compound_exercises) // len(self.body_parts)
        self.sets_reps_generator = SetsRepsGenerator(goal_type)

        for day in range(1, workout_days + 1):
            self.print_workout_plan(day, workout_days, used_compound_exercises, body_part_counts, even_body_part_count)

    def print_workout_plan(self, day, workout_days, used_compound_exercises, body_part_counts, even_body_part_count):
        workout_plan = []
        compound_exercises_copy = self.compound_exercises.copy()
        accessory_exercises_copy = self.accessory_exercises.copy()

        # Ensure only one compound exercise is added per day for 2-5 day workouts
        if workout_days > 1:
            compound_exercise = self.get_random_exercise(compound_exercises_copy)
            if (compound_exercise and compound_exercise["name"] not in used_compound_exercises
                and body_part_counts[compound_exercise["body_part"]] < even_body_part_count):
                workout_plan.append(compound_exercise)
                used_compound_exercises.add(compound_exercise["name"])
                body_part_counts[compound_exercise["body_part"]] += 1

        while len(workout_plan) < 4:
            if workout_days == 1:
                compound_exercise = self.get_random_exercise(compound_exercises_copy)
                if compound_exercise:
                    workout_plan.append(compound_exercise)
            else:
                accessory_exercise = self.get_random_exercise(accessory_exercises_copy)
                if accessory_exercise:
                    workout_plan.append(accessory_exercise)

        print(f"Day {day}:")
        for exercise in workout_plan:
            sets, reps = self.sets_reps_generator.get_sets_reps(exercise['type'])
            print(f"  {exercise['name']} ({exercise['body_part']}) - {reps} reps, {sets} sets")
        print()