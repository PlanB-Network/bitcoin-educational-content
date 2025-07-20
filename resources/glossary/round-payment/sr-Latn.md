---
term: PLAĆANJE U KRUGU
---

Interna heuristika za analizu lanca na Bitcoin koja omogućava hipotezu o prirodi izlaza transakcije na osnovu zaokruženih iznosa. Generalno, kada se suočimo sa jednostavnim obrascem plaćanja (1 ulaz i 2 izlaza), ako jedan od izlaza troši zaokružen iznos, onda on predstavlja plaćanje. Eliminacijom, ako jedan izlaz predstavlja plaćanje, drugi predstavlja kusur. Stoga se može interpretirati da je verovatno da korisnik koji unosi transakciju i dalje poseduje izlaz identifikovan kao kusur.


Treba napomenuti da ova heuristika nije uvek primenljiva, jer se većina plaćanja i dalje vrši u fiat valutama. Zaista, kada trgovac u Francuskoj prihvati Bitcoin, obično ne prikazuju stabilne cene u Sats. Radije bi se odlučili za konverziju između cene u evrima i iznosa u bitkoinima koji treba platiti putem njihovog POS-a (kao što je BTCPay Server, na primer). Stoga, ne bi trebalo da postoji okrugli broj u izlazu transakcije. Ipak, analitičar bi mogao pokušati da izvrši ovu konverziju uzimajući u obzir Exchange kurs koji je bio na snazi kada je transakcija emitovana na mreži. Ako jednog dana Bitcoin postane preferirana obračunska jedinica u našim razmenama, ova heuristika bi mogla postati još korisnija za analize.


![](../../dictionnaire/assets/11.webp)