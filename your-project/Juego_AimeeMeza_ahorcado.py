import pygame

imagen=pygame.image.load("Imagen1.png")
pantalla=pygame.display.set_mode((100,200))
pantalla.fill(255,255,255)
pantalla.blit(imagen,(300,50))
pygame.display.update()
