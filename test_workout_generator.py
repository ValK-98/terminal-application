import pytest
from workout_generator import WorkoutGenerator

# Define a pytest fixture named 'generator'. 
@pytest.fixture(scope="function")
def generator():
    return WorkoutGenerator()

# Here, we're setting up parameterized tests with pytest. 
# Parameterized tests allow us to run a single test function multiple times but with different arguments.
@pytest.mark.parametrize("days, index, expected_type", [
    (1, 0, "compound"),  # For a 1-day plan, at index 0 (first exercise), we expect a compound exercise.
    (3, 0, "compound"),  # For a 3-day plan, at index 0 (first exercise), we expect a compound exercise.
    (3, 1, "accessory"), # For a 3-day plan, starting at index 1, we expect the subsequent exercises to be accessory exercises.
    (3, 2, "accessory"),
    (3, 3, "accessory"),
])

# This function uses the 'generator' fixture and the parameters defined above.
def test_workout_generator(generator, days, index, expected_type):
    
    # Generate a workout schedule using the 'generator' with the goal of "muscle gain"
    workout_schedule = generator.generate_workout(days, "muscle gain")
    
    # If the plan is for 1 day...
    if days == 1:
        # Get the list of exercises for the first day.
        exercises = workout_schedule[0]["Exercises"]
        
        # Assert that the length of the exercises list is 4 (i.e., there are 4 exercises).
        assert len(exercises) == 4
        
        # Loop through each exercise in the exercises list.
        for ex in exercises:
            # Assert that the body part of the current exercise exists in the body parts of the expected type of exercises (either compound or accessory) from the generator.
            assert ex["Body Part"] in [e.body_part for e in getattr(generator, f"{expected_type}_exercises")]
    else:
        # If the plan is for more than 1 day (like 3 days in our test case)...
        
        # Get the list of exercises for the first day.
        exercises_day1 = workout_schedule[0]["Exercises"]
        
        # Assert that the body part of the exercise at the specified index exists in the body parts of the expected type of exercises (either compound or accessory) from the generator.
        assert exercises_day1[index]["Body Part"] in [e.body_part for e in getattr(generator, f"{expected_type}_exercises")]
