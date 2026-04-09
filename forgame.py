import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


images = [
    pygame.image.load('newshaxter/player_right_1.png').convert_alpha(),
    pygame.image.load("newshaxter/player_right_2.png").convert_alpha(),
    pygame.image.load("newshaxter/player_right_3.png").convert_alpha(),
    pygame.image.load("newshaxter/player_right_4.png").convert_alpha(),
]


button_rect = pygame.Rect(373, 300, 100, 50)
button_color = (100, 100, 100)
font = pygame.font.SysFont("Arial", 24)

index = 0
play = False

running = True
while running:
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                play = True
                index = 0


    if play:
        index += 1
        if index >= len(images):
            index = 0


    screen.blit(images[index], (250, 150))


    mouse_pos = pygame.mouse.get_pos()
    current_color = (150, 150, 150) if button_rect.collidepoint(mouse_pos) else button_color
    pygame.draw.rect(screen, current_color, button_rect)


    text = font.render("PLAY!", True, "blue")

    screen.blit(text, (button_rect.x + 20, button_rect.y + 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()




