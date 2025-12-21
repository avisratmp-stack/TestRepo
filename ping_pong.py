import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 15
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping Pong Game")
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.speed = 6
        self.score = 0

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < WINDOW_HEIGHT - self.height:
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.dx = 5
        self.dy = 3

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off top and bottom walls
        if self.y <= 0 or self.y >= WINDOW_HEIGHT - BALL_SIZE:
            self.dy *= -1

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, BALL_SIZE, BALL_SIZE))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BALL_SIZE, BALL_SIZE)

    def check_paddle_collision(self, paddle):
        if self.get_rect().colliderect(paddle.get_rect()):
            self.dx *= -1
            # Add some variation based on where the ball hits the paddle
            hit_pos = (self.y - paddle.y) / paddle.height
            self.dy = (hit_pos - 0.5) * 10

def draw_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def main():
    # Create game objects
    left_paddle = Paddle(30, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    right_paddle = Paddle(WINDOW_WIDTH - 30 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()

    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys
        keys = pygame.key.get_pressed()

        # Left paddle controls (W/S)
        if keys[pygame.K_w]:
            left_paddle.move_up()
        if keys[pygame.K_s]:
            left_paddle.move_down()

        # Right paddle controls (UP/DOWN arrows)
        if keys[pygame.K_UP]:
            right_paddle.move_up()
        if keys[pygame.K_DOWN]:
            right_paddle.move_down()

        # Move ball
        ball.move()

        # Check paddle collisions
        ball.check_paddle_collision(left_paddle)
        ball.check_paddle_collision(right_paddle)

        # Check scoring
        if ball.x <= 0:
            right_paddle.score += 1
            ball.reset()
        elif ball.x >= WINDOW_WIDTH - BALL_SIZE:
            left_paddle.score += 1
            ball.reset()
            ball.dx *= -1  # Serve to the right

        # Drawing
        screen.fill(BLACK)

        # Draw center line
        for i in range(0, WINDOW_HEIGHT, 20):
            pygame.draw.rect(screen, GRAY, (WINDOW_WIDTH // 2 - 2, i, 4, 10))

        # Draw game objects
        left_paddle.draw()
        right_paddle.draw()
        ball.draw()

        # Draw scores
        draw_text(str(left_paddle.score), 48, WINDOW_WIDTH // 4, 50)
        draw_text(str(right_paddle.score), 48, WINDOW_WIDTH * 3 // 4, 50)

        # Draw controls hint
        draw_text("W/S: Left Paddle    UP/DOWN: Right Paddle    ESC: Quit", 24, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 30)

        # Update display
        pygame.display.flip()

        # Check for ESC to quit
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
