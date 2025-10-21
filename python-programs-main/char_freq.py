string=input("enter a string :")
char_frequency={}
for char in string :
    char_frequency[char]=char_frequency.get(char,0)+1
print(f"character frequencies in '{string}'")
for char,count in char_frequency.items():
    print(f"{char} occur {count} times.")
