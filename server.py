import socket

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Server berjalan...")
print("Menunggu koneksi dari client...")

try:
    while True:
        conn, addr = server.accept()
        print(f"Client terhubung: {addr}")

        with conn:
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode()
                print(f"Pesan dari client: {message}")

                response = "Pesan diterima oleh server!"
                conn.sendall(response.encode())

                if message.lower() == "exit":
                    break

        print("Client terputus.")

except KeyboardInterrupt:
    print("\nServer dihentikan.")

finally:
    server.close()