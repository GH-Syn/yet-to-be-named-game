import pygame
import math

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set screen size
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images
character_img = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png")
character_img=pygame.transform.scale(character_img,(250,250))
screen.blit(character_img,(340,190))
character_rect = character_img.get_rect()
enemy_img = pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png")
enemy_img=pygame.transform.scale(enemy_img,(400,400))
screen.blit(enemy_img,(340,190))

# Set character and enemy starting position
character_x = 50
character_y = 50
enemy_x = 150
enemy_y = 150

# Set enemy speed
enemy_speed = 4
character_img_speed= 5

# Set distance at which enemy and character starts attacking character
attack_distance_enemy_img = 200
attack_distance_character_img= 300

# Set enemy and character attack range
attack_range_enemy_img = 1
attack_range_character_img = 6

# Set character health and attack power
character_health = 500
character_attack_power = 2

# Set enemy health and attack power
enemy_health = 300
enemy_attack_power = 1

# Define function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get character movement and attack input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_img_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_img_speed
    if keys[pygame.K_UP]:
        character_y -= character_img_speed
    if keys[pygame.K_DOWN]:
        character_y += character_img_speed
    if keys[pygame.K_w]:
        if distance_to_enemy< attack_range_character_img:
          enemy_health -= character_attack_power

    
    # Move enemy towards character
    enemy_dx = character_x - enemy_x
    enemy_dy = character_y - enemy_y
    distance_to_character = distance(character_x, character_y, enemy_x, enemy_y)
    distance_to_enemy = distance(enemy_x, enemy_y, character_x, character_y)
    if distance_to_character < attack_distance_enemy_img:
        # If within attack distance, attack character
        if distance_to_character < attack_range_enemy_img:
            character_health -= enemy_attack_power
           # Otherwise, move towards character
        else:
            enemy_dx = enemy_dx / distance_to_character * enemy_speed
            enemy_dy = enemy_dy / distance_to_character * enemy_speed
            enemy_x += enemy_dx
            enemy_y += enemy_dy

    
    # Draw images on screen
    screen.fill((255, 255, 255))
    screen.blit(character_img, (character_x, character_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))


    # Display health bars for character and enemy
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, character_health, 10))
    pygame.draw.rect(screen, (255, 0, 0), (screen_width - 110, 10, enemy_health, 10))

    global colors # Difign Colors
    colors = {
    "WHITE":(255,255,255),
    "RED"  :(255,0,0),
    "GREEN":(0,255,0),
    "BLUE" :(0,0,255),
    "BLACK":(0,0,0)
     }

    # Check if character or enemy health is 0 or below, end game or set changes if true
    if enemy_health <= 0:
     enemy_attack_power = 0
     enemy_speed = 0
     enemy_y = 1000
    if character_health <= 0:
     pygame.quit
     quit()

     draw()   
    clock.tick(80)


    # Update display
    pygame.display.update()
