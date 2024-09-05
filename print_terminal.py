class Display_para:
    
    def display_terminal(self,pos_1, pos_2):
        run = "____________________________"
        step = list(run)
        step.insert(pos_1, "1")
        step.insert(pos_2, "0")
        print("".join(step))
        
    def display_terminal_1(self,pos_1):
        run = "_______________________________________"
        step = list(run)
        step.insert(pos_1, "1")
        print("".join(step))