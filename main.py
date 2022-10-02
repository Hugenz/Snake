import pygame, time, random


# Fenetre
dimensions = largeur, hauteur = 900, 600
couleur_fond = 0, 0, 0

# couleur du serpent et de la pomme
couleur_snake = 0, 255, 0
couleur_pomme = 255, 0, 0

# vitesse du serpent
blocsec = 10

# timer pour fixer la vitesse du serpent
chrono = time.time()
clock = pygame.time.Clock()

# variable score
score = 0

# position de la pomme
pomme_position_x = random.randrange(0, largeur,30)
pomme_position_y = random.randrange(0, hauteur,30)

# position du serpent
snake_position_y = 300
snake_position_x = 450

# direction du serpent
snake_direction_x = 0
snake_direction_y = 0


# creer une liste de coordonnées pour le snake
position_snake = []

# creer une liste pour la taille du snake
taille_snake = 1


## pygame ##
# initialisation de pygame
pygame.init()
# variable pour la fenetre avec les dimensions
fenetre = pygame.display.set_mode((dimensions))
# titre de la fenetre
pygame.display.set_caption("Snake by Hugenz")
pygame.display.flip()



#####################################################################################################
                                  # BOUCLE PRINCIPALE #
#####################################################################################################

continuer = True
while continuer:


    """
    affichage de la grille
    """
    fenetre.fill((55, 148, 8))
    for i in range(30):
        for j in range(30):
            pygame.draw.rect(fenetre, (109, 148, 3), (i * 30, j * 30, 30, 30), 1)

    """
    si l'utilisateur ferme la fenetre, le jeu s'arrete
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False


    # creation des evenements pour pour bouger le serpent avec les touches directionnelles

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            # lorsque l'on presse la touche UP, le serpent se deplace vers le haut
            snake_direction_y = -1
            snake_direction_x = 0
        if event.key == pygame.K_DOWN:
            # lorsque l'on presse la touche DOWN, le serpent se deplace vers le bas
            snake_direction_y = 1
            snake_direction_x = 0
        if event.key == pygame.K_LEFT:
            # lorsque l'on presse la touche LEFT, le serpent se deplace vers la gauche
            snake_direction_x = -1
            snake_direction_y = 0
        if event.key == pygame.K_RIGHT:
            # lorsque l'on presse la touche RIGHT, le serpent se deplace vers la droite
            snake_direction_x = 1
            snake_direction_y = 0


    # lorsque le serpent depasse les limites de la fenetre, le jeu s'arrete
    if snake_position_x < 0:
        continuer = False
    if snake_position_x > largeur:
        continuer = False
    if snake_position_y < 0:
        continuer = False
    if snake_position_y > hauteur:
        continuer = False




    # faire bouger le serpent
    if time.time() - chrono >= 1 / blocsec:
        snake_position_x += snake_direction_x * 30 # 30 = taille du bloc
        snake_position_y += snake_direction_y * 30
        timer = time.time()



    # lorsque le serpent mange la pomme, il grandit et la pomme apparait a un autre endroit

    if snake_position_x == pomme_position_x and snake_position_y == pomme_position_y:
        pomme_position_x = random.randrange(0, largeur, 30)
        pomme_position_y = random.randrange(0, hauteur, 30)
        taille_snake += 1
        score += 1
        print(score)


    # on cree une liste de coordonnees pour le serpent
    snake_head = []
    snake_head.append(snake_position_x)
    snake_head.append(snake_position_y)

    # on ajoute les coordonnees du serpent a la liste
    position_snake.append(snake_head)

    # on limite la taille de la liste
    if len(position_snake) > taille_snake:
        del position_snake[0]

    # on dessine le serpent
    for x in position_snake:
        pygame.draw.rect(fenetre, couleur_snake, (x[0], x[1], 30, 30))

    # on dessine la pomme
    pygame.draw.rect(fenetre, couleur_pomme, (pomme_position_x, pomme_position_y, 30, 30))


    # affichage du score
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    fenetre.blit(text, (0, 0))


    # si le serpent se mord la queue, le jeu s'arrete
    for x in position_snake[:-1]:
        if x == snake_head:
            text = font.render("GAME OVER", True, (255, 255, 255))
            fenetre.blit(text, (largeur / 2 - 100, hauteur / 2 - 100))
            text = font.render("Score: " + str(score), True, (255, 255, 255))
            fenetre.blit(text, (largeur / 2 - 100, hauteur / 2 - 50))
            # on attend 2 secondes avant de fermer la fenetre
            time.sleep(2)
            continuer = False



    # on met a jour l'ecran
    pygame.display.flip()

    # on limite la vitesse du serpent car sinon il va trop vite
    clock.tick(10)



# on quitte pygame
pygame.quit()



