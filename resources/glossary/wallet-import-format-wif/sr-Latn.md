---
term: Wallet FORMAT UVOZA (WIF)
---

Metoda za kodiranje privatnog ključa Bitcoin na način da se može lakše uvesti ili izvesti između različitih novčanika. WIF se zasniva na kodiranju `Base58Check`, koje uključuje informacije o verziji, kompresiji odgovarajućeg javnog ključa i kontrolni zbir za otkrivanje grešaka pri kucanju. WIF privatni ključ počinje sa znakovima `5` za nekompresovane ključeve, ili `K` i `L` za kompresovane ključeve, i sadrži sve znakove potrebne za rekonstrukciju originalnog privatnog ključa. WIF format pruža standardizovano sredstvo za prenos privatnog ključa između različitih Wallet softvera.