import tkinter as tk
import system_control as sys_c
root = tk.Tk()
root.geometry("400x200")
master = sys_c.Main_system()

def connect_comps():
    master.start_server()

def close_listen_fun():
    master.server.close()

Connection_frame = tk.Frame(root)
Connection_frame.grid(row=0,column=0)

connect_btn = tk.Button(Connection_frame, text= "Connect",command= connect_comps )
connect_btn.grid(row=0, column=0,padx=10)

close_listen_btn = tk.Button(Connection_frame, text="Close listen",command=close_listen_fun)
close_listen_btn.grid(row=0, column=1,padx=10)

root.mainloop()