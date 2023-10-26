import pytest
from sets_reps_generator import SetsRepsGenerator

# Define a fixture named 'sr_generator' with a scope limited to individual test functions.
# This fixture will generate an instance of the SetsRepsGenerator class for both "muscle gain" and "strength gain".
@pytest.fixture(scope="function", params=["muscle gain", "strength gain"])
def sr_generator(request):
    # Return an instance of SetsRepsGenerator with the goal type specified by 'params'
    return SetsRepsGenerator(request.param)

# Parametrize the test function below to run multiple test cases.
# Each test case uses a different combination of 'goal_type', 'exercise_type', 'expected_sets', and 'reps_range'.
@pytest.mark.parametrize("goal_type, exercise_type, expected_sets, reps_range", [
    ("muscle gain", "compound", 4, (10, 12)),
    ("muscle gain", "accessory", 3, (10, 15)),
    ("strength gain", "compound", 5, (4, 6)),
    ("strength gain", "accessory", 3, (5, 10))
])
def test_sets_reps_generator(goal_type, exercise_type, expected_sets, reps_range):
    # Create an instance of SetsRepsGenerator with the specified 'goal_type'
    sr_gen = SetsRepsGenerator(goal_type)

    # Run the test 100 times for each parameterized case to ensure consistent behavior
    # especially given the randomness in the 'get_sets_reps' method.
    for _ in range(100):
        # Call the 'get_sets_reps' method and unpack the returned sets and reps values
        sets, reps = sr_gen.get_sets_reps(exercise_type)

        # Assert that the returned 'sets' matches the 'expected_sets'
        assert sets == expected_sets

        # Assert that the returned 'reps' is within the expected range specified by 'reps_range'
        assert reps_range[0] <= reps <= reps_range[1]
