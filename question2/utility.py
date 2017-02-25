from random import choice
from random import randint
import csv

def Utili():
    BT = ['Miser','Geek','Generous']
    GT = ['Choosy','Normal','Desperate']
    GFT= ['Essential','Luxury','Utility']
    Boy = [('B'+str(i),randint(2,20),randint(44,120),randint(100,300),randint(1,16),choice(BT))for i in range(1,51)]
    Girl = [('G'+str(i),randint(2,18),randint(36,100),randint(90,250),choice(GT))for i in range(1,26)]
    Gift = [('GFT'+str(i),randint(70,200),randint(90,150),choice(GFT))for i in range(1,100)]
    
    Create('Boys.csv',Boy)
    Create('Girls.csv',Girl)
    Create('Gifts.csv',Gift)
def Create(file,l):
    f = open(file,"w")
    write = csv.writer(f,delimiter = ',')

    for i in l:
        write.writerow(i)







    
