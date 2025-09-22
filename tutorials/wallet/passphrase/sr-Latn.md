---
name: BIP-39 Passphrase
description: Razumevanje kako passphrase funkcioniše
---
![cover](assets/cover.webp)


## Šta je BIP39 passphrase?


HD novčanici se obično generišu iz Mnemonic fraze koja se sastoji od 12 ili 24 reči. Ova fraza je veoma važna jer omogućava obnavljanje svih ključeva Wallet u slučaju da se njegov fizički medijum (kao što je Hardware Wallet, na primer) izgubi. Međutim, ona predstavlja jednu tačku kvara jer, ako je kompromitovana, napadač bi mogao da ukrade sve bitkoine.


![PASSPHRASE BIP39](assets/notext/01.webp)


Ovde dolazi passphrase. To je opcionalna lozinka koju možete slobodno izabrati, a koja se dodaje Mnemonic frazi u procesu derivacije ključa kako bi se poboljšala sigurnost Wallet.


![PASSPHRASE BIP39](assets/notext/02.webp)


Pazite da ne pomešate passphrase sa PIN kodom vašeg Hardware Wallet ili lozinkom koja se koristi za otključavanje pristupa vašem Wallet na računaru. Za razliku od svih ovih Elements, passphrase igra ulogu u derivaciji ključeva vašeg Wallet. **To znači da bez njega nikada nećete moći da povratite svoje bitkoine.**

passphrase radi u tandemu sa frazom Mnemonic, menjajući seed iz kojeg se generišu ključevi. Dakle, čak i ako neko dobije vašu frazu od 12 ili 24 reči, bez passphrase, ne može pristupiti vašim sredstvima. **Korišćenje passphrase u suštini stvara novi Wallet sa različitim ključevima. Modifikovanje (čak i minimalno) passphrase će generate drugačiji Wallet.**

## Zašto bi trebalo da koristite passphrase?

passphrase je proizvoljan i može biti bilo koja kombinacija karaktera koju korisnik odabere. Korišćenje passphrase stoga nudi nekoliko prednosti. Prvo, smanjuje sve rizike povezane sa kompromitovanjem Mnemonic fraze zahtevajući drugi faktor za pristup sredstvima (provala, pristup vašem domu, itd.).

Dalje, može se strateški koristiti za kreiranje mamca Wallet, kako bi se nosilo sa fizičkim ograničenjima za krađu vaših sredstava kao što je ozloglašeni "*napad ključem od $5*". U ovom scenariju, ideja je imati Wallet bez passphrase koji sadrži samo malu količinu bitkoina, dovoljno da zadovolji potencijalnog napadača, dok je pravi Wallet skriven. Ovaj poslednji koristi istu Mnemonic frazu, ali je osiguran dodatnim passphrase.

Konačno, korišćenje passphrase je zanimljivo kada neko želi da kontroliše nasumičnost generacije seed modela HD Wallet.

## Kako odabrati dobar passphrase?

Prema [studiji koju je sproveo Trezor 2019. godine](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af), napadač koji ima pristup vašem seed-u i koristi vrhunski GPU iznajmljen preko AWS-a (NVIDIA Tesla V100) mogao bi testirati skoro 620 miliona lozinki za 1 dolar. Kao okvirna procena, sa mogućnostima iz 2019. godine, fraza od 12 nasumičnih malih slova koštala bi u proseku **77 miliona dolara** da se probije.

Ipak, ne preporučujem da se ograničite na 12 karaktera. Umesto toga, ciljajte na trenutne standarde za jake lozinke: u 2025. godini, koristite najmanje 13 nasumičnih karaktera uključujući brojeve, mala i velika slova i simbole; ili 14 karaktera ako koristite samo mala i velika slova. Naravno, savetujem da idete i dalje, na primer da koristite lozinku od 20 karaktera sa simbolima, kako biste predvideli buduće promene i uzeli u obzir ljudske rizike koji nisu obuhvaćeni u ovim studijama.

Da bi passphrase bio efikasan, mora biti dovoljno dug i nasumičan. Baš kao i sa jakom lozinkom, preporučujem odabir passphrase koji je što duži i nasumičniji, sa raznovrsnim slovima, brojevima i simbolima kako bi bilo koji napad grubom silom bio nemoguć.

Takođe je važno pravilno sačuvati ovaj passphrase, na isti način kao i frazu Mnemonic. **Gubitak znači gubitak pristupa vašim bitcoinima**. Snažno savetujem protiv memorisanja isključivo u glavi, jer to nerazumno povećava rizik od gubitka. Idealno je zapisati ga na fizički medijum (papir ili metal) odvojen od fraze Mnemonic. Ova rezervna kopija mora očigledno biti uskladištena na drugom mestu od onog gde se čuva vaša fraza Mnemonic kako bi se sprečilo da obe budu istovremeno ugrožene.

## Tutorijali

Da biste postavili passphrase na uređaju Ledger (Stax, Flex ili Nano), možete pogledati ovaj vodič:

https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Na COLDCARD-u:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

Na Jade Plus:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Na pasošu (serija-2):

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Na Trezor uređaju (Safe 3, Safe 5 ili Model One):

https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42