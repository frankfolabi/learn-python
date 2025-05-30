# Dictionary inside dectionary
users = {
        'aeinstien' : {
            'first' : 'albert',
            'last' : 'einstien',
            'location' : 'princeton',
            },
        'mcurie' : {
            'first' : 'marie',
            'last' : 'curie',
            'location' : 'paris',
            },
        }

for username, user_info in users.itmes():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}" 
    # Note: A variable was used store then f-string to join two spaces values
    location = user_info['location']
    
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
