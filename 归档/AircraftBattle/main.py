import sys
import pygame
import setting

pygame.init()


'主窗口'
screen_image = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_rect = screen_image.get_rect()

pygame.display.set_caption('my game')
'ship'
ship_image = pygame.image.load('images/me2.png')
ship_rect = ship_image.get_rect()
ship_rect.midbottom = screen_rect.midbottom
moving_left = False
moving_right = False

# bullets
bullets =  []

# jisuan
alien_image = pygame.image.load('images/enemy1.png')
alien_image_rect = alien_image.get_rect()
alien_width = alien_image_rect.height
alien_height = alien_image_rect.height
screen_width, screen_height = screen_rect.size
ship_width, ship_height = ship_rect.size
space_x = screen_width - 2 * alien_width
space_y = screen_height - ship_height - 3 * alien_height
column_number = space_x // (2 * alien_width)
line_number = space_y // (2 * alien_height)

print(column_number)
print(line_number)

# 外星人
aliens = pygame.sprite.Group()
for y_number in range(column_number):
    for x_number in range(column_number):
        alien_sprite = pygame.sprite.Sprite()
        alien_sprite.image = pygame.image.load('images/enemy1.png')
        alien_sprite.rect = alien_sprite.image.get_rect()
        alien_sprite.rect.x = alien_width + 2 * alien_width * x_number
        alien_sprite.rect.y = alien_height + 2 * alien_height * y_number
        aliens.add(alien_sprite)


# alian
# aliens = {}
# for y_number in range(line_number):
#     for x_number in range(column_number):
#         alien_image = pygame.image.load('images/enemy1.png')
#         alien_rect = alien_image.get_rect()
#         alien_rect.x = alien_width + 2 * alien_width * x_number
#         alien_rect.y = alien_height + 2 * alien_height * y_number
#         aliens[alien_image] = alien_rect

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                new_bullet_rect = pygame.Rect(0, 0, 5, 15)
                new_bullet_rect.midbottom = ship_rect.midtop
                bullets.append(new_bullet_rect)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    if moving_left and ship_rect.left > screen_rect.left:
        ship_rect.x -= setting.ship_speed
    if moving_right and ship_rect.right < screen_rect.right:
        ship_rect.x += setting.ship_speed

    'hui zhi'
    screen_image.fill(setting.color1)
    screen_image.blit(ship_image, ship_rect)
    for bullet_rect  in bullets:
        pygame.draw.rect(screen_image, setting.color2, bullet_rect)
        bullet_rect.y -= 1
        if bullet_rect.bottom < 0:
            bullets.remove(bullet_rect)
    aliens.draw(screen_image)
    # for key_image, value_rect in aliens.items():
    #     screen_image.blit(key_image, value_rect)

    pygame.display.flip()