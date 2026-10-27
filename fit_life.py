# Проект FitLife - MVP версия 1.0


def fit_life(weight, height):
    """Рассчитывает индекс массы тела и норму воды."""
    bmi = weight / (height**2)

    # Подсчет воды: вес * 30 мл
    # TODO: Рассчитай water_needed
    water_needed = weight * 30
    water_l = water_needed / 1000
    return bmi, water_l


prompt_text = [
    'Напишите ваше имя:\nНапример "Андрей"\n',
    'А теперь возраст:\nДопустим "19"\n',
    'Можно узнать ваш вес:\nНужна информация в "65" кг\n',
    'Также потребуется рост:\nВ метрах "1.75" через точку\n',
]


def main():
    """Запускает опрос пользователя и выводит итоговый фитнес-отчет."""
    # 1. Знакомство
    # TODO: Спроси у пользователя имя и сохрани в переменную user_name
    # TODO: Спроси возраст и сохрани в переменную user_age
    user_name = input(prompt_text[0]).strip()
    user_age = int(input(prompt_text[1]))

    # 2. Сбор данных
    # TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
    # TODO: Запроси рост (в метрах) и сохрани в user_height (тип float)
    user_weight = float(input(prompt_text[2]))
    user_height = float(input(prompt_text[3]))

    # Расчет параметров
    bmi, water_l = fit_life(user_weight, user_height)

    # 4. Вывод красивого результата
    # TODO: Используй f-строку, чтобы вывести приветствие
    # TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
    print(f"\nПривет, {user_name}!")

    border = "-" * 40
    print(
        f"{border}\n"
        f"Отчет для пользователя: {user_name} ({user_age} г.)\n"
        f"Твой Индекс Массы Тела: {round(bmi, 1)}\n"
        f"Рекомендуемая норма воды: {round(water_l, 1)} л. в день\n"
        f"{border}\n"
        f"Расчет окончен. Будьте здоровы!\n",
    )


if __name__ == "__main__":
    main()
