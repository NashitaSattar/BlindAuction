#Nesting

#Simple dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berline",
}

#Nesting a list in a dictionary,
#Each key can only hold one value which is a list or a dictionary
#Nesting a dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
        },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
        },
}

#Nesting a dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12 
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]
    




