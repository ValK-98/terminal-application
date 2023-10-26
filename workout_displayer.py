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
        options = {
            "1": self.remove_workout,
            "2": self.swap_workout,
            "3": "exit"
        }
        
        while True:
            try:
                self.display_workout_schedule(workout_schedule)
                print("Options:")
                for key, value in options.items():
                    print(f"{key}. {value.__name__.replace('_', ' ').capitalize() if callable(value) else value.capitalize()}")
                option = input("Select an option: ")
                if option in options:
                    if option == "3":
                        break
                    options[option](workout_schedule)
                else:
                    print("Invalid option. Try again.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
