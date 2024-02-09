import pwn # pip install pwntools

HOST = "2048.challs.olicyber.it"
PORT = 10007

remote = pwn.remote(HOST, PORT)

# Prodotto
# Potenza
# Somma
# Differenza
# Divisione intera

# Rimuovere roba inutile
remote.recvlines(2)

for _ in range(2048):
    data = remote.recv().decode().split() # Riceve la prima operazione da fare e splittarla
    
    operatore, num1, num2 = data
    # Stessa cosa di sta roba qua
    # operatore = data[0]
    # num1 = data[1]
    # num2 = data[2]
    
    num1 = int(num1)
    num2 = int(num2)
    
    print(operatore, num1, num2)
    
    match operatore:
        case "SOMMA":
            res = num1 + num2
        case "DIFFERENZA":
            res = num1 - num2
        case "PRODOTTO":
            res = num1 * num2
        case "POTENZA":
            res = num1 ** num2
        case "DIVISIONE_INTERA":
            res = num1 // num2
    
    remote.sendline(f"{res}")
    
# Non si sa come il server ci invierà la flag, quindi utilizziamo interactive
remote.interactive()
    
    

