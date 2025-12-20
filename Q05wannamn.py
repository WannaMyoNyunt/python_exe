games_list = ["Roblox", "Minecraft", "PUBG", "Fortnite", "Among Us", "Valorant"]
print(games_list)
games_list.append("Monster Hunters")
print(games_list)
games_list.remove("Among Us")
print(games_list)
minecraft_index = games_list.index("Minecraft")
games_list.insert(2, "Mobile Legends")
print(games_list)
games_list.sort()
print(games_list)

del games_list[4]
print(games_list)

print(f"Number of games in the list {len(games_list)}")