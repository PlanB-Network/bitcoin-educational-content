---
name: Trezor Shamiri varukoopia
description: Ühe ja mitme aktsia Mnemonic fraasid Trezoril
---
![cover](assets/cover.webp)



*Pildi krediit: [Trezor.io](https://trezor.io/)*



## Trezori uued varundusvõimalused



Alates 2023. aastast pakub Trezor uut varundusvormingut ***Single-share Backup***, asendades järk-järgult klassikalise BIP39-põhise lähenemisviisi, mis on enamikul portfellidel olemas. Erinevalt traditsioonilistest 12- või 24-sõnalistest Mnemonic fraasidest põhineb see uus formaat ühel 20-sõnalisel fraasil, mis on tuletatud SatoshiLabs'i poolt välja töötatud standardist: **SLIP39**. Eesmärk on parandada varundamise töökindlust ja loetavust, võimaldades samal ajal sujuvat üleminekut hajutatud varundusmudelile.



Seda jaotatud mudelit nimetatakse ***Multi-share Backup***. See põhineb samal põhimõttel, kuid ühe Mnemonic fraasi genereerimise asemel jagatakse see mitmeks fragmendiks, mida nimetatakse ***osakuteks***, millest igaüks on omaette Mnemonic fraas. Portfelli taastamiseks tuleb teatav arv neid *osakuid* (mis on määratletud *künnisega*) taasühendada. Näiteks 3/5 skeemi puhul taastab portfelli mis tahes 3 *osakut* 5-st. Pange tähele, et Trezori hajutatud varundussüsteem erineb Multisig rahakottidest. Bitcoinide kulutamiseks on vaja ainult Hardware Wallet Trezori. Vaja on ainult ühte allkirja. Jaotus kehtib ainult Mnemonic fraasi, st varukoopia tasandil.



![Image](assets/fr/01.webp)



See süsteem lahendab Mnemonic fraasi ühe punkti tõrke probleemi ilma Multisig või passphrase piiripunktide39 haldamisega seotud puudusteta. Taastamisprotsess ei põhine enam ühel, vaid mitmel teabel, kusjuures lisakasu on kaotusetaluvus tänu künnisele.



Kasutajad, kes on loonud portfelli *Single-share Backup* abil, saavad igal ajal üle minna *Multi-share Backup*-le, ilma et nad peaksid oma portfelli migreerima. Vastuvõtuaadressid ja kontod jäävad samaks. *Multi-share* süsteem mõjutab ainult varukoopiaid, ülejäänud portfell jääb muutumatuks.



Multi-share Backup* on saadaval Trezor Model T, Safe 3 ja Safe 5 puhul. Seda funktsiooni ei toeta Trezor Model One.



**Tähtis märkus:** Trezori *Multi-share* süsteem on krüptograafiliselt turvaline, kuna see kasutab levitamiseks *Shamiri salajase jagamise* skeemi. Me soovitame tungivalt mitte rakendada sarnast süsteemi käsitsi, jagades ise klassikalist Mnemonic fraasi. See on halb praktika, mis suurendab oluliselt teie bitcoinide varguse ja kaotamise riski, seega ärge tehke seda. Klassikaline Mnemonic fraas salvestatakse tervikuna.



## Shamiri salajane jagamine SLIP39-is



Trezori *Multi-share* varundamise aluseks olev krüptograafiline mehhanism on *Shamiri salajase jagamise skeem* (SSSS). Selle põhimõte on järgmine: salajane teave (antud juhul portfelli seed) teisendatakse matemaatiliseks polünoomiks. Seejärel arvutatakse selle polünoomi mitu punkti, millest igaühes saab aktsia. Algne saladus rekonstrueeritakse polünoomi interpolatsiooni abil, kogudes minimaalse arvu punkte (lävend).



Ühtegi salajast teavet ei ole võimalik tuletada lävendist väiksema arvu aktsiate põhjal, mis tagab salajase teabe täiusliku teoreetilise turvalisuse. Teisisõnu, isegi piiramatu arvutusvõimsusega ründaja ei saa seed ära arvata, kui lävend ei ole saavutatud.



SLIP39 kasutab seda skeemi seed portfelli jaotamiseks. Iga aktsia on 20-sõnaline lause, mis on koostatud 1024 sõnast koosnevast nimekirjast (erineb BIP39 nimekirjast).



## Multi-share varukoopia seadistamine Trezoril



Portfelli loomisel Trezoris on teil kolm erinevat võimalust:




- Kasutage klassikalist BIP39 Mnemonic fraasi, mis koosneb 12 või 24 sõnast;
- Kasutage ühe ühiku Mnemonic fraasi (SLIP39);
- Mitme Mnemonic fraasi konfigureerimine mitme jagatud funktsiooni (SLIP39) puhul.



Kui valite ühe aktsia SLIP39 Mnemonic fraasi, saate hiljem uuendada mitme aktsia fraasi, ilma et peaksite portfelli tagasi seadma. Teisest küljest, kui alustate klassikalise BIP39 portfelliga (12- või 24-sõnaline fraas), ei saa te seda otse Multi-share'iks muuta. Peate looma uue Multi-share portfelli nullist ja kandma oma vahendid vanast portfellist uude portfelli ühe või mitme Bitcoin tehingu kaudu. See on keerulisem ja kulukam toiming. Kui soovite seda migratsiooni teha, soovitan teil osta uus Hardware Wallet Trezor, et vältida oma seed sisestamist portfelli tarkvarasse.



Selles õpetuses vaatame kõigepealt, kuidas luua mitme aktsia portfelli loomisel, seejärel vaatame järgmises osas, kuidas muuta olemasoleva portfelli puhul ühe aktsia mitme aktsia portfelliks.



Kui vajate abi seadme esmasel seadistamisel, on meil iga Trezori mudeli kohta ka üksikasjalik õpetus:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Uue portfelli kohta



Nüüd olete Trezori algse konfiguratsiooni lõpetanud ja olete valmis portfelli loomiseks. Vajutage Trezor Suite'is nupule "*Loo uus Wallet*".



![Image](assets/fr/02.webp)



Valige valik "*Multi-share Backup*", seejärel klõpsake "*Create Wallet*".



![Image](assets/fr/03.webp)



Nõustuge Trezori kasutustingimustega ja kinnitage portfelli loomine.



![Image](assets/fr/04.webp)



Trezor Suite'is klõpsake nuppu "*Vajuta varundamist*".



![Image](assets/fr/05.webp)



Lugege hoolikalt läbi juhised, kinnitage need, seejärel klõpsake "*Loo Wallet varukoopia*".



![Image](assets/fr/06.webp)



Lisateabe saamiseks selle kohta, kuidas oma Mnemonic fraase õigesti salvestada ja hallata, soovitan tungivalt jälgida seda teist õpetust, eriti kui olete algaja:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Valige Trezori seadistamisel aktsiate koguarv, mida soovite konfigureerida. Kõige levinumad konfiguratsioonid on 2-de-3 ja 3-de-5. Selle näite jaoks loome 2-de-3, seega valin 3 aktsiat. Iga aktsia esindab 20-sõnalist Mnemonic fraasi.



*Safe 5 kasutajate puhul, kuigi ekraanil on kirjas "*Tippige jätkamiseks*", peate kinnitamiseks tegelikult ülespoole pühkima



![Image](assets/fr/07.webp)



Seejärel kinnitage künnis, st aktsiate arv, mis on vajalik, et saada uuesti juurdepääs Wallet-le ja selles sisalduvatele bitcoinidele.



![Image](assets/fr/08.webp)



Trezor loob teie eri aktsiaid (Mnemonic fraasid), kasutades oma juhusliku numbrigeneraatorit. Veenduge, et teid ei jälgita selle toimingu ajal. Kirjutage ekraanil esitatud sõnad oma valitud füüsilisele andmekandjale. Oluline on, et sõnad oleksid nummerdatud ja järjestikku.



Soovitan märkida iga aktsia eraldi andmekandjale ja hallata hoolikalt nende säilitamist, et vältida mitme aktsia kättesaadavust samas kohas. Näiteks minu omataolise 2-ast-3-konfiguratsiooni puhul oleks üks võimalus hoida ühte aktsiat minu kodus, teist usaldusväärse sõbra juures ja viimast panga seifis. Säilituskohtade valik sõltub teie isiklikust turvastrateegiast.



Ekraani ülaosas on näha, millist aktsiat te parajasti vaatate.



loomulikult ei tohi te neid sõnu kunagi internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidist Wallet kasutatakse ainult Testnet peal ja see kustutatakse õpetuse lõpus.**_



![Image](assets/fr/09.webp)



Järgmiste sõnade juurde liikumiseks klõpsake ekraani allosas. Tagasi saate minna, libistades allapoole. Kui olete kõik sõnad üles kirjutanud, hoidke sõrme ekraanil, et liikuda edasi järgmise osa juurde, ja korrake toimingut.



![Image](assets/fr/10.webp)



Iga jagatud salvestuse lõpus palutakse teil valida sõnad oma Mnemonic fraasis, et kinnitada, et olete need õigesti üles kirjutanud.



![Image](assets/fr/11.webp)



Ja see ongi kõik, olete edukalt varundanud oma portfelli, kasutades mitme aktsia võimalust. Nüüd saate jätkata ülejäänud seadistamisjuhistega.



### Olemasoleva ühe aktsia portfelli puhul



Kui teil on juba Trezor Wallet, millel on üheosakute varundamine (SLIP39 Mnemonic fraas, mitte klassikaline BIP39 fraas), ja soovite parandada oma Wallet varundamise kättesaadavust ja turvalisust, saate luua mitmeosakute süsteemi, ilma et peaksite oma bitcoine üle kandma.



Selleks ühendage ja avage oma Hardware Wallet. Trezor Suite'is minge seadistustesse.



![Image](assets/fr/12.webp)



Mine vahekaardile "*Seade*".



![Image](assets/fr/13.webp)



Seejärel klõpsake nupule "*Loo mitme ühiskasutuse varukoopia*".



![Image](assets/fr/14.webp)



Lugege juhiseid, seejärel klõpsake nupule "*Loo mitme jagatud varukoopia*".



![Image](assets/fr/15.webp)



Seejärel peate sisestama oma praeguse Mnemonic fraasi (üksikosa) Trezori ekraanil. Valige sõnade arv (vaikimisi on 20).



![Image](assets/fr/16.webp)



Seejärel kasutage Trezori ekraaniklaviatuuri, et sisestada oma praeguse Mnemonic fraasi iga sõna.



![Image](assets/fr/17.webp)



Seejärel saate valida oma Multi-share Backup'i konfiguratsiooni, järgides eelmises jaotises toodud juhiseid.



![Image](assets/fr/18.webp)



Kui olete loonud oma mitme jagatud varukoopia, peate otsustama, mida teha oma algse ühe jagatud Mnemonic fraasiga. Kuna Bitcoin portfell jääb samaks, võimaldab see üksikfraas sellele alati juurdepääsu. See sõltub teie turvastrateegiast, kuid üldiselt on soovitav see fraas hävitada, et kõrvaldada see ainus veapunkt, mis ongi just Multi-share Backup'i eesmärk. Kui te otsustate selle hävitada, veenduge, et teete seda turvaliselt, sest **see annab endiselt juurdepääsu teie bitcoinidele**.



Palju õnne, te olete nüüd kursis Trezori riistvaraliste rahakottide ühe ja mitme jagamise varukoopiate kasutamisega. Kui soovite oma Wallet turvalisust veelgi edasi arendada, vaadake seda õpetust BIP39 paroolide kohta:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite allpool Green pöidla. Jagage seda artiklit julgelt oma suhtlusvõrgustikes. Tänan teid väga!



## Täiendavad ressursid





- [SLIP-0039: Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup on Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamiri salajane jagamine](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).