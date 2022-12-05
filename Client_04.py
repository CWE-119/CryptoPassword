import socket
import random
import time

t = round(time.time() * 1000)
t = str(t)
t = t[int(-random.random()):int(t)]
t = int(t) ** abs(int(random.random()*10000))
print(t)


# t = int(t)

def generate_partial_phrase(x):
    random.seed(x)
    y = random.random()
    z = y
    random.seed(z)
    return random.random()


randoms = (int(generate_partial_phrase(t) * 10 ** 8))

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

generated_seed = str(randoms)
print(f"This is the generated seed: {generated_seed}")
client.send(f"{generated_seed}".encode('utf-8'))
