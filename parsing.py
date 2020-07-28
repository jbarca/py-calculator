from math import pow

def tokenization(expr):
    """
    Input: A string representing a mathematical expression consisting of non-negative numbers
    and the symbols listed in the background including potential spaces.
    Output: Returns a list of 'tokens' corresponding to the given expression.
    """
    # A list of all the possible tokens in an expression, excluding floats.
    tokens = ["+", "-", "*", "/", "^", "(", ")"]

    # Set up variables for mutation.
    tokens_in_expr = []
    current_index = 0

    # While the current index is less than the length of the string, continue.
    while current_index < len(expr):
        # Check if the character at the current index is in the list of tokens.
        # if so, add it to the list of tokens in expression.
        if expr[current_index] in tokens:
            tokens_in_expr.append(expr[current_index])
            current_index += 1
        # If the element is a digit, find all successive digits as well as
        # float values.
        elif expr[current_index].isdigit():
            digits = find_digits(expr[current_index:])
            tokens_in_expr.append(digits[0])
            current_index += digits[1]
        # Otherwsie, increase the index by 1.
        else:
            current_index += 1

    return tokens_in_expr

def find_digits(expr):
    """
    Input: A string containing an expression
    Output: The digits contained in the string and the length of those digits.
    """
    # Set up necessary declarations.
    value = ""
    current_index = 0
    # While the current element is a digit or it is a '.' to signify a float,
    # add it to the accumulated value.
    while expr[current_index].isdigit() or expr[current_index] == ".":
        value += expr[current_index]
        # If the index is out of range, break, otherwise increase the index
        # by 1.
        if current_index+1 < len(expr):
            current_index += 1
        else:
            break

    return float(value), len(value)


def has_precedence(op1, op2):
    """
    Input: Two operator tokens from a set of tokens.
    Output: Returns True if 'op1' has higher precedence than 'op2', otherwise it 
    returns False.
    """

    tokens = ["+", "-", "*", "/", "^"]

    # Check the different precedence cases. Return true or false depending on 
    # situation.
    if op1 in tokens and op2 in tokens and op1 != op2:
        if op1 == "^":
            return True
        elif op2 == "^":
            return False
        elif op1 == "/" and op2 in ["+", "-"]:
            return True
        elif op1 == "*" and op2 in ["+", "-"]:
            return True
        else:
            return False
    else:
        return False

def find_highest_precedence(token_list):
    """
    Input: Takes in a token_list from an expression
    Output: Returns the highest precedence token in the list. If two tokens are equal
    in precedence, it returns the first one.
    """
    best_token = token_list[0]

    # Look for the best token in the list
    for token in token_list:
        if has_precedence(token, best_token):
            best_token = token

    return best_token

def evaluate_token(token_list, token):
    """
    Input: The token to be evaluated.
    Output: The evaluated expression in place of the tokens and numbers.
    """
    # Check each token in the token list, if the tokens are equal, perform
    # the specific arithemetic operation on it.
    if token == "^":
        evaluation = token_list[token_list.index(token)-1] ** token_list[token_list.index(token)+1]
        
    elif token == "/":
        evaluation = token_list[token_list.index(token)-1] / token_list[token_list.index(token)+1]

    elif token == "*":
        evaluation = token_list[token_list.index(token)-1] * token_list[token_list.index(token)+1]

    elif token == "-":
        evaluation = token_list[token_list.index(token)-1] - token_list[token_list.index(token)+1]

    elif token == "+":
        evaluation = token_list[token_list.index(token)-1] + token_list[token_list.index(token)+1]
        
    # Condense the entire expression into a single floating point value.
    token_list[token_list.index(token)-1:token_list.index(token)+2] = [evaluation]
        
    return token_list    

def simple_evaluation(tokens):
    """
    Input: A list of tokens (excluding parenthesis)
    Output: A single floating point number corresponding to the result of the tokenized
    arithmetic expression.
    """
    # Make a list containing all the possible tokens
    possible_tokens = ["+", "-", "*", "/", "^"]
    token_list = []

    # If a token is in the possible token list, append it to the actual token list.
    for token in tokens:
        if token in possible_tokens:
            token_list.append(token)
    
    # If a recursive call gives a single element list, we are done with the evaluation, so
    # return the value as a float.
    if len(tokens) == 1:
        return float(tokens[0])

    # Otherwise recursively call simple_evaluation to condense the expression into a single value.
    return simple_evaluation(evaluate_token(tokens, find_highest_precedence(token_list)))

def find_last_bracket(tokens):
    """
    Not a required function.
    Input: A token list (with brackets)
    Output: The index at which the last starting bracket occurs in the list.
    """
    for i in range(1, len(tokens)+1):
        if tokens[-i] == "(":
            return (-i)+len(tokens)

    return None

def complex_evaluation(tokens):
    """
    Input: A list of tokens (including parenthesis)
    Output: Returns a single floating point number corresponding to the result of the 
    tokenized arithmetic expression.
    """
    current_index = 0

    # While there are still brackets in the expression, find the deepest bracket in the list.
    while tokens.count("(") > 0 and tokens.count(")") > 0:
        current_index = find_last_bracket(tokens)
        # While the bracket hasn't been closed yet, find the closing bracket.
        while tokens[current_index] != ")":
            current_index += 1
        # Replace the slice of the list where the bracket started and ended with the evaluated expression.
        tokens[find_last_bracket(tokens):current_index+1] = [simple_evaluation(tokens[find_last_bracket(tokens)+1:current_index])]
    # When the expression contains no more brackets, we can simply use simple_evaluation to evaluate
    # the rest of the expression.
    return simple_evaluation(tokens)

def evaluation(string):
    """
    Input: A string containing a well-formed arithmetic expression
    Output: The single float corresponding to its result.
    """
    return complex_evaluation(tokenization(string))