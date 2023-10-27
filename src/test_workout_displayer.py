import pytest
from workout_displayer import WorkoutDisplayer
from unittest.mock import patch, Mock

# Sample workout
SAMPLE_WORKOUT_SCHEDULE = [
    {
        "Day": 1,
        "Exercises": [
            {"Name": "squats", "Body Part": "legs", "Reps": 10, "Sets": 3},
            {"Name": "push-ups", "Body Part": "chest", "Reps": 12, "Sets": 3},
        ],
    },
    {
        "Day": 2,
        "Exercises": [
            {"Name": "bicep curl", "Body Part": "arms", "Reps": 10, "Sets": 3},
            {"Name": "front raises", "Body Part": "shoulders", "Reps": 12, "Sets": 3},
        ],
    },
]


@pytest.fixture
def workout_displayer():
    """Sets up an instance of WorkoutDisplayer for tests."""
    return WorkoutDisplayer()


def test_get_valid_day_and_exercise_valid_input(workout_displayer):
    """Test '_get_valid_day_and_exercise' method with valid inputs."""
    # Mocking the 'input' function to return '1' and then '2'
    with patch("builtins.input", side_effect=["1", "2"]):
        # Calling the method and storing the results
        day, exercise_num = workout_displayer._get_valid_day_and_exercise(
            SAMPLE_WORKOUT_SCHEDULE
        )

        # Assert that the method returned expected values
        assert day == 1
        assert exercise_num == 1


def test_get_valid_day_and_exercise_invalid_input(workout_displayer):
    """Test '_get_valid_day_and_exercise' method with a series of invalid inputs followed by valid ones."""
    # Mocking the 'input' function to return '10', '0', 'a' (invalid values) and then '2', '1' (valid values)
    with patch("builtins.input", side_effect=["10", "0", "a", "2", "1"]):
        # Calling the method and storing the results
        day, exercise_num = workout_displayer._get_valid_day_and_exercise(
            SAMPLE_WORKOUT_SCHEDULE
        )

        # Assert that after discarding the invalid values, the method returned the expected valid values
        assert day == 2
        assert exercise_num == 0
