def token_maker(text: str):
    if text[0] == " ":
        return ("Space", " ")
    else:
        return ("Error", text[0])

def skaner(text: str):
    tab = []
    with open('test.txt', 'r') as file:
        text = file.read()
        print(repr(text))
        while len(text)>0:
            token = token_maker(text)
            text = text[len(token[1]):]
            tab.append(token)
    print(tab)
    return tab

skaner("")