import pygame, time, random


# Fenetre
dimensions = largeur, hauteur = 900, 600
couleur_fond = 0, 0, 0

# couleur du serpent et de la pomme
couleur_snake = 0, 255, 0
couleur_pomme = 255, 0, 0
couleur_ananas = 255, 255, 0

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

# position de l'ananas
ananas_position_x = random.randrange(0, largeur,30)
ananas_position_y = random.randrange(0, hauteur,30)

# couleur obstacle
couleur_obstacle = 255, 255, 255

# position obstacle
obstacle_position_x = random.randrange(0, largeur,30)
obstacle_position_y = random.randrange(0, hauteur,30)


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


# initialisation de pygame
pygame.init()
# variable pour la fenetre avec les dimensions
fenetre = pygame.display.set_mode((dimensions))
# titre de la fenetre
pygame.display.set_caption("Snake by Hugenz")
pygame.display.flip()

# fonction pour afficher le score dans la fenetre a la fin du jeu
def fin_jeu():
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render("Game Over", True, (255, 255, 255))
    fenetre.blit(text, (largeur / 2 - 100, hauteur / 2 - 50))
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    fenetre.blit(text, (largeur / 2 - 50, hauteur / 2))
    pygame.display.flip()
    time.sleep(4)


#####################################################################################################
                                  # BOUCLE PRINCIPALE #
#####################################################################################################

continuer = True
while continuer:


    # affichage de la grille

    fenetre.fill((55, 148, 8)) # couleur de fond
    for i in range(30): # ligne verticale
        for j in range(30): # ligne horizontale
            pygame.draw.rect(fenetre, (109, 148, 3), (i * 30, j * 30, 30, 30), 1) # couleur de la grille


    # si l'utilisateur ferme la fenetre le jeu s'arrete

    for event in pygame.event.get(): # parcourir la liste des evenements
        if event.type == pygame.QUIT: # si l'evenement est de type QUIT
            continuer = False # arreter la boucle


    # creation des evenements pour bouger le serpent avec les touches directionnelles

    if event.type == pygame.KEYDOWN: # si une touche est enfoncée
        if event.key == pygame.K_UP:
            # lorsque l'on presse la touche UP, le serpent se deplace vers le haut
            snake_direction_y = -1 # direction vers le haut
            snake_direction_x = 0 # direction vers le haut
        if event.key == pygame.K_DOWN:
            # lorsque l'on presse la touche DOWN, le serpent se deplace vers le bas
            snake_direction_y = 1 # direction vers le bas
            snake_direction_x = 0 # direction vers le bas
        if event.key == pygame.K_LEFT:
            # lorsque l'on presse la touche LEFT, le serpent se deplace vers la gauche
            snake_direction_x = -1 # direction vers la gauche
            snake_direction_y = 0 # direction vers la gauche
        if event.key == pygame.K_RIGHT:
            # lorsque l'on presse la touche RIGHT, le serpent se deplace vers la droite
            snake_direction_x = 1 # direction vers la droite
            snake_direction_y = 0 # direction vers la droite


    # lorsque le serpent depasse les limites de la fenetre, le jeu s'arrete

    if snake_position_x < 0: # si le serpent depasse la limite gauche
        fin_jeu()
        continuer = False # arreter la boucle
    if snake_position_x > largeur: # si le serpent depasse la limite droite
        fin_jeu()
        continuer = False # arreter la boucle
    if snake_position_y < 0: # si le serpent depasse la limite haute
        fin_jeu()
        continuer = False # arreter la boucle
    if snake_position_y > hauteur: # si le serpent depasse la limite basse
        fin_jeu()
        continuer = False # arreter la boucle



    # faire bouger le serpent

    if time.time() - chrono >= 1 / blocsec: # si le temps ecoulé est superieur ou egal a 1 / blocsec (vitesse du serpent = 10)
        snake_position_x += snake_direction_x * 30 # ajouter 30 a la position du serpent en x
        snake_position_y += snake_direction_y * 30 # ajouter 30 a la position du serpent en y
        timer = time.time() # timer = temps ecoulé



    # lorsque le serpent mange la pomme, il grandit et la pomme apparait a un autre endroit

    if snake_position_x == pomme_position_x and snake_position_y == pomme_position_y: # si la position du serpent est egale a la position de la pomme
        pomme_position_x = random.randrange(0, largeur, 30) # la pomme apparait a un autre endroit en x
        pomme_position_y = random.randrange(0, hauteur, 30) # la pomme apparait a un autre endroit en y
        taille_snake += 1 # le serpent grandit de 1
        score += 1 # le score augmente de 1
        print(score)


    if snake_position_x == ananas_position_x and snake_position_y == ananas_position_y:
        ananas_position_x = random.randrange(0, largeur, 30)
        ananas_position_y = random.randrange(0, hauteur, 30)
        taille_snake += 5
        score += 2
        print(score)


    # on cree une liste de coordonnees pour le serpent

    snake_head = [] # creer une liste vide
    snake_head.append(snake_position_x) # ajouter la position du serpent en x a la liste
    snake_head.append(snake_position_y) # ajouter la position du serpent en y a la liste

    # on ajoute les coordonnees du serpent a la liste
    position_snake.append(snake_head) # ajouter la liste snake_head a la liste position_snake

    # on limite la taille de la liste
    if len(position_snake) > taille_snake: # si la taille de la liste est superieur a la taille du serpent
        del position_snake[0] # supprimer la premiere valeur de la liste

    # on dessine le serpent
    for x in position_snake: # pour chaque valeur de la liste position_snake
        pygame.draw.rect(fenetre, couleur_snake, (x[0], x[1], 30, 30)) # dessiner un rectangle de couleur snake aux coordonnees x[0] et x[1] avec une taille de 30 par 30

    # on dessine une boule pour la pomme
    pygame.draw.circle(fenetre, couleur_pomme, (pomme_position_x + 15, pomme_position_y + 15), 15) # dessiner un cercle de couleur pomme aux coordonnees pomme_position_x + 15 et pomme_position_y + 15 avec un rayon de 15
    # on dessine un carre pour l ananas
    pygame.draw.rect(fenetre, couleur_ananas, (ananas_position_x, ananas_position_y, 30, 30))


    # apparition de 1 obstacle tous les 10 points
    if score == 5 :
        pygame.draw.rect(fenetre, couleur_obstacle, (obstacle_position_x, obstacle_position_y, 30, 30))
    if score == 10 :
        pygame.draw.rect(fenetre, couleur_obstacle, (obstacle_position_x, obstacle_position_y, 30, 30))
    if score == 15 :
        pygame.draw.rect(fenetre, couleur_obstacle, (obstacle_position_x, obstacle_position_y, 30, 30))
    if score == 20 :
        pygame.draw.rect(fenetre, couleur_obstacle, (obstacle_position_x, obstacle_position_y, 30, 30))
    if score == 25 :
        pygame.draw.rect(fenetre, couleur_obstacle, (obstacle_position_x, obstacle_position_y, 30, 30))
    if score == 30 :
        pygame.draw.rect(fenetre, couleur_obstacle, (obstacle_position_x, obstacle_position_y, 30, 30))
    if score == 35 :
        pygame.draw.rect(fenetre, couleur_obstacle, (obstacle_position_x, obstacle_position_y, 30, 30))
    if score == 40 :
        pygame.draw.rect(fenetre, couleur_obstacle, (obstacle_position_x, obstacle_position_y, 30, 30))





    # affichage du score
    font = pygame.font.SysFont("comicsansms", 30) # police d'ecriture et taille
    text = font.render("Score: " + str(score), True, (255, 255, 255)) # texte a afficher
    fenetre.blit(text, (0, 0)) # afficher le texte



    # si le serpent se mord la queue, le jeu s'arrete

    for x in position_snake[:-1]: # pour chaque valeur de la liste position_snake sauf la derniere
        if x == snake_head: # si la valeur de la liste est egale a la liste snake_head
            fin_jeu()
            continuer = False # arreter la boucle


    # on met a jour l'ecran
    pygame.display.flip()

    clock.tick(10) # 10 fps (images par seconde)


# on quitte pygame
pygame.quit()


