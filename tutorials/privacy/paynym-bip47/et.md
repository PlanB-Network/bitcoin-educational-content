---
name: BIP47 - PayNym
description: Kasutage Ashigaru korduvkasutatavat maksekoodi
---
![cover](assets/cover.webp)



Halvim privaatsusviga, mida Bitcoin puhul teha saab, on aadresside korduvkasutamine. Iga kord, kui samale aadressile tehakse mitu makset, ühendatakse need tehingud omavahel, andes maailmale teie tehingute kaardi. Seetõttu on tungivalt soovitatav, et generate kasutaksite iga kviitungi puhul alati unikaalset aadressi. Kuid mõnede Bitcoin rakenduste puhul ei ole see lihtne.



Justus Ranvier'i poolt 2015. aastal välja pakutud BIP47 pakub sellele probleemile elegantset vastust. Selles võetakse kasutusele **korduvkasutatava maksekoodi** kontseptsioon: unikaalne identifikaator, mis võimaldab praktiliselt piiramatul arvul bitcoini makseid ahelas vastu võtta, ilma et aadressi korduvalt kasutataks. Tänu ECDH (*Diffie-Hellman on elliptic curves*) vahetusel põhinevale krüptograafilisele mehhanismile annab iga samale koodile tehtud makse tulemuseks tühja aadressi, mis on omane saatja ja saaja vahelisele suhtele.



![Image](assets/fr/01.webp)



Seda BIP47 põhimõtet rakendab eelkõige **PayNym**, mis on algselt Samourai Wallet poolt välja töötatud ja nüüd Ashigaru poolt üle võetud süsteem. Selles õpetuses vaatame, kuidas aktiveerida oma PayNym, vahetada maksekoode korrespondendiga ja teostada tehinguid ilma aadressi korduvkasutamiseta.



Ma ei hakka siinkohal BIP47 üksikasjalikku toimimist käsitlema. Kui soovite teemasse sügavamalt süveneda, vaadake minu BTC 204 koolituskursuse peatükki 6.6.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Eeltingimused



Selle õpetuse jälgimiseks on vaja vaid wallet Ashigaru rakenduses. Kui te ei tea, kuidas rakenduse alla laadida, kontrollida, paigaldada või luua wallet, siis soovitan kõigepealt tutvuda selle õpetusega:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Taotlus PayNym



Esimene samm on oma PayNymi taotlemine. Seda toimingut tuleb teha ainult üks kord wallet kohta. See seostab teie seed-st saadud BIP47 maksekoodi (`PM...`) PayNymi rakendusele omase unikaalse identifikaatoriga. Seda lühemat ja loetavamat identifikaatorit saab seejärel edastada teie korrespondentidele, et hõlbustada teabevahetust, ilma et oleks vaja jagada pikka, täielikku BIP47-koodi.



Selleks klõpsa oma PayNymi pildil kasutajaliidese vasakus ülaosas ja seejärel oma maksekoodil "PM...".



![Image](assets/fr/02.webp)



Seejärel klõpsake kolmel väikesel punktil üleval paremas nurgas ja valige "Taotlus PayNym".



![Image](assets/fr/03.webp)



Kinnitage, klõpsates nupule "CLAIM YOUR PAYNYM".



![Image](assets/fr/04.webp)



Värskendage lehte: teie PayNym ID kuvatakse nüüd teie pildi all, kohe teie BIP47 maksekoodi kohal.



![Image](assets/fr/05.webp)



Teie PayNym on nüüd aktiivne ja valmis kasutama oma esimesi BIP47 tehinguid.



## Ühendage kontaktiga



PayNymi vahel on kahte tüüpi ühendus: **jälgida** ja **ühendada**. `jälgimine` on täiesti tasuta. See loob ühenduse kahe PayNymi vahel Sorobani kaudu, mis on Samourai meeskonna poolt välja töötatud ja Ashigaru poolt kasutusele võetud Toril põhinev krüpteeritud suhtlusprotokoll. See ühendus võimaldab kahel üksteist jälgival kasutajal vahetada teavet privaatselt, eelkõige selliste ühistehingute nagu Stowaway või StonewallX2 koordineerimiseks, mida me vaatame teises õpetuses. See samm on PayNymile omane ja ei ole osa BIP47-protokollist.



![Image](assets/fr/06.webp)



Ühendamise operatsioon (`connect`) seevastu nõuab on-chain tehingut. See seisneb teatamistehingu sooritamises, nagu on määratletud BIP47-s. See Bitcoin tehing sisaldab metaandmeid OP_RETURN väljundis, mis loob krüpteeritud sidekanali maksja ja saaja vahel. Selle kanali kaudu saab maksja iga makse jaoks generate unikaalse vastuvõtuaadressi ja saaja saab nendest maksetest teate ning saab generate aadressidega seotud eravõtmeid, et neid vahendeid hiljem kulutada.



See teavitustehing on kulukas: mining tasu ja 546 sats, mis saadetakse vastuvõtja teavitusaadressile, et anda märku ühenduse loomisest. Kui ühendus on loodud, saab BIP47 kaudu teha peaaegu lõpmatult palju makseid.



Lühidalt:




- follow": tasuta, loob Sorobani kaudu krüpteeritud suhtluse, mis on kasulik Ashigaru koostöövahenditele;
- "Ühendamine": tasuline, teostab BIP47 teavitustehingu, et aktiveerida kanal maksja ja saaja vahel.



PayNymiga suhtlemiseks peate esmalt *jälgima* seda. See on esimene samm enne BIP47 ühenduse loomist. Oletame, et soovite saata korduvaid makseid PayNymile `+instinctiveoffer10`.



Mine oma PayNymi lehele Ashigaru's, seejärel klõpsa liideses paremal allosas olevale nupule "+".



![Image](assets/fr/07.webp)



Seejärel saate kas sisestada saaja täieliku maksekoodi või skaneerida tema QR-koodi.



![Image](assets/fr/08.webp)



Kui teil on ainult tema PayNym ID, minge [Paynym.rs](https://paynym.rs/), et leida tema maksekoodiga seotud QR-kood.



![Image](assets/fr/09.webp)



Kui olete QR-koodi skaneerinud, klõpsake PayNymi jälgimiseks nupule "FOLLOW".



![Image](assets/fr/10.webp)



Tegevus `FOLLOW` on piisav ühistehingute (*cahoots*) jaoks. BIP47 maksete saatmiseks peate aga looma ühenduse: klõpsake `CONNECT`, et sooritada teavitustehing.



![Image](assets/fr/11.webp)



Seejärel edastatakse teavitustehing võrgus. Oodake enne esimese makse sooritamist, kuni see on saanud vähemalt ühe kinnituse.



![Image](assets/fr/12.webp)



## Tehke makse BIP47



Nüüd olete saajaga ühenduses ja saate saata makse unikaalsele aadressile, mis luuakse automaatselt BIP47-protokolli abil, ilma eelneva suhtluseta saajaga.



Klõpsake oma PayNymi pealehel kontaktil, kellele soovite makse saata.



![Image](assets/fr/13.webp)



Klõpsake kasutajaliidese paremas ülaosas noolesümbolile.



![Image](assets/fr/14.webp)



Sisestage saadetav summa. Te ei pea sisestama vastuvõtja aadressi: see tuletatakse automaatselt, kasutades BIP47-protokolli.



![Image](assets/fr/15.webp)



Kontrollige hoolikalt tehingu üksikasju, sealhulgas tasusid, seejärel lohistage rohelist noolt ekraani allosas, et allkirjastada ja edastada tehing.



![Image](assets/fr/16.webp)



Tehing on saadetud.



![Image](assets/fr/17.webp)



Selles näites tehti makse teisele minu PayNymi rahakotile. Seega näen, et see on saabunud minu teise Ashigaru wallet, ilma et ühtegi aadressi oleks käsitsi vahetatud: kasutati ainult PayNymi identifikaatorit.



![Image](assets/fr/18.webp)



Nüüd te teate, kuidas kasutada BIP47 korduvkasutatavaid maksekoode tänu PayNymi rakendusele Ashigaru rakenduses. Nüüd saate seda maksekoodi jagada kõigi nendega, kes soovivad teile makseid (eriti korduvaid makseid) saata. Samuti võite avaldada oma PayNymi ID-d oma veebisaidil või sotsiaalvõrgustikes, et saada annetusi.



Et süvendada oma teadmisi selle protokolli kohta, mõista üksikasjalikult selle toimimist ja selle mõju konfidentsiaalsusele, soovitan tungivalt läbida minu BTC 204 kursus:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c