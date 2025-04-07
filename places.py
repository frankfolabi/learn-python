favorite_places = {
                'di' : ['kaduna', 'zaria', 'abuja'],
                'drugs' : ['ota', 'yola', 'kano'],
                'rnk' : ['ibadan', 'benin', 'oyo'],
                }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
        print(place.title())
