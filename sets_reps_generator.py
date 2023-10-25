import numpy as np

class SetsRepsGenerator:
    def __init__(self, goal_type):
        if goal_type == "muscle gain":
            self.compound = {"sets": 4, "reps_range": (10, 12)}
            self.accessory = {"sets": 3, "reps_range": (10, 15)}
        else: 
            self.compound = {"sets": 5, "reps_range": (4, 6)}
            self.accessory = {"sets": 3, "reps_range": (5, 10)}

    def get_sets_reps(self, exercise_type):
        info = self.compound if exercise_type == "compound" else self.accessory
        reps = np.random.randint(info["reps_range"][0], info["reps_range"][1] + 1)
        # sets = np.random.choice([info["sets"], info["sets"]-1, info["sets"]+1])
        return info["sets"], reps