---
name: Firefox
description: Kuidas konfigureerida Firefoxi, et kaitsta oma privaatsust?
---

![cover](assets/cover.webp)



## Sissejuhatus



Me kõik veedame tundide kaupa aega internetis, sageli teadvustamata, mida meie veebilehitseja meie kohta paljastab. Iga klõps, iga otsing, iga külastatav veebileht toidab tohutut isikuandmete kogumise tööstust.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Veebibrauserite turuosa: Chrome domineerib 65% turuosaga, järgnevad Safari ja Edge. Allikas: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Nagu see graafik näitab, domineerib Google Chrome massiliselt, üle 65% maailma kasutusest. Selline hegemoonia tähendab, et enamik internetikasutajaid usaldab oma sirvimisandmed Google'ile, mille ärimudel põhineb suunatud reklaamil. Firefox, mille turuosa on vaid 3%, on alternatiiv, mille on välja töötanud Mozilla, mittetulundusühing, kellel puudub äriline huvi teie andmete ärakasutamise vastu.



Kuid Firefoxi valimine on ainult esimene samm. Vaikimisi vajab isegi Firefox kohandusi, et maksimeerida oma kaitset. See juhend viib teid samm-sammult, alates kõige lihtsamast kuni kõige edasijõudnumani, et muuta Firefox tõeliseks kilbiks jälgimise vastu, säilitades samal ajal meeldiva sirvimiskogemuse.



### Miks Firefox?





- Vaba ja avatud lähtekoodiga** (Gecko mootor): kontrollitav, läbipaistev kood
- Mittetulundusühing**: Mozilla Foundation, üldhuviteenused
- Sisseehitatud omamaine kaitse**: Täiustatud jälgimiskaitse (ETP), täielik küpsiste kaitse (TCP), oleku partitsioneerimine, ainult HTTPS-režiim, DNS üle HTTPS (DoH)
- Täiustatud kohandamine**: erinevalt Chrome'ist saate Firefoxi käitumist põhjalikult muuta



### Olulised põhimõtted enne alustamist





- Ei ole universaalset retsepti**: mida rohkem te muudate, seda rohkem riskite eristuda (sõrmejälg). Eesmärk on olla paremini kaitstud, ilma et paistaksite silma.
- Samm-sammult edasiminek**: Muutke seadistust, testige oma tavapäraseid saite ja jätkake seejärel. Ei ole vaja kõike korraga muuta.
- Isiklik tasakaal**: Leia SINU kompromiss privaatsuse ja kasutusmugavuse vahel.



## Kiire paigaldus



![Téléchargement Firefox](assets/fr/02.webp)



**Official download:** Mine aadressile [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). Sellel lehel valige oma operatsioonisüsteem (Windows, macOS, Linux), et pääseda vastavale allalaadimislehele koos konkreetsete paigaldusjuhistega.





- Windows**: laadige alla installer `.exe`, tehke topeltklõps ja järgige paigaldusviisarit
- macOS**: laadige alla `.dmg` fail, avage see ja lohistage Firefox rakenduste kausta
- Linux**: mitu võimalust - pakett `.deb`/`.rpm`, Flatpak (Flathub), Snap või paketihalduri (apt, dnf, pacman) kaudu. Eelistada Mozilla ametlikke allikaid.



**Vihje:** Kui olete installinud, kontrollige uuenduste olemasolu Abi → **About Firefox** kaudu (oluline turvaparanduste jaoks).



![Configuration initiale Firefox](assets/fr/03.webp)


*Esimene ekraan Firefoxi käivitamisel: määrake Firefox oma vaikimisi brauseriks, lisage see oma otseteedesse, seejärel klõpsake "Salvesta ja jätka "*



![Création compte Firefox](assets/fr/04.webp)


*Valikuline samm: looge Firefoxi konto või logige sellesse sisse. Selle sammu saate vahele jätta, kui klõpsate paremal allosas oleval nupul "Mitte nüüd "*



![Page d'accueil Firefox](assets/fr/05.webp)


*Firefoxi avakuva, kui seadistamine on lõpetatud. Pange tähele ☰ menüüd üleval paremal, mis annab ligipääsu Firefoxi kohandamise seadetele ja laiendustele*



## Kaitsed on juba vaikimisi aktiveeritud (rahustav)





- Saitide isoleerimine (Fission)**: järkjärguline kasutuselevõtt. See funktsioon käivitab iga saidi eraldi protsessina, et vältida ühe pahatahtliku vahekaardi juurdepääsu teise saidi andmetele. Kontrollige selle staatust `about:support` kaudu (otsinguga "Fission"). Kui see ei ole lubatud, saate selle käsitsi aktiveerida `about:config`is, kasutades `fission.autostart = true`.
- Täielik küpsiste kaitse (TCP)**: vaikimisi aktiivne. Küpsised ja muu salvestamine piirdub esimese osapoole saidiga (üks "purk" saidi kohta), mis neutraliseerib saidiülese jälgimise. Vajaduse korral tehakse ajutisi erandeid Storage Access API kaudu (integreeritud sisselogimisnupud).
- Bounce/Redirect Tracking Protection**: Firefox tuvastab ja puhastab automaatselt küpsised, mille on jätnud põrgatavad saidid (lingid, mis suunavad teid enne sihtkohta jälgimise kaudu ümber), vähendades seda jälgimiskanalit ilma teiepoolse tegevuseta.



## Tase 1 - oluline (≤ 10 minutit)



Eesmärk: suur privaatsuse suurendamine ilma veebi lõhkumata. 90% kasutajate jaoks.



Seadetele juurdepääsemiseks klõpsake üleval paremal menüüs ☰ ja seejärel **"Seaded "**:



![Paramètres généraux](assets/fr/07.webp)


*Firefoxi seadete leht - vahekaart "Üldine". Siin saate konfigureerida enamiku oma privaatsusseadetest*



**Seirekaitse (ETP)**




- Vahetage **ETP** vastu **Strict**. Te blokeerite rohkem jälgimisseadmeid (saidiülesed küpsised, sõrmejäljed, krüptomining, sotsiaalsed vidinad...).
- Kui mingi sait katkeb (video, sisselogimise nupp...), lülitage kaitse ainult selle saidi jaoks välja 🛡️ kilbi kaudu, seejärel värskendage vahekaarti.



Siin on erinevad ETP turvatasemed:




- Standard** (tasakaalustatud, maksimaalne ühilduvus)
  - Blokeerib: sotsiaalsed jälgimisseadmed, saidiülesed küpsised (kõik aknad), sisu jälgimine privaatses sirvimises, krüptoraha kaevandajad, sõrmejälgede detektorid.
  - Sisaldab **Total Cookie Protection** (TCP): üks purk saidi kohta.
- Range** (soovitatav konfidentsiaalsuse tagamiseks)
  - Blokeerib ka jälgimise sisu kõigis akendes + teadaolevad ja kahtlustatavad sõrmejäljed.
  - Võib rikkuda mõned saidid; kasutage 🛡️ kilpi kohaliku erandi tegemiseks.
- Kohandatud** (täiustatud)
  - Peenhäälestus: küpsised, sisu jälgimine, alaealised, sõrmejäljed (teadaolevad/kahtlustatavad).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Küpsised ja saidi andmed




- Lülita sisse **"Kustuta küpsised ja saidi andmed sulgemisel "**, et taaskäivitada puhtalt iga kord, kui taaskäivitad.
- Lisage soovi korral **Erandid** 2-3 olulise saidi jaoks (e-post, pank).


**Automaatne andmete sisestamine, ettepanekud ja koduleht**




- Deaktiveerige **automaatne täitmine** (ID-d, aadressid, kaardid). Kasutage selle asemel paroolihaldurit.
- Otsing**: deaktiveeri **"Näita otsingusoovitusi "**.
- Address riba**: lõigatud **"Sponsorlusettepanekud "** ja **"Kontekstipõhised ettepanekud "**.
- Avaleht**: keelake **Tasku** ja **sponsoreeritud sisu**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Kasutatakse ainult *HTTPS**




- Aktiveerige **"HTTPS-režiim ainult kõigis akendes "**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Telemeetria ja reklaami mõõtmine




- "Andmete kogumine Firefoxi poolt", **lülita kõik** välja.
- Deaktiveerige **"Privaatsussõbralikud reklaamimeetmed "** (PPA).
- Turvaline sirvimine**: hoidke see sisse lülitatud (soovitatav). Firefox kontrollib saite ohunimekirjade alusel hashed-küsitluste ja kohalike kontrollide abil, kaitstes neid andmepüügi ja pahavara eest minimaalse mõjuga eraelu puutumatusele.



**Globaalne privaatsuse kontroll (valikuline)**




- Aktiveerige **GPC**, et anda märku andmete müümisest/jagamisest keeldumisest.



**otsingumootor




- Vahetage **DuckDuckGo**, **Startpage**, **Qwant** või **Brave Search** (Seaded → Search).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Privaatne navigatsioon**




- Eraldi aknad (Ctrl/Cmd+Shift+P) ühekordsete seansside jaoks (kingitused, sekundaarkontod...). Vältige "alati privaatne" režiimi: laiendused võivad olla mitteaktiivsed ja küpsiste erandid vähem kasulikud.



**Vajalikud laiendused** (paigaldada ametlikust kataloogist)




- uBlock Origin**: blokeerib reklaame ja praegust jälgimist, kergekaaluline.
- Privacy Badger**: õpib blokeerima, mis teid jälgib; saadab Do Not Track / GPC.
- ClearURLs** (valikuline): Firefox (ETP Strict) ja uBO puhastavad juba palju; jätke see alles, kui näete endiselt "räpaseid" URL-e (utm, fbclid).
- Firefoxi mitme konto konteinerid**: **Isoleerib küpsised/sessioonid ja salvestusruumi konteineri kohta; paralleelselt mitu kontot; vähem saidiülest jälgimist**. Ametlik laiendus: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Paroolid ja 2FA**




- Kasutage spetsiaalset paroolihaldurit** (Bitwarden, KeePassXC). **Vältige** paroolide salvestamist brauseris. **Võimaldage võimaluse korral 2FA**.



## Tase 2 - tugevdatud (kompartmentaliseerimine ja võrgustik)



Eesmärk: jaotada tegevus osadeks ja vähendada võrgulekkeid.



**DNS üle HTTPS (DoH)**




- Vaikimisi staatus**: Automaatselt aktiveeritud mõnes piirkonnas (USA, Kanada, Venemaa, Ukraina). Mujal on vajalik käsitsi aktiveerimine.
- Konfiguratsioon**: Seaded → Üldine → Võrgu seaded → **Enable DoH** → **Cloudflare** või **Quad9** → **Maximumkaitse**.
- Maksimaalne kaitse = ainult TRR** (ei taganeta süsteemi DNS-i). Kui ettevõtte/hotelli võrk blokeerib, lülitage tagasi **Standard** või keelake DoH.
- Koondamine**: DoH võib olla üleliigne, kui kasutate juba usaldusväärset VPN-i, millel on oma turvaline DNS.
- Kontrolltest**: "https://www.dnsleaktest.com/" peaks kuvama ainult valitud DoH teenusepakkujat.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Konteinerite ja profiilidega jaotamine




- Mitme konto konteinerid**: looge ruumid (isiklik, töö, rahandus, sotsiaalvõrgustikud, ostud, ühekordsed). Konfigureerige **"Avage alati selles konteineris "** oma korduvate saitide jaoks. Ametlik laiendus: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Miks neid kasutada?
  - Küpsiste/seansside/salvestuse tugev eraldamine** ruumi järgi.
  - Vähem saidiülest jälgimist**: piirata hiiglasi (Facebook, Google).
  - Samaaegne mitme konto** samas teenuses.
  - Väiksem CSRF/XSS** risk segmenteeritud identiteetide vahel.
  - Vihje: vähemalt spetsiaalsed konteinerid sotsiaalvõrgustike/Google, töö ja rahanduse jaoks.
- Facebooki konteiner** (valikuline): FB/Instagrami jaoks mõeldud lihtsustatud versioon.
- Eraldi profiilid**: `about:profiles` kaudu (põhiprofiil, minimaalne "üliturvaline" profiil, testprofiil). Andmete ja laienduste täielik jaotamine.



**Kõrgendatud laiendused** (reserveeritakse)




- Cookie AutoDelete**: kustutab saidi küpsised kohe, kui vahekaart suletakse (kasulik, kui Firefox on pikka aega avatud).
- LocalCDN**: teenindab praeguseid raamatukogusid lokaalselt (vähendab Google/Microsoft-kõnesid). Osaline ühilduvus.



**Mobiil (Android)**




- Firefox Android + uBlock Origin**: sarnane kaitse liikvel olles.



## Tase 3 - ekspert (about:config & Arkenfox)



Eesmärk: täiustatud karastamine koos aktsepteeritud kompromissidega. Soovitatav **eraldi profiilil**.



Valige ainult üks kahest järgmisest lähenemisviisist:



**Käsitlusviis A - käsitsi muutmine**: Mõned sihipärased kohandused `about:config` kaudu (lihtsam ja täpsem kontroll)


**Käsitlusviis B - Arkenfox user.js**: Täielik automatiseeritud konfiguratsioon (keerulisem, maksimaalne kaitse)



➡️ **Arkenfox sisaldab juba KÕIK allpool mainitud about:config muudatusi** + sadu muid muudatusi. Kui valite Arkenfoxi, ignoreerige about:config jaotist.



### Lähenemisviis A: Manuaalsed muudatused about:config kaudu



Sisestage Address riba `about:config` → Võtke risk vastu.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Vastupidavus sõrmejälgede võtmisele (päritud Tor Browserist)


```text
privacy.resistFingerprinting = true
```


Mõju: (standardsed aknasuurused), standardiseeritud kasutaja-agent/-põhimõtted, Canvas/WebGL/AudioContext piirangud. Rohkem ühtsust, kuid mõned "veidrused" (nihkes aeg, mõnikord natuke inglise keel).





- Lülita WebRTC välja (väldib IP-lekkeid; rikub Web visio)


```text
media.peerconnection.enabled = false
```





- Referer pluss ühilduv (vaikimisi)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Range variant (võib katkestada maksed/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Jutlustavate APIde ja spekulatsioonide piiramine


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Kuldne reegel: kui miski katkeb, mine tagasi viimase muudatuse juurde.



### Lähenemisviis B: Arkenfox user.js (täielikult automatiseeritud konfiguratsioon)



Projekt **Arkenfox** pakub kogukonna poolt hooldatavat faili `user.js`, mis rakendab automaatselt sadu privaatsusele ja turvalisusele suunatud Firefoxi eelistusi. Uuesti käivitamisel loeb Firefox seda faili teie profiilist ja rakendab neid seadeid.





- Mis on selle mõte? Alustage **kõrge karastatud baasilt** ilma "kõikjal klõpsutamata"; vähendage eksimusi; säästke aega.
- Mida see muudab (näited): telemetria kärpimine, küpsised/cache/referrer/HTTPS tugevdatud, **RFP** + letterboxing, **WebRTC välja lülitatud**, DoH/TLS kohandused, jutukas APId piiratud.
- Millal seda kasutada: kui soovite, et Firefox oleks 10 minutiga karastatud ja aktsepteeriksite mõningaid erandeid (DRM/streaming, Web visio, SSO/maksed).
- Eelised: kiire, järjepidev, **uuendatud** (ESR-iga vastavusse viidud), väga hästi **dokumenteeritud** (wiki + kommentaarid), **kohandatav** ülestähenduste kaudu.
- Piirangud: ühilduvus (mõned veebirakendused), mugavus (UTC, aknasuurused) ja meeldetuletus: **see ei ole Tor** (ei ole võrgu anonüümsust).



Paigaldamine (ideaaljuhul **dedicated profile**)


1. Salvestage profiil/lemmikud ja loendage oma saite küpsiste eranditega.


2. Lae `user.js` alla aadressilt `https://github.com/arkenfox/user.js` (ESR/stabiilne versioon).


3. Leidke oma profiilikaust `about:profiles` kaudu:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4. Sulgege Firefox ja viige `user.js` profiili kausta juurde.


5. Taaskäivitamine; kohandage `about:config` või ülestähenduste faili kaudu.



Uuendused




- Jälgige Arkenfoxi väljalaskeid (ESR-ga joondatud), asendage `user.js`, käivitage Firefox uuesti; lugege väljalaske märkusi.



**Kujundamine ülestähenduste kaudu**



Arkenfox on vaikimisi tahtlikult piirav. Teatud seadete kohandamiseks teie vajadustele (voogedastus, visio, konkreetsed saidid) saate luua faili `user-overrides.js` samas kaustas kui `user.js`. See fail võimaldab teil teatud Arkenfoxi eelistusi ilma põhifaili muutmata "tühistada".



Looge `user-overrides.js` ja lisage oma kohandused:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Parimad tavad




- Kasutage eraldi **"Arkenfox"-profiili** ja säilitage mugavuse huvides "tavaline" profiil.
- Minimeeri laiendused (uBlock Origin OK), et piirata rünnakupinda ja unikaalsust.
- Lisage vajaduse korral saidipõhised erandid (kilp 🛡️, uBO, NoScript, kui seda kasutatakse).
- Testige pärast iga muudatust: WebRTC/DNS lekked, Cover Your Tracks, CreepJS.



## Parimad tavad





- Uuendused**: Firefox ja laiendused on ajakohased.
- Pikendused**: mõistlikud ja usaldusväärsed; jälgige "kahtlasi" lunastusi.
- Allalaadimised**: ettevaatust; testige tundlikke faile VirusTotalis.
- Paroolid**: **dedicated manager** (Bitwarden, KeePassXC); **2FA** lubatud; vältida salvestamist brauseris.
- Hügieen**: piirake Google/Facebook konteineritesse; sulgege/avage regulaarselt, et "lähtestada" konteksti.



## Piirangud ja alternatiivid





- Karastatud brauser ≠ võrgu anonüümsus: ilma **VPNita** jääb teie IP nähtavaks; isegi sellega on korrelatsioon võimalik.
- Liiga palju muutmine võib muuta teid **unikaalseks**. **RFP** standardiseerib; randomiseerimisvahendid (nt Chameleon) võivad teid... eristada. Testige, võrrelge, kohandage.
- Alternatiivid/täiendused:
 - Tor Browser: võrgu anonüümsus Tor'i kaudu; aeglasem. Vaata meie täielikku paigaldus- ja seadistusjuhendit**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad Browser: "Tor ilma Torita, kombineeritav VPN-iga; standardiseeritud jalajälg. Uuri, kuidas seda paigaldada meie spetsiaalsest õpetusest**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Soovitatavad kombinatsioonid: Firefox (tase 2) + VPN igapäevaseks kasutamiseks; Tor/Mullvad tundlike tegevuste jaoks; eraldi profiilid eraldamiseks.



## Kokkuvõte



Järgides seda samm-sammult koostatud juhendit, olete muutnud Firefoxi tõeliseks kaitsevalliks digitaalse jälgimise vastu. Alates olulistest 1. taseme seadetest kuni Arkenfoxi täiustatud konfiguratsioonideni tugevdab iga muudatus teie privaatsust, ilma et see kahjustaks teie sirvimiskogemust.



** Teie privaatsus on nüüd paremini kaitstud**: reklaamtrackerid blokeeritud, küpsised eraldatud, IP Address lekked neutraliseeritud, telemetria välja lülitatud. Firefox ei ole enam lihtsalt brauser, vaid teie vajadustele kohandatud digitaalne vastupanuvahend.



**Mäleta: konfidentsiaalsus ei ole kunagi iseenesestmõistetav. Testige oma kaitset regulaarselt, uuendage oma seadeid ja ärge kartke oma konfiguratsiooni kohandada, kui teie harjumused muutuvad. Teie anonüümsus internetis sõltub nii teie vahenditest kui ka teie tavadest.



## Ressursid



### Plan ₿ Network




- SCU 202 - Isikliku digitaalse turvalisuse parandamine: Et rohkem teada saada selles õppesuunas käsitletud digitaalse turvalisuse kontseptsioonidest**



https://planb.network/courses/ameliorer-sa-securite-numerique-personnelle-4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla dokumentatsioon




- [Tõhustatud jälgimiskaitse] (https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Ametlik juhend tõhustatud jälgimiskaitse kohta
- [Riigi jaotamine](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Tehniline dokumentatsioon riigi partitsioneerimise kohta
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Täielik viide veebiturvalisuse kohta



### Arkenfox




- [Wiki ja paigaldusjuhend](https://github.com/arkenfox/user.js/wiki): Täielik Arkenfox projekti dokumentatsioon
- [Hoiustamine ja vabastamine](https://github.com/arkenfox/user.js): User.js faili allalaadimine ja uuenduste jälgimine



### Juhendid ja kogukonnad




- [PrivacyGuides - Töölaua brauserid](https://www.privacyguides.org/en/desktop-browsers/): Soovitused ja võrdlused brauserite kohta
- Reddit**: r/firefox, r/privacy tagasiside ja toetuse saamiseks
- PrivacyGuides foorum**: põhjalikud tehnilised arutelud



### Testimisvahendid




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Digitaalne sõrmejälgimine ja jälgimisvastase võitluse tõhusus
- [DNS Leak Test](https://www.dnsleaktest.com/): DNS lekke test ja DoH tõhusus
- [BrowserLeaks](https://browserleaks.com/): (WebRTC, Canvas, kirjatüübid jne.)
- [BadSSL](https://badssl.com/): SSL/TLS sertifikaadi valideerimise testid
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Rohkem kui 50 sõrmejälgede vektori täiustatud analüüs
- [Cloudflare DNS Test](https://1.1.1.1/help): Kontrollida, et Cloudflare DoH töötab korralikult