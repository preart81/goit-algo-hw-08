"""
Знайти порядок об'єднання, який мінімізує загальні витрати.
 
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз
в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших
витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а
загальні витрати дорівнюють сумі з'єднання всіх кабелів."""

import heapq

set


def merge_cables(cables: list, debug: bool = False) -> tuple:
    """
    Об'єднує кабелі з метою мінімізації загальних витрат

    Параметри:
        cables (list): список кабелів (кожен елемент - довжина кабеля)
        debug (bool): флаг для виводу додаткової інформації
    """
    merge_order = []
    heap = cables.copy()
    heapq.heapify(heap)
    if debug:
        print("Початковий стан купи:")
        print(f"{heap}")
        print("Обрахунок витрат:")
        print(f"{'сума':>5} | {'відрізки '} | {'стан купи'}")

    total_cost = 0
    while len(heap) > 1:
        cost1, cost2 = heapq.heappop(heap), heapq.heappop(heap)
        total_cost += cost1 + cost2
        merge_order.append((cost1, cost2))
        heapq.heappush(heap, cost1 + cost2)
        if debug:
            print(f"{total_cost:>5} | {cost1:>3} + {cost2:>3} | {heap}")

    return merge_order, total_cost


if __name__ == "__main__":
    cables = [5, 8, 12, 13, 2, 1, 4]
    # cables = [-5, -8, -12, -13, -2, -1, -4]
    print(f"Відкрізки кабелів:\n{cables}")

    merge_order, total_cost = merge_cables(cables, debug=True)

    print(f"Порядок об'єднання кабелів: {merge_order}")
    print(f"Загальні витрати: {total_cost}")
    print(f"{cables = }")
