a = int(1)
def sjson(data, nom_fichier):
    #data = [int(i) for i in data]
    with open(nom_fichier, 'a') as f:
       json.dump(data, f)
    print("La sauvegarde a été faites")

sjson(a,"tirage.json")

