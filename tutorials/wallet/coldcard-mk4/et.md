---
name: COLDCARD Mk4
description: Juhend COLDCARD Mk4 seadistamiseks ja kasutamiseks koos Sparrow Wallet-ga
---

![cover-mk4](assets/cover.webp)


**Hardware wallet** on füüsilised seadmed, mis on loodud ainult Bitcoini privaatvõtme turvaliseks säilitamiseks. Need salvestavad privaatvõtmeid võrguühenduseta, mis tähendab, et häkkerid ei pääse neile interneti kaudu ligi. Kui **tarkvara walletd** kasutatakse peamiselt igapäevasteks tehinguteks, siis **hardvara walletd** kasutatakse sageli suuremate bitcoinide turvaliseks ja pikaajaliseks säilitamiseks. Bitcoin tehingu tegemisel, kasutades **hardvara wallets**, saab wallet allkirjastada tehingud seadme sees, nii et privaatne võti ei ole kunagi avatud internetiühendusega keskkondadele.


Selles õpetuses uurime ühte kõige populaarsemat Coinkite toodetud wallet riistvara, Coldcard Mk4. Vaatame, kuidas seadistada ja kasutada seda riistvaralist wallet-i Bitcoin tehingute tegemiseks.


## Coldcard Mk4 ülevaade


Coldcard Mk4 on ainult Bitcoin riistvara wallet, mida toodab Coinkite. See seade on varustatud ekraani, numbrilise klaviatuuri ja libiseva kaitsekattega. Lisaks pakub seade mitmeid ühendus- ja suhtlemisvõimalusi, sealhulgas USB-C, õhuga ühendatud töö MicroSD-kaardi abil, NFC ja virtuaalse ketta režiim. Mk4 sisaldab ka täiustatud turvaelemente, nagu BIP39 passphrase ja trikitrikkide PIN-koodid, mis annavad kasutajatele suurema kontrolli ja kaitse oma Bitcoin üle.


## Esialgne seadistamine: PIN-kood ja andmepüügivastased sõnad


Alustamiseks saab Coldcard Mk4 osta otse [Coinkite'i veebisaidilt](https://store.coinkite.com/store). Ostjad saavad valida ka fiat-valuutaga või Bitcoin-ga maksmise. Lisaks on vaja ka MicroSD-kaarti (4 GB on piisav) ja vooluallikat, mida saab ühendada USB-C kaabli kaudu (Coldcard Mk4-l on ainult USB-C toitepordi sisend). Pange tähele, et kuna Mk4-l ei ole sisseehitatud akut, peab see olema kasutamise ajal kogu aeg vooluallikaga ühendatud.


Saate oma Mk4 seadme võltsimiskindlas kotis. Palun veenduge, et kott ei ole kahjustatud. Kui märkate midagi, mis võib olla probleemne, näiteks kahjustusi või rebenemist kotil, võite sellest teavitada Coinkite'i, saates e-kirja aadressil support@coinkite.com. Lisaks leiate võltsimisohutu koti peal 12-kohalise numbri, mida me nimetame Mk4 koti numbriks. Seda kotinumbrit kasutatakse hiljem selleks, et kontrollida, et seadet ei ole saatmise ajal võltsitud ja et see pärineb otse Coinkite'ilt. Koti number salvestatakse turvaliselt Coldkaardi secure element-sse, kasutades OTP (ühekordselt programmeeritav) välkmälu, mis tähendab, et seda ei saa pärast programmeerimist muuta. Kui lülitate seadme esimest korda sisse, peab ekraanil kuvatav number vastama kotil olevale numbrile. See tagab, et teie saadud Mk4 on tehasest saadud originaalseade, mida ei ole asendatud ega muudetud. Kuigi see kontroll kinnitab ainult seadme terviklikkust esimese sisselülitamise ajal, kaitseb secure element jätkuvalt teie isiklikke võtmeid, PIN-koodi ja passphrase, mistõttu on äärmiselt raske, et teie Bitcoin saaks manipuleerida. Lisaks sellele aitavad head tavad, näiteks walletga seotud andmete nõuetekohane turvamine, kaasa Coldkaardi enda üldisele turvalisusele. Täiendavat teavet leiate sellest [artiklist] (https://blog.coinkite.com/understanding-mk4-security-model/), kus on üksikasjalikult kirjeldatud Coldkaardi turvamudelit.


Klaviatuur koosneb 10 numbrilisest nupust, nupust OK (✓) ja nupust tühistamine (✕). Mõnda numbrinuppu saab kasutada ka navigeerimiseks: "5" navigeerimiseks üles ("^"), "7" navigeerimiseks vasakule ("<"), "8" navigeerimiseks alla (`˅`) ja "9" navigeerimiseks paremale (">").


![01](assets/en/01.webp)


Kui pakendiga ei ole probleeme, võite koti avada. Mk4 tuleb koos wallet varukaardiga, mida saab kasutada seadme PIN-koodi, andmepüügivastaste sõnade ja seedphrase kohta käiva teabe salvestamiseks. Järgige initsialiseerimiseks järgmisi samme:


1. Valmistage ette paber ja pliiats.

2. Ühendage Mk4 vooluallikaga (USB-C-kaabel) ja sisestage MicroSD-kaart.

3. Kui seade on esimest korda sisse lülitatud, kuvatakse ekraanil sõnum Coldcardi müügi- ja kasutustingimuste kohta. Navigeerige alla, seejärel vajutage `✓`, et jätkata.

4. Seejärel kuvatakse ekraanil 12-kohaline number. Kontrollige seda numbrit võltsimisvastasel kotil oleva numbriga ja täiendava koopia koti numbriga, mis oli kaasas võltsimisvastasel kotil, et veenduda, et seadet ei ole võltsitud. Kui numbrid ei vasta, võtke enne edasist tegevust kohe ühendust Coinkite toega. Vastasel juhul vajutage jätkamiseks `✓`.


![02](assets/en/02.webp)


5. Valige "Vali PIN-kood".

6. Liikuge allapoole, kui loete juhiseid, et liikuda edasi järgmise sammu juurde.


![03](assets/en/03.webp)


7. Looge ja sisestage Mk4-s PIN-koodi eesliide (peab olema 2-6 tähemärki pikk) ja kirjutage see üles, seejärel vajutage jätkamiseks `✓`.

8. Kirjutage üles kaks sõna, mis kuvatakse ekraanil. Need on andmepüügivastased sõnad. Jätkamiseks vajutage `✓`.


![04](assets/en/04.webp)


9. Looge ja sisestage PIN-koodi järelliide (või PIN-koodi ülejäänud osa, mis peab olema 2-6 tähemärki pikk) ja kirjutage see üles. Jätkamiseks vajutage `✓`.

10. Sisestage uuesti oma PIN-koodi eesliide. Jätkamiseks vajutage `✓`.


![05](assets/en/05.webp)


11. Kontrollige, kas andmepüügivastased sõnad on samad, mida kirjutasite sammu 8 juures. Jätkamiseks vajutage `✓`.

12. Sisestage uuesti oma PIN-koodi järelliide (või PIN-koodi ülejäänud osa). Jätkamiseks vajutage `✓`.


![06](assets/en/06.webp)


13. Teie Mk4-i PIN-kood ja andmepüügivastased sõnad on nüüd edukalt loodud ja salvestatud seadmesse.


![07](assets/en/07.webp)


Pange tähele, et Mk4 palub teil alati PIN-koodi sisestada iga kord, kui lülitate seadme sisse. Ilma selle PIN-koodita ei saa te oma Coldcard Mk4-le ligi. Seega veenduge, et loote piisava varukoopia PIN-koodi ja andmepüügivastaste sõnade jaoks.


## Wallet seadistamine


Järgmine samm on wallet seadistamine. Selleks on kolm võimalust:


- Uue wallet loomine (standard)
- Uue wallet loomine täringuviskega
- wallet importimine


### Uue wallet loomine (standard)


Uue wallet loomiseks tehke lihtsalt järgmised sammud.


1. Valige "Uus Wallet" (või "Uued seemnesõnad") > Valige "12 sõna" või "24 sõna (vaikimisi)", olenevalt teie eelistustest.


![08](assets/en/08.webp)


2. Seade genereerib vastavalt teie valikule 12 või 24 sõna kui seedphrase. Navigeerige allapoole, kui kirjutate hoolikalt iga sõna õiges järjekorras. Seejärel vajutage jätkamiseks `✓`.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Seade palub teil kontrollida oma seedphrase, küsides seda juhuslikus järjekorras (näiteks "Sõna 1 on?", siis "Sõna 5 on?", siis "Sõna 12 on?" jne) ja iga küsimuse puhul on kolm sõnavalikut. Vaadake 2. sammu märkust ja valige sõnad õigesti (vajutades `1`, `2` või `3`, olenevalt sellest, mis vastab õigele sõnale), et täita wallet loomist.


![09](assets/en/09.webp)


4. Mk4 küsib seejärel, kas soovite lubada NFC/Tap või mitte. Praegu valige selleks valikuks `✕`. Seda saab tulevikus seadetes muuta.

5. Lõpuks, Mk4 ka siis, kui soovite keelata USB-porti (mida saab kasutada mitte-õhu kaudu toimuvaks andmeedastuseks). Praegu valige selleks valikuks `✓`. Seda saab tulevikus seadetes muuta.

6. Ekraanil kuvatakse nüüd peamenüü, mille ülaosas on "Valmis allkirjastama". See tähistab wallet loomise protsessi lõpuleviimist.


![10](assets/en/10.webp)


### Uue wallet loomine koos täringuviskega


Te võite ka valida uue seedphrase genereerimise entroopia abil. Tehke seda, kui te ei usalda Mk4 värskelt genereeritud seedphrase.


Coldcard Mk4 puhul on protseduur järgmine:


1. Valige "Uus Wallet" (või "Uued seemnesõnad") > Valige "12 sõna täringuviskamine" või "24 sõna täringuviskamine", olenevalt teie eelistustest.

2. Teil palutakse sisestada oma täringuviskete tulemused. Iga täringuviskega lisatakse wallet loomise protsessi juhuslikkus, mis tagab, et teie seedphrase genereeritakse täiesti turvaliselt ja ettearvamatult. 12-sõnalise seedphrase puhul on minimaalne visete arv 50 ja 24-sõnalise seedphrase puhul 99. Vajutage `✓` pärast seda, kui olete sisestanud vähemalt 99 täringurulli väärtust.


![11](assets/en/11.webp)


3. Seade genereerib vastavalt teie valikule 12 või 24 sõna kui seedphrase. Navigeerige allapoole, kui kirjutate hoolikalt iga sõna õiges järjekorras. Seejärel vajutage jätkamiseks `✓`.

4. Seade palub teil kontrollida oma seedphrase, küsides juhuslikus järjekorras (näiteks "Sõna 1 on?", siis "Sõna 5 on?", siis "Sõna 12 on?" jne) ja iga küsimuse puhul on kolm sõnavalikut. Vaadake 3. sammu märkust ja valige sõnad õigesti (vajutades `1`, `2` või `3`, olenevalt sellest, mis vastab õigele sõnale), et täita wallet loomist.


![12](assets/en/12.webp)


5. Mk4 küsib seejärel, kas soovite lubada NFC/Tap või mitte. Praegu valige selleks valikuks `✕`. Seda saab tulevikus seadetes muuta.

6. Lõpuks, Mk4 ka siis, kui soovite keelata USB-porti (mida saab kasutada mitte-õhu kaudu toimuvaks andmeedastuseks). Praegu valige selleks valikuks `✓`. Seda saab tulevikus seadetes muuta.

7. Ekraanil kuvatakse nüüd peamenüü, mille ülaosas on "Valmis allkirjastama". See tähistab wallet loomise protsessi lõpuleviimist.


![13](assets/en/13.webp)


### wallet importimine


Viimane võimalus on importida wallet. Seda saate teha, kui soovite wallet taastada juba olemasolevast seedphrase-st. Võite järgida järgmisi samme:


1. Valige "Olemasoleva importimine".

2. Valige "24 sõna", "18 sõna" või "12 sõna", sõltuvalt teie seedphrase sõnade arvust.


![14](assets/en/14.webp)


3. Coldcard Mk4 küsib seejärel, mis on iga sõna järjestikku. Navigeerige iga sõna puhul allapoole või ülespoole, kuni leiate iga sõna kirjutamise eesliite. Seade kitsendab võimalusi, kuni leiate õige sõna. Tehke seda ka ülejäänud sõnade puhul.

4. Coldcard Mk4 kuvab lõpliku sõna puhul ainult piiratud arvu võimalikke sõnu. Kui vasteid ei leidu, võis juhtuda, et olete sõnu valesti sisestanud. Vastasel juhul valige sõna, mis vastab teie seedphrase kaardil olevale sõnale.


![15](assets/en/15.webp)


5. Mk4 küsib seejärel, kas soovite lubada NFC/Tap või mitte. Praegu valige selleks valikuks `✕`. Seda saab tulevikus seadetes muuta.

6. Lõpuks, Mk4 ka siis, kui soovite keelata USB-porti (mida saab kasutada mitte-õhu kaudu toimuvaks andmeedastuseks). Praegu valige selleks valikuks `✓`. Seda saab tulevikus seadetes muuta.

7. Ekraanil kuvatakse nüüd peamenüü, mille ülaosas on "Valmis allkirjastama". See tähistab wallet loomise protsessi lõpuleviimist.


![16](assets/en/16.webp)


Pange tähele, et seedphrase on ainus juurdepääs teie wallet taastamiseks. Looge oma seedphrase-st varukoopia ja hoidke seda turvalises kohas. **Ei teie võtmed, ei teie mündid**, kellel iganes on teie seedphrase, on juurdepääs teie bitcoinidele!


## passphrase seadistamine


Üks parimaid tavasid Bitcoin puhul on kasutada passphrase. passphrase toimib 13. või 25. sõnana lisaks seedphrase-le. Erinevus seisneb selles, et te saate valida mis tahes fraasi, samas kui seedphrase valitakse 2048 sõnast koosnevast ettemääratud nimekirjast. Vaikimisi alustate pärast wallet seadistamist wallet-ga, millel on tühi passphrase. Mitte tühja passphrase seadistamiseks tehke lihtsalt järgmised toimingud:


1. Minge `Passphrase` juurde.

2. Navigeerige allapoole, et lugeda passphrase kirjeldust, seejärel vajutage `✓`, et jätkata.

3. Valige `Edit Phrase`.


![17](assets/en/17.webp)


4. Sisestage oma passphrase:


   - Vajutage "1" (tähed), "2" (numbrid) või "3" (sümbolid), et valida märgitüüp.
   - Vajutage `4`, et vahetada väiketähtede ja suurtähtede vahel (saab kasutada ainult tähtede sisestamisel).
   - Navigeerige, kasutades `^` või `˅`, et valida oma passphrase jaoks märk.
   - Liikumiseks märkide vahel kasutage `<` või `>`. Kasutage ka `>`, et lisada tühikuid.
   - Märkide kustutamiseks vajutage `✕`.
   - Kui olete passphrase redigeerimise lõpetanud, vajutage `✓`.

5. Lisaks on teistel valikutel järgmised funktsioonid:


   - Funktsiooniga `Add Word` või `Add Numbers` saab lisada tähti/numbreid passphrase-le, mida te parajasti redigeerite.
   - Vajutage nuppu `Clear ALL`, et lähtestada passphrase, mida te parajasti redigeerite.
   - Vajutage "CANCEL", et minna tagasi peamenüüsse.

6. Kirjutage oma passphrase üles varukoopiana.

7. Vajutage nuppu `APPLY`, et avada wallet koos äsja seadistatud passphrase-ga.

8. Mk4 kuvab seejärel 8 tähemärgi pikkuse peavõti sõrmejälje. Seda võib pidada wallet "ID-ks". Kirjutage see sõrmejälg üles ja jätkamiseks vajutage `✓`.


![18](assets/en/18.webp)


9. Nüüd kuvab wallet wallet peamenüü koos sisestatud passphrase-ga.

10. Oluline on märkida, et wallet ei ütle teile, et olete sisestanud vale passphrase, sest iga passphrase vastab igale wallet-le unikaalse identiteediga (peavõti sõrmejälg). Seetõttu on hea tava sisestada sama passphrase uuesti ja kontrollida, kas see annab sama wallet sõrmejälje, tagades, et olete selle õigesti sisestanud. Selleks tehke sammud 11-14.

11. Valige peamenüüst `Restore Master` ja vajutage `✓`. Nüüd olete tagasi wallet peamenüüs tühja passphrase-ga.


![19](assets/en/19.webp)


12. Minge uuesti menüüsse `Passphrase`, seejärel vajutage `✓`, et jätkata.

13. Sisestage uuesti passphrase, mille olete kirja pannud sammu 6 juures, ja vajutage seejärel nuppu "KASUTA".

14. Kontrollige 8-kohalise pika peavõti sõrmejälge selle sõrmejäljega, mille olete üles kirjutanud sammu 8 juures. Kui mõlemad sõrmejäljed ei ühti, võib juhtuda, et olete sisestanud valesti sobivaid sümboleid. Selle asemel võite valida uue passphrase ja korrata protsessi alates sammust 1. Kui aga mõlemad sõrmejäljed langevad kokku, tähendab see, et olete passphrase õigesti sisestanud.

15. wallet koos teie valitud passphrase-ga on kasutusvalmis.


## Wallet eksportimine Sparrow-sse


Nagu ka teisi wallet riistvara, ei saa ka Coldcard Mk4 kasutada eraldi. See peab olema ühendatud tarkvaralise wallet-ga, mis toimib liidesena. Tarkvara wallet võimaldab teil vaadata oma saldot, luua tehinguid ja hallata aadresse, samal ajal kui Coldcard allkirjastab need tehingud turvaliselt, ilma et teie isiklikud võtmed kunagi avalikuks muutuksid.


Selles õppematerjalis kasutame liidesena Sparrow Wallet. wallet eksportimise protseduur on järgmine:


1. Veenduge, et teil on Mk4-i sisestatud MicroSD-kaart.

2. Viige läbi "passphrase seadistamine" sammud wallet koos passphrasega, mida soovite eksportida. Kui soovite eksportida wallet koos tühja passphrase-ga, võite selle sammu vahele jätta.

3. Mine menüüsse `Advanced/Tools` > Vali `Export Wallet` > Vali `Generic JSON` > Liigu allapoole, kui loed juhiseid, ja vajuta `✓`.


![20](assets/en/20.webp)


4. Mk4 on nüüd loonud MicroSD-kaardile faili formaadis `.json`.


![21](assets/en/21.webp)


5. Eemaldage MicroSD-kaart Coldkaardilt ja sisestage see seadmesse, kuhu on paigaldatud Sparrow Wallet.

6. Avage Sparrow Wallet.

7. Klõpsake nupule "Fail"


![22](assets/en/22.webp)


Seejärel klõpsake nuppu "Uus Wallet"


![23](assets/en/23.webp)


Seejärel sisestage wallet nimi


![24](assets/en/24.webp)


Seejärel klõpsake nupule "Loo Wallet"


![25](assets/en/25.webp)


8. Valige `Skripti tüüp`.


![26](assets/en/26.webp)


9. Valige jaotises Võtmehoidla `Airapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Otsige üles Coldcard ja klõpsake nuppu `Import File...`.


![28](assets/en/28.webp)


11. Valige sammus 4 loodud fail (see, mille vorming on `.json`).


![29](assets/en/29.webp)


12. Mk4-s naaske peamenüüsse ja valige "Täiustatud/tööriistad" > "Identiteedi vaatamine". Veenduge, et Mk4 ekraanil kuvatav sõrmejälg vastab Sparrow Wallet sõrmejäljele (Master fingerprint on Keystore sektsioonis)

13. Vajutage nupule "Rakendada" all paremas nurgas.


![30](assets/en/30.webp)


14. Valikuliselt saate lisada ka salasõna eksporditud wallet-le. See parool on vajalik iga kord, kui avate rakenduse Sparrow Wallet, et pääseda wallet juurde. Kui te unustate tulevikus parooli, saate lihtsalt korrata samme 1-13 ja valida uue parooli.


![31](assets/en/31.webp)


15. wallet on nüüd edukalt eksporditud ja valmis kasutamiseks.


![32](assets/en/32.webp)


## Bitcoini vastuvõtmine


Järgmisena õpime, kuidas võtta Bitcoin vastu Mk4 abil. See protsess on üsna lihtne, sest te ei pea kasutama Mk4 seadet ennast. Kui te olete oma wallet juba Sparrow-sse eksportinud, saate Bitcoin otse Sparrow Wallet kaudu vastu võtta. Järgige neid samme, et saada bitcoine Mk4-ga:


1. Avatud Sparrow Wallet.

2. Valige "Avage Wallet" > Valige wallet fail, kuhu soovite bitcoin'e saada > Sisestage selle walletga seotud parool.


![33](assets/en/33.webp)


3. Sparrow kasutajaliideses klõpsake kasutajaliidese vasakul poolel oleval vahekaardil "Vastuvõtmine".


![34](assets/en/34.webp)


4. Üles ilmub aadress koos QR-koodiga. Saate aadressi kopeerida ja kleepida või skaneerida QR-koodi, kasutades wallet, mida kasutate bitcoinide saatmiseks Sparrow Wallet. Valikuliselt saate sisestada saadud bitcoin'ile sildi.


![35](assets/en/35.webp)


5. Pärast bitcoinide saatmist klõpsake Sparrow kasutajaliideses liideses vasakul pool vahekaardil "Tehingud". Näete tehinguajaloo ülaosas uut kirjet, mis vastab teie äsja tehtud tehingule.


![36](assets/en/36.webp)


6. Samuti saate navigeerida liidese vasakul poolel oleval vahekaardil "UTXOs", et näha äsja saadud bitcoin'e.


![37](assets/en/37.webp)


## Bitcoini saatmine


Erinevalt bitcoinide vastuvõtmisest, peate oma Cold-kaardiga seotud bitcoinide kulutamiseks kasutama Cold-kaarti tehingute allkirjastamiseks. Mk4-ga bitcoinide saatmise protseduur on järgmine:


1. Sisestage MicroSD-kaart seadmesse, kuhu on paigaldatud teie Sparrow Wallet.

2. Avatud Sparrow Wallet.

3. Valige "Avage Wallet" > Valige wallet fail, millega soovite bitcoinide saatmiseks kasutada > Sisestage selle wallet-ga seotud parool.


![38](assets/en/38.webp)


4. Sparrow kasutajaliideses klõpsake kasutajaliidese vasakul poolel oleval vahekaardil "Saada".


![39](assets/en/39.webp)


5. Sisestage vahekaardil "Pay to" aadress, kuhu soovite bitcoinid saata.

6. Lisage tehingule silt.

7. Sisestage bitcoinide summa, mida soovite saata.

8. Sisestage tasu, lülitades valikut "Range" või sisestades otse numbri väljale "Tasu".


![40](assets/en/40.webp)


9. Klõpsake all paremas nurgas nuppu "Tehingu loomine".


![41](assets/en/41.webp)


10. Teil avaneb uus tehingu vahekaart, mille nimeks on sammus 6 sisestatud silt. Klõpsake nuppu `Finalize Transaction for Signing`.


![42](assets/en/42.webp)


11. Klõpsake nuppu "Salvesta tehing" ja salvestage tehing MicroSD-kaardile. Vajaduse korral nimetage fail ümber. See samm salvestab tehingu PSBT failina.


![43](assets/en/43.webp)


12. Eemaldage MicroSD-kaart ja sisestage see Coldcard Mk4-i.

13. Lülitage Mk4 sisse, ühendades selle vooluallikaga.

14. Sisestage oma PIN-kood.

15. Mine `Passphrase` ja sisesta passphrase wallet, mida soovid kasutada bitcoinide saatmiseks. Kui soovite kasutada wallet tühja passphrase-ga, jätke see samm vahele.

16. Veenduge, et üldvõtme sõrmejälg on sama, mis on teie Sparrow Wallet-l. Seda saate kontrollida Sparrow Wallet liidese vasakul poolel oleval vahekaardil `Settings` (seaded). Seejärel vajutage Mk4-l jätkamiseks `✓`. See viib teid peamenüüsse.

17. Valige Mk4 peamenüüst "Valmis allkirjastama". Ekraanile ilmub teade "OLE KÕIGE SÕNDA?". Veenduge, et bitcoinide summa, mida soovite saata, ja vastuvõtja aadress on kõik õiged. Kinnitamiseks vajutage `✓` või tühistamiseks `✕`.

18. Kui valida saab mitme PSBT faili vahel, kuvab Mk4 teate "Valige allkirjastatav PSBT fail". Jätkamiseks vajutage `✓`. Seejärel valige PSBT fail, mida soovite allkirjastada, navigeerides allapoole või ülespoole. Tehke selle tehingu puhul samm 17.


![44](assets/en/44.webp)


19. Mk4 kuvab nüüd teate "PSBT allkirjastatud" koos allkirjastatud PSBT faili nimega. Jätkamiseks vajutage `✓`.

20. Eemaldage MicroSD-kaart Coldkaardilt ja sisestage see seadmesse, kuhu on paigaldatud Sparrow Wallet.

21. Sparrow Wallet klõpsake nuppu "Laadige tehing".


![45](assets/en/45.webp)


22. Valige fail, mille nimi on sama, mis sammus 19 loodud fail.


![46](assets/en/46.webp)


23. Klõpsake nuppu "Tehingu edastamine".


![47](assets/en/47.webp)


24. Teie tehing on edastatud ja seda töödeldakse. Teie tehingu kinnituse staatuse vaatamiseks saate minna vahekaardile "Tehingud".


![48](assets/en/48.webp)


## Firmware uuendamine


### Firmware versiooni kontrollimine


Coldcard Mk4 püsivara saab alati uuema versiooniga uuendada. Selleks, et kontrollida, kas teie Mk4 on uuendatud uusima versiooniga või mitte, tehke järgmised toimingud:

1. Lülitage Mk4 sisse, ühendades selle vooluallikaga.

2. Sisestage oma PIN-kood.

3. Valige `Advanced/Tools` > Valige `Upgrade Firmware` > Valige `Show Version`.


![49](assets/en/49.webp)


Kontrollige Mk4 ekraanil kuvatavat versiooni [Coinkite'i veebisaidil](https://coldcard.com/downloads) oleva versiooniga. Kui versioon on erinev, saate uuendada püsivara uuemasse versiooni.


![50](assets/en/50.webp)


### Firmware uuendamine


Kui soovite uuendada püsivara uusima versioonini, tehke järgmised toimingud:


1. Sisestage MicroSD-kaart sülearvutisse/arvutisse.

2. Mine [Coinkite'i veebisaidile](https://coldcard.com/downloads) ja lae uusim püsivara oma MicroSD-kaardile (punane nupp paremal Mk4-pildist, millel on versiooni number).


![51](assets/en/51.webp)


Te saate alla laadida ka teisi versioone, klõpsates "Kõik Mk4 failid" ja uurides versiooni, mida soovite alla laadida. Allalaaditud fail on `.dfu` formaadis.


![52](assets/en/52.webp)


3. Eemaldage MicroSD-kaart ja sisestage see Mk4-i.

4. Lülitage Mk4 sisse, ühendades selle vooluallikaga.

5. Sisestage oma PIN-kood.

6. Mine menüüsse `Advanced/Tools` > Vali `Upgrade Firmware` > Vali `From MicroSD` > Liikuge allapoole, kui loed juhiseid ja vajuta `✓`.


![53](assets/en/53.webp)


7. Valige sammus 2 allalaaditud fail `.dfu`.

8. Coldcard Mk4 kuvab teate "Installige see uus püsivara?". Kerige allapoole, kui loete juhiseid, ja vajutage seejärel `✓`.


![54](assets/en/54.webp)


9. Oodake, kuni Mk4 lõpetab uue püsivara installimise. Ärge ühendage installimise ajal vooluallikat lahti.

10. Pärast lõpetamist käivitab Mk4 end uuesti. Saate sisestada oma PIN-koodi ja teostada sammud "Firmware versiooni kontrollimine", et kontrollida, kas püsivara on uuendatud või mitte.


## Täiustatud funktsioonid


### Muuda oma PIN-koodi


Kui soovite oma sisselogimise PIN-koodi muuta, tehke lihtsalt järgmised toimingud:


1. Valmistage ette pliiats ja paber.

2. Lülitage Mk4 sisse, ühendades selle vooluallikaga.

3. Sisestage oma PIN-kood.

4. Minge menüüsse "Seaded" > Valige "Sisselogimise seaded" > Valige "Muuda põhipINi"

5. Navigeerige sõnumit lugedes allapoole ja vajutage seejärel jätkamiseks `✓`.


![55](assets/en/55.webp)


6. Sisestage oma vana PIN-kood.

7. Sisestage oma uus PIN-koodi eesliide (peab olema 2-6 tähemärki pikk) ja kirjutage see üles.

8. Mk4 kuvab nüüd kaks uut andmepüügivastast sõna, kirjutage need üles ja vajutage seejärel jätkamiseks `✓`.

9. Sisestage oma uus PIN-koodi järelliide (või PIN-koodi ülejäänud osa, mis peab olema 2-6 tähemärki pikk) ja kirjutage see üles.


![56](assets/en/56.webp)


10. Sisestage uuesti oma uus PIN-koodi eesliide.

11. Kontrollige, kas andmepüügivastased sõnad vastavad sammus 8 kirjutatud sõnadele.

12. Sisestage uuesti oma uus PIN-koodi järelliide (või ülejäänud PIN-kood).


![57](assets/en/57.webp)


13. Teie PIN-kood on edukalt muudetud.


### Trikkide PIN-koodid - Lisa uus trikk


Trikk-PIN on alternatiivne PIN-kood, mis erineb sellest, mida kasutate Coldcard Mk4 esmakordsel seadistamisel. Kui lülitate oma Mk4 sisse, saate teatud toimingute käivitamiseks sisestada trikk-PIN-koodi(d) oma põhipIN-koodi asemel. Trikk-PINi seadistamiseks Mk4-s saate teha järgmised sammud:


1. Valmistage ette pliiats ja paber.

2. Lülitage Mk4 sisse, ühendades selle vooluallikaga.

3. Sisestage oma PIN-kood.

4. Mine menüüsse "Seaded" > Vali "Sisselogimise seaded" > Vali "Trikk-PINid" > Vali "Lisa uus trikk".


![58](assets/en/58.webp)


5. Sisestage oma trikk PIN-koodi eesliide (peab olema 2-6 tähemärki pikk) ja kirjutage see üles.

6. Mk4 kuvab nüüd kaks uut andmepüügivastast sõna, kirjutage need üles ja vajutage seejärel jätkamiseks `✓`.

7. Sisestage oma trikk PIN-koodi järelliide (või PIN-koodi ülejäänud osa, mis peab olema 2-6 tähemärki pikk) ja kirjutage see üles.


![59](assets/en/59.webp)


8. Navigeerige allapoole või üles, et valida tegevus, mida soovite siduda äsja loodud trikkide PIN-koodiga. Tegevuste loetelu on järgmine:


    - kui valitakse "Brick Self", hävitatakse teie Mk4 kiibid pärast PIN-koodi sisestamist, muutes teie Mk4 lõplikult kasutamiskõlbmatuks.
    - "Seemne pühkimine", saate valida järgmiste toimingute vahel:
      - "Puhastamine ja taaskäivitamine": seed kustutatakse ja Coldkaart taaskäivitatakse pärast PIN-koodi sisestamist.
      - `Silent Wipe`: seed kustutatakse vaikselt, kuid Coldkaart käitub nii, nagu oleks PIN-kood valesti sisestatud.
      - `Puhastada -> Wallet`: seed pühitakse vaikselt ja Coldkaart viib teid sundseisundisse wallet.
    - `Duress Wallet`, kui see on valitud, viib teie Mk4 pärast PIN-koodi sisestamist sunniviisilisele wallet-le.
    - `Login Countdown`, saate valida järgmiste tegevuste vahel:
      - `Puhastus ja tagasiarvestus`: seed kustutatakse kohe, seejärel hakkab Mk4 näitama tagasiarvestust.
      - `Countdown & Brick`: Tagasiarvestus algab ja Mk4 müüritab end pärast aja möödumist.
      - "Just Countdown": Mk4 alustab tagasiarvestust ja taaskäivitub pärast aja lõppemist.
    - "Look Blank", kui see on valitud, käitub Coldkaart pärast trikk-PINi sisestamist nii, nagu oleks seedphrase kustutatud, kuid tegelikult on see endiselt mälus.
    - `Just Reboot`, kui see on valitud, taaskäivitub Coldcard ise pärast trikk-PINi sisestamist.
    - see täiustatud funktsioon on mõeldud kogenud kasutajatele ja on mõeldud kaitseks tõsiste ohtude eest, näiteks siseringi teadmistega isiku poolt sundimise eest. Kui delta-režiim on aktiveeritud, näib COLDCARD avanevat tõeline wallet, mis võimaldab ründajal sirvida ja kinnitada, et see näeb välja ehtne. Siiski blokeerib see salaja kõik tehingute allkirjastamised, nii et bitcoine ei saa saata. Samuti keelab see juurdepääsu seed fraasile ja iga katse seda vaadata kustutab selle täielikult. Selleks, et võltsitud wallet näeks veenvam välja, peab Delta Mode'i jaoks kasutatav Trick PIN-kood algama samade numbritega kui tõeline PIN-kood (nii et see näitab samu andmepüügivastaseid sõnu), kuid lõppema teisiti.
    - "Poliitika avamine", kui see on valitud, lülitatakse ühekordse allkirja andmise poliitika (SSSP) välja pärast trikk-PINi sisestamist.
    - "Policy Unlock & Wipe", kui see on valitud, teeb ta näiliselt nii, et keelab SSSP, kuid see pühib seedphrase samal ajal.

9. Pärast seda, kui olete valinud tegevuse, mida soovite trikk-PINiga siduda, kinnitage oma valik, vajutades `✓`. Teie trikk-PIN on edukalt konfigureeritud.

10. Menüüs "Seaded" > "Sisselogimise seaded" > "Trikk-PINid" näete loodud trikk-PINide ja nendega seotud tegevuste loetelu. Saate trikk-PINide ja nendega seotud toimingute ümberkonfigureerimise valida. Saate selle ka varjata või kustutada, valides PIN-koodi ja valides seejärel `Peita trikk` või `Kustuta trikk`.


![60](assets/en/60.webp)


### Trikk PIN-koodid - Lisa, kui see on vale


Alternatiivina saate lisada tegevuse "Lisa, kui vale", mis käivitub pärast seda, kui vale PIN-kood on sisestatud teatud arv kordi. Seda saate konfigureerida järgmiste sammude abil:


1. Lülitage Mk4 sisse, ühendades selle vooluallikaga.

2. Sisestage oma PIN-kood.

3. Minge menüüsse "Seaded" > Valige "Sisselogimise seaded" > Valige "Trikk-PINid" > Valige "Lisa kui vale".


![61](assets/en/61.webp)


4. Mk4 kuvab selle seadistuse kohta teate. Navigeerige selgituse läbilugemisel allapoole ja vajutage seejärel jätkamiseks `✓`.

5. Sisestage meetme käivitamiseks vajalike valede katsete arv. Märkus: Maksimaalne katsete arv on "12". See on tingitud sellest, et Mk4 on konstrueeritud selliselt, et kui vale PIN-kood sisestatakse "13" korda, siis seadet pannakse kinni, muutes selle lõplikult kasutuskõlbmatuks. Pärast numbri sisestamist vajutage jätkamiseks `✓`.

6. Tegevuse valimiseks navigeeri üles või alla. Kättesaadavad toimingud on järgmised:


   - "Pühi, stopp": seedphrase kustutatakse ja seade näitab "Seed is wiped, Stop"
   - "Puhastamine ja taaskäivitamine": seedphrase kustutatakse ja seade käivitub uuesti ilma sõnumita.
   - `Silent Wipe`: seedphrase kustutatakse vaikselt ja seade käitub nagu vale PIN-koodi kustutamise katse (puudub ilmne kustutussõnum).
   - `Brick Self`: Seade on püsivalt välja lülitatud ja näitab ainult "Bricked"
   - "Viimane võimalus": seedphrase kustutatakse, kuid teil on veel üks viimane PIN-katse; sisestage uuesti vale PIN-kood ja seade kustutatakse.
   - `Just Reboot`: Seade lihtsalt taaskäivitub ja midagi muud ei muutu.

Valige soovitud tegevus ja jätkamiseks vajutage `✓`


![62](assets/en/62.webp)


7. Teid viiakse tagasi kataloogi `Settings > Login Settings > Trick PINs` (Seadistused > Sisselogimise seaded > Trick PINs). Kataloogi `Trick PINs:` alt leiate trikk-pinide nimekirja koos toiminguga `WRONG PIN`. Saate selle ka peita või kustutada, valides PIN-koodi ja seejärel valides `Hide Trick` või `Delete Trick`.


![63](assets/en/63.webp)



## Kokkuvõte


Selles õpetuses on esitatud juhised selle kohta, kuidas Mk4 seadistada, kuidas teostada Bitcoin tehinguid Mk4-ga ja kuidas kasutada Mk4 mõningaid täiustatud funktsioone. See pakub turvalisi ja paindlikke võimalusi oma bitcoinide hoidmiseks ja haldamiseks. Selle disain tagab, et privaatvõtmed ei lahku kunagi seadmest, samas kui sellised funktsioonid nagu passphrase, trikk-PINid ja õhu kaudu toimuvad tehingud annavad kasutajatele täieliku kontrolli oma turvaeeskirja üle. Seda saab ühendada Sparrow Wallet-ga, et luua, allkirjastada ja hallata Bitcoin-tehinguid kasutajasõbralikult, ilma et see kahjustaks privaatsust või turvalisust.


Kui soovite uurida muid funktsioone, võite vaadata dokumentatsiooni Coinkite'i veebisaidil [siin](https://coldcard.com/docs/). Loodan, et see õpetus on teile kasulik, kui kasutate oma Coldcard Mk4-i. Tänan teid ja kohtumiseni järgmisel korral!