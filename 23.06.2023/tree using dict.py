#Dictionary (forest of 3 trees:)
Families={
    'Sharley':
    {'Sam':{'Boxy','Rosy'},
     'Nila':{'Pepsi'}},
    'Devi':
    {'Tommy':{'Tony'},
     'Timmy':{'Hamster'},
     'Tammy':{'Hamster'}},
    'Carlos':
    {'Diego':'Cat','Ferret':'Fox'}
    }
for Parent, Children in Families.items():
    print(f"{Parent} has {len(Children)} kid(s):")
    print(f"{',and '.join([str(Child) for Child in[*Children]])}")
    
    
