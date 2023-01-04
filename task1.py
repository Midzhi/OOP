# # 1 1-балл
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.
#
# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

class Soldier:
    def __init__(self, name):
        self.name = name


class Guns(Soldier):
    def __init__(self, name, weapon, patrons):
        super().__init__(name)
        self.weapon = weapon
        self.patrons = patrons


class Act_of_Shooting(Guns):
    def shoot(self):
        weapon_patrons = self.patrons
        while True:
            print(f'Солдат {self.name} стреляет из {self.weapon}: «тиги-тигитиш»')
            weapon_patrons -= 1
            if weapon_patrons == 0:
                repeat = int(input(f'Магазин {self.weapon} пуст, перезарядить? (Да-1, Нет-0): '))
                if repeat == 1:
                    weapon_patrons = self.patrons
                    continue
                else:
                    return 'Стрельба окончена'


shooting = Act_of_Shooting('Ryan', 'AK-47', 30)
print(shooting.shoot())
