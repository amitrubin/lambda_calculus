def parens_string_to_parens_structure(s):
    #print(f"parens_string_to_parens_structure input: {s=}")
    processed_string = s[1:-1]
    if processed_string == "":
        #print("return []")
        return []
    elif processed_string.find("(") < 0:
        #print(f"return {processed_string=}")
        return [processed_string]
    output_array = []
    remaining_substring = processed_string
    while len(remaining_substring) != 0:
        if remaining_substring.startswith("("):
            balanced_substring = get_balanced_substring(remaining_substring)
            substring_parens_structure = parens_string_to_parens_structure(balanced_substring)
            output_array.append(substring_parens_structure)
            remaining_substring = remaining_substring.removeprefix(balanced_substring)

        else:
            next_parens_index = remaining_substring.find("(")
            if next_parens_index < 0:
                output_array.append(remaining_substring)
                remaining_substring = ""
            else:
                substring = remaining_substring[:next_parens_index]
                output_array.append(substring)
                remaining_substring = remaining_substring.removeprefix(substring)
    return output_array


def get_balanced_substring(s):
    if not s.startswith("("):
        raise Exception(f"doesn't start with a '(': {s}")
    match_count = 1
    index = 0
    substring = ""
    for c in s[1:]:
        index += 1
        if c == "(":
            match_count += 1
        elif c == ")":
            match_count -= 1
        if match_count == 0:
            return s[0: index+1]

s1 = "(s1 (s2 (s4 (s5) (s6) s7) s3))"
s2 = "()"
s3 = "(())"
s4 = "(s1 (s2 (s4 (s5 zzz) (s6) s7) s3))"
s5 = "(a b c)"

x1 = get_balanced_substring(s1)
x2 = get_balanced_substring(s2)
x3 = get_balanced_substring(s3)
x4 = get_balanced_substring(s4)
x5 = get_balanced_substring(s5)

y1 = parens_string_to_parens_structure(s1)
y2 = parens_string_to_parens_structure(s2)
y3 = parens_string_to_parens_structure(s3)
y4 = parens_string_to_parens_structure(s4)
y5 = parens_string_to_parens_structure(s5)

#print(f"{s1=}\n{x1=}\n{y1}")
print(f"{s2=}\n{y2=}\n")
print(f"{s3=}\n{y3=}\n")
print(f"{s4=}\n{y4=}\n")
print(f"{s5=}\n{y5=}\n")


