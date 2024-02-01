message = input(">")
words = message.split(' ')
print(words)
emojis = {
    ":)" : "😀😀😀", ##### to get emojis hit ctrl+cmd+space
    ":(" : "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
