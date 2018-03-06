#stars pt1
def draw_stars(arr):
    for idx in range(0,len(arr)):
        star = ""
        for i in range(0,arr[idx]):
            star += "*"
        print star
draw_stars([4,6,1,3,5,7,25])

#stars pt2
def draw_stars(arr):
    for idx in range(0,len(arr)):
        star = ""
        if type(arr[idx]) == int:
            for i in range(0,arr[idx]):
                star += "*"
        elif type(arr[idx]) == str:
            for ii in range(0,len(arr[idx])):
                arr[idx]=arr[idx].lower()
                star += str(arr[idx][0])
        print star
draw_stars([4,'Tom',1,'Michael',5,7,'Jimmy Smith'])