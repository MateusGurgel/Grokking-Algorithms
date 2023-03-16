from collections import deque

graph = {}
graph["You"] = ["Alice", "Bob", "Enzo Santos"]

graph["Alice"] = ["João Flamengo", "Jonathans Corintians"]
graph["Bob"] = ["Kevin", "John"]
graph["Enzo Santos"] = ["Guilherme Coutinho", "Alessandro"]
graph["Guilherme Coutinho"] = ["Alessandro"]

graph["João Flamengo"] = []
graph["Jonathans Corintians"] = []
graph["Guilherme Coutinho"] = []
graph["Kevin"] = []
graph["Alessandro"] = []
graph["John"] = []

def BSF(name):
    searchQueue = deque(graph["You"])
    verified  = []

    while searchQueue:
        people = searchQueue.popleft()

        if people in verified:
            continue

        if people == name:
            return True
        else:
            searchQueue += graph[people]
            verified.append(people)
    
    return False

name = "João Flamengo"
result = BSF(name)

print("is there a person named {} in your social networks? : {} ".format(name, result ))









