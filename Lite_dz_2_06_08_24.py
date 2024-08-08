def validate_user_input(data):
    """
    Функция проверяет, является ли входное значение словарём с корректными ключами 'name' и 'age'. Генерирует исключения при некорректных данных.
    
    Аргументы:
    data: словарь с данными пользователя, который должен содержать ключи 'name' и 'age'.
    
    Исключения:
    TypeError: если входное значение не является словарём.
    ValueError: если отсутствует ключ 'name', его значение не является строкой,
                отсутствует ключ 'age' или его значение не является положительным числом.
    """
    # Проверка, является ли data словарём
    if not isinstance(data, dict):
        raise TypeError("Входные данные должны быть словарём.")
    
    # Проверка наличия ключа 'name' и того, что его значение является строкой
    if 'name' not in data:
        raise ValueError("Ключ 'name' отсутствует в данных.")
    if not isinstance(data['name'], str):
        raise ValueError("Значение ключа 'name' должно быть строкой.")
    
    # Проверка наличия ключа 'age' и того, что его значение является положительным числом
    if 'age' not in data:
        raise ValueError("Ключ 'age' отсутствует в данных.")
    if not (isinstance (data['age'], int) and data['age'] > 0):
        raise ValueError("Значение ключа 'age' должно быть положительным целым числом.")
    
    print("Данные пользователя валидны.")
    return True 

# Проверка функции с корректными данными
try:
    validate_user_input({"name": "Alice", "age": 30})
except Exception as e:
    print(e)

# Проверка функции с отсутствующим ключом 'name'
try:
    validate_user_input({"age": 30})
except Exception as e:
    print(e)

# Проверка функции с некоректным значением для 'age'
try:
    validate_user_input({"name": "Alice", "age": -5})
except Exception as e:  
    print(e)      


    
