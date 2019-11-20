import pygame


class StausBar:
    def __init__(self, screen):
        self.screen = screen
        self.textfontobj = pygame.font.SysFont('SimHei', 32)
        self.textsurfaceobj = self.textfontobj.render('test', True, GREEN, BLUE)
        self.textrectobj = self.textsurfaceobj.get_rect()
        self.textrectobj.center = (200, 150)

    def printtext(self):
        self.screen.blit(textsurfaceobj, textrectobj)
