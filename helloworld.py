# from random import *
# id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(id)

# print("-- 당첨자 발표 --")
# winner = int(random()*21)
# print("치킨 당첨자 :", winner)
# id.remove(winner)

# print("커피 당첨자 :", sample(id, 3))
# print("-- 축하합니다 --")

from random import *
id = range(1,21)
# print(type(id)) 타입이 range이므로 list로 변경해주기

id = list(id)
shuffle(id)

winners = sample(id, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

print("신입이 쓴 글입니다.")
print("모두 방가방가")