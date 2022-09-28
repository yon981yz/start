from random import *

class Unit: 
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [소도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, dmg):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

class Attackunit(Unit):
    def __init__(self, name, hp, speed, dmg):
        Unit.__init__(self, name, hp, speed)
        self.dmg = dmg
    
    def atk(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.dmg))

class Marine(Attackunit):
    def __init__(self):
        Attackunit.__init__(self, "마린", 40, 1, 5)

    def Stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않았습니다."\
                .format(self.name))

class Tank(Attackunit):
    seize_developed = False

    def __init__(self):
        Attackunit.__init__(self, "탱크", 150, 1, 150)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.dmg *= 2
            self.seize_mode = True

        else:
            print("{0} : 시즈보드를 해제합니다.".format(self.name))
            self.dmg /= 2
            self.seize_mode = False


class Flyable(Unit): 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format\
            (name, location, self.flying_speed))

class Flyableatkunit(Attackunit, Flyable):
    def __init__(self, name, hp, dmg, flying_speed):
        Attackunit.__init__(self, name, hp, 0, dmg)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(Flyableatkunit):
    def __init__(self):
        Flyableatkunit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 실행합니다".format(self.name))
            self.clocked = True


# class Buildingunit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

# supply_depot = Buildingunit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

atk_units = []
atk_units.append(m1)
atk_units.append(m2)
atk_units.append(m3)
atk_units.append(t1)
atk_units.append(t2)
atk_units.append(w1)

for unit in atk_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in atk_units:
    if isinstance(unit, Marine):
        unit.Stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in atk_units:
    unit.atk("1시")

for unit in atk_units:
    unit.damaged(randint(5, 21))



game_over()

