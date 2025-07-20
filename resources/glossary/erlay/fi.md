---
term: ERLAY
---

Ehdotettu verkkoprotokolla, jolla parannetaan Bitcoin-solmujen välisten vahvistamattomien tapahtumien välittämisen tehokkuutta.


Tällä hetkellä jokainen tapahtuma leviää järjestelmän kautta, jossa jokainen solmu lähettää tietämänsä tapahtuman kaikille vertaisverkoilleen. Ongelmana on, että tämä johtaa runsaaseen redundanssiin ja kaistanleveyden käyttöön kaksoiskappaleiden vuoksi. Monet transaktiolähetykset ovat tarpeettomia, koska vastaanottaja tietää jo näistä transaktioista, ja jokaisen solmun tarvitsee tietää jokaisesta transaktiosta vain kerran. 


Erlay vähentäisi kaistanleveyden kulutusta noin 40 prosenttia, mikä helpottaisi Full node:n toimintaa käyttäjille, joilla on rajalliset Internet-yhteydet, ja edistäisi siten verkon hajauttamista. Tämä protokolla myös säilyttäisi kaistanleveyden kulutuksen lähes vakiona yhteyksien määrän kasvaessa. Tämä tarkoittaa sitä, että solmujen operaattoreiden olisi paljon yksinkertaisempaa hyväksyä hyvin suuri määrä yhteyksiä vertaisiltaan, mikä parantaisi Bitcoin -verkon turvallisuutta vähentämällä tahallisen tai tahattoman osioitumisen riskiä. Lisäksi Erlay vaikeuttaisi tapahtuman lähettävän solmun määrittämistä, mikä lisäisi luottamuksellisuutta sellaisten solmujen käyttäjille, jotka eivät toimi Tor-verkossa.


Erlay ehdotetaan BIP330:ssä.