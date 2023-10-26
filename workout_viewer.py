class WorkoutViewer:
 
 def display_workout_schedule(self, workout_schedule):
        for daily_plan in workout_schedule:
            self.display_workout_plan(daily_plan["Day"], daily_plan)

def display_workout_plan(self, day, daily_plan):
        print(f"Day {day}:")
        for exercise in daily_plan["Exercises"]:
            print(f"  {exercise['Name']} ({exercise['Body Part']}) - {exercise['Reps']} reps, {exercise['Sets']} sets")
        print()


