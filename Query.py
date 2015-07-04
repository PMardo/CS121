import tkinter
import sys
from resultInterface import ResultApplication
from Scorer import Scorer

DEFAULT_FONT = ('Verdana', 12)

class NameDialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        self._dialog_window.geometry("600x300")
        self._dialog_window.title("Informatics 121")
        
        query_label = tkinter.Label(
            master = self._dialog_window, text = 'Search:',
            font = ('Helvetica', 20))

        query_label.grid(
            row = 3, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)
        
        self._query_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        
        self._query_entry.grid(
        row = 3, column = 1, columnspan = 10, padx = 10, pady = 1,
        sticky = tkinter.W + tkinter.E)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self._dialog_window.rowconfigure(10, weight = 2)
        self._dialog_window.columnconfigure(10, weight = 2)
        
        self._dialog_window.config(height = 600, width = 300)
        
        self._ok_clicked = False
        self._query = ''
        
    def show(self):
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self):
        return self._ok_clicked

    def get_query(self):
        return self._query
    
    def _on_ok_button(self):
        self._ok_clicked = True
        self._query = self._query_entry.get()
        self._dialog_window.destroy()
        
    def _on_cancel_button(self):
        self._dialog_window.destroy()
        sys.exit(0)
        
class IntroApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._root_window.withdraw()
        self._on_intro()
        self._query = ''
        
    def start(self):
        self._root_window.mainloop()        

    def _on_intro(self):      
        dialog = NameDialog()
        dialog.show()
        self._root_window.destroy()

        if dialog.was_ok_clicked():
            self._query = dialog.get_query()
            with open("Store/Results.txt", "w") as q:
                top_urls = []
                top_urls = Scorer.Get_RelevancyList(self._query)
                if top_urls is not None:
                    q.write("Top Results for: "+self._query+"\n")
                    i = 1
                    for url in top_urls:                
                        q.write(str(i)+". "+url+"\n")
                        i += 1
                    q.write("\n")           
                else:
                    q.write("No Results for: "+self._query+"\n\n")

if __name__ == '__main__':
    Scorer = Scorer()
    Scorer.Calc_Doc_Mags()
    while True:
        IntroApplication().start()
        ResultApplication("Store/Results.txt")
