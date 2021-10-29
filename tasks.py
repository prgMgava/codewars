# imports
import math

# -----------------------------------------------------------------------------


# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
def is_prime(num):
    if num <= 1: return False
    if num == 2: return True
        
    for i in range(3,int(math.sqrt(num)) + 1,2):
        if num % i == 0: 
            return False
    return True

    # or

    # return sum(1 for i in range(1,num + 1) if num%i == 0) == 2
# print(is_prime(23))

# -----------------------------------------------------------------------------


# https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/python
def predict_age(age_1: int, age_2: int, age_3: int, age_4: int, age_5: int, age_6: int, age_7: int, age_8: int):
    """Multiplicar cada numero por si, somar todos e dividir por dois a soma 

    Args:
        age_1 (int): a number as age
        age_2 (int): a number as age
        age_3 (int): a number as age
        age_4 (int): a number as age
        age_5 (int): a number as age
        age_6 (int): a number as age
        age_7 (int): a number as age
        age_8 (int): a number as age

    Return:
        age (int): a number
    """
    age = math.floor(math.sqrt(age_1**2 + age_2**2 + age_3**2 + age_4**2 +age_5**2 +age_6**2 + age_7**2 + age_8**2)/2)
    return age

# print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))

def predict_age2(*ages):
    output = (sum(age**2 for age in ages) ** .5) // 2
    return output

# print(predict_age2(65, 60, 75, 55, 60, 63, 64, 45))

# -----------------------------------------------------------------------------


# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accumulator(string : str):
    """

    Args:
        string (str): uma string

    Returns:
        string: resultante da string de entrada
    """
    output = ""
    for i,letter in enumerate(string):
        if i == 0: 
            output += letter.upper()
        else:
            for j in range(i + 1):
                if j == 0: 
                    output += letter.upper()
                else:
                    output += letter.lower()
        if i is not len(string) - 1:
            output += "-"
    # return output
    # or
    return "-".join((letter * i).title() for i,letter in enumerate(string, 1))
# print(accumulator("asdf"))

def sum_triangular_numbers(n):
    # output = []
    # triangular_number = 0
    # for i in range(1,n + 1):
    #     triangular_number += i
    #     output.append(triangular_number)
    # sum_numbers = sum(output)
    # return sum_numbers

    # or

    output2 = []
    triangular_number2 = 0
    # for i in range(1,n + 1):
    #     triangular_number2 = (i(i + 1))/2
    #     output2.append(triangular_number2)
    sum_numbers2 = sum(((i * (i + 1))/2) for i in range(1,n + 1))
    return sum_numbers2
    
# print(sum_triangular_numbers(4))


# -----------------------------------------------------------------------------


# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python


def deep_count(array):
    count = 0
    for item in array:
        if type(item) is list:
            count += 1
            count += deep_count(item)
        else:
            count += 1
    return count

# print(deep_count([1,2,3,[4,5]]))

# https://www.codewars.com/kata/586ee462d0982081bf001f07/train/python

def fillable(stock, merch, n):
    # try:
    #     return bool([item for item in stock if stock[merch] >= n])
    # except KeyError:
    #     return False

    return stock.get(merch, 0) >= n
# print(fillable({'football': 4, 'boardgame': 10, 'leggos': 1, 'doll': 5},'leggos', 2))


# https://www.codewars.com/kata/586f61bdfd53c6cce50004ee/train/python

def user_contacts(data):
    return {item[0]: (item[1] if len(item) > 1 else None) for item in data}
