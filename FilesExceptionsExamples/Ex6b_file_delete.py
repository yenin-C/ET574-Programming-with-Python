# To delete a file,
# import os module,
# and run os.remove().

import os
file = "newfile.txt"

# OSError in the case of invalid
# or inaccessible file names and path
#os.remove(file)

# To avoid getting an error
# use exception handling to check the file exists before delete it
try:
    file = "newfile.txt"
    os.remove(file)
    print("The file has been removed.")
except:
    print("The file does not exist.")
