# Create your own replace command

word = input("Enter a word: ")
string = input("Enter a string: ")
replace = input("Enter a replacement: ")

end = ""
for i in range(word.count(string)):
    end += (word[:word.find(string)])
    word = word[word.find(string)+len(string):]
    end += (replace)

end += word
print(end)