
"""
make key for second element max and min
    tup
    return tup[1]

counter number = 0 
find min and pop largest while adding to list
everytime we remove add the largest number
then add the min num to act as return
when number = 2 add the final number return number
while num in list is > 2

"""
def solve(people):
    route_list = []
    tracks = 0

    def key_help(tup):
            return tup[1]

    def find_min(lst):
        return min(lst, key=key_help)
    
    while len(people) > 2:
        helped_person = max(people, key=key_help)
        route_list.append([find_min(people)[0], helped_person[0]])
        route_list.append([find_min(people)[0]])
        tracks += helped_person[1]
        people.remove(helped_person)
        tracks += find_min(people)[1]

    tracks += max(people, key=key_help)[1]
    route_list.append([people[0][0], people[1][0]])

    
    return route_list

    

print(solve([('Alice', 1), ('Bob', 1)]))


# ("1 person", [("Alice", 2)], 2),
# ("2 people #1", [("Alice", 2), ("Bob", 1)], 2),
# ("2 people #2", [("Alice", 1), ("Bob", 1)], 1),
# ("3 people", [("Alice", 1), ("Bob", 4), ("Charlie", 5)], 10),
# ("4 people #1", [("Alice", 1), ("Bob", 4), ("Charlie", 5), ("David", 8)], 19),
# ("4 people #2", [("Alice", 1), ("Bob", 2), ("Charlie", 5), ("David", 8)], 15),
# ("6 people", [("Alice", 1), ("Bob", 4), ("Charlie", 5), ("David", 8), ("Eva", 9), ("Frank", 12)], 40),