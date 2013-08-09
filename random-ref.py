import random

players = []
dates = []

f = open('players.txt', 'r')
for line in f:
	players.append(line)
f.close()

g = open('dates.txt', 'r')
for line in g:
	dates.append(line)
g.close()

h = open('result.txt', 'w')
for date in dates:
	h.write('%s' % (date,))
	number_1 = random.randint(0,len(players)-1)
	h.write('%s' % (players[number_1],))
	players.pop(number_1)
	number_2 = random.randint(0,len(players)-1)
	h.write('%s\n' % (players[number_2],))
	players.pop(number_2)
h.close()