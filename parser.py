import sys
from csv import reader
from device_detector import DeviceDetector


def is_bot(ua: str) -> bool:
    try:
        return DeviceDetector(ua).parse().is_bot()
    except:
        return False

filename = sys.argv[1]
with open(filename, 'r') as csv_file:
    print("userAgent,is_bot")
    csv_reader = reader(csv_file)
    next(csv_reader, None)
    for row in csv_reader:
        print(f"\"{row[0]}\",{is_bot(row[0])}")
