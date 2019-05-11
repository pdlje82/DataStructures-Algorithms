# Code

def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here
    str_index = len(our_string) - 1
    new_str = ""

    while str_index >= 0:
        new_str += our_string[str_index]
        str_index -= 1
    return(new_str)


# Test Cases

# print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
# print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
# print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")


# Code

def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here
    str1 = (str1.lower().replace(" ", ""))
    str2 = (str2.lower().replace(" ", ""))
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Test Cases

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")