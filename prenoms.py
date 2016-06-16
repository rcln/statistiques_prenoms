# -*- coding: utf-8 -*-
import csv

#file origine le csv
myfile ="c:\Python27\prenoms.csv" 

#file sql nouveau
myfile2 ="c:\Python27\prenoms.sql" 

#file sql avec nouveau formatage
myfile3 ="c:\Python27\prenoms2.sql" 

i=0
n="'"
app = "\'"
vir = ","

#pour lire le csv
lire = csv.reader(open(myfile,"rb")) 

#pour ecrire en csv dans le fichier sql
ecrire = csv.writer(open(myfile2, "wb")) 

#ouverture du fichier sql
f2 = open(myfile2,'r')

#ouverture du 2ème ficher sql 
f3 = open(myfile3,'w')

#lecture du csv
for row in lire:
  annee = row[0]
  qtt = row[1]
  id = row[2]
  #pour remplacer le "'" par "\'" dans prenom
  ch = row[3]
  if n in ch:
    ch = ch.replace("'","\\'")
  prenom = app+ch+"\');"
  req = 'insert into prenoms_insee (annee, qtt, id, prenom) values ('+annee+vir+qtt+vir+app+id+app+vir+prenom
  #ecrire dans le fichier sql
  ecrire.writerow([req])
  #lecture dans le fichier qu'on vient de créer
  lines = f2.readline()
  lines2 = str(lines)
  #supprime le " en debut et fin de ligne
  lines2 = lines2[1:len(lines2) - 2]+'\n'
  #pour supprimer la premiere ligne du fichier sql
  if (lines != ''):
    i = i+1
  #ecrit dans le 2ème fichier sql avec nouveau format et à partir de la 2ème lignes
  if ((lines != '') and (i > 1)):
    f3.writelines(lines2)
f2.close()
f3.close()
