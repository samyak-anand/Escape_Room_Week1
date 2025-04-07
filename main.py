"""
Defining all the necessary dictionaries for Escape Room objects.

Listed dictionaries include:
    1. Couch = couch
    2. Bed = bed
    3. Piano = piano
    4. Dining Table = dining_table
    7. Keys = key_A, key_C, key_D
    8. Rooms = game_room, bedroom_1, bedroom_2, living_room, outside
"""

# Creating dictionaries
couch = {'name': 'Couch', 
         'type': 'furniture'}

piano = {'name': 'Piano',
         'type': 'instrument'}
game_room = {"name": "Game Room",
             "type": "room"}
key_A = {'name': 'Key A',
         'type': 'key',
         'target': 'Door A'}

# Bedroom 2 
bedroom_2 = {'name': 'Bedroom 2',
             'type': 'room' }
double_bed = {'name': 'Double Bed',
       'type': 'furniture'}
dresser = {'name': 'Dresser',
           'type': 'furniture'}
key_C = {'name': 'Key C',
         'type': 'key',
         'target': 'Door C'}
key_D = {'name': 'Key D',
         'type': 'key',
         'target': 'Door D'}

#Living Room 

living_room = {'name': 'Living Room',
             'type': 'room' }  
dining_table = {'name': 'Dining Table',
       'type': 'furniture'}

# Outside
outside = {'name': 'Outside'}

#Doors 

door_A = {'name': 'Door A',
          'type': 'door',
          'locked': True,
          'key': 'key_A'}
door_B= {'name': 'Door B',
          'type': 'door',
          'locked': True,
          'key': 'key_B'}
door_C = {'name': 'Door C',
          'type': 'door',
          'locked': True,
          'key': 'key_C'}
door_D = {'name': 'Door D',
          'type': 'door',
          'locked': True,
          'key': 'key_D'}

# Bedroom 1
bedroom_1 ={'name': ''}


"""
since we define all the dictionaries

"""
#defining all room objects
all_rooms = ['game_room', 'bedroom_1', 'bedroom_2', 'living_room', 'outside']
all_doors= ['door_A', 'door_B','door_C', 'door_D']

# Defining the relation between the object and rooms
object_relations = {
    'game_room': [couch,piano,door_A],
    'piano' :  [key_A],
    'doorA': [game_room,bedroom_1],
    'bedroom_2': [double_bed,dresser,door_B],
    'double_bed': [key_C],
    'dresser': [key_D],
    'doorB': [bedroom_1,bedroom_2],
    'living_room': [dining_table,door_C,door_D],
    'doorC': [bedroom_1,living_room],
    'doorD': [living_room, outside]
}

## temp 
print(all_doors)