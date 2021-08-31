# https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7290721-enregistrez-des-donnees-complexes-avec-des-dictionnaires

# 1) Créez une variable de type dictionnaire appelée "chaussure"
chaussure = {}

""" 2) Ajoutez les éléments suivants dans le dictionnaire :
   - clef "taille" avec la valeur 42
   - clef "marque" avec la valeur "Nike"
   - clef "race" avec la valeur "berger-allemand"
"""

chaussure["taille"] = 42 
chaussure["marque"] = "Nike"
chaussure["race"] = "berger-allemand"

# 3) On s'est trompés ! Supprimez la clef "race" du dictionnaire :)

chaussure.pop("race")

print(chaussure); 

# 4) Récupérez la taille de la chaussure dans une variable appelée "taille"

taille = chaussure["taille"]
print(f"La taille de la chaussure est {taille}")  # 42 normalement !