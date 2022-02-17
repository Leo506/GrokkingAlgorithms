#!/bin/python3

# Поиск в ширину
# Выполняется за O(V+E), где V-кол-во вершин, E-кол-во ребер
# Помогает ответить на 2 типа вопроса:
# 1. Если путь от узла А к узлу В?
# 2. Какой кратчайший путь от A до B?

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"]  =[]
graph["jonny"] = []

def personIsSeller(person):
    return person[-1] == 'm'

def search(name):
    searchQueue = deque()
    searchQueue += graph[name]
    searched = []  # Этот массив используется для отслеживания уже проверенных людей
    while searchQueue:  # Пока очередь не пуста
        person = searchQueue.popleft()  # Из очереди извлекается первый человек
        if not person in searched:
            if personIsSeller(person):  # Проверяем, является ли человек продавцом
                print(person + " is a mango seller")
                return True
            else:
                searchQueue += graph[person]  # Если не является, то добавляем всех его друзей в очередь
                searched.append(person)  # Человек помечается как проверенный
    return False

search("you")
