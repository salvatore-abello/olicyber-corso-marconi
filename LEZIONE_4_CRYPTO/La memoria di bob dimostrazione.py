from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

key = b"A"*16
chat = b"flag{test}"
cipher = AES.new(key, AES.MODE_ECB)

def split_len(s, l):
    return [s[x:x+l] for x in range(0, len(s), l)]

def main():
    mittente = b"Bob: "
    loop = '1'
    while loop == '1':
        msg = input(f'Dammi il tuo messaggio segreto:\n{mittente}').encode()
        plaintext = mittente + msg + chat
        print("PLAINTEXT: ")
        for x in split_len(pad(plaintext, 16), 16):
            print(x.hex(), x)
            
        ciphertext = cipher.encrypt(pad(plaintext, 16))

        print("CIPHERTEXT: ")
        for x in split_len(ciphertext, 16):
            print(x.hex(), x)
        print('ecco la nostra conversazione super protetta. Nessuno potrà decriptare questo messaggio!')
        print(b64encode(ciphertext).decode())
        loop = input(
            'non è il messaggio che volevi mandare?\nRiprova pure premendo 1\n')[0]
    print('ciao ;-)')


if __name__ == '__main__':
    main()
