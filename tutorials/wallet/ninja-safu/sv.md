---
name: SAFU Ninja
description: Rädda din seed med SAFU Ninja-metoden
---

![cover](assets/cover.webp)


## 1. Inledning



Metoden **Ninja SAFU** är en **DIY-lösning (Do It Yourself)** som låter dig skapa en **hållbar, säker och diskret** säkerhetskopia av din **seed-fras** (en Mnemonic-fras på 12 eller 24 ord som definieras av standarden **BIP-39**). Denna fras är nödvändig för att återställa en Bitcoin Wallet eller någon annan kompatibel Wallet.



I stället för att skriva ner dina ord på papper - en enkel men sårbar metod - graverar du dem på **brickor i rostfritt stål**, monterade på en **Bolt**. Resultatet blir en kompakt, brand-, korrosions-, vatten- och stöttålig backup. Till skillnad från papper, som kan förstöras av lågor, fukt eller tid, garanterar rostfritt stål långsiktigt bevarande, även under extrema förhållanden (upp till 1300°C eller 20 tons tryck).



Ninja SAFU-metoden erbjuder flera fördelar:





- **Konfidentialitet**: Du köper inte en produkt som är identifierad som avsedd för säkerhetskopiering av kryptovaluta. Komponenterna är standard (brickor, bultar, metallåda), tillgängliga i hårdvaruaffärer, vilket minskar risken för inriktning i händelse av en dataläcka från en specialiserad leverantör.





- **Prisvärdhet**: Den här lösningen kostar mellan **15 och 140 EUR**, beroende på vilka verktyg du redan har.





- **Tillförlitlighet**: Metoden har testats sedan 2020 och har testats av säkerhetsexperter som [Jameson Lopp](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/), som har utsatt den för rigorösa stresstester (extrem värme, korrosion, mekaniskt tryck).



Denna steg-för-steg-guide visar dig hur du gör din egen Ninja SAFU-säkerhetskopia för att bättre skydda dina bitcoins mot förlust eller förstörelse. Om du vill lära dig mer om säkerhetskopiering och skydd av en seed-fras kan du läsa bilagorna.




## 2. Hårdvara



För att skapa en Ninja SAFU-säkerhetskopia behöver du följande komponenter, som alla finns i hårdvaruaffärer eller på nätet.



### 2.1 Material som krävs





- **Brickor i rostfritt stål (M8 rekommenderas)**:
- **Material**: Rostfritt stål (t.ex. 304 eller V4A för förbättrad korrosionsbeständighet)
- **Storlek**: M8 (innerdiameter 8 mm, ytterdiameter ~24 mm). M6-brickor är för små och svåra att gravera.
- **Antal**: 12 eller 24 brickor för en standard seed-sats, plus extra brickor (se avsnitt 3.4) och ett tiotal för tester eller fel.





- **Rostfritt stål Bolt och mutter (M8)**:
- **Specifikationer**: Bolt 2,5 till 5 cm lång, beroende på antal och tjocklek på brickorna, diameter 8 mm. En vingmutter underlättar verktygsfri öppning, men en enkel mutter kan också användas.



![image](assets/fr/03.webp)





- **Stanssats för bokstäver och siffror (3 mm eller 6 mm)**:
- **Specifikationer**: 6 mm höga tecken underlättar läsbarheten och kan vara att föredra om en del av bokstäverna är nedbrutna. Välj en robust uppsättning för upprepad användning.



![image](assets/fr/04.webp)





- **Hammare eller slägga**:
    - En slägga är att föredra för tillräcklig och exakt stämplingskraft





- **Ankare eller robust yta**:
 - En tjock Hard-yta (t.ex. 1 kg städ eller 10 cm marksten) för att absorbera stötar.



Om du inte vill investera i en uppsättning stansar kan du också gravera dina brickor med en gravyrpenna. Denna lösning är ofta mer ekonomisk, men kräver större omsorg för att få ett tillfredsställande resultat.



### 2.2 Valfria verktyg





- **Stämpelanordning**: Håller brickan och styr stansen, vilket möjliggör exakt, ren stämpling, bättre orientering och jämnt avstånd mellan bokstäverna



![image](assets/fr/05.webp)





- **Förseglingsanordningar**: Förseglad påse eller förseglingsremsa



![image](assets/fr/06.webp)





- **Hermetiskt tillsluten behållare**: För förvaring av brickblocket



![image](assets/fr/07.webp)


### 2.3 Säkerhet





- **Handskar** och **Säkerhetsglasögon** rekommenderas.
- **Rörtång** att skjuta in stansen i, så att du håller i stansen med rörtången och inte med fingrarna.



### 2.4 Mängder och beräknad kostnad





- **Kvantitet för en 24 ords backup**: 24 brickor (minimum), 1 Bolt, 1 vingmutter, 1 uppsättning stansar, 1 hammare/massett, 1 städ/stöd.





- **Total kostnad**:
 - Brickor och skruvar/muttrar: ~ 15 EUR
 - Punch set: ~ 45 EUR
 - Skyddande fodral: ~ 55 EUR
 - Med alla tillbehör: ~ 140 EUR





- Se appendix för exempel på utrustning.




## 3. Steg-för-steg-instruktioner



1. **Gör dig redo:**




 - Privat plats, inga kameror (inklusive smartphones)
 - Robust, stötdämpande yta
 - Handskar och skyddsglasögon
 - Rengör brickorna från fett och smuts
 - Övning på testbrickor


2. **Bränn Mnemonic ord** :




    - Gravera hela ordet på ena sidan. Begränsa dig inte till de första 4 bokstäverna, om den 4:e skulle skadas.
    - Slå hårt med hammaren och håll i slaget med en rörtång


3. **Antala brickor** :




    - På samma sida graveras ordet positionsnummer, viktigt om brickorna lossnar.


4. **Registrera information** (valfritt och rekommenderat) :




    - Gravera det överflödiga ordet på andra sidan av pucken
    - Gravera en Wallet-identifierare på en extra bricka
    - Gravera in härledningsvägen för det konto du använder på en extra bricka. Du hittar den här informationen i inställningarna för din portföljprogramvara. Till exempel, för en standard Taproot-portfölj kommer standardavledningsvägen att vara: `m / 86' / 0' / 0' /`
    - Skriv in PIN-koden för att låsa upp din Hardware Wallet, eller antiphishing-orden om du använder ett COLDCARD.


5. ** Bränn INTE passphrase :**




 - Om du använder en passphrase, se till att du inte skriver ner den på samma kort som din Mnemonic. passphrase är utformad för att skydda din Wallet i händelse av stöld av Mnemonic. Mer information finns i appendix.


6. **Kontrollera läsbarheten** :




    - Se till att varje ord och siffra är tydlig och läsbar.


7. **Montera brickorna** :




    - Gänga fast brickorna på Bolt i nummerordning.
    - Valfritt: lägg till blankbrickor i ändarna.
    - Skruva på vingmuttern för att säkra batteriet.
    - Dra åt ordentligt för att öka skyddet mot vatten, brand och mekanisk påfrestning.


8. **Test backup** :




    - Försök att återställa din portfölj från din nya säkerhetskopia
- **Försegling av säkerhetskopian** (valfritt och rekommenderat):
 - Genom förseglade remsor eller i förseglade påsar.
 - Om du använder en påse, anteckna dess unika identifikationsnummer, så att du kan kontrollera att det är rätt påse och inte en attrapp som ersätter originalet.




## 4. Förvaring



### 4.1 Välj en lämplig plats



Förvara din säkerhetskopia på en **diskret plats**, utom synhåll och tillgänglig för regelbundna kontroller. Välj **brandsäker och vattentät förvaring**, hemma eller på en plats under din **exklusiva kontroll**.



Undvik platser där du är beroende av en tredje part (bankfack, notarie): du kommer att förlora självständig tillgång till dina medel, vilket strider mot Bitcoin:s principer om suveränitet.



Avslöja aldrig att du använder en metod som Ninja SAFU. Diskretion är en Layer av säkerhet i sig själv.



### 4.2 Redundans



Om så krävs, skapa **flera kopior** och förvara dem på **olika geografiska platser**.


Även om de material som valts för din enhet är vatten- och brandsäkra kommer du inte att kunna komma åt den om den är begravd under m3 bråte i ditt hem, och det kommer att bli mycket svårt, om inte omöjligt, att hämta den.




## 5. Uppföljning och underhåll



Även om din säkerhetskopia är väl förvarad måste den **kontrolleras regelbundet**:





- Inspektera backupen utom synhåll **en eller två gånger om året**.
- I händelse av **försämring av graveringar**, skapa en ny säkerhetskopia, **testa den** och **förstör sedan den gamla kopian** noggrant.
- Om säkerhetskopian finns i en förseglad påse :
 - Kontrollera din inloggning
 - Kontrollera dess integritet
 - Öppna kuvertet regelbundet för att inspektera gravyrernas skick, och om allt är bra, placera säkerhetskopian i en ny ficka




**HÅLL DIG SÄKER!**


![image](assets/fr/08.webp)




## BILAGOR



### A.1 Spara din återställningsfras



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### A.2 Förståelse av passphrase BIP39



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

### A.3 Hur Bitcoin-portföljerna fungerar



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### A.4 Klassificering av Ninja SAFU-metoden



Enligt Jameson Lopp:





- [Rapportera](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/) om Ninja SAFU-metoden





- Jämförelsetabell [komplett](https://jlopp.github.io/metal-Bitcoin-storage-reviews/?ref=blog.lopp.net)





- Delvis tabell :


![image](assets/fr/09.webp)



### A.5 Exempel på hårdvara





- **Brickor** för
 - [Titan](https://pleb.style/fr-fr/products/disques-de-seed-supplementaires-titan-Wallet)
- **Brickor + mutter + skyddsfodral** (för brickor)
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-premium-acier-steel-Wallet-backup?variant=50022696419664)
 - [TerraSteel](https://pleb.style/fr-fr/products/terrasteel-Wallet-plebstyle-acier-backup)
- Stansuppsättning
 - [PlebStyle](https://pleb.style/fr/products/schlagstempelset-a-z-0-9-3mm)
- **Grund för typning**
 - [PlebStyle](https://pleb.style/fr/products/schlagunterlage-10cm-x-10cm-x-1-5cm)
- **Tappningsanordning** (guide)
 - [TerraSteel](https://pleb.style/fr-fr/products/zubehor-einschlag-vorrichtung?_pos=1&_sid=2767fd66f&_ss=r)
- Tätningsanordning
 - [Förseglad påse](https://pleb.style/fr/products/zubehor-5x-sicherheitstasche-tamper-evident)
 - [Tätningslister](https://pleb.style/fr/products/zubehor-5x-siegel-streifen-fur-dein-seed-backup)
- **Komplett** sats
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-diy-kit-premium-seed-backup-steelwallet-plebstyle?pr_prod_strat=e5_desc&pr_rec_id=aa9f36359&pr_rec_pid=8728733155664&pr_ref_pid=8730877788496&pr_seq=uniform)
 - [TerraSteel](https://pleb.style/fr-fr/products/kopie-von-terrasteel-Wallet-starter-kit)



Obs: Länkar till onlinebutiker tillhandahålls endast i informationssyfte.


Det finns inget kommersiellt partnerskap mellan Plan B och ovan nämnda säljare och tillverkare.


Plan B kan inte hållas ansvarigt för defekter, prisvariationer eller problem relaterade till produkternas kvalitet eller leverans. **DYOR**




### A.6 Fotokreditering



https://pleb.style/fr/


https://x.com/lopp/status/1463155802345193475


https://bitcointalk.org/index.php?topic=5389446.0


https://x.com/econoalchemist/status/1329271981712289797


https://www.waivio.com/@themarkymark/skapa-din-egen-metall-seed-nyckel-backup


https://github.com/minibolt-guide/minibolt/blob/main/bonus/Bitcoin/safu-ninja.md