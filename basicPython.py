
###############
# Python code sample all basic operations and constructs
###############

# Single Line Comment #

'''
Multi 
line
Comment 
print ("Not Printed")
'''

##########
# Functions
##########
def arthimeticOperators():
	print ("\n-----Arthmetic Operators-----\n")
	# Addition, Subtraction Operator //
	print ("Addition, Subtraction Operator 13-4+2 : {}".format(13 - 4 + 2))
	# Division /
	print ("Division 13/4 : {}".format(13 / 4))
	# Integer Division //
	print ("Integer Division 13/4 : {}".format(13 / 4))
	# Modulo Operator //
	print ("Modolo Operator 13%4 : {}".format(13 % 4))

	print ("Assignment and Del: del keyword used to delete the assignment done by assignment operator = ")
	a = 5
	try :
		print ("Try printing value of a after assignment a=5")
		print ("Value of a:")
		print (a)
	except NameError:
		print ("Got Name Error")
	del a
	try :
		print ("Try printing value of a after del a")
		print ("Value of a:")
		print (a)
	except NameError as ne:
		print ("Got Name Error : " + str(ne))

def logicalOperators():
	print ("\n-----Logical Operators-----\n")
	a, b , c , d = 1,2,3,3
	print ("The variable values : a b c d are {} {} {} {}".format(a,b,c,d))
	print ("isEqual a == b : {} ".format(a == b))
	print ("notEqual a != b : {} ".format(a != b))
	print ("greater than c > d : {} ".format(c > d))
	print ("greater than or equal c >= d : {} ".format(c >= d))
	print ("less than c < d : {} ".format(c < d))
	print ("less than or equal c <= d : {} ".format(c <= d))
	
def stringOperations():
	print ("\n-----String Operations-----\n")
        # Assignment can be done using Single or Double Quotes	
	greeting = "Hello "
	message = 'World'
	msg = greeting + message
	print("Variables greeting, message, msg have values : {} {} {}".format(greeting, message, msg))
	print ("Concatenation greeting + message : {}".format(greeting + message))
	print ("String contains word greeting in msg : {}".format(greeting in msg))
	print ("length of msg len(msg) : {}".format(len(msg)))
	repeat = int(input ("How many times should I repeat? "))
	print ("Repeat of greeting {} times : {}".format(repeat,greeting * repeat))
	print ("\n-----Slicing and Dicing-----\n")
	print ("Slice first 5 msg[0:5] : {}".format(msg[0:5]))
	print ("Slice 4th letter (Index starts from 0) msg[4] : {}".format(msg[4]))
	print ("Slice 3rd letter from end msg[-3] : {}".format(msg[-3]))
	print ("Slice first 3 msg[:3] : {}".format(msg[:3]))
	print ("Slice last 3 msg[:-3] : {}".format(msg[:-3]))
	print ("Slice all but 3 msg[-3:] : {}".format(msg[-3:]))
	print ("Entire String literal msg[:] : {}".format(msg[:]))
	print ("\n-----String formatting-----\n")
	print ("msg as-is  : {}".format(msg))
	print ("msg left justified : {}".format(msg.ljust(30)))
	print ("msg right justified : {}".format(msg.rjust(30)))
	print ("msg center aligned : {}".format(msg.center(30)))
	print ("msg zero fill : {}".format(msg.zfill(30)))
        

def listOperations():
	print ("\n-----Lists-----\n")
	listOfNumbers = [3, 4, 5, 6]
	print ("List used for operations : {}".format(listOfNumbers))
	print ("List contains 4, 4 in list? :  {}".format(4 in listOfNumbers))
	print ("List contains 8, 8 not in list? : {}".format(8 not in listOfNumbers))
	print ("Concat new elements [5,4] listOfNumbers + [5 , 4] : {}".format(listOfNumbers + [5 , 4]))
	listOfNumbers += [5 , 4]
	print ("Concat and update new elements [5,4] listOfNumbers += [5 , 4] : {}".format(listOfNumbers))
	del listOfNumbers[-2:]
	print ("Del last 2 elements del listOfNumbers [-2:] : {}".format(listOfNumbers))
	repeat = int(input ("How many times should I repeat? "))
	print ("Repeat list {} #times, listOfNumbers * {}  : {}".format(repeat, repeat, listOfNumbers * repeat))
	print ("Length len(list) : {}".format(len(listOfNumbers)))
	print ("Max max(list) : {}".format(max(listOfNumbers)))
	print ("Min max(list) : {}".format(min(listOfNumbers)))
	print ("Sum sum(list) : {}".format(sum(listOfNumbers)))

	newList = [3, 9, 10]
	listOfNumbers.extend(newList)
	print ("Extend list with new list list.extend(newList) : {}".format(listOfNumbers))
	listOfNumbers.append(12)
	print ("Append element 12 to  list list.append(12) : {}".format(listOfNumbers))
	listOfNumbers.insert(2,14)
	print ("Insert element 14 at index 2 list.insert(2,14) : {}".format(listOfNumbers))
	listOfNumbers.remove(14)
	print ("Remove element 14 list.remove(14) : {}".format(listOfNumbers))
	listOfNumbers.pop()
	print ("Remove last element list.pop() : {}".format(listOfNumbers))
	listOfNumbers.count(3)
	print ("Count occurences of 3 list.count(3) : {}".format(listOfNumbers.count(3)))
	listOfNumbers.reverse()
	print ("Reverse list.reverse() : {}".format(listOfNumbers))
	listOfNumbers.sort()
	print ("Sort list.sort() : {}".format(listOfNumbers))
	newList2 = listOfNumbers.copy()
	print ("copy list2 = list.copy() : {}".format(newList2))
	newList3 = listOfNumbers[:]
	print ("copy list3 = list[:] : {}".format(newList3))
	listOfNumbers.clear()
	print ("Clear list.clear() : {}".format(listOfNumbers))

def tupleOperations():
	print ("\n-----Tuple Operations-----\n")
	print ("Tuple differe from List only in fact that they are immutable and defined using comma seperated elements surrounded by optional round brackets instead of square brackets")
	print ("Tuple used when the elements are constant like enum?")
	#responses = 'Yes' , 'No'
	#outcomes = ('Pass' , 'Fail')
	print ("Use string split and join methods to convert list to tuples vice versa")
	fruits = 'apple mango guava banana melon'.split()
	print ("List created using split : {}".format(fruits))
	stringNew ='::'.join(fruits)
	print ("List created using '::'.join : {}".format(stringNew))

def dictOperations():
	print ("\n-----Dictionary Operations-----\n")
	print ("Key value pairs accessed by keys")
	database = {
		"Name" : "ABC", "Age" : 24, "Gender" : "M"
	}
	print ("Sample database : {}".format(database))
	print ("Accessing value of key Age db[\"Age\"]: {}".format(database["Age"]))	
	print ("Key exists Gender in database: {}".format("Gender" in database))	
	database['email']='m@gmail.com'
	print ("Add new key data['key']=value : {}".format(database))
	database.pop('email')
	print ("Pop specific key data.pop(\'key\') : {}".format(database))
	newDatabase={'email':'m@gmail.com','weight':78}
	database.update(newDatabase)
	print ("Add new data.update(newData) : {}".format(database))


	print ("Iterate using data.items() gives tuples of key and values:")
	for k,v in database.items():
		print (k + "::" + str(v))
	print ("Iterate using data.keys() gives keys used to access values:")
	for k in database.keys():
		print (k + "::" + str(database[k]))
	print ("Iterate using data.values() gives values")
	for v in database.values():
		print (str(v))

	details = [('name','M'),('age',38),('gender','M')]
	database2 = dict(details)
	print ("New details list of tuples : {} ".format(details))
	print ("New database convert from list of tuples dict(details): {} ".format(database2))

def misc():
	itemsList = [1,2,3,4]
	print ("Working on variable itemList : {}".format(itemsList))
	if all(itemsList):
		print("All printed")
	elif any(itemsList):
		print("Any thing printed")
	
	for i in range(2,10):
		print (i+1)

	for i,item in enumerate(itemsList):
		print("{}. {}".format(i+1,item))

	database = [ {'Name':'M', 'Gender':'M'}, {'Name':'N','Email':'N@Gm.com'}]
	for data in database:
		for k,v in data.items():
			print("{} : {}".format(k,v))

	for item,data in zip(itemsList,database):
		print("{} and {}".format(item,data))

	squares = [x**2 for x in itemsList]
	print(squares)
	squaredict = {x:x**2 for x in itemsList}
	print(squaredict)

def wrapper(functionToCall):
	return functionToCall

def clear():
	from os import system as sys
	sys('clear')

def printOptions():	
	print("\n\n\nChoose the option you want to view:")
	print("\t1. arthimeticOperators")
	print("\t2. logicalOperators")
	print("\t3. stringOperations")
	print("\t4. listOperations")
	print("\t5. tupleOperations")
	print("\t6. dictOperations")
	print("\t7. misc")
	print("\t0. Exit")
	print ("\n")
	return int(input("Select what function you want to review : "))

def executeOption(opt):
	switcher = {
		1:'arthimeticOperators',
		2:'logicalOperators',
		3:'stringOperations',
		4:'listOperations',
		5:'tupleOperations',
		6:'dictOperations',
		7:'misc',
		0:'exit'
	}
	#print (switcher.keys())
	func=switcher[opt]
	print("Executing function : {}".format(func))
	#return eval(func)
	#wrapper(func)
	#globals()[func])
	exec (func+'()')

def getOpts():
	opt=999
	while (opt != 0):
		opt=printOptions()
		executeOption(opt)

def runAll():
	arthimeticOperators()
	logicalOperators()
	stringOperations()
	listOperations()
	tupleOperations()
	dictOperations()
	misc()
	print ("\n")

##########
# Main
##########
#runAll()
getOpts()
