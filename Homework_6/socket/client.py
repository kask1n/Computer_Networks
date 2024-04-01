import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            elif message == "!quit":
                print(">>> Logged out.")
                client.close()
                break
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        data_in = input("")
        if data_in == "!quit":
            client.send(data_in.encode("utf-8"))
            # client.close()
            break
        else:
            message = "{}: {}".format(nickname, data_in)
            client.send(message.encode("utf-8"))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
