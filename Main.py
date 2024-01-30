import tkinter as tk
import system_control as sys_c
from time import sleep
root = tk.Tk()
root.geometry("400x200")
master = sys_c.Main_system()

def connect_comps():
    master.start_server()

def close_listen_fun():
    master.server.close()

def shut_computers_fun():
    master.gui_msg = "shutdown /s"
    sleep(0.5)
    master.gui_msg = ""

Connection_frame = tk.Frame(root)
Connection_frame.grid(row=0,column=0)

connect_btn = tk.Button(Connection_frame, text= "Connect",command= connect_comps )
connect_btn.grid(row=0, column=0,padx=10)

close_listen_btn = tk.Button(Connection_frame, text="Close listen",command=close_listen_fun)
close_listen_btn.grid(row=0, column=1,padx=10)

shut_computers_btn = tk.Button(Connection_frame, text="System_shutdown",command=shut_computers_fun)
shut_computers_btn.grid(row=0, column=2,padx=10)

text_input = tk.Text(Connection_frame,width= 10,height=2).grid(row=1,column=0)


root.mainloop()