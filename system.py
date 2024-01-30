import socket
import threading

class Main_system:
    def __init__(self):
        self.HEADER = 2084
        self.PORT = 5555
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER,self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.current_ship_pos = None

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen()
        
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        print(self.SERVER)
    
    def handle_client(self,conn,addr):
        conn.setblocking(False)
        connected = True
        while connected:
            client_msg = conn.recv(2048).decode(self.FORMAT)
            if client_msg == "!Connected":
                try:
                    conn.send(str("Works!")).encode(self.FORMAT)
                except Exception as e:
                    print(e)



    def start_server(self):
        conn, addr = self.server.accept()
        
        print("connected to: ", addr)
        thread = threading.Thread(target=self.handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")