class bot_vel_controller():
    def __init__(self, bot_id = 0, vel_x = 0, vel_y = 0, angle = 0):
        self.bot_id = bot_id
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.angle = angle
    
    def move(self, vel_x, vel_y, angle):
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.angle = angle