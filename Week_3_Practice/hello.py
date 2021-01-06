#%%
print("hello")
# %%
somestring = "Test"
print (somestring)
type(somestring)

# Python's six datatypes
myName = "Brian McRae"
myAge = 50
myBDay = '06/01/1970'

# String interpolation
myIntroduction = f"""
My name is {myName} and I am {myAge} years old.
I was born {myBDay}
"""
print(myIntroduction)
# %%

# Use non-destructive editing strategies.  Don't edit the 
# code that's broken.  Copy it, comment the code, then 
# make the edit, that way you have a history.  Non-destructive 
# editing.
# ctrl slash to insert comment - keyboard

# Lists
# Lists are akin to columns in a spreadsheet
someListOfInt = [0,1,2,3,4]

# Indexing in Python starts at 0
# String indexing always starts at zero and never includes the
# endpoint in the slice
print(someListOfInt[0])

# String Slicing
print(someListOfInt[0:2])

# %%
# Python data typing is fluid with lists
aMixedList = ['a', 1,11, 1.0, True, None, "me", [0,1,2]]
for item in aMixedList :
    print(type(item))

# %%
# if x in list: works like a for loop, looping through all items in the list
# check types a lot 
