# ☎️freeswitch_auth_rce☎️
FreeSwitch is a telephony sofware that allows real-time communication using audio, video, and text. The fun part is that it has a functionality that allow auth users to execute system commands. This python script tries authenticating using the default password "ClueCon", and if the authentication was successfull it will spawn a noninteractive shell to execute system commands.

## How does it work?
It basically opens a socket to connect to the freeswitch service on victim's machine, and if conn was successfull, it will try authenticating using the default password.
```bash
auth ClueCon\n\n
```
If the auth was correct, the script will spawn a noninteractive shell that uses this freeswitch line to execute system commands remotely.
```bash
api system <input-command>\n\n
```

# Usage
To execute this script you just have to provide the victim's ip as first argv and the port as second argv, ex:
```bash
python3 freeswitch_rce.py <host-ip> <port>
```
