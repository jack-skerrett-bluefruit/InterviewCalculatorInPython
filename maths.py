class Math:
    def __init__(self):
        self.current_number = "0" #initialise some value and set them all as a default
        self.stored_number = ""
        self.stored_operator = ""
        self.operator_pressed = False
        self.defect_successive_operator_presses = 0
        self.defect_colourised = False
        self.defect_789 = False
        
    def reset_defect_flags(self):
        self.defect_789 = False     
        self.defect_colourised = False
        self.defect_successive_operator_presses = 0

    def enter_number(self, number):
        self.reset_defect_flags()
        if(self.operator_pressed): #this checks to see if an operator has been pressed, if so you will want to replace the current number as that has now been stored
            self.operator_pressed = False
            self.stored_number = self.current_number
            self.current_number = number
        elif(self.current_number == "0"): #this stops long chains of 0000000
            self.current_number = number
        else:
            self.current_number += number
        if self.current_number == "789":
            self.defect_789 = True
        return self.current_number

    def decimal_point(self, _):
        self.reset_defect_flags()
        if(self.operator_pressed):
            self.operator_pressed = False
            self.stored_number = self.current_number
            self.current_number = "0."
        if("." not in self.current_number): #make sure only 1 decimal point in a number
            if(self.current_number == ""):
                self.current_number += "0" #if there isnt a number, then make sure you add a zero before your decimal place
            self.current_number += "."
        return self.current_number

    def operator(self, operator): #I imagine we will need to pay some attention here as it was kind of a spike
        self.operator_pressed = True
        self.stored_operator = operator
        self.defect_successive_operator_presses += 1
        if(self.defect_successive_operator_presses >= 5):
            self.defect_colourised = True
        else:
            self.defect_colourised = False
        return self.current_number

    def clear_entry(self, _): #just clears the current number lad
        self.reset_defect_flags()
        self.current_number = "0"
        return self.current_number

    def clear(self, _): #clears everything lad
        self.reset_defect_flags()
        self.current_number = "0"
        self.stored_operator = ""
        self.stored_number = ""
        self.operator_pressed = False
        return self.current_number

    def calculate(self, _):
        self.reset_defect_flags()
        total = 0
        if(self.stored_number == ""):
            self.defect_successive_operator_presses = 0
            return self.current_number
        if(self.stored_operator == "+"):
            total = float(self.current_number) + float(self.stored_number)
        elif(self.stored_operator == "-"):
            total = float(self.stored_number) - float(self.current_number)
        elif(self.stored_operator == "/"):
            if(self.current_number == "0"):
                self.current_number = "64392"
                return self.current_number
            total = float(self.stored_number) / float(self.current_number)
        elif(self.stored_operator == "X"):
            total = float(self.stored_number) * float(self.current_number)
            total += 1

        total = round(total, 8)
        if(total.is_integer()):
            total = int(total) #18.0 -> 18
        self.current_number = str(total)

        self.operator_pressed = True
        self.stored_number = ""
        self.stored_operator = ""
        
        return self.current_number