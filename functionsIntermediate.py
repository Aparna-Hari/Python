x = [ [5,2,3], [10,8,9] ] 
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]= 15
print(x)

#2Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

#3.In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#4.Change the value 20 in z to 30

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)


#5.Iterate Through a List of Dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for item in some_list: #traversing through the list
        for key in item.keys(): #traversing through the keys of each item
            print(f"{key}- {item[key]}, ")



#6.Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
#the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
def iterateDictionary2(key_name, some_list):
    for val in range(len(some_list)):
        print(some_list[val][key_name])
        

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#print("4. Iterate through a Dictionary with List Values")
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    # print(some_dict)
    # for i in range(0, len(some_dict))
    for key in some_dict:
        count = len(some_dict[key]) 
        print(f"{count} {key.upper()}")
        for value in range (count):
            print(some_dict[key][value])


printInfo(dojo)












iterateDictionary(students)


"""def iterateDictionary2(key_name,students):
    key_name='first_name'
    values_of_key=[a_dict[key_name] for a_dict in students]
    print(values_of_key)
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)"""

# def printInfo(some_dict):
#     # print(some_dict)
#     # for i in range(0, len(some_dict))
#     for key in some_dict:
#         count = len(some_dict[key]) 
#         print(f"{count} {key.upper()}")
#         for value in range (count):
#             print(some_dict[key][value])


# printInfo(dojo)

