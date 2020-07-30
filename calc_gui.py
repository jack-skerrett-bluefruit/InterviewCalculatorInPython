from tkinter import *
from maths import Math

#add in history of button presses so you can see what you are typing

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.maths = Math()
        self.grid()
        self.label = Label(self, bg = "white", font = ("Arial", 25), borderwidth = 2, relief = "groove", text = "0", anchor=E)
        self.label.bind("<Button-3>", window_duplicator)
        self.label.grid(column = 0, row = 1, columnspan = 5, sticky = "ew")
        self.create_buttons()    

    def create_buttons(self):
        self.buttons = []
        self.button_position = 0
        self.create_button("1", 0, 5)
        self.create_button("2", 1, 5)
        self.create_button("3", 2, 5)
        self.create_button("X", 3, 5)
        self.create_button("=", 4, 5, rowSpan = 2)
        self.create_button("4", 0, 4)
        self.create_button("5", 1, 4)
        self.create_button("6", 2, 4)
        self.create_button("-", 3, 4)
        self.create_button("C", 4, 4)
        self.create_button("7", 0, 3, font = "Comic Sans MS")
        self.create_button("8", 1, 3)
        self.create_button("9", 2, 3)
        self.create_button("+", 3, 3)
        self.create_button("CE", 4, 3)
        self.create_button("0", 0, 6, columnSpan = 2)
        self.create_button(".", 2, 6)
        self.create_button("/", 3, 6)

    def create_button(self, text, column, row, columnSpan = 1, rowSpan = 1, font = "Arial", fontSize = 30):
        self.buttons.append(Button(self, text = text, font = (font, fontSize)))
        self.buttons[self.button_position].bind("<Button-1>", self.parse_button)
        self.buttons[self.button_position].bind("<Button-3>", window_duplicator)
        self.buttons[self.button_position].grid(column = column, row = row, columnspan = columnSpan, rowspan = rowSpan, sticky = "nesw")
        if(text == "CE"):
            self.buttons[self.button_position].bind("<Enter>", self.CE_disabled)
            self.buttons[self.button_position].bind("<Leave>", self.CE_enabled)
        self.button_position += 1
        

    def parse_button(self, event):
        #switcher is a dictionary holds references to all the different keys
        #we can press, and what functions should be called when those keys are pressed
        switcher = {
            "1": self.maths.enter_number,
            "2": self.maths.enter_number,
            "3": self.maths.enter_number,
            "4": self.maths.enter_number,
            "5": self.maths.enter_number,
            "6": self.maths.enter_number,
            "7": self.maths.enter_number,
            "8": self.maths.enter_number,
            "9": self.maths.enter_number,
            "0": self.maths.enter_number,
            ".": self.maths.decimal_point,
            "+": self.maths.operator,
            "-": self.maths.operator,
            "/": self.maths.operator,
            "X": self.maths.operator,
            "CE":self.maths.clear_entry,
            "C": self.maths.clear,
            "=": self.maths.calculate
        }
        if(event.widget["text"] == "3"):
            calculated_number = self.maths.enter_number("4")
        else:
            calculated_number = switcher[event.widget["text"]](event.widget["text"])
        self.label["text"] = calculated_number   

        if(float(calculated_number) < 0):
            self.label["anchor"] = W
        else:
            self.label["anchor"] = E

        if(self.maths.defect_colourised):
            self.label["background"] = "Blue"
        else:
            self.label["background"] = "White"          

        if(self.maths.defect_789):
            self.buttons[12]["text"] = ""
        else:
            self.buttons[12]["text"] = "9"
        
    def CE_disabled(self, event):
        self.buttons[14]["state"] = DISABLED

    def CE_enabled(self, event):
        self.buttons[14]["state"] = NORMAL

def window_duplicator(event):
    main()

def main():
    window = Tk()
    window.resizable(True, False)
    window.title("Claculator")
    calculator = Application(window)
    window.mainloop()
    
if __name__ == "__main__":
     main()