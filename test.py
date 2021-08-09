string = 'Day, mice. "Year" is a mistake!'.split(',')
# шифр цезаря
def cezar(string, num):
    n = 0
    for i in range(len(string)):
        n = ord(string[i]) - num
        if n < 97:
            n = 122 - (96 - n)
        elif n < 65:
            n = 90 - (65 - n)
        return  chr(n)
# находим длину слова
def len_word(string):
    array = ''
    for i in string:
        for j in i:
            if j.lower() in 'abcdefghijklmnopqrstuvwxyz' or j == ' ':
                array += j
    array = array.split(' ')
    new_array = []
    for i in array:
        new_array.append(len(i))
    return new_array

def words(string):
    array = ''
    for i in string:
        for j in i:
            if j.lower() in 'abcdefghijklmnopqrstuvwxyz' or j == ' ':
                array += j
    array = array.split(' ')
    new_array = []
    for i in array:
        new_array.append(i)
    return new_array

print(words(string))
print(len_word(string))





