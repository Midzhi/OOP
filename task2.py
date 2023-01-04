# 2 1-балл
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.


class House:
    def __init__(self, type_house, total_s):
        self.type_house = type_house
        self.total_s = total_s

    def fu(self):
        fu_list = []
        for i in self.furniture.items():
            fu_list.append(i)
        return fu_list

    def info(self):
        fu_s = 0
        for i in self.furniture.values():
            fu_s += i

        remaining_s = int(self.total_s) - fu_s

        return f'Дом типа {self.type_house} общей площадью {self.total_s}, мебель {self.fu()}, оставшаяся площадь {remaining_s}'




house = House('Barnhouse', 100)
house.furniture = {'bedroom': 4, 'wardrobe': 2, 'table': 1.5}
print(house.info())

# Или же решение ниже:

# class Furniture:
#     def __init__(self, type_house, total_s, furniture={'item': 's', 'item': 's', 'item': 's'}):
#         self.type_house = type_house
#         self.total_s = total_s
#         self.furniture = furniture
#
#     def fu(self):
#         fu_list = []
#         for i in self.furniture.items():
#             fu_list.append(i)
#         return fu_list
#
#     def info(self):
#         fu_s = 0
#         for i in self.furniture.values():
#             fu_s += i
#
#         remaining_s = int(self.total_s) - fu_s
#
#         return f'Дом типа {self.type_house} общей площадью {self.total_s}, мебель {self.fu()}, оставшаяся мебель {remaining_s}'
#
#
#
#
# furnit = Furniture('Barnhouse', '100', furniture={'bedroom': 4, 'wardrobe': 2, 'table': 1.5})
# print(furnit.fu())
# print(furnit.info())
