import threading
from tkinter import *
from tkinter import simpledialog

import grpc

import proto.chat_pb2 as chat
import proto.chat_pb2_grpc as rpc

address = 'localhost'
port = 9999

class Client:
  def __init__(self, name: str, window):
    self.window = window
    self.display_name = name

    channel = grpc.insecure_channel(address + ':' + str(port))
    self.conn = rpc.ChatServerStub(channel)

    threading.Thread(target=self.__listen_for_messages, daemon=True).start()
    self.__setup_ui()
    self.window.mainloop()

  def __listen_for_messages(self):
    for note in self.conn.ChatStream(chat.Empty()):
      print("R[{}] {}".format(note.name, note.message))
      self.chat_list.insert(END, "[{}] {}\n".format(note.name, note.message))

  def __send_message(self, event):
    message = self.entry_message.get()
    if message != '':
      n = chat.Note()
      n.name = self.display_name
      n.message = message
      print("S[{}] {}".format(n.name, n.message))
      self.conn.SendNote(n)

  def __setup_ui(self):
    self.chat_list = Text()
    self.chat_list.pack(side=TOP)
    self.lbl_display_name = Label(self.window, text=self.display_name)
    self.lbl_display_name.pack(side=LEFT)
    self.entry_message = Entry(self.window)
    self.entry_message.bind('<Return>', self.__send_message)
    self.entry_message.focus()
    self.entry_message.pack(side=BOTTOM)


if __name__ == '__main__':
  root = Tk()
  frame = Frame(root, width=300, height=300)
  frame.pack()
  root.withdraw()
  display_name = None
  while display_name is None:
    display_name = simpledialog.askstring("表示名", "表示名を入力してください", parent=root)
  root.deiconify()
  c = Client(display_name, frame)
