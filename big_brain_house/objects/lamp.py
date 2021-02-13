from client import Client

class Lamp(Client):
  
  def __init__(self, state):
    self.state = False
    self.type = 'Lamp'

  def receive(self, client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode(Client.FORMAT)
            print(f"Comando recebido: {message}")
            if message.split()[0] == "set_status":
                if message.split()[1] == "true":
                    self.state = True
                elif message.split()[1] == "false":
                    self.state = False
                else:
                    pass
            print(f"Novo status:{self.state}")
        except:
            print("An error occured!")
            client_socket.close()
            break
