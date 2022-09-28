# from random import *

# population = range(1, 21)
# population = list(population)
# print(type(population))
# shuffle(population)
# print(population)

# sample = sample(population,4)

# print("--당청자 발표--")
# print("치킨 당첨자 : {}".format(sample[0]))
# print("커피 당첨자 : {}".format(sample[1:4]))
# print("--축하합니다--")


# url = "http://google.com"
# url = url.replace("http://","")
# print(url)

# url = url[:url.index(".")]

# print(url)

# print(url[0:3] + str(len(url)) + str(url.count("e")) + "!")

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -\n".format(i))
#         report_file.write("부서 :\n")
#         report_file.write("이름 :\n")
#         report_file.write("임무 요약 :")

class Unit:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print("{0}이 생성되었습니다".format(self.name))
        print("체력 {0} 공격력 {1} ".format(self.hp, self.dmg))

    def atk(self, location):
        print("{0} : {1}시 반향으로 공격합니다. [공격력 {2}]".format\
            (self.name, location, self.dmg))
        
    def damaged(self, dmg):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, self.dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파과되었습니다.".format(self.name))


marine1 = Unit("마린", 40, 6)
marine1.atk("1시")
marine1.damaged(25)
marine1.damaged(25)

        
