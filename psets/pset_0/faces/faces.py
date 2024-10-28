# define the main function
def main():
    # get the input from the user
    content = input()
    # use the convert function to convert the text and print it
    print(convert(content))

# define the convert function
def convert(text):
    # replace the text with the emojis
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    # return the text
    return text

# call the main function
main()