from monitor_keystrokes import MonitorKeyStrokes
from monitor_mouse import MonitorMouse
from pynput import mouse, keyboard
from logger import Logger
from threading import Thread
from config import config
from time import sleep

csv_logger = Logger()
m_mouse = MonitorMouse()
m_keyboard = MonitorKeyStrokes()


def on_move(x, y):
    m_mouse.update(x, y)


def on_press(key):
    m_keyboard.update()


def update_logger():
    while True:
        csv_logger.update_log(m_mouse, m_keyboard)
        sleep(config["LOG_INTERVAL"])


if __name__ == "__main__":

    logger_thread = Thread(target=update_logger, args=())

    m_listener = mouse.Listener(on_move=on_move)
    kb_listener = keyboard.Listener(on_press=on_press)

    m_listener.start()
    kb_listener.start()
    logger_thread.start()
    logger_thread.join()
    m_listener.join()
    kb_listener.join()
