workout_list = []

def get_last_id():
    if workout_list:
        last_workout = workout_list[-1]
    else:
        return 1
    return last_workout.id + 1

class Workout:
    def __init__(self, name, length, directions, body_part):
        self.id = get_last_id()
        self.name = name
        self.length = length
        self.directions = directions
        self.body_part = body_part
        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'length': self.length,
            'directions': self.directions,
            'body_part': self.body_part
        }