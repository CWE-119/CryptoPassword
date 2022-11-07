import socket
import random


def generate_partial_phrase(x):
    random.seed(x)
    x = random.random()
    return x


# better to use the wireless LAN adapter Wi-Fi IP
# this is your device ip address
HOST = '127.0.0.1'

PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

# data = input("Enter data that you want to send")
# client.send(data.encode('utf-8'))

client.send("Hello World\n".encode('utf-8'))

# client.send("Hello World again\n".encode(('utf-8')))
# client.send("Hello World again and again\n".encode(('utf-8')))
# client.send("Hello World again and again and again\n".encode(('utf-8')))


# print whatever you receive form the server
received_message = client.recv(1024).decode('utf-8')
print(received_message)

received_message = client.recv(1024).decode('utf-8')
print(received_message)
lists = received_message.split(" ")
print(lists)

generated_seed = str(generate_partial_phrase(float(lists[4])))
print(f"This is the generated seed: {generated_seed}")
client.send(f"{generated_seed}".encode('utf-8'))
