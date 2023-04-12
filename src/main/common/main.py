import pygame
import registries.colors
import registries.animations
import registries.elements
import registries.buttons

#pygame initialization
pygame.init()
class Player:
    #Initial Player attribute assignment
    def __init__(currentImage):
        Player.defaultSpeed = 10
        Player.jumpsound = pygame.mixer.Sound("src/main/assets/sounds/jump.wav")
        Player.jumpsound.set_volume(0.25)
        Player.speed = Player.defaultSpeed
        Player.jumpvar = -16 #Important for jumping calculation
        Player.facingRight = True
        Player.facingLeft = False
        Player.standing = True
        Player.jumping = False
        Player.walking = False
        Player.collidingLeft = False
        Player.collidingRight = False
        Player.rect = pygame.Rect((800, 562),(100, 200)) # Create the players hitbox
        Player.animationFrameUpdate = 1
        Player.debuggingMode = False
        Player.visible = True
        Player.locked = False
        Player.debuggingMenu = False
        Player.test = False
        Player.flying = 0
        Player.colliding = 0
        Player.allowJump = True

    def keybinds(self,camera_pos):
        global player_x
        global player_y
        self.doorhandling = 0 #Door mechanics
        player_x = self.rect.x #Camera following the player
        player_y = self.rect.y

        player_x, player_y = camera_pos #Assign variables to the camera position

        key = pygame.key.get_pressed() #Receive keyboard input
        if key[pygame.K_UP] and Player.jumpvar == -16 and Player.visible == True and Player.locked == False and Player.allowJump == True: #Jumping
            Player.jumpvar = 14.3
        elif key[pygame.K_SPACE] and Player.jumpvar == -16 and Player.visible == True and Player.locked == False and Player.allowJump == True: #Alternative jumping keybind
            Player.jumpvar = 14.3

        if Player.jumpvar == 14.3: #Play jump sound when the player jumps
            pygame.mixer.Sound.play(Player.jumpsound)

        if Player.jumpvar >= -15: #Jumping movement
            n = 1
            if Player.jumpvar < 0:
                n = -1
            self.rect.y -= (Player.jumpvar**2)*0.17*n
            Player.jumping = True
            Player.jumpvar -= 1
        else:
            Player.jumpvar = -16
            Player.jumping = False

        if key[pygame.K_RIGHT] and Player.visible == True and Player.collidingRight == True and Player.locked == False and Player.locked == False: #Player walking
            Player.facingLeft = False
            Player.facingRight = True
        elif key[pygame.K_RIGHT] and Player.collidingRight == False and Player.locked == False:
            Player.facingLeft = False
            Player.facingRight = True
            Player.standing = False
            self.rect.x += Player.speed
        else:
            Player.standing = True
            Player.walking = False

        if key[pygame.K_LEFT] and Player.visible == True and Player.collidingLeft == True and Player.locked == False: #Player walking
            Player.facingLeft = True
            Player.facingRight = False
        elif key[pygame.K_LEFT] and Player.collidingLeft == False and Player.locked == False:
            Player.facingLeft = True
            Player.facingRight = False
            Player.standing = False
            self.rect.x -= Player.speed
        else:
            Player.standing = True
            Player.walking = False

        if Player.collidingLeft == True:
            print("colliding left")
        if Player.collidingRight == True:
            print("colliding right")

        #Debug mode to help developers
        if key[pygame.K_d] and Player.debuggingMode == False:
            pygame.time.wait(200)
            Player.debuggingMode = True
            print("e")
        elif key[pygame.K_d] and Player.debuggingMode == True and Player.debuggingMenu == False:
            pygame.time.wait(200)
            Player.debuggingMode = False
            print("a")

        if key[pygame.K_0] and Player.debuggingMode == True and Player.debuggingMenu == False:
            pygame.time.wait(200)
            Player.locked = True
            Player.debuggingMenu = True
            print("e")
        elif key[pygame.K_0] and Player.debuggingMode == True:
            pygame.time.wait(200)
            Player.locked = False
            Player.debuggingMenu = False
            print("o")

        if key[pygame.K_DOWN] and Player.visible == True and registries.elements.registerElements.colliding == False and Player.debuggingMode == True and Player.locked == False and Player.flying == 1:
            Player.standing = False
            Player.facingLeft = False
            Player.facingRight = True
            self.rect.y += Player.speed 
        else:
            Player.standing = True
            Player.walking = False
            
        if key[pygame.K_u] and Player.visible == True and registries.elements.registerElements.colliding == False and Player.debuggingMode == True and Player.locked == False and Player.flying == 1:
            Player.standing = False
            Player.facingLeft = False
            Player.facingRight = True
            self.rect.y -= Player.speed 
        else:
            Player.standing = True
            Player.walking = False

        if key[pygame.K_p] and Player.debuggingMode == True:
            print(Player.rect.x)
    
    #End of debugging mode functions

        if key[pygame.K_LEFT] and Player.visible == True and Player.locked == False or key[pygame.K_RIGHT] and Player.visible == True  and Player.locked == False: #Walking animations
            Player.walking = True

        if Player.walking == True and key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]: #Sprinting
            Player.speed = 18
            Player.countUp = 2
        else:
            Player.speed = Player.defaultSpeed

        return (-self.rect.x + 680, -self.rect.y + 450) # Return new player position
    
    def render(self,screen): #Player and player hitbox rendering
        if Player.visible == True:
            Player.currentSprite = pygame.transform.scale(Player.currentSprite,(32 * 8,32 * 8))
            screen.blit(self.currentSprite,(self.rect.x - 75,self.rect.y-50)) #Drawing the player to the screen
            if Player.debuggingMode == True:
                pygame.draw.rect(screen, (0, 255, 0), Player.rect, 4) #Drawing the hitbox to the screen	

    def renderDebugMenu(self):
        if Player.debuggingMenu == True:
            pygame.draw.rect(screen, registries.colors.BLUISH_GRAY, debug_menu, 10000)
            if toggleAdvMove.drawToggle(screen):
                if Player.flying > 1:
                    Player.flying = 0
                Player.flying += 1
                if Player.flying == 1:
                    print("selected")
                if Player.flying == 2:
                    print("not selected") 
            screen.blit(toggleAdvMoveText, (100, 135))
            if toggleCollisions.drawToggle(screen):
                if Player.colliding > 1:
                    Player.colliding = 0
                Player.colliding += 1
                if Player.colliding == 1:
                    print("selected")
                if Player.colliding == 2:
                    print("not selected") 
            screen.blit(toggleCollisionsText, (80, 235))

        
    def collisions(self):
        #Wall collisions, do not delete!!!!
        if Player.rect.x < 700:
            Player.collidingLeft = True
        else:
            Player.collidingLeft = False

#Loading element textures
placeholder = registries.elements.registerElements("environment/blocks/cobble", 5)
wooden_sign = registries.elements.registerElements("environment/blocks/wooden_sign", 5)
tree_stump = registries.elements.registerElements("environment/blocks/tree_stump", 5)
placeholder3 = registries.elements.registerElements("environment/blocks/cobble", 5)

grassElement = pygame.image.load("src\main/assets/textures\elements\Environment/blocks\grass_dirt.png")
grassElementScaled = pygame.transform.scale(grassElement, (grassElement.get_width() * 3, grassElement.get_width() * 3))
dirtElement = pygame.image.load("src\main/assets/textures\elements\Environment/blocks\dirt.png")
dirtElementScaled = pygame.transform.scale(dirtElement, (dirtElement.get_width() * 3, dirtElement.get_width() * 3))
cobbleElement = pygame.image.load("src\main/assets/textures\elements\Environment/blocks\cobble.png")
cobbleElementScaled = pygame.transform.scale(cobbleElement, (cobbleElement.get_width() * 3, cobbleElement.get_width() * 3))

print(tree_stump.get_width())

#Loading element hitboxes
placeholder_hitbox = pygame.Rect((400, 750),(int(placeholder.get_width()), int(placeholder.get_height())))
tree_stump_hitbox = pygame.Rect((800, 730),(int(placeholder.get_width()), int(placeholder.get_width())))

#Loading floor and background
floor = pygame.image.load("src\main/assets/textures\levels\grass_floor.png")
floor_width = floor.get_width()
floor_height = floor.get_height()
floor = pygame.transform.scale(floor, (int(floor_width * 8), int(floor_height * 8)))
floor_hitbox = pygame.Rect((0, 850), (floor_width * 8, floor_height * 8))

font = pygame.font.SysFont('joystixmonospaceregular', 25)
text = font.render("Press 0 to open/close the debug menu", True, registries.colors.DARK_ORANGE)

debug_menu = pygame.Rect((70, 70), (300, 400))

toggleCollisionsText = font.render("collides", True, registries.colors.BLACK)
toggleCollisions = registries.buttons.registerButton("toggle", 300, 250,  12.0, "", registries.colors.BLACK, "")

toggleAdvMoveText = font.render("flying", True, registries.colors.BLACK)
toggleAdvMove = registries.buttons.registerButton("toggle", 300, 150,  12.0, "", registries.colors.BLACK, "")

screen_width = 1000
screen_height = 800

"""game_map = [[0,0,0,2,2,2,0,0,2,2,2,2,0,0,2,2,2,2,0],
            [0,0,1,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0],
            [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
            [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
            [2,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,2,2,2,2,0,0,2,2,2,2,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
            [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
            [0,0,0,2,2,2,0,2,2,2,2,2,0,0,2,2,2,2,0]]""" #Lovely css map

game_map = [[00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def Main(screen,clock):
    world = pygame.Surface((8000,8000)) # Create Map
    player = Player() # Initialize Player Class
    camera_pos = (0, 0) #camera starting position

    #values for animation calculation
    idleValue = 0
    walkingValue = 0

    while True:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or(event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                return
        #idle animation calculation
        if idleValue >= len(registries.animations.idle_sprite):
            idleValue = 0

        #loading the idle animation
        Player.currentSprite = registries.animations.idle_sprite[idleValue]
        
        if walkingValue >= len(registries.animations.walking_sprite):
            walkingValue = 0
        
        #Player movement
        camera_pos = player.keybinds(camera_pos) 

        #Movement animation rendering
        if Player.walking == True:
            Player.currentSprite = registries.animations.walking_sprite[walkingValue]
        if Player.facingLeft == True:
            Player.currentSprite = pygame.transform.flip(Player.currentSprite, True, False)

        #Render background
        world.fill(registries.colors.AQUA)

        #Fill the background outside of the map
        screen.fill(registries.colors.AQUA)

        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile != 00:
                    tileRect = pygame.Rect(x * dirtElementScaled.get_width(), y * dirtElementScaled.get_width(), dirtElementScaled.get_width(), dirtElementScaled.get_width())
                    tile_rects.append(tileRect)
                if tile == 1:
                    world.blit(dirtElementScaled, (tileRect.x, tileRect.y))
                    pygame.draw.rect(world, (255, 255, 255), tileRect, 2)
                if tile == 2:
                    world.blit(grassElementScaled, (tileRect.x, tileRect.y))
                    pygame.draw.rect(world, (255, 255, 255), tileRect, 2)
                if tile == 3:
                    world.blit(cobbleElementScaled, (tileRect.x, tileRect.y))
                    pygame.draw.rect(world, (255, 255, 255), tileRect, 2)
                x += 1
            y += 1

        if key[pygame.K_9]:
            Player.rect.y = tileRect.y
            Player.rect.x = tileRect.x

        #Render the player
        player.render(world)
        
        player.collisions()

        #Render the map to the screen
        screen.blit(world, (player_x,player_y))

        if Player.debuggingMode == True:
            screen.blit(text, (320, 30))

        #Rendering the debug menu
        player.renderDebugMenu()
        
        print(str(Player.rect.x) + ", " + str(Player.rect.y))
        print(str(tileRect.x) + ", " + str(tileRect.y))

        #Idle animations
        if Player.standing == True:
            idleValue += 1
        if Player.walking == True:
            walkingValue += Player.animationFrameUpdate

        clock.tick(200)
        pygame.display.flip()

if __name__ in "__main__":
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("CameraView")
    clock = pygame.time.Clock()
    Main(screen,clock) # Run Main Loop