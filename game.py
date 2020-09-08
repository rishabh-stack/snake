import pygame
import random
import os 
pygame.mixer.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
pygame.init()
window=pygame.display.set_mode((1200,550))
pygame.display.set_caption("Snake game")
clock= pygame.time.Clock()
bg=pygame.image.load("snake.jpg")
bg=pygame.transform.scale(bg,(1200,550)).convert_alpha()

font=pygame.font.SysFont(None,55)
def score_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    window.blit(screen_text,[x,y])
def welcome():
    exit_game=False
    while not exit_game:
        window.fill((233,220,229))
        score_screen("welcome to Rishabh snakes",black,350,250)
        score_screen("press space to play",black,420,290)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameloop()
        pygame.display.update()
        clock.tick(60)

def plot_snake(window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])
pygame.mixer.music.load('back.mp3')
pygame.mixer.music.play()
def gameloop():
    exit_game=False
    game_over=False
    init_velocity=6
    snake_x=45
    snake_y=55
    snake_size=15
    velocity_x=0
    velocity_y=0
    food_x= random.randint(20,600)
    food_y= random.randint(20,250)
    fps=50
    score=0
    snake_list=[]
    snake_length=1
    with open("hi.txt","r") as f:
        hiscore=f.read()
    while not exit_game:
        if game_over:
            with open("hi.txt","w") as f:
                f.write(str(hiscore))
            window.fill(white)
            score_screen("Game Over! Press enter to continue",red,300,250 )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game =True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('back.mp3')
                        pygame.mixer.music.play()
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game =True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key == pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x-food_x)<6 and abs (snake_y-food_y)<6:
                score+=10
                food_x= random.randint(20,600)
                food_y= random.randint(20,250)
                snake_length +=5
                if score>int(hiscore):
                    hiscore=score
            window.fill(white)
            window.blit(bg,(0,0))
            score_screen('Score: '+str(score),red,5,5)
            pygame.draw.rect(window,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('over.wav')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>1200 or snake_y<0 or snake_y>550:
                game_over=True
                pygame.mixer.music.load('over.wav')
                pygame.mixer.music.play()
            pygame.draw.rect(window,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(window,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
welcome()

gameloop()