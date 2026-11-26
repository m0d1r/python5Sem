import random


def first_fit(items, capacity=1.0):
    bins = []
    for item in items:
        placed = False
        for i in range(len(bins)):
            if round(bins[i] + item, 6) <= capacity:
                bins[i] = round(bins[i] + item, 6)
                placed = True
                break
        if not placed:
            bins.append(item)
    return len(bins)


def best_fit(items, capacity=1.0):
    bins = []
    for item in items:
        best_idx = -1
        min_space_left = capacity + 1
        for i in range(len(bins)):
            space_left = round(capacity - (bins[i] + item), 6)
            if 0 <= space_left < min_space_left:
                min_space_left = space_left
                best_idx = i
        if best_idx != -1:
            bins[best_idx] = round(bins[best_idx] + item, 6)
        else:
            bins.append(item)
    return len(bins)


def next_fit(items, capacity=1.0):
    if not items:
        return 0
    bins_count = 1
    current_load = 0.0
    for item in items:
        if round(current_load + item, 6) <= capacity:
            current_load = round(current_load + item, 6)
        else:
            bins_count += 1
            current_load = item
    return bins_count


def worst_fit(items, capacity=1.0):
    bins = []
    for item in items:
        worst_idx = -1
        max_space_left = -1.0
        for i in range(len(bins)):
            space_left = round(capacity - (bins[i] + item), 6)
            if space_left >= 0 and space_left > max_space_left:
                max_space_left = space_left
                worst_idx = i
        if worst_idx != -1:
            bins[worst_idx] = round(bins[worst_idx] + item, 6)
        else:
            bins.append(item)
    return len(bins)


if __name__ == "__main__":
    sample = [0.5, 0.7, 0.3, 0.9, 0.6, 0.8, 0.1, 0.4, 0.2, 0.5]
    print("Тест на примере из методички (ожидается 6, 5, 7, 7):")
    print(f"First Fit: {first_fit(sample)}, Best Fit: {best_fit(sample)}, "
          f"Next Fit: {next_fit(sample)}, Worst Fit: {worst_fit(sample)}\n")

    print(f"{'Кол-во':<8} | {'Первый (FF)':<12} | {'Наиболее (BF)':<14} | {'Следующий (NF)':<15} | {'Наименее (WF)':<14}")
    print("-" * 72)
    for count in [50, 100, 200, 500]:
        random_items = [round(random.uniform(0.1, 0.9), 1) for _ in range(count)]
        ff = first_fit(random_items)
        bf = best_fit(random_items)
        nf = next_fit(random_items)
        wf = worst_fit(random_items)
        print(f"{count:<8} | {ff:<12} | {bf:<14} | {nf:<15} | {wf:<14}")
