# # 4 1-балл
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:
#
# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"
#
# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()
#
# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

class MoneyFmt:
    def __init__(self, value):
        self.value = value

    def update(self, new_value):
        self.value = new_value

    def __str__(self):
        self.value = round(float(self.value), 2)
        self.value = list(str(self.value))
        for i in range(self.value.index('.') - 3, 0, -3):
            self.value.insert(i, ',')

        if self.value[0] == '-' and self.value[1] == ',':
            del self.value[1]
            self.value.insert(1, '$')
        elif self.value[0] == '-':
            self.value.insert(1, '$')
        else:
            self.value.insert(0, '$')

        result = ''.join(self.value)
        self.result = result

        return str(self.result)

    def __repr__(self):
        return repr(self.result)


money = MoneyFmt(-1123456.3)
print(money)
money.update(-0.3)
print(money)
