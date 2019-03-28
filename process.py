import os
import os.path
import json

# str -> List[Entry]
# Entry = (lot_type, total_lots, lots_available, ...)
carparks = {}

for x in os.listdir('raw'):
    with open(os.path.join('raw', x), 'r') as f:
        y = json.load(f)
    for carpark_data in y['items'][0]['carpark_data']:
        carpark_number = carpark_data['carpark_number']
        if carpark_number not in carparks:
            carparks[carpark_number] = []
        items = carparks[carpark_number]
        myitem = [carpark_data['update_datetime']]
        for z in carpark_data['carpark_info']:
            myitem.append(z['lot_type'])
            myitem.append(z['total_lots'])
            myitem.append(z['lots_available'])
        items.append(myitem)

for k, items in carparks.items():
    items.sort()
    with open('out/{}.csv'.format(k), 'w') as f:
        for x in items:
            f.write(','.join(str(z) for z in x) + '\n')
