# ask the user a question
print("What is the Answer to the Great Question of Life, the Universe, and Everything?")

# get the user's response
response = str(input("> "))

# convert the response to lower-case & strip leading whitespace
response = response.lower().strip()

if response == "42" or response == "forty two" or response == "forty-two":
    print("Yes")
else:
    print("No")