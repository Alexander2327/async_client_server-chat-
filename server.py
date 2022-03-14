from Socket import Socket
import asyncio


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.users = []

    def set_up(self):
        self.socket.bind(('127.0.0.1', 9997))
        self.socket.listen()
        self.socket.setblocking(False)
        print('Server is listening')

    async def send_data(self, data):
        for user in self.users:
            await self.main_loop.sock_sendall(user, data)

    async def listen_socket(self, listened_socket=None):
        if not listened_socket:
            return
        while True:
            try:
                data = await self.main_loop.sock_recv(listened_socket, 2048)
                await self.send_data(data)
            except ConnectionResetError:
                self.users.remove(listened_socket)
                return

    async def accept_sockets(self):
        while True:
            client, addr = await self.main_loop.sock_accept(self.socket)
            print(f'User {addr[0]} connected!')
            client.send('You are connected'.encode('utf-8'))
            self.users.append(client)
            self.main_loop.create_task(self.listen_socket(client))

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())


if __name__ == '__main__':
    server = Server()
    server.set_up()
    server.start()
