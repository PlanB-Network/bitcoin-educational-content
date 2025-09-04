---
name: Ledger U2F & FIDO2
description: Parandage oma veebiturvalisust Ledger abil
---
![cover](assets/cover.webp)



Ledger seadmed on riistvaralised rahakotid, mis on algselt mõeldud Bitcoin Wallet turvamiseks, kuid neil on ka täiustatud võimalused tugevaks autentimiseks veebis. Tänu nende ühilduvusele **U2F** ja **FIDO2** protokollidega võimaldavad nad teil kaitsta juurdepääsu oma veebikontodele, luues teise autentimisteguri.



U2F (Universal 2nd Factor) protokolli võtsid Google ja Yubico kasutusele 2014. aastal, seejärel standardiseeris seda FIDO Alliance. See võimaldab sisselogimisel lisada teise füüsilise autentimisteguri (2FA). Kui see on aktiveeritud, peavad kasutajad lisaks klassikalisele paroolile kinnitama iga kontoga ühendamise katse, vajutades nuppu oma Ledger-l. Selles kontekstis töötab Ledger sarnaselt Yubikey'ga. U2F on tegelikult FIDO2-standardi alamkomponent, mis hõlmab seda, tuues samas olulisi täiustusi, sealhulgas kaasaegsete brauserite loomulikku tuge ja suuremat paindlikkust autentimisvõtmete haldamisel.



Need meetodid põhinevad asümmeetrilisel krüptograafial: salajasi andmeid ei edastata, mis muudab andmepüügi- või pealtkuulamisrünnakud ebatõhusaks. U2F ja FIDO2 on nüüd paljude veebiteenuste poolt toetatud.



Selles õpetuses näitame teile, kuidas aktiveerida U2F ja FIDO2 kahefaktorilise autentimise jaoks Ledger-ga.



**Märkus:** U2F ja FIDO2 on toetatud kõigis Ledger seadmetes, mis on varustatud uuema püsivara versiooniga: alates versioonist 2.1.0 Nano X ja Nano S classic ning alates versioonist 1.1.0 Nano S Plus. Stax ja Flex mudelid on algselt ühilduvad.



## Installige rakendus Ledger Security Key



Kui kasutate Ledger seadet, siis teate tõenäoliselt, et püsivara üksi ei sisalda kõiki krüptokontode haldamiseks vajalikke funktsioone. Näiteks Bitcoin Wallet kasutamiseks peate installima rakenduse "*Bitcoin*". Samamoodi peate MFA võtmete haldamiseks installima rakenduse "*Security Key*".



Enne alustamist veenduge, et olete oma Bitcoin Wallet seadistanud Ledger-l. Oluline on salvestada oma Mnemonic õigesti, sest 2FA jaoks kasutatavad võtmed on tuletatud sellest Mnemonic-st. Kui teie Ledger on kadunud või kahjustatud, saate taastada juurdepääsu oma võtmetele, sisestades oma Mnemonic fraasi teises Ledger seadmes (hetkel ei toeta Ledgers veel FIDO2-tunnuseid režiimis "*passwordless*", seega ei ole residentseid tunnuseid).



Ühendage Ledger arvutiga ja vabastage see.



![Image](assets/fr/01.webp)



Rakenduse installimiseks avage tarkvara [Ledger Live] (https://www.Ledger.com/Ledger-live), seejärel minge vahekaardile "*My Ledger*". Leidke rakendus "*Security Key*" ja installige see oma seadmesse.



![Image](assets/fr/02.webp)



Nüüd peaks rakendus "*Turvalisuse võti*" ilmuma koos teiste teie Ledger-le paigaldatud rakendustega.



![Image](assets/fr/03.webp)



Klõpsake rakendusel, et jätta see õpetuse järgmiste sammude jaoks avatuks.



![Image](assets/fr/04.webp)



## U2F/FIDO2 kasutamine 2FA jaoks koos Ledger-ga



Juurdepääs kontole, mida soovite kaitsta kahefaktorilise autentimisega. Näiteks kasutan Bitwardeni kontot. Tavaliselt leiate 2FA valiku teenuse seadetest, vahekaartide "*autentimine*", "*turvalisus*", "*login*" või "*salasõna*" alt.



![Image](assets/fr/05.webp)



Valige kahefaktorilise autentimise sektsioonis valik "*Passkey*" (mõiste võib sõltuvalt kasutatavast saidist erineda).



![Image](assets/fr/06.webp)



Sageli palutakse teil oma praegust parooli kinnitada.



![Image](assets/fr/07.webp)



Andke oma turvavõtmele nimi, et see oleks hõlpsasti äratuntav, ja klõpsake seejärel nupule "*Luge võtit*".



![Image](assets/fr/08.webp)



Teie konto andmed ilmuvad Ledger ekraanile. Vajutage kinnitamiseks nuppu "*Registreeri*" (või mõlemat nuppu korraga, sõltuvalt kasutatavast mudelist).



![Image](assets/fr/09.webp)



Juurdepääsuvõti on edukalt registreeritud.



![Image](assets/fr/10.webp)



Registreerige see turvavõti.



![Image](assets/fr/11.webp)



Nüüdsest alates palutakse teil oma kontole sisselogimisel lisaks tavapärasele paroolile ühendada ka teie Ledger.



![Image](assets/fr/12.webp)



Seejärel saate autentimise kinnitamiseks vajutada Ledger ekraanil nuppu "*Log in*" (või mõlemat nuppu korraga, olenevalt kasutatavast mudelist).



![Image](assets/fr/13.webp)



Hardware Wallet Ledger kasutamise eelis kahefaktorilise autentimise puhul on see, et tänu Mnemonic fraasile saate võtmed hõlpsasti taastada. Lisaks sellele põhilisele varukoopiale saate kasutada ka iga teenuse, kus olete 2FA aktiveerinud, pakutavat hädaolukoodi. See hädaolukorra kood võimaldab teil oma kontoga ühendust võtta, kui kaotate oma turvavõti. Seega asendab see vajaduse korral 2FA ühenduse loomiseks.



Näiteks Bitwardenis saate sellele koodile ligi, kui klõpsate nupule "*View recovery code*".



![Image](assets/fr/14.webp)



Soovitan seda koodi hoida erinevas kohas, kus te säilitate oma põhiparooli, et vältida nende koos varastamist. Näiteks kui teie parool on salvestatud paroolihaldurisse, siis hoidke 2FA hädaolukorra koodi eraldi paberil.



See lähenemisviis pakub teile 2FA-autentimise Ledger kadumise korral kahetasemelist varukoopiat: esimene varukoopia, milles kasutatakse Mnemonic fraasi kõigi teie kontode jaoks, ja teine kontospetsiifiline varukoopia, milles kasutatakse hädaolukorra koode. Siiski on oluline **ei segi ajada Mnemonic rolli hädaabikoodiga**:




- 12- või 24-sõnaline Mnemonic fraas annab teile juurdepääsu mitte ainult kõigi teie kontode 2FA jaoks kasutatavatele võtmetele, vaid ka teie Ledger abil kaitstud bitcoinidele;
- Hädaolukorra kood võimaldab teil ajutiselt 2FA taotlusest mööda minna ainult asjaomasel kontol (antud näites ainult Bitwardenis).



Palju õnne, te olete nüüd oma Ledger kasutamisega MFA jaoks kursis! Kui leidsite selle õpetuse kasulikuks, oleksin väga tänulik, kui jätaksite allpool Green pöidla. Palun jagage seda õpetust julgelt oma suhtlusvõrgustikes. Tänan teid väga!



Soovitan ka seda teist õpetust, kus me vaatame teist lahendust U2F ja FIDO2 autentimiseks:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e