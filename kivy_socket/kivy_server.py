import socket
import threading
import json
import os

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(1) # Restrict number of clients

# To avoid the following error     
# server.bind(ADDR)
# OSError: [Errno 98] Address already in use
os.system('sudo netstat -nlp | grep PORT')


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {ADDR} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            # convert back to dictionary
            msg_dict = eval(msg)

            k1 = list(msg_dict.keys())
            k2 = list(msg_dict[k1[0]].keys())
            lbl = ""
            for k in k1:
                lbl += k + "\t\t"
            print(lbl)

            for i in k2:
                    temp = ""
                    for k in k1:
                        temp += str(msg_dict[k][i]) + "\t\t"
                    print(temp)

            conn.send("Msg recvd".encode(FORMAT))
            print("\n")
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        print(f"connected with {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


if __name__ == "__main__":
    print(f"[STARTING] server is starting...")
    start()
