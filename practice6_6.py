from random import *
count = 0

for passenger in range(1, 51) :
    time = randrange(5, 51)
    if 5 <= time <= 15 :
        count += 1
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(passenger, time))
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(passenger, time))

print("총 탑습 승객 : {0} 분".format(count))