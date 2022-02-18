# Жадный алгоритм
# Используется для решения NP-полных задач

# Штаты, которые нужно покрыть
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Радиостанции и штаты, которые они покрывают
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

best_station = None  # Станция, покрывающая наибольшее кол-во штатов
states_covered = set()  # Множество штатов, которое покрывает best_station

result = []

while states_needed:
    best_station = None  # Станция, покрывающая наибольшее кол-во штатов
    states_covered = set()  # Множество штатов, которое покрывает best_station
    
    for station, states in stations.items():
        covered = states & states_needed
        if len(covered) > len(states_covered):
            states_covered = covered
            best_station = station
    
    result.append(best_station)
    states_needed -= states_covered

print(result)