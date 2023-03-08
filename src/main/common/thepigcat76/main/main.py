import pygame
from colors import *
import animations

class main():
    #Pygame initialization
    pygame.init()
    #Setup for fps
    Clock = pygame.time.Clock()

    #Loading world elements
    background = pygame.image.load("src/main/assets/elements/background/hallway.jpg")
    floor = pygame.image.load("src\main/assets/elements/background/floor.jpg")
    door_closed = pygame.image.load("src\main/assets\elements\doors\door_1_closed.png")
    door_open = pygame.image.load("src\main/assets\elements\doors\door_1_open.png")

    #Screen dimensions
    screen_width = 1280
    screen_height = 800

    #Loading utility assets
    icon = pygame.image.load('src/main/assets/gui/icon/icon.png')
    
    #Setting up the gui
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Muffin Group")
    #pygame.display.is_fullscreen might be helpful in the future

    #Loading assets
    character_image = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1.png").convert_alpha() #Makes the background invisible
    character_image_inverted = pygame.transform.flip(character_image, True, False)
    jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
    doorsound = pygame.mixer.Sound("src\main/assets\sounds\entities\Door_Closing.wav")
    #Dynamic images
    currentSprite = character_image
    currentDoorSprite = door_closed  

    #Assigning variables
    #Character dimensions
    characterWidth = 32
    characterHeight = 32
    
    #Art scale
    scale = 10

    # Set initial position
    character_x = 150
    character_y = 410
    
    # Set character speed
    character_speed = 5
    
    #Values for animations
    IdleValue = 0
    WalkingValue = 0
    

    #Character attributes
    jumpvar = -16
    doorhandling = 0
    visible = True
    standing = True
    walking = False
    jumping = False

    #Image dimensions
    image_width = character_image.get_width()
    image_height = character_image.get_height()

    #Door dimensions
    door_width = door_closed.get_width()
    door_height = door_closed.get_height()

    #Camera positions
    cameraPos = (192,192)

    #Physics, still requires a lot of work
    leftWall = pygame.draw.rect(screen, (0,0,0), (0,0,2,1000), 0)
    rightWall = pygame.draw.rect(screen, (0,0,0), (1100,0,2,1000), 0)

    #Scaling images
    character_image = pygame.transform.scale(character_image, (int(image_width * scale), int(image_height * scale)))
    character_image_inverted = pygame.transform.scale(character_image_inverted (int(image_width * scale), int(image_height * scale)))
    door_closed = pygame.transform.scale(door_closed, (int(door_width * scale/2), int(door_height * scale/2)))
    door_open = pygame.transform.scale(door_open, (int(door_width * scale/2), int(door_height * scale/2)))
    
    def draw():
        # Draw the character and update the screen
        main.screen.fill(COLORS.BLACK)
        main.screen.blit(main.background, (0,0))
        main.screen.blit(main.floor, (0,730))
        main.screen.blit(main.currentDoorSprite, (990,420))   
        pygame.display.update

    running = True    
    #Main game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            #Receive closing attempt
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        # Handle keyboard input
        keys = pygame.key.get_pressed()
        #Player hitbox
        player = pygame.Rect(character_x, character_y, 40, 80)
        door = pygame.Rect(990, 410, 40, 80)