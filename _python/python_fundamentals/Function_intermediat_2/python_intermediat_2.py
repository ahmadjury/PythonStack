

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#------------------------------------------------------------
print("_" * 35)

x[1][0]=15
print(x)

students[0]['last_name']="Bryant"
print(students)

sports_directory['soccer'][0]='Andres'
print(sports_directory)

z[0]['y']=30
print(z)


print("_" * 35)
#------------------------------------------------------------

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students): 
    for i in students:
        print( f"'first_name : {i['first_name']} ,'last_name_name : {i['last_name']} ")
print(iterateDictionary(students))

print("_" * 35)
#------------------------------------------------------------



def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name',students)


print("_" * 35)

iterateDictionary2('last_name',students)

print("_" * 35)

#------------------------------------------------------------

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dect):
    for key in some_dect:    
        print (len(some_dect[key]),key.upper())
        for i in range ((len(dojo[key]))):
            print(some_dect[key][i])
        print("\n")
printInfo(dojo)        


print("_" * 35)

#------------------------------------------------------------


