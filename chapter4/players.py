players = ['charles','martina','michael','florence','eli']
print(players)
print("开始切片了")
print(players[0:2])
print(players[-3:])

print('---------遍历切片--------')
for player in players[-4:]:
    print(player)

print('-------复制列表----------')
player_copy = players[:]
print(players)
print(player_copy)
players.pop(3)
print(players)
print(player_copy)