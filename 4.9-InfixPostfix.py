from pythonds.basic import Stack

def infixToPostfix(expression):

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    tempStack = Stack()
    postfixList = []
    tokenList = expression.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":

            postfixList.append(token)
        elif token == "(":
            tempStack.push(token)
        elif token == ")":
            toptoken = tempStack.pop()
            while toptoken != '(':
                postfixList.append(toptoken)
                toptoken = tempStack.pop()
        else:
            while (not tempStack.isEmpty()) and (prec[tempStack.peek()] >= prec[token]):
                postfixList.append(tempStack.pop())
            tempStack.push(token)

    while not tempStack.isEmpty():
        postfixList.append(tempStack.pop())

    return " ".join(postfixList)

def main():
    print(infixToPostfix("A * B + C * D"))

main()
