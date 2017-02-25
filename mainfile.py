from boys import Boy
from girls import Girl
from utility import Utili

import csv
import logging

logging.basicConfig(format='%(asctime)s %(name)s - %(levelname)s %(message)s:',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='log.txt',filemode='w')

def allocate():
    with open('Boys.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        B = [Boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]))for row in reader]
        csvfile.close()

    with open('Girls.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        G = [Girl(row[0],int(row[1]),int(row[2]),int(row[3]))for row in reader]
        csvfile.close()

    logging.info('Profile Matching start:\n')
    for g in G:
        for b in B:
            logging.info('Commitment: Girl ' + g.name +' is checking profile of Boy '+b.name)
            if (b.is_elligible(g.bud,g.atr)) and (g.is_elligible(b.bud)) and g.status == 'single' and b.status == 'single':
                g.status = 'commited'
                b.status = 'commited'
                g.bname = b.name
                b.gname = g.name
                logging.info('Commitment Girl: '+g.name+' got commited with boy: '+b.name)
                break


    print("Couples formed \n")
    for g in G:
        if g.status == 'single':
            print('Girl: ' + g.name + '  is not commited to anyone')
        else:
            print('Girl: ' + g.name + '  is commited with  Boy: ' + g.bname)

Utili()
allocate()
