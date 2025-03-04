import pygame
import registries.colors

pygame.init()
textfont = pygame.font.SysFont('joystixmonospaceregular', 20)

int10 = textfont.render('Hello!', True, registries.colors.BLACK)
int11 = textfont.render('Nice to see you!', True, registries.colors.BLACK)
int12 = textfont.render('In this game you will find', True, registries.colors.BLACK)
int13 = textfont.render('some nice levels with enemies,', True, registries.colors.BLACK)
int14 = textfont.render('interesting tasks and much more!', True, registries.colors.BLACK)
int15 = textfont.render('Press Enter', True, registries.colors.BLACK)

int20 = textfont.render('Before you start,', True, registries.colors.BLACK)
int21 = textfont.render('you should learn how to move and act.', True, registries.colors.BLACK)
int22 = textfont.render('I will explain this now', True, registries.colors.BLACK)
int23 = textfont.render('Press Enter', True, registries.colors.BLACK)

int30 = textfont.render('First we learn how to walk.', True, registries.colors.BLACK)
int31 = textfont.render('To walk forward press RIGHT or d', True, registries.colors.BLACK)
int32 = textfont.render('Great!', True, registries.colors.BLACK)
int33 = textfont.render('To walk back press LEFT or a', True, registries.colors.BLACK)
int34 = textfont.render('Well done!', True, registries.colors.BLACK)

int40 = textfont.render('If you want to be faster', True, registries.colors.BLACK)
int41 = textfont.render('you can press SHIFT to sprint.', True, registries.colors.BLACK)
int42 = textfont.render('That`s faster, right?', True, registries.colors.BLACK)

int50 = textfont.render('Sometimes you have to jump.', True, registries.colors.BLACK)
int51 = textfont.render('For this press UP or SPACE.', True, registries.colors.BLACK)
int52 = textfont.render('Nice jump!', True, registries.colors.BLACK)

int60 = textfont.render('Now you know how to move.', True, registries.colors.BLACK)
int61 = textfont.render('But of course there are some enemies.', True, registries.colors.BLACK)
int62 = textfont.render('So you have to attack them.', True, registries.colors.BLACK)
int63 = textfont.render('For this press F', True, registries.colors.BLACK)
int64 = textfont.render('Try it out on this oger!', True, registries.colors.BLACK)
int65 = textfont.render('Good job!', True, registries.colors.BLACK)

int70 = textfont.render('Now you got the controls.', True, registries.colors.BLACK)
int71 = textfont.render('If you are ready go to the door.', True, registries.colors.BLACK)
int72 = textfont.render('This door will bring you to the castle.', True, registries.colors.BLACK)
int73 = textfont.render('And now press DOWN or s', True, registries.colors.BLACK)
int74 = textfont.render('to start the game.', True, registries.colors.BLACK)
int75 = textfont.render('Good luck!', True, registries.colors.BLACK)


Info1 = 'on'
Info2 = 'off'
Info3_1 = 'off'
Info3_2 = 'off'
Info4_1 = 'off'
Info4_2 = 'off'
Info5 = 'off'
Info6 = 'off'
Info7 = 'off'


def introduction(running, jumpvar, doorhandling, visible, standing, walking, jumping, character_speed, character_x, character_y, leftWall, rightWall, screen):

    pygame.init()
    keys = pygame.key.get_pressed()
    Spieler = pygame.Rect(character_x, character_y, 40, 80)
    Door = pygame.Rect(990, 410, 40, 80)

    global Info1, Info2, Info3_1,Info3_2, Info4_1, Info4_2, Info5, Info6, Info7


    if Info1 == 'on':
        screen.blit(int10, (100,100))
        screen.blit(int11, (100,125))
        screen.blit(int12, (100,150))
        screen.blit(int13, (100,175))
        screen.blit(int14, (100,200))
        screen.blit(int15, (100,250))
        if keys[pygame.K_RETURN]:
            Info1 = 'off'
            Info2 = 'on'


    if Info2 == 'on':
        screen.blit(int20, (100,100))
        screen.blit(int21, (100,125))
        screen.blit(int22, (100,150))
        screen.blit(int23, (100,175))
        if keys[pygame.K_RETURN]:
            Info2 = 'off'
            Info3_1 = 'on'

    
    if Info3_1 == 'on':
        screen.blit(int30, (100,100))
        screen.blit(int31, (100,125))
        if keys[pygame.K_RIGHT] and not Spieler.colliderect(rightWall) and visible == True:
            standing = False
            walking = True
            print(character_x)
            character_x += character_speed
            print(character_x)
        elif keys[pygame.K_d] and not Spieler.colliderect(rightWall) and visible == True:
            standing = False
            walking = True
            character_x += character_speed
        else:
            standing = True
            walking = False
        if character_x >= 300:
            Info3_1 = 'off'
            Info3_2 = 'on'
    
    if Info3_2 == 'on':
        screen.blit(int30, (100,100))
        screen.blit(int31, (100,125))
        screen.blit(int32, (100,150))
        screen.blit(int33, (100,175))
        if keys[pygame.K_LEFT] and not Spieler.colliderect(leftWall) and visible == True:
            standing = False
            walking = True
            character_x -= character_speed
        elif keys[pygame.K_a] and not Spieler.colliderect(leftWall) and visible == True:
            standing = False
            walking = True
            character_x -= character_speed
        else:
            standing = True
            walking = False
        if character_x <= 100:
            screen.blit(int34, (100,200))
            pygame.time.wait(200)
            Info3_2 = 'off'
            Info4 = 'on'

        
        if Info4_1 == 'on':
            screen.blit(int40, (100,100))
            screen.blit(int41, (100,125))
            if keys[pygame.K_LSHIFT] and keys[pygame.K_a] and visible == True:
                character_speed = 7.5
            elif keys[pygame.K_LSHIFT] and keys[pygame.K_d] and visible == True:
                character_speed = 7.5
            elif keys[pygame.K_RSHIFT] and keys[pygame.K_d] and visible == True:
                character_speed = 7.5
            elif keys[pygame.K_RSHIFT] and keys[pygame.K_a] and visible == True:
                character_speed = 7.5
            elif keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT] and visible == True:
                character_speed = 7.5
            elif keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT] and visible == True:
                character_speed = 7.5
            elif keys[pygame.K_RSHIFT] and keys[pygame.K_RIGHT] and visible == True:
                character_speed = 7.5
            elif keys[pygame.K_RSHIFT] and keys[pygame.K_LEFT] and visible == True:
                character_speed = 7.5
            else:
                character_speed = 5