product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product :
    def __init__(self, name, code) :
        self.name = name
        self.code = int(code)

ProductA = Product("codetree", 50)
ProductB = Product(product_name, product_code)

print(f"product {ProductA.code} is {ProductA.name}")
print(f"product {ProductB.code} is {ProductB.name}")