import pyautogui
import time
import keyboard
from tkinter import *
from tkinter import ttk
import tkinter as tk

window = Tk()

def algorythm():
    pyautogui.hotkey('win', 'r')  
    pyautogui.typewrite('notepad')  
    pyautogui.press('enter')  
    time.sleep(2)

    lower_step = lower_step_num.get() 
    higher_step = higher_step_num.get()
    your_text=filled_text.get()
    lower_step=int(lower_step)
    higher_step=int(higher_step)

    for i in range(lower_step, higher_step + 1):        
        generated_string = your_text.format(i=i)
        keyboard.write(generated_string+'\n')
        time.sleep(0.5)

    pyautogui.hotkey('ctrl', 's')  
    time.sleep(1)
    keyboard.write('пример_1.txt')  
    pyautogui.press('enter')  
    pyautogui.hotkey('alt', 'f4')  

lower_step_num = ttk.Entry(window)
higher_step_num = ttk.Entry(window)
low_num = ttk.Label(window,
    text='Укажите минимальное число',
    width=60,
    anchor=S
)
high_num = ttk.Label(window,
    text='Укажите максимальное число',
    width=60,
    anchor=S
)
changed_text= ttk.Label(window,
    text='Введите текст, в котором хотите изменить число, изменяемое число обозначьте "{i}"',
    width=80,
    anchor=S
)
filled_text=ttk.Entry(window, width=100)
button_ip_3 = ttk.Button(window,
    text="Start",
    command=algorythm,
    width=60,
)

low_num.pack(fill=tk.BOTH, expand=True)
lower_step_num.pack(fill=tk.BOTH, expand=True)
high_num.pack(fill=tk.BOTH, expand=True)
higher_step_num.pack(fill=tk.BOTH, expand=True)
changed_text.pack(fill=tk.BOTH, expand=True)
filled_text.pack(fill=tk.BOTH, expand=True)
button_ip_3.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

window.mainloop()