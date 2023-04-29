"""Пример программы для получения многоканальных данных по протоколу LSL"""

from pylsl import StreamInlet, resolve_stream

def main():
    print("Ожидание данных...")
    streams = resolve_stream('type', 'EEG') # Ищем нужный сигнал
    # Создаем вход для получения данных
    inlet = StreamInlet(streams[0])

    while True:
        # Получение нового измерения
        sample, timestamp = inlet.pull_sample()
        print(timestamp, sample)

if __name__ == '__main__':
    main()