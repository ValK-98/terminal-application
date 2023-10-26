import workout_database


class WorkoutDisplayer:
    def display_workout_schedule(self, workout_schedule):
        for daily_plan in workout_schedule:
            self.display_workout_plan(daily_plan["Day"], daily_plan)

    def display_workout_plan(self, day, daily_plan):
        print(f"Day {day}:")
        for exercise in daily_plan["Exercises"]:
            print(f"  {exercise['Name']} ({exercise['Body Part']}) - {exercise['Reps']} reps, {exercise['Sets']} sets")
        print()

    def modify_workout_plan(self, workout_schedule):
        while True:
            self.display_workout_schedule(workout_schedule)
            print("Options:")
            print("1. Remove a workout")
            print("2. Swap a workout")
            print("3. Finish editing")
            option = input("Select an option (1/2/3): ")
            if option == "1":
                self.remove_workout(workout_schedule)
            elif option == "2":
                self.swap_workout(workout_schedule)
            elif option == "3":
                break
            else:
                print("Invalid option. Try again.")

