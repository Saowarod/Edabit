print("****************************************************")
print("Invert Keys and Value")
print("****************************************************")
keyvalue = {"bai": 4, "fern": 2}
print("Key and Value Before Invert = ",keyvalue)
print("****************************************************")
reversed_keyvalue = {value : key for (key, value) in keyvalue.items()}
print("Key and Value After Invert = ",reversed_keyvalue)
print("****************************************************")