def popular_words(text, words):
    # your code here
    text = text.lower()
    slicedText = text
    dic = {}
    for str in words:
        dic[str] = 0
        slicedText = text
        while slicedText.find(str) != -1:
            slicedText = slicedText[slicedText.find(str) + len(str):]
            dic[str] += 1
        
    return dic
F = open('file.txt', 'r')
file = F.read()
words = ['guerra', 'vitória']
print(popular_words(file, words))
