# random code by using system time
import socket
import time

times = time.gmtime(0)
epoch = time.asctime(times)
t = round(time.time()*1000)
t = str(t)
t = t[5:]
t = int(t)


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


generated_seed = t
print(f"This is the generated seed: {generated_seed}")
client.send(f"{generated_seed}".encode('utf-8'))
