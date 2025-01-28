---
name: Alby Hub
description: Kuidas käivitada oma Lightning-sõlme lihtsalt?
---
![cover](assets/cover.webp)

Alby Hub on populaarse veebipikenduse Lightning taga oleva ettevõtte Alby uusim tarkvara. Alby Hub on lihtne kasutajaliides Lightning-sõlmede haldamiseks.

Selles õpetuses vaatleme erinevaid võimalusi, kuidas kasutada Alby Hubi oma Lightning-sõlme haldamiseks ja kuidas ühendada see Alby Go, Alby mobiilirakendusega. See võimaldab teil oma sati liikvel olles oma sõlme iseseisvalt hallata.

![ALBY HUB](assets/fr/01.webp)

## Mis on Alby Hub?

Aastal 2024 tähistas Alby strateegilist muutust. Aastaid on nad pakkunud mitmesuguseid vahendeid, mis on seotud Bitcoini ja Lightning Networkiga, sealhulgas ikoonilist Alby laiendust, mis võimaldab teil kasutada Lightningi rahakotti, hoiustatud või muul viisil. Kuid 2025. aastal kavatsevad nad lõpetada oma jagatud hoiustatava rahakoti teenuse ja keskenduda ainult ise hoiustavatele lahendustele. Alby Hubist saab Alby ökosüsteemi uus lipulaev. See tarkvara võimaldab kasutajatel hõlpsasti hallata oma Lightning-sõlme, säilitades samal ajal oma võtmete omandiõiguse (self-custody).

Alby Hub on väga kohandatav vahend. See vastab nii algajate kui ka edasijõudnute vajadustele. Algajad kasutavad seda, et hõlpsasti juhtida tõelist Lightning-sõlme iseseisvalt, ilma et nad peaksid tegelema selle aluseks oleva keerukusega. Kogenumate kasutajate jaoks saab Alby Hubi kasutada olemasoleva Lightning-sõlme täiustatud haldamiseks täieliku kasutajaliidesena.

Sõltuvalt teie vajadustest on Alby Hub saadaval 4 konfiguratsioonis:


- Alby Hub Cloud :**

See esimene võimalus on ideaalne algajatele, see on Alby pilvevõimalus. See võimaldab teil võtta Lightning-sõlme kasutusele otse Alby hallatavas serveris, millele pääseb ligi Alby Hubi liidese kaudu. Kuigi Alby haldab serverit, säilitate oma rahaliste vahendite üle suveräänsuse, sest teie võtmed on krüpteeritud ainult teile teadaoleva parooliga. Siiski peavad teie võtmed jääma sõlme tööks lahti krüpteeritud RAM-i, mis teoreetiliselt seab need ohtu, kui keegi pääseb füüsiliselt serverile ligi. See on huvitav kompromiss algajatele, kuid on oluline olla teadlik riskidest.

Selle võimaluse peamine eelis on see, et saate Lightning-sõlme, mis töötab 24/7, ilma et peaksite ise haldama hostingut. Lisaks on Lightning-sõlme varukoopiad lihtsustatud ja automatiseeritud, võrreldes isehostitud võimalustega, kus peate ise haldama kanali varukoopiaid.

Alby pakub seda teenust 21 000 sati eest kuus (detsembri 2024. aasta hind, mis võib muutuda [vaadake nende hinnakujundust](https://albyhub.com/#pricing)). Tasu arvatakse automaatselt maha teie sõlmpunktist Alby poolt väljastatud Lightning arve kaudu. See toimub NWC-ühenduse kaudu, mis konfigureerib teie sõlme nii, et see maksab automaatselt Alby tellimusega seotud arveid.


- Alby Hub koos olemasoleva sõlmpunktiga :**

Kui teil on juba olemas sõlme hostimine, näiteks Umbrel või Start9, saab Alby Hubi kasutada täiustatud haldusliidesena samamoodi nagu ThunderHubi või RTLi.


- Alby Hub kohalik :**

Samuti on võimalik paigaldada Alby Hub ja oma sõlme otse arvutisse, kuigi see võimalus on vähem praktiline, sest arvuti peab Lightning-sõlme kaugjuurdepääsuks olema kogu aeg aktiivne. See alternatiiv võib siiski sobida teie konkreetsete vajaduste jaoks.


- Alby Hub isiklikul serveril :**

Edasijõudnud kasutajate jaoks saab Alby Hubi võtta kasutusele isiklikus serveris lihtsa käsuga. Seda võimalust ei käsitleta selles õpetuses, kuid te leiate spetsiaalsed juhised [Alby GitHubis](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

See õpetus keskendub peamiselt kasutajaliidesele, mis on sama, olenemata valitud valikust. Vaatame ka seda, kuidas Alby Hubi kasutusele võtta tasulise pilvevõimalusega, seejärel node-in-box-variandiga (Umbrel või Start9).

![ALBY HUB](assets/fr/02.webp)

Kohaliku paigaldamise korral arvutisse [laadige alla ja installige tarkvara vastavalt oma operatsioonisüsteemile](https://github.com/getAlby/hub/releases), seejärel järgige samu juhiseid kasutajaliideses.

![ALBY HUB](assets/fr/03.webp)

## Loo Alby konto

Esimene samm on luua Alby konto. Kuigi see ei ole Alby Hubi kasutamiseks hädavajalik, võimaldab see teil kasutada kõiki olemasolevaid võimalusi, sealhulgas võimalust saada Lightning-aadress.

Mine [Alby ametlikule veebisaidile](https://getalby.com/) ja klõpsa nupule "*Loo konto*".

![ALBY HUB](assets/fr/04.webp)

Sisestage hüüdnimi ja e-posti aadress, seejärel klõpsake "*Sign up*". Seda e-posti aadressi kasutatakse hiljem teie kontole sisselogimiseks.

![ALBY HUB](assets/fr/05.webp)

Sisestage e-kirjaga saadud kinnituskood.

![ALBY HUB](assets/fr/06.webp)

Kui olete oma veebikontole sisse loginud, klõpsake nupule "*Jätka*".

![ALBY HUB](assets/fr/07.webp)

Klõpsake uuesti "*Jätka*".

![ALBY HUB](assets/fr/08.webp)

## Pilvehostingu võimalus

Seejärel peate valima kas isehostitava variandi, mille puhul majutate Lightning-sõlme oma riistvaral, või tasulise variandi, mille puhul kasutate Alby pilve. Alustan selgitades, kuidas toimida pilvevariandi puhul (pange tähele, et see on tasuline variant, vt üksikasju eelmises jaotises).

Klõpsake nuppu "*Upgrade*".

![ALBY HUB](assets/fr/09.webp)

Kinnitage, klõpsates nupule "*Tellige nüüd*".

![ALBY HUB](assets/fr/10.webp)

Klõpsake nupule "*Launch Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Oodake mõned hetked, kuni teie sõlme luuakse.

![ALBY HUB](assets/fr/12.webp)

Ja see ongi kõik, teie Alby Hub on nüüd seadistatud. Järgmises jaotises näitan teile, kuidas paigaldada Alby Hub olemasolevale sõlmpunktile. Kui teil ei ole seda vaja, võite hüpata järgmise jaotise juurde, et oma sõlme konfigureerida.

![ALBY HUB](assets/fr/13.webp)

## Self-hosting võimalus

Kui eelistate kasutada Alby Hubi olemasoleva Lightning-sõlme liidesena, on teil mitu võimalust: paigaldage see serverisse, lokaalselt oma arvutisse või node-in-boxi (Umbrel või Start9) kaudu. Alby Hubi kasutamine nendes konfiguratsioonides on tasuta. Keskendume node-in-boxi võimalusele, sest minu arvates kujutab servervõimalus ilma füüsilise juurdepääsuta endast sarnaseid riske nagu pilveversioon ja lokaalne paigaldus arvutisse on sageli ebasobiv.

Selle seadistamiseks Umbrelil (sammud Start9 puhul on identsed), peab teil kõigepealt olema juba konfigureeritud LND-sõlm.

Logige sisse oma Umbreli kasutajaliidesesse ja minge rakenduste poodi.

![ALBY HUB](assets/fr/14.webp)

Otsige rakendust "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Paigaldage see oma sõlme.

![ALBY HUB](assets/fr/16.webp)

Teie Alby Hubi kasutajaliides on nüüd valmis. Te võite järgida ülejäänud õpetust nii, nagu kasutaksite pilviliidest, kuid ilma tasulise versiooni võimalusteta. Veelgi enam, erinevalt pilveversioonist hoitakse teie võtmeid lokaalselt teie sõlmes, mitte Alby serverites.

![ALBY HUB](assets/fr/17.webp)

## Alby Hubi käivitamine

Vajutage nupule "*Alusta*".

![ALBY HUB](assets/fr/18.webp)

Seejärel palub Alby Hub teil valida parool. See parool on väga oluline, sest seda kasutatakse teie rahakoti krüpteerimiseks. Tasulises pilveversioonis salvestatakse teie võtmed Alby serveris, krüpteeritakse selle parooliga, mida teate ainult teie, seejärel dekrüpteeritakse ja salvestatakse ainult RAM-i, et vajadusel tehinguid allkirjastada.

Seetõttu on oluline valida tugev parool. Igaüks, kes seda salasõna kasutab, võib potentsiaalselt saada juurdepääsu teie sõlmpunktile. Tehke kindlasti ka üks või mitu füüsilist varukoopiat sellest paroolist paberile või veel parem, kui see on metalltükil, et suurendada turvalisust. **Kui kaotate selle parooli, on võimatu taastada ligipääsu oma bitcoinidele**, kuna Alby ei saa seda kuidagi taastada. Selle salasõna kaotamine tähendab teie bitcoinide kaotamist.

Kui olete hoolikalt valinud ja salvestanud oma salasõna, klõpsake "*Loo salasõna*".

![ALBY HUB](assets/fr/19.webp)

Nüüd on teil juurdepääs oma Lightning-sõlmele.

![ALBY HUB](assets/fr/20.webp)

Esimene toiming, mida tuleb teha, on salvestada oma taastamisfraas, millest teie võtmed on tuletatud. See fraas võimaldab teil taastada juurdepääsu oma onchaini rahakotile ja, koos oma kanalite viimase seisuga, oma satsidele Lightningis. Selleks klõpsake nupule "*Settings*".

![ALBY HUB](assets/fr/21.webp)

Seejärel minge vahekaardile "*Backup*". Sisestage oma parool, et sellele ligi pääseda.

![ALBY HUB](assets/fr/22.webp)

Seejärel saate juurdepääsu oma 12-sõnalisele taastumisfraasile. Tehke sellest fraasist üks või mitu füüsilist varukoopiat paberile või metallile ja hoidke seda turvalises kohas.

![ALBY HUB](assets/fr/23.webp)

Kui olete fraasi salvestanud, kontrollige ruutu, et kinnitada selle salvestamist, ja vajutage "*Jätka*".

![ALBY HUB](assets/fr/24.webp)

## Kuidas saan taastada juurdepääsu oma bitcoinidele?

Enne raha saatmist oma sõlmpunkti on oluline mõista, kuidas neid probleemide korral tagasi saada ja milliseid andmeid on selleks vaja. Protsess varieerub sõltuvalt taastatavate vahendite laadist ja teie sõlme hostimisviisist.

Tasuliste pilveteenuste kasutajate jaoks on bitcoinide täielikuks taastamiseks vaja kolme olulist elementi:


- Teie taastumisfraas;
- Teie parool (mida kasutatakse teie sõlme jaoks) ;
- Juurdepääs oma Alby kontole, et saada teada oma Lightning-kanalite uusim staatus.

Nende 3 teabe puudumise korral oleks teie bitcoinide täielik tagasisaamine võimatu.

Nende puhul, kes majutavad oma sõlme, on taastamisprotsess identne mis tahes Lightning-sõlme taastamisprotsessiga. Teil on vaja :


- Teie taastumisfraas;
- Teie Lightning-kanalite viimane staatus. Selle teabe kaitsmiseks pakub Umbrel [võimalust](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) selle krüpteerimiseks ja dünaamiliseks ja anonüümseks salvestamiseks Tor'i kaudu.

## Osta oma esimene Lightning kanal

Nüüd saate järgida Alby Hubi juhiseid. Vajutage nupule, et avada oma esimene kanal sissetuleva sularaha jaoks.

![ALBY HUB](assets/fr/25.webp)

Valige "*Open Channel*". Kui te ei kavatse saada marsruudisõlme ja ei vaja seda konkreetselt, siis soovitan valida privaatseid kanaleid.

![ALBY HUB](assets/fr/26.webp)

Alby Hub koostab teile arve, mille eest saate tasuda. See makse katab teie kanali avamiseks vajalikud tehingutasud, samuti LSP (*Lightning Service Provider*) teenustasud, kes avab kanali teie sõlme, mis võimaldab teil kohe makseid saada.

![ALBY HUB](assets/fr/27.webp)

Kui arve on tasutud ja tehing kinnitatud, on loodud teie esimene Lightning-kanal.

![ALBY HUB](assets/fr/28.webp)

Vahekaardil "*Sõlm*" näete, et teil on nüüd sissetulev raha, mis võimaldab teil Lightning'i kaudu makseid vastu võtta.

![ALBY HUB](assets/fr/29.webp)

Makse vastuvõtmiseks klõpsake vahekaardil "*Pangakassa*" ja seejärel "*Võta vastu*".

![ALBY HUB](assets/fr/30.webp)

Sisestage summa ja lisage vajadusel kirjeldus, seejärel klõpsake "*Loo arve*".

![ALBY HUB](assets/fr/31.webp)

Sain oma esimese makse 120 000 sati.

![ALBY HUB](assets/fr/32.webp)

Tagasi pöördudes vahekaardile "*Pangakott*", saate kontrollida oma rahakoti saldot. Pange tähele, et Alby Hub paneb automaatselt 354 sati kõrvale, kui teete oma esimese makse. Iga järgneva avatud Lightning-kanali puhul paneb Alby Hub automaatselt kõrvale 1% kanali mahust. See reserv on turvameede, mis võimaldab teie sõlmpunktil kanali raha tagasi saada, kui teie partner üritab pettust teha. Sellepärast, kuigi ma olen saatnud 120 000 sati, on minu bilansil näidatud ainult 119 646 sati.

![ALBY HUB](assets/fr/33.webp)

## Bitcoinide hoiustamine onchain

Kui soovite maksete tegemiseks väljaminevat sularaha, võite ka ise avada kanali. Selleks vajate oma rahakotis onchaini bitcoine.

Klõpsake vahekaardil "*Sõlm*" nupule "*Panek*".

![ALBY HUB](assets/fr/34.webp)

Saatke bitcoinid kuvatavale aadressile. See aadress on tuletatud teie eelnevalt salvestatud taastamislausest.

![ALBY HUB](assets/fr/35.webp)

Ma saatsin 72 000 sati. Need on nüüd nähtavad jaotises "*Säästusaldo*", mis sisaldab kõiki vahendeid, mida ma oman onchainis, mitte Lightningis.

![ALBY HUB](assets/fr/36.webp)

## Avage Lightning kanal

Nüüd, kui teil on olemas onchaini vahendid, saate avada uue Lightning-kanali. Soovitatav on avada mitu kanalit, piisavate summadega, et saaksite alati piiranguteta makseid teha. Enamik LSPsid (*Lightning Service Providers*) nõuavad teiega kanali avamiseks vähemalt 150 000 sati.

Klõpsake vahekaardil "*Sõlm*" nupule "*Avanenud kanal*".

![ALBY HUB](assets/fr/37.webp)

Valige oma kanali suurus. Soovitan, et te ei avaks liiga väikeseid kanaleid, pidades silmas, et tegemist on Lightning-sõlmega ja teie võtmeid majutav masin ei paku sama suurt turvalisust kui riistvaraline rahakott. Nii et olge ettevaatlik summade osas, mida valite blokeerimiseks.

![ALBY HUB](assets/fr/38.webp)

Menüüs "*Advanced Options*" saate valida, millise LSPga oma kanalit avada, või sisestada käsitsi mõne teise Lightning-sõlme.

![ALBY HUB](assets/fr/39.webp)

Seejärel klõpsake nupule "*Open Channel*".

![ALBY HUB](assets/fr/40.webp)

Oodake, kuni teie kanal kinnitatakse onchain.

![ALBY HUB](assets/fr/41.webp)

Teie uus kanal ilmub nüüd vahekaardile "*Sõlm*".

![ALBY HUB](assets/fr/42.webp)

## Ühendage kulurakendus

Nüüd, kui teil on toimiv Lightning-sõlm, saate seda kasutada igapäevaseks sati vastuvõtmiseks ja kulutamiseks. Kuigi Alby Hubi veebiliides on mugav oma sõlme haldamiseks, ei ole see ideaalne kiirete tehingute tegemiseks liikvel olles. Selleks kasutame oma nutitelefoni paigaldatud Lightningi rahakoti rakendust.

Selles õpetuses soovitan valida Alby Go, mida on väga lihtne kasutada, kuid võite kasutada ka teisi ühilduvaid rakendusi, näiteks Zeus.

![ALBY HUB](assets/fr/43.webp)

Alby Go installimiseks minge oma seadme rakenduste poodi:


- [Androidile](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Androidi kasutajad saavad rakenduse paigaldada ka `.apk` faili kaudu [saadaval Alby GitHubis](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Kui rakendus on käivitunud, klõpsake nupule "*Connect Wallet*".

![ALBY HUB](assets/fr/46.webp)

Klõpsake oma Alby Hubis vahekaardil "*Connections*" (*ühendused*) nupule "*Add Connection*" (*Lisenda ühendus*).

![ALBY HUB](assets/fr/47.webp)

Andke sellele ühendusele nimi, et see oleks hõlpsasti tuvastatav teie keskuses, ja valige õigused, mida soovite rakendusele anda. Minu puhul valisin "*Täielik juurdepääs*", et mul oleks nutitelefonist täielik juurdepääs oma Lightning-sõlme rahalistele vahenditele, kuid te võite piirata juurdepääsu ka maksimaalse eelarve alusel, valida lubatud funktsioonid või määrata nende õiguste kehtivusaja. Kui olete seadistanud, klõpsake nuppu "*Järgmine*".

![ALBY HUB](assets/fr/48.webp)

Seejärel loob Alby Hub ühenduse loomiseks saladuse.

![ALBY HUB](assets/fr/49.webp)

Mine tagasi Alby Go rakendusse, skaneeri QR-kood või kleebi saladus sisse.

![ALBY HUB](assets/fr/50.webp)

Klõpsake nuppu "Lõpeta*".

![ALBY HUB](assets/fr/51.webp)

Nüüd on teil nutitelefonist kaugjuurdepääs oma Lightning-sõlmele, mis võimaldab teil iga päev liikvel olles hõlpsasti satelliite kulutada ja vastu võtta.

![ALBY HUB](assets/fr/52.webp)

Vajaduse korral saate selle ühenduse õigusi hallata otse Alby Hubis, klõpsates sellel.

![ALBY HUB](assets/fr/53.webp)

Satelliitide vastuvõtmiseks klõpsake lihtsalt nupule "*Vaata*".

![ALBY HUB](assets/fr/54.webp)

Muutke arve summat ja kirjeldust, klõpsates nupul "*Arve*".

![ALBY HUB](assets/fr/55.webp)

Laadige arve, et saada satsid.

![ALBY HUB](assets/fr/56.webp)

Satsi saatmiseks klõpsake "*Saatmine*".

![ALBY HUB](assets/fr/57.webp)

Skaneerige arve, mida soovite tasuda.

![ALBY HUB](assets/fr/58.webp)

Seejärel klõpsake nupule "*Maksa*".

![ALBY HUB](assets/fr/59.webp)

Teie tehing on kinnitatud.

![ALBY HUB](assets/fr/60.webp)

Kui klõpsate väikesele noolega, saate juurdepääsu oma tehinguajaloole.

![ALBY HUB](assets/fr/61.webp)

Need tehingud on nähtavad ka teie Alby Hubis.

![ALBY HUB](assets/fr/62.webp)

## Kohandage oma Lightning-aadressi

Alby pakub teile võimalust kasutada välkkiirte aadressi. See võimaldab teil saada makseid oma sõlme, ilma et peaksite iga kord käsitsi arvet koostama. Vaikimisi määrab Alby teile Lightning-aadressi, kuid te saate seda kohandada. Logige sisse oma Alby veebikontole, klõpsake paremas ülemises nurgas oma nimele ja valige seejärel "*Settings*".

![ALBY HUB](assets/fr/63.webp)

Navigeerige menüüsse "*Lightning Address*".

![ALBY HUB](assets/fr/64.webp)

Muutke oma aadressi, seejärel kinnitage see, klõpsates "*Update your lightning address*".

![ALBY HUB](assets/fr/65.webp)

Pange tähele, et kui teie aadress on muudetud, ei kuulu see enam teile. Nii et veenduge, et te ei saada sati enam kunagi sellele aadressile.

Ja see ongi kõik, te teate nüüd, kuidas kasutada Lightningut oma sõlme kasutades Alby Hubi tööriista. Kui leidsid selle õpetuse kasulikuks, oleksin väga tänulik, kui paneksid alla rohelise pöidla. Palun jagage seda artiklit julgelt oma sotsiaalsetes võrgustikes. Tänan teid väga!

Et mõista üksikasjalikult kõiki Lightning mehhanisme, millega me selles õpetuses manipuleerisime, soovitan tungivalt tutvuda meie tasuta koolitusega sel teemal :

https://planb.network/courses/lnp201