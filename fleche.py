class FlecheSimulation:
    def __init__(self, target, position_arrow_initial, arrow_speed, number_stages):
        self.target = target
        self.position_arrow = position_arrow_initial
        self.arrow_speed = arrow_speed
        self.number_stages = number_stages
        self.current_step = 0

    def avancer(self):
        if self.current_step < self.number_stages:
            self.position_arrow += self.arrow_speed
            self.current_step += 1
            gap = self.target - self.position_arrow
            return self.position_arrow, gap
        return self.position_arrow, self.target - self.position_arrow
