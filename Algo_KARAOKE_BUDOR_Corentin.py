class Player:
    def __init__(self,Pseudo,song0,song1,song2,song3,song4):
        self.__Name=Pseudo
        self.__Song1=song0
        self.__Song2=song1
        self.__Song3=song2
        self.__Song4=song3
        self.__Song5=song4

    def getScoreTotal(self):
        Total= self.__Song1 + self.__Song2 + self.__Song3 + self.__Song4 + self.__Song5
        print(self.__Name,"possède",Total,"points")
    
    
    def getMeilleurScore(self):
        MScore=self.__Song1
        ScoreN = 0

        for i in range(5) : 
            A = "self.__Song" + i
            if MScore>A :
                MScore=A
                ScoreN=i

        print("Ton meilleur score est",MScore)

    def getPireScore(self) :
        MScore=self.__Song1
        ScoreN=0

        for i in range(5) : 
            A = "self.__Song" + i
            if MScore>A :
                MScore=A
                ScoreN=i

        print("Ton dernier score est",A)

    def AjouteScore(self) :
        Chanson = int(input("Quel chanson viens tu de chanter?"))
        Score = int(input("Et quel score as tu fait ?"))

        if Chanson == 1:
            self.__Song1 = Score
        
        elif Chanson == 2:
            self.__Song2 = Score

        elif Chanson == 3:
            self.__Song3 = Score
        
        elif Chanson == 4:
            self.__Song4 = Score

        elif Chanson == 5:
            self.__Song5 = Score
        
        print("Ton score est de",Score)

    def Moyenne(self) :
        Reponse1= 0
        Reponse2= 0
        OUI = Reponse1
        NON = Reponse2
        int(input("Veux tu savoir ta moyenne ? OUI ou NON"))
        if OUI :
            print("Ton score moyen est"(self.__Song1 + self.__Song2 + self.__Song3 + self.__Song4 + self.__Song5)/5)
        elif NON :
            print("OK")
            




Pseudo = input("Quel est ton Pseudo ?")

Joueur1 = Player(0,0,0,0,0)

fin = False
while fin != True :
    P = int(input("Que souhaitez vous faire ?  Ajouter score = 1   Somme des scores = 2    Moyenne des scores = 3    Pire score = 4"))
    if P == 1 :
        Joueur1.getAjouteScore
    
    elif P == 2 : 
        Joueur1.getScoreTotal

    elif P == 3 :
        Joueur1.Moyenne

    elif P == 4 :
        Joueur1.getPireScore




