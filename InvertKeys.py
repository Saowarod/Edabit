def invert(dct):
      return {dct[i]:i for i in dct}

print("****************************************************")
print("Invert Keys and Value")
print("****************************************************")
dct = {"a": 1, "b": 2, "c": 3}
print("Key and Value Before Invert = ",dct)
print("****************************************************")
# reversed_keyvalue = {value : key for (key, value) in keyvalue.items()}
print("Key and Value After Invert = ", invert(dct))
print("****************************************************")