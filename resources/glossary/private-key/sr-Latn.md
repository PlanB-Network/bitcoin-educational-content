---
term: PRIVATNI KLJUČ
---

Privatni ključ je osnovni element asimetrične kriptografije. To je broj (256 bita u kontekstu Bitcoin) koji predstavlja kriptografski tajni podatak. Ovaj ključ se koristi za digitalno potpisivanje transakcija i dokazivanje Ownership javnog ključa Bitcoin (i posredno, primanje Address) ispunjavanjem `scriptPubKey`. Dakle, privatni ključevi omogućavaju trošenje bitkoina otključavanjem UTXO-a povezanih sa odgovarajućim javnim ključem. Privatni ključevi moraju biti strogo poverljivi, jer bi njihovo otkrivanje moglo omogućiti zlonamernim trećim stranama da preuzmu kontrolu nad povezanim sredstvima.


U sistemu Bitcoin, privatni ključ je povezan sa javnim ključem putem algoritma digitalnog potpisa koristeći eliptičke krive (ECDSA ili Schnorr). Javni ključ se izvodi iz privatnog ključa, ali obrnuti proces je praktično nemoguće postići zbog računarske složenosti inherentne u rešavanju osnovnog matematičkog problema (problema diskretnog logaritma). Javni ključ se generalno koristi za generate Bitcoin Address, koji se koristi za zaključavanje bitkoina koristeći skriptu. U kriptografiji, privatni ključevi su često nasumični ili pseudo-nasumični brojevi. U specifičnom kontekstu Bitcoin determinističkih i hijerarhijskih novčanika, privatni ključevi se deterministički izvode iz seed. Privatni ključevi se često mešaju sa seed ili sa frazom za oporavak (Mnemonic). Međutim, ovi Elements su različiti.


> ► *Na engleskom, privatni ključ se zove "private key." Ovaj termin se ponekad skraćuje kao "privkey," ili "PV."*