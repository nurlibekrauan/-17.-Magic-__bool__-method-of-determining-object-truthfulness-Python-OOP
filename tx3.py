class Server:
    def __init__(self,load) -> None:
        self.load = load
    def __bool__(self):
        return self.load < 80
server1 = Server(load=50)
server2 = Server(load=85)

if server1:
    print("Server is operational.")  # Выводится
if server2:
    print("Server is operational.")  # Не выводится
