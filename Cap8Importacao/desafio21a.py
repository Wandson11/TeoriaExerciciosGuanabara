import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Audioslave - Like A Stone (Baixar Musicas Gratis_QZf1zaGwJNE_1378865729).mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
