from pos_logic.products.product import getAllProduct, createTable as createProductTable, addProduct, updateProduct,getProduct, deleteProduct

#region product functions
def product_menu():
    print('01: Add Product')
    print('02: Update Product')
    print('03: Get Product By ID')
    print('04: Get All Product')
    print('05: Delete Product By ID')

def product_operations():
   product_input = int(input("Enter your choice: "))
   if product_input == 1:
       product_name = input('Enter Product Name: ')
       product_category = input('Enter Product Category: ')
       product_price = float(input('Enter Procuct Price: '))
       product_stock_quantity = int(input('Enter Product Quantity: '))
       addProduct(product_name, product_category, product_price, product_stock_quantity)
   elif product_input == 2:
       product_id = int(input('Enter Product ID: '))
       product_name = input('Enter Product Name: ')
       product_category = input('Enter Product Category: ')
       product_price = float(input('Enter Procuct Price: '))
       product_stock_quantity = int(input('Enter Product Quantity: '))
       updateProduct(product_id, product_name, product_category, product_price, product_stock_quantity)
   elif product_input == 3:
       product_id = int(input('Enter Product ID: '))
       getProduct(product_id)
   elif product_input == 4:
       all_products = getAllProduct()
       for product in all_products:
           print(str(product[0:]))
   elif product_input == 5:
       product_id = int(input("Enter Product ID: "))
       deleteProduct(product_id)
#endregion        