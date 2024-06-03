# Basic Python Keylogger

This is a basic keylogger program written in Python that records and logs all keystrokes on a computer. The keystrokes are saved to a log file.

## Features

- Records all alphanumeric keys and special keys.
- Logs keystrokes to a specified file.

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/metaphor11/basic-python-keylogger.git
cd basic-python-keylogger
```

2. Install the required `pynput` library:

```sh
pip install pynput
```

## Usage

1. Run the keylogger script:

```sh
python keylogger.py
```

2. The keylogger will start recording keystrokes and saving them to `key_log.txt` in the same directory.

## Code Explanation

### `keylogger.py`

1. **Import the `pynput` library**:
    - `from pynput import keyboard` imports the necessary module to monitor keyboard events.

2. **Specify the log file**:
    - `log_file = "key_log.txt"` sets the filename where keystrokes will be logged.

3. **Define the `on_press` function**:
    - This function handles key press events.
    - It tries to write the character of the key pressed to the log file.
    - If the key is a special key (e.g., Shift, Ctrl), it catches an `AttributeError` and logs the key name in a formatted way.

4. **Start the keyboard listener**:
    - `with keyboard.Listener(on_press=on_press) as listener: listener.join()` starts the listener that will call the `on_press` function whenever a key is pressed.

## Ethical Considerations

- **Permission**: Always get explicit permission before running a keylogger on any device.
- **Usage**: Ensure the keylogger is used for ethical purposes, such as testing security or monitoring your own devices.
- **Legal Compliance**: Be aware of and comply with all relevant laws and regulations regarding the use of such software in your jurisdiction.

## Disclaimer

This script is for educational purposes only. Misuse of keylogger software can lead to severe legal consequences. Always use such tools responsibly and ethically.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
