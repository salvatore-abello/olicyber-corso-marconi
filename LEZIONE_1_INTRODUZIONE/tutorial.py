import pwn

host = "tcp.challs.olicyber.it"
port = 12210

# 

remote = pwn.remote(host, port)
remote.interactive()

# Per inviare roba
# remote.sendline("ciao") -> remote.send("ciao\n")
# remote.send("ciao")

# Per ricevere roba
# remote.recvline
# remote.recv(n)


