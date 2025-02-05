def emoji_converter(message):
    word = message.split(' ')

    emojis = {
        ":)": "◉‿◉",
        ":(": "┏༼ ◉ ┏┓◉༽┓",
        "xD": "(´∀｀)"
    }

    output = ""

    for word in word:
        output += emojis.get(word, word) + " "
    return output


command = input("> ")
emoji_message = emoji_converter(command)
print(emoji_message)
