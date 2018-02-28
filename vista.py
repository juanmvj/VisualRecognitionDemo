import tkinter
from pru_cla import conexion as cx
import pru_cla



class WatsonApp(tkinter.Tk):
    
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("WatsonVRec")
        self.geometry("400x400")

        self.button = tkinter.Button(text="train Watson", command=self.on_button_click_train)
        self.button1 = tkinter.Button(text="Start Watson Visual Recognition", command=self.on_button_click)
        self.label = tkinter.Label("")
        self.label["text"] = "Start and choose an image"
        
        
        self.button1.pack(expand=1)
        self.label.pack(fill=tkinter.BOTH, expand=1)
        self.button.pack( expand=1)

        


    def on_button_click(self):
        
        self.label["text"] = cx()

    def on_button_click_train(self):
        self.label["text"] = "Entrenando..."
        pru_cla.clasificar()




if __name__ == "__main__":
    application = WatsonApp()
    application.mainloop()


