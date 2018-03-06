name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def list_to_dict(arr1,arr2):
    new_dict = {}
    if len(arr1) < len(arr2):
        large = arr2
        small = arr1
    elif len(arr1) >= len(arr2):
        large = arr1
        small = arr2
    for i in range(len(small),len(large)):
        small.append(0)
    for idx in range(0,len(large)):
        new_dict.update({large[idx]:small[idx]})

    print new_dict
    return new_dict
list_to_dict(name,favorite_animal)