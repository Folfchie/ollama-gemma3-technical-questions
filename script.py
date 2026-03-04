from ollama import chat
import datetime

autosave = True
# Setting infile to None allows you to type a prompt.
# infile only supports plain text messages!
infile = 'message.txt'

instructions = ["Write using technical writing principles.",
                "Frequently use ordered lists, unordered lists, and tables to display information.",
                "Use bold, italics, and underlining to emphasize key phrases.",
                "If applicable to the subject, use code blocks for examples.",
                "Do not write backronyms more than once.",
                "Format your response using markdown syntax.",
                "At the top of your response, write 'Generated with Gemma. Distribution of this material is unrestricted.",
                "At the bottom of your response, write 'This material is AI-generated. Information may be inaccurate."]

while True:
    if infile:
        with open(infile, 'r') as f:
            message = f.read()
    else:
        message = input("\nEnter your message: ")
    print("\nGenerating response...")
    response = chat(
        model='gemma3:12b',
        messages=[{'role': 'user', 'content': f'Instructions:\n{instructions}\nMessage:\n{message}'}],
    )
    print(response.message.content)
    if autosave:
        save = "y"
    else:
        save = input("\nDo you want to save this message? (y/n): ")
    if save == "y":
        print("\nSaving...")
        with open(f'ollama-message-{datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H%M%SZ")}.md', 'w') as outfile:
            outfile.write(response.message.content)
            print("Message Saved")
    elif save == "n":
        print("\nNot Saved")
    else:
        print("\nPlease enter either 'y' or 'n'")
    if infile:
        print("\nExiting...")
        exit()
