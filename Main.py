import pygame

pygame.init()

screen = pygame.display.set_mode((600,700))
pygame.display.set_caption("Pygame shapes")


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen.fill((0,25,255))
pygame.display.update()
while True:
   class Circle():
       def __init__(self,colour,center,radius):
           self.circle_surf = screen
           self.circle_colour = colour
           self.circle_center = center
           self.circle_radius = radius

       def draw(self):
           self.Draw_circle = pygame.draw.circle(self.circle_surf, self.circle_colour, self.circle_center, self.circle_radius)

   greenCircle=Circle(green,(150,120),100)
   redCircle=Circle(red,(250,300),150)
   whiteCircle=Circle(white,(400,500),200)
   whiteCircle.draw()
   greenCircle.draw()
   redCircle.draw()
   for event in pygame.event.get():
       if event.type==pygame.QUIT:
           pygame.quit()
   pygame.display.update()
