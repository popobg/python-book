import math

class Ball:
    def __init__(self, height, elasticity):
        # the unit of measurement of distance is the meter
        self._height = height
        self._elasticity = elasticity
        self._speed = 0.0
        self._acceleration = 9.8

    def get_height(self):
        return self._height

    def get_speed(self):
        return self._speed

    def get_elasticity(self):
        return self._elasticity

    def reset_height(self):
        self._height = 0

    def reset_speed(self):
        self._speed = 0

    def update_height(self, s):
        self._height = self._height - s

    def update_speed(self, dt):
        self._speed = self._speed + self._acceleration * dt

    def calculate_height_after_bounce(self):
        self._height = -self._height * self._elasticity

    def calculate_speed_after_bounce(self, t_bounce):
        self._speed = -(self._speed + self._acceleration * t_bounce) * self._elasticity

    def calculate_elasticity(self):
        if self._elasticity < 0.03:
            self._elasticity = 0.0
        else:
            self._elasticity = self._elasticity - 0.03

    def calculate_tbounce(self, start_speed, start_height):
        t_bounce = (-start_speed + math.sqrt(start_speed**2 +2 * self._acceleration * start_height))/self._acceleration
        return t_bounce

    def calculate_fall_distance(self, dt):
        s = 0.5 * self._acceleration * dt**2 + self._speed * dt
        return s

    def bouncing_simulation(self, dt):
        start_height = self.get_height()
        start_speed = self.get_speed()
        s = self.calculate_fall_distance(dt)
        self.update_height(s)
        self.update_speed(dt)
        if self.get_height() < 0:
            t_bounce = self.calculate_tbounce(start_speed, start_height)
            self.calculate_height_after_bounce()
            self.calculate_speed_after_bounce(t_bounce)
            self.calculate_elasticity()
        elif start_speed * self.get_speed() < 0:
            self.reset_speed()
        if self.get_height() < 0:
            self.reset_height()


ball = Ball(3.0, 0.5)

while ball.get_elasticity() != 0:
    ball.bouncing_simulation(0.1)
    print(f"The ball's speed is {ball.get_speed():.3f} and the ball is at {ball.get_height():.3f} meters.")
print("The ball is on the ground. No more bouncing.")