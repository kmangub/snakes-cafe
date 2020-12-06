
welcome_message = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""

print(welcome_message)

orders = {
  'Wings': 0,
  'Cookies': 0,
  'Spring Rolls': 0,
  'Salmon': 0,
  'Steak': 0,
  'Meat Tornado': 0,
  'A Literal Garden': 0,
  'Ice Cream': 0,
  'Cake': 0,
  'Pie': 0,
  'Coffee': 0,
  'Tea': 0,
  'Unicorn Tears': 0
}

print('''
Appetizers
----------
Wings
Cookies
Spring Rolls
''')

print('''
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
''')

print('''
Desserts
--------
Ice Cream
Cake
Pie
''')

print('''
Drinks
------
Coffee
Tea
Unicorn Tears
''')

# for key in orders:
#   print(key)

print("""
***********************************
** What would you like to order? **
***********************************
"""
)

while True:
  order_input = input('> ').title()
  if order_input == 'Quit': 
    break

  for key in orders:
    if order_input == key:
      orders[key] += 1
      order_quantity = orders[key]
      order_response = f"""
      ** {order_quantity} order of {order_input} have been added to your meal **
      """
      print(order_response)
print(orders)
    
    


