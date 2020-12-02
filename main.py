# Space Invaders is a popular video game created by Tomohiro Nishikado in 1978. 
# It was manufactured and sold by Taito in Japan. 
# Space Invaders is a shooting game  in which aliens come to attack earth and human beings
# use spaceship for shooting them down.


import pygame, sys
import random
import math

# Initialize  pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load("images/background.png")

# Title and icon
pygame.display.set_caption("Cybersquare - Space invaders")
icon = pygame.image.load("images/cs_logo.png")
pygame.display.set_icon(icon)

# Player spaceship
playerImg = pygame.image.load("images/spaceship.png")
playerImg = pygame.transform.scale(playerImg, (64, 128))
playerX = 370
playerY = 480
playerX_change = 0


# Player enemy
enemyImg = pygame.image.load("images/enemy1.png")
enemyImg = pygame.transform.scale(enemyImg, (64, 64))
enemyX = random.randint(0,735)
enemyY = random.randint(100,200)
enemyX_change = 1
enemyY_change = 30

# Bullet
bulletImg = pygame.image.load("images/bullet.png")
bulletImg = pygame.transform.scale(bulletImg, (32, 32))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10 #Speed of the bullet
bullet_state = "ready" # Ready - Can't see bullet, Fire - Bullet is moving

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    display_score = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(display_score, (x,y))


def player(x, y):
    screen.blit(playerImg,(x, y))


def emeny(x, y):
    screen.blit(enemyImg,(x, y))


def fire_bullet(x, y): # Movement of bullet
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16, y+10))


# Check bullet hits enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()


        # Handle key strokes left and right
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                print("Space bar pressed")
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystorke has been released")
                playerX_change = 0
    
    playerX += playerX_change

    # Set the movement limit to size of the window
    if playerX < 0: # Move the player to zero when the player goes beyond left edge
        playerX = 0
    elif playerX > 736: # Move the player inside the screen when the player goes beyond right edge
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change
    if enemyX < 0:
        enemyX_change = 1  # Change the direction of movement to right when reaches at left side
        enemyY += enemyY_change # Change Y position of the enemy
    elif enemyX > 736:
        enemyX_change = -1 # Change the direction of movement to left when reaches at right side
        enemyY += enemyY_change

    # Bullet movement
    if bulletY < 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    # Reset the bullet and update score after hitting the emeny
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(100,200)

    # show the  score
    show_score(textX, textY)

    # Update positions
    player(playerX, playerY)
    emeny(enemyX, enemyY)
    pygame.display.update()


