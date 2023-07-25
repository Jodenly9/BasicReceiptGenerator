def main():
    """
    -Basic Receipt Generator-
    Allows the user to input the name, the city and the address of the company.
    Allows the user to input multiple products and their prices, then stores them separately.
    
    This function prompts the user to input the name and price of products they want to sell. 
    It uses a while loop to continue the process until the user decides to stop. The products 
    and their prices are stored separately in a list, where each product is represented as a 
    dictionary containing the 'name' and 'price' keys.
    """    
    productos = []  # List to store the products and their prices
    print("Ingrese los Datos de la Empresa")
    company_name= input("Nombre: ")
    company_city= input("Ciudad: ")
    company_address= input("Dirección: ")

    message = "Gracias por su compra, tenga Buen Dia!"

    while True:
        prod_name = input("\nIngrese el nombre del producto a vender: ")
        prod_price = float(input(f"Ingrese el precio de {prod_name}: "))

        product = {"name": prod_name, "price": prod_price}  # Create a dictionary for the product
        productos.append(product)  # Add the product to the list of products

        seguir = input("Quieres agregar mas productos? (Ingresa 'S' para continuar, otra letra para terminar): ")
        if seguir.upper() != "S": #Continue adding products or make the receipt
            break

    #Print the receipt
    print("\n","*" * 50 )
    print(f"\t\t{company_name.title()}")
    print(f"\t\t{company_city}")
    print(f"\t\t{company_address}")
    print("-" * 50 )
    print("\tProducto\tPrecio")

    total= 0.0
    for product in productos:
        print(f"Producto: {product['name']}\tPrecio: {product['price']}")
        total += product["price"]

    print("=" * 50 )
    print("\t\t\tTotal")
    print(f"\t\t\t${total}")
    print("=" * 50 )
    print(f"\n\t{message}\n")
main()
