import socket

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)

try:
    client.connect((HOST,PORT))
    print("Berhasil terhubung ke server!")
    print("Ketik 'exit' untuk keluar.")

    while True:
        message= input("Masukkan pesan: ")

        client.sendall(message.encode())

        response = client.recv(1024).decode()
        print("Balasan Server:" ,response)

        if message.lower()=="exit":
            break

except ConnectionRefusedError:
    print("Gagall terhubung. Pastikan server sudah berjalan.")

finally:
    client.close()
    print("Koneksi client ditutup.")