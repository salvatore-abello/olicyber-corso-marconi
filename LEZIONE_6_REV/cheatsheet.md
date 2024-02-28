# Cheatsheet comandi gdb

## Breakpoint
```shell
b <nome funzione>
b *<indirizzo>
# Esempio: b main
# Esempio: b *0x55555555609d
```

## Ricerca di stringhe/valori in memoria
```shell
grep <stringa/valore>
# Esempio: grep "flag"
```

## Ricerca di stringhe nello stack
```shell
x/s $rsp
x/100s $rsp
x/200s $rsp
...
```

## Runnare l'eseguibile
```shell
run
r
```

## Continuare l'esecuzione
```shell
continue
c
```

## Selezionare il file da debuggare
```shell
file <nomefile>
# Esempio: file ./trulySecureGate
```

## Visualizza la lista dei breakpoint
```shell
i b
```

## Rimozione di un breakpoint
```shell
del <numero breakpoint>
# Esempio: del 1
```

## Visualizzare l'assembly di una funzione
```shell
disass <nome funzione>
# Esempio: disass main
```

## Chiamare una funzione
```shell
call <nome funzione con cast e parametri se necessario>
# Esempio
call (int)serie(1000)
```
