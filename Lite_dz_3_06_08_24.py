class NegativeNumberError(Exception):
    """
    Класс собственного исключения для обработки отрицательных чисел.
    Наследуется от базового класса Exception.

    Атрибуты:
    value: Значение отрицательного числа, которое вызвало исключение.
    messege: Сообщение об ошибке, описывающее причину исключения.
    """

    def __init__(self, value, message="Число не должно быть отрицательным."):
        """
        Конструктор класса NegativeNumberError.
       
        Аргументы:
        value: Значение отрицательного числа.
        message: Сообщение об ошибке (по умолчанию "Число не должно быть отрицательным.").
        """
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        Переопределение метода __str__ для вывода информативного сообщения об ошибке.
        """   
        return f'{self.value} -> {self.message}'  
    
def check_positive_number(number):
    """
    Функция проверяет, является ли число положительным.
    Если число отрицательное, вызывает исключение NegativeNumberError.

    Аргументы:
    number: Число для проверки.
    
    Исключения:
    NegativeNumberError: Если число отрицательное.
    """
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(f"{number} является положительным числом.") 
        return True

# Проверка функции с отрицательным числом
try:
    check_positive_number(-10)    
except NegativeNumberError as e:
    print(e)

# Проверка функции с положительным числом
try:
    check_positive_number(10)
except NegativeNumberError as e:
    print(e)    