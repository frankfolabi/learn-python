spike = {
    'owner' :'segun',
    'kind' : 'eskimo',
    }

blac = {
    'owner' : 'ope',
    'kind' : 'eskimo',
    }
rocky = {
    'owner' : 'sally',
    'kind' : 'aus'
}

pets = [spike, blac, rocky]

for pet in pets:
    owner = (pet['owner'])
    kind = (pet['kind'])
    print(f"{owner.title()} owns an {kind.title()} dog.")
    
