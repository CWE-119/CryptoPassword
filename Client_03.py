# random code using api
import requests
import random
import socket
import re


API_URL = "https://api-inference.huggingface.co/models/xlm-roberta-base"
headers = {"Authorization": f"Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# step to use here:
# The user should be giving a unique response phrase to generate the keywords

output = query({
    "inputs": "<mask>",
})

passwords_keys = []

for i in output:
    # print(i)
    for j in i:
        if j == 'sequence':
            print(i[j])
            x = i[j]
            x = x.split(" ")
            passwords_keys.append(x[0])

dictionary = "1234567890"


def key_generator(x):
    lists = x
    key = random.choice(lists)
    print(f"The chosen key phrase was: {key}")
    return key

generated_key = key_generator(passwords_keys)
key_number = 0
for i in generated_key:
    location_of_string = dictionary.find(i)
    key_number = location_of_string + key_number

# print(f"The final key is: {key_number}")
apiNumber = key_number

# sent to server
HOST = '127.0.0.1'

PORT = 9090
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
client.send("Hello World\n".encode('utf-8'))

# print whatever you receive form the server
received_message = client.recv(1024).decode('utf-8')
print(received_message)

received_message = client.recv(1024).decode('utf-8')
print(received_message)
some_string = received_message
num = re.findall(r'\d+', some_string)
s = [str(i) for i in num]
num = str("".join(s))
num = num[2:-4]
num = int(num)

# apiNumber = (int(apiNumber) ** float(num))
print(f"number is {num}")
lists = received_message.split(" ")
print(lists)


generated_seed = apiNumber + num
print(f"This is the generated seed: {generated_seed}")
client.send(f"{generated_seed}".encode('utf-8'))
