def checkio(expression):
    last = ""
    for i in expression:
        if i == "(":
            last += "p"
        elif i == "[":
            last += "b"
        elif i == "{":
            last += "c"
        elif i == ")":
            if last == "":
                return False
            if last[-1] != "p":
                return False
            else:
                last = last[:-1]
        elif i == "]":
            if last == "":
                return False
            if last[-1] != "b":
                return False
            else:
                last = last[:-1]
        elif i == "}":
            if last == "":
                return False
            if last[-1] != "c":
                return False
            else:
                last = last[:-1]
        print(last)
    if last=="":
        return True
    else:
        return False
