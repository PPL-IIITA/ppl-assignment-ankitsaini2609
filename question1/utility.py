from random import randint
import csv

def Utili():
    Boy = [('B'+str(i),randint(2,200),randint(44,1200),randint(100,3000),randint(1,160))for i in range(1,101)]
    Girl = [('G'+str(i),randint(2,180),randint(36,1000),randint(90,2500))for i in range(1,51)]

    Create('Boys.csv',Boy)
    Create('Girls.csv',Girl)

def Create(file,l):
    f = open(file,"w")
    write = csv.writer(f,delimiter = ',')

    for i in l:
        write.writerow(i)





    
