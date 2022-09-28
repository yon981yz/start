name = "마린"
hp = 40
dmg =  5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력{0}, 공격력 {1}\n".format(hp, dmg))

tank_name = "탱크"
tank_hp = 150
tank_dmg = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력{0}, 공격력 {1}\n".format(tank_hp, tank_dmg))

tank2_name = "탱크"
tank2_hp = 150
tank2_dmg = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력{0}, 공격력 {1}\n".format(tank2_hp, tank2_dmg))

def atk(name, location, dmg):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
        name, location, dmg))

atk(name, "1시",dmg)
atk(tank_name, "1시", tank_dmg) 
atk(tank2_name, "1시", tank2_dmg)    

class Unit: 
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp, self.dmg))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력: {1}".format(wraith1.name, wraith1.dmg))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

class Attackunit:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
    
    def atk(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.dmg))
    
    def damaged(self, dmg):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

firebat1 = Attackunit("파이어뱃", 50, 16)
firebat1.atk("5시")

firebat1.damaged(25)
firebat1.damaged(25)



class Unit: 
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [소도 {2}]"\
            .format(self.name, location, self.speed))

class Attackunit(Unit):
    def __init__(self, name, hp, speed, dmg):
        Unit.__init__(self, name, hp, speed)
        self.dmg = dmg
    
    def atk(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.dmg))
    
    def damaged(self, dmg):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

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

valkyrie = Flyableatkunit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


vulture = Attackunit("벌처", 80, 10, 20)

battlecruiser = Flyableatkunit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("11시")

class Buildingunit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

supply_depot = Buildingunit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    pass

game_start()
game_over()

