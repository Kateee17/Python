from address import Address
from mailing import Mailing

to_address = Address("100000", "Москва", "Тверская", "1", "10")
from_address = Address("200000", "Санкт-Петербург", "Невский", "50", "5")

mailing = Mailing(to_address, from_address, 150.00, "TRK123456")

print(mailing)