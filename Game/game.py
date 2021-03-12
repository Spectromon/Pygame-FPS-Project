import pygame as pg
import random
#init
pg.init()

#Functions
def check_collision(enemies, health):
    for enemy in enemies:
        enemy_index = enemies.index(enemy)
        if character_rect.colliderect(enemy):
            health -= 1
            del enemies[enemy_index]            
        
    return health

def check_game(health):
    if health <= 0:
        return False
    else:
        return True

def check_shot(enemies, bullets, score):
    for enemy in enemies:
        enemy_index = enemies.index(enemy)
        for bullet in bullets:
            bullet_index = bullets.index(bullet)
            if enemy.colliderect(bullet):
                del bullets[bullet_index]
                del enemies[enemy_index]
                score += 1
    
    return score
                

def create_enemy():
    random_enemy_x = random.choice(enemy_x)
    ychoice = (20, 470)
    random_enemy_y = random.choice(ychoice)
    if random_enemy_x == 100 or random_enemy_x == 450:
        random_enemy_y = random.choice(enemy_y)
    enemy = enemy_surface.get_rect(center = (random_enemy_x, random_enemy_y))

    return enemy

def move_enemy(enemies):
    for enemy in enemies:
        if character_rect.centerx < enemy.centerx:
            enemy.centerx -= 1
        elif character_rect.centerx > enemy.centerx:
            enemy.centerx +=1

    for enemy in enemies:
        if character_rect.centery < enemy.centery:
            enemy.centery -= 1
        elif character_rect.centery > enemy.centery:
            enemy.centery +=1
    
    return enemies
def draw_enemy(enemies):
    for enemy in enemies:
        win.blit(enemy_surface, enemy)
def create_bullet():
    bullet = bullet_surface.get_rect(center = (character_rect.centerx, character_rect.centery))
    return bullet

def draw_bullet(bullets):
    for bullet in bullets:
        win.blit(bullet_surface, bullet)

def move_bullets_up(bullets):
    for bullet in bullets:
        bullet.centery -= 5
    
    return bullets
def move_bullets_left(bullets):
    for bullet in bullets:
        bullet.centerx -= 5
    
    return bullets
def move_bullets_down(bullets):
    for bullet in bullets:
        bullet.centery += 5
    
    return bullets
def move_bullets_right(bullets):
    for bullet in bullets:
        bullet.centerx += 5
        
    return bullets

def HUD_display():
    magazine_surface = game_font.render('MAG: ' + str(magazine), True, (0,0,0))
    magazine_rect = magazine_surface.get_rect(center = (450, 30))
    win.blit(magazine_surface,magazine_rect)

    # if health == 5:
    #     colour = (0, 128, 0)
    # elif health == 4:
    #     colour = (127,255, 0)
    # elif health == 3:
    #     colour = (255,255, 0)
    # elif health == 2:
    #     colour = (255, 127, 0)
    # elif health == 1:
    #     colour = (255, 0, 0)
    # else:
    #     colour = (0,255,255)
    health_surface = game_font.render("HP: " + str(health), True, (0,0,0))
    health_rect = health_surface.get_rect(center = (50,30))
    win.blit(health_surface, health_rect)


    score_surface = game_font.render('Score: ' + str(score), True, (0,0,0))
    score_rect = score_surface.get_rect(center = (435, 60))
    if score > 10:
        score_rect = score_surface.get_rect(center = (430, 60))
    if score > 99:
        score_rect = score_surface.get_rect(center = (425, 60))
    win.blit(score_surface, score_rect)

def gameOver():
    gameOver_surface = game_font.render('GAME OVER', True, (0,255,255))
    gameOver_rect = gameOver_surface.get_rect(center = (250,225))
    win.blit(gameOver_surface, gameOver_rect)

    score_surface = game_font.render('Score: ' + str(score), True, (0,255,255))
    score_rect = score_surface.get_rect(center = (250, 255))
    win.blit(score_surface, score_rect)

def gameStartup():
    gameStart_surface = game_font.render('PRESS SPACE\n TO START', True, (0,255,255))
    gameStart_rect = gameStart_surface.get_rect(center = (250,225))
    win.blit(gameStart_surface, gameStart_rect)

#Set Variables
game_font = pg.font.Font('gameFont.ttf',30)
nRows = 500
nColumns = 500
FPS = 60
fpsClock = pg.time.Clock()

#Game Variables
character_movementx = 0
character_movementy = 0

empty_clip_sound = pg.mixer.Sound('gun_empty.mp3')

enemy_list = []
SPAWNENEMY = pg.USEREVENT
pg.time.set_timer(SPAWNENEMY, 1200)
enemy_x = [50,  200, 300, 350, 400, 450]
enemy_y = [100, 150, 200, 300, 350, 400]



win = pg.display.set_mode((nRows, nColumns))
pg.display.set_caption("Shooting Game")

#Background
bg = pg.image.load('bg.png')

#Character
character_surface = pg.transform.scale2x(pg.image.load('character.png'))
character_surface = pg.transform.scale2x(character_surface)
character_rect = character_surface.get_rect(center = (100,100))

#Bullet
bullet_surface = pg.image.load('Bullet.png')
bullet_rect = bullet_surface.get_rect(center = (character_rect.centerx, character_rect.centery))

bullet_list_up = []
bullet_list_left = []
bullet_list_down = []
bullet_list_right = []

magazine = 8

#Enemy
enemy_surface = pg.transform.scale2x(pg.image.load('enemy.png'))


#Score
score = 99
health = 5
gameActive = False
gameStart = True
run = True

while run:
    win.blit(bg, (0,0))
    if gameStart == True:
        gameStartup()
    if gameActive == True:
        keys = pg.key.get_pressed()
        health = check_collision(enemy_list, health)
        gameActive = check_game(health)
        score = check_shot(enemy_list, bullet_list_up, score)
        score = check_shot(enemy_list, bullet_list_left, score)
        score = check_shot(enemy_list, bullet_list_down, score)
        score = check_shot(enemy_list, bullet_list_right, score)
        #Character Movement
        if keys[pg.K_w]:
            if character_movementy != 0:
                character_movementy = 0
            else:                
                character_movementy -= 2
        if keys[pg.K_s]:
            if character_movementy != 0:
                character_movementy = 0
            else:                
                character_movementy += 2
        if keys[pg.K_a]:
            if character_movementx != 0:
                character_movementx = 0
            else:                
                character_movementx -= 2
        if keys[pg.K_d]:
            if character_movementx != 0:
                character_movementx = 0
            else:                
                character_movementx += 2


        #Character Movement Calculation
        if character_movementx != 0:
            character_rect.centerx += character_movementx
            if character_rect.centerx >= 500-45:
                character_rect.centerx = 500-45
            if character_rect.centerx <= 0 + 45:
                character_rect.centerx = 0 + 45

        if character_movementy != 0:
            character_rect.centery += character_movementy
            if character_rect.centery >= 500-45:
                character_rect.centery = 500-45
            if character_rect.centery <= 0 + 45:
                character_rect.centery = 0 + 45
        win.blit(character_surface, character_rect)
        character_movementx = 0
        character_movementy = 0

        #Bullet Calculation:
        bullet_list_up = move_bullets_up(bullet_list_up)
        bullet_list_left = move_bullets_left(bullet_list_left)
        bullet_list_down = move_bullets_down(bullet_list_down)
        bullet_list_right = move_bullets_right(bullet_list_right)

        #Drawing Bullets
        #Until I figure out how to do this in 1 func, I'll keep as 4, as it checks each frame.
        draw_bullet(bullet_list_up)
        draw_bullet(bullet_list_left)
        draw_bullet(bullet_list_down)
        draw_bullet(bullet_list_right)


        #Enemy
        enemy_list = move_enemy(enemy_list)
        draw_enemy(enemy_list)



        #Magazine and Score
        HUD_display()

    elif not gameActive and not gameStart:
        gameOver()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWNENEMY:
            enemy_list.append(create_enemy())
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and gameStart:
                gameStart = False
                health = 5
                enemy_list.clear()
                bullet_list_up.clear()
                bullet_list_left.clear()
                bullet_list_right.clear()
                bullet_list_down.clear()
                character_rect.center = (100,100)
                score = 0
                magazine = 8
                gameActive = True
            if event.key == pg.K_SPACE and not gameActive:
                health = 5
                enemy_list.clear()
                bullet_list_up.clear()
                bullet_list_left.clear()
                bullet_list_right.clear()
                bullet_list_down.clear()
                character_rect.center = (100,100)
                score = 0
                magazine = 8
                gameActive = True
            if magazine > 0:
                if event.key == pg.K_UP:
                    bullet_list_up.append(create_bullet())
                    magazine -= 1
                if event.key == pg.K_LEFT:
                    bullet_list_left.append(create_bullet())
                    magazine -= 1
                if event.key == pg.K_DOWN:
                    bullet_list_down.append(create_bullet())
                    magazine -= 1
                if event.key == pg.K_RIGHT:
                    bullet_list_right.append(create_bullet())
                    magazine -= 1
            if magazine <= 0:
                if event.key == pg.K_UP or event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_DOWN:
                    empty_clip_sound.play()
                
                if event.key == pg.K_r:
                    magazine = 8





    

    pg.display.update()
    fpsClock.tick(FPS)
pg.quit()
