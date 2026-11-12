import time
from datetime import datetime

import schedule


def cuckoo():
    print('Ку' * (datetime.now().hour % 12 or 12))


schedule.every().hour.at(':00').do(cuckoo)
while True:
    schedule.run_pending()
    time.sleep(1)
