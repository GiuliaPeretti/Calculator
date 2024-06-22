import pygame
from settings import *
import ast

def draw_backgrownd():
    screen.fill(BACKGROUND_COLOR)
    draw_screen()


def draw_screen():
    pygame.draw.rect(screen, BACKGROUND_COLOR, (10, 10, SCREEN_WIDTH-20, SCREEN_HEIGHT/4))
    pygame.draw.rect(screen, (0,0,0), (10, 10, SCREEN_WIDTH-20, SCREEN_HEIGHT/4),3)

def draw_buttons():
    font = pygame.font.SysFont('arial', 40)
    offset_tx,offset_ty=33,15
    color_button=(230,230,230)
    color_button2=(200,200,250)

    boxes=[]

    x,y,w,h=10, SCREEN_HEIGHT/4+20, (SCREEN_WIDTH-50)/4, ((3*(SCREEN_HEIGHT/4)-20)-50)/5
    pygame.draw.rect(screen, color_button2, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("D", True, (0,0,0))
    screen.blit(text, (x+offset_tx-4, y+offset_ty))
    boxes.append({'name': 'D', 'box':((x,x+w),(y,y+h))})
   
    x = x+w+10
    pygame.draw.rect(screen, color_button2, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("(", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty-3))
    boxes.append({'name': '(', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button2, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render(")", True, (0,0,0))
    screen.blit(text, (x+offset_tx+6, y+offset_ty-3))
    boxes.append({'name': ')', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button2, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("^", True, (0,0,0))
    screen.blit(text, (x+offset_tx+1, y+offset_ty))
    boxes.append({'name': '^', 'box':((x,x+w),(y,y+h))})
 

    x, y= 10, y+h+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("7", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '7', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("8", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '8', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("9", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '9', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button2, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("+", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '+', 'box':((x,x+w),(y,y+h))})
 

    x, y= 10, y+h+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("4", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '4', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("5", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '5', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("6", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '6', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button2, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("-", True, (0,0,0))
    screen.blit(text, (x+offset_tx+5, y+offset_ty))
    boxes.append({'name': '-', 'box':((x,x+w),(y,y+h))})
 

    x, y= 10, y+h+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("1", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '1', 'box':((x,x+w),(y,y+h))})
 
    x = x+w+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("2", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '2', 'box':((x,x+w),(y,y+h))})

    x = x+w+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("3", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '3', 'box':((x,x+w),(y,y+h))})

    x = x+w+10
    pygame.draw.rect(screen, color_button2, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("*", True, (0,0,0))
    screen.blit(text, (x+offset_tx+3, y+offset_ty))
    boxes.append({'name': '*', 'box':((x,x+w),(y,y+h))})


    x, y= 10, y+h+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("0", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '0', 'box':((x,x+w),(y,y+h))})

    x = x+w+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render(".", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '.', 'box':((x,x+w),(y,y+h))})

    x = x+w+10
    pygame.draw.rect(screen, color_button, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 3)
    text=font.render("=", True, (0,0,0))
    screen.blit(text, (x+offset_tx, y+offset_ty))
    boxes.append({'name': '=', 'box':((x,x+w),(y,y+h))})

    x = x+w+10
    pygame.draw.rect(screen, color_button2, (x,y,w,h))
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h),3)
    text=font.render("/", True, (0,0,0))
    screen.blit(text, (x+offset_tx+5, y+offset_ty))
    boxes.append({'name': '/', 'box':((x,x+w),(y,y+h))})

    return boxes

def displaye_exp(t):
    global expression
    font = pygame.font.SysFont('arial', 35)
    draw_screen()
    if(t=='D'):
        expression=expression[:len(expression)-1]
    elif(t=='='):
        result(expression)
    else:
        expression=expression+t
    text=font.render(expression, True, (0,0,0))
    screen.blit(text, (20,20))

def result(text):
    print(check_validity(text))
    if(check_validity(text)):
        print(calculate(text))
    else:
        font = pygame.font.SysFont('arial', 35)
        text=font.render("Syntax error", True, (255,0,0))
        screen.blit(text, (SCREEN_WIDTH-20-190, SCREEN_HEIGHT/4-35))
    print("result")

def check_validity(text):
    if (text==''):
        return False
    if ('()'in text):
        return False
    if(not(text[-1].isnumeric()) and text[-1]!='(' and text[-1]!=')'):
        print("no ultimo car")
        return False
    count=0
    for c in text:
        if count<0:
            print(")in piu")
            return False
        if c=='(':
            count+=1
        elif c==')':
            count-=1
    if (count!=0):
        print("( in piu")
        return False
    for i in range(0, len(text)-2):
        if((not(text[i].isnumeric()) and text[i]!='(' and text[i]!=')') and (not(text[i+1].isnumeric()) and text[i+1]!='(' and text[i+1]!=')')):
            print("non num")
            return False
    return True

def calculate(text):
    while('(' in text):
        pos1, pos2=inside_par(text)
        if (text[pos1+1:pos2].isnumeric()):
            text=text[:pos1]+text[pos1+1:pos2]+text[pos2+1:]
        else:
            pass
    return(text)


def inside_par(text):  #(34((23)*2)3(23))
    pos1=text.index('(')
    pos2=text.index(')')
    text=text[pos+1:text.index(')')]
    while('(' in text):
        pos=text.index('(')
        text=text[pos+1:]
    return(pos,pos2)





pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Progress bar')
font = pygame.font.SysFont('arial', 20)
run=True
draw_backgrownd()
boxes=draw_buttons()
expression=''

while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            for i in boxes:
                if (x>i['box'][0][0] and x<=i['box'][0][1] and y>=i['box'][1][0] and y<=i['box'][1][1]):
                    displaye_exp(i['name'])

        if (event.type == pygame.KEYDOWN):
            pass
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()