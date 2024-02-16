import re
from pwn import *


r = remote("hcaptcha.challs.olicyber.it", 20007)

r.recvlines(2)

patterns = {
    "  _(__  <": '3',
    "|____  \ ": '5',
    "/   __  \ ": '6',
    "/  ____/ ": '2',
    "_)    (__ ": '*',
    ">      < ": '8',
    "\____    / ": '9',
    "   /    /": '7',
    " ______": '-',
    " /  /_\  \  ": '0',
    " |   |": '1',
    "/   |  |_": '4',
    " __|  |___ ": '+'
}

def find_all_occurrences_multiple(string, substrings):
    occurrences = {}
    for substring in substrings:
        start = 0
        while True:
            start = string.find(substring, start)
            if start == -1:
                break
            occurrences[start] = patterns[substring]
            start += 1
    return occurrences

for i in range(100):
    to_parse = r.recvuntil(b"Risposta: ", True).decode().split("\n")[2]

    indexes = find_all_occurrences_multiple(
        to_parse, patterns
    )

    to_eval = ''
    for x in sorted(indexes):
        to_eval += indexes[x]
        
    r.sendline(f"{eval(to_eval)}")
    print(f"{i}%")

r.interactive()
