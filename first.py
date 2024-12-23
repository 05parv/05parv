import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Set up ball
ball_color = (255, 0, 0)
ball_radius = 20
ball_pos = [width // 2, height // 2]
ball_speed = [3, 3]

# Set up font for displaying points
font = pygame.font.Font(None, 36)

# Initialize points counter
points = 0

# Run the game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_pos[0] += ball_speed[45
                              ]
    ball_pos[1] += ball_speed[1]

    # Bounce the ball off the walls and update points
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_speed[0] = -ball_speed[0]
        points += 1
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_speed[1] = -ball_speed[1]
        points += 1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # Render the points text
    points_text = font.render(f"Points: {points}", True, (255, 255, 255))
    screen.blit(points_text, (10, height - 40))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
