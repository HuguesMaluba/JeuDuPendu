import sys
import os
from PyQt5.QtWidgets import QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QMainWindow,QWidget,QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from random import randint


class MaFenetre(QMainWindow): #Ma fenetre du jeu du pendu
    def __init__(self):
        self.mot = None #qui stocke le mot a trouver
        self.nbEssaie = 8 #qui stocke le nombre d'essaies
        super().__init__()
        self.setGeometry(100,100,650,550)
        self.setWindowTitle("Jeu Du Pendu")
        self.setMaximumSize(450,250)
        self.setMinimumSize(450,250)
        self.setupIU()
        self.btnJouer.clicked.connect(self.jouer)
        self.btnA.clicked.connect(lambda:self.ajouterLettre(self.btnA.text()))
        self.btnB.clicked.connect(lambda:self.ajouterLettre(self.btnB.text()))
        self.btnC.clicked.connect(lambda:self.ajouterLettre(self.btnC.text()))
        self.btnD.clicked.connect(lambda:self.ajouterLettre(self.btnD.text()))
        self.btnE.clicked.connect(lambda:self.ajouterLettre(self.btnE.text()))
        self.btnF.clicked.connect(lambda:self.ajouterLettre(self.btnF.text()))
        self.btnG.clicked.connect(lambda:self.ajouterLettre(self.btnG.text()))
        self.btnH.clicked.connect(lambda:self.ajouterLettre(self.btnH.text()))
        self.btnI.clicked.connect(lambda:self.ajouterLettre(self.btnI.text()))
        self.btnJ.clicked.connect(lambda:self.ajouterLettre(self.btnJ.text()))
        self.btnK.clicked.connect(lambda:self.ajouterLettre(self.btnK.text()))
        self.btnL.clicked.connect(lambda:self.ajouterLettre(self.btnL.text()))
        self.btnM.clicked.connect(lambda:self.ajouterLettre(self.btnM.text()))
        self.btnN.clicked.connect(lambda:self.ajouterLettre(self.btnN.text()))
        self.btnO.clicked.connect(lambda:self.ajouterLettre(self.btnO.text()))
        self.btnP.clicked.connect(lambda:self.ajouterLettre(self.btnP.text()))
        self.btnQ.clicked.connect(lambda:self.ajouterLettre(self.btnQ.text()))
        self.btnR.clicked.connect(lambda:self.ajouterLettre(self.btnR.text()))
        self.btnS.clicked.connect(lambda:self.ajouterLettre(self.btnS.text()))
        self.btnT.clicked.connect(lambda:self.ajouterLettre(self.btnT.text()))
        self.btnU.clicked.connect(lambda:self.ajouterLettre(self.btnU.text()))
        self.btnV.clicked.connect(lambda:self.ajouterLettre(self.btnV.text()))
        self.btnW.clicked.connect(lambda:self.ajouterLettre(self.btnW.text()))
        self.btnX.clicked.connect(lambda:self.ajouterLettre(self.btnX.text()))
        self.btnY.clicked.connect(lambda:self.ajouterLettre(self.btnY.text()))
        self.btnZ.clicked.connect(lambda:self.ajouterLettre(self.btnZ.text()))
        self.show()
    
    def setupIU(self):
        #Boutons des lettres
        self.btnA = QPushButton('a')
        self.btnB = QPushButton('b')
        self.btnC = QPushButton('c')
        self.btnD = QPushButton('d')
        self.btnE = QPushButton('e')
        self.btnF = QPushButton('f')
        self.btnG = QPushButton('g')
        self.btnH = QPushButton('h')
        self.btnI = QPushButton('i')
        self.btnJ = QPushButton('j')
        self.btnK = QPushButton('k')
        self.btnL = QPushButton('l')
        self.btnM = QPushButton('m')
        self.btnN = QPushButton('n')
        self.btnO = QPushButton('o')
        self.btnP = QPushButton('p')
        self.btnQ = QPushButton('q')
        self.btnR = QPushButton('r')
        self.btnS = QPushButton('s')
        self.btnT = QPushButton('t')
        self.btnU = QPushButton('u')
        self.btnV = QPushButton('v')
        self.btnW = QPushButton('w')
        self.btnX = QPushButton('x')
        self.btnY = QPushButton('y')
        self.btnZ = QPushButton('z')
        
        #bouton qui lance le jeu
        self.btnJouer = QPushButton('Jouer')
        
        #label qui contient les images
        self.essaie = QLabel("8")
        self.essaie.setStyleSheet("font-size:110px;")
        self.essaie.setAlignment(Qt.AlignJustify)
        
        #label qui va contenir le mot 
        self.labelMot = QLabel("Trouvez Le Verbe      ")
        self.labelMot.setAlignment(Qt.AlignCenter|Qt.AlignJustify)
        self.labelMot.setStyleSheet("font-size:30px;")
        
        #positionnement des elements
        #1ere ligne pour les lettres
        self.HBox1 = QHBoxLayout()
        self.HBox1.addWidget(self.btnA)
        self.HBox1.addWidget(self.btnB)
        self.HBox1.addWidget(self.btnC)
        self.HBox1.addWidget(self.btnD)
        self.HBox1.addWidget(self.btnE)
        self.HBox1.addWidget(self.btnF)
        self.HBox1.addWidget(self.btnG)
        
        #2eme ligne pour les lettres
        self.HBox2 = QHBoxLayout()
        self.HBox2.addWidget(self.btnH)
        self.HBox2.addWidget(self.btnI)
        self.HBox2.addWidget(self.btnJ)
        self.HBox2.addWidget(self.btnK)
        self.HBox2.addWidget(self.btnL)
        self.HBox2.addWidget(self.btnM)
        self.HBox2.addWidget(self.btnN)
        
        #3eme ligne pour les lettres
        self.HBox3 = QHBoxLayout()
        self.HBox3.addWidget(self.btnO)
        self.HBox3.addWidget(self.btnP)
        self.HBox3.addWidget(self.btnQ)
        self.HBox3.addWidget(self.btnR)
        self.HBox3.addWidget(self.btnS)
        self.HBox3.addWidget(self.btnT)
        self.HBox3.addWidget(self.btnU)
        
        #4eme ligne pour les lettres
        self.HBox4 = QHBoxLayout()
        self.HBox4.addWidget(self.btnV)
        self.HBox4.addWidget(self.btnW)
        self.HBox4.addWidget(self.btnX)
        self.HBox4.addWidget(self.btnY)
        self.HBox4.addWidget(self.btnZ)
        
        #colenne qui contient toutes les lettres
        self.VBox1 = QVBoxLayout()
        self.VBox1.addLayout(self.HBox1)
        self.VBox1.addLayout(self.HBox2)
        self.VBox1.addLayout(self.HBox3)
        self.VBox1.addLayout(self.HBox4)
        
        #ligne qui contient tous les boutons
        self.HBox5 = QHBoxLayout()
        self.HBox5.addWidget(self.btnJouer)
        self.HBox5.addLayout(self.VBox1)
        
        #ligne qui contient tous les labels
        self.HBox6 = QHBoxLayout()
        self.HBox6.addWidget(self.essaie)
        self.HBox6.addWidget(self.labelMot)
        
        
        #widget central qui contient tous les autres widgets et layouts
        self.centralWidget	=	QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.VBox = QVBoxLayout(self.centralWidget)
        self.VBox.addLayout(self.HBox6)
        self.VBox.addLayout(self.HBox5)
        
    #autres methodes
    def convertirFichier(self,nomFichier):
        #Retourner une liste  des mots du fichier place en parametre
        verbes1 = "avoir etre boire voir choisir venir copier coller garder bouger danser partir finir sortir mettre convertir tomber chanter perdre obtenir "
        verbes2 = "coder devoir pouvoir jouer prevoir manger dormir venir laisser rendre vivre penser croire tenir rire rester mourir devenir lire etudier "
        verbes3 = "porter eviter montrer tirer arriver vouloir oublier poser aimer sentir arreter quitter etablir revenir marcher tendre lever gagner perdre aider "
        verbes4 = "revoir oser creer tuer courir rentrer ajouter toucher payer jeter agir preparer battre offrir glisser former partir finir"
        motDeVerbes =  verbes1 +  verbes2 +  verbes3 +  verbes4
        verbes = motDeVerbes.split(" ")
        cwd = os.getcwd()
        src = os.path.join(cwd,'src')
        if os.path.exists(nomFichier):#fichier existe
            with open(nomFichier,'r') as fichier:
                return [ligne.strip() for ligne in fichier]
        elif not os.path.exists(nomFichier):#fichier n'existe pas 
            os.makedirs(src)
            with open(src + '/verbes.txt','w') as fichier:
                for i in range(len(verbes)):
                    if i == len(verbes) - 1:
                        fichier.write(verbes[i])
                    else:
                        fichier.write(verbes[i] +"\n")   
        return verbes


    def unMot(self,liste):
        #Retourner un mot de la liste
        return liste[randint(0,len(liste)-1)]
    
    def lettreDuMot(self,lettre,mot):
        #fonction qui modifie le contenu du label
        #si la lettre se trove dans le mot qu'on cherche
        if mot != None:
            labelContenu = list(self.labelMot.text())
            for i in range(0,len(labelContenu)):
                if lettre == mot[i]:
                    labelContenu[i] = lettre
            self.labelMot.setText(''.join(labelContenu))
            
    def gameOver(self):
        #fin du jeu
         if self.nbEssaie == 0:
            self.essaie.setText("Game Over")
            self.essaie.setStyleSheet("font-size:25px;")
            self.essaie.setAlignment(Qt.AlignCenter|Qt.AlignJustify)
            self.etatBoutons(True)
    
    def ajouterLettre(self,lettre):
        #Logiue du jeu
        if self.mot != None: 
            self.gameOver()
            if lettre in self.mot and self.nbEssaie != 0:
                self.lettreDuMot(lettre,self.mot)
                if self.labelMot.text() == self.mot:
                    self.essaie.setText("You Win")
                    self.essaie.setStyleSheet("font-size:25px;")
                    self.essaie.setAlignment(Qt.AlignCenter|Qt.AlignJustify)
                    self.etatBoutons(True)
                else:
                    self.mettreAJour()
                
            elif self.nbEssaie != 0:
                self.mettreAJour()
                
        else:
            self.labelMot.setText("Cliquez Sur Jouer      ")
            self.etatBoutons(True)
            
    def mettreAJour(self):
        #Qui met a jour la valeur du label 
        self.nbEssaie -= 1
        self.essaie.setText(str(self.nbEssaie))
        self.gameOver()
        
    def etatBoutons(self,etat):
        #Modifier l'etat de boutons
            self.btnA.setDisabled(etat)
            self.btnB.setDisabled(etat)
            self.btnC.setDisabled(etat)
            self.btnD.setDisabled(etat)
            self.btnE.setDisabled(etat)
            self.btnF.setDisabled(etat)
            self.btnG.setDisabled(etat)
            self.btnH.setDisabled(etat)
            self.btnI.setDisabled(etat)
            self.btnJ.setDisabled(etat)
            self.btnK.setDisabled(etat)
            self.btnL.setDisabled(etat)
            self.btnM.setDisabled(etat)
            self.btnN.setDisabled(etat)
            self.btnO.setDisabled(etat)
            self.btnP.setDisabled(etat)
            self.btnQ.setDisabled(etat)
            self.btnR.setDisabled(etat)
            self.btnS.setDisabled(etat)
            self.btnT.setDisabled(etat)
            self.btnU.setDisabled(etat)
            self.btnV.setDisabled(etat)
            self.btnW.setDisabled(etat)
            self.btnX.setDisabled(etat)
            self.btnY.setDisabled(etat)
            self.btnZ.setDisabled(etat)
        
    def jouer(self):
        #lancer le jeu
        self.mot = self.unMot(self.convertirFichier('src/verbes.txt'))
        self.labelMot.setText('-'*len(self.mot))
        self.labelMot.setAlignment(Qt.AlignCenter|Qt.AlignJustify)
        self.nbEssaie = 8
        self.essaie.setText("8")
        self.essaie.setStyleSheet("font-size:110px;")
        self.essaie.setAlignment(Qt.AlignJustify)
        self.etatBoutons(False)
        
        

app = QApplication([])
fenetre = MaFenetre()
sys.exit(app.exec_())