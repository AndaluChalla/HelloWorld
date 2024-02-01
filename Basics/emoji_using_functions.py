def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀😀😀",  ##### to get emojis hit ctrl+cmd+space
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
result = emoji_converter(message)
print(result)
