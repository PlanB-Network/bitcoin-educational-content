---
name: Esimese Lightning-sõlme seadistamine
goal: Lightning-sõlme mõistmine, paigaldamine, konfigureerimine ja kasutamine
objectives: 


  - Mõista Lightning-sõlme rolli ja eesmärki.
  - Määrake kindlaks erinevad olemasolevad tarkvaralahendused.
  - Paigaldage ja konfigureerige Lightning-sõlm (LND).
  - Ühendage kulukonto.
  - Teadke, millised on välgussõlme kasutamisega seotud riskid.


---

# Teie esimene samm Lightningi autonoomia suunas



Olete juba omandanud oma esimese sats, kindlustanud omaenda rahalised vahendid ja võtnud kasutusele Bitcoin sõlme, et olla suveräänne oma on-chain kasutuses. Järgmine samm on saavutada sama autonoomia Lightningil: just see on selle kursuse eesmärk.



LNP202 on suunatud edasijõudnud kasutajatele ja juhendab teid samm-sammult läbi esimese Lightning-sõlme kasutuselevõtu, ilma edasijõudnud tehniliste oskusteta.



Saate teada, kuidas paigaldada LND Umbrel-le, avada ja hallata oma kanaleid, jälgida oma sõlme ja ühendada mobiilne wallet, nii et saate nautida hooldatava wallet-ga võrreldavat kogemust, säilitades samas täieliku kontrolli oma rahaliste vahendite üle.



+++


# Sissejuhatus


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Kursuse ülevaade


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 on praktiline kursus, mis on mõeldud selleks, et muuta teid iseseisvalt Lightning'i abil oma sõlme käitamiseks. Eesmärk on lihtne: alustage juba olemasoleva Bitcoin sõlmega, võtke LND kasutusele Umbrel peal, kindlustage see korralikult, avage ja haldage oma esimesi kanaleid, seejärel kasutage oma sõlme igapäevaselt mobiilsest wallet-st. See kursus eeldab, et olete juba võtnud BTC 202, sest ma eeldan, et teie Bitcoin sõlme Umbrel on paigas ja sünkroonitud. Me ei hakka siinkohal uuesti läbi käima, kuidas Bitcoin sõlme seadistada.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Lightning'i sisemise mehaanika paremaks mõistmiseks on samuti väga soovitatav läbida kursus LNP 201, kuigi see ei ole selle kursuse eeltingimus:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Selle LNP202 kursuse esimeses osas vaatleme, mis Lightning-sõlm tegelikult on, kuidas see erineb lihtsast wallet-st ja miks isikliku sõlme kasutamine on ainus viis Lightningi kasutamiseks ilma sats delegeerimiseta usaldusväärsele kolmandale osapoolele. See osa lõpeb strateegilise valikuga: milline lahendus on teie jaoks õige, alates kõige lihtsamatest lähenemisviisidest kuni klassikalise Lightning-sõlmeni, mida me sellel kursusel rakendame.



Kursuse 2. osas paigaldate LND Umbrel-le, seejärel panete paika elemendid, mis hoiavad ära kõige kallimad vead: realistlik varundusstrateegia ja kaitse pettuse vastu vaatetorni abil. Kui need põhitõed on paigas, avate oma esimese kanali, et saaksite oma infrastruktuuriga Lightningile maksma hakata.



Nii et näete: selles LNP202 kursuses seadistame Lightning-sõlme plug-and-play režiimis Umbrel abil, mitte klassikalise käsureal põhineva lähenemisviisi, et see sobiks ka edasijõudnutele. Kui te eelistate käsurea paigaldamist, siis soovitan järgida alljärgnevat õpetust. Ettevalmistamisel on ka teised, edasijõudnute käsureale orienteeritud Lightningi kursused.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

3. osa viib teid siis töötavast sõlmest selleni, mida te oskate kontrollida. Alustate Lightning-sõlme operaatoriprofiili (tarbija, kaupmees või marsruuter) määramisest, seejärel saate hakkama täieliku haldustarkvara paketiga, et jälgida oma kanaleid ja tegutseda puhtalt oma topoloogias. Lõpuks tegelete väga olulise Lightningi punktiga: kuidas saada sissetulevat likviidsust, kas tasuliste või ühiste lahenduste kaudu.



4. osa keskendub igapäevasele kasutamisele. Saate luua ühenduse oma sõlme ja mobiilikliendi vahel, et saaksite maksta ja koguda lihtsalt oma nutitelefonist, ilma et loobuksite iseenda haldamisest. Vaatleme kõigepealt võrgupõhist lähenemist *Tailscale* kaudu, seejärel protokollipõhist lähenemist *Nostr Wallet Connect* kaudu, koos nende vastavate eeliste ja kompromissidega. Kursus lõpeb lõpupeatükiga, mis annab teile õiged harjumused, et säilitada isehaldust nii operatiivselt kui ka pedagoogiliselt.



Kui te järgite seda LNP202 kursust õiges järjekorras, on teil selle lõpuks oma Lightning-sõlme täielik konfiguratsioon, mis on igapäevaseks kasutamiseks toimiv ja eelkõige kontrolli all.




## Lightning-sõlmede mõistmine


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Enne oma sõlme käivitamist vaadatakse selles peatükis lühidalt üle Lightning Network põhiteooria. On tõepoolest oluline mõista asjaomaseid mehhanisme, sest see võimaldab teil tuvastada riske ja võtta kasutusele häid tavasid nende piiramiseks. Ma ei hakka siinkohal siiski üksikasjadesse laskuma, sest see ei ole selle kursuse peamine eesmärk. Kui soovite teemasse süveneda, siis soovitan tungivalt tutvuda Fanis Michalakise kursusega LNP 201, mis on selles valdkonnas referentsiks:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Mis on välgussõlm?



Läheme tagasi põhitõdede juurde: enne sõlme määratlemist peame mõistma, mis on Lightning Network. See on tippkihi protokoll, mis on ehitatud Bitcoin peal ja mille eesmärk on võimaldada ahelaväliseid BTC tehinguid, mis on kiired (peaaegu kohese lõplikkusega) ja üldiselt odavad. "Offchain" tähendab, et Lightning'iga teostatud tehingud ei ole ette nähtud Bitcoin põhiplokiahelas ilmumiseks. Lightning on ka osaline vastus Bitcoin kasvavale kasutamisele ja ahelasisesele ülekoormusele, mis tekitab muret süsteemi skaleeritavuse pärast.



Lightning tugineb toimimiseks osalejate vaheliste maksekanalite avamisele, mille raames saab tehinguid teostada peaaegu koheselt, sageli minimaalsete tasudega, ilma et neid oleks vaja ükshaaval Bitcoin plokiahelas registreerida. Need kanalid võivad jääda avatuks väga pikaks ajaks, nõudes ahelas toimuvaid tehinguid ainult nende avamisel ja sulgemisel.



Lightning-sõlm on Lightning-võrgus osaleja, kes avab kanaleid ja teeb makseid teiste sõlmedega. Konkreetselt öeldes on Lightning-sõlm arvutis töötav tarkvara, mis rakendab Lightning Network protokolli. Näiteks LND, Core Lightning või Eclair. Selle tarkvara peamine roll on:




- ühendada Bitcoin sõlme, et saada teavet peamise plokiahela pealt;
- luua ja hallata kahesuunalisi maksekanaleid teiste sõlmedega;
- vahetada sõnumeid kogu Lightning-võrguga.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: oluline erinevus



Bitcoin (onchain) puhul viitab "*wallet*" tarkvarale, mis haldab teie isiklikke võtmeid, arvutab teie saldot teie UTXO-st ja koostab teie tehinguid. See wallet võib põhineda teie enda Bitcoin sõlmel või kellegi teise omal, kuid tänapäeval on sõlme ja onchain wallet roll selgelt erinev.



Lightningi puhul on sellist sõnavara keerulisem taaskasutada, ilma et see tekitaks segadust. Mõiste "*Lightning wallet*" on üsna ebamäärane, sest tegelikult ei ole olemas tõeliselt isemoodi Lightning wallet, kui see ei põhine sõlmel. Seega on võimalik ainult kaks olukorda:



- Tõelise Lightning-sõlme omamine (s.t. mittekasutatav): tarkvara, mida kasutate (nt mobiilirakendus nagu Phoenix või LND instants Umbrel), on tegelikult sõlme käivitav ja teil on tegelikult võtmed oma bitcoinide kättesaamiseks. Sellisel juhul on teie "*Lightning wallet*" tegelikult lihtsalt kasutajaliides Lightning-sõlme peal, olgu see siis sisseehitatud või eemal asuv.



- Hoiuteenuse kasutamine: te kasutate rakendust, mis näitab teile Lightning'is saldot sats-s, kuid taustal on vahendid teenusepakkuja sõlmes (nt Wallet of Satoshi). Teil ei ole võtmeid ega kontrolli kanalite üle. Teie saldo on lihtsalt raamatupidamiskirje ettevõtte andmebaasis. See on võrreldav sellega, et jätate oma bitcoinid vahetusplatvormile, koos kõigi sellega kaasnevate riskidega. Sellisel juhul on teie "*Lightning wallet*" lihtsalt juurdepääs kontole, mida haldab operaator, kes omakorda juhib reaalset Lightning-sõlme.



Seega ei ole Lightningi puhul mingit vahepealset olukorda: kas sul on sõlmpunkt (isegi varjatud), nii et sa oled ise halduses, või ei ole, nii et sinu sats kuulub ettevõttele. Kuid nagu me järgmistes peatükkides näeme, on neid kahte kasutusviisi mõnikord raske eristada. Näiteks Phoenix on mobiilirakendus, mis varjab endas tõelist Lightning-sõlme, kuid kasutaja ei pruugi sellest teadlik olla, sest selle töö täielik keerukus on peaaegu täielikult varjatud.



### Meeldetuletus Lightning Network tööpõhimõtete kohta



Selles jaotises annan teile kiire meeldetuletuse, kuidas Lightning töötab. Veel kord, kui soovite teoreetiliste mõistete põhjalikumat esitlust, kutsun teid üles vaatama spetsiaalset kursust LNP 201.



#### Maksekanalid: avamine, uuendamine ja sulgemine



Lightning-võrgu süda põhineb kahesuunalistel maksekanalitel. Kanali saab avada (st luua), uuendada, kui Lightning-tehingud toimuvad, ja seejärel sulgeda. Onchaini seisukohalt ei ole kanal midagi muud kui 2/2 mitme allkirjaga väljund.



![Image](assets/fr/002.webp)



Lightning'i seisukohast on tegemist maksekanaliga, mille likviidsus on jagatud kahe osaleja vahel.



![Image](assets/fr/003.webp)





- Kanali avamine:**



Kaks sõlme otsustavad avada kanali. Üks neist paneb bitcoine ahelasiseses tehingus, mida nimetatakse *finantseerimistehinguks*. See tehing loob väljundi, mis põhineb 2-of-2 multisignatuuriskriptil, mis tähendab, et nende vahendite kulutamiseks Bitcoin-s on vaja mõlema kanali sõlme allkirja. Enne selle tehingu väljastamist palub raha andev pool teisel poolel allkirjastada *väljavõtutehing*, mida ei väljastata ahelas, kuid mis võimaldab tal probleemide korral oma raha tagasi saada.



![Image](assets/fr/004.webp)





- Commitment tehingud:**



Kanali seisundit (st sats jaotust A ja B vahel) esindab *commitment transaction*, mis on teada mõlemale sõlmpunktile, kuid mida ei edastata kohe plokiahelas. See tehing kirjeldab, kuidas kanali rahalised vahendid jaotatakse ahelas ümber vastavalt Lightning'ile tehtud maksetele.



Iga Lightning-makse korral allkirjastavad kaks sõlme uue seisundi, mis asendab eelmise. Vana olek tühistatakse tänu tühistamisvõtme mehhanismile: kui üks osalejatest üritab vana olekut edastada, saab teine osaleja karistusena tagasi nõuda kogu summa.



Oluline mõte on see, et alati on olemas allkirjastatud Bitcoin tehing, mida sõlmed ei edasta ahelas, mida sõlmed hoiavad ja mis võimaldab üksteise sats ümberjaotamist vastavalt Lightning Network tehtud maksetele.



![Image](assets/fr/005.webp)





- Kanali sulgemine:**



Kanali võib sulgeda puhtalt, kui mõlemad osapooled lepivad kokku kanali lõppseisundis, või ühepoolselt (sunniviisiline sulgemine), kui üks osalejatest lõpetab koostöö või muutub kättesaamatuks. Kõigil juhtudel toimub sulgemine ahelas toimuva tehingu vormis, mis kulutab 2/2 väljundit ja jaotab vahendid osalejate vahel vastavalt kanali viimasele kehtivale olekule.



![Image](assets/fr/006.webp)



Lightning toimib seega Bitcoin-le ankurdatud sekundaarse kihina: ainult teatud sündmused (kanalite avamine ja sulgemine) ilmuvad põhiplokiahelas. Vahepealsed maksed jäävad ahelaväliseks.



Enne edasist tegevust on siin kaks olulist mõistet, mis aitavad mõista, kuidas Lightning-kanalit hallata:




- Liquidity*: sats kogus, mis on saadaval kanali ühel poolel;
- *Kapatsiteet*: see on 2/2 multisig väljundis lukustatud kogusumma, st kanali mõlema poole likviidsuse summa.



#### Kanalite ja likviidsuse võrgustik



Kanal ei ole ainult maksete tegemiseks kahe sõlme vahel: see on osa omavahel ühendatud kanalite ülemaailmsest võrgustikust. Teie sõlme saab suunata makseid teistele kasutajatele oma kanalite kaudu ja te võite saata sats Lightning-sõlme, millega teil ei ole otsekanalit, kui teie kahe sõlme vahel on võimalik leida kehtiv tee.



Iga sõlmpunkt teab kuulujutuprotokolli kaudu selle võrgu kaarti: millised kanalid on olemas, millised sõlmed on ühendatud kahesuunalise kanaliga ja millised võimsused on avaldatud. Selleks, et saata makse vastuvõtjale ilma otsekanalita, arvutab oma sõlme marsruudi, mis koosneb mitmest hüppest: oma sõlme → sõlme X → sõlme Y → vastuvõtja sõlme. Igal hüppel läbib makse kanalit, millel peab olema piisav likviidsus makse suunas.



![Image](assets/fr/007.webp)



Kanali likviidsus ei ole seega sümmeetriline: üks pool võib olla tugevalt koormatud, samas kui teine pool on peaaegu tühi. Selle likviidsuse haldamine, st teadmine, kus sats on ja millises suunas nad võivad voolata, on üks Lightning-sõlme käitamise kõige olulisemaid aspekte. Vaatleme seda üksikasjalikumalt järgmistes praktilistes peatükkides.



#### HTLC: makse transportimine ilma röövimata



Selleks, et maksed liiguksid läbi vahesõlmede ilma usalduse vajaduseta, kasutab Lightning nutikaid lepinguid nimega *HTLC* (*Hashed Time-Locked Contracts*). Lihtsustatult öeldes seab HTLC raha ülekandmise tingimuseks saladuse avalikustamise ja sisaldab ajalist piirangut, et kaitsta saatjat tehingu ebaõnnestumise korral. Iga makse eeldab seega eelkujutise esitamist (saladus, mille hash vastab kokkulepitud väärtusele). Kui lõplik saaja esitab selle eelkujutise, saab ta raha nõuda, mis omakorda võimaldab igal vahendussõlmel oma raha tagasi saada.



![Image](assets/fr/008.webp)



Ma säästan teid HTLC töö tehniliste üksikasjadega, kuna need ei ole selle kursuse jaoks olulised. Põhjaliku selgituse leiate LNP 201 teooriakursusest. Pidage lihtsalt meeles, et HTLC võimaldab aatomivahetust: kas ülekanne viiakse lõpule ja keegi ei saa marsruutimisest kahju, või see ebaõnnestub ja iga osaleja saab oma esialgsed vahendid tagasi. Vahepealset olukorda ei ole.



### Peamised Lightning-sõlmede rakendused



Nagu Bitcoin puhul, on ka Lightning-protokolli rakendamiseks mitmeid lahendusi. Mitmed sõltumatud meeskonnad töötavad välja oma versioone, mis kõik on koostalitlusvõimelised, kuna nad järgivad samu spetsifikaate (BOLTid). Järgnevalt on esitatud peamised praegu kasutusel olevad rakendused.



#### LND (*Lightning Network Daemon*)



LND on Lightning-protokolli täielik implementatsioon, mis on kirjutatud Go keeles ja mille on välja töötanud Lightning Labs.



![Image](assets/fr/009.webp)



#### Core Lightning (*CLN*)



Core Lightning (varem *C-Lightning*) on Blockstream'i poolt välja töötatud rakendus. See on kirjutatud C keeles, mõned komponendid on Rust keeles.



![Image](assets/fr/010.webp)



#### Eclair



Eclair on Scala keeles kirjutatud rakendus, mille on välja töötanud Prantsuse ettevõte ACINQ. ACINQ haldab Eclairiga üht tähtsamat marsruutimiskeskust Lightning-võrgus ning kasutab seda rakendust oma toodete, näiteks Phoenix rakenduse tarkvaralisena.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) on Rust arenduskomplekt, mida hooldab Spiral (Block, endine Square). See ei ole valmis daemon nagu LND või CLN, vaid raamatukogu arendajatele, kes soovivad Lightningut otse oma rakendustesse integreerida.



![Image](assets/fr/012.webp)



Sellel LNP202 kursusel keskendume peamiselt LND-le: see on rakendus, mida kasutatakse kõige sagedamini eraklientidele mõeldud võtmevalmis lahendustes, näiteks Umbrel.



Nii palju sellest lühikesest meeldetuletusest, kuidas Lightning töötab. Veel kord, kui teil on mõni mõiste, millest te ei saa aru, või kui te tahate enne praktikasse rakendamist veidi süveneda, siis Fanis Michalakise kursus on oluline viide sellel teemal:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Miks käivitada oma Lightning-sõlme?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Sellele küsimusele vastamine on üsna lihtne, sest see on retooriline: ilma oma sõlme kasutamata ei kasuta sa enam tegelikult Lightningut, vaid ainult Lightningu illusiooni kogu ettevõtte infrastruktuuris.



Lightning custodial wallet kasutamine tähendab, et bitcoinid kuuluvad tehniliselt sõlme haldavale ettevõttele. Teil ei ole privaatvõtmeid ja te ei kontrolli kanaleid. Teie wallet saldo on lihtsalt rida teenusepakkuja andmebaasis. Selline olukord on algajatele kindlasti väga mugav ja kasutajakogemus on sageli sujuv, kuid põhiküsimus on: mis kasu on Bitcoin ja Lightningi kasutamisest, kui lõpuks loobute just nendest aspektidest, mis eristavad neid traditsioonilistest valuutadest ja pankadest?



Bitcoin kaks peamist väärtuspakkumist on rahaline suveräänsus (raha väljaandmine ja hoidmine ei sõltu enam keskasutusest) ja tsensuurikindlus (kolmanda osapoole võimetus makseid takistada või filtreerida). Lightningi hoiusüsteem läheb mõlema eesmärgi vastu: te ei saa kontrollida platvormi sisemist rahapakkumist ning definitsiooni kohaselt saab operaator, kes hoiab kõiki vahendeid ja kõiki kanaleid, teie makseid tsenseerida, edasi lükata, prioritiseerida või blokeerida. Nendel tingimustel võime me õigustatult küsida, **milleks on mõtet kasutada bitcoini Lightningi kaudu, kui see hakkab taastootma samu usalduse ja sõltuvuse mustreid nagu traditsiooniliste riiklike rahasüsteemide puhul**.



> Vaja on elektroonilist maksesüsteemi, mis põhineb usalduse asemel krüptograafilisel tõestusel, mis võimaldab kahel soovival osapoolel teha omavahel otse tehinguid, ilma et oleks vaja usaldusväärset kolmandat osapoolt.
*Satoshi Nakamoto, Bitcoin Valge raamat


Kui filosoofia kõrvale jätta, siis konkreetsemad puudused teie jaoks on järgmised. Esiteks ei ole teil võimalik kontrollida, et ettevõte tegelikult omab kuvatavatele saldodele vastavaid bitcoine. See võib toimida murdvaral, olla häkitud, minna pankrotti või lihtsalt kaduda. Sellisel juhul olete lihtsalt veel üks võlausaldaja, ilma reaalse garantiita, et saate oma raha tagasi.



Teiseks on ettevõte avatud regulatiivsetele riskidele: ettekirjutused, rahaliste vahendite külmutamine, kasutajate või tehingute blokeerimise taotlused, tugevdatud järelevalve või isegi tegevuse otsene keelamine teatavates jurisdiktsioonides. Iga piirang, mis teenusepakkujat koormab, peegeldub mehaaniliselt ka teile.



Konfidentsiaalsuse osas ei ole olukord parem. Hooldusoperaator näeb kõiki teie rahavooge: summasid, sagedusi, saajaid, saldosid, kulutamisharjumusi. Kombineerituna rakendusest saadava teabega ja võimaluse korral Bitcoin aluseks oleva ahelaanalüüsiga, võib see teave anda väga täpse profiili teie finantstegevusest. Jällegi, see on kaugel Bitcoin eesmärgist vähendada finantsjärelevalvet.



Hea uudis on see, et tänapäeval ei ole oma Lightning-sõlme käitamine enam tehniliste ekspertide pärusmaa, nagu see võis olla 2010. aastate lõpus. Kodukasutajatele on saadaval suhteliselt lihtsad lahendused, mida selgitame üksikasjalikult järgmises peatükis.




## Õigete lahenduste valimine


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Tänapäeval on võimalik saada kasutajakogemus, mis on väga lähedane välklambi wallet kasutajakogemusele, jäädes samal ajal ise hooldatavaks. Selle peatüki eesmärk on aidata teil valida teie profiilile kõige sobivam tee.



### Võimalus 1: Ära kasuta välku otse



Esimene lahendus on lihtsalt mitte kasutada Lightningut algupäraselt, vaid kasutada Bitcoin või Liquid wallet, mis sisaldab aatomivahetusi. Näiteks Aqua või Bull Bitcoin Wallet rakendused kasutavad seda meetodit, võimaldades teil tasuda Lightningi arveid ilma Lightningi sõlme ise käitamata, jäädes samas ise haldusse.



Põhimõte on lihtne: teie rahalised vahendid jäävad Bitcoin-sse, kas on-chain-sse või Liquid-sse, ja te pääsete neile ligi wallet kaudu, kus te hoiate võtmeid traditsioonilisel viisil. Kui skaneerite Lightning-arve, algatab teie wallet tehingu (on-chain või Liquid) aatomivahetusteenusele. See teenus haldab seejärel Lightning-makset oma sõlme kaudu, kasutades teie poolt on-chain või Liquid kaudu antud bitcoine. Selle tulemusena ei pea te ise ühtegi Lightning-kanalit haldama, kuid saate siiski sujuvalt Lightning-arveid arveldada.



![Image](assets/fr/013.webp)



Selle lähenemisviisi peamine eelis võrreldes tavapärase välkdepositooriumi wallet-ga on see, et teie rahalised vahendid on alati 100% ulatuses teie valduses. Bitcoins on teie onchainis või Liquid wallet, millel on teie enda mnemo fraas. Isegi vahetuse ajal jääte oma rahaliste vahendite valdusesse, sest vahetus on aatomiline. See tugineb krüptograafilisele mehhanismile, mis tagab, et on ainult kaks võimalikku tulemust: kas vahetus õnnestub täielikult või ebaõnnestub ja teenus ei saa teie raha omastada.



Enamik portfelle, mis pakuvad seda tüüpi funktsioone, tuginevad [Boltz](https://boltz.exchange/) vahetuse tehnilise osa jaoks.



See lahendus pakub huvitavaid eeliseid ka konfidentsiaalsuse osas, eriti kui see on ühendatud Liquidga. Algaja jaoks on seda ka väga lihtne seadistada ja salvestada: klassikaline mnemofraas, ei mingeid kanaleid, ei mingit likviidsust, mida tasakaalustada...



Teisest küljest on sellel lähenemisviisil omad piirangud. Esiteks, see ei ole hindamatu: te sõltute vahetusteenuse kättesaadavusest ja heast tahtest. Kui see ei soovi enam teie kontot töödelda või lõpetab tegevuse, ei saa te selle kaudu enam välkarvete eest tasuda. Siis on veel märkimisväärsed tasud: te maksate nii onchaini või Liquid tehingutasu kui ka vahetusteenuse vahendustasu. Kui onchaini tasud järsult tõusevad, võib Lightningi kasutamine muutuda väga kalliks.



Nii et juhuslikuks kasutamiseks on see veel vastuvõetav, kuid väga aktiivse Lightning'i kasutaja jaoks on parem teha asju õigesti tõelise Lightning'i sõlme abil.



### Võimalus 2: Pardal olevad välgussõlmede sõlmpunktid



Teise kategooria lahendused põhinevad otse mobiilirakendusse integreeritud Lightning-sõlmedel. Phoenix Wallet oli selle mudeli teerajaja ja on endiselt eeskujuks. Tänapäeval pakuvad võrreldavaid lähenemisviise ka teised projektid, näiteks Zeus (sisseehitatud režiimis) või BitKit.



Idee on lihtne: rakendus töötab tegelikult Lightning-sõlme, kuid kõik keerulised toimingud toimuvad automaatselt taustal. Teil on "*Lightning wallet*" kasutajaliides koos mnemofraasiga varundamiseks, te näete saldot ja maksate arveid, kuid te ei halda kanaleid, likviidsust ega enamikku parameetreid.



![Image](assets/fr/014.webp)



Need lahendused on alati isetehtud. Fondide kontrollimiseks kasutatavad võtmed on generated ja neid hoitakse teie telefonis ning varundamine toimub seed või samaväärse mehhanismi abil. Teil ei ole lihtsalt konto teenusepakkuja juures, vaid te tegelikult omate bitcoin'e, mis on lukustatud kanalitesse, mis kuuluvad teile ja mida ei saa varastada.



LN pardasõlmede eelised on arvukad:




- äärmiselt lihtne paigaldada ja kasutada;
- kasutajakogemus, mis on sarnane hooldusvahendi Lightning wallet kasutajakogemusele, kuid millel on enesehooldus;
- puudub kanalite või likviidsuse käsitsi haldamine;
- suhteliselt lihtne varundamine.



Kuid neil sisseehitatud wallet-l on ka märkimisväärsed piirangud. Esiteks on teenuseoperaatoril (nt ACINQ Phoenix puhul) konfidentsiaalsuse osas üsna üksikasjalik ülevaade teie sõlme läbivatest voogudest: summad, sagedused, vastuvõtjad, kuigi see on kindlasti paranemas, eriti *Trampoliinisõlmede* järkjärgulise kasutuselevõtuga. Teiseks, te olete sellest operaatorist kui teie peamisest Lightning-partnerist tugevalt sõltuv. Kui ACINQ-sõlm muutub kättesaamatuks (Phoenix puhul), kui ettevõte satub regulatiivse surve alla või muudab oma ärimudelit, võib teie kasutajakogemus oluliselt halveneda või isegi ohtu sattuda.



Lõpuks on sellel lihtsusel oma hind. Sisseehitatud LN-sõlmede teenused võtavad üldiselt konkreetseid tasusid hoiuste, väljamaksete või teatavate kanalihaldusoperatsioonide eest. Minu arvates on see mudel pakutava teenuse mõttes mõistlik, kuid intensiivse kasutamise puhul võib see olla palju kallim kui hästi hallatav tavaline Lightning-sõlm.



### Valik 3: klassikaline Lightning-sõlm



Kolmas lahendus, mida me selles LNP202 kursuses põhjalikumalt vaatleme, on tavalise Lightning-sõlme kasutamine spetsiaalses serveris või seadmes.



"Klassikalise" all pean silmas seda, et te paigaldate ja konfigureerite Lightning'i rakenduse (nt LND) ise oma Bitcoin sõlme peale. Te valite oma partnerid, avate oma kanalid, haldate oma sissetulevat ja väljaminevat likviidsust ning määrate oma marsruutimistasu poliitikad.



Suveräänsuse seisukohalt on see parim lahendus. Te ei ole enam sõltuvuses konkreetsest ettevõttest oma kanalite või maksete osas: kui mõni partner tsenseerib teid või sulgeb kanali, saate avada teise kanali teise sõlme abil. Kui teenus kaob, jääb teie sats teie kontrolli all olevatesse kanalitesse ja te saate need onchaini tagasi saata. Samuti saate optimeerida oma pikaajalisi kulusid: kui teie kanalid on õigesti dimensioneeritud ja hallatud, võivad maksete kogukulud muutuda väga madalaks.



Konfidentsiaalsuse osas kehtivad teile ilmselt Lightningi enda mudeli piirangud, kuid te ei anna kogu oma äri üle ühele operaatorile.



Seevastu klassikalise Lightning-sõlme loomine on ilmselgelt keerulisem: tuleb paigaldada, konfigureerida, hooldada, jälgida uuendusi, mõista kanalite loogikat ja maksupoliitikat, hallata kanaleid ja rahavoogusid jne. Vale konfigureerimine, lohakas varundamine või hooletu haldamine võib kergemini viia sats kaotamiseni. Samuti peab sõlme pidevalt töötama.



Just seda teed soovitan ma teile sellel kursusel järgida, olles teile igal sammul kaasas, et piirata riske ja struktureerida oma lähenemist.



### Milline lahendus millise kasutajaprofiili jaoks?



Selleks, et valida õige lahendus teie Lightningi kasutajaprofiili jaoks, peate arvestama kahte tegurit: kui tihti te Lightningit kasutate ja kui palju soovite tehnilist haldust.



Kui te ei tee aeg-ajalt palju välkmakseid, kuid soovite siiski aeg-ajalt oma telefonist LN arveid arveldada, ilma et loobuksite isehaldusest: Bitcoin või Liquid wallet vahetusfunktsiooniga on tõenäoliselt parim valik. Te säilitate oma rahaliste vahendite omandiõiguse, ei halda ühtegi sõlme ja võtate lihtsuse eest vastu veidi kõrgemad tasud.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Kui kasutate Lightningut üsna regulaarselt ja soovite tõelise sõlme eeliseid, kuid ei soovi kulutada aega kanalite, tasude või infrastruktuuri haldamisele, on mobiilne varjatud Lightningusõlm hea lahendus. Te säilitate oma rahaliste vahendite haldamise, kasutajaliides jääb väga ligipääsetavaks ja kogu keerukus on varjatud, kuid selle hinnaga, et olete märgatavalt sõltuvuses operaatorist.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Kui olete edasijõudnud või edasijõudnud kasutaja, kes on valmis investeerima aega oma infrastruktuuri mõistmisse ja haldamisse ning soovib maksimaalset kontrolli oma kanalite, likviidsuse ja kulude üle: klassikaline serveripõhine Lightning-sõlm on õige lahendus. See on kõige nõudlikum lahendus, kuid ühtlasi ka kõige rohkem kooskõlas Bitcoin suveräänsuse ideega.




# Esimese Lightning-sõlme loomine


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## LND paigaldamine koos Umbrel-ga


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Nüüd, kui oleme Lightning'i põhitõed ja olemasolevad lahendused läbi vaadanud, on aeg asuda asja juurde. Selle kursuse läbimiseks on teil vaja Bitcoin sõlme, mis on sünkroniseeritud Umbrel-ga. See LNP202 koolituskursus on jätkuks BTC 202-le; kui teil ei ole veel Bitcoin sõlme, kutsun teid üles võtma seda teist koolituskursust, enne kui te siia tagasi tulete, kui teie sõlm on sünkroniseeritud. Soovitan tungivalt tutvuda sellega, sest ma ei lähe selle toimimise, konfigureerimise ja turvameetmete kohta üksikasjalikult läbi.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Selles esimeses peatükis vaatame, kuidas LND Umbrel-le paigaldada. Umbrel tööpõhimõte teeb selle sammu väga lihtsaks, sest teil tuleb vaid paigaldada rakendus.



Avage avalehelt kasutajaliidese allosas asuv "rakenduste pood".



![Image](assets/fr/015.webp)



Sisestage otsinguribale `Lightning Node`, seejärel klõpsake rakendusel.



![Image](assets/fr/016.webp)



Seejärel klõpsake installimise käivitamiseks nupule `Install`.



![Image](assets/fr/017.webp)



Avage rakendus avalehel, klõpsake selle avamiseks, seejärel valige "Uue sõlme loomine".



![Image](assets/fr/018.webp)



Teile antakse 24-sõnaline mälulause. Hoidke seda kindlas kohas. Järgmises peatükis vaatleme üksikasjalikumalt, kuidas taastada juurdepääs oma välgumihklile (see on palju keerulisem protsess kui lihtsa Bitcoin wallet puhul), kuid pidage esialgu meeles, et see fraas mängib otsustavat rolli ja seda tuleb säilitada ülima hoolikusega.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Salvestage see lause samamoodi nagu tavaline mnemooniline lause: füüsilisel andmekandjal (paber või metall), mida hoitakse turvalises kohas, seejärel klõpsake nupule "NEXT".



![Image](assets/fr/019.webp)



Seejärel sisestage oma lause sõnad, et kontrollida, kas olete need õigesti kirja pannud.



![Image](assets/fr/020.webp)



Hoiatussõnum tuletab teile meelde, et rakendus on beetaversioonis ja et Lightning Network on endiselt eksperimentaalne tehnoloogia. Loomulikult ärge kunagi pühendage oma Lightning-sõlme summasid, mida te ei ole valmis kaotama.



Seejärel jõuate oma Lightning-sõlme põhiliidesesse. Vasakul leiate oma Bitcoin onchain wallet, mis asub teie sõlmes. See on üks generated 24-sõnalisest fraasist, mille te just salvestasite.



Keskel on teie Lightning wallet. See kujutab tegelikult teie väljaminevat raha, st bitcoin'e, mida te oma Lightning-kanalites omate.



Paremal pool näete mitmeid olulisi andmeid oma sõlme kohta:




- Ühenduste ja avatud kanalite arv;
- Teie kogu väljaminev rahavoog, st see, mida te teoreetiliselt saate kulutada Lightning'ile;
- Teie kogu sissetulev likviidsus, st see, mida te teoreetiliselt saate Lightning'ilt.



![Image](assets/fr/021.webp)



Alustame meie sõlme kohandamisest. Klõpsake kolmel väikesel punktil kasutajaliidese paremas ülaosas, seejärel valige "Täiustatud seaded". Allmenüüs `Personaliseerimine` saate määrata oma sõlme avaliku nime (vältige oma tegeliku nime kasutamist) ja valida selle värvi.



![Image](assets/fr/046.webp)



Seejärel klõpsake rohelisel nupul `SAVE AND RESTART`, et taaskäivitada oma sõlme ja rakendada need muudatused.



Teie Lightning-sõlm on nüüd valmis avama oma esimesed kanalid maksete tegemiseks. Kuid kõigepealt vaatame, kuidas kaitsta oma sats!



## Lightning-sõlme salvestamine


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Enne esimese sats saatmist oma sõlmpunkti on oluline mõista, kuidas selle varundamine toimib ja millised on sellega seotud riskid. Erinevalt lihtsast Bitcoin onchaini portfellist on Lightning-sõlme varundamine üsna keeruline: vale strateegia võib viia teie vahendite lõpliku kadumiseni. Selles peatükis vaatleme, mida tegelikult on vaja varundada ja kuidas Umbrel seda protsessi LND abil käsitleb.



Sellel kursusel kasutame LND (*Lightning Network Daemon*) rakendamist. Kuigi põhimõtted on teiste rakenduste puhul sarnased, on taastamisfailid ja protseduurid, millest ma räägin, LND spetsiifilised.



### Mida ma peaksin Lightning-sõlme salvestama?



Lightning-sõlme puhul ei piisa seed päästmisest ja lootusest, et kõik taastub normaalseks. Mitmed elemendid mängivad erinevaid rolle, seega on oluline neid eristada.



#### seed (*aezeed*)



LND initsialiseerimisel saate 24-sõnalise seed. See on LND-spetsiifiline vorming, mida nimetatakse "*aezeed*". See ei ole klassikaline seed BIP39, kuigi see näeb sellele väga sarnane välja. Sellest seed-st saab LND tuletada teie Lightning-sõlmega seotud onchain wallet privaatvõtmed, st aadressid, kuhu saate vastu võtta või kuhu saate bitcoine tagasi saata pärast kanali sulgemist.



![Image](assets/fr/019.webp)



Seda seed saab seega kasutada teie sõlmega seotud wallet-ga seotud ahelas oleva wallet taasluua ja juba ahelas tagasi saadud raha tagasi saada (nt pärast kanali sulgemist). Teisest küljest ei piisa seed-st üksi teie veel avatud Lightning-kanalite taastamiseks, sest see ei sisalda vajalikku teavet teie kanalite staatuse kohta.



#### Kanali andmebaas (`channel.db`)



LND salvestab teie kanalite üksikasjaliku staatuse andmebaasi nimega `channel.db`. See andmebaas sisaldab:




- teie avatud kanalite nimekiri;
- teie eakaaslased ja nende identifikaatorid;
- iga kanali viimased commitment transaction (järjestikused olekud, mis määravad, kellele kanalis mis kuulub, ja võimaldavad probleemide korral taastada ahelas olevad vahendid);
- teave, mis on vajalik selleks, et karistada eakaaslast, kes üritab edastada vana aruannet.



Probleem selle andmebaasi puhul on see, et see muutub pidevalt: iga makse, iga marsruutimine, iga kanali avamine või sulgemine muudab selle sisu. Seetõttu on tavapärane varundamine (nt perioodiline koopia teie `channel.db`-st) ohtlik. Kui te taastate `channel.db` liiga vana versiooni ja panete sõlme selle vananenud olekuga uuesti kokku, võivad teie eakaaslased arvata, et te edastate vana kanali olekut. Sellisel juhul näeb protokoll ette karistuse: teie eakaaslane võib nõuda tagasi kogu kanali raha, nagu oleksite püüdnud petta.



Praktikas ei ole "channel.db" seega varunduskandja kui selline. See on teie sõlme elav olek. Ainus olukord, kus seda on mõttekas kasutada oma sõlme taastamiseks, on see, kui sa taastad selle andmebaasi otse masinast, mis on just välja kukkunud (nt ketas, mis on veel loetav). Sellisel juhul taastate kõige värskema oleku ja saate LND uuesti käivitada teises masinas selle andmebaasi põhjal, olles kindel, et see olek on võimalikult ajakohane, sest vana masin ei tööta enam. Teine olukord, kus see meetod võib olla asjakohane varukoopia, on kahe plaadi konfiguratsioonis, kus ühelt plaadilt teisele tehakse dünaamiline, püsiv koopia. Sellist tüüpi seadistust on aga keerulisem rakendada.



Kuid `channel.db`st perioodiliste koopiate tegemine ja nende salvestamine varukoopiana, mida saab hiljem taastada, on väga halb mõte: päeval, mil te neid kasutate, on oht, et te karistate ennast ja kaotate kogu oma sats.



#### Staatiline kanali varundamine (SCB)



Katastroofide taastamise võimaldamiseks on LND kasutusele võtnud *Static Channel Backup* (SCB) mehhanismi. See on spetsiaalne fail, mida sageli nimetatakse `channel.backup`, mis sisaldab staatilist teavet teie kanalite kohta: kes on teie kolleegid, kuidas nendega ühendust võtta ja millised on teie kanalid.



See fail ei sisalda üksikasjalikku kanali staatust ega uuenduste ajalugu. See ei võimalda teil avada kanaleid uuesti täpselt samas olekus, milles nad olid, ega jätkata selle Lightning-sõlme kasutamist. Pigem on selle roll toimida ankurduspunktina, et paluda oma eakaaslastel aidata teil kõik oma kanalid puhtalt sulgeda ja seega saada oma sats onchain, võtmetel, mida saate tänu seed-le tagasi saada. Seega, erinevalt `channel.db` failist, mida muudetakse iga makse või marsruutimisega, uuendatakse SCB faili ainult siis, kui kanal avatakse või suletakse.



SCB kaudu taastamise protsess on järgmine:




- Sa taastad oma seed (*aezeed*), mis taastab sinu Lightning-sõlmega seotud onchain wallet;
- Te esitate LND koos oma viimase SCB-ga;
- LND kasutab SCB-d, et leida teie eakaaslaste nimekiri ja kanalid, mis teil nendega on;
- See võtab ühendust iga partneriga, teatab neile, et teil on tekkinud andmekaotus, ja palub neil teie kanal nendega "sunniviisiliselt sulgeda", et saaksite taastada oma onchain-osa.



Idee on selles, et teie kolleegid, kes märkavad, et te teatate andmekaotusest, edastavad oma viimase commitment transaction ja sulgevad jõukanali. Kui need tehingud on kinnitatud, ilmuvad teie rahalised vahendid taas teie ahelaportfelli (mis on seotud seed-ga).



See taastamismehhanism ei ole siiski täiuslik. Esiteks ei taastata sellega tegelikult teie Lightning-sõlme, sest kõik kanalid suletakse. Seejärel tuleb teil luua uus Lightning-sõlm nullist. Teiseks ei garanteeri see 100% taastamist, kuigi see suurendab oluliselt tõenäosust, et probleemide korral onchaini saldod taastuvad. Tõepoolest, see taastamisprotokoll sõltub teie partnerite koostööst ja kättesaadavusest: kui üks neist on offline, on kaotanud oma andmed või keeldub koostööst, võivad teie vahendid jääda blokeerituks või isegi jäädavalt kaduma. Seepärast on oluline, et teie Lightning-sõlme kanalid ei jääks pikaks ajaks avatuks, kui teie eakaaslased ei ole kättesaadavad. Kui teil tekib sel hetkel andmekaotus ja partner jääb kättesaamatuks, on SCB kaudu taastamine võimatu ja teie vahendid jäävad kaduma, kuni see partner uuesti võrku jõuab (võib-olla igavesti).



Kokkuvõtteks võib öelda, et hea Lightning varundusstrateegia LND puhul tugineb kolmele sambale:




- Teie seed (*aezeed*), onchaini kihi jaoks;
- Usaldusväärne automaatne SCB varundamine;
- Hea kanalihaldus, valides usaldusväärsed partnerid ja sulgedes ennetavalt need, mis on sageli kättesaamatud.



### Kuidas haldab Umbrel teie LND sõlme varundamist?



Umbrel pakub LND sõlme jaoks lihtsustatud varundusmehhanismi, mis põhineb täpselt SCB-l. Idee on säästa teid selle faili enda manipuleerimisest, sellest varukoopia tegemisest ja selle protsessi automatiseerimisest nii palju kui võimalik.



Kui loote oma sõlme Umbrel, saate seed, millel on kaks rolli:




- see tuletab teie Bitcoin onchain wallet, mis on seotud teie Lightning-sõlmega;
- seda kasutatakse varukoopia identifikaatori ja krüpteerimisvõtme tuletamiseks, mida kasutatakse SCB kaugvarukoopiate tegemiseks.



Tänu sellele mehhanismile teeb Umbrel automaatselt teie SCB-st krüpteeritud varukoopia ja salvestab selle oma serveritesse Tor'i kaudu. SCB salvestatakse krüpteeritult tänu teie seed-st saadud võtmele. Nii et andmete kadumise korral tuleb teil vaid uuesti luua Bitcoin ja Lightning node Umbrel, samas või teises masinas, ning seejärel sisestada oma seed. Seejärel saate Umbrel serveritest välja laadida viimase SCB staatuse, dekrüpteerida selle ja alustada oma rahaliste vahendite taastamise protsessi.



Need varukoopiad krüpteerib teie sõlmpunkt enne saatmist lokaalselt, mis tagab teie andmete konfidentsiaalsuse: Umbrel ei saa lugeda SCB sisu. Edastamine toimub Tori kaudu, mis takistab teie IP-aadressi lekkimist. Veelgi enam, teie Umbrel lisab liiklusse müra (juhuslik polsterdus ja ebakorrapärase intervalliga saadetud valesalvestused), et server ei saaks täpselt järeldada, millal te kanalit avate või sulgete.



Selle meetodi peamine eelis on see, et see lihtsustab oluliselt teie Lightning-sõlme varundamist: te peate seed varundama ainult üks kord sõlme initsialiseerimise ajal. Sellega kaasneb küll mõningane risk, kuna tegemist on ainult SCB varundamisega, kuid mõistlike summade puhul on see vastuvõetav kompromiss.



### Parimad tavad kahjuriski piiramiseks



Isegi Umbrel varundamise korral saab mõne lihtsa hea tava abil sats kaotamise ohtu oluliselt vähendada:





- Jälgige oma kolleegide kättesaadavust:



Kui oluline kanal on sageli seotud kättesaamatu või ebastabiilse partneriga, on turvalisem see puhtalt sulgeda, kui teie sõlmpunkt veel töötab. Ennetav koostöö või sunniviisiline sulgemine kõrvaldab SCB taastamise korral võimaliku probleemiallika.





- Vältige liigse likviidsuse koondamist tundmatutele eakaaslastele:



Mida suurem kanal, mida suurem on eakaaslase suhtluskanal, seda olulisem on olla usaldusväärne. Valige tõsiseltvõetavad, hästi ühendatud ja aktiivsed sõlmed, et igasugune tulevane taastamine SCB kaudu saaks sujuvalt toimida.





- Täiendage Umbrel kohalike varukoopiatega:



Lisaks Umbrel automaatsele varundamisele võite hoida oma SCB-faili (`channel.backup`) krüpteeritud koopiat ka välisel andmekandjal ja seda perioodiliselt uuendada. Ideaalis peaksite seda uuendama iga kord, kui avate või sulgete kanali. See annab teile varunduslahenduse, kui Umbrel automaatne varundusteenus mingil põhjusel ei ole kättesaadav.





- seed õige haldamine



Teie seed Umbrel mitte ainult ei taastata teie ahelas olevat wallet, vaid tuletab ka krüpteerimisvõtme varukoopiate jaoks. Ründaja, kellel on sellele juurdepääs, võib seega käivitada taastamise ja kanda teie vahendid oma wallet-le, ilma et tal oleks isegi füüsilist juurdepääsu teie sõlmpunktile.



Seega, kui teil on vaja taastada oma sõlme, kuid teil ei ole enam seed, ei saa te midagi taastada: kogu teie sats on kadunud. Seega on väga oluline, et te salvestaksite oma seed väga hoolikalt, ainult füüsilisel andmekandjal (paberil või metallist) ja hoiaksite seda turvalises kohas. Lisateavet seed haldamise kohta leiate sellest juhendmaterjalist:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Kuidas ma salvestan oma välgussõlme Umbrel?



Nüüd, kui olete mõistnud, kuidas teooria toimib, läheme asja juurde. Klõpsake oma Lightning Node'i rakendusest (mis on tegelikult LND) kolmele väikesele punktile üleval paremas nurgas.



![Image](assets/fr/022.webp)



Varundamise jaoks on siin kolm huvipakkuvat elementi:




- Kontrollige, et valik `Automaatilised varundused` oleks lubatud. See saadab teie krüpteeritud SCB automaatselt Umbrel serveritesse.
- Seejärel saate valida, kas saata Tori või clearneti kaudu, kasutades valikut `Backup over Tor`. Nagu eelmistes punktides selgitatud, soovitan tungivalt kasutada Tor'i, et säilitada oma konfidentsiaalsus.
- Lõpuks on olemas nupp "Lae alla kanali varukoopia fail", mis võimaldab teil laadida arvutisse alla faili "channel.backup", st oma SCB krüpteeritud hetkefaili. See võimaldab teil aeg-ajalt teha täiendavaid lokaalseid varukoopiaid lisaks neile, mis saadetakse automaatselt Umbrel serveritesse.



Nüüd teate, kuidas kaitsta oma Lightning-sõlme sats andmekaotuse eest. Järgmises peatükis vaatleme, kuidas kaitsta oma sõlme petmiskatsete eest.




## Watchtower: roll ja ülesehitus


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



Lightningis põhineb iga kanal järjestikuste seisundite järjestusel, mida esindavad avaldamata commitment transaction-d. Iga Lightning-makse või marsruutimise korral loovad kanali 2 osalejat uue commitment transaction paari, mis kajastab vahendite jooksvat jaotust kanalis. Vanad commitment transaction-d muutuvad aegunuks.



Kui üks osapool avaldab aegunud seisundi, on teisel osapoolel õigus seda sanktsioneerida ja nõuda tagasi kogu kanali raha. Selles peatükis vaatame lühidalt, kuidas see mehhanism toimib, ja seejärel selgitame, kuidas luua ***watchtower***: süsteem, mis kaitseb teie Lightning-sõlme võimalike petmiskatsete eest.



### Vahitornide toimimise mõistmine


Igal hetkel on igal kanali osalisel commitment transaction, mille avaldamine võimaldaks neil kanalit sulgeda ja oma osa rahalistest vahenditest tagasi saada. Seda protsessi tuntakse kui *vajutatud sulgemist*. Kui nad aga üritaksid avaldada vanemat commitment transaction, mis vastab kanali varasemale seisundile, kus neil oli rohkem sats, siis käsitatakse seda tehingut petmiskatsena. Sellisel juhul saab vastaspool kasutada selle vanema olekuga seotud tühistamisvõtit, et saada tagasi kogu kanalis olev rahasumma, samal ajal kui pettur on ajutiselt blokeeritud ajalukuga.


See süsteem tähendab, et vana seisundi avaldamine, st pettuse katse, on väga riskantne: kui teine pool näeb seda tehingut mempoolis või plokiahelas enne ajaluku lõppemist, võib ta kasutada tühistamisvõtit ja saada tagasi kõik vahendid. **Sellest tulenevalt sõltub teie välgukanali turvalisus teie võimest tuvastada petmiskatse timelocki poolt kehtestatud ajaakna jooksul**.



#### Miks on vaatetornid vajalikud?



Karistusmehhanism toimib ainult siis, kui kannatanu on võimeline:




- jälgida iga uut Bitcoin plokki, et näha, kas kanal commitment transaction on avaldatud;
- määrata, kas see tehing vastab viimasele kehtivale või tühistatud olekule;
- tühistamise korral edastada õiguspärane tehing õigeaegselt, kasutades tühistamisvõtit, et taastada kõik vahendid enne ajaluku lõppemist.



![Image](assets/fr/023.webp)



Ideaalses stsenaariumis on teie Lightning-sõlm 24/7 võrgus, see on sünkroonitud ja jälgib pidevalt plokiahelat. Sel põhjusel suudab ta ühe käega tuvastada petmiskatse ja reageerida. Tegelikkuses võib isiklik Lightning-sõlm aga välja lülituda, eriti pikaajalise voolukatkestuse või internetiühenduse katkemise korral.



Just sellistel seisakuperioodidel muutub oht reaalseks: kui ebaaus peer avaldab vana staatuse ajal, mil teie sõlme ei ole võrgus, ja ajalukk lõpeb ilma teiepoolse reaktsioonita, muutub petmine tõhusaks. Te kaotate osa või kõik oma vahendid kanalis.



Selle riski vähendamiseks võeti kasutusele Watchtower. Valvetorn on väline teenus, mis jälgib teie nimel plokiahelat, skaneerides vana staatuse võimalikku avaldamist mõnes teie kanalis ja vajaduse korral edastab teie nimel automaatselt karistustehingu. Seega, isegi kui teie Lightning-sõlm jääb pikemaks ajaks võrguühenduseta, suudab teie kasutatav Watchtower kaitsta teie raha, jälgides kõiki petmiskatseid ja kohaldades vastavat trahvi, niipea kui ta seda avastab.



#### Kuidas vahitorn töötab



Valvetorn on loodud nii, et see minimeerib teie kanalite kohta saadavat teavet, andes samal ajal vahendid, et probleemi korral tegutseda:




- Igaks uueks kanaliseisundiks eakaaslasega valmistab teie sõlm eelnevalt ette võimaliku trahvitehingu. Kui see võrdväärne osapool petab, võimaldab see tehing teil saada tagasi kõik kanalis olevad vahendid;
- Seejärel krüpteerib teie sõlmpunkt selle trahvitehingu, kasutades vastava commitment transaction TXID-d (seda, mida kasutataks, kui pettur üritaks pettust). Niikaua, kuni ei toimu sulgemist, ei saa valvur seda tehingut dekrüpteerida, kuna ta ei tea täielikult pettustehingu TXID-d;
- Teie sõlme saadab vaatetornile paketi, mis sisaldab krüpteeritud trahvitehingut ja pool potentsiaalse pettustehingu TXID-d.



Kuna vaatlustornile edastatud TXID on mittetäielik, ei saa ta õigustoimingut dekrüpteerida. Siiski saab ta jälgida plokiahelat, et leida TXID, mis vastab talle kuuluvale osale. Kui ta tuvastab sellise tehingu, püüab ta seejärel kasutada selle tehingu täielikku TXID-d teie trahvitehingu dekrüpteerimiseks. Kui dekrüpteerimine õnnestub, teab ta, et tegemist on pettusekatsega, ja avaldab teie trahvitehingu kohe.



![Image](assets/fr/024.webp)



Seetõttu ei ole valvuril võimalik näha teie kanalite üksikasju: ei teie partnerite identiteeti, saldosid ega tehingute struktuuri. Ta näeb ainult krüpteeritud pakette. Ainus teave, mida ta saab tuletada, on teie kanalite uuendamise kiirus, sest ta saab iga uue seisundi kohta paketi, kuid ei saa teada selle sisu. Pettuse korral avastab ta kindlasti kanalite teabe, kui ta dekrüpteerib trahvitehingu, kuid vähemalt teie sats on päästetud.



See mehhanism põhineb kompromissil: te delegeerite võimaluse avaldada eelnevalt allkirjastatud trahvitehing valvurile, kuid see tehing jääb valvurile täiesti läbipaistmatuks, kuni toimub mingi pettus. Valvetorn ei saa muuta saajaid ega suunata vahendeid, sest tal on ainult juba allkirjastatud tehing, mille väljundid on teie kasuks külmutatud. Samuti ei saa ta teada kanali üksikasju seaduslikus sund- või koostöösulgemisel, kuna TXID-d ei vasta. Teisest küljest jääb watchtower minimaalselt usaldusväärseks kolmandaks osapooleks: peate lootma, et ta on võrgus ja edastab õigluse tehingu korralikult, kui seda vajate.



#### Valvetorniks saamine



Teoreetiliselt võib iga Lightning-sõlm tegutseda teiste sõlmede jaoks vaatetornina (kui nad kasutavad sama rakendust, nt LND), olles ise kaitstud teiste sõlmede poolt, mis mängivad seda rolli tema jaoks. Järgnevates praktilistes osades näitan teile, kuidas seda lihtsat mehhanismi LND-l Umbrel all sisse seada.


Sellest tulenevalt võiks huvitav strateegia olla leppida usaldusväärsete bitcoiner sõpradega kokku, et nad tegutsevad teineteise valvurina. Teie jälgite nende kanaleid ja nemad jälgivad teie kanaleid.



### Leia altruistlik vaatetorn



Kui te ei tunne kedagi enda ümber, kes võiks pakkuda valveteenust, on olemas hulk altruistlikke avalikke valveteenuseid, millega saate ühendust võtta. Näiteks selles LNP202 kursuses soovitan teil ühendada end LN+ ja Voltage ühiselt pakutava vaatetorni teenusega, mis on LND vaatetorn.


Siin on teil sisselogimise andmed:



- Tor'i kaudu:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Clearneti kaudu:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Et tänada neid selle tasuta vahitorniteenuse pakkumise eest, [saate teha annetuse välklambi kaudu](https://lightningnetwork.plus/donation).


Nüüd, kui me kasutame altruistlikku valveteenust, vaatame, kuidas seda LND sõlme Umbrel all konfigureerida.


### Valvetorni püstitamine


Rakenduses "Lightning Node" klõpsake kolmele punktile kasutajaliidese paremas ülaosas, seejärel valige "Täiustatud seaded".


![Image](assets/fr/025.webp)


Seejärel minge menüüsse "Watchtower".


![Image](assets/fr/026.webp)



Aktiveerige valik `Watchtower Client`, seejärel klõpsake nuppu `SAVE AND RESTART NODE`. Oodake, kuni LND taaskäivitub.


![Image](assets/fr/027.webp)


Kui taaskäivitamine on lõppenud, minge tagasi samasse menüüsse ja sisestage oma valitud altruistliku vaatetorni ID vastavasse lahtrisse. Seejärel klõpsake kinnitamiseks nupule `ADD`. Samuti saate reguleerida parameetrit `Watchtower Client Sweep Fee Rate`: see on tasu määr, mida olete valmis maksma võimaliku õiglustehingu eest, mida vaatetorn edastab. Ei ole vaja valida liiga kõrget määra, kuid te peaksite vältima ka liiga madalat määra, sest vastasel juhul ei kinnitata õigustoimingut õigeaegselt.


Muudatuste rakendamiseks taaskäivitage oma sõlme, kasutades nuppu `SAVE AND RESTART NODE` (Salvesta ja taaskäivita sõlme).


![Image](assets/fr/028.webp)



Kui te naasete samasse menüüsse, näete, et teie välgumihkliksõlme kaitseb nüüd just lisatud vahitorn.



![Image](assets/fr/029.webp)



Üldiselt piisab altruistlikust vahitornist, eriti kui te ei paiguta oma välgumihklile suuri summasid ja kui te haldate oma sõlme hästi (ärge jätke seda liiga kauaks välja). Veelgi suurema turvalisuse saavutamiseks võite sama protsessi kordades lisada ka mitu.



## Avage oma esimene Lightning kanal


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Kui olete jõudnud nii kaugele, siis teate juba, et Lightning-sõlm ilma kanalita on natuke nagu tühi wallet: see on küll olemas, kuid kasutu. Selleks, et saaks makseid saata või vastu võtta, peab teie sõlme olema kanaliga ühendatud vähemalt ühe teise Lightning-võrgu sõlmega. Tulevikus soovitame vastupidavuse ja marsruutimise tõhususe huvides tungivalt avada mitu kanalit. Järgnevates peatükkides vaatleme ka seda, kuidas hallata oma likviidseid varasid, optimeerida oma kanalite topoloogiat ja kasutada Umbrel-i põhilisest LND-liidesest kaugemale ulatuvaid vahendeid.



Kuid selles sissejuhatavas peatükis on eesmärk lihtsalt mõista, kuidas valida hea Lightning-peer, kust leida teavet, mida vajate oma peeride valimiseks, ja lõpuks, kuidas avada oma esimene kanal LND põhiliidese kaudu.



### Kuidas valida hea Lightning peer?



Kui avate kanali, peate valima partneri: teise Lightning-sõlme, millega teie sõlme otse kanaliga ühendatakse. See partneri valik on oluline, sest see mõjutab otseselt:




- teie maksete hõlpsam leidmine;
- teie kanalite usaldusväärsust aja jooksul;
- teie marsruutimiskulud.



Ei ole olemas sellist asja nagu täiuslik sobivus igaühe jaoks, kuid on olemas mitmeid usaldusväärseid kriteeriume heade kandidaatide tuvastamiseks.



#### 1. Sõlme ühenduvus



Hea partner on sõlmpunkt, mis on Lightning-võrguga hästi ühendatud. See ei tähenda mitte ainult suurt arvu kanaleid (kuigi see võib olla näitaja), vaid eelkõige seda, et ta on ühendatud teiste usaldusväärsete sõlmedega ja asub võrgu graafikus piisavalt kesksel kohal.



Hästi ühendatud sõlmpunkt suurendab teie võimalusi leida tõhusat marsruuti enamikku makse sihtkohtadesse. See vähendab ka vajalike vahendussõlmede arvu, mis hoiab kulud madalal.



Seevastu esimese kanali avamine isoleeritud või nõrgalt ühendatud sõlmpunktile võib piirata teie võimalusi: te suudate küll maksta sellele partnerile, kuid ülejäänud võrgule on palju raskem maksta.



#### 2. Kapitaliseerimine ja kanali läbilaskevõime



Hea eakaaslane on ka piisavalt kapitaliseeritud sõlme. Seda näitab tema kanali koguvõimsus (kõigi tema kanalite jaoks eraldatud sats summa) ja keskmine kanalivõimsus (sageli on parem, kui on vaid mõned hästi kapitaliseeritud kanalid kui paljud väikesed).



Naeruväärse võimsusega sõlmpunkt, või mille kanalid on kõik pisikesed, ei suuda suurte summadega makseid suunata, mille tulemuseks on teie jaoks marsruutimise ebaõnnestumine.



#### 3. Kulupoliitika



Iga sõlmpunkt kehtestab oma marsruutimistasud (baastasu ja tasumäär). Hea partner ei võta strateegiliste kanalite eest ülemääraseid tasusid. Esimese kanali jaoks on kõige parem valida pigem mõõdukate tasudega sõlmpunkt, et mitte oma makseid halvendada.



Pidage meeles, et teie enda marsruutimistasud mõjutavad ka seda, kuidas teised teid kui partnerit tajuvad: sõlme, mis muudab pidevalt oma tasusid või kehtestab absurdseid kulusid, hinnatakse harva.



#### 4. Stabiilsus ja staaž



Vastastikune stabiilsus on väga oluline kriteerium. Heal sõlmpunktil on kõrge kasutusaeg (ta on väga harva võrguühenduseta), ta hoiab oma kanalid kaua avatud ja ta ei ava/sulge kanalid pidevalt ilma põhjuseta.



Vanad ja endiselt aktiivsed kanalid on hea signaal: need viitavad sellele, et suhe on eakaaslase jaoks kasumlik, et sõlmpunkt oskab oma kapitali hallata ja et ta ei sulge igal ajal, nii et te ei pea pidevalt maksma onchaini tasusid sulgemise ja taasavamise eest.



Seevastu partner, kes on sageli offline või sulgeb kiiresti kanalid, võib teile probleeme tekitada ja uute kanalite avamisel lisakulusid tekitada.



Isegi nende kriteeriumide alusel ei tee te esimesel korral täiuslikku valikut. See on normaalne: eakaaslase tegelik kvaliteet selgub selle kasutamisel. Seega on oluline:




- jälgida kanali aktiivsust (suunatavad mahud, kättesaadavus jne);
- sulgeda kanalid, mis ei teeni mingit eesmärki või mille eakaaslased on liiga sageli offline;
- suunata oma kapitali aja jooksul ümber parematele eakaaslastele.



Mõte ei ole avada ja sulgeda kanaleid iga päev (mis oleks kulukas, kuna see oleks kulukas onchain-kulude osas), vaid arendada oma topoloogiat järk-järgult, et jõuda usaldusväärsete, hästi ühendatud ja teie vajadustele vastavate eakaaslaste kogumini.



### Kuidas ma leian eakaaslase?



Nende kriteeriumide kohaldamiseks on vaja vahendeid, mis võimaldavad Lightning-võrgu nähtavust. Selleks on saadaval mitu explorerit ja teenust. Tuntuimad Lightning explorerid on [1ML](https://1ml.com/) ja [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Siinkohal soovitan siiski kasutada [Lightning Labs'i Lightning Terminal'i vahendit](https://terminal.lightning.engineering/), mis annab (mööndavasti osaliselt subjektiivsetel kriteeriumidel põhineva) pingerea Lightning-sõlmede kohta, mida peetakse kanali avamiseks kõige asjakohasemaks.



![Image](assets/fr/030.webp)



Selle edetabeli tipus olevate väga suurte Lightning-sõlmede probleem on see, et enamik neist ei aktsepteeri kanalite avamisi alla väga suurte summade. Paljud rakendavad ka rangeid peer-juhtimise põhimõtteid, mis võivad viia teie kanali sulgemiseni. Teisest küljest ei ole neil sõlmedel üldiselt vajadust sissetuleva likviidsuse järele, arvestades nende ühenduste arvu.



Seepärast soovitan teil liikuda pingereas allapoole, et leida sõlme, mis on hästi ühendatud, usaldusväärne ja piisavalt keskne võrgu graafis, ilma et see oleks liiga suur. Siinkohal olen näiteks tuvastanud stacker.news'i Lightning-sõlme, mis on väga hästi ühendatud, suure võimsusega ja asub võrgu graafikus kesksel kohal.



![Image](assets/fr/031.webp)



Teine huvitav lähenemine on avada kanal sõlmpunkti, mis vajab sissetulevat likviidsust, näiteks tuttava kaupmehe, ühingu või kogukonna juurde. Sellel strateegial on kolm eelist:




- Kuna valitud üksus vajab sissetulevat likviidsust, on tal loogiliselt vähem stiimuleid teie kanalit põhjuseta sulgeda;
- Selle majandustegevus suurendab võimalusi selle kanali kaudu suunata ja seega koguda mõningaid tasusid;
- Teete ökosüsteemile teene ja annate väärtusliku panuse teistele bitcoini kasutajatele.



Kui olete asjakohase sõlme tuvastanud, saate selle sõlme ID välja otsida. See on lihtsalt sõlme avaliku võtme, eraldusjoone `@`, IP- või Tor-aadressi ja kasutatud pordi liitmine. See ID on hõlpsasti kättesaadav sõlme profiilist mis tahes Lightning Exploreris.



### Avage oma esimene kanal LND kaudu



Nüüd, kui oleme tuvastanud sõlme, millega avame oma esimese kanali, peame sats sellega lukustama. Selleks peate söötma Bitcoin onchain wallet, mis on seotud teie LND-ga.



LND põhiliidesest otsige üles oma Bitcoin Wallet, seejärel klõpsake nupul "Deposiit". Onchaini vastuvõtuaadress on siis generated: saatke sats sinna. Ülekandmisele kuuluv summa sõltub sellest, kui suur on teie esimesele kanalile eraldatav võimsus, kuid pidage meeles, et peate saatma veidi rohkem kui sihtmaht. Näiteks kui soovite avada 500 000 sats kanali, ärge saatke täpselt 500 000 sats, vaid suurema summa.



![Image](assets/fr/032.webp)



Kui tehing on edastatud, ilmub see kasutajaliidesesse. Enne kanali avamist oodake kinnitust. Kui see on kinnitatud, näete selle kõrval rohelist noolt.



![Image](assets/fr/033.webp)



Kerige põhiliidesele, seejärel klõpsake `+ OPEN CHANNEL`.



![Image](assets/fr/034.webp)



Sisestage selle sõlme "Node ID", millega soovite avada kanali, märkige summa, mida soovite lukustada, ja seejärel kohandage avamistehingu tasu vastavalt ahela tasu turu olukorrale. Loomulikult veenduge, et teil on eelnevalt piisavalt vahendeid oma LND onchaini portfellis.



Kui kõik parameetrid on määratud, klõpsake nupule "OPEN CHANNEL".



![Image](assets/fr/035.webp)



Oodake, kuni avamistehingu kinnitamine onchain. Teie esimene kanal on nüüd ametlikult töökorras: õnnitleme!



Näete, et hetkel on 100% kanali likviidsusest minu poolel: see on normaalne, sest mina olen see, kes selle kanali avas. Kui maksed ja marsruutimine arenevad, muutub see jaotus, kuid kanali koguvõimsus jääb alati samaks.



![Image](assets/fr/036.webp)



Nüüd, kui teil on olemas kanal, saate teha oma esimesed Lightning-maksed, eeldusel, et valitud sõlme on korralikult võrku ühendatud. Loomulikult vaatame hilisemates peatükkides, kuidas luua mugavam meetod Lightning-arvete maksmiseks mobiiltelefoni kaudu. Aga praegu proovime teha esimese makse otse LND-st Umbrel-le.



Selleks klõpsake jaotises `Lightning Wallet` nupule `SEND` ja kleebige seejärel seadistatav arve.



![Image](assets/fr/037.webp)



Kuvatakse arve summa. Kinnitage makse, vajutades nupule "SEND".



![Image](assets/fr/038.webp)



Kui kehtiv marsruut leitakse, peaks teie esimene välkmakse olema edukas.



![Image](assets/fr/039.webp)



Kui me siis vaatame likviidsuse jaotust kanalis, näeme, et minu eakaaslasel on nüüd 5,002 sats tema poolel. See vastab minu äsja tehtud makse 5000 sats-le, mille ta suunas saaja sõlme. Täiendavad 2 sats esindavad minu makstud marsruutimistasusid, sest saaja sai täpselt 5000 sats.



![Image](assets/fr/040.webp)



Meie maksete usaldusväärsuse parandamiseks on ilmselgelt vaja avada muid kanaleid. Sõltuvalt meie eesmärkidest peame leidma ka viisi, kuidas teha sissetulev likviidsus kättesaadavaks, et saaksime Lightning'ile makseid vastu võtta. Seda käsitletakse järgmises punktis.



# Lightning-sõlme haldamine


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Määrake oma sõlmeoperaatori profiil


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Nüüd, kui teie Lightning-sõlm on loodud ja töötab, on järgmine samm määrata oma kaupleja profiil. See on oluline valik, sest see määrab teie kanali avamise strateegia, teie eelistatavate eakaaslaste tüübi ja likviidsuse haldamise viisi.



Lightningi puhul on selle toimimiseks vaja likviidsust õiges suunas. Väljaminev likviidsus vastab teie maksevõimele (sats, mis on saadaval teie poolel kanalites). Sissetulev likviidsus vastab teie vastuvõtuvõimele (sats, mis on saadaval teie vastaspoolel). Teisisõnu, teie profiil taandub lihtsale küsimusele: kas teie sats lahkub enamasti teie sõlme või siseneb sinna?



### Tarbija



See on enamiku kasutajate profiil. Te kasutate oma sõlme Lightning-maksete tegemiseks: kaupade ja teenuste ostmiseks, arvete maksmiseks, jootraha saatmiseks - lühidalt öeldes Lightningi kui kiire maksevahendi kasutamiseks. Teisalt saate Lightningist vähe või ainult marginaalselt, näiteks mõned annetused, sõprade vahelised tagasimaksed või mõned mikromaksed.



Seda profiili on kõige lihtsam hallata, sest teie peamine vajadus on maksta. Praktiliselt tähendab see, et vajate väljaminevat likviidsust. Kui olete avanud ühe või mitu õigesti dimensioneeritud kanalit stabiilsete, hästi ühendatud sõlmedega, liigutavad teie väljaminevad maksed mehaaniliselt likviidsust teie kanalite teisele poole. Just see liikumine loob loomulikult mõistliku koguse sissetulevat likviidsust. Selle tulemusena, isegi kui te ei soovi regulaarselt saada, saate aeg-ajalt saada ilma keerulist strateegiat rakendamata. Seega ei pea te oma sissetuleva likviidsuse pärast muretsema.



Selles LNP202 kursuses keskendume sellele "tarbijasõlme" operaatoriprofiilile, kuna see vastab peaaegu kõigile Bitcoin Lightningi kasutajatele.



### Jaemüüja



Kaupmees on teatud mõttes tarbija vastand. Siin ei ole peamine eesmärk mitte maksta, vaid koguda. Ettevõtte, teenusepakkuja, veebipood või müügipunkt, mis aktsepteerib Lightningut, saab palju sissetulevaid makseid ja teeb suhteliselt vähe väljaminevaid makseid sellest sõlmpunktist.



See profiil on nõudlikum, sest välklambi maksmisest keeldumine tähendab potentsiaalselt kaotatud müüki. Seetõttu muutub prioriteet sissetulevaks likviidsuseks. Kui teie sõlmpunktis ei ole piisavalt sissetulevat likviidsust, näevad teie kliendid, et nende maksed ebaõnnestuvad, isegi kui neil on raha olemas, lihtsalt sellepärast, et puudub tee, kuidas likviidsus õiges suunas teie juurde toimetada.



Suurim väljakutse kaupmehe jaoks tuleneb ka kanalite loomulikust arengust. Kui te ainult võtate vastu, täituvad teie kanalid järk-järgult teie poolt. Seega on teil vaja mehhanisme, et säilitada ja uuendada oma sissetulevat likviidsust.



Siiski on olemas ka lihtsam juhtum: tarbija/kaupmehe segaprofiil. Kui te kogute Lightningi kaudu, kuid kulutate ka Lightningi kaudu (ärikulud, maksed tarnijatele või isegi isiklikud kulutused), siis teie väljaminevad maksed loovad loomulikult uuesti sissetulevaid makseid. Juhtimine muutub sujuvamaks, sest rahavood tasakaalustavad üksteist ja teil on vähem vajadust kasutada kunstlikke mehhanisme, mis on loodud üksnes sissetuleva likviidsuse taastamiseks.



### Marsruuter



Marsruuter on konkreetne profiil. See ei kasuta oma Lightning-sõlme maksmiseks ega kogumiseks, vaid teiste inimeste maksete suunamiseks ja tasude kogumiseks. Eesmärk on olla kasulik, usaldusväärne ja majanduslikult konkurentsivõimeline marsruut Lightningi graafikus.



Ausalt öeldes on Lightning'i ruuteriks olemine keerulisem äri, kui tundub, ja kasumlikkust on raske saavutada. Esiteks on kanalite avamine ja sulgemine kulukas onchaini kuludes. Tõhusaks marsruutimiseks peate sageli kohandama oma topoloogiat, testima, sulgema vähekasutatavaid kanaleid, avama uusi ja tasakaalustama regulaarselt oma likviidsust. Teiseks, konkurents on tihe: suured, väljakujunenud sõlmed hõivavad loomulikult suure osa liiklusest ja on raske saada jalge alla ilma märkimisväärset kapitali sidumata hästi suurtesse kanalitesse.



Samuti on kõrge kasutusnõue. Marsruudisõlm peab olema äärmiselt stabiilne, jälgitav, nõuetekohaselt varundatud ja rangelt hallatav. Te peate jälgima kanali jõudlust, kohandama oma tasupoliitikat, säilitama tasakaalustatud likviidsuse, haldama eakaaslasi ja lahendama kiiresti tehnilised probleemid. Selline tase võib olla huvitav kui tehniline hobi või panus infrastruktuuri, kuid kui teie eesmärk on lihtsalt Lightningu suveräänne kasutamine, on marsruutimisega tegelemine raha teenimise eesmärgil harva asjakohane. Seepärast ei käsitle see kursus LNP202 seda profiili põhjalikult.



### Enne edasiminekut selgeks teha oma positsioon



Kui te sobite tarbija profiiliga, on teie prioriteediks usaldusväärne ja lihtsa haldusega maksmine. Kui olete kaupmees, siis on teie prioriteediks ebaõnnestumata sularaha, mis eeldab sissetuleva likviidsuse hankimise strateegiat. Kui te kaalute marsruudi, peate lähenema sellele kui nõudlikule, majanduslikult ebakindlale ja aeganõudvale tegevusele.



Selle profiili määratlemine praegu aitab teil vältida klassikalist lõksu: rakendada kanalistrateegiat, mis on mõeldud kaupmehe või ruuteri jaoks, kui te olete lihtsalt kasutaja, kes tahab maksta.



## Lightning node manager'i kasutamine


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



Selle LNP202 koolituskursuse eelmises osas kasutasime Umbrel rakenduse `Lightning Node` põhiliidest. See kasutajaliides on piisav põhiliste toimingute jaoks (saldode kontrollimine, sularaha jaotuse vaatamine, kanalite avamine ja sulgemine), kuid see on tahtlikult väga lihtsustatud. Selline lihtsus piirab olemasolevaid võimalusi ja ei anna juurdepääsu paljudele LND sõlme täiustatud funktsioonidele. Seetõttu kasutame nüüd teist, põhjalikumat Lightning-sõlme haldustarkvara.



See lisatarkvara on lihtsalt teie sõlme täiendav haldusliides. See tähendab, et võite jätkata paralleelselt `Lightning Node` liidestuse kasutamist ja soovi korral isegi mitut erinevat liidestust kasutada. Need on lihtsalt erinevad viisid sama Lightning-sõlmega suhtlemiseks.



Tuntuimad tarkvaraprogrammid on järgmised:




- [Alby Hub] (https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub] (https://thunderhub.io/).



Kõik kolm on head lahendused. Soovi korral võite testida kõiki kolme oma sõlme, enne kui valite endale sobivaima. Mina isiklikult kasutan ThunderHub harjumusest ja sellepärast, et see tundub teistest täiuslikum. See on vahend, mida ma selles koolituskursuses tutvustan, kuid te võite valida ka ühe kahest teisest alternatiivist. Plan ₿ Academy kohta on meil iga programmi jaoks eraldi õpetus.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Paigaldage ThunderHub



Kõiki neid programme saab väga lihtsalt paigaldada Umbrel App Store'ist. Nagu ma ütlesin, kasutame siin ThunderHub, kuid kui soovite hiljem testida mõnda teist, on protseduur sarnane.



![Image](assets/fr/041.webp)



Umbrel annab teile vaikimisi parooli ThunderHub-le juurdepääsuks. Kopeerige see: te vajate seda kohe. Ärge unustage seda ka oma paroolihaldurisse salvestada, sest seda küsitakse teil iga kord, kui te tarkvara avate.



![Image](assets/fr/042.webp)



Klõpsake "Login", seejärel sisestage sisselogimiseks Umbrel poolt antud parool.



![Image](assets/fr/043.webp)



Seejärel viiakse teid ThunderHub avalehele, kus kuvatakse põhiteave teie Lightning-sõlme kohta.



![Image](assets/fr/044.webp)



Alustuseks soovitan teil aktiveerida kahefaktoriline autentimine (2FA). Klõpsake seadetes lihtsalt `Enable` kõrval `Enable 2FA`, seejärel järgige tavalist protsessi.



![Image](assets/fr/045.webp)



### Kasutage ThunderHub



ThunderHub on suhteliselt lihtne õppida. Kõik menüüd on kättesaadavad kasutajaliidese vasakpoolsest veerust. Kokkuvõtteks on siin, mida iga menüü teeb:




- home: sõlmede ülevaade, saldod ja kiirtegevused;
- armatuurlaud: kohandatav armatuurlaud koos vidinate ja mõõdikutega;
- peers: vaadata ja hallata ühendusi teiste Lightning-sõlmedega;
- kanalid": täielik kanalite haldamine (likviidsus, tasud, sulgemine jne);
- rebalance": vahend kanalite tasakaalustamiseks ringmaksete kaudu;
- tehingud: saadetud ja saadud Lightning-maksete ajalugu;
- edasi`: marsruutimisstatistika ja kulud generated oma sõlme poolt;
- "Kett": Bitcoin onchain portfell (UTXO ja tehingud);
- gW-201 integratsioon jälgimiseks ja varundamiseks;
- `Tööriistad`: täiustatud tööriistad (varukoopiad, aruanded, makaronid, allkirjad jne);
- vahetada: Boltz kaudu;
- "Statistik": üldine statistika ja Lightning-sõlme jõudlus.



Selle funktsioonikomplekti abil on teil olemas kõik vahendid, mida vajate oma Lightning-sõlme tõhusaks haldamiseks. Iga võimalust ei ole vaja kohe üksikasjalikult omandada: me tutvume nendega järk-järgult selle kursuse jooksul. Kui soovite aga tarkvara põhjalikumalt tundma õppida, vaadake meie ThunderHub õpetust:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Menüü, mis meid siin kõige rohkem huvitab, on "Kanalid". See pakub üksikasjalikku ülevaadet kõigist teie sõlme kanalitest ja nende likviidsuse jaotusest. Eelkõige näete, millised kanalid on avatud jaotises `Open`, millised ootavad avamist või sulgemist jaotises `Pending` ja millised on juba suletud jaotises `Closed`.



![Image](assets/fr/047.webp)



Teatud kanali puhul saate klõpsata partneri nimele või kanali ID-le, et avada selle Amboss leht ja saada lisateavet. Samuti saate klõpsata pliiatsi ikoonil, et muuta kanali parameetreid, sealhulgas selle kanali suhtes kohaldatavat tasupoliitikat, kui teie sõlm suunab makseid oma partneri sõlme.



![Image](assets/fr/048.webp)



Kui kasutate oma Lightning-sõlme peamiselt "tarbijana", ei pea te neid tasusid muutma: võite säilitada vaikimisi väärtused. Teisest küljest, kui soovite paremini mõista, kuidas marsruutimise tasud Lightningis toimivad, soovitan LNP 201 koolitust ja eriti peatükki 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Kui klõpsate väikesel ristil võrdväärse partneri kõrval, saate algatada kanali sulgemise. Kui märkate näiteks, et mõni partner on regulaarselt mitteaktiivne, võib olla asjakohane see kanal sulgeda, et suunata oma kapital ümber usaldusväärsemale partnerile.



Seejärel on teil kaks võimalust. Esimene ja alati eelistatavam on koostöö lõpetamine. Selle tegevuse kinnitamisega palub teie sõlmpunkt oma vastaspoolel kanal ühiselt sulgeda. Kui ta nõustub, saate te edastada ahelas toimuva sulgemistehingu ja saada tagasi oma osa vahenditest. Selle meetodi eeliseks on see, et te valite tehingu onchaini tasud, vältides seega tarbetuid kulusid, ja et vahendid saadakse kiiremini tagasi, ilma ajalokita.



![Image](assets/fr/049.webp)



Teine võimalus on sunniviisiline sulgemine. Sellisel juhul ei küsi te kolleegide nõusolekut ja edastate otse viimase teie valduses oleva commitment transaction. Ma ei soovitaks seda meetodit, välja arvatud juhul, kui see on viimane abinõu, näiteks kui partner keeldub süstemaatiliselt koostööst või ei vasta enam. Sunnitud sulgemisel on kaks peamist puudust: tasud on sageli väga kõrged, kuna need on eelnevalt kindlaks määratud, et ennetada ahelatasu tõusu, ja vahendite tagasisaamine viibib, kuna need on blokeeritud ajalukuga. See timelock annab eakaaslasele aega reageerida pettusekatse korral (mida siin ilmselgelt ei ole, kuid ootama peab siiski).



![Image](assets/fr/050.webp)



Lõpuks, uue kanali avamiseks minge menüüsse `Kodu` ja klõpsake jaotises `Liquidity` kanalit `Avada kanal`. Seejärel saate sisestada valitud sõlme ID, kanali mahu, soovitud Lightning-juhttasu ja avamistehingu onchain-tasu.



![Image](assets/fr/051.webp)



Need on peamised toimingud, mida peate ThunderHub puhul tegema. LNP202 kursuse käigus avastame ka teisi funktsioone.



## Sissetuleva likviidsuse saamine


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Nagu näete, ei ole väljuva likviidsuse omamine Lightningi maksete tegemiseks eriti keeruline. Lihtsalt avage omal algatusel kanalid teiste sõlmedega ja alustage sats saatmist. Teisalt on Lightningi maksete vastuvõtmiseks sissetuleva likviidsuse omamine keerulisem, sest teil on vaja, et teised sõlmed avaksid teile kanalid või et te ise liigutaksite likviidsust maksete tegemisega.



Kui te võtate vastu "tarbija" profiili, ei ole üldjuhul vaja muretseda sissetuleva likviidsuse pärast. Teie Lightning-sõlme kasutamine on valdavalt makse-, mitte sularahakasutuses. Tehes lihtsalt mõned Lightning-maksed, loote aja jooksul loomulikult sissetulevat likviidsust.



Teisalt, kui teil on "kaupmehe" profiil, on olukord vastupidine: te peate peamiselt koguma makseid ja tegema neid vähe. Seega ei saa te sissetuleva likviidsuse osas tugineda ainult oma maksetele. Seetõttu muutub vajalikuks, et teised Lightning-sõlmed avaksid kanalid teie juurde. Kuid kuidas seda saavutada? Kuidas panna teised operaatorid teie jaoks kapitali siduma? Just seda uurime selles peatükis.



### Sissetuleva likviidsuse ostmine



Nagu arvata võib, on kõige tõhusam viis kedagi tegutsema panna, kui talle makstakse. Lightning-sõlme sissetuleva likviidsuse puhul on põhimõte täpselt sama. Lihtsaim viis kanalite saamiseks teie sõlme on maksta teenuse ja sellega seotud kapitali sidumise eest.



Kui olete ettevõte või jaemüüja, tähendab see lähenemisviis, et saate kiiresti saada usaldusväärseid kanaleid, et koguda klientidelt makseid ilma hõõrdumisteta.



Sissetuleva likviidsuse ostmiseks on palju võimalusi. Isiklikult kasutan ja soovitan Amboss [Magma](https://magma.amboss.tech/) platvormi. Seda on väga lihtne kasutada, kanali avamine on kiire ja hinnad on üldiselt mõistlikud. Magma töötab nagu turuplats, kus on tegijad ja võtjad, kuid versioon 2 on kogemust oluliselt lihtsustanud: lihtsalt looge taotlus, makske hind Lightning'i kaudu ja Magma sobitab selle automaatselt parima võimaliku pakkumisega. Pärast kuut onchaini kinnitust on teie kanal koos sissetuleva likviidsusega käivitatud. Nii see toimib:



Mine [Magma veebilehele](https://magma.amboss.tech/buy), sektsioonis "Osta kanaleid".



![Image](assets/fr/052.webp)



Soovi korral võite luua konto oma ostude jälgimiseks, kuid see ei ole kohustuslik. Kui te ei loo kontot, annab Magma teile lihtsalt seansi ID, mis võimaldab teil hiljem oma ostud tagasi saada.



Kui olete saidil, täitke likviidsuse ostmiseks vajalikud andmed. Ühekordse ostu puhul valige "ühekordne", seejärel sisestage summa, mida olete valmis sissetuleva likviidsuse eest maksma. Mida suurem on makstud summa, seda suurem on teie sõlme jaoks avatud kanali maht. Allpool kuvatakse kanali hinnanguline võimsus: see on ligikaudne, kuna lõplik summa sõltub Magma poolt leitud parimast pakkumisest, mis on mõnikord suurem, mõnikord väiksem.



![Image](assets/fr/053.webp)



Seejärel sisestage oma sõlme ID. Selle leiate näiteks Umbrel rakenduse "Lighti Node" menüüst "Node ID".



![Image](assets/fr/054.webp)



Kui kogu teave on täidetud, klõpsake nupule "Ülevaade ja tellimus avada".



![Image](assets/fr/055.webp)



Kui te ei ole kontot loonud, annab Magma teile sessiooni võtme ja varukoopiafaili. Hoidke neid kahte elementi turvalises kohas, sest nende abil saate tellimuse hiljem tagasi võtta või selle staatust probleemide korral jälgida. Kui olete faili salvestanud, klõpsake nupule "Pay with Lightning".



![Image](assets/fr/056.webp)



Magma saadab seejärel generates välkarved teie valitud summa kohta. Te peate selle tasuma. Kui teie Lightning-sõlmes on juba kanalid olemas, võite tasuda otse sellest või kasutada mõnda muud välist Lightning wallet.



![Image](assets/fr/057.webp)



Kui makse on tehtud, kuvatakse Magma liideses, et tehing on töödeldud.



![Image](assets/fr/058.webp)



Mõne minuti pärast on taotlus töödeldud: teie Lightning-sõlme jaoks avatakse kanal sats-ga. Kui avamistehing on ahelas kinnitatud, on teil juurdepääs vastavale sissetulevale likviidsusele.



![Image](assets/fr/059.webp)



Magma on integreeritud ka otse ThunderHub-sse. Vahekaardil "Home" kerige alla jaotisele "Liquidity" ja klõpsake "Osta sissetulevat Liquidity". Kõik, mida peate tegema, on sisestada soovitud summa ja kinnitada. Te ei pea ühtegi arvet käsitsi tasuma, sest ThunderHub hoolitseb automaatselt teie sõlme maksmise eest.



![Image](assets/fr/060.webp)



Kui olete kaupmees, on seda tüüpi teenus eriti sobiv, sest see võimaldab teil saada kiiresti suure hulga sissetulevat likviidsust usaldusväärsetest sõlmpunktidest, mis tagab, et teie kliendid saavad teile raskusteta maksta. Teisest küljest, kui olete eraisik või kui te ei soovi sissetuleva likviidsuse eest maksta, on olemas ka tasuta lahendused. Vaatame lähemalt.



### Ühistegevuslik sissetulev likviidsus



Kui te ei ole kaupleja, kuid vajate siiski veidi sissetulevat likviidsust (näiteks selleks, et käivitada oma sõlme käivitamisel, kuni ootate mõningaid makseid), ei pea te selle eest tingimata maksma. Üks minu eelistatud lahendusi on teha koostööd teiste sõlmede operaatoritega, kes samuti vajavad sissetulevat likviidsust, et avada üksteisele Lightning-kanalid. Sel viisil toob kanali avamine teile väljaminevat likviidsust, pakkudes teile samal ajal tasuta (modulo onchaini tasud avamise eest) sissetulevat likviidsust.



Loomulikult saate seda korraldada ka otse bitcoin'idega. Siiski on olemas platvorm, mis on pühendatud sellisele ringide avamisele: [Lightning Network +](https://lightningnetwork.plus/). Põhimõte on, et mitte avada kaks kanalit samade inimeste vahel, vaid luua ringikujulisi avamisi, mis hõlmavad vähemalt kolme osalejat või isegi rohkem.



Võtame näite, et mõista, kuidas Lightning Network + töötab:




- Sõlmeoperaator nimega `A` avaldab teate, et ta soovib avada 1 miljoni sats kanali koos kahe teise inimesega;
- Kuulutus jääb aktiivseks kuni uute osalejate lisamiseni;
- Hiljem ühinevad kaks operaatorit, "B" ja "C", sõlme "A" teatega. Kolmnurk on nüüd valmis ja avamisfaas võib alata.
- Sõlm "A" avab kanali sõlme "B" jaoks;
- Sõlm "B" avab kanali sõlme "C" jaoks;
- Sõlm "C" avab kanali sõlme "A" juurde.



Operatsiooni lõpus on igal sõlmpunktil 1 miljon sats väljaminevat likviidsust ja 1 miljon sats sissetulevat likviidsust. Seda skeemi saab laiendada neljale või viiele osalejale.



Loomulikult ei ole olemas tehnilist mehhanismi, mis tagaks, et osaleja tõepoolest avab kanali, mille loomiseks ta on võtnud kohustuse. Seepärast on platvormil loodud mainesüsteem, mis põhineb positiivsetel hinnangutel, kui operaatorid täidavad oma kohustusi. Ja halvimal juhul, kui te satute kellegagi kokku, kes ei tee koostööd, ei ole te kaotanud raha: te olete lihtsalt jätnud kasutamata võimaluse sissetuleva likviidsuse saamiseks.



See lahendus sobib eriti hästi "tarbija" profiilile, sest see võimaldab teil saada sissetulevat likviidsust tasuta, ühendades samal ajal oma sõlme teiste väikeste operaatoritega. Teisest küljest, kui olete kaupleja, ei ole see lähenemisviis üldiselt asjakohane: iga sissetuleva likviidsuse sat nõuab väljamineva likviidsuse sat'i blokeerimist ja teie suured vajadused sissetuleva likviidsuse järele tähendaksid siis liiga suure kapitali sidumist.



Lightning Network+ kasutamiseks on teil kaks võimalust: kas kasutada Umbrel-sse integreeritud rakendust või kasutada klassikalist veebisaiti ja luua konto, logides sisse oma sõlme kaudu. Soovitan viimast, sest integreeritud rakendus ei paku kõiki olemasolevaid funktsioone.



Mine [Lightning Network +](https://lightningnetwork.plus/) veebilehele ja klõpsa kasutajaliidese paremas ülaosas olevale nupule "Login".



![Image](assets/fr/061.webp)



Enda autentimiseks peate esitatud sõnumi allkirjastama, kasutades oma Lightning-sõlme privaatvõtit. ThunderHub abil on see toiming väga lihtne. Alustage LN+ poolt kuvatud sõnumi kopeerimisest.



![Image](assets/fr/062.webp)



Mine ThunderHubs vahekaardile "Tööriistad" ja klõpsa seejärel nupule "Allkiri" sektsioonis "Sõnumid".



![Image](assets/fr/063.webp)



Sisestage LN+ poolt esitatud autentimissõnum, seejärel klõpsake nuppu "Allkirjastada".



![Image](assets/fr/064.webp)



Seejärel allkirjastab ThunderHub selle sõnumi, kasutades teie sõlme privaatvõtit. Kopeerige generated allkiri.



![Image](assets/fr/065.webp)



Sisestage see allkiri LN+ saidi vastavasse väljale ja klõpsake seejärel nuppu `Sign in`.



![Image](assets/fr/066.webp)



Te olete nüüd oma Lightning-sõlme abil ühendatud LN+-ga. See protsess võimaldab LN+ kontrollida, et te olete nende platvormil taotletava sõlme seaduslik omanik.



![Image](assets/fr/067.webp)



Soovi korral saate oma LN+ profiili isikupärastada, lisades näiteks lühikese elulookirjelduse.



Et osaleda oma esimese ringkanalite avamisel, mine kasutajaliidese ülaosas asuvasse menüüsse `Swaps`. Siit leiate kõik hetkel saadaval olevad swaps, sõltuvalt teie sõlme omadustest.



![Image](assets/fr/068.webp)



Olemasoleva vahetuspakkumisega liitumiseks klõpsake lihtsalt sellel ja registreeruge. LN+ puhul võib vahetustehingu looja siiski kehtestada osalejatele teatud tingimusi, näiteks minimaalne kanalite arv või minimaalne sõlme koguvõimsus. Seetõttu on võimalik, et eriti algusaegadel on teie sõlme jaoks vähe pakkumisi. Minu puhul ei olnud minu sõlme jaoks ühtegi pakkumist saadaval, kuigi mõned kanalid olid juba avatud. Seega lõin ma omaenda vahetuse ja te võite sama teha, kui olete samas olukorras.



Klõpsake nuppu "Start Liquidity Swap", seejärel sisestage oma pakkumise parameetrid:




- Valige osalejate koguarv (3, 4 või 5);
- Märkige avatavate kanalite arv (veenduge, et teil on vähemalt see arv oma onchain wallet-s);
- Määrake kanali lahtioleku aeg. See on ajavahemik, mille jooksul osalejad nõustuvad neid mitte sulgema;
- Paremal pool saate määrata osalejatele piiranguid: minimaalne kanalite arv, minimaalne koguvõimsus ja vastuvõetava ühenduse tüüp.



Kui kõik parameetrid on määratud, klõpsake nuppu "Start Liquidity Swap".



![Image](assets/fr/069.webp)



Teie vahetusapakkumine on nüüdseks loodud. Nüüd peate vaid ootama, et teised sõlmeoperaatorid registreeruksid. Kui teie tingimused ei ole liiga piiravad, ei tohiks see liiga kaua aega võtta. Ärge unustage jälgida oma vahetustehingu staatust järgnevate tundide või päevade jooksul.



![Image](assets/fr/070.webp)



Kõik vahetuskohad on hõivatud: nüüd liigume edasi kanali avamise faasi. Iga osaleja näeb oma LN+ kasutajaliidesest, millise sõlme jaoks ta peab avama välkekanali.



![Image](assets/fr/084.webp)



Avage kanal, kasutades LN+ poolt antud sõlme ID-d ja järgides näidatud summat. Nagu eelmistes peatükkides nägime, saate seda teha kas ThunderHub kaudu, mõne teise Lightning-sõlme haldajaga või otse Lightning-sõlme põhirakenduse liidesest.



![Image](assets/fr/085.webp)



Kui avamine on käivitatud, näete seda ootavate kanalite sektsioonis. Minu puhul on see kanal, mille sõlme `Plebian_fr`.



![Image](assets/fr/086.webp)



Seejärel saate naasta LN+-sse, et kinnitada, et olete algatanud kanali avamise. Vajutage lihtsalt nupule `Kanali avamine algas`.



![Image](assets/fr/087.webp)



Kui kõik teised osalejad on samuti avanud kanali, millele nad on pühendunud, ärge unustage jätta neile positiivne hinnang.



![Image](assets/fr/088.webp)



Raskuste või viivituste korral võite võtta otse ühendust oma kolleegidega lehe allosas oleva kommentaaride sektsiooni kaudu.



![Image](assets/fr/089.webp)



Mõned osalejad võivad soovida tasakaalustada ringkanalid algusest peale, tehes makseid endale. See tagab raha tasakaalustatud jaotuse igas kanalis. Kui olete "tarbija" profiilis, ei ole see oluline, kuid võite seda tasakaalustamist soovi korral kas ise teha või seada oma kanali tasud ajutiselt nulliks, et lihtsustada seda sooviva kaaslase jaoks. Mõnikord ei taha keegi seda teha.



![Image](assets/fr/090.webp)




# Lightning-sõlme potentsiaali vallandamine


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Mobiilse wallet ühendamine Tailscale kaudu


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



See ongi kõik, teil on nüüd hästi ühendatud Lightning-sõlm, millel on nii sissetulev kui ka väljaminev likviidsus. Seega olete valmis oma Lightning-sõlme reaalselt kasutama. Siiani oleme alati kasutanud liidesed otse Umbrel, kas `Lightning Node` rakendus või `ThunderHub` liides. Need vahendid töötavad maksete saatmiseks ja vastuvõtmiseks, kuid ei ole selgelt optimeeritud igapäevaste Lightning-maksete jaoks. Kasutajaliides on mõeldud kasutamiseks arvutis, nutitelefonis ebapraktiline ja nõuab ka nõuetekohaseks toimimiseks ühendust sama võrguga (kuigi tehniliselt on võimalik ühendust luua ka eemalt Tor'i kaudu).



Tegelikkuses otsime me bitcoin'i kasutajatena klassikalist Lightning wallet kasutajaliidest nutitelefonis: võimalust skaneerida arveid QR-koodi abil ning lihtsat kasutajaliidest sats maksmiseks ja väljamaksmiseks. Just seda me selles ja järgmises peatükis ka rakendame. Üldine idee on, et teie nutitelefonis on mobiilne Lightning wallet rakendus, mida saab kasutada ükskõik kust (mitte ainult kohalikust võrgust), kuid mis tugineb taustal maksete saatmiseks ja vastuvõtmiseks teie enda Lightning-sõlmele.



### Millised on lahendused mobiilse kliendi ühendamiseks?



Tänapäeval on selleks mitmeid võimalusi nii mobiilirakenduse kui ka teie sõlme ja selle rakenduse vahelise ühenduse tüübi osas. Kolm peamist ühendusviisi on järgmised:




- ***Tor*** kaudu;
- vPN-i kaudu ***Tailscale***;
- ***Nostr Wallet Connect*** kaudu.



Mõned aastad tagasi kasutasin ***Tor*** kaudu ühendust, kuid lõpetasin selle kiiresti: ebaõnnestumiste arv ja kommunikatsiooniviivitused olid liiga suured. Teoreetiliselt see toimib, kuid praktikas oli kasutajakogemus katastroofiline. Seepärast soovitan ma seda lähenemisviisi mitte kasutada.



Alternatiiv, mille ma siis kasutusele võtsin, oli kasutada ***Tailscale*** VPN-i, et tagada side mobiilirakenduse ja sõlme vahel. See lahendus töötab väga hästi: isegi madala läbilaskevõimega mobiilsidevõrkudes lähevad minu maksed alati probleemideta läbi. Seda meetodit tutvustan käesolevas peatükis esimesena Zeus'i rakendusega.



Järgmises peatükis vaatleme teist, uuemat lahendust, mis samuti väga hästi töötab: ***Nostr Wallet Connect***. Seekord kasutame Alby Go rakendust, et tutvustada teile alternatiivi, kuigi Zeus ühildub soovi korral ka NWC-ga.



### Tailscale paigaldamine ja konfigureerimine



Selle esimese meetodi jaoks vajame Tailscale. See on WireGuard-l põhinev VPN-lahendus, mis võimaldab teil turvaliselt ühendada üle interneti hajutatud seadmeid, hallates samal ajal automaatselt krüpteerimist, autentimist ja NAT-i ületamist. Lihtsustatult öeldes on see nii, nagu oleksid kõik teie seadmed ühendatud samasse LAN-i kui teie ruuter, kuigi nad võivad olla ükskõik kus Internetis.



Selle kasutamiseks looge kõigepealt konto. Mine Tailscale veebisaidile, seejärel klõpsa nupule "Alusta".



![Image](assets/fr/071.webp)



Seejärel valige oma Tailscale konto jaoks identiteedi pakkuja. Mina isiklikult kasutasin sisselogimiseks ühte oma GitHubi kontot.



![Image](assets/fr/072.webp)



Kui olete sisse loginud, esitatakse teile mõned küsimused teie kasutuse kohta. Jätkamiseks vastake neile lühidalt.



![Image](assets/fr/073.webp)



Tailscale pakub seejärel kliendi installimist teie masinasse. Hetkel ei ole see see, mis meid huvitab: minge otse Umbrel ja installige Tailscale rakendus App Store'ist.



![Image](assets/fr/074.webp)



Kui rakendus avaneb, klõpsake nupule "Logi sisse", seejärel järgige autentimisprotsessi, kasutades sama meetodit, mida kasutasite konto loomisel.



![Image](assets/fr/075.webp)



Kinnitamiseks klõpsake nuppu "Ühenda". Teie Umbrel on nüüd ühendatud teie VPN-võrku.



![Image](assets/fr/076.webp)



Seejärel laadige Tailscale rakendus oma nutitelefoni ja logige sisse sama kontot kasutades. Pange tähele: Androidi puhul ei ole võimalik kasutada kahte VPN-i samaaegselt. Selleks, et Tailscale töötaks, peate keelama kõik teised aktiivsed VPN-id. Veelgi enam, iga kord, kui soovite oma Lightning-sõlme Zeuse kaudu kasutada, peate Tailscale VPN-i aktiveerima, vastasel juhul ühendus ei teki.



![Image](assets/fr/077.webp)



Nüüd, kui Tailscale saidil on vähemalt kaks klienti ühendatud, saate juurdepääsu halduskonsoolile, kus on nimekiri kõigist teie võrku ühendatud seadmetest ja nende Tailscale IP-aadressidest.



![Image](assets/fr/078.webp)



### Ühenda Zeus



Paigaldage Zeuse rakendus oma telefoni. Kui see avaneb, valige "Täiustatud seadistused" ja seejärel "Loo või ühenda wallet".



![Image](assets/fr/079.webp)



Jaotises "Wallet liides" valige "LND (REST)". Seejärel sisestage oma Tailscale aadress, mille leiate Tailscale armatuurlaualt või otse Umbrel rakendusest Tailscale. Pordi jaoks sisestage `8080`.



![Image](assets/fr/080.webp)



Seejärel palub Zeus teil anda "makroon". See on autoriseerimise token, mis võimaldab teil täpselt määratleda rakendusele (antud juhul Zeusile) antud õigused teie Lightning-sõlmega suhtlemiseks. On võimalik generate makaroon ThunderHub menüüst `Tööriistad`, `Bakeri` alammenüüst, kuid selleks otstarbeks on kõige lihtsam viis seda saada otse `Lightning Node` rakendusest.



Klõpsake kolmel väikesel punktil liidese paremas ülaosas, seejärel klõpsake nupul "Ühenda Wallet". Valige `REST (kohalik võrk)`. Seejärel saate vastavate õigustega makarone kopeerida.



![Image](assets/fr/081.webp)



Sisestage see Zeuse vastavasse lahtrisse, seejärel klõpsake nupule `SAVE WALLET CONFIG`.



![Image](assets/fr/082.webp)



Nüüd saate oma Lightning-sõlme Zeuse rakendusest kasutada. See tähendab, et saate generate arveid saada makseid otse oma Lightning-sõlme nutitelefonist ning samuti tasuda Lightning-arveid, olenemata sellest, kus te parasjagu viibite.



![Image](assets/fr/083.webp)



Vihje: Tailscale ei ole piiratud Lightning-sõlme kaugkasutamisega. See võimaldab teil kasutada kõiki teie Umbrel tööriistu ka teistest tarkvaradest, isegi eemalt. Näiteks saate kasutada Tailscale IP-aadressi oma Umbrel-sõlme Bitcoin ühendamiseks (Electrs või Fulcrumi kaudu) Sparrow Wallet-sõlmega, ilma Tor'i kaudu minemata. Sellega välditakse jällegi Torile omast aeglust. Lihtsalt installige Tailscale klient oma arvutisse ja ühendage see oma võrku.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

Järgmises peatükis vaatleme teist, sama tõhusat viisi, kuidas ühendada mobiilne klient teie Lightning-sõlmega: Nostr Wallet Connect. Me kasutame Zeusist erinevat rakendust (kuigi Zeus ühildub ka NWC-ga), nimelt Alby Go.



## Mobiilse wallet ühendamine NWC kaudu


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Kui Tailscale ühendus teid ei veena või kui kahekordse VPN-i haldamine tundub liiga tülikas, pakutakse selles peatükis välja teine võimalus kasutada kaugmobiiliklienti, et tasuda ja saada sats oma Lightning-sõlme kaudu: ***Nostr Wallet Connect***.



Selles näites kasutame Alby Go mobiilirakendust, mis on väga hästi kujundatud ja eriti kergesti õpitav. Sellegipoolest võite kasutada ka Zeust või mõnda muud NWC-ga ühilduvat mobiilirakendust. Ühilduvate rakenduste loetelu leiate [`awesome-nwc` GitHubi repositooriumist](https://github.com/getAlby/awesome-nwc).



### Kuidas Nostr Wallet Connect töötab?



Nostr Wallet Connect on standardiseeritud protokoll, mis võimaldab rakendusel või veebisaidil käivitada tegevusi kauges Lightning-sõlmes, ilma et oleks vaja luua selle sõlmega otsest võrguühendust (ei mingit API LND, mis oleks avatud, ei mingit VPN-i, ei mingit `.onion` teenust...). NWC määratleb, kuidas rakendus sõnastab kavatsuse (nt `pay_intece`) ja saab tulemuse.



See toimib üsna lihtsalt. Sessioon käivitatakse QR-koodi skaneerimisega või süvalingiga `nostr+walletconnect:`. See string sisaldab seansi parameetreid ja autoriseerimissaladust. Seejärel, kui rakendus soovib maksta, seeriaviisib ta taotluse, krüpteerib selle ja avaldab selle sündmuse kujul Nostr relees. Sõlm loeb sündmust relees, dekrüpteerib selle, kontrollib, et autor on selle seansi jaoks autoriseeritud, teostab makse ja tagastab seejärel krüpteeritud vastuse (edu koos eelkuvandiga või viga). Relee toimib ainult transpordi vahendajana: ta ei saa lugeda sisu, kuid ta saab jälgida päringute ajastust ja sagedust.



Võrreldes Tailscale või Tori kaudu loodud ühendusega on NWC peamine eelis see, et teie sõlme ei saa väljastpoolt otse kätte. See lihtsustab oluliselt mobiilset kasutamist: teie sõlmpunkt ei pea vastu võtma sissetulevaid ühendusi, ta peab lihtsalt suutma suhelda releega. Teisest küljest kehtestate funktsionaalse sõltuvuse Nostr releedest: kui need ei ole kättesaadavad, siis kogemus halveneb. Samuti, isegi kui sõnumid on krüpteeritud, võib relee jälgida teatud tasemel tegevuse metaandmeid.



Oluline on ka turvamudelite erinevus. Tailscale või Toriga avate otsese juurdepääsu oma sõlmpunktile (API või LND kaudu), mis on kaitstud väga tundlike saladustega. See on võimas, sest saate kõike hallata, kuid see on ka madalama tasandi rünnakupind. NWC puhul on juurdepääs rakenduslikum: te delegeerite sessiooni token, mis lubab ainult teatud tegevusi.



### Paigaldage Alby Hub oma Lightning-sõlme



Varem oli Umbrel App Store'is spetsiaalselt NWC-ühendustele pühendatud rakendus, kuid kahjuks ei ole see enam saadaval. Nüüd peate seda tüüpi ühenduse loomiseks kasutama Alby Hub. Selleks alustage Alby Hub rakenduse installimisega otse poest.



![Image](assets/fr/091.webp)



Avamisel jätke sissejuhatavad ekraanid vahele, seejärel klõpsake nupule "Alusta (LND)". Oluline on kontrollida, et sulgudes oleks kirjas `LND`, mitte `LDK`. Kui kuvatakse `LND`, tähendab see, et Alby Hub on teie olemasoleva Lightning-sõlme õigesti tuvastanud ja konfigureerib end selle liideseks. Kui aga kuvatakse `LDK`, siis tähendab see, et Alby Hub ei ole teie sõlme tuvastanud ja kavatseb luua uue sõlme, mis ei ole siinkohal eesmärk.



![Image](assets/fr/092.webp)



Seejärel palutakse teil luua Alby konto. NWC-ga piiratud kasutamiseks ei ole see vajalik, kuid kui soovite kasutada Alby eriteenuseid, võite seda teha. Kui mitte, klõpsake jätkamiseks nuppu "Võib-olla hiljem".



![Image](assets/fr/093.webp)



Seejärel valige tugev ja ainulaadne parool. See kaitseb teie sõlme Alby Hub juurdepääsu. Ärge unustage seda oma paroolihaldurisse salvestada.



![Image](assets/fr/094.webp)



See viib teid Alby Hub liidese juurde. Te ei pea kogu konfigureerimisprotsessi läbi tegema, välja arvatud juhul, kui soovite seda kasutada oma Lightning-sõlme põhihaldurina. Nagu me varem nägime, võib Alby Hub tegelikult asendada ThunderHub kasutamist teie sõlme haldamiseks. Kui soovite Alby Hub võimaluste kohta rohkem teada saada, vaadake meie spetsiaalset õpetust:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Mine menüüsse "Ühendused".



![Image](assets/fr/095.webp)



Siin näete kõiki rakendusi, mis saavad teie Lightning-sõlme NWC kaudu ühendada. Nende hulka kuulub ka Zeus, mida juba mainiti eelmises peatükis. Siinkohal kasutame Alby Go. Klõpsake Alby Go-l, seejärel nupul `Connect to Alby Go`, et alustada ühendamisprotsessi.



![Image](assets/fr/096.webp)



### Alby Go paigaldamine ja ühendamine



Installeerige nutitelefoni rakendus Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



Konfigureerige Alby Hub-süsteemis õigused, mida soovite oma Lightning-sõlme Alby Go rakendusele anda. Võite näiteks määrata kulutuste piirangud perioodi kohta, NWC-ühenduse aegumise kuupäeva või jätta täieliku kontrolli. Kui olete parameetrid seadistanud, klõpsake nupule `Next`.



![Image](assets/fr/097.webp)



Alby Hub saadab seejärel generatei QR-koodi, et luua NWC-ühendus teie Lightning-sõlme ja Alby Goi vahel.



![Image](assets/fr/098.webp)



Alby Go rakenduses klõpsake esimesel avamisel nupule "Ühenda Wallet", seejärel skannige Alby Hub esitatud QR-koodi.



![Image](assets/fr/099.webp)



Valige selle wallet identifitseerimiseks nimi. Nüüd on teil Alby Go kaudu kaugjuurdepääs oma Lightning-sõlmele. Te saate generate arveid vastu võtta sats oma sõlme või määrata Lightning arveid otse sellega.



![Image](assets/fr/100.webp)



Näiteks saatsin 1543 sats Alby Go liidesest.



![Image](assets/fr/101.webp)



Kui ma lähen oma Umbrel Lightning-sõlme põhiliidesesse, näen, et minu sõlme poolt on see makse tõepoolest tehtud.



![Image](assets/fr/102.webp)



Nüüd teate, kuidas oma Lightning-sõlme hõlpsasti kõikjalt kasutada.



## Pikaajaline autonoomia Lightningil


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Oleme nüüd jõudnud selle LNP202 praktilise kursuse lõpuni. Teil on nüüd Lightning Network suveräänseks kasutamiseks vajalikud põhitõed: te mõistate sõlme tegelikku rolli, erinevate lähenemisviiside kompromissid ning olete LND instantsi Umbrel-l koos järjepideva varundus- ja kaitsestrateegiaga seadistanud. Samuti olete avanud oma esimesed kanalid, õppinud, kuidas hallata likviidsust, et muuta oma maksed igapäevaselt usaldusväärseks.



Operatiivsest vaatenurgast peaks teie sõlmpunkt nüüd sisenema hooldusrütmi. Peamine on jälgida seda (tööaeg, sünkroniseerimine, kanalite olek, maksehäired jne), rakendada Umbrel pakutavaid uuendusi, kui stabiilsed versioonid on saadaval, ning kontrollida perioodiliselt, kas teie varukoopiad ja valvekorraldused on endiselt aktiivsed.



Kui tegemist on kanalitega, kasutage pragmaatilist lähenemist: hoidke need, mis on teile kasulikud, sulgege need, mis on püsivalt mitteaktiivsed või seotud ebastabiilsete eakaaslastega, ja suunake oma kapital järk-järgult ümber tugevama topoloogia suunas.



**Üks kõige tavalisem lõks selles etapis on liiga suure kapitali eraldamine oma välgussõlme jaoks. Pidage meeles, et teie Lightning-sõlm on palju vähem turvaline kui riistvaraline wallet ja et teie kanalitele eraldatud vahendite kättesaadavus sõltub varamehhanismidest, mis jäävad ebatäiuslikuks. Seetõttu on väga oluline hoida mõistlikke summasid, mille kaotamist probleemide korral saate endale lubada, ja hoida alati enamus oma sats-i riistvaralises wallet-s.



Mis puutub vahenditesse, siis soovitan teil jääda uudishimulikuks ja tähelepanelikuks uute arengute suhtes. Sellel koolitusel avastasime mitmeid neist, kas oma sõlme haldamiseks, selle ühenduvuseks või maksete tegemiseks kaugkasutamiseks. Lightning on aga eriti dünaamiline valdkond. Igal aastal ilmub uusi ja asjakohaseid vahendeid ning ka Umbrel-le ilmub palju uusi rakendusi. Nende uute arengutega kursis olemine võib võimaldada teil avastada võimsamaid või praktilisemaid lahendusi, kui need, mida selles kursuses tutvustatakse.



Mis puutub haridusse, siis kui te pole seda veel teinud, siis soovitan teil tungivalt läbida Fanis Michalakise LNP 201 teooria kursus, mis on pühendatud Lightning Network käitamisele. See aitab teil paremini mõista selles LNP202 kursuses tehtavaid manipulatsioone ja annab teile suurema kindlustunde oma sõlme igapäevases juhtimises.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Erinevalt, kuid bitcoini teekonna jaoks sama oluline, soovitan ka Ludovic Lars'i suurepärast kursust Bitcoin loomise ajaloost.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Kuid enne edasiliikumist võite kirjutada selle LNP202 kursuse kohta ülevaate ja muidugi võtta diplomi, et kinnitada, et olete kogu selle sisust aru saanud.



# Viimane osa


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Arvamused ja hinnangud


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Lõpueksam


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Kokkuvõte


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>