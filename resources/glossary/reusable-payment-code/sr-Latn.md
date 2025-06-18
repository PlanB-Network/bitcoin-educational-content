---
term: PONOVLJIVI KOD ZA PLAĆANJE
---

U BIP47, višekratno upotrebljiv kod za plaćanje je statični identifikator generisan iz Bitcoin Wallet koji omogućava transakciju obaveštenja i derivaciju jedinstvenih adresa. Ovo izbegava ponovnu upotrebu adresa, što dovodi do gubitka privatnosti, bez potrebe za ručnim derivisanjem i prenosom novih, neiskorišćenih adresa za svaku uplatu. U BIP47, višekratno upotrebljivi kodovi za plaćanje se konstruiraju na sledeći način:


- Bajt 0 odgovara verziji;
- Bajt 1 je bit polje za dodavanje informacija u slučaju specifične upotrebe;
- Bajt 2 označava paritet `y` javnog ključa;
- Od bajta 3 do bajta 34, naći ćete `x` vrednost javnog ključa;
- Od bajta 35 do bajta 66, nalazi se lančani kod povezan sa javnim ključem;
- Od bajta 67 do bajta 79, postoji popunjavanje nulama.


Deo čitljiv za ljude (HRP) se obično dodaje na početku koda za plaćanje, a kontrolni zbir na kraju, a zatim se kodira u base58. Konstrukcija koda za plaćanje je stoga prilično slična konstrukciji proširenog ključa. Evo mog BIP47 koda za plaćanje u base58, na primer:


```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```


U implementaciji PayNym-a BIP47, kodovi za plaćanje mogu biti izraženi i u obliku identifikatora povezanih sa slikom robota. Evo mog, na primer:


```text
+throbbingpond8B1
```


Korišćenje platnih kodova sa PayNym implementacijom trenutno je dostupno na Sparrow Wallet na računaru i na Samourai Wallet na mobilnom.