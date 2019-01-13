import socket, threading
from tkinter import *

def send():
    while True:
        msg = input('\nMe > ')
        cli_sock.send(msg.encode())

def receive():
    while True:
        data = cli_sock.recv(1024)

        #print('\n' + str(data.decode()))
        mylist.insert(END,str(data.decode()) )
        mylist.see(END)
def enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    mylist.insert(END,'me > '+input_get)
    mylist.see(END)
    cli_sock.send(input_get.encode())
  #  label = Label(canvas, text=input_get)
    input_user.set('')
   # label.pack()
    return "break"
if __name__ == "__main__":   
    # socket
    window = Tk()
    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)
    vbar=Scrollbar(window,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    mylist = Listbox(window, yscrollcommand = vbar.set )

    mylist.pack( fill=BOTH, expand=True )
    vbar.config(command=mylist.yview)
    input_field.bind("<Return>", enter_pressed)
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5023
    cli_sock.connect((HOST, PORT))     
    print('Connected to remote host...')
   
    uname = input('Enter your name to enter the chat > ')
    cli_sock.send(uname.encode())
    mylist.insert(END,'welcome '+uname)
    """thread_send = threading.Thread(target = send)
    thread_send.start()"""

    thread_receive = threading.Thread(target = receive)
    thread_receive.start()
    window.mainloop()
