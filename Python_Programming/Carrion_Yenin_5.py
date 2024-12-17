'''
create python code to:
        Request an email address from the console.
        Write the email address to a file: email.txt.
        Print the email address to the console (the output window).
'''
filename = "email.txt" #This will be the file name: "email.txt"

email_address = input("Please enter your email address ") #This command requests the user for their email address
with open(filename, 'x') as file_object: #This command will create the file
    file_object.write(f"QCC EMAIL: {email_address} also has been written to the email.txt") #This comand will add the information to the file

print(input)