def roman_numbers(roman):
    roman_values = {
        'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
    }
    total=0
    prev_value=0

    for char in reversed(roman):
        value= roman_values[char]
        if value< prev_value:
            total-=value
        else:
            total+= value
        prev_value=value

    return total


print("Please enter a roman number")
num=input()
print(num,"=",roman_numbers(num))