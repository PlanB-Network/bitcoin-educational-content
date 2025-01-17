---
name: Tor Browser
description: Kuidas kasutada Tor brauserit?
---
![kaas](assets/cover.webp)

Nagu nimigi viitab, on brauser tarkvara, mida kasutatakse Internetis navigeerimiseks. See toimib väravana kasutaja masina ja veebi vahel, tõlkides veebilehtede koodi interaktiivseteks ja loetavateks lehtedeks. Teie brauseri valik on väga oluline, kuna see mõjutab mitte ainult teie sirvimiskogemust, vaid ka teie veebiturvalisust ja privaatsust.

Olge ettevaatlik, et mitte ajada segamini brauserit otsingumootoriga. Brauser on tarkvara, mida kasutate Interneti juurdepääsuks (nagu Chrome või Firefox), samas kui otsingumootor on teenus, näiteks Google või Bing, mis aitab teil veebis teavet leida.

Tänapäeval on Google Chrome kaugelt kõige enam kasutatav brauser. See moodustab umbes 65% ülemaailmsest turuosast aastal 2024. Chrome'i hinnatakse selle kiiruse ja jõudluse poolest, kuid see ei pruugi olla parim valik kõigile, eriti kui privaatsus on teile oluline. Chrome kuulub Google'ile, ettevõttele, mis on tuntud oma kasutajate andmete kogumise ja analüüsimise poolest. Tõepoolest, nende oma brauser on nende jälgimisstrateegia südames. See tarkvara on enamiku teie veebipõhiste suhtluste keskne komponent. Andmete kogumise valdamine teie brauseris on Google'i jaoks oluline küsimus.
![TOR BROWSER](assets/notext/01.webp)
*Allikas: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*

On mitmeid peamisi brauserite perekondi, millest igaüks põhineb kindlal renderdamismootoril. Brauserid nagu Google Chrome, Microsoft Edge, Brave, Opera või Vivaldi on kõik rajatud Chromiumi brauserile, mis on Google'i poolt arendatud Chrome'i kerge ja avatud lähtekoodiga versioon. Kõik need brauserid kasutavad Blink renderdamismootorit, mis on WebKiti haru, mis omakorda pärineb KHTML-ist. Chromiumi valitsev seisund turul muudab sellest tuletatud brauserid eriti tõhusaks, kuna veebiarendajad kipuvad oma saite peamiselt Blinki jaoks optimeerima.

Safari, Apple'i brauser, kasutab WebKiti, mis samuti pärineb KHTML-ist.

Teisest küljest tuginevad brauserid nagu Mozilla Firefox, LibreWolf ja Tor Browser Gecko renderdamismootorile, mis algselt pärineb Netscape'i brauserist.

Õige brauseri valimine sõltub teie vajadustest. Kuid kui olete vähemalt mures oma privaatsuse ja seega turvalisuse pärast, soovitan üldiseks kasutamiseks minna Firefoxiga ja veelgi suurema privaatsuse jaoks Tor Browseriga. Selles õpetuses näitan teile, kuidas Tor brauseriga kergesti alustada.
![TOR BROWSER](assets/notext/02.webp)

## Sissejuhatus Tor brauserisse

Tor brauser on spetsiaalselt loodud turvaliseks ja võimalikult privaatseks internetis navigeerimiseks. Brauser põhineb Firefoxil ja seega Gecko renderdamismootoril.
Tor brauser kasutab Tor võrku, et krüpteerida ja suunata teie liiklust mitme relee serveri kaudu enne selle sihtkohta edastamist. See mitmekihilise marsruutimise protsess, mida tuntakse kui "*sibulmarsruutimist*", aitab varjata teie tegelikku IP-aadressi, muutes teie asukoha ja veebitegevuste tuvastamise keeruliseks. Siiski on sirvimine tingimata aeglasem kui standardbrauseriga, mis ei kasuta Tor võrku, kuna see on kaudne.
Erinevalt teistest brauseritest integreerib Tor brauser spetsiifilisi funktsioone, et vältida teie veebitegevuste jälgimist, näiteks iga külastatud veebilehe isoleerimine ja küpsiste ning ajaloo automaatne kustutamine sulgemisel. See on ka kujundatud minimeerima sõrmejälje jätmise riske, muutes kõik kasutajad külastatud saitidele võimalikult sarnaseks.
Tor Browserit saab väga hästi kasutada tavaliste veebilehtede (`.com`, `.org` jne) külastamiseks. Sel juhul anonüümiseeritakse teie liiklus, läbides mitu Tori sõlme enne lõppsõlme jõudmist, mis suhtleb lõpliku saidiga selgenetis. ![TOR BROWSER](assets/notext/03.webp)
Samuti võib Tor Browserit kasutada peidetud teenuste (aadressid, mis lõppevad `.onion`) ligipääsuks. Selles stsenaariumis jääb kogu liiklus Tori võrku, ilma väljumissõlmeta, tagades täieliku privaatsuse nii kasutajale kui ka sihtserverile. Seda toimimisviisi kasutatakse märkimisväärselt ligipääsuks sellele, mida mõnikord nimetatakse "*dark web*"-iks, interneti osaks, mida traditsioonilised otsingumootorid ei indekseeri.
![TOR BROWSER](assets/notext/04.webp)

## Mis vahe on Tori võrgul ja Tori brauseril?

Tori võrk ja Tori brauser on kaks erinevat asja, mida ei tohiks segi ajada, kuid need täiendavad teineteist. Tori võrk on globaalne relee-serverite infrastruktuur, mida kasutajad opereerivad, mis anonüümiseerib internetiliiklust, suunates seda läbi mitme sõlme enne selle lõppsihtkohta suunamist. See on kuulus sibulmarsruutimine.

Tori brauser seevastu on spetsiifiline brauser, mis on loodud selle võrgu kasutamise lihtsustamiseks. See integreerib vaikimisi kõik vajalikud seaded Tori võrguga ühenduse loomiseks ja kasutab muudetud versiooni Firefoxist, et pakkuda tuttavat sirvimiskogemust, maksimeerides samal ajal privaatsust ja turvalisust.

Tori võrku kasutatakse mitte ainult Tori brauseri poolt. Seda saavad kasutada mitmesugused tarkvarad ja rakendused oma suhtluse turvamiseks. Näiteks on võimalik lubada suhtlus Tori võrgu kaudu oma Bitcoin'i noodil, et peita oma IP-aadress teistelt kasutajatelt ja vältida oma Bitcoiniga seotud liikluse jälgimist internetiteenuse pakkujate poolt.
Kokkuvõttes on Tori võrk infrastruktuur, mis pakub privaatsust meie internetis surfamisel, ja Tori brauser on tarkvara, mis võimaldab meil seda võrku veebis surfamise osana kasutada.

## Kuidas paigaldada Tori brauserit?

Tori brauser on saadaval Windowsile, Linuxile ja macOS-ile arvutites, samuti Androidile nutitelefonides. Tori brauseri oma arvutisse paigaldamiseks külastage [ametlikku Tori projekti veebilehte](https://www.torproject.org/).
![TOR BROWSER](assets/notext/05.webp)
Klõpsake nupul "*Download Tor Browser*".
![TOR BROWSER](assets/notext/06.webp)
Valige teie operatsioonisüsteemile sobiv versioon.
![TOR BROWSER](assets/notext/07.webp)
Klõpsake käivitataval failil, et alustada paigaldamist, seejärel valige oma keel.
![TOR BROWSER](assets/notext/08.webp)
Valige kaust, kuhu tarkvara paigaldatakse, seejärel klõpsake nupul "*Install*".
![TOR BROWSER](assets/notext/09.webp)
Oodake, kuni paigaldamine on lõpetatud.
![TOR BROWSER](assets/notext/10.webp)
Lõpuks klõpsake nupul "*Finish*".
![TOR BROWSER](assets/notext/11.webp)

## Kuidas kasutada Tori brauserit?

Tori brauserit kasutatakse nagu tavalist brauserit.
![TOR BROWSER](assets/notext/12.webp)
Esimesel käivitamisel esitleb brauser teile lehte, mis kutsub teid ühenduma Tori võrguga. Lihtsalt klõpsake nupul "*Connect*", et ühendus luua.
![TOR BROWSER](assets/notext/13.webp)
Kui soovite, et tarkvara ühenduks Tori võrguga automaatselt teie tulevastel kasutuskordadel, märkige valik "*Always connect automatically*".
![TOR BROWSER](assets/notext/14.webp)
Ühenduse loomisel Tori võrguga jõuate avalehele.
![TOR BROWSER](assets/notext/15.webp)Internetis otsingu sooritamiseks sisestage lihtsalt oma päring otsinguribale ja vajutage "*enter*" klahvi.
![TOR BROWSER](assets/notext/16.webp)
Seejärel saate oma otsingumootorist tulemused samamoodi nagu teiste brauserite puhul.
![TOR BROWSER](assets/notext/17.webp)
DuckDuckGo "*Onionize*" valik võimaldab kasutada otsingumootorit selle peidetud teenuse kaudu Tor võrgus, pääsedes ligi selle `.onion` aadressile.
![TOR BROWSER](assets/notext/18.webp)

## Kuidas seadistada Tor brauserit?

Brauseri ekraani ülaosas leiate valiku oma lemmikute importimiseks. See võimaldab automaatselt integreerida järjehoidjad teie vanast brauserist Tor brauserisse.
![TOR BROWSER](assets/notext/19.webp)
Samuti on teil võimalus lisada uusi järjehoidjaid, klõpsates tärniikoonil, mis asub külastatava veebilehe paremas ülanurgas.
![TOR BROWSER](assets/notext/20.webp)
Paremal asuvas menüüs pääsete ligi erinevatele valikutele.
![TOR BROWSER](assets/notext/21.webp)"*Uus identiteet*" nupp võimaldab teil muuta oma Tor identiteeti. See tähendab, et saate alustada uut kasutajasessiooni Tor'is, muutes oma IP-aadressi ja lähtestades küpsised ning avatud sessioonid.
![TOR BROWSER](assets/notext/22.webp)
"*Järjehoidjad*" menüü võimaldab teil hallata oma järjehoidjaid.
![TOR BROWSER](assets/notext/23.webp)
"*Ajalugu*" annab teile juurdepääsu teie sirvimisajaloole, kui olete selle seadetes lubanud.
![TOR BROWSER](assets/notext/24.webp)
"*Lisandmoodulid ja teemad*" menüü võimaldab kohandada brauseri välimust või lisada laiendusi. Kuna Tor brauser põhineb Mozilla Firefoxil, saate kasutada Firefoxi jaoks saadaolevaid teemasid ja laiendusi.
![TOR BROWSER](assets/notext/25.webp)
Lõpuks annab "*Seaded*" nupp teile juurdepääsu brauseri seadetele.
![TOR BROWSER](assets/notext/26.webp)
"*Üldine*" vahekaardil seadetes on mitmesuguseid valikuid, mis võimaldavad kohandada Tor brauseri kasutajaliidest.
![TOR BROWSER](assets/notext/27.webp)
"*Kodu*" vahekaardil saate muuta vaikimisi lehte, mis kuvatakse Tor brauseri avamisel ja uute vahelehtede avamisel.
![TOR BROWSER](assets/notext/28.webp)
"*Otsing*" vahekaardil saate valida otsingumootori. Tor brauseri vaikimisi valik on DuckDuckGo, otsingumootor, mis keskendub kasutajate privaatsuse kaitsmisele, kuid võite valida ka Google'i või Startpage'i, näiteks.
![TOR BROWSER](assets/notext/29.webp)
Samuti saate seadistada oma otsingumootoris otseteid.
![TOR BROWSER](assets/notext/30.webp)
Näiteks võite tippida "*@wikipedia*" järgnevalt oma otsinguterminiga, näiteks "*Bitcoin*", brauseri otsinguribale.
![TOR BROWSER](assets/notext/31.webp)
See funktsioon sooritab seejärel otsingu teie termini kohta otse Wikipedia saidil.
![TOR BROWSER](assets/notext/32.webp)
Nii saate seadistada ka teisi kohandatud otseteid erinevatele saitidele.

Järgmisena, "*Privaatsus & Turvalisus*" vahekaardil, leiate kõik seaded, mis on seotud privaatsuse ja turvalisusega.
![TOR BROWSER](assets/notext/33.webp)
Teil on võimalus hoida või kustutada oma sirvimisajalugu.
![TOR BROWSER](assets/notext/34.webp) Samuti saate hallata erinevatele veebilehtedele antud juurdepääsuõiguseid.
![TOR BROWSER](assets/notext/35.webp)
Oma brauseri üldise turvalisuse tagamiseks võimaldavad "*Turvalisem*" ja "*Kõige turvalisem*" režiimid kohandada veebifunktsioone ja skripte, mida külastatavad saidid täidavad. See vähendab haavatavuste ärakasutamise riske, kuid mõjutab vastutasuks saitide kuvamist ja interaktiivsust. ![TOR BROWSER](assets/notext/36.webp) Leiate ka teisi turvavalikuid, sealhulgas ohtliku sisu blokeerija ja ainult-HTTPS režiimi, mis tagab, et ühendused saitidega järgivad järjepidevalt seda protokolli. ![TOR BROWSER](assets/notext/37.webp) Lõpuks leiate "*Ühenduse*" vahelehelt kõik seaded, mis on seotud Tor võrguga ühendamisega. Siin saate seadistada silla, et pääseda Torile juurde piirkondadest, kus sellele võidakse juurdepääsu tsenseerida. ![TOR BROWSER](assets/notext/38.webp) Ja ongi kõik, nüüd olete valmis Internetis turvalisemalt ja privaatsemalt surfama! Kui veebipõhine privaatsus on teema, mis teid huvitab, soovitan avastada ka seda teist õpetust Mullvad VPN-i kohta:

https://planb.network/tutorials/others/general/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8