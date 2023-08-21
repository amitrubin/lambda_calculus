from pathlib import Path
from parens_parser import get_balanced_substring, parens_string_to_parens_structure


s1 = "(\ x y z. x y z)"
s2 = "(\ x y z. x (y z))"
s3 = "(\ a b c d. (a b) (c d))"
#s4 = ""
#s5 = "(a b c)"

x1 = get_balanced_substring(s1)
x2 = get_balanced_substring(s2)
x3 = get_balanced_substring(s3)
#x4 = get_balanced_substring(s4)
#x5 = get_balanced_substring(s5)

y1 = parens_string_to_parens_structure(s1)
y2 = parens_string_to_parens_structure(s2)
y3 = parens_string_to_parens_structure(s3)
#y4 = parens_string_to_parens_structure(s4)
#y5 = parens_string_to_parens_structure(s5)
print(f"{s1=}\n{y1=}\n")
print(f"{s2=}\n{y2=}\n")
print(f"{s3=}\n{y3=}\n")
#print(f"{s4=}\n{y4=}\n")
#print(f"{s5=}\n{y5=}\n")


