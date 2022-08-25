def std_weight(height, gender):
    height /= 100
    if gender == "남자" or gender == "남" :
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(round(height*100), round(height * height * 22, 2)))
    elif gender == "여자" or gender == "여": 
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(round(height*100), round(height * height * 21, 2)))
    else : 
        print("성별을 잘못 입력했습니다.")

height = int(input("키를 적으시오: "))
gender = input("성별을 적으시오: ")

std_weight(height, gender)