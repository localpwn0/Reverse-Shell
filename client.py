from socket import *
from colorama import Fore, Style
import sys, random, time, os

class Client:
    b = Fore.BLUE
    g = Fore.GREEN
    c = Fore.CYAN
    reset = Style.RESET_ALL
    r = Fore.RED
    w = Fore.WHITE
    y = Fore.YELLOW


    def __init__(self):
        try:
            self.server_ip = str(sys.argv[2]).split(':')[0]
            self.server_port = str(sys.argv[2]).split(':')[1]
        except IndexError:
            self.cleaner()
            self.logo_printer()
            print("{}Usage : {}python {}{} {}connect {}ip{}:{}port\n{}example : {}python {}{} {}connect {}127.0.0.1{}:{}9050{}".format(
                self.g, self.r, self.b, sys.argv[0], self.r, self.w, self.g, self.w, self.g,
                self.r, self.b, sys.argv[0], self.r, self.w, self.g, self.w, self.reset
            ))
            sys.exit(True)
        
        self.make_loop(self.server_ip, self.server_port)
        

    def make_loop(self, ip, port):
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((str(ip), int(port)))
        self.cleaner()
        self.logo_printer()
        print("{}Type exit for break the loop{}".format(self.c, self.reset))
        while True:
            
            user_input = input("{}@> {}{}".format(self.g, self.y, self.reset))
            if user_input == "exit" or user_input == "Exit":
                break
            client.send(bytes(user_input, encoding="utf-8"))
            print('{}{}{}'.format(self.g, client.recv(1024).decode('utf-8'), self.reset))

        

    def logo_printer(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """

  _____                                 _____ _          _ _ 
 |  __ \         Version: 1.0          / ____| |        | | |
 | |__) |_____   _____ _ __ ___  ___  | (___ | |__   ___| | |
 |  _  // _ \ \ / / _ \ '__/ __|/ _ \  \___ \| '_ \ / _ \ | |
 | | \ \  __/\ V /  __/ |  \__ \  __/  ____) | | | |  __/ | |
 |_|  \_\___| \_/ \___|_|  |___/\___| |_____/|_| |_|\___|_|_|
            iran-cyber.net - github.com/localpwn0
                  Wrote by: iwHH with <3   
                   Telegram: @Localpwn                                              
        """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" %(random.choice(colors), line, clear))
            time.sleep(0.05)
    
    def cleaner(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

if __name__ == "__main__":
    run = Client()
