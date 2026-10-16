notes=[12,8,15,17,9,14,6,18,11,13]
moyenne=sum(notes)/ len(notes)
nb_admis=0
for note in notes:
    if note>=10:
        nb_admis+=1
maximum=max(notes)

def est_admis(note):
    return note>=10

p_admis= nb_admis/len(notes)*100

print("Nombre de notes: ", len(notes))
print("Moyenne: ", moyenne)
print("le max est:", maximum)
print("le nombre d'admis est", nb_admis,"soit",p_admis,"%")
