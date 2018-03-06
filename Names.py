#Names pt1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def compoundNames(arr):
    for idx in range(0,len(arr)):
        print arr[idx]['first_name']+' '+arr[idx]['last_name']
compoundNames(students)

#pt2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def studentsInstructors(obj):
    for key in obj:
        print key
        for idx in range(0,len(obj[key])):
            print idx,"-",obj[key][idx]['first_name'],obj[key][idx]['last_name'],'-',len(obj[key][idx]['first_name'])+len(obj[key][idx]['last_name'])
studentsInstructors(users)