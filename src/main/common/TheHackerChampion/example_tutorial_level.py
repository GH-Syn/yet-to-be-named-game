import pygame
import colors


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

#Load background
background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_0.jpg")
floor = pygame.image.load("src\main/assets/textures/elements/background/placeholder_floor.jpg")
door = pygame.image.load("src/main/assets/textures/elements/doors/door_1_closed.png")

# Set screen dimensions
scale = 10

# Set screen dimensions
screen_width = 1280
screen_height = 800

# Create a screen surface
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
icon = pygame.image.load('src\main/assets/textures\elements\gui\icon\icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Muffin Group")
leftWall = pygame.draw.rect(screen, (0,0,0), (0,0,2,1000), 0)
rightWall = pygame.draw.rect(screen, (0,0,0), (1100,0,2,1000), 0)

#Create Sound
jumpsound = pygame.mixer.Sound("src/main/assets/sounds/jump.wav")
jumpsound.set_volume(0.25)
doorsound = pygame.mixer.Sound("src\main/assets\sounds\door_closing.wav")

# Load character image
character_image = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png").convert_alpha()
introducer_image = pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png")

#Image dimensions
image_width = character_image.get_width()
image_height = character_image.get_height()
character_image = pygame.transform.scale(character_image, (int(image_width * scale), int(image_height * scale)))
door_width = door.get_width()
door_height = door.get_height()
door = pygame.transform.scale(door, (int(door_width * scale), int(door_height * scale)))
int_widht = introducer_image.get_width()
int_height = introducer_image.get_height()
introducer_image = pygame.transform.scale(introducer_image, (int(int_widht * scale), int(int_height * scale)))

# Sizes door: 320, 320

# Set initial position
character_x = 0
character_y = 410

# Set character speed
character_speed = 5

def draw():
    # Draw the character and update the screen
    screen.fill(colors.BLACK)
    screen.blit(background, (0,0))
    screen.blit(floor, (0,730))
    screen.blit(door, (990,410))
    screen.blit(introducer_image, (100, 150))
    if visible == True:
        screen.blit(character_image, (character_x, character_y))
    pygame.display.update()


# Game loop
running = True
jumpvar = -16
doorhandling = 0
visible = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle keyboard input
    keys = pygame.key.get_pressed()
    Spieler = pygame.Rect(character_x, character_y, 40, 80)
    Door = pygame.Rect(990, 410, 40, 80)
    if keys[pygame.K_LEFT] and not Spieler.colliderect(leftWall) and visible == True:
        character_x -= character_speed
    if keys[pygame.K_RIGHT] and not Spieler.colliderect(rightWall) and visible == True:
        character_x += character_speed
    if keys[pygame.K_UP] and jumpvar == -16 and visible == True:
        jumpvar = 15
    if keys[pygame.K_DOWN] and Spieler.colliderect(Door) and visible == True:
        doorhandling = 1

    if jumpvar == 15:
        pygame.mixer.Sound.play(jumpsound)

    if jumpvar >= -15:
        n = 1
        if jumpvar < 0:
            n = -1
        character_y -= (jumpvar**2)*0.17*n
        jumpvar -= 1

    if doorhandling == 1:
        door = pygame.image.load("src/main/assets/textures/elements/doors/door_1_open.png")
        door = pygame.transform.scale(door, (int(door_width * scale), int(door_height * scale)))

    draw()

    if doorhandling == 1:
        pygame.time.wait(500)
        pygame.mixer.Sound.play(doorsound)
        door = pygame.image.load("src/main/assets/textures/elements/doors/door_1_closed.png")
        door = pygame.transform.scale(door, (int(door_width * scale), int(door_height * scale)))
        visible = False
        doorhandling = 0
    clock.tick(60)

# Quit Pygame
pygame.quit()