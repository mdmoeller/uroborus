import string

mem = '0'

def to_decimal(ndn):
    "Converts a Negadecimal number to a Decimal number"
    ndn = int(ndn)
    u = ndn % 10
    t = (ndn / 10) % 10
    h = (ndn / 100) % 10
    th = (ndn / 1000) % 10
    tth = (ndn / 10000) % 10
    hth = (ndn / 100000) % 10
    thth = (ndn / 1000000) % 10
    u = u * 1
    t = t * -10
    h = h * 100
    th = th * -1000
    tth = tth * 10000
    hth = hth * -100000
    thth = thth * 100000
    decimal = u + t + h + th + tth + hth + thth
    return decimal

def to_negadecimal(dec): #this function was adapted from Wikipedia link given by Prof. Dave
    "Returns a string representing the negadecimal value"
    n_decimal = ''
    if not dec:
        n_decimal = '0'
    else:
        while dec != 0:
            dec = int(dec)
            dec, remainder = divmod(dec, -10)
            if remainder < 0:
                dec, remainder = dec + 1, remainder + 10
            n_decimal = str(remainder)+ n_decimal
    return n_decimal

def add(ndn_1, ndn_2):
    "Returns the sum of the two parameters."
    add = ndn_1 + ndn_2
    return add

def subtract(ndn_1, ndn_2):
    "Returns the difference ndn_1 - ndn_2."
    subtract = ndn_1 - ndn_2
    return subtract

def multiply(ndn_1, ndn_2):
    "Returns the product of the two parameters."
    multiply = ndn_1 * ndn_2
    return multiply

def divide(ndn_1, ndn_2):
    "Returns the quotient ndn_1 / ndn_2. Does not check to make sure ndn_2 != 0."
    divide = ndn_1 / ndn_2
    return divide

def remainder(ndn_1, ndn_2):
    "Returns the modulus ndn_1 % ndn_2. Does not check to make sure ndn_2 != 0"
    remainder = ndn_1 % ndn_2
    return remainder

def negate(negadecimal):
    "Returns the number which, when added to negadecimal, would give zero"
    dec_eq = to_decimal(negadecimal)
    dec_eq = dec_eq * -1
    return dec_eq

def store(ndn):
    "Saves ndn in the global variable mem"
    global mem
    mem = ndn
    return mem

def fetch():
    "Returns the negadecimal string previously saved in the global variable mem"
    return mem

def evaluate(string):
    "Evaluates a string under the criteria specified in the assignment"
    string_list = string.split()
    string = string.replace('mem', str(mem))
    if (len(string_list) > 3):
        return string_legality(string)
    elif ('dec' in string) or ('neg' in string):
        string = string_trans(string)
        return string
    elif 'fetch' in string:
        string = fetch()
        return string
    else:
        string = string_trans(string)
        string = to_negadecimal(string)
        store(string)
        return string

def string_trans(string):
    if '+' in string:
        string = string.split('+')
        string[0] = to_decimal(string[0])
        string[1] = to_decimal(string[1])
        string = add(int(string[0]), int(string[1]))
        return string
    elif ('-' in string) and ('neg' not in string):
        a = string.split()
        if len(a) > 1:
            string = string.split('-')
            string[0] = to_decimal(string[0])
            string[1] = to_decimal(string[1])
            string = subtract(int(string[0]), int(string[1]))
            return string
        else:
            string = string.split('-')
            string = negate(int(string[1]))
            return string
    elif '*' in string:
        string = string.split('*')
        string[0] = to_decimal(string[0])
        string[1] = to_decimal(string[1])        
        string = multiply(int(string[0]), int(string[1]))
        return string
    elif '/' in string:
        string = string.split('/')
        string[0] = to_decimal(string[0])
        string[1] = to_decimal(string[1])        
        string = divide(int(string[0]), int(string[1]))
        return string
    elif '%' in string:
        string = string.split('%')
        string[0] = to_decimal(string[0])
        string[1] = to_decimal(string[1])        
        string = remainder(int(string[0]), int(string[1]))
        return string
    elif 'dec' in string:
        string = string.split()
        string = to_decimal(string[1])
        return string
    elif 'neg' in string:
        string = string.split()
        string = to_negadecimal(string[1])
        return string
    else:
        return string_legality(string)

def string_legality(string):
    string = string.split()
    if len(string) > 3:
        return "Invalid input. Please try again."
    elif len(string) == 3:
        string_1st = string[0]
        string_2nd = string[1]
        string_3rd = string[2]
        op_list = ['+', '-', '*', '/', '%']
        if (string_1st.isdigit() == False) and (string_1st != 'mem'):
            return "Please use numbers as your input values"
        elif (string_3rd.isdigit() == False) and (string_3rd != 'mem'):
            return "Please use numbers as your input values"
        elif string_2nd not in op_list:
            return "Sorry! You may only use one of the following operators: \n\t+\n\t-\n\t*\n\t/\n\t%"
        elif ((string_2nd == '/') or (string_2nd == '%')) and (string_3rd == '0'):
            return "Sorry, division or mod operation by zero is not possible."
        elif string_1st != 'mem':
            if int(string_1st) > 9999999:
                return "This calculator is only capable of using values less than 10000000"
        elif string_3rd != 'mem':
            if int(string_3rd) > 9999999:
                return "This calculator is only capable of using values less than 10000000"
    elif len(string) == 2:
        if (string[0] != 'dec') and (string[0] != 'neg'):
            return "This calculator only accepts the 'dec' or 'neg' command. Please try again"
        elif string[1].startswith('-') and ((string[1])[1:].isdigit()):
            pass
        elif (string[1].isdigit() == False) and (string[1] != 'mem'):
            return "Please give a valid number to the 'dec' or 'neg' command"
    elif len(string) == 1:
        if (string[0] != 'quit') and (string[0] != 'fetch()'):
            string = ' '.join(string)
            if string[0] != '-':
                return "Sorry! I don't understand this. Please enter another input"
    else:
        return "Please enter a valid input"
        

def REPL():
    string = raw_input('Calculate: ').strip().lower()
    if string == 'quit':
        print "Program ending..."
        return
    else:
        try:
            print evaluate(string)
        except:
            print string_legality(string)
    return REPL()


if __name__ == '__main__':
    REPL()
