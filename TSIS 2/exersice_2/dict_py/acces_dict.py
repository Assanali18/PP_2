thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] # or x = thisdict.get("model")
print(x)
# Mustang

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
print(x)
# dict_keys(['brand', 'model', 'year'])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change

# dict_keys(['brand', 'model', 'year'])
# dict_keys(['brand', 'model', 'year', 'color'])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()
print(x)
# dict_values(['Ford', 'Mustang', 1964])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

#dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 2020])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()
print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Yes, 'model' is one of the keys in the thisdict dictionary