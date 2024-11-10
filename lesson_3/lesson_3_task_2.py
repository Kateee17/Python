from smartphone import Smartphone

# Создаем список с экземплярами класса Smartphone
catalog = [
    Smartphone('Apple', 'iPhone 14', '+79161234567'),
    Smartphone('Samsung', 'Galaxy S22', '+79012345678'),
    Smartphone('Xiaomi', 'Mi 11', '+79876543210'),
    Smartphone('Google', 'Pixel 6', '+79567890123'),
    Smartphone('OnePlus', '9 Pro', '+79456789012'),
]

# Печатаем весь каталог
for smartphone in catalog:
    print(smartphone)