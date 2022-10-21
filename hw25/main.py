from hw25.models import (
    Product,
    Order,
)

# Product(id='aaaaa', name='iPhone 14', price=24000, quantity=100, reserved_quantity=0).add_product()
# Product(id='bbbbb', name='iPhone 13', price=22000, quantity=100, reserved_quantity=0).add_product()
# Product(id='ccccc', name='iPhone 12', price=20000, quantity=100, reserved_quantity=0).add_product()
# Product(id='ddddd', name='iPhone 11', price=18000, quantity=100, reserved_quantity=0).add_product()

# product1 = Product.get_by_id("aaaaa")
# product2 = Product.get_by_id("bbbbb")
#
# new_order1 = Order(
#     id='gfdsa',
#     destination_address='just address 2',
#     customer_first_name='Jane',
#     customer_last_name='Dow',
#     status='New'
# )

# new_order1.insert([(product1, 2), (product2, 4)])

# new_order2 = Order(
#     id='poiuy',
#     destination_address='just address 3',
#     customer_first_name='Jane',
#     customer_last_name='Dow',
#     status='New'
# )

# new_order2.insert([(product1, 2), (product2, 4)])

# Order.change_status("gfdsa", "Canceled")
# Order.change_status("poiuy", "Processed")