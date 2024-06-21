import pygame
from settings import *
import ast

def draw_backgrownd():
    screen.fill(BACKGROUND_COLOR)
    draw_scrren()
    draw_buttons()

def draw_scrren():
    pygame.draw.rect(screen, (0,0,0), (10, 10, SCREEN_WIDTH-20, SCREEN_HEIGHT/4),3)

def draw_buttons():
    font = pygame.font.SysFont('arial', 40)
    offset_tx,offset_ty=33,15

    x,y,w,h=10, SCREEN_HEIGHT/4+20, (SCREEN_WIDTH-50)/4, ((3*(SCREEN_HEIGHT/4)-20)-50)/5
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("D", True, (0,0,0))
    screen.blit(text, (x+offset_tx-4, y+offset_ty))
   
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("(", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty-3))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render(")", True, (0,0,0))
    screen.blit(text, (x+offset_tx+6, y+offset_ty-3))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("^", True, (0,0,0))
    screen.blit(text, (x+offset_tx+1, y+offset_ty))
 

    x, y= 10, y+h+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("7", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("8", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("9", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("+", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
 

    x, y= 10, y+h+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("4", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("5", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("6", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("-", True, (0,0,0))
    screen.blit(text, (x+offset_tx+5, y+offset_ty))
 

    x, y= 10, y+h+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("1", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
 
    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("2", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))

    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("3", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))

    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("x", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))



    x, y= 10, y+h+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("0", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))

    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render(".", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))

    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("=", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))

    x = x+w+10
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("/", True, (0,0,0))
    screen.blit(text, (x+offset_tx+5, y+offset_ty))

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Progress bar')
font = pygame.font.SysFont('arial', 20)
run=True
draw_backgrownd()

while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()

        if (event.type == pygame.KEYDOWN):
            pass
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()