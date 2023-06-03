import csv
import time
from datetime import datetime

with open('rows_300.csv', mode='w', newline='') as csv_file:
    fieldnames = ['№', 'Дата и время', 'Секунда', 'Микросекунда']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()

    for i in range(1, 301):
        now = datetime.now()
        second = now.second
        microsecond = now.microsecond

        writer.writerow({'№': i, 'Дата и время': now, 'Секунда': second, 'Микросекунда': microsecond})

        time.sleep(0.01)