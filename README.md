# ollama-gemma3-technical-questions

This script utilizes the Ollama library to interact with a local Gemma 3 model. It combines a user-provided message with a predefined set of instructions, then sends the combined prompt to the model. The resulting output is displayed in the terminal and can be optionally saved to a Markdown file.  The script leverages the Gemma 3 model (specifically the 12B variant) for text generation.

## Prerequisites

*   **Python 3.7+:** This script requires Python 3.7 or a later version.
*   **Ollama:**  Ollama must be installed and a Gemma 3 model (e.g., `gemma3:12b`) must be pulled. See [https://ollama.com/](https://ollama.com/) for installation instructions.
*   **`ollama` Python Package:** Install the Ollama Python package using pip:

    ```bash
    pip install ollama
    ```

## Usage

1.  **Basic Execution:**

    To run the script, execute the following command in your terminal:

    ```bash
    python script.py
    ```

2.  **Input Options:**

    *   **Input File:** The script can read a message from a text file. By default, it attempts to read from a file named `message.txt`.  The file should contain plain text.
    *   **Interactive Input:** To provide a message interactively, set the `infile` variable to `None` within the script before execution.  This will prompt you to enter the message directly in the terminal.

## Configuration

The script's behavior is controlled by several variables.  These variables are defined at the beginning of the script and can be modified to adjust functionality.

### Variable Definitions

| Variable     | Description                                                        | Data Type | Default Value |
| :----------- | :----------------------------------------------------------------- | :-------- | :------------ |
| `autosave`   | Automatically saves the generated response to a file.  If `False`, the script prompts the user for confirmation before saving. | `bool`     | `True`        |
| `infile`     | Path to a file containing the input message. Set to `None` for interactive input. | `str`      | `'message.txt'`|
| `instructions` | A list of instructions to provide to the Gemma 3 model.  These instructions guide the model's output style and content. | `list`     | *See example below* |

### Example `instructions` List

The `instructions` list significantly influences the generated output.

```python
instructions = ["Write using technical writing principles.",
                "Frequently use ordered lists, unordered lists, and tables to display information.",
                "Use bold, italics, and underlining to emphasize key phrases.",
                "If applicable to the subject, use code blocks for examples.",
                "Do not write backronyms more than once.",
                "Format your response using markdown syntax.",
                "At the top of your response, write 'Generated with Gemma. Distribution of this material is unrestricted.",
                "At the bottom of your response, write 'This material is AI-generated. Information may be inaccurate."]
```

## Output

The script prints the generated response from the Gemma 3 model to the terminal.  If `autosave` is `True` or the user confirms saving, the response is also saved to a file named `ollama-message-{timestamp}.md`, where `{timestamp}` is the current date and time in UTC.

## Error Handling

*   The script assumes Ollama is running and the specified Gemma 3 model is available. If either of these conditions is not met, the script will likely encounter an error during the `chat` function call.
*   File I/O errors may occur if the `infile` is not found or if there are issues writing to the output file.
