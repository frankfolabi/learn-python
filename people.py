people = {
        'rnk' : {
            'first' : 'frank',
            'last' : 'afolabi',
            'cong' : 'new bodija',
            'status' : 'elder',
                },
        'sally' : {
            'first' : 'salome',
            'last' : 'afolabi',
            'cong' : 'new bodija',
            'status' : 'regular pioneer',
                },
        'drugs' : {
            'first' : 'femi',
            'last' : 'afolabi',
            'cong' : 'ifesowapo',
            'status' : 'elder',
                },
        'em' : {
            'first' : 'alice',
            'last' : 'afolabi',
            'cong' : 'durbar',
            'status' : 'publisher',
                },
        'di' : {
            'first' : 'dorcas',
            'last' : 'ogu',
            'cong' : 'kumin mashi',
            'status' : 'publisher',
                },
        'nduka' : {
            'first' : 'courage',
            'last' : 'etieh',
            'cong' : 'park',
            'status' : 'elder',
                },
        }

for nickname, person_data in people.items():
    full_name = f"{person_data['first']} {person_data['last']}"
    congregation = person_data['cong']
    status = person_data['status']
    print(f"My name is {full_name.title()}.\nI'm privileged to serve as a "
       f"{status} with {congregation.title()} congregation. Some friends "
       f"call me {nickname}\n")
