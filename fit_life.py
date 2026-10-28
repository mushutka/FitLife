# Проект FitLife - MVP версия 1.0
def calculation_index(weight, height):
    """Рассчитывает индекс массы тела и норму воды."""
    bmi = weight / (height ** 2)
    # Подсчет воды: вес * 30 мл
    water_needed = weight * 30
    water_l = water_needed / 1000
    return bmi, water_l

def age_adaptation(years):
    """Адаптируем окончание возраста"""
    last_digit = years % 10
    if 11 <= years <= 19:
        age = "лет"
    if last_digit == 1:
        age = "год"
    elif 2 <= last_digit <= 4:
        age = "года"
    else:
        age = "лет"
    return age

prompt_text = [
    'Напишите ваше имя:\nНапример "Андрей"\n',
    'А теперь возраст:\nДопустим "19"\n',
    'Можно узнать ваш вес:\nНужна информация в "65" кг\n',
    'Также потребуется рост:\nВ метрах "1.75" через точку\n',
]

def main():
    """Запускает опрос пользователя и выводит итоговый фитнес-отчет."""
    # 1. Знакомство
    user_name = input(prompt_text[0]).strip()
    user_age = int(input(prompt_text[1]))
    # 2. Сбор данных
    user_weight = float(input(prompt_text[2]))
    user_height = float(input(prompt_text[3]))
    # Расчет параметров
    bmi, water_l = calculation_index(user_weight, user_height)
    age = age_adaptation(user_age)
    # 4. Вывод красивого результата
    print(f"\nПривет, {user_name}!")
    border = '-' * 40
    print(
        f'{border}\n'
        f'Отчет для пользователя: {user_name} ({user_age} {age}.)\n'
        f'Твой Индекс Массы Тела: {round(bmi, 1)}\n'
        f'Рекомендуемая норма воды: {round(water_l, 1)} л в день\n'
        f'{border}\n'
        f'Расчет окончен. Будьте здоровы!\n',
    )
# Я скопировал пример вывода из задания по этому там тоже надо исправить. )
if __name__ == '__main__':
    main()