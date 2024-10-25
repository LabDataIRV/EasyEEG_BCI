# Пример программы для получения данных с приложения EasyEEG BCI по протоколу UDP
# Совместим с приложением версии выше 2.0 включительно
# Входной пакет данных с включенным спектром:
# payload = {
#         'd':int, - время между измерениями в мс
#         'E':float, - значение ЭЭГ, отн.ед.
#         'd1':int, - дельта диапазон, отн. ед.
#         't1':int, - тета1 диапазон, отн. ед.
#         't2':int, - тета2 диапазон, %
#         'a1':int, - альфа1 диапазон, %
#         'a2':int, - альфа2 диапазон, %
#         'b1': int, - бета1 диапазон, %
#         'b2': int, - бета2 диапазон, %
#         'b3': int, - бета3 диапазон, %
#         'g1': int - гамма диапазон, %
#         }
# С выключенным спектром
#payload = {
#        'd':int, - время между измерениями в мс
#        'E':float, - значение ЭЭГ, отн.ед.
#        }
# LabData.ru

import socket
import json

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udp_host = '0.0.0.0'
udp_port = 2000
sock.bind((udp_host,udp_port))
bandsNames = ['d1','t1','t2','a1','a2','b1','b2','b3','g1']
bands = [0] * 9
t = 0.0
while True:
	print("Ожидание данных с устройства ...")
	data,addr = sock.recvfrom(1024)
	try:
		dt = json.loads(data.decode())["d"]
		EEG = json.loads(data.decode())["E"]
		t += dt
	except:
		EEG = 0
		dt = 0

	try:
		for bn, Name in enumerate(bandsNames):
			bands[bn] = json.loads(data.decode())[Name]
	except:
		bands = [0] * 9

	print(f"EEG= { EEG } time= { t } Bands= " + str(bands))
