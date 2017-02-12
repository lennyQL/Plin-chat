#<=====Plin's GUI=====>

import tkinter as tk

###############
# interface
###############

def run():
# global variable
    global enter, response_area, lb, action

# main window
    root = tk.Tk()
# window size
    root.geometry("880x560")
# window title
    root.title("Chat Bot : PLIN")
#  font
    font = ("Helevetica", 14)
    font_log = ("Helevetica", 11)


# main loop
    root.mainloop()

#*****main program*****
if __name__ == "__main__":
    run()
