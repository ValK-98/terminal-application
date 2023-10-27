import functools

import workout_database
from sets_reps_generator import SetsRepsGenerator
from workout_exporter import export_workout_to_file


class WorkoutDisplayer:
    @staticmethod
    def _handle_exception(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"An error occurred: {e}")

        return wrapper

    @_handle_exception
    def display_workout_schedule(self, workout_schedule):
        for daily_plan in workout_schedule:
            self.display_workout_plan(daily_plan["Day"], daily_plan)

    def display_workout_plan(self, day, daily_plan):
        print(f"Day {day}:")
        for exercise in daily_plan["Exercises"]:
            self._display_single_exercise(exercise)
        print()

    def _display_single_exercise(self, exercise):
        print(
            f"  {exercise['Name']} ({exercise['Body Part']}) - "
            f"{exercise['Reps']} reps, {exercise['Sets']} sets"
        )

    def _display_options(self, options):
        print("Options:")
        for key, value in options.items():
            option_name = (
                value.__name__.replace("_", " ").capitalize()
                if callable(value)
                else value.capitalize()
            )
            print(f"{key}. {option_name}")

    @_handle_exception
    def modify_workout_plan(self, workout_schedule):
        options = {
            "1": self.remove_workout,
            "2": self.swap_workout,
            "3": self.add_exercise,
            "4": self.export_workout,
            "5": "exit",
        }

        while True:
            self.display_workout_schedule(workout_schedule)
            self._display_options(options)
            option = input("Select an option: ")
            if option in options:
                if option == "5":
                    break
                options[option](workout_schedule)
            else:
                print("Invalid option. Try again.")

    def _get_input_within_range(self, prompt, upper_bound, lower_bound=1):
        while True:
            try:
                value = int(input(prompt))
                if lower_bound <= value <= upper_bound:
                    return value
                else:
                    print(
                        f"Please enter a number between {lower_bound} and {upper_bound}."
                    )
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def _get_valid_day(self, workout_schedule):
        return self._get_input_within_range(
            "Enter the day number: ", len(workout_schedule)
        )

    def _list_exercises(self, workout_day):
        for idx, exercise in enumerate(workout_day["Exercises"], start=1):
            print(f"{idx}. {exercise['Name']}")

    def _get_valid_exercise(self, workout_day, action="modify"):
        self._list_exercises(workout_day)
        prompt = f"Choose an exercise number to {action}: "
        return self._get_input_within_range(prompt, len(workout_day["Exercises"])) - 1

    @_handle_exception
    def _get_valid_day_and_exercise(self, workout_schedule, action="modify"):
        day = self._get_valid_day(workout_schedule)
        exercise_num = self._get_valid_exercise(workout_schedule[day - 1], action)
        return day, exercise_num

    @_handle_exception
    def remove_workout(self, workout_schedule):
        day, to_remove = self._get_valid_day_and_exercise(workout_schedule, "remove")
        if day and to_remove is not None:
            del workout_schedule[day - 1]["Exercises"][to_remove]

    @_handle_exception
    def _find_exercise(self, body_part, exercise_type, excluded_names):
        return next(
            e
            for e in workout_database.workouts
            if e.body_part == body_part
            and e.type == exercise_type
            and e.name not in excluded_names
        )

    @_handle_exception
    def swap_workout(self, workout_schedule):
        day, to_swap = self._get_valid_day_and_exercise(workout_schedule, "swap")
        if day and to_swap is not None:
            swap_with_body_part = input(
                "Enter the body part to swap with (or type 'same' for the same body part): "
            )
            if swap_with_body_part == "same":
                swap_with_body_part = workout_schedule[day - 1]["Exercises"][to_swap][
                    "Body Part"
                ]
            new_exercise = self._find_exercise(
                swap_with_body_part,
                "",
                [ex["Name"] for ex in workout_schedule[day - 1]["Exercises"]],
            )
            workout_schedule[day - 1]["Exercises"][to_swap]["Name"] = new_exercise.name
            workout_schedule[day - 1]["Exercises"][to_swap][
                "Body Part"
            ] = new_exercise.body_part

    @_handle_exception
    def add_exercise(self, workout_schedule):
        day = self._get_valid_day(workout_schedule)
        body_part = input("Enter the body part for the exercise: ")
        exercise_type = input("Enter the exercise type (compound/accessory): ").lower()

        available_exercises = [
            e
            for e in workout_database.workouts
            if e.body_part == body_part
            and e.type == exercise_type
            and e.name
            not in [ex["Name"] for ex in workout_schedule[day - 1]["Exercises"]]
        ]
        if not available_exercises:
            print(f"No available exercises for {body_part} as {exercise_type}.")
            return

        new_exercise = available_exercises[0]
        sets_reps_generator = SetsRepsGenerator(
            workout_schedule[day - 1]["Exercises"][0]["Sets"]
        )
        sets, reps = sets_reps_generator.get_sets_reps(exercise_type)

        workout_schedule[day - 1]["Exercises"].append(
            {
                "Name": new_exercise.name,
                "Body Part": new_exercise.body_part,
                "Reps": reps,
                "Sets": sets,
            }
        )

        print(f"Added {new_exercise.name} for Day {day}.")

    @_handle_exception
    def export_workout(self, workout_schedule):
        filename = input("Enter the filename (or press enter for 'workout_plan.txt'): ")
        if not filename:
            filename = "workout_plan.txt"
        export_workout_to_file(workout_schedule, filename)
        print(f"Workout plan exported to {filename}!")
