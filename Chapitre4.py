# https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7290436-enregistrez-des-groupes-de-donnees-avec-les-listes

liste_nombres = [1, 6, 98, 52, 1045, 3]

#1) classez la liste

liste_nombres.sort(); 

#2) supprimez le premier element de la liste

liste_nombres.pop(0); 

#3) ajoutez le nombre 1047 à la fin de votre liste 

liste_nombres.append(1047); 

#4) récuperez le deuxième élement de la liste dans une variable "deuxieme_element" 

deuxieme_element = liste_nombres[2]; 


#5) Affichez en une ligne la longeur de la liste après avoir supprimé le dernier élement 

liste_nombres.pop(-1); 

print(len(liste_nombres)); 

