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
                CP += [(b,g)]
                break


    print("Couples formed \n")
    for g in G:
        if g.status == 'single':
            print('Girl: ' + g.name + '  is not commited to anyone')
        else:
            print('Girl: ' + g.name + '  is commited with  Boy: ' + g.bname)
    print("-"*100)
    C = [Couple(c[0],c[1]) for c in CP]
    calculate_happiness(C)


def calculate_happiness(C):
    with open('Gifts.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',')
        GFT = [Gift(row[0],int(row[1]),int(row[2]),row[3])for row in reader]
        csvfile.close()

    GFT = sorted(GFT,key=lambda k:k.price)
    logging.info('Gifting')
    for c in C:
        if (c.boy.type == 'Miser'):
            happy_miser(GFT,c)

        if (c.boy.type == 'Generous'):
            happy_generous(GFT,c)

        if (c.boy.type == 'Geek'):
            happy_geek(GFT,c)

    print_gifts(C)


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
			logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')

	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness = exp(v1).real
	c.boy.happiness = c.boy.bud
	c.set_happiness()
	c.set_compatibility()

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
			logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')
	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness = exp(v1).real
	c.boy.happiness = c.girl.happiness
	c.set_happiness()
	c.set_compatibility()

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
			logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')

	for i in GFT:
		if (i not in c.GFT) and (i.type == 'luxury') and (i.price <= c.boy.bud):
			v2 = v2 + 2*i.price
			v1 = v1 + i.price
			c.GFT = c.GFT + [i]
			c.boy.bud = c.boy.bud - i.price
			logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + i.name + ' of price = ' + str(i.price) + ' rupees')
			break


	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness =exp(v1).real
	c.boy.happiness = c.girl.intel
	c.set_happiness()
	c.set_compatibility()

def print_gifts(C):
	for c in C:
		print('Gifts given from Boy:  ' + c.boy.name + '  to Girl:  ' + c.girl.name + ':')
		for g in c.GFT:
			print('Gift named:  ' + g.name + '  of type:  ' + g.type)
		print ('\n')
		k = randint(1, len(C))
	print_hc(C, k)

def print_hc(C, k):
	A = sorted(C, key=lambda item: item.happiness)
	B = sorted(C, key=lambda item: item.compatibility)
	print(str(k) + ' most Happy couples:')
	for i in range(k):
		print (A[i].boy.name + ' and ' + A[i].girl.name)

	print ('\n' + str(k) + ' most Compatible couples:')
	for i in range(k):
		print(B[i].boy.name + ' and ' + B[i].girl.name)

Utili()
allocate()
