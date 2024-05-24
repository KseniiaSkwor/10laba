"""Работа с JSON"""

import json
import os

from typing import Optional
from dataclasses import dataclass, asdict


JSON_PATH = os.path.join(os.getcwd(), "lab_10", "10.1.json")


@dataclass
class Product:
    """Типизация словаря продукта"""

    name: str
    price: int
    weight: int
    available: Optional[bool]


def print_product_info(product: Product):
    """Форматированный вывод информации о продукте"""
    print("Название:", product.name)
    print("Цена:", product.price, "руб.")
    print("Вес:", product.weight, "гр.")
    print("В наличии" if product.available else "Нет в наличии!")
    print("-----")


# For 10.2
def add_new_item(data):
    """Добавить новый продукт"""
    new_item_info = input("Введите через запятую значения: название,цена,вес:\n")
    try:
        new_name, new_price, new_weight = new_item_info.split(",")
        new_item = Product(
            name=new_name,
            price=int(new_price),
            weight=int(new_weight),
            available=True,
        )
        data["products"].append(asdict(new_item))

        with open(JSON_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("[ОШИБКА] Неверный ввод.")


def lab_10_1():
    """Получение и вывод JSON содержимого"""
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            products: list[dict] = data["products"]
            for p in products:
                product = Product(**p)
                print_product_info(product)

        need_add_new = input("Добавить новые товары? [y/n]: ")
        if need_add_new == "y":
            add_new_item(data)

    except OSError:
        print("[ОШИБКА] Проблемы с файламом JSON.")


def lab_10_3():
    """Чтение и запись словаря"""
    en_ru_path = os.path.join(os.getcwd(), "lab_10", "en_ru.txt")
    ru_en_path = os.path.join(os.getcwd(), "lab_10", "ru_en.txt")

    eng_dict = {}
    ru_dict = {}

    try:
        with open(en_ru_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                (eng_w_str, ru_w_str) = line.split(" - ")
                ru_words = ru_w_str.replace("\n", "").split(", ")
                eng_dict[eng_w_str] = ru_words

                for rw in ru_words:
                    if rw in ru_dict:
                        ru_dict[rw].append(eng_w_str)
                    else:
                        ru_dict[rw] = [eng_w_str]

        with open(ru_en_path, "w+", encoding="utf-8") as f:
            for ru_w, eng_w in sorted(ru_dict.items()):
                f.write(f"{ru_w} - {', '.join(eng_w)}\n")

    except OSError:
        print("[ОШИБКА] Проблемы с файлом.")


lab_10_3()