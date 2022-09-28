class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}방향으로 이동합니다. [속도{2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, dmg):
        print("{0} : {1}데미지를 입었습니다.".format(self.name, dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp >= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))



# Marine = Unit("마린", 40, 10)
# print(Marine)