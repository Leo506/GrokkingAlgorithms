#!/bin/python3

# Алгоритм Дийкстры
# Используется для поиска кратчайшего пути во взвешанных графах
# кратчайший путь - путь с наименьшим весом
# ВНИМАНИЕ: нельзя использовать с отрицательными весами и циклическими графами

graph = {}    # Хеш-таблица, представляющая граф
costs = {}    # Хеш-таблица, представляющая стоимость перехода
parents = {}  # Хеш-таблицв, представляющая родителей узлов

graph["start"] = { "a" : 6, "b" : 2 }
graph["a"] = { "finish" : 1 }
graph["b"] = { "a" : 3, "finish" : 5 }
graph["finish"] = {}

costs = { "a" : 6, "b" : 2, "finish" : float("inf") }

parents = { "a" : "start", "b" : "start", "finish" : None }

processed = []


''' Функция находит ближайший узел '''
def find_lowest_cost_node():
    cost = float("inf")
    node = None
    for n in costs:
        if costs[n] < cost and n not in processed:
            cost = costs[n]
            node = n
    return node


node = find_lowest_cost_node()
while node is not None:
    cost = costs[node]  # Стоимость текущего узла
    # Проходим всех соседей узла
    for n in graph[node]:
        new_cost = cost + graph[node][n]

        # Если новая стоимость меньше старой стоимости, то мы нашли более короткий путь
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node()


print(parents)

