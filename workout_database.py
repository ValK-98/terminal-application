from collections import namedtuple

Exercise = namedtuple('Exercise', ['name', 'body_part', 'type'])

workouts = [
    Exercise("squats", "legs", "compound"),
    Exercise("leg extensions", "legs", "accessory"),
    Exercise("hamstring curl", "legs", "accessory"),
    Exercise("lunges", "legs", "accessory"),
    Exercise("leg press", "legs", "compound"),
    Exercise("calf raises", "legs", "accessory"),
    Exercise("bench press", "chest", "compound"),
    Exercise("push-ups", "chest", "compound"),
    Exercise("dips", "chest", "accessory"),
    Exercise("pec deck fly", "chest", "accessory"),
    Exercise("incline dumbbell bench press", "chest", "compound"),
    Exercise("cable fly", "chest", "accessory"),
    Exercise("bicep curl", "arms", "accessory"),
    Exercise("hammer curls", "arms", "accessory"),
    Exercise("skull crushers", "arms", "accessory"),
    Exercise("tricep extensions", "arms", "accessory"),
    Exercise("overhead press", "shoulders", "compound"),
    Exercise("front raises", "shoulders", "accessory"),
    Exercise("shrugs", "shoulders", "accessory"),
    Exercise("arnold press", "shoulders", "accessory"),
    Exercise("lat raises", "shoulders", "accessory"),
    Exercise("deadlifts", "back", "compound"),
    Exercise("bent-over rows", "back", "compound"),
    Exercise("pull-ups", "back", "compound"),
    Exercise("lat pulldown", "back", "accessory"),
    Exercise("rows", "back", "accessory"),
    Exercise("t-bar rows", "back", "compound"),
    Exercise("face pulls", "shoulders", "accessory"),
    Exercise("rear delt fly", "shoulders", "accessory"),
    Exercise("concentration curls", "arms", "accessory"),
    Exercise("dumbbell kickbacks", "arms", "accessory"),
    Exercise("barbell curls", "arms", "compound"),
    Exercise("pushdowns", "arms", "accessory"),
    Exercise("chin-ups", "back", "compound"),
    Exercise("seated leg curls", "legs", "accessory"),
    Exercise("bulgarian split squats", "legs", "accessory"),
    Exercise("hack squats", "legs", "compound"),
    Exercise("decline bench press", "chest", "compound"),
    Exercise("cable crossovers", "chest", "accessory"),
    Exercise("dumbbell pullovers", "chest", "accessory"),
    Exercise("hyperextensions", "back", "accessory"),
]