# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:23:26 2018

@author: Manuel
"""

import nltk
import MySQLdb

#conexión a la bd
db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="db_diccionario")
cursor = db.cursor()
sql = 'select * from palabras'
cursor.execute(sql)

#Obtienes el documento .txt y lo guardas en la variable texto
archivo=open('output.txt','r')
texto=archivo.read()

#Obtienes las palabras del documento pdf en una lista
tokens=nltk.word_tokenize(texto,"spanish")

#Obtienes en una tupla las columnas de la bd de la tabla palabras
palabras = cursor.fetchall()
    
#Determinamos el tamaños de las palabras del diccionario y del pdf
tam1 = len(sql)
tam2 = len(tokens)

#Declaramos un contador para el conteo de palabras que si existen en el
#diccionario del español
cont = 0

#Realizamos una comparación
for i in range(0,tam1):
    for j in range(0,tam2):
        if(tokens[j] == palabras[i][1]):
            cont = cont + 1

#Medimos el performance de las palabras trasnformadas del pdf al .txt
performance = float(cont)/float(tam2)
print('Tenemos un porcentante de performance gramático de :',performance)