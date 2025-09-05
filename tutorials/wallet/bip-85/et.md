---
name: BIP-85
description: Kuidas saan ma kasutada BIP-85, et generate mitu seemnefraasi peast seed?
---
![cover](assets/cover.webp)



## 1. BIP-85 mõistmine



### 1.1 Mis on BIP-85?



BIP-85 on täiustatud funktsioon, mis võimaldab luua ühest **seed põhifraasist** mitu **seed sekundaarfraasi**.



Iga seed teisese lause abil saab luua täiesti iseseisva Bitcoin portfelli. Neid portfelle saab kasutada mitmesugustel eesmärkidel: Hot Wallet mobiilis, portfell sugulasele, eraldi säästuportfell jne.



Kõik seed alamlaused on **matemaatiliselt tuletatud**, kuid alamlausest on **mõeldav tagasi seed põhifraasini**. See tagab iga portfelli täieliku eraldatuse.



Niikaua kui teil on juurdepääs oma seed põhifraasile (ja sellega seotud passphrase-le, kui te kasutate seda), saate taastada mis tahes seed sekundaarse fraasi **identaalselt**, ilma et peaksite seda eraldi salvestama.



### 1.2 Miks kasutada BIP-85?



BIP-85 on kasulik, kui soovite :





- Luua mitu sõltumatut Bitcoin portfelli ilma mitme varukoopiata
- Halda oma raha vastavalt erinevatele kasutusviisidele (säästud, kulud, pere, projektid)
- Sugulastele tagatiste tagamine ("onu Jim" funktsioon)
- Portfelli kustutamine ilma juurdepääsu kaotamata oma rahalistele vahenditele
- Lihtsustage oma turvalisust: ainult üks seed võtmeväljend kaitsmiseks



### 1.3 Eelised BIP-32 ees



BIP-32 abil saab ühe seed lause abil luua generate täieliku Bitcoin kontode ja aadresside hierarhia, kasutades tuletamisradasid (näiteks: `m/44'/0'/0'/0'/0/0`). Iga tee võib esindada eraldi kontot, kuid **kõik millised neist on seotud sama seed lausega**. Seega, kui see seed lause on ohustatud, **saavad **kõik millised tuletatud kontod kättesaadavaks**.



BIP-85 abil saab seed põhilauset kasutada generate mitme täiesti sõltumatu seed kõrvallause jaoks: **Kui üks neist sekundaarsetest seemnetest on ohustatud, ei saa ründaja kunagi tagasi seed põhisalvestuse juurde ega pääse ligi teistele portfellidele**.


See võimaldab riskide killustamist:





- Te võite kasutada Hot Wallet või ajutise kasutamise jaoks sekundaarset seed, aktsepteerides suuremat kokkupuudet.
- Isegi kui see Hot Wallet satub ohtu, jäävad teie muud vahendid, mida kaitsevad teised sekundaarsed seemned või mida hoitakse võrguühenduseta, **sellu**.



Teisest küljest on nii BIP-32 kui ka BIP-85 puhul, kui peamine seed on ohustatud, **kõik millised fondid on haavatavad**. Seetõttu on väga oluline kaitsta seda kõige kõrgema turvalisuse tasemega.



![image](assets/fr/02.webp)


## 2. BIP-85 praktilised kasutusjuhud



BIP-85 võimaldab teil luua ühest seed põhifraasist mitu Bitcoin portfelli, millest igaühel on oma seed sekundaarne fraas. Siin on viis praktilist kasutusjuhtumit Bitcoin vahendite organiseerimiseks ja kindlustamiseks. Iga juhtum selgitab, miks BIP-85 kasutamine on praktilisem kui mitme konto haldamine ühe seed fraasiga BIP-32 abil.



### 2.1 Vähem turvalise portfelli riski piiramine





- Stsenaarium**: Kasutate igapäevasteks tehinguteks Hot Wallet (paigaldatud internetti ühendatud seadmesse).
- Lahendus BIP-85**: Looge seed sekundaarne fraas, mis on pühendatud sellele portfellile.
- Eelis võrreldes BIP-32ga**: Te ei pea seed esmast fraasi oma telefoni importima, mis vähendab häkkimise ohtu. Ainult seed sekundaarne fraas on ohustatud, mis kaitseb teie teisi rahakotte. BIP-32 puhul peate kasutama seed põhifraasi ja ümbersõiduteed, mis paljastab kõik teie rahalised vahendid.



### 2.2 Loo portfoolio pereliikme jaoks





- Stsenaarium**: Bitcoin Wallet seadistate kellelegi lähedasele (nt teie emale), olles samas võimeline seda tagasi saama, kui ta selle kaotab.
- Lahendus BIP-85**: Looge spetsiaalne seed sekundaarne lause ja jagage ainult seda.
- Eelis võrreldes BIP-32ga**: BIP-32 puhul on konto loomiseks lähedasele vaja kas jagada oma peamist seed fraasi, riskides sellega kõigi oma rahaliste vahenditega ja raskendades oma lähedase jaoks haldamist (hargnemisradade haldamine), või luua uus seed fraas, mida salvestada lisaks oma peamisele seed fraasile.



### 2.3 Eraldiseisvate portfellide haldamise hõlbustamine





- Stsenaarium**: Eraldate oma bitcoinid erinevatel eesmärkidel (nt pikaajalised säästud, mitte-KYC vahendid).
- Lahendus BIP-85**: Te loote seed teiseseid fraase, mis on pühendatud igale eesmärgile.
- Eelis võrreldes BIP-32ga**: BIP-32 puhul kasutavad kõik kontod sama seed fraasi, mis muudab halduse kolmandate osapoolte portfellides keerulisemaks, kuna see nõuab tuletamisradade haldamist, näiteks `m/44'/0'/0'/0'`. Lisaks ei ole võimalik määrata iga seadme kohta eraldi kontot (nt "säästud Coldcardil", "igapäevane mobiilil", "puhkus Trezoril"). BIP-85 määrab iga eesmärgi kohta unikaalse seed sekundaarse fraasi, mida on lihtne tuvastada ja importida igas seadmes eraldi.



### 2.4 Ajutise Wallet kasutamine tehingute jaoks





- Stsenaarium**: Näiteks: teil on vaja ajutist portfelli ühekordse tehingu jaoks või konfidentsiaalsuse säilitamiseks (nt: vahendite segamine, suhtlemine Exchange KYC-ga jne).
- Lahendus BIP-85**: Te loote seed teisese lause, kasutate seda tehingu jaoks, seejärel hävitate selle vajaduse korral, teades, et seda saab taastada.
- Eelis võrreldes BIP-32ga**: BIP-32 puhul sõltub ajutine konto seed põhilausest, mis paljastab kõik teie rahalised vahendid, kui need satuvad ohtu.





## 3. Enne alustamist





- Riistvara** (valikuline)
 - Coldcard Mk4 või Q1
 - MicroSD-kaart





- Põhiteadmised
 - Mnemonic fraaside mõistmine (BIP-39): 12-24 sõna sisaldav loetelu portfelli salvestamiseks.
 - Tea, mis on Bitcoin Wallet: tarkvara või seade oma bitcoinide haldamiseks ja kuidas seda Mnemonic fraasiga taastada.
 - Rohkem ressursse lisades.





- Ühilduv** tarkvara
 - Sparrow wallet (arvuti, ainult vaatlemiseks või edasijõudnute haldamiseks)
 - Nunchuck (mobiilne, mitme allkirja jaoks)
 - BlueWallet (mobiilne)
 - ...





- 3.4 Coldcard** konfiguratsioon
 - Esialgne 24 sõnast koosnev seed lause Coldcard'ile.
 - Vabatahtlik: Lisage passphrase, et tagada juurdepääs BIP-85 harudele.
 - Aktiveerige kasulikud valikud: (ekspordiks), USB-ühenduse keelamine aku korral (turvalisus).




## 4. Samm-sammult õpetus



Järgige järgmisi samme, et luua, kasutada ja saada oma Coldcardil teisese Mnemonic koos BIP-85-ga.



### 4.1 generate a seed sekundaarne lause



Te loote seed teisese fraasi oma seed põhifraasist.


Lülitage oma Coldcard sisse, sisestage PIN-kood.





- 1. Kui olete passphrase rakendanud oma peamise seed:**
 - Avakuvalt avaneb valik "passphrase".
    - Valige "Lisa sõna" ja sisestage oma parool.
    - Vajutage nuppu "Rakenda".
    - Kontrollige Wallet identiteeti: Wallet sõrmejälje märkimiseks valige `Advanced > View Identity` (Täiustatud > Vaata identiteeti).





- 2. Mine menüüsse BIP-85**
 - Avakuval valige "Täiustatud > tuletada seed B85"
 - Lugege hoiatust ja kinnitage.



ColdCard teavitab teid, et genereeritud seemned on matemaatiliselt tuletatud teie peamisest seed-st, kuid krüptograafiliselt täiesti sõltumatud.


![image](assets/fr/03.webp)





- 3. Valige formaat


Valige seed lauseformaat: 12, 18 või 24 sõna. Kontrollige sõnade arvu, mida aktsepteerib Wallet, millesse soovite oma seed fraasi importida.


![image](assets/fr/04.webp)





- 4. Valige indeks
 - Sisestage indeks vahemikus 0 kuni 9999.
 - See indeks on oluline sekundaarse seed hilisemaks taastamiseks. Hoidke seda hoolikalt sildiga nagu: "Indeks 1 = Wallet mobiilne", "Indeks 2 = pereprojekt", "Indeks 4 = katsesegu", ...
 - Kui kaotate selle, ei kaota te juurdepääsu oma rahalistele vahenditele, kuid peate nende leidmiseks katsetama kombinatsioone 0 kuni 9999.


![image](assets/fr/05.webp)





- 5. Märkus või eksport seed sekundaarne lause**


ColdCard kuvab nüüd uut seed sekundaarset lauset. Saate :




 - **märkus käsitsi**.
 - Press :
     - 1", et salvestada see SD-kaardile
     - "2", et **siseneda ColdCard'i režiimi "kasutada seda seed"** (kasulik tehingu eksportimiseks või allkirjastamiseks)
     - 3", et kuvada **QR-kood** (mida saab skaneerida mobiilirakendusega, näiteks BlueWallet või Nunchuck)
     - 4", et saata see **NFC** kaudu



💡 Siinkohal on teil sõltumatu seed fraas, mida saab kasutada mis tahes Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Sekundaarse seed kasutamine



Seda tuletatud seed saate nüüd kasutada uue portfelli loomiseks dokumendis :




- mobiilirakendus
- teine Hardware Wallet
- gW-69 portfell



### 4.3 Kaotatud seed sekundaarse fraasi taastamine



Teise seed väljavõtmiseks igal ajal korrake protsessi:


1. Taaskäivitage oma ColdCard


2. Sisestage oma PIN-kood


3. Sisestage oma passphrase, kui see on määratletud


4. Mine "Täiustatud > tuletada seed B85"


5. Valige vorming (12/18/24 sõna)


6. Sisestage sama indeks (nt `1`)


7. Saate täpselt sama teisejärgulise seed




## 5. Piirid, riskid ja parimad tavad



### 5.1 Sõltuvus seed põhilausest + passphrase



BIP85 kasutamine tugineb täielikult 24-sõnalisele seed põhilausele, samuti passphrase-le, kui te olete seda rakendanud.




- Nendest kahest Elements-st saab taastada kõik seed sekundaarsed fraasid.
- Ilma ühega neist 2 Elements kaotate juurdepääsu kõikidele tuletisportfellidele.



### 5.2 Riskid mitme allkirja konfiguratsioonis



Soovitame tungivalt vältida multi-sig konfiguratsioonis samast esmasest seed fraasist genereeritud teiseseid seed fraase: kui seade või esmane seed fraas on ohustatud, võib ründaja kõik multi-sig võtmed uuesti genereerida.



### 5.3 Tarkvara ühilduvus



Kõik rakendused ei toeta otseselt BIP85 tuletamist. BIP85 abil genereeritud seemned on siiski standardsed BIP39 seemned (12, 18 või 24 sõna) ja neid saab seega kasutada mis tahes BIP39-ga ühilduvas portfellis.



### 5.4 BIP85 kontoregister



Soovitatav on pidada ajakohast isiklikku registrit seed sekundaarsete fraaside kohta.




- See võimaldab teil kiiresti välja selgitada, milline BIP85 indeks millisele portfellile vastab, ilma et peaksite seed sekundaarseid fraase pidama.
- See register peaks jääma minimalistlikuks, ilma Bitcoin selgesõnalise mainimiseta, ja seda tuleks hoida põhilisest seed-st eraldi. Ärge unustage seda oma pärimisplaanis mainida.



Register võib sisaldada :




- kasutatud bIP85 indeks (number 0 kuni 9999)
- kasutus- või viitenimi (nt Hot Wallet, isiklikud säästud, Wallet emalt)
- vajaduse korral Wallet sõrmejälg ColdCard'i kontrollimiseks



### 5.5 Varukoopia



Varukoopiad peavad sisaldama :




- peamine seed
- gW-76 (kui kasutatakse)



Mitte kunagi ei tohi neid koos ladustada:




- peamised seed ja passphrase
- peamine seed ja BIP85 kontoregister



Rohkem ressursse lisades.




## LIITED



## A.1 Sõnastik





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed fraas](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Salvesta oma taastamislause



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 passphrase BIP39 mõistmine



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Kuidas Bitcoin portfellid töötavad



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f