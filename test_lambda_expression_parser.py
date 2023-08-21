#from lambda_expression_parser import *
#from parens_parser import parens_string_to_parens_structure
from all_ import *

def get_church_numeral(n):
    if n == 0:
        return "(\\ s z. z)"
    elif n == 1:
        return "(\\ s z. s z)"
    else:
        return f"(\\s z. {__helper(n)})" 

def __helper(n):
    if n == 1:
        return "s z"
    else:
        return f"s({__helper(n-1)})"

def get_application(l):
    if len(l) < 2:
        raise Exception("__get_composition expectsa list with at least 2 strings")
    s = " ".join(l)
    return "(" + s + ")"

def get_right_composition(l):
    if len(l) < 2:
        raise Exception("get_right_composition expects a list with at least 2 strings")
    s = "(".join(l)
    s += ")" * (len(l) - 1)
    return "(" + s + ")"


# STRINGS:

class LAMBDA_CALCULUS_STRINGS:
    def __init__(self):
        
    # lambda expressions:
        self.I = "(\\x. x)"
        self.K = "(\\p x.p)" 
        self.B = "(\\p q x. p (q x))"
        self.S = "(\\ p q x. p x (q x))"
        self.C = "(\\ p q x. p x q)"
        self.successor = "(\\ n s z. s(n s z))"
        self.add = f"(\\n1 n2. n2 {self.successor} n1)"
        self.compose_I_K = get_application([self.I, self.K])
        self.compose_S_B = get_application([self.S, self.B])
        self.three_composition = get_right_composition([self.successor, self.successor, self.successor, get_church_numeral(0)])
        self.three_plus_two = get_application([self.add, get_church_numeral(3), get_church_numeral(2)])



def test1():
    strings = LAMBDA_CALCULUS_STRINGS()
    string_list = [strings.I, strings.K, strings.B, strings.C, strings.C, strings.successor, strings.add, strings.compose_I_K, strings.compose_S_B, strings.three_composition, strings.three_plus_two]

    #parens_structure_list = [parens_string_to_parens_structure(s) for s in string_list]
        
    #multi_lambda_calculus_result_list = [multi_lambda_calculus_parser(struct) for struct in parens_structure_list]


    
    for i in range(len(string_list)):
        print(str(i) + ". ")
        print(f"string_list[{i}]")
        print(string_list[i])
        print(f'parens_string_to_parens_structure(string_list[i])')
        print(parens_string_to_parens_structure(string_list[i]))
        print('multi_lambda_calculus_parser(parens_string_to_parens_structure(string_list[i])')
        print(multi_lambda_calculus_parser(parens_string_to_parens_structure(string_list[i])))
        #print(parens_structure_list[i])
        #print(multi_lambda_calculus_result_list[i])
        print()


test1()
