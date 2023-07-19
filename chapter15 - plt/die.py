from random import randint
class Die:
    """骰子类"""
    
    def __init__(self, num_sides=6) -> None:
        self.num_sides = num_sides
        
    def roll(self):
        """返回投掷数字"""
        return randint(1, self.num_sides)