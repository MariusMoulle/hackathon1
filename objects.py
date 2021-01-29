from random import randint
class Objects:

    def __init__(self, position):
        self.position = position
    
class Food(Objects):
    def __init__(self, position):
        super().__init__(position)
        self.value = random.randint(1, 10)
        self.type = 'food'
        self.repr = 'a'

class Water(Objects):
    def __init__(self, position):
        super().__init__(position)
        self.value = random.randint(1, 10)
        self.type = 'water'
        self.repr = 'w'

class Arms(Objects):
    def __init__(self, position):
        super().__init__(position)
        self.value = random.randint(10, 50)
        self.type = 'arm'
        self.repr = 'T'

class Armor(Objects):
    def __init__(self, position):
        super().__init__(position)
        self.value = random.randint(10, 50)
        self.type = 'armor'
        self.repr = 'A'

class Gold(Objects):
    def __init__(self, position):
        super().__init__(position)
        self.value = random.randint(5, 100)
        self.type = 'gold'
        self.repr = 'o'

