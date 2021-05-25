import pygame
import sys
class Grille:

    def __init__(self,ecran):
        """
        initie la grille
        :param: ecran
        """
        self.ecran = ecran
        self.lignes = [(( 200,0),(200,600)),((400,0),(400,600)),
        ((0,200),(600,200)),
        ((0,400),(600,400))]
        # initer la grille
        self.grille =[[None for x in range (0,3)] for y in range (0,3)]
        #initier une variable pour verifier si le compteur est 'ON'
        self.compteur_on = False
    def afficher(self):
        """
        Affiche la grille et les X/0
        """

        for ligne in self.ligne_:
            pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],2)
        #afficher les X et O
        for y in range(0,len(self.grille)):
            for x in range(0,len(self.grille)):
                if self.grille[y][x] == 'X':
                    pygame.draw.line(self.ecran, (0, 0, 0), (x * 200, y* 200), (200 + (x * 200), 200 + (y *200)), 3)
                    pygame.draw.line(self.ecran, (0, 0, 0), ((x * 200), 200 + (y * 200)), (200 + (x * 200), (y * 200)), 3)

                elif self.grille[y][x] == '0':

                    pygame.draw.circle(self.ecran, (0, 0, 0), (100 + (x * 200), 100 + (y * 200)), 100, 3)

    def print_grille(self):
        """
        Afficher la grille dans la console
        """
        print(self.grille)
    def fixer_la_valeur(self,x,y,valeur):
        """
        Fixe la valeur d'une case dans la grille

        :param: x
        :param: y
        :param : valeur
        """
        # cond si une case possede la valeur None
        if self.grille[y][x] == None :
            self.grille[y][x] = valeur
        #le compteur est ON
        self.compteur_on = True
    #creer une fonction qui fixe la valeur des cases a None
    def fixer_None(self,ligne,colonne,valeur):
        self.grille[ligne][colonne] = valeur



class Jeu :

    def __init__(self):
        self.ecran = pygame.display.set_mode((600,600))
        pygame.display.set_caption('Tic Tac Toe')
        self.jeu_encours = True
        self.grille = Grille(self.ecran)
        #fixer les variables 'X' et 'O'
        self.player_X = 'X'
        self.player_O = 'O'

        #fixer le compteur
        self.compteur = 0
        self.ecran_debut = True

    def fonction_principale(self):
        """
        execute le while loop
        """
        while self.jeu_encours:
            while self.ecran_debut:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.ecran_debut = False

                self.ecran.fill((230,230,230))

                self.creer_message('grande', 'Tic Tac Toe', (0,0,0), [200,30,200,50])
                self.creer_message('petite', "ce jeu ce joue à deux",(0,0,0), [50,130,400,50])
                self.creer_message('petite', 'X ou O', (0,0,0), [220,150,100,100])
                self.creer_message('petite', 'premier aligner 3 trois symboles gagne', (0,0,0), [50,170,200,50])
                self.creer_message('moyenne','recommencer jeu appuis entrer', (0,0,0), [70,350,200,50])
                self.creer_message('moyenne', 'appuie espace pour commencer', (0,0,0), [70,400,200,50])
                self.creer_message('moyenne', 'echap pour revenir menu', (0,0,0), [70,450,200,50])



                pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # ajouter l'evenement qui correspond au clique droit
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    # obtenir la position de la souris
                    position = pygame.mouse.get_pos()
                    print(position)
                    position_x , position_y = position[0]//200 ,position[1]//200
                    print(position_x,position_y)


                    # cond si le compteur est pair ou impair
                    print(self.compteur,self.compteur%2)
                    if self.compteur %2 == 0 :
                        self.grille.fixer_la_valeur(position_x,position_y,self.player_X)
                    else:
                        self.grille.fixer_la_valeur(position_x,position_y,self.player_O)
                    #cond si le compteur ON est vrai
                    if self.grille.compteur_on:
                        self.compteur += 1
                    #fixe le compteur_ON = Faux
                        self.grille.compteur_on = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.recommencer()
                    if event.key == pygame.K_ESCAPE:
                        self.ecran_debut = True

        liste_X = []
        liste_O = []
        liste_lignes_X = []
        liste_colonnes_X = []
        liste_lignes_O = []
        liste_colonnes_O = []

        self.gagnant(liste_X, liste_O, liste_colonnes_X, liste_lignes_X, liste_colonnes_O, liste_lignes_O)

        #print(self.compteur)
        #self.grille.print_grille()
        self.ecran.fill((240,240,240))
        self.grille.afficher()
        pygame.display.flip()
    def gagnant(self, liste_X, liste_O, liste_colonnes_X, liste_lignes_X, liste_colonnes_O, liste_lignes_O):
                """
                algorithm permettant de chercher si un joueur gagne
                :param: liste_X
                :param: liste_O
                :param: liste_colonnes_X
                :param: liste_lignes_X
                :param: liste_colonnes_O
                :param: liste_lignes_O


            """
                for ligne in range(0, len(self.grille.grille)):
                    for colonne in range(0,len(self.grille.grille)):
                        if self.grille.grille[ligne][colonne] == 'X':
                            X_position = (ligne,colonne)
                            liste_X.append(X_position)

                if self.grille.grille[ligne][colonne] == 'O':
                        O_position = (ligne,colonne)
                        liste_O.append(O_position)

                if len(liste_X) >= 3:
                    for (ligne,colonne) in liste_X:
                        liste_lignes_X.append(ligne)
                    liste_colonnes_X.append(colonne)

                if liste_lignes_X.count(0) == 3 or liste_lignes_X.count(1) == 3 or liste_lignes_X.count(2) == 3 :
                    print('X Gagne')

                if liste_colonnes_X.count(0) == 3 or liste_colonnes_X.count(1) == 3 or liste_colonnes_X.count(2) == 3 :
                    print('X gagne')

                if liste-lignes_X == liste_colonnes_X or ligste_lignes_X == liste_colonnes_X[::-1]:
                    print('X Gagne')


                if len(liste_O) >= 3 :
                    for (ligne,colonne) in liste_O:
                        liste_lignes_O.append(ligne)
                    liste_colonnes_O.append(colonne)

                if liste_lignes_O.count(0) == 3 or liste_lignes_O.count(1) == 3 or liste_lignes_O.count(2) == 3 :
                    print('O Gagne')

                if liste_colonnes_O.count(0) == 3 or liste_colonnes_O.count(1) == 3 or liste_colonnes_O.count(2) == 3 :
                    print('O gagne')

                if liste-lignes_O == liste_colonnes_O or ligste_lignes_O == liste_colonnes_O[::-1]:
                    print('O Gagne')

    #cree une fonction qui va attribuer la valeur None a chacune des cases.
    def recommencer(self):
        for ligne in range(0,len(self.grille.grille)):
            for colonne in range(0,len(self.grille.grille)):
                self.grille.fixer_None(ligne,colonne,None)

    def creer_message(self,font,couleur,message,message_rectangle):

        if font =='petite':
            font = pygame.font.SysFont('Lato', 20, False)

        elif font =='moyenne':
            font = pygame.font.SysFont('Lato', 30, False)
        elif font == 'grande':
            font = pygame.font.SysFont('Lato', 40, True)
        message = font.render(message,False,couleur)

        self.ecran.blit(message,message_rectangle)




pygame.init()
jeu=Jeu()
jeu.fonction_principale()
pygame.quit()