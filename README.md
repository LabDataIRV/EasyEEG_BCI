## EasyEEG_BCI
LabData brain-computer interface

Страница проекта https://labdata.ru/project/easyeeg_project

Обзор нейроинтерфейса EasyEEG https://labdata.ru/news/easyeeg-bci

Пример получения данных с устройства смотрите в файле EasyBCI_LSL_recive.py

# Программа для ПК

## версия 1.2b

[Windows x64](https://www.dropbox.com/scl/fi/2tv0l7xn5vmd1r1m6364q/EasyEEG_BCI_v12b_win64.zip?rlkey=neye4mulpv6xtaym7quazdxwa&dl=0) 

[Linux x64](https://www.dropbox.com/scl/fi/n6ies7edlvg3k0enhck0x/EasyEEG_BCI_v12b_linux64.zip?rlkey=ubajs2p8evbolvufznqjjlale&dl=0) 

Исправления, вошедшие в данный релиз:
1. Исправление пропуска столбца времени в запись частотных диапазонов
   
## версия 1.0b

[Windows x64](https://www.dropbox.com/s/ag5dv3c3kozduou/EasyEEG_BCI_100b.exe?dl=0)

[Linux x64](https://www.dropbox.com/s/tgb8ponckw0djw0/EasyEEG_BCI_100b?dl=0)

Исправления, вошедшие в данный релиз:
1. Добавлена функция отключения фильтров
2. Добавлена инерция спектра с настройкой из интерфейса
3. Перекрашивание частотных диапазонов
4. Добавлен вывод спектра сигнала.
5. Изменен диапазон частот с 40 до 45 Гц.
6. Изменен расчет амплитудного спектра на спектр мощности (квадрат амплитуд)
7. Изменен способ нормирования спектра с 7 по 45 Гц для компенсации влияния НЧ артефактов
8. Изменен способ сохранения файла ЭЭГ - фильтрованный сохраняется при включенном фильтре, иначе - сырой
9. Добавление возможности отключения спектра
10. Добавление контроль уровня сигнала
11. Добавление передачи данных через LSL
12. Добавление сохранения частотных диапазонов в файл

## версия 0.0a

[Windows x64](https://www.dropbox.com/s/trxjl37eypg8op5/EasyEEG_BCI_v00a_win.zip?dl=0)

[Linux x64](https://www.dropbox.com/s/rs5n1t0aadqs976/EasyEEG_BCI_v00a_linux.zip?dl=0)
