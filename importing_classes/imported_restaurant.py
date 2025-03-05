"""Excer1."""


from restaurant import Restaurant

french_rest = Restaurant('Brasserie', 'French')
italian_rest = Restaurant('Luigi', 'Italian')
chinese_rest = Restaurant('Beijing Temple', 'Chinese')

french_rest.describe_restaurant()
print("---")
italian_rest.describe_restaurant()
print("---")
chinese_rest.describe_restaurant()