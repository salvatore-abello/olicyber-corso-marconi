import pwn

host = "tcp.challs.olicyber.it"
port = 12210

# 

remote = pwn.remote(host, port)
remote.interactive() # Ci permette di comunicare con il server come se si stesse usando una CLI

# Per inviare roba
# remote.sendline("ciao") -> remote.send("ciao\n")
# remote.send("ciao")

# Per ricevere roba
# remote.recvline
# remote.recv(n)


