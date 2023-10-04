"""
Parentheses Clusters by Timothy Eden
Date Last Modified: October 4, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/Fpymv2HieqEd7ptAq
"""


def split(txt):
    """
    Since strings are difficult to work with, we first convert txt into a list for easier iteration. Our first cluster
    is initialized as a blank string, and our two accumulator variables, which count the number of opening and closing
    parentheses, are initialized at 0. The reason we use the while loop is because every time we iterate over a
    character in our "string" (list), we remove it, and we know we're done when the list gets empty. So, for every
    character, we add it to the cluster, then based on whether it is an opening or closing parenthese, we increment one
    of the accumulators, then delete that item from the list. At the end of each iteration, we check to see if the two
    accumulators are equal, which means our cluster is complete. If so, the cluster is added to the list that will be
    returned at the end, and everything is reset to begin the next cluster. Once we've iterated over everything, the
    list will be empty and we can return the result.
    """
    result = []
    txt_list = []
    for char in txt:
        txt_list.append(char)
    cluster = ''
    opening = 0
    closing = 0
    while len(txt_list) > 0:
        if txt_list[0] == '(':
            cluster += '('
            opening += 1
            del txt_list[0]
        elif txt_list[0] == ')':
            cluster += ')'
            closing += 1
            del txt_list[0]
        if opening == closing:
            result.append(cluster)
            cluster = ''
            opening = 0
            closing = 0
    return result


"""
A better solution found on Edabit:

def split(txt):
    a = []
    b = ""
    for i in txt:
        b += i
        if b.count("(") == b.count(")"):
            a.append(b)
            b = ""
    return a
"""


def main():
    assert split("()()()") == ["()", "()", "()"]
    assert split("") == []
    assert split("()()(())") == ["()", "()", "(())"]
    assert split("(())(())") == ["(())", "(())"]
    assert split("((()))") == ["((()))"]
    assert split("()(((((((((())))))))))") == ["()", "(((((((((())))))))))"]
    assert split("((())()(()))(()(())())(()())") == ["((())()(()))", "(()(())())", "(()())"]
    assert split("((()))(())()()(()())") == ["((()))", "(())", "()", "()", "(()())"]
    assert split("((())())(()(()()))") == ["((())())", "(()(()()))"]
    assert split("(()(()()))()(((()))()(()))(()((()))(())())") == \
           ["(()(()()))", "()", "(((()))()(()))", "(()((()))(())())"]


if __name__ == '__main__':
    main()
