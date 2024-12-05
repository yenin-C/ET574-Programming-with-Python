# To delete an entire folder, use the os.rmdir() method:
# Remove the folder “myfolder":
import os
#os.rmdir("myfolder")

# Python starts by executing the try clause.
# If all goes well, it skips the except clause and proceeds.
# If an exception occurs,
# it jumps out of the try clause and executes the except clause.
try:
    folder = 'myfolder'
    os.rmdir(folder)
    print("The folder has been removed.")
except:
    print("Exceptions: Something went wrong.")
