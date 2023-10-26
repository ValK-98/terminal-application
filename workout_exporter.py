def export_workout_to_file(workout_schedule, filename="workout_plan.txt"):
    with open(filename, 'w') as file:
        for daily_plan in workout_schedule:
            day = daily_plan["Day"]
            file.write(f"Day {day}:\n")
            for exercise in daily_plan["Exercises"]:
                file.write(f"  {exercise['Name']} ({exercise['Body Part']}) - {exercise['Reps']} reps, {exercise['Sets']} sets\n")
            file.write("\n")
