#1 Display first 3 characters of your first name by using the characte
print('*    *\t\t*****\t\t*      *')
print(' *  *\t\t*\t\t* *    *')
print('   *\t\t*****\t\t*   *  *')
print('   *\t\t*\t\t*     **')
print('   *\t\t*****\t\t*      *')

#2 A-D: identify the errors and rewrite the statement in the correct syntax

#Part A
#0.05 = interest   <---- Incorrect ('interest' should be the variable and not the number)
interest = 0.05
balance = 10
print(interest*balance)

#Part B
bal = 123
#dep = $100 <---- Incorrect (dollar sign has to be removed)
dep = 100
print(bal+dep)

#Part C
a = 2
b = 3
#a+b = c <----- Incorrect (c must be defined prior to print())
c = a + b
print(c)

#Part D
txt = 'hi'
num = 123
#print(txt+num) <------- Incorrect (can only concatenate str to str, not int to str)
print(txt + "123") 

#3 Write one line of code for each step a - h | All string text values should be lower case. Use string methods to change cases

#a) Create variables greet and store “welcome to a new semester!” into greet | b) Display greet with string method, capitalize().
greet = 'welcome to a new semester!'
print(greet.capitalize())

#c) Create variables first, last and use multiple assignment to store your first name in first and last name in last. | d) Use concatenation to store the data from first and last separated by a space into name. | e) Display name with string method, title()
first = 'yenin'
last = 'carrion'
name = first + ' ' + last
print(name.title())

#f) Use any of your three classes in this term and use multiple assignment to store your classes in to class1, class2, and class3. | g) Use concatenation to store the data from class1, class2, and class3 separated by a tab into courses. | h) Display courses with string method, upper().
class1 = 'eng101'
class2 = 'ma114'
class3 = 'et574'
courses = class1 + '\t' + class2 + '\t' + class3
print(courses.upper())

#4 Write a program to perform the following:
email = 'yenin.carrion@outlook.com'
username = email.split('@')[0]
company = email.split('@')[1]
#Use slicing to print the email address:
print(email[-30:30])
#Use slicing and string methods to print only the user name all in lowercase. (Did not use lower() because email is already in lower case):
print(username)
#Use slicing and string methods to print only the company name all in uppercase:
print(company.upper()) 

#5 Display a triangle by using repetition of strings

print('       *')
print('      ***')
print('     *****')
print('    *******')
print('   *********')
print('  ***********')
print(' *************')
print('***************')
