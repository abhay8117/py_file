'''This Python project uses the langdetect module (see pip install instructions) to help us identify the language that has been entered. This can be really useful if you’re unsure which language you’re dealing with. 

This is another example where we have used tkinter to create a simple GUI involving labels, buttons, and an entry field. We can then collect text from the entry field and process this with the langdetect to determine which language was entered. Finally, we print this result to the GUI to let the user know the result.

Note that the results returned by langdetect are abbreviated language codes. For example, if we enter English text, we will see ‘en’ as the return value.

Source Code:
'''
'''
Language Detector
-------------------------------------------------------------
pip install langdetect
'''


from langdetect import detect
import tkinter as tk


def detect_lang():
   window = tk.Tk()
   window.geometry('600x400')
   head = tk.Label(window, text='Language Detector', font=('Calibri 15'))
   head.pack(pady=20)

   def check_language():
       new_text = text.get()
       lang = detect(str(new_text))
       tk.Label(window, text=lang, font=('Calibri 15')).place(x=260, y=200)

   text = tk.StringVar()
   tk.Entry(window, textvariable=text).place(
       x=200, y=80, height=30, width=280)
   tk.Button(window, text='Check Language',
             command=check_language).place(x=285, y=150)
   window.mainloop()


if __name__ == '__main__':
   detect_lang()