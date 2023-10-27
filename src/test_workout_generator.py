import pytest
from workout_generator import WorkoutGenerator


@pytest.fixture(scope="function")
def generator():
    """Define a pytest fixture named 'generator'."""
    return WorkoutGenerator()


@pytest.mark.parametrize(
    "days, index, expected_type",
    [
        (
            1,
            0,
            "compound",
        ),  # For a 1-day plan, at index 0, we expect a compound exercise.
        (
            3,
            0,
            "compound",
        ),  # For a 3-day plan, at index 0, we expect a compound exercise.
        (
            3,
            1,
            "accessory",
        ),  # For a 3-day plan, from index 1, we expect accessory exercises.
        (3, 2, "accessory"),
        (3, 3, "accessory"),
    ],
)
def test_workout_generator(generator, days, index, expected_type):
    """Test function using the 'generator' fixture and the defined parameters."""

    # Generate a workout schedule with the goal of "muscle gain"
    workout_schedule = generator.generate_workout(days, "muscle gain")

    # For a 1-day plan
    if days == 1:
        exercises = workout_schedule[0]["Exercises"]
        assert len(exercises) == 4

        for ex in exercises:
            expected_body_parts = [
                e.body_part for e in getattr(generator, f"{expected_type}_exercises")
            ]
            assert ex["Body Part"] in expected_body_parts
    else:
        # For plans more than 1 day
        exercises_day1 = workout_schedule[0]["Exercises"]
        expected_body_parts = [
            e.body_part for e in getattr(generator, f"{expected_type}_exercises")
        ]
        assert exercises_day1[index]["Body Part"] in expected_body_parts
