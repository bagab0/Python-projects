class Hat:
    def __init__(self, **balls):
        """
        Initialize the hat with a variable number of balls of each color.
        The 'contents' list will contain strings representing each ball.
        """
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)  # Add each color ball 'count' times to the list
    
    def draw(self, num_balls):
        """
        Draw a specified number of balls randomly from the hat.
        If num_balls is greater than the number of balls in the hat,
        return all the balls in the hat.
        """
        # Check if num_balls to draw exceeds the available number of balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()  # Return all the balls in the hat
            self.contents.clear()  # Empty the hat after drawing all balls
            return drawn_balls
        
        # Otherwise, randomly draw 'num_balls' from the hat
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove the drawn balls from the hat
        
        return drawn_balls

