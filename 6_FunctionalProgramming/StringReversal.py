#str(start:stop:step)

trial="sachin"
new_trial=trial[::-1]
print("Reversed string is :",new_trial)

# secondmethod
def string_reverse(str):
    if len(str)==0:
        return str
    else:
        return string_reverse(str[1:])+str[0]
    
str='sachin'
print("Reverse of the given string is : ",string_reverse(str))