from address import Address
from mailing import Mailing

# Создаем адрес получателя
to_addr = Address("109472", "г.Москвa", "ул. Ташкентская", "д.36", "кв.15")
# Создаем адрес отправителя
from_addr = Address("236017", "г.Калининград", "ул. Врубеля", "д.5", "кв.20")

# Создаем экземпляр Mailing
mail = Mailing(to_addr, from_addr, 1042.10, "TRACK12345XYZ")

# Вывод информации
print(
    f"\nОтправление {mail.track} :"
    f"\nиз {mail.from_address.index:<6} {mail.from_address.city:<15} "
    f"{mail.from_address.street:<15} {mail.from_address.house:<3}, {mail.from_address.apartment:<3} "
    f"\nв {mail.to_address.index:<6} {mail.to_address.city:<15} "
    f"{mail.to_address.street:<15} {mail.to_address.house:<3} , {mail.to_address.apartment:<3} "
    f"\nСтоимость {mail.cost:.2f} р"
)