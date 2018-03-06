my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def make_tuple(obj):
    arr = []
    for key in obj:
        tup = (key,obj[key])
        arr.append(tup)
    print arr
make_tuple(my_dict)