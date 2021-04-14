def invert(dct):
      return {dct[i]:i for i in dct}

print("****************************************************")
print("Invert Keys and Value")
print("****************************************************")
dct = {"bai": 4, "fern": 2}
print("Key and Value Before Invert = ",dct)
print("****************************************************")
# reversed_keyvalue = {value : key for (key, value) in keyvalue.items()}
print("Key and Value After Invert = ", invert(dct))
print("****************************************************")