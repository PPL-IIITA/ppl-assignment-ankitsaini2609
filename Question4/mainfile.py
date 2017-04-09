from cmath import exp, log10
from math import floor
from random import randint
from gifts import Gift
from couples import Couple
from boys import Boy
from girls import Girl
from utility import Utili

import csv
import logging

logging.basicConfig(format='%(asctime)s %(name)s - %(levelname)s %(message)s:',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='log.txt',filemode='w')

def allocate():
    with open('Boys.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        B = [Boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5])for row in reader]
        csvfile.close()

    with open('Girls.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        G = [Girl(row[0],int(row[1]),int(row[2]),int(row[3]),row[4])for row in reader]
        csvfile.close()

    CP = []
    logging.info('Before valentine couple formation:')
    for g in G:
        for b in B:
            if (b.is_elligible(g.bud,g.atr)) and (g.is_elligible(b.bud)) and g.status == 'single' and b.status == 'single':
                g.status = 'commited'
                b.status = 'commited'
                g.bname = b.name
                b.gname = g.name
                logging.info('Commitment Girl: '+g.name+' got commited with boy: '+b.name)
                CP += [(b,g)]
                break


    C = [Couple(c[0],c[1]) for c in CP]
    calculate_happiness(C,G,B)


def calculate_happiness(C,G,B):
    with open('Gifts.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',')
        GFT = [Gift(row[0],int(row[1]),int(row[2]),row[3])for row in reader]
        csvfile.close()

    GFT = sorted(GFT,key=lambda k:k.price)
    for c in C:
        if (c.boy.type == 'Miser'):
            happy_miser(GFT,c)

        if (c.boy.type == 'Generous'):
            happy_generous(GFT,c)

        if (c.boy.type == 'Geek'):
            happy_geek(GFT,c)
    
    #p is used for atleast k happy value of happiness.
    p = randint(1,100)
    break_up(C,p,G,B)


def happy_miser(GFT, c):
	v1 = 0
	v2 = 0
	for g in GFT:
		if (g.price == c.girl.bud) or (g.price - c.girl.bud <= 100) and (c.boy.bud >= 0) and (c.boy.bud - g.price > 0):
			if (g.type == 'Luxury'):
				v2 = v2 + 2*g.price
			else:
				v2 = v2 + g.price
			v1 = v1 + g.price
			c.GFT = c.GFT + [g]
			c.boy.bud = c.boy.bud - g.price

	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness = exp(v1).real
	c.boy.happiness = c.boy.bud
	c.set_happiness()


def happy_generous(GFT, c):
	v1 = 0
	v2 = 0
	for g in GFT:
		if ((g.price == c.boy.bud) or (c.boy.bud-g.price <= 300)) and (c.boy.bud >= 0) and (c.boy.bud - g.price > 0):
			if (g.type == 'Luxury'):
				v2 = v2 + 2*g.price
			else:
				v2 = v2 + g.price
			v1 = v1 + g.price
			c.GFT = c.GFT + [g]
			c.boy.bud = c.boy.bud - g.price

	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness = exp(v1).real
	c.boy.happiness = c.girl.happiness
	c.set_happiness()


def happy_geek(GFT, c):
	v1 = 0
	v2 = 0
	for g in GFT:
		if (g.price == c.girl.bud) or (g.price-c.girl.bud <= 100) and (c.boy.bud >= 0) and (c.boy.bud - g.price > 0):
			if (g.type == 'Luxury'):
				v2 = v2 + 2*g.price
			else:
				v2 = v2 + g.price
			v1 = v1 + g.price
			c.GFT = c.GFT + [g]
			c.boy.bud = c.boy.bud - g.price

	for i in GFT:
		if (i not in c.GFT) and (i.type == 'luxury') and (i.price <= c.boy.bud):
			v2 = v2 + 2*i.price
			v1 = v1 + i.price
			c.GFT = c.GFT + [i]
			c.boy.bud = c.boy.bud - i.price
			break


	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness =exp(v1).real
	c.boy.happiness = c.girl.intel
	c.set_happiness()


def break_up(c, p,G,B):
    A = sorted(c, key=lambda item: item.happiness)
    logging.info("Couple Breakup start")
    for i in c:
        if i.happiness < p:
            logging.info("Commitment Girl: "+i.girl.name+ " Breaked up to the boy: "+ i.boy.name)
            for j in range(0,len(G)):
                if (i.girl == G[j].name):
                    G[j].status = 'single'
                    G[j].bname = ''
                    G[j].happiness = 0
                    break
            for j in range(0,len(B)):
                if (i.girl.name == B[j].name):
                    B[j].status = 'single'
                    B[j].gname = ''
                    B[j].happiness = 0
                    break
            c.remove(i)
    CP = []
    for g in G:
        for b in B:
            if (b.is_elligible(g.bud,g.atr)) and (g.is_elligible(b.bud)) and g.status == 'single' and b.status == 'single':
                g.status = 'commited'
                b.status = 'commited'
                g.bname = b.name
                b.gname = g.name
                CP += [(b,g)]
                break
    for i in CP:
        c.append(Couple(i[0],i[1]))
    logging.info('Again Profile Matching start After Breakup:\n')

    for i in c:
        logging.info('Commitment Girl: '+i.girl.name+' got commited with boy: '+i.boy.name)
        
    
Utili()
allocate()
