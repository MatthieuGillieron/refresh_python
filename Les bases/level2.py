# Les listes

#insert -> mettter val a un endroit precis
#[1:4] -> a parti de l element 1 jusqua l'element 4
#append -> ajouter en bout de liste
#pop -> suprimmer element via son index
#remove -> surpimmer via nom
#clear -> nettoyer la liste


online_players = ["bob", "kev", "frank"]
print(online_players[-1])

#modifier element
online_players[2] = "sarah"
print(online_players[-1])

#ajouter element
online_players.insert(3, "Ana")
print(online_players)

#modifier a partir d'un certain endroit
print(online_players[1:4])
online_players[1:4] = ["pop", "jay", "britney"]
print(online_players)


#ajter en fin de liste
online_players.append("test")
print(online_players)


#suprimmer element
online_players.pop(1)
print(online_players)
online_players.remove("test")
print(online_players)
online_players.clear()
print(online_players)
