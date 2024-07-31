
class Entety:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.controller = Animation_controller()

    def take_damage(self, damage):
        self.health -= damage


class Animation_controller():

    def __init__(self):
        pass
        