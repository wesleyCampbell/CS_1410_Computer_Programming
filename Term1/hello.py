import pygame
import colorsys


class Game:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 80)
        self.width = 900
        self.height = 400
        self.win = pygame.display.set_mode((self.width, self.height))
        self.fps = 30
        self.message = "Hello World!"
        self.hue = 0
        self.clr = (0, 0, 0)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    print("You quit!")
                    break
            self.win.fill((255, 255, 255))
            self.render_text(self.win, "Hello World!")
            self.update_color()
            pygame.display.update()

    def render_text(self, win, text):
        text = self.font.render(
            text, False, self.clr)
        width, height = self.font.size(self.message)
        win.blit(text, (self.width / 2 - width /
                        2, self.height / 2 - height / 2))

    def update_color(self):
        self.hue = self.hue + 1 if self.hue < 359 else 0
        print(self.hue)
        self.clr = tuple(round(i * 255)
                         for i in colorsys.hsv_to_rgb(self.hue, 1, 1))


def normalize(color):
    return color[0] / 255.0, color[1] / 255.0, color[2] / 255.0


# if __name__ == "__main__":
#     game = Game()
#     game.run()


color = (66, 1, 1)

updated_color = colorsys.hls_to_rgb(color[0], color[1], color[2])
print(updated_color)
