#def repeat_str(repeat, string):
    #res = ''
    #for ind in range(repeat):
        #res += string
    #return res

#Solution 2
def repeat_str(repeat, string):
    return repeat * string

print(repeat_str(6, 'I'))
print(repeat_str(5, 'Hello'))
print(repeat_str(4, 'a'))
print(repeat_str(3, 'hello '))
print(repeat_str(2, 'abc'))
