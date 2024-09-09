import pygame
import sys
from arrow import ArrowSimulation


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 700
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("The Arrow Paradox")
        self.clock = pygame.time.Clock()
        self.running = True
        self.police_c1 = pygame.font.Font("GRECOromanLubedWrestling.ttf", 25)
        self.black = (0, 0, 0)

        self.simulation = ArrowSimulation(
            target=500, position_arrow_initial=0, arrow_speed=5, number_stages=100
        )

    def text_c1(self, text, color, x, y):
        text_surface = self.police_c1.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def img_back(self, name, path):
        name = pygame.image.load(path).convert_alpha()
        L_name, H_name = name.get_size()
        name = pygame.transform.scale(name, (L_name, H_name))
        x = (self.screen_width - L_name) // 2
        y = (self.screen_height - H_name) // 2
        self.screen.blit(name, (x, y))

    def image(self, path, width, height, x, y):
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (width, height))
        rect = image.get_rect(topleft=(x, y))
        self.screen.blit(image, rect)
        return rect

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw_arrow(self, position_x, position=100):
        pygame.draw.line(
            self.screen,
            self.black,
            (position_x, self.screen_height // 2),
            (50 + position, self.screen_height // 2),
            5,
        )

    def draw(self):
        self.img_back("Back", "img/background.jpg")
        self.text_c1("The Arrow Paradox", self.black, 260, 100)
        self.image("img/target.png", 150, 200, 500, 190)
        self.image("img/logo_grec.png", 100, 100, 100, 50)

        position_arrow, gap = self.simulation.avancer()

        if position_arrow < 100:
            self.draw_arrow(50, position_arrow)

        else:
            self.draw_arrow(50)

        if position_arrow > 200 and position_arrow < 300:
            self.draw_arrow(250, position_arrow)

        elif position_arrow > 300:
            self.draw_arrow(250, 300)

        if position_arrow > 450:

            self.draw_arrow(450, position_arrow)

        self.text_c1(f"Arrow position: {position_arrow}", self.black, 10, 370)
        self.text_c1(f"Deviation from target: {gap}", self.black, 10, 400)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(30)

    def cleanup(self):
        pygame.quit()
        sys.exit()


game = Game()
game.run()
game.cleanup()
