quests1 = ["Bethaney Bain", "Kacey Johns", "Manpreet Saunders"]
quests2 = ["Elwood Curtis", "Diya Griffin", "Kacey Johns"]
quests3 = ["Tobey Weiss", "Kadie Barnes", "Diya Griffin"]
name = quests1 + quests2 + quests3
questsALL = []
for i in name:
    if i not in questsALL:
        questsALL.append(i)
questsALL.sort()
print("\n".join(questsALL))
