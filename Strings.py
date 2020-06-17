#How to a string
print("Anu")
print('''Oluwatise
Caleb
Fatokun''')
#How to access characters in a string
str = "Program"
print(str[0])
#Python String Methods
#Capitalize - Convert the first letter in a string to upper and others to lowercase
name = "anuoluwa Fatokun"
print(name.capitalize())
#cenrter() - takes two argument; width and char fill
print("BlackLivesMatter".center(25,"#"))
#casefold() - convert char to lowercase and used for caseless match, like for comparison
firstname = "Anuoluwapo"
lastname = "anuoluwapo"
if firstname.casefold() == lastname.casefold():
    print("yes")
#count() - retunr the number of occurence of a substring
print(firstname.count("o"))
#endswith() - return ture if a string ends with the specified suffix
print(firstname.endswith('po'))
print(firstname.endswith(("po", 'sha'))) # you can pass a tuple and any of the tuple content that is true will make it true
#find() - find the index of a substring first occurence, if it does not it return -1
print(firstname.find("o"))
print(firstname.rfind('o')) #highest occurence 
print(firstname.index('o'))
print(firstname.rindex('o'))
#isalnum()
#isalpha()
#isdecimal()
#isdigit()
#islower()
#isnumeric()
#isspace()
#istitle() - If all words in a string begins with a upper letter
s = 'Python Is Good'
print(s.istitle())
#isupper()
#join()
sonname = ["Oluwatise", "Caleb", "Isaac", "Fiyinfoluwa", "Ewaoluwa"]
print(", ".join(sonname))
#ljust() - returns a left justified string of a given minimum width
print(s.ljust(24, "*"))
print(s.rjust(24, "*"))
#lower() - converts all uppercase char in a string to a lowercase
print(s.lower())
print(s.upper())
print(s.swapcase())
#lstrip() - method returns a copy of a string with leading char removed 
print(s.lstrip("Python"))
print(s.rstrip("Good"))
print(s.strip())
#partition(separator) - takes a string parameter that separate the string at the first occurrence of it. 
#The partition method returns a 3-tuple containing; the part b4 d separator, the separator, and d part after it. 
#if it does not comtain the separator, it return the string itself and two empty string


#replace(oldword, newword)
#split(separator, maxsplit) - returns a list of strings
text = "love thy neighbor"
print(text.split())
grocery = '''Milk, 
Chicken, 
Bread'''
print(grocery.split(','))
print(grocery.rsplit(','))
#splitlines() - splits the string at the line breaks and returns a list of linces in the string
print(grocery.splitlines())
#startswith()
#title()
