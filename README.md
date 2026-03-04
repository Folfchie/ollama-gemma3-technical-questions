# Synopsis

This script combines user input (`message` variable) with a set of predefined instructions (`instructions` variable) and sends the result to a Gemma 3 model running locally via Ollama.
The output is printed to the terminal and can optionally be saved to a markdown file.

# Usage

```bash
$ python script.py
```

# Notes

- The `autosave` variable can be set to True or False. If set to False, the user will be prompted if they want to save the output after it is printed to the terminal.
- Setting the `infile` variable to None allows you to type a prompt from the terminal when executing the script.
