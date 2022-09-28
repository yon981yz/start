# from random import *
# cnt = 0
# for customer in range(1,51) :
#     time = randrange(1,51)
#     if time >= 5 and time <= 15 :
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
#         cnt += 1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
# print("총 탑승 승객 : {}분".format(cnt))

    
# from random import *
# time = int(randrange(1,50))
# print(time)

# for customer in range(1,50) :
#     if time >= 5 and time <= 15 :
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
#         continue
#     else:print("[] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))

# from random import randrange


# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
    
# print("총 탑승 승객 : {}분".format(cnt))

# from random import * 
# cnt =  0 
# for customer in range(1, 51):
#     time = randrange(1, 51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
#         cnt += 1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
# print("총 탑승 승객 : {}분".format(cnt))

# def std_weight(height, gender):
#     if gender == "남자":
#         print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height, height*height*22))
#         return height*height*22
#     elif gender == "여자":
#         print("키 {0}cm 여자의 표준 체중은 {1:.2f}kg 입니다.".format(height, height*height*21))
#         return height*height*21

# height = 1.80
# height = std_weight(1.80, "남자")

# height = std_weight(1.6, "여자")

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "여자"
# weight = round(std_weight(height / 100, gender),2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# score_file = open("1주차.txt", "w", encoding="utf8")
# print("- X 주차 주간보고 -", file=score_file)
# print("부서 :", file=score_file)
# print("이름 :", file=score_file)
# print("엄무 요약 :", file=score_file)
# score_file.close()

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서:")
#         report_file.write("\n이름:")
#         report_file.write("\n엄무 요약:")

# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year


#     def show_detail(self):
#         print(self.location, self.house_type,\
#             self.deal_type, self.price, self.completion_year)



# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)


# print("총 {0}대의 매물이 있습니다".format(len(houses)))
# for house in houses:
#     house.show_detail()


# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 : {0}".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order < 1:
#             raise ValueError 
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#                 raise SoldOutError

#     except ValueError:
#         print("잘못된 값을 입력하셨습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# import byme
# byme.sign()

