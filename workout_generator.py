import workout_database
import random
from sets_reps_generator import SetsRepsGenerator

class WorkoutGenerator:
    def __init__(self):
        self.body_parts = set(exercise.body_part for exercise in workout_database.workouts)
        self.compound_exercises = [exercise for exercise in workout_database.workouts if exercise.type == "compound"]
        self.accessory_exercises = [exercise for exercise in workout_database.workouts if exercise.type == "accessory"]

    def get_random_exercise(self, exercise_list, excluded_names=set()):
        exercise_list = [e for e in exercise_list if e.name not in excluded_names]
        random.shuffle(exercise_list)
        return exercise_list.pop() if exercise_list else None

    def generate_workout(self, workout_days, goal_type):
        workout_schedule = [] 
        used_compound_exercises = set()
        body_part_counts = {part: 0 for part in self.body_parts}
        self.sets_reps_generator = SetsRepsGenerator(goal_type)

        for day in range(1, workout_days + 1):
            daily_plan = self.get_workout_plan_for_day(day, workout_days, used_compound_exercises, body_part_counts)
            workout_schedule.append(daily_plan)
        
        return workout_schedule 

    def get_workout_plan_for_day(self, day, workout_days, used_compound_exercises, body_part_counts):
        workout_plan = []
        compound_exercises_copy = self.compound_exercises.copy()
        accessory_exercises_copy = self.accessory_exercises.copy()

        if workout_days == 1:
            while len(workout_plan) < 4:
                compound_exercise = self.get_random_exercise(compound_exercises_copy, used_compound_exercises)
                if compound_exercise:
                    workout_plan.append(compound_exercise)
                    used_compound_exercises.add(compound_exercise.name)
        else:
            compound_exercise = self.get_random_exercise(compound_exercises_copy, used_compound_exercises)
            if compound_exercise:
                workout_plan.append(compound_exercise)
                used_compound_exercises.add(compound_exercise.name)
                body_part_counts[compound_exercise.body_part] += 1

            while len(workout_plan) < 4:
                underworked_body_parts = [part for part, count in body_part_counts.items() if count == min(body_part_counts.values())]
                possible_exercises = [ex for ex in accessory_exercises_copy if ex.body_part in underworked_body_parts]
                accessory_exercise = self.get_random_exercise(possible_exercises)
                
                if accessory_exercise:
                    workout_plan.append(accessory_exercise)
                    body_part_counts[accessory_exercise.body_part] += 1

        return {
            "Day": day,
            "Exercises": [{
                "Name": exercise.name,
                "Body Part": exercise.body_part,
                "Reps": reps,
                "Sets": sets
            } for exercise, (sets, reps) in zip(workout_plan, [self.sets_reps_generator.get_sets_reps(e.type) for e in workout_plan])]
        }

class WorkoutDisplayer:
    def display_workout_schedule(self, workout_schedule):
        for daily_plan in workout_schedule:
            self.display_workout_plan(daily_plan["Day"], daily_plan)

    def display_workout_plan(self, day, daily_plan):
        print(f"Day {day}:")
        for exercise in daily_plan["Exercises"]:
            print(f"  {exercise['Name']} ({exercise['Body Part']}) - {exercise['Reps']} reps, {exercise['Sets']} sets")
        print()
