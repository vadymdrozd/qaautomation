from hw25.models import Product
from hw25.models import Order

# Product(id='aaaaa', name='iPhone 14', price=24000, quantity=100, reserved_quantity=0).add_product()
# Product(id='bbbbb', name='iPhone 13', price=22000, quantity=100, reserved_quantity=0).add_product()
# Product(id='ccccc', name='iPhone 12', price=20000, quantity=100, reserved_quantity=0).add_product()
# Product(id='ddddd', name='iPhone 11', price=18000, quantity=100, reserved_quantity=0).add_product()

# product1 = Product.get_product_by_id("aaaaa")
# product2 = Product.get_product_by_id("bbbbb")

# new_order1 = Order(
#     id='uwuwu',
#     destination_address='just address 2',
#     customer_first_name='Jane',
#     customer_last_name='Dow',
#     status='New'
# )
#
# new_order1.create_order([(product1, 2), (product2, 4)])

# new_order2 = Order(
#     id='qwqwq',
#     destination_address='just address 3',
#     customer_first_name='Jane',
#     customer_last_name='Dow',
#     status='New'
# )
#
# new_order2.create_order([(product1, 2), (product2, 4)])

# Order.change_order_status("uwuwu", "Canceled")
# Order.change_order_status("qwqwq", "Processed")