# To delete a file,
# import os module,
# and run os.remove().

import os
file = "new.txt"

# OSError in the case of invalid
# or inaccessible file names and path
#os.remove(file)

# To avoid getting an error
# using if-else to check the file exists before delete it
if os.path.exists(file):
    print("The file has been removed.")
    os.remove(file)
else:
    print("The file does not exist.")
