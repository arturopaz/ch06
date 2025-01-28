# Store information about a pizza being ordered.

pizza = {
    'grosor': 'delgada',
    'ingredientes': ['queso','champiñones']
}

# Summarize the order.
print(f"Has pedido una pizza {pizza['grosor']}"
      " con los siguientes ingredientes:")

for ingrediente in pizza['ingredientes']:
    print(f"\t{ingrediente}")

