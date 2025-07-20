---
term: PRETPOSTAVI VAŽEĆE
---

Konfiguracioni parametar u većinskom klijentu Bitcoin Core koji omogućava čvoru koji je upravo inicijalizovan (ali još nije izvršio IBD) da preskoči verifikaciju potpisa za sve transakcije uključene u blokove pre određenog datog bloka. Ovaj poznati blok je definisan otiskom njegovog zaglavlja, tj. njegovim Hash. Izabrani blok se obnavlja sa svakom novom verzijom Bitcoin Core. Po svojoj inicijalizaciji, ako je čvor aktivirao ovaj parametar, proveriće lanac zaglavlja blokova kako bi pronašao granu sa najviše akumuliranog rada. Ako čvor detektuje Hash koji je obezbedio Core u grani koju je izabrao, izostaviće verifikaciju potpisa za prethodne blokove. U suprotnom, čvor će nastaviti sa tradicionalnom sinhronizacijom (IBD) kako bi sve proverio samostalno.


Cilj funkcije Pretpostavi Validno je da ubrza proces početne sinhronizacije čvora bez ugrožavanja bezbednosti, pod pretpostavkom da je većina mreže već potvrdila ove transakcije u prošlosti. Jedini pravi kompromis za čvor je da u slučaju prethodne krađe bitkoina, neće biti obavešten. Međutim, i dalje može osigurati tačnost iznosa izdatih bitkoina. Čvorovi nastavljaju verifikaciju potpisa za transakcije koje slede nakon bloka Pretpostavi Validno. Ovaj pristup se zasniva na pretpostavci da, ako je transakcija dovoljno dugo prihvaćena od strane mreže bez spora, malo je verovatno da je prevarantska.