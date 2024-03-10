sample_dict={
    "name":"John","age":30,"city":"New York"
}
sample_dict["name"]="Joh Walker"
def get_value(dictionary,key):
    if key in dictionary:
        return dictionary[key]
    else:
        raise KeyError("The given key is not present in the dictionary")
print(get_value(sample_dict,"name")) # John


print(sample_dict.items())

for key,value in sample_dict.items() : 
    print(f"{key}: {value}")

