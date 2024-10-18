import csv
import os

word_dict = {}

def init():  
    
    file1 = open('/Users/gauss/UNI/IA/Progetti/neg_words.txt','r')
    negative = file1.read()
    file2 = open('/Users/gauss/UNI/IA/Progetti/pos_words.txt','r')
    positive = file2.read()
    
    with open('/Users/gauss/UNI/IA/Progetti/train.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            if len(row) > 1:
                seconda_colonna = row[1]
                
                parole = seconda_colonna.split()
                
                for parola in parole:
                    if parola in positive:
                        word_dict[parola] = 1
                    elif parola in negative:
                        word_dict[parola] = -1
                    else:
                        word_dict[parola] = 0

def fineTuning():
    modifica = 1/7000
    
    file = open('/Users/gauss/UNI/IA/Progetti/train.csv', 'r')
    reader = csv.reader(file)

    next(reader)
 
    for riga in reader:
        parole = riga[1].split() 
        
        sentimento = riga[2].strip().lower()

        for parola in parole:
            if sentimento == 'positive':
                word_dict[parola] = word_dict.get(parola, 0) + modifica
            elif sentimento == 'negative':
                word_dict[parola] = word_dict.get(parola, 0) - modifica

def test():
    test = open('/Users/gauss/UNI/IA/Progetti/test.csv', mode='r')
    out = open('/Users/gauss/UNI/IA/Progetti/output.txt',mode='w')
    reader = csv.reader(test)
    

    for row in reader:
        punteggio = 0
        if len(row) > 1:
            frase = row[1] 
            parole = frase.split()  
            
            for parola in parole:
                if parola in word_dict:
                    punteggio += word_dict[parola]
        if punteggio > 0:
            out.write(row[0]+' positive'+'\n')
        elif punteggio < 0:
            out.write(row[0]+' negative'+'\n')
        else:
            out.write(row[0]+' neutral'+'\n')

init()
fineTuning()
test()