import random
from task4 import Queue


def car_wash_simulation(total_minutes=20):
    wash_queue = Queue()
    current_car = None
    busy_until = 0
    car_id = 0
    served = 0
    total_wait = 0

    for minute in range(total_minutes):
        arrivals = random.randint(0, 2)
        for _ in range(arrivals):
            car_id += 1
            wash_queue.enqueue((car_id, minute))
            print(f"мин {minute:2}: машина #{car_id} встала в очередь")

        if current_car is None and not wash_queue.is_empty():
            cid, arr = wash_queue.dequeue()
            wait = minute - arr
            total_wait += wait
            current_car = cid
            busy_until = minute + random.randint(2, 5)
            print(f"мин {minute:2}: мойка начала машину #{cid} (ждала {wait} мин)")

        if current_car is not None and minute >= busy_until:
            print(f"мин {minute:2}: машина #{current_car} вымыта")
            served += 1
            current_car = None

    print(f"\nОбслужено: {served}")
    if served:
        print(f"Среднее время ожидания: {total_wait / served:.2f} мин")
    print(f"Осталось в очереди: {wash_queue.size()}")


def run_tests():
    random.seed(1)
    car_wash_simulation(total_minutes=20)


if __name__ == "__main__":
    run_tests()