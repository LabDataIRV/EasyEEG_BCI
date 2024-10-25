## EasyEEG_BCI
LabData brain-computer interface

Страница проекта [Нейроинтерфейс EasyEEG BCI](https://labdata.ru/project/easyeeg-bci-project)

Обзор нейроинтерфейса EasyEEG https://labdata.ru/news/easyeeg-bci

Пример получения данных с устройства смотрите в файле EasyBCI_LSL_recive.py

[Библиотека LSL для Linux](https://www.dropbox.com/scl/fi/rfwt666hstcqp9zwt12r0/liblsl-1.16.1-jammy_amd64.deb?rlkey=bu1ie9kw79p4s9b6z5u1fo956&dl=0) (Debian дистрибутивы) Примечание: LSL поддерживается только версиями до 2.0!

# Программа для ПК

## версия 2.0b

[Windows x64](https://www.dropbox.com/scl/fi/slv7nfrhrtb5hprqo7jrg/EasyEEG_BCI_v20b_win64.zip?rlkey=ccba9s9xcigm1kumcs3laxhqj&st=zq3idgw5&dl=0) 

[Linux x64](https://www.dropbox.com/scl/fi/t685fwqinu2hl96s8ng54/EasyEEG_BCI_v20b_linux64.zip?rlkey=z6nzw7xpzc89bn0gorkft7nv1&st=0cdb0hzs&dl=0) 

Исправления, вошедшие в данный релиз:
Переход на обмен данными по широковещательному UDP протоколу. (LSL больше не поддерживается).
Передача кроме ЭЭГ, также частотных диапазонов в JSON
payload = {
        'd':int,
        'E':float,
        'd1':int,
        't1':int,
        't2':int,
        'a1':int,
        'a2':int,
        'b1': int,
        'b2': int,
        'b3': int,
        'g1': int
        }
Ускорение реакции индикатора уровня сигнала
Небольшие исправления алгоритма спектральной обработки

## версия 1.3b

[Windows x64](https://www.dropbox.com/scl/fi/fuzy3b0b5ixx3hmbpfqb3/EasyEEG_BCI_13b_win64.zip?rlkey=gjpz3iyzpmnrldffi5to7cq4t&dl=0) 

[Linux x64](https://www.dropbox.com/scl/fi/3rddho1yh9axoeipel3oi/EasyEEG_BCI_v13b_linux64.zip?rlkey=yitynu1vtjm1vyqrtmbdkhscr&dl=0) 

Исправления, вошедшие в данный релиз:
1. Увеличение диапазона спектральных параметров в отчете
2. Настройка диапазона спектра
3. Изменение шкалы уровня сигнала
4. Автоматический поиск порта
5. Отработка ошибок подключения к устройству

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
