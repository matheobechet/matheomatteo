import pygame
import sys
class Grille:

    def __init__(self,ecran):
        """
        initie la grille
        :param: ecran
        """
        self.ecran = ecran
        self.lignes = [(( 200,0),(200,600))
        ((400,0),(400,600))
        ((0,200),(600,200))
        ((0,400),(600,400)),]
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


class Jeu :

    def __init__(self):
        self.ecran = pygame.display.set_mode((600,600))
        pygame.dipslay.set_caption('Tic Tac Toe')
        self.jeu_encours = True
        self.grille = Grille(self.ecran)
        #fixer les variables 'X' et 'O'
        self.player_X = 'X'
        self.player_O = 'O'
        
        #fixer le compteur
        self.compteur = 0
    
    def fonction_principale(self):
        while self.jeu_encours:
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
            liste_X = []
            liste_O = []
            liste_lignes_X = []
            liste_colonnes_X = []
            liste_lignes_O = []
            liste_colonnes_O = []
            
            for ligne in range(0,len(self.grille/grille)):
                for colonne in range(0,len(self.grille.grille)):
                    if self.grille.grille[ligne][colonne] == 'X':
                        
                        X_position = (ligne,colonne)
                        liste_X.append(X_position)
                        
                    elif self.grille.grille[ligne][colonne] == 'O':
                        O_position = (ligne,colonne)
                        liste_O.append(O_position)
            
            if len(liste_X) >= 3 :
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
                
                
              
                

                
            


            #print(self.compteur)
            #self.grille.print_grille()
            self.ecran.fill((240,240,240))
            self.grille.afficher()
            pygame.display.flip()


if __name__ == ' main':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()