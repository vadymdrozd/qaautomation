select_all_query = (
    "SELECT * "
    "FROM products;")

add_new_products_query = (
    "INSERT INTO products (id, name, quantity, price) values "
    "('ddddd', 'Nokia 3310', 12, 3000), "
    "('eeeee', 'Alcatel R220', 9, 2500), "
    "('fffff', 'Sony Ericson W880', 5, 4500), "
    "('ggggg', 'Samsung Galaxy S20', 16, 25000), "
    "('hhhhh', 'Motorola RAZR V3', 20, 4700), "
    "('iiiii', 'Huawei P90', 4, 19000), "
    "('lllll', 'Xiaomi Mi 11', 16, 21000), "
    "('mmmmm', 'Samsung A51', 3, 9800), "
    "('nnnnn', 'iPhone Xr', 7, 11000), "
    "('ooooo', 'Кирпич', 12, 12500000);")

price_modification_query = ("UPDATE products "
                            "SET price = 1000000 "
                            "WHERE quantity < 10")

delete_query = ("DELETE FROM products "
                "WHERE quantity > 10")