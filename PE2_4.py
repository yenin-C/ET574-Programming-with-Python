email = 'yenin.carrion@outlook.com'
username = email.split('@')[0]
company = email.split('@')[1]
print(email) #Use slicing to print the email address.
print(username) #Use slicing and string methods to print only the user name all in lowercase. (Did not use lower() because email is already in lower case)
print(company.upper()) #Use slicing and string methods to print only the company name all in uppercase.
