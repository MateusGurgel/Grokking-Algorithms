stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfor"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

def get_best_station(coveredStates):
    bestStation = None
    bestStationCovered = float('inf')
     
    for station, states in stations.items():
        statesAlreadyCovered = len(states & coveredStates)

        if statesAlreadyCovered < bestStationCovered:
            bestStation = station
            bestStationCovered = statesAlreadyCovered

    return bestStation
        
def get_best_states(numberOfStations):
    bestStates = set()

    for i in range(numberOfStations):
        bestStation = get_best_station(bestStates)

        for state in stations[bestStation]:
            bestStates.add(state)
    
    return bestStates

def get_best_stations(numberOfStations):
    bestStations = set()
    bestStates = set()

    for i in range(numberOfStations):
        bestStation = get_best_station(bestStates)
        bestStations.add(bestStation)

        for state in stations[bestStation]:
            bestStates.add(state)
    
    return bestStations

print(get_best_states(4))
print(get_best_stations(4))
