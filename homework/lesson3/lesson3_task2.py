from smartphone import Smartphone

catalog = [
    Smartphone("Huawei", "Pura P80 Pro", "+7(916)234-42-11"),
    Smartphone("Huawei", "P80 Ultra", "+7(926)564-17-49"),
    Smartphone("Huawei", "Pura P80 ", "+7(977)984-20-14"),
    Smartphone("Huawei", "Mate XT ULTIMATE DESIGN", "+7(999)977-88-12"),
    Smartphone("Huawei", "Mate 70 Pro", "+7(906)356-03-95")
]


def add_elem(count=5):
    print("Заполните каталог телефонов.")
    for i in range(count):
        print(f"\nВведите элемент {i + 1} из {count}:")
        brand = input("Бренд: ")
        model = input("Модель: ")
        number = input("Номер: ")
        catalog.append(Smartphone(brand, model, number))
        print("Элемент добавлен в список.")


def show_list():
    print("\nКаталог:")
    for phone in catalog:
        print(f"{phone.ph_brand:<{len(phone.ph_brand)}} - {phone.ph_model:<5}. {phone.ph_number}")


print("Хотите добавить еще телефонов вручную?(уes/no)")
if (input(">") == "yes"):
    add_elem()


show_list()
