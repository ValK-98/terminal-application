class WorkoutExporter:
    def export_to_file(self, workout_schedule):
        filename = "workout_schedule.txt"
        with open(filename, 'w') as file:
            for daily_plan in workout_schedule:
                day = daily_plan["Day"]
                file.write(f"Day {day}:\n")
                for exercise in daily_plan["Exercises"]:
                    file.write(f"  {exercise['Name']} ({exercise['Body Part']}) - {exercise['Reps']} reps, {exercise['Sets']} sets\n")
                file.write("\n")
        print(f"Workout schedule has been successfully saved to {filename}!")
