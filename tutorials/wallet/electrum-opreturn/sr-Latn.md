---
name: Electrum OP_RETURN
description: Registrujte poruku na Blockchain Bitcoin sa Electrum
---

![cover](assets/cover.webp)




Ovaj vodič korak po korak pokazuje vam kako da napišete poruku na Blockchain Bitcoin koristeći Wallet Electrum. Ova operacija koristi OP_RETURN instrukciju za umetanje teksta u transakciju, javno vidljivu na Blockchain. Pratite ove jednostavne korake za uspešnu registraciju.



---
## Preduslovi





- Računar (Windows, macOS ili Linux).
- Internet konekcija.
- Nekoliko satoshija (Sats) ili bitkoina (BTC) u vašem Wallet da pokrijete iznos transakcije i naknade.
- Konverter teksta u heks (npr. online sajt) ili posvećen alat kao što je [ovaj OP_RETURN generator skripti](https://resources.davidcoen.it/opreturnelectrum/).



---

## Korak 1: Preuzmite i instalirajte Electrum



![image](assets/fr/01.webp)



1. Posetite zvaničnu Electrum veb stranicu: [electrum.org](https://electrum.org/).


2. Preuzmite verziju koja odgovara vašem operativnom sistemu (Windows, macOS, Linux).


3. Instalirajte Electrum prema uputstvima instalatera.


4. Proverite integritet preuzete datoteke (opciono, ali preporučljivo iz bezbednosnih razloga) poređenjem potpisa datoteke ili Hash.



→ Više detalja o Electrum vodiču :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Korak 2: Kreiraj ili uvezi Wallet



1. Pokrenite Electrum.


2. Izaberite Kreiraj novi Wallet ili Vrati postojeći Wallet ako već imate seed frazu (fraza za oporavak).


3. Pratite uputstva za konfigurisanje vašeg Wallet :




 - Za novi Wallet, zabeležite svoju seed rečenicu i čuvajte je na sigurnom mestu (papir, sef, itd.).
 - Za postojeći Wallet, unesite svoju seed frazu da biste ga vratili.


4. Postavite lozinku da osigurate vaš Wallet.



→ Više detalja o Electrum vodiču :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Korak 3: Proveri dostupna sredstva



Uverite se da vaš Wallet sadrži dovoljno bitkoina (BTC) ili satoshija (Sats) da:




- Iznos transakcije (na primer, 0.00001 BTC ili 1000 Sats).
- Naknade za transakcije, koje variraju u zavisnosti od veličine mreže (uglavnom nekoliko hiljada Sats).



Konsultujte stanje u Electrumu da proverite svoja sredstva.



![image](assets/fr/02.webp)



Ako je potrebno, prenesite BTC ili Sats da napunite svoj Wallet. Da biste to uradili, idite na karticu 'Receive' i kliknite na 'Create Request' :



![image](assets/fr/03.webp)



Ovo će prikazati prijem Address:



![image](assets/fr/04.webp)



→ Više detalja o Electrum vodiču :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Korak 4: Pripremite poruku za urezivanje



Odaberite poruku koju želite uneti (npr. `Hvala Satoshi`). Napomena: Poruke OP_RETURN su ograničene na 80 bajtova, tj. oko 80 ASCII karaktera.



*Odvojite trenutak za razmišljanje: ono što napišete na Blockchain Bitcoin je večno i dostupno svima, zato :*




- ostavite lep izraz naše humanosti,
- izbegavajte unos sadržaja zbog kojeg biste mogli zažaliti



*Blockchain svemir i tvoji bitkoini su dragoceni, koristi ih mudro i sa namerom*



Pretvori svoju poruku u heksadecimalni oblik:




- Možete koristiti [online alat](https://www.rapidtables.com/convert/number/ascii-to-hex.html), ali budite oprezni da tamo ne obrađujete osetljive podatke (iako, u principu, informacije namenjene za objavljivanje na Blockchain Bitcoin putem OP_RETURN ne predstavljaju probleme poverljivosti);
- Za veću poverljivost, izvršite konverziju lokalno koristeći mali Python skript:



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Primer: `Thanks Satoshi` u ASCII daje `5468616e6b73205361746f736869` u heksadecimalnom formatu.



Pripremite skriptu transakcije. Evo primera očekivanog formata:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



koji se sastoji od :





- **Destination Address**: A valid Bitcoin Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. This can be your own Address, if you wish to return the transferred funds to yourself;
- **Iznos prenosa**: iznos transakcije, ovde `0.00001` BTC. **Molimo obratite pažnju**: pošto je jedinica koja se koristi u Electrum-u BTC, iznos naveden u skripti transakcije mora biti izražen u BTC, a ne u Sats;
- Script **OP_RETURN**: Poruka konvertovana u heksadecimalni oblik prethodi skripti (`OP_RETURN <poruka>), 0`. Ovde, `5468616e6b73205361746f736869` za poruku u heksadecimalnom obliku.



⚠️ **Pažnja**: Veoma je važno navesti `0` nakon OP_RETURN, jer ovaj opcode označava skriptu kao nevažeću, čineći izlaz trajno nepotrošivim. Mrežni čvorovi će obrisati ovaj izlaz iz svog UTXO seta. Ako unesete vrednost drugačiju od `0`, ona će biti nepovratno izgubljena: vaši bitkoini će se smatrati spaljenim. Stoga uvek treba uneti `0` sa OP_RETURN kako biste zabeležili željene podatke, ali bez povezivanja sredstava sa tim, koja bi bila izgubljena.



Savet: Koristite alat [OP_RETURN Generator](https://resources.davidcoen.it/opreturnelectrum/) da automatski generate skriptu. Čak i ako ovaj alat predlaže unos iznosa u BTC, zadržite jedinicu podešenu u Electrum.



![image](assets/fr/05.webp)



Da biste promenili jedinicu koju koristi Electrum, u traci menija pronađite "Preferences", zatim u kartici "Units" izaberite BTC / mBTC / bits ili Sats :



![image](assets/fr/06.webp)




---

## Korak 5: Pošaljite transakciju



U Electrumu, idite na karticu Pošalji.



![image](assets/fr/07.webp)



U polje "Plati" nalepite pripremljeni skript (na primer, onaj iznad).



![image](assets/fr/08.webp)



Polje "Pay to" treba da bude prikazano u Green, a iznos transakcije treba da se pojavi na liniji ispod.



Proverite iznos i njegovu jedinicu u polju za iznos.



Kliknite na "Plati..." i prilagodite naknade za transakciju prema iznosu koji ste spremni platiti i brzini kojom želite da vaša transakcija bude obrađena od strane Miner i integrisana u blok.



![image](assets/fr/09.webp)



Kliknite OK i potvrdite transakciju vašom lozinkom. Pojaviće se prozor za potvrdu.




---

## Korak 6: Verifikujte registraciju



Jednom kada transakcija bude potvrđena (ovo može potrajati nekoliko minuta), idite na karticu "Istorija".



![image](assets/fr/10.webp)



Desni klik na transakciju i izaberi "View on Explorer" da vidiš detalje.



Alternativno, kopirajte odredište Address (na primer, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) i pogledajte ga na Blockchain exploreru kao što su [Mempool.space](https://Mempool.space/) ili [blockstream.info](https://blockstream.info/).



Potražite polje OP_RETURN u detaljima transakcije da biste videli svoju poruku.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Saveti i najbolje prakse





- Testirajte sa malim iznosom: Počnite sa malom transakcijom (npr. Sats 1000) kako biste izbegli skupe greške.
- Uverite se da je izlaz koji sadrži OP_RETURN jednak nuli, inače će vaši bitkoini biti trajno izgubljeni.
- Proverite jedinicu: Uverite se da uneseni iznos odgovara jedinici prikazanoj u Electrum-u (BTC, mBTC ili Sats).
- Naknada za transakciju: Ako je mreža zagušena, povećajte naknadu za bržu potvrdu.
- Kratka poruka: OP_RETURN unosi su ograničeni na 80 bajtova. Planirajte svoju poruku u skladu s tim.



---

## Korisni resursi





- Preuzmite Electrum: [electrum.org](https://electrum.org/)
- OP_RETURN skript generator: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Istraživači: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)