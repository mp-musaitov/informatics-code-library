# ipaddress: практическая шпаргалка
# Независимые блоки: копируйте нужный вместе с импортами и данными.
# Для работы используйте solution.py в отдельной папке.
# Запуск этого файла: python -I ipaddress.py (подробнее в README).

# БЛОК 1. Сеть по адресу узла
from ipaddress import ip_network

network = ip_network('192.168.1.5/24', strict=False)
print(network.network_address)  # 192.168.1.0
print(network.netmask)  # 255.255.255.0

# БЛОК 2. Границы и размер сети
from ipaddress import ip_network

network = ip_network('192.168.1.0/30')
print(network.broadcast_address)  # 192.168.1.3
print(network.prefixlen)  # 30
print(network.num_addresses)  # 4

# БЛОК 3. Принадлежность сети
from ipaddress import ip_address, ip_network

network = ip_network('192.168.1.0/24')
print(ip_address('192.168.1.200') in network)  # True
print(ip_address('192.168.2.1') in network)  # False

# БЛОК 4. Все адреса и адреса узлов
from ipaddress import ip_network

network = ip_network('192.168.1.0/30')
print([str(address) for address in network])
# ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3']
print([str(address) for address in network.hosts()])
# ['192.168.1.1', '192.168.1.2']

# БЛОК 5. Двоичная запись из 32 бит
from ipaddress import ip_address

address = ip_address('192.168.1.1')
bits = format(int(address), '032b')
print(bits)  # 11000000101010000000000100000001
print(bits.count('1'))  # 7

# БЛОК 6. Адреса с чётным числом единиц
from ipaddress import ip_network

network = ip_network('192.168.1.0/29')
count = 0
# По условию этого примера рассматриваем ВСЕ адреса сети.
for address in network:
    bits = format(int(address), '032b')
    if bits.count('1') % 2 == 0:
        count += 1
print(count)  # 4

# Частые ошибки
# 1. Забывать strict=False, когда дан адрес узла.
# 2. Исключать первый и последний адрес, хотя требуется перебрать всю сеть.
# 3. Считать точки частью двоичного представления адреса.
# 4. Перебирать огромную сеть вместо анализа битов.
# 5. Использовать строки вместо объектов при проверке принадлежности сети.
