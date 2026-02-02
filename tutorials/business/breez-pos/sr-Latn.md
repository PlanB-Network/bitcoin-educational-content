---
name: Breez - POS
description: Breez olakšava prikupljanje bitcoin uplata za vaše poslovanje.
---

![cover](assets/cover.webp)



Od pandemije COVID-19, beskontaktna digitalna plaćanja postala su rasprostranjena, čak i u najmanjim prodavnicama. Tokom ovog perioda, mnogi biznisi su otkrili praktičnost bitcoin cash rešenja, omogućavajući im da primaju uplate iz celog sveta. Međutim, ova rešenja su ponekad teška za korišćenje ili neprikladna za male biznise. U ovom vodiču, pogledaćemo Breez terminal za plaćanje, rešenje koje se ističe svojom lakoćom korišćenja, dok vam pruža potpunu kontrolu nad upravljanjem vašim bitcoinima.



## Instaliraj Breez POS



Breez POS je usluga samostalnog čuvanja koju pruža Breez wallet. Korisnost ove usluge je omogućavanje trgovcima da prikupljaju uplate putem Bitcoin dok ostaju na jednostavnom interfejsu, vrlo sličnom raznim Lightning novčanicima. Breez POS je dostupan na platformama za preuzimanje [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) i [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS).



![download](assets/fr/01.webp)



![setup](assets/fr/12.webp)



⚠️ Važno je napomenuti da su ove aplikacije još uvek u razvoju i da može doći do grešaka u korišćenju funkcionalnosti. Preporučujemo umereno korišćenje.



Sa ovom aplikacijom, Breez vam daje potpunu kontrolu nad mrežnim konfiguracijama i postavkama naknada, dok garantuje vašu suverenost u upravljanju vašim bitcoinima.



Možete istražiti različite Breez wallet opcije prateći naš vodič ispod. Ovaj korak će vam pomoći da bolje razumete ekosistem prodajnog mesta i usvojite najbolje prakse za efikasno osiguranje bitkoina povezanih sa vašim seed.



https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Korišćenje Breez POS



U ovom vodiču, fokusiraćemo se na odeljak "*Point-of-Sale*" kako bismo vam pomogli da razumete kako da ga integrišete kao sredstvo plaćanja u vašem poslovanju.



Prodajno mesto je integralni deo Breez portfolija i oslanja se prvenstveno na Lightning Network za prikupljanje uplata.



U meniju "*Point of Sale*", imate direktan interfejs za prikupljanje uplata. Podeljen je na dva dela:



### Direktno zaduženje



Prvi deo je tastatura za direktno zaduženje. Ovaj interfejs je koristan za naplatu celokupnog iznosa kada znate ukupne kupovine vašeg kupca, ili kada vam nije potreban fiksni katalog proizvoda u vašem poslovanju (npr. freelance usluge).



![keyboard](assets/fr/02.webp)



Da biste prvi put koristili Breez POS, potrebno je da prikupite uplatu od preko 2.500 satoshija (oko 3 evra po današnjem kursu). Ovaj iznos, plaćen samo prilikom vaše prve isplate, predstavlja trošak kreiranja platnog kanala kako biste mogli komunicirati sa drugim Lightning Network čvorovima i slati i primati satoshije.



![channel_fee](assets/fr/03.webp)


### Katalog proizvoda



Drugi deo je katalog proizvoda. Ovaj interfejs je idealan kada imate katalog proizvoda sa unapred definisanim cenama. Ovde možete unapred konfigurisati svoje proizvode i zatim ih koristiti za generate fakture kako biste poboljšali sledljivost svojih novčanih priznanica.



![items](assets/fr/04.webp)



Možete ručno konfigurisati svaku stavku iz ovog interfejsa klikom na dugme "**Plus**" i zatim definisanjem imena, cene i identifikatora za ovu stavku.



![add_items](assets/fr/05.webp)



Zatim ga možete dodati i definisati njegovu količinu da biste prikupili povezanu uplatu.



Kada je vaš katalog prilično velik, može postati komplikovano dodavati proizvode jedan po jedan. U tu svrhu, u odeljku **Preferences > Point of Sale Settings**, iz menija "Item list", možete automatski uvoziti i izvoziti listu artikala iz CSV fajlova.



![import](assets/fr/07.webp)



U ovom istom odeljku možete definisati period važenja vaših Lightning faktura. Od sada, za sve vaše fakture, vaši kupci imaju `N` sekundi da izvrše uplatu, u suprotnom ćete morati da generišete novu Lightning fakturu.



![invoice_time](assets/fr/08.webp)



Kao menadžer, možete ojačati sigurnost svojih bitkoina dodavanjem lozinke koja će biti potrebna za sve odlazne uplate sa vašeg wallet. Ova funkcija je posebno korisna kada niste jedini koji upravlja vašim prodajnim mestom.



![manager](assets/fr/09.webp)



U meniju **Transactions** pronaći ćete listu svih uplata koje ste prikupili. Takođe možete filtrirati rezultate za određeni period klikom na dugme **Calendar**.



![transactions](assets/fr/10.webp)



Takođe možete pogledati dnevni rezime vaših prodaja i ukupan iznos prikupljen klikom na dugme **Dokument**.



![summary](assets/fr/11.webp)



Sada imate potpuno razumevanje prodajnog mesta koje nudi Breez aplikacija za besprekornu integraciju Bitcoin u vaše poslovanje. Ako ste smatrali da je ovaj vodič koristan, preporučujemo naš vodič o be-BOP, e-commerce platformi koja vam omogućava da primate uplate u bitkoinima i monetizujete vaše poslovanje.



https://planb.academy/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa