class Settings():
    def __init__(self):
        self.screen_width = 1366
        self.screen_height = 700
        self.bg_color = (0,0,0)
        self.fleet_drop_speed=100
        self.ship_limit=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(233,212,200)
        self.bullets_allowed = 100
        self.speedup_scale=1.1
        self.score_scale = 1.5
        self.initialise_dynamic_settings()
    def initialise_dynamic_settings(self):
        self.ship_speed_factor =1.5
        self.bullet_speed_factor =3
        self.alien_speed_factor=1
        self.fleet_direction=1
        self.alien_points = 10
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*= self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)
