import tkinter as tk
root = tk.Tk()
root.geometry("400x200")



Connection_frame = tk.Frame(root)
Connection_frame.grid(row=0,column=0,padx=15)

user_input = tk.Button(Connection_frame, text= "Connect")
user_input.grid(row=0, column=0)




root.mainloop()