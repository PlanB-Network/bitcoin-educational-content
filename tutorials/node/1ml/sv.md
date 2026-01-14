---
name: 1ML
description: Lär dig hur du använder 1ML explorer för att förstå och analysera Bitcoin:s Lightning-nätverk.
---
![cover](assets/cover.webp)



## Inledning



Lightning Network är en snabb och billig betalningslösning som bygger på Bitcoin och möjliggör omedelbara och säkra transaktioner. Att observera detta nätverk är viktigt för att förstå hur det fungerar, dess topologi och tillståndet för de noder som utgör det. En Lightning explorer, som 1ML, används för att visualisera nätverkets offentliga data, inklusive aktiva noder, öppna kanaler och tillgänglig kapacitet, vilket ger en värdefull översikt för användare, utvecklare och nodoperatörer.



## Få tillgång till 1ML och förstå startsidan



För att komma åt 1ML öppnar du helt enkelt din webbläsare och skriver in [https://1ml.com](https://1ml.com). Detta tar dig till startsidan, som fungerar som Lightning Network:s globala instrumentpanel.



![capture](assets/fr/03.webp)



På den här sidan visas flera viktiga statistiska uppgifter längst upp på skärmen, bland annat :





- Det **totala antalet aktiva noder** i nätverket, dvs. de datorer som är involverade i att skicka och ta emot Lightning-betalningar.
- **antalet öppna kanaler**, vilket motsvarar förbindelserna mellan dessa noder som möjliggör överföringar av medel.
- Den **totala nätverkskapaciteten**, uttryckt i bitcoin (BTC), som anger summan av kapaciteten hos alla offentliga kanaler.



Dessa siffror uppdateras regelbundet för att återspegla nätverkets nuvarande tillstånd. De ger en uppfattning om dess storlek, tillväxt och robusthet.



![capture](assets/fr/04.webp)



Strax nedanför erbjuder sidan listor med rangordningar:





- De **mest anslutna noderna**, som har de mest öppna kanalerna till andra noder.
- De **högsta kapaciteterna** på noderna, vilket anger vilka noder som kan överföra de största beloppen.
- De viktigaste kanalerna när det gäller kapacitet.



Filter kan också användas för att förfina dessa listor efter geografisk plats eller andra kriterier.



Den här sidan är en perfekt utgångspunkt för att utforska Lightning Network och förstå dess allmänna topologi.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Utforska Lightning-noder



För att utforska en nod på 1ML kan du börja med att använda sökfältet högst upp på sidan. Du kan ange **Node ID**, dvs. nodens unika identifierare, eller dess **alias**, som är ett namn som är lättare att komma ihåg.



När sökningen har slutförts klickar du på motsvarande nod för att komma till dess detaljerade sida.



![capture](assets/fr/07.webp)



På den här sidan visas flera viktiga informationsbitar:





- Node ID**: denna unika identifierare är en lång teckensträng som gör det möjligt att exakt identifiera noden i hela nätverket.



![capture](assets/fr/08.webp)





- Alias**: detta är det namn som nodägaren har valt för att representera noden offentligt.



![capture](assets/fr/09.webp)





- **Antalet kanaler** anger hur många anslutningar noden har öppna med andra noder, medan **Total kapacitet** representerar summan av bitcoins som finns tillgängliga i dessa kanaler. En nod med ett stort antal kanaler och hög kapacitet är i allmänhet väl ansluten och kan snabbt överföra stora summor pengar över nätverket.



![capture](assets/fr/10.webp)





- **Upptid**, eller tillgänglighet, mäter hur länge en nod har varit aktiv och tillgänglig online, vilket återspeglar dess tillförlitlighet. Nodens **ålder**, å andra sidan, anger hur länge den har funnits i nätverket, vilket återspeglar dess stabilitet och erfarenhet inom Lightning Network.



![capture](assets/fr/11.webp)



Dessa data hjälper dig att förstå hur viktig och tillförlitlig en nod är i Lightning Network. Till exempel är en nod med ett stort antal kanaler, hög kapacitet och hög drifttid ofta en viktig aktör i nätverket.



## Utforska blixtkanaler



### Vad är en Lightning-kanal?



En Lightning-kanal är en direkt anslutning mellan två nätverksnoder. Den gör det möjligt för dessa två noder att utbyta omedelbara betalningar till låg kostnad utan att gå igenom Bitcoin:s huvudkedja för varje transaktion. Kanaler är grunden som gör Lightning Network snabb och skalbar.



### Läs kanalinformation på 1ML



På 1ML har varje kanal sin egen sida eller beskrivningsblad som innehåller ett antal viktiga uppgifter:



Från en nods sida kan du komma åt en lista över dess kanaler. Genom att klicka på en kanal visar 1ML en särskild sida med flera viktiga delar av informationen.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



De viktigaste synliga uppgifterna är följande:





- Partnernoder**: varje kanal länkar två noder. 1ML visar båda identifierarna och deras respektive alias.



![capture](assets/fr/14.webp)





- Kanalkapacitet**: detta är den totala mängden bitcoins som är låsta i den här kanalen. Denna kapacitet representerar den maximala gränsen för betalningar som kan transiteras genom denna kanal.



![capture](assets/fr/15.webp)





- Channel age**: anger hur länge kanalen har varit öppen. En gammal kanal är ofta ett tecken på en stabil relation mellan två noder.



![capture](assets/fr/16.webp)



### Begränsningar av kanalens synlighet



Det är viktigt att förstå att 1ML bara visar **del** av Lightning Network. Utforskaren visar endast **publika kanaler**, dvs. de som har tillkännagivits i nätverket. Privata kanaler, som ofta används av sekretesskäl eller av strategiska skäl, syns inte. Vidare visar 1ML inte den exakta fördelningen av medel på varje sida av en kanal, inte heller de betalningar som gjorts eller den likviditet som faktiskt är tillgänglig vid ett givet tillfälle. Den information som visas kan därför användas för att analysera nätverkets **generella struktur**, men inte dess faktiska finansiella aktivitet eller detaljerade likviditetsstatus.



## Utforska Lightning Network efter plats



### Noder per land och region



1ML låter dig utforska Lightning Network enligt en **geografisk uppdelning**. Från startsidan eller via dedikerade sektioner är det möjligt att visa noder per land eller region. Denna funktion är baserad på platsinformation som deklarerats av nodoperatörer.


I navigeringsfältet ser du länken **Location**. På sidan är noderna grupperade efter världsdel, land och stad.



![capture](assets/fr/17.webp)



Genom att välja ett land visar 1ML en lista över associerade noder, tillsammans med aggregerad statistik såsom antalet noder och total synlig kapacitet för det geografiska området.



#### Vad detta säger om lokal adoption





- Antagande av teknik**: Ett stort antal noder i en region indikerar att Bitcoin-användare, företag eller tjänster aktivt använder Lightning Network. Detta visar på teknisk mognad och en vilja att dra nytta av Lightnings fördelar (snabba transaktioner, lägre kostnader).
- Ekonomiskt ekosystem** : Den täta förekomsten av noder kan också signalera en lokal ekonomisk struktur runt Bitcoin: handlare som accepterar Lightning, nystartade företag som utvecklar verktyg, samhällsevenemang etc.
- Säkerhet och motståndskraft**: Olika geografisk distribution ökar nätverkets motståndskraft mot lokala avbrott eller begränsningar. Ju mer utspridda noderna är, desto mer decentraliserat och svårare att censurera nätverket.
- Policyer och regelverk**: I vissa länder kan införandet gå snabbare tack vare ett gynnsamt regelverk eller ett proaktivt samhälle. Omvänt kommer antalet noder att vara lägre i områden där regelverket är strikt eller fientligt.



#### Begränsningar av geografiska data



Tänk dock på att geolokaliseringen av Lightning-noder har sina begränsningar och fördomar:





- Ungefärlig IP-placering**: 1ML använder i allmänhet den offentliga IP-adressen för noder för att uppskatta deras plats. Denna metod kan dock förvrängas genom användning av VPN, molnservrar (AWS, Google Cloud) eller hosting i länder som skiljer sig från nodägarens faktiska hemvist.
- Virtuella noder**: Vissa operatörer hostar sina noder på fjärrservrar av tillförlitlighets- och tillgänglighetsskäl, vilket kan ge en falsk känsla av fysisk plats.
- Användarens rörlighet**: En nodoperatör kan byta plats, flytta sin infrastruktur eller öppna flera noder i olika regioner, vilket gör dataläsningen mer komplicerad.
- Osynliggörande av privata noder**: Vissa noder publicerar inte sin IP-adress eller använder metoder för att dölja sin plats, vilket gör geolokalisering omöjlig.



## 1ML konkreta användningsfall



### Förståelse för nätverkstopologi



med 1ML kan du visualisera den **generella strukturen för Lightning Network**. Genom att observera kopplingarna mellan noder, antalet kanaler och den totala kapaciteten är det möjligt att förstå hur nätverket är organiserat, vilka noder som spelar en central roll och hur betalningsflöden teoretiskt kan cirkulera.



Denna förståelse är nödvändig för att vi ska kunna förstå hur Lightning Network fungerar, och inte bara för portföljanvändning.



### Identifiera viktiga noder



Tack vare de rankningar som 1ML erbjuder (mest anslutna noder, högsta kapacitet, ålder) är det möjligt att identifiera de noder som har en viktig plats i nätverket. Dessa noder fungerar ofta som stora gateways för Lightning-betalningar.



![capture](assets/fr/18.webp)



### Kontrollera den offentliga synligheten för en nod



För en nodoperatör ger 1ML dig möjlighet att kontrollera om din nod är **offentligt annonserad** på Lightning Network. Om en nod visas på 1ML betyder det att den är synlig och tillgänglig för andra noder för att öppna offentliga kanaler.


Detta kan vara användbart för att diagnostisera problem med synlighet eller anslutning.



### Att se Lightning Network utvecklas över tid



Genom att jämföra global statistik under olika perioder gör 1ML det möjligt för oss att observera utvecklingen av Lightning Network: ökning eller minskning av antalet noder, variationer i total kapacitet eller förändringar i den geografiska fördelningen.


Dessa observationer ger ett intressant perspektiv på Lightning Network:s tillväxt, mognad och trender.



## bästa praxis och begränsningar för 1ML



### Offentliga uppgifter ≠ fullständig verklighet



1ML baseras enbart på de **offentligt tillkännagivna** uppgifterna om Lightning Network. Detta innebär att verktyget endast visar en del av verkligheten. Många kanaler kan vara privata, vissa noder kanske inte annonseras och den faktiska likviditeten som finns tillgänglig i kanalerna är inte synlig. Det är därför viktigt att använda 1ML som ett globalt analysverktyg, inte som en uttömmande representation av nätverket.



### Sekretess och blixtnedslag



Lightning Network har utformats med ett starkt fokus på **betalningssekretess**. Enskilda transaktioner är inte synliga på 1ML och exakta kanalsaldon är inte offentliga. Denna begränsning är inte ett fel hos utforskaren, utan en grundläggande funktion i Lightning Network, utformad för att skydda användarnas integritet.



### Dra inte förhastade slutsatser



En nod med hög kapacitet eller många kanaler är inte nödvändigtvis mer "tillförlitlig" eller "effektiv" i alla lägen. På samma sätt behöver en tillfällig minskning av den totala nätkapaciteten inte nödvändigtvis betyda att det finns ett strukturellt problem. Siffror bör alltid tolkas i efterhand och sättas in i sitt sammanhang.



### Komplementaritet med andra verktyg



1ML är en utmärkt startpunkt för att utforska Lightning Network, men det används bäst tillsammans med andra verktyg som Lightning-portföljer, gränssnitt för nodhantering och andra utforskare. Detta tillvägagångssätt ger en mer komplett och nyanserad bild av nätverket.



## 1ML-anslutningsalternativ (avancerad funktionalitet)



1ML erbjuder ett alternativ för **inloggning/skapande av konto**, synligt på webbplatsen, men detta är **inte nödvändigt** för att visa Lightning Network-data. Alla funktioner som diskuterats hittills i denna handledning är tillgängliga **utan konto**.



Anslutningen riktar sig i första hand till **Lightning node operators**. Den gör det möjligt att associera en nod med ett 1ML-konto för att hantera viss publik information, såsom nodens presentation, kontaktlänkar och andra metadata. Denna funktion är utformad för att förbättra synligheten och identifieringen av en nod i utforskaren.



Det är viktigt att notera att 1ML **inte är en depåtjänst**. Skapandet av ett konto ger inte tillgång till medel, kanaler eller betalningar för en nod. Det tjänar endast till att interagera med utforskaren från en deklarativ och informativ synvinkel.



När det gäller att lära sig eller upptäcka Lightning Network kan detta alternativ därför betraktas som **valfritt** och reserveras för mer avancerad användning.



## Slutsats



1ML är ett värdefullt verktyg för att observera och förstå Lightning Network från dess offentliga data. Det låter dig utforska nätverkets struktur, analysera noder och kanaler och spåra den övergripande utvecklingen av Lightning Network-adoption över tid. Utan behov av ett konto eller hantering av medel erbjuder 1ML en tillgänglig gateway för alla som vill fördjupa sin förståelse för hur Lightning fungerar.


Om du vill gå vidare med Lightning Network rekommenderar jag den kompletta kursen Introduktion till Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb