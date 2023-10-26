import workout_database
from sets_reps_generator import SetsRepsGenerator

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
            "3": self.add_exercise,
            "4": "exit"
        }
        
        while True:
            try:
                self.display_workout_schedule(workout_schedule)
                print("Options:")
                for key, value in options.items():
                    print(f"{key}. {value.__name__.replace('_', ' ').capitalize() if callable(value) else value.capitalize()}")
                option = input("Select an option: ")
                if option in options:
                    if option == "4":
                        break
                    options[option](workout_schedule)
                else:
                    print("Invalid option. Try again.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

    def _get_input_within_range(self, prompt, upper_bound, lower_bound=1):
        while True:
            try:
                value = int(input(prompt))
                if lower_bound <= value <= upper_bound:
                    return value
                else:
                    print(f"Please enter a number between {lower_bound} and {upper_bound}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def _get_valid_day(self, workout_schedule):
        try:
            return self._get_input_within_range("Enter the day number: ", len(workout_schedule))
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def _list_exercises(self, workout_day):
        try:
            for idx, exercise in enumerate(workout_day["Exercises"], start=1):
                print(f"{idx}. {exercise['Name']}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _get_valid_exercise(self, workout_day, action="modify"):
        try:
            self._list_exercises(workout_day)
            return self._get_input_within_range(f"Choose an exercise number to {action}: ", len(workout_day["Exercises"])) - 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def _get_valid_day_and_exercise(self, workout_schedule, action="modify"):
        try:
            day = self._get_valid_day(workout_schedule)
            if day is None:
                return None, None
            exercise_num = self._get_valid_exercise(workout_schedule[day-1], action)
            if exercise_num is None:
                return None, None
            return day, exercise_num
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None

    def remove_workout(self, workout_schedule):
        try:
            day, to_remove = self._get_valid_day_and_exercise(workout_schedule, "remove")
            if day and to_remove is not None:
                del workout_schedule[day-1]['Exercises'][to_remove]
        except Exception as e:
            print(f"An error occurred: {e}")

    def swap_workout(self, workout_schedule):
        try:
            day, to_swap = self._get_valid_day_and_exercise(workout_schedule, "swap")
            if day and to_swap is not None:
                swap_with_body_part = input("Enter the body part to swap with (or type 'same' for the same body part): ")
                if swap_with_body_part == 'same':
                    swap_with_body_part = workout_schedule[day-1]['Exercises'][to_swap]['Body Part']
                new_exercise = next(e for e in workout_database.workouts if e.body_part == swap_with_body_part and e.name not in [ex['Name'] for ex in workout_schedule[day-1]['Exercises']])
                workout_schedule[day-1]['Exercises'][to_swap]['Name'] = new_exercise.name
                workout_schedule[day-1]['Exercises'][to_swap]['Body Part'] = new_exercise.body_part
        except StopIteration:
            print("No available exercises to swap with. Try another body part.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def add_exercise(self, workout_schedule):
        day = self._get_valid_day(workout_schedule)
        if day is None:
            return
        
        body_part = input("Enter the body part for the exercise: ")
        exercise_type = input("Enter the exercise type (compound/accessory): ").lower()
        
        try:
            available_exercises = [e for e in workout_database.workouts if e.body_part == body_part and e.type == exercise_type and e.name not in [ex['Name'] for ex in workout_schedule[day-1]['Exercises']]]
            if not available_exercises:
                print(f"No available exercises for {body_part} as {exercise_type}.")
                return

            new_exercise = available_exercises[0]
            sets_reps_generator = SetsRepsGenerator(workout_schedule[day-1]["Exercises"][0]["Sets"])
            sets, reps = sets_reps_generator.get_sets_reps(exercise_type)

            workout_schedule[day-1]['Exercises'].append({
                "Name": new_exercise.name,
                "Body Part": new_exercise.body_part,
                "Reps": reps,
                "Sets": sets
            })
            
            print(f"Added {new_exercise.name} for Day {day}.")
        except Exception as e:
            print(f"An error occurred: {e}")

