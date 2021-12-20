import random

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')

def users_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

full_name = users_full_name(first_name,last_name)

print(f'''Welcome {full_name} to Day Trip Generator!
This generator will give you a random Destination to go too,
a Restaurant at that destination, a way of Transportation to get there,
as well as a form of Entertainment for the evening!''')

def select_random_destination():
  destinations_list = ['Idaho', 'Florida', 'New York', 'Minnesota', 'Arizona']
  confirmation = None
  while confirmation != 'Y':
    destination = random.choice(destinations_list)
    print(f'To start the Destination we have chosen for you is {destination}')
    confirmation = input('Are you happy with this Destination (Y/N): ')
  return destination

def select_random_restaurants():
  restaurants_list = ['BWW', 'McDonalds', 'Subway', 'Applebees', 'Chipotle']
  confirmation = None
  while confirmation != 'Y':
    restaurant = random.choice(restaurants_list)
    print(f'Your Restaurant is {restaurant}')
    confirmation = input('Are you happy with this Restaurant (Y/N): ')
  return restaurant

def select_random_transportation():
  transportation_list = ['Sports Car', 'Taxi', 'Horse and Buggie', 'Walking', 'Heliopter']
  confirmation = None
  while confirmation != 'Y':
    transportation = random.choice(transportation_list)
    print(f'Your mode of Transportation is {transportation}')
    confirmation = input('Are you happy with this way of Transportation (Y/N): ')
  return transportation

def select_random_entertainment():
  entertainment_list = ['Movie', 'Shopping', 'Sight-seeing', 'Concert']
  confirmation = None
  while confirmation != 'Y':
    entertainment = random.choice(entertainment_list)
    print(f'Your random selection of Entertainment is {entertainment}')
    confirmation = input('Are you happy with this choice of Entertainment (Y/N): ')
  return entertainment

random_destination = select_random_destination()
random_restaurant = select_random_restaurants()
random_transportation = select_random_transportation()
random_entertainment = select_random_entertainment()

print(f'''Congratulations {full_name} on your random day trip! You have chosen {random_destination} as your random destination, {random_restaurant} as your random restaurant,
{random_transportation} as your random mode of transportation, and {random_entertainment} as your random choice of entertainment!''')
 


























