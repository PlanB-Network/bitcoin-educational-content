---
name: Inleiding tot formele cryptografie
goal: Een diepgaande introductie in de wetenschap en praktijk van cryptografie.
objectives: 

  - Verken Beale cijfers en moderne cryptografische methoden om de basis en historische concepten van cryptografie te begrijpen.
  - Verdiep je in getaltheorie, groepen en velden om de belangrijkste wiskundige concepten die ten grondslag liggen aan cryptografie onder de knie te krijgen.
  - Bestudeer het RC4-stroomcijfer en AES met een 128-bits sleutel om meer te leren over symmetrische cryptografische algoritmen.
  - Onderzoek het RSA cryptosysteem, sleuteldistributie en Hash functies om asymmetrische cryptografie te verkennen.


---
# Diep duik in cryptografie


Het is moeilijk om veel materialen te vinden die een goede middenweg bieden in het cryptografieonderwijs.


Aan de ene kant zijn er lange, formele verhandelingen die echt alleen toegankelijk zijn voor mensen met een sterke achtergrond in wiskunde, logica of een andere formele discipline. Aan de andere kant zijn er inleidingen op zeer hoog niveau die echt te veel details verbergen voor iedereen die op zijn minst een beetje nieuwsgierig is.


Deze inleiding tot cryptografie probeert de middenweg te vinden. Hoewel het relatief uitdagend en gedetailleerd zou moeten zijn voor iedereen die nieuw is in cryptografie, is het niet het konijnenhol van een typische fundamentele verhandeling.


+++

# Inleiding

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>


## Cursusoverzicht

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Welkom bij de CYP302 cursus!


Dit boek biedt een diepgaande introductie in de wetenschap en praktijk van cryptografie. Waar mogelijk richt het zich op conceptuele in plaats van formele uiteenzetting van het materiaal.


Deze educatieve inhoud is aangepast van het boek en de repo [JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Hoewel de auteur vriendelijk heeft ingestemd met het educatieve gebruik ervan, blijven alle intellectuele eigendomsrechten bij de oorspronkelijke maker.


**Motivatie en doelen**


Het is moeilijk om veel materialen te vinden die een goede middenweg bieden in het cryptografieonderwijs.


Aan de ene kant zijn er lange, formele verhandelingen die echt alleen toegankelijk zijn voor mensen met een sterke achtergrond in wiskunde, logica of een andere formele discipline. Aan de andere kant zijn er inleidingen op zeer hoog niveau die echt te veel details verbergen voor iedereen die op zijn minst een beetje nieuwsgierig is.


Deze inleiding tot cryptografie probeert de middenweg te vinden. Hoewel het relatief uitdagend en gedetailleerd zou moeten zijn voor iedereen die nieuw is in cryptografie, is het niet het konijnenhol van een typische fundamentele verhandeling.



**Doelpubliek**


Van ontwikkelaars tot de intellectueel nieuwsgierigen, dit boek is nuttig voor iedereen die meer wil dan een oppervlakkig begrip van cryptografie. Als het je doel is om cryptografie onder de knie te krijgen, dan is dit boek ook een goed startpunt.



**Leesrichtlijnen**


Het boek bevat momenteel zeven hoofdstukken: "Wat is cryptografie?" (Hoofdstuk 1), "Wiskundige grondslagen van cryptografie I" (Hoofdstuk 2), "Wiskundige grondslagen van cryptografie II" (Hoofdstuk 3), "Symmetrische cryptografie" (Hoofdstuk 4), "RC4 en AES" (Hoofdstuk 5), "Asymmetrische cryptografie" (Hoofdstuk 6), en "Het RSA cryptosysteem" (Hoofdstuk 7). Een laatste hoofdstuk, "Cryptografie in de praktijk", zal nog worden toegevoegd. Het richt zich op verschillende cryptografische toepassingen, waaronder transport Layer beveiliging, onion routing, en Bitcoin's waarde Exchange systeem.


Tenzij je een sterke achtergrond in wiskunde hebt, is getaltheorie waarschijnlijk het moeilijkste onderwerp in dit boek. Ik geef er een overzicht van in hoofdstuk 3, en het komt ook voor in de uitleg van AES in hoofdstuk 5 en het RSA cryptosysteem in hoofdstuk 7.


Als je echt moeite hebt met de formele details in deze delen van het boek, raad ik je aan om ze de eerste keer op hoog niveau te lezen.



**Erkenningen**


Jonathan Katz en Yehuda Lindell's _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL), 2015, was het meest invloedrijke boek om deze cursus vorm te geven. Een bijbehorende cursus is beschikbaar op Coursera onder de naam "Cryptography"


De belangrijkste aanvullende bronnen die behulpzaam zijn geweest bij het maken van het overzicht in dit boek zijn Simon Singh, _The Code Book_, Fourth Estate (Londen, 1999); Christof Paar en Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) en [een cursus gebaseerd op het boek van Paar genaamd "Introduction to Cryptography"](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); en Bruce Schneier, Applied Cryptography, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons).


Ik zal alleen zeer specifieke informatie en resultaten citeren die ik uit deze bronnen haal, maar ik wil hier mijn algemene dankbaarheid aan hen erkennen.


Voor lezers die na deze inleiding meer geavanceerde kennis over cryptografie willen, kan ik het boek van Katz en Lindell van harte aanbevelen. Katz's cursus op Coursera is iets toegankelijker dan het boek.



**Bijdragen**


Kijk alsjeblieft naar [het bijdragenbestand in het archief](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) voor wat richtlijnen over hoe je het project kunt ondersteunen.



**Notatie**


**Key terms:**


Sleuteltermen in de primers worden geïntroduceerd door ze vet te maken. Bijvoorbeeld, de introductie van het Rijndael cijfer als sleutelterm zou er als volgt uitzien: **Rijndael cijfer**.


Belangrijke termen worden expliciet gedefinieerd, tenzij het eigennamen zijn of de betekenis duidelijk uit de discussie naar voren komt.


Een definitie wordt meestal gegeven bij de introductie van een sleutelterm, hoewel het soms handiger is om de definitie tot een later punt te laten rusten.



**Beklemtoonde woorden en zinnen:**


Woorden en zinnen worden cursief weergegeven. De zin "Onthoud uw wachtwoord" ziet er bijvoorbeeld als volgt uit: *Onthoud uw wachtwoord*.



**Formele notatie:**


De formele notatie heeft voornamelijk betrekking op variabelen, willekeurige variabelen en verzamelingen.



- Variabelen: Deze worden meestal aangeduid met een kleine letter (bijvoorbeeld "x" of "y"). Soms worden ze voor de duidelijkheid met een hoofdletter aangegeven (bijvoorbeeld "M" of "K").
- Willekeurige variabelen: Deze worden altijd aangeduid met een hoofdletter (bijvoorbeeld "X" of "Y")
- Sets: Deze worden altijd aangeduid met vette hoofdletters (bijv. **S**)


Klaar om de fascinerende wereld van cryptografie te verkennen? Laten we gaan!


# Wat is cryptografie?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>


## De Beale-sleutels

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>


Laten we ons onderzoek op het gebied van cryptografie beginnen met een van de charmantere en vermakelijkere episodes uit de geschiedenis: dat van de Beale cijfers. [1]


Het verhaal van de Beale-cijfers is volgens mij eerder fictie dan werkelijkheid. Maar het zou als volgt zijn gegaan.


Zowel in de winter van 1820 als in die van 1822 verbleef ene Thomas J. Beale in een herberg van Robert Morriss in Lynchburg (Virginia). Aan het einde van Beale's tweede verblijf overhandigde hij Morriss een ijzeren kist met waardevolle papieren voor de bewaring.


Een paar maanden later ontving Morriss een brief van Beale gedateerd 9 mei 1822. Hierin werd de grote waarde van de inhoud van de ijzeren doos benadrukt en werden enkele instructies aan Morriss gegeven: als noch Beale noch een van zijn medewerkers ooit de doos zou komen opeisen, zou hij deze precies tien jaar na de datum van de brief (dat wil zeggen 9 mei 1832) moeten openen. Sommige van de papieren in de doos zouden in gewone tekst geschreven zijn. Verscheidene andere zouden echter "onbegrijpelijk zijn zonder de hulp van een sleutel" Deze "sleutel" zou dan in juni 1832 door een niet nader genoemde vriend van Beale aan Morriss worden geleverd.


Ondanks de duidelijke instructies opende Morriss de doos niet in mei 1832 en de mysterieuze vriend van Beale dook nooit op in juni van dat jaar. Pas in 1845 besloot de herbergier eindelijk de doos te openen. Morriss vond er een briefje in waarin werd uitgelegd hoe Beale en zijn compagnons goud en zilver hadden ontdekt in het Westen en dit, samen met wat juwelen, voor de veiligheid hadden begraven. Daarnaast bevatte de doos drie **cijferteksten**: dat zijn teksten geschreven in code die een **cryptografische sleutel**, of een geheim, en een bijbehorend algoritme nodig hebben om te ontsluiten. Het ontsluiten van een cijfertekst staat bekend als **decryptie**, terwijl het vergrendelen bekend staat als **encryptie**. (Zoals uitgelegd in Hoofdstuk 3 kan de term cijfer verschillende betekenissen hebben. In de naam "Beale ciphers" is het een afkorting voor ciphertexts)


De drie cijferteksten die Morriss vond in de ijzeren doos bestaan elk uit een reeks getallen gescheiden door komma's. Volgens Beale's notitie geven deze cijferteksten afzonderlijk de locatie van de schat, de inhoud van de schat en een lijst met namen van rechtmatige erfgenamen van de schat en hun aandelen (deze laatste informatie is relevant voor het geval Beale en zijn medewerkers de doos nooit komen opeisen).


Morris probeerde de drie cijferteksten twintig jaar lang te ontcijferen. Dit zou gemakkelijk zijn geweest met de sleutel. Maar Morriss had de sleutel niet en was niet succesvol in zijn pogingen om de originele teksten, of **plaintexts** zoals ze meestal worden genoemd in de cryptografie, terug te krijgen.


Aan het eind van zijn leven gaf Morriss de doos in 1862 door aan een vriend. Deze vriend publiceerde vervolgens een pamflet in 1885, onder het pseudoniem J.B. Ward. Het bevatte een beschrijving van de (vermeende) geschiedenis van de doos, de drie cijferteksten en een oplossing die hij had gevonden voor de tweede cijfertekst. (Blijkbaar is er één sleutel voor elke cijfertekst, en niet één sleutel die werkt op alle drie de cijferteksten zoals Beale oorspronkelijk suggereerde in zijn brief aan Morriss)


Je kunt de tweede cijfertekst zien in *Figuur 2* hieronder. [2] De sleutel tot deze cijfertekst is de Onafhankelijkheidsverklaring van de Verenigde Staten. De ontcijferingsprocedure komt neer op het toepassen van de volgende twee regels:



- Zoek voor elk getal n in de cijfertekst het n-de woord in de Onafhankelijkheidsverklaring van de Verenigde Staten
- Vervang het getal n door de eerste letter van het woord dat je hebt gevonden



*Figuur 1: Beale-cijfer nr. 2*


![Figure 1: Beale cipher no 2.](assets/Figure1-1.webp "Figure 1: Beale cipher no. 2")



Bijvoorbeeld, het eerste getal van de tweede cijfertekst is 115. Het 115e woord van de Onafhankelijkheidsverklaring is "ingesteld", dus de eerste letter van de klare tekst is "i" De cijfertekst geeft niet direct woordafstand en hoofdlettergebruik aan. Maar na het ontcijferen van de eerste paar woorden kun je logischerwijs afleiden dat het eerste woord van de klaartekst gewoon "I" was (De klare tekst begint met de zin "I have deposited in the county of Bedford.")


Na ontcijfering geeft het tweede bericht de gedetailleerde inhoud van de schat (goud, zilver en juwelen) en suggereert dat de schat begraven was in ijzeren potten en bedekt met rotsen in Bedford County (Virginia). Mensen houden van een goed mysterie, dus zijn er grote inspanningen geleverd om de andere twee Beale cijfers te ontcijferen, vooral het cijfer dat de locatie van de schat beschrijft. Zelfs verschillende prominente cryptografen hebben geprobeerd ze te ontcijferen. Tot nu toe is het echter nog niemand gelukt om de andere twee cijfers te ontcijferen.



**Noten:**


[1] Voor een goede samenvatting van het verhaal, zie Simon Singh, *The Code Book*, Fourth Estate (Londen, 1999), pp. 82-99. Een korte film van het verhaal werd gemaakt door Andrew Allen in 2010. Je kunt de film, "The Thomas Beale Cipher," [op zijn website](http://www.thomasbealecipher.com/) vinden.


[2] Deze afbeelding is beschikbaar op de Wikipedia pagina voor de Beale cijfers.



## Moderne cryptografie

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>


Kleurrijke verhalen zoals dat van de Beale cijfers associëren de meesten van ons met cryptografie. Toch verschilt moderne cryptografie op minstens vier belangrijke manieren van dit soort historische voorbeelden.


Ten eerste is cryptografie historisch gezien enkel bezig geweest met **geheimhouding** (of vertrouwelijkheid). [3] Cijferteksten worden gemaakt om ervoor te zorgen dat alleen bepaalde partijen toegang hebben tot de informatie in de klare tekst, zoals in het geval van de Beale cijfers. Opdat een encryptieschema dit doel goed zou dienen, zou het ontcijferen van de cijfertekst alleen mogelijk moeten zijn als je de sleutel hebt.


Moderne cryptografie houdt zich bezig met een breder scala aan thema's dan alleen geheimhouding. Deze thema's omvatten voornamelijk (1) **berichtintegriteit**-dat wil zeggen, verzekeren dat een bericht niet gewijzigd is; (2) **authenticiteit**-dat wil zeggen, verzekeren dat een bericht echt van een bepaalde afzender komt; en (3) **onweerlegbaarheid**-dat wil zeggen, verzekeren dat een afzender later niet valselijk kan ontkennen dat hij een bericht verzonden heeft. [4]


Een belangrijk onderscheid om in gedachten te houden is dus tussen een **encryptieschema** en een **cryptografisch schema**. Een encryptieschema houdt zich alleen bezig met geheimhouding. Terwijl een encryptieschema een cryptografisch schema is, is het omgekeerde niet waar. Een cryptografisch schema kan ook de andere hoofdthema's van cryptografie dienen, zoals integriteit, authenticiteit en onweerlegbaarheid.


De thema's integriteit en authenticiteit zijn net zo belangrijk als geheimhouding. Onze moderne communicatiesystemen zouden niet kunnen functioneren zonder garanties met betrekking tot de integriteit en authenticiteit van de communicatie. Onweerlegbaarheid is ook een belangrijk aandachtspunt, zoals voor digitale contracten, maar minder alomtegenwoordig nodig in cryptografische toepassingen dan geheimhouding, integriteit en authenticiteit.


Ten tweede is er bij klassieke versleutelingsschema's zoals de Beale-sleutels altijd sprake van één sleutel die gedeeld wordt door alle betrokken partijen. Veel moderne cryptografische schema's bevatten echter niet slechts één, maar twee sleutels: een **private** en een **publieke sleutel**. Terwijl de eerste in alle toepassingen privé moet blijven, is de tweede meestal publiekelijk bekend (vandaar hun respectievelijke namen). Op het gebied van encryptie kan de publieke sleutel worden gebruikt om het bericht te versleutelen, terwijl de privésleutel kan worden gebruikt om het bericht te ontsleutelen.


De tak van cryptografie die zich bezighoudt met schema's waarbij alle partijen één sleutel delen, staat bekend als **symmetrische cryptografie**. De enige sleutel in zo'n schema wordt meestal de **privésleutel** (of geheime sleutel) genoemd. De tak van cryptografie die zich bezighoudt met schema's die een privaat-publiek sleutelpaar vereisen staat bekend als **asymmetrische cryptografie**. Deze takken worden soms ook respectievelijk **private sleutel cryptografie** en **publieke sleutel cryptografie** genoemd (hoewel dit tot verwarring kan leiden, aangezien publieke sleutel cryptografische schema's ook privésleutels hebben).


De opkomst van asymmetrische cryptografie aan het einde van de jaren 1970 is een van de belangrijkste gebeurtenissen in de geschiedenis van cryptografie. Zonder dit zouden de meeste van onze moderne communicatiesystemen, waaronder Bitcoin, niet mogelijk zijn, of op zijn minst erg onpraktisch.


Belangrijk is dat moderne cryptografie niet uitsluitend de studie is van symmetrische en assymetrische sleutel cryptografische schema's (hoewel dat een groot deel van het veld beslaat). Cryptografie houdt zich bijvoorbeeld ook bezig met Hash functies en pseudorandom getalgeneratoren, en je kunt toepassingen bouwen op deze primitieven die niet gerelateerd zijn aan symmetrische of assymetrische sleutelcryptografie.


Ten derde waren klassieke versleutelingsschema's, zoals die gebruikt werden in de Beale cijfers, meer kunst dan wetenschap. Hun veiligheid was grotendeels gebaseerd op intuïtie over hun complexiteit. Ze werden meestal gepatcht als er een nieuwe aanval op hen werd ontdekt, of helemaal geschrapt als de aanval bijzonder ernstig was. Moderne cryptografie is echter een rigoureuze wetenschap met een formele, wiskundige aanpak voor zowel het ontwikkelen als het analyseren van cryptografische schema's. [5]


In het bijzonder draait het bij moderne cryptografie om formele **bewijzen van veiligheid**. Elk veiligheidsbewijs voor een cryptografisch schema verloopt in drie stappen:


1.	De verklaring van een **cryptografische definitie van beveiliging**, dat wil zeggen, een verzameling beveiligingsdoelen en de dreiging die uitgaat van de aanvaller.

2.	De verklaring van wiskundige aannames met betrekking tot de rekencomplexiteit van het schema. Een cryptografisch schema kan bijvoorbeeld een pseudo-willekeurige getallengenerator bevatten. Hoewel we het bestaan hiervan niet kunnen bewijzen, kunnen we wel aannemen dat deze bestaat.

3.	De uiteenzetting van een wiskundig **bewijs van beveiliging** van het schema op basis van het formele begrip van beveiliging en eventuele wiskundige aannames.


Ten vierde, terwijl cryptografie in het verleden vooral werd gebruikt in militaire omgevingen, is het in het digitale tijdperk doorgedrongen in onze dagelijkse activiteiten. Of je nu online bankiert, berichten plaatst op sociale media, een product bij Amazon koopt met je creditcard of een vriend Bitcoin fooi geeft, cryptografie is de conditio sine qua non van ons digitale tijdperk.


Gezien deze vier aspecten van moderne cryptografie, kunnen we moderne **cryptografie** karakteriseren als de wetenschap die zich bezighoudt met de formele ontwikkeling en analyse van cryptografische schema's om digitale informatie te beveiligen tegen aanvallen van tegenstanders. [6] Veiligheid moet hier breed worden opgevat als het voorkomen van aanvallen die de geheimhouding, integriteit, authenticatie en/of onweerlegbaarheid in communicatie aantasten.


Cryptografie kan het best worden gezien als een subdiscipline van **cyberbeveiliging**, die zich bezighoudt met het voorkomen van diefstal, beschadiging en misbruik van computersystemen. Merk op dat veel cyberbeveiligingskwesties weinig of slechts gedeeltelijk verband houden met cryptografie.


Als een bedrijf bijvoorbeeld dure servers lokaal onderbrengt, kan het zich zorgen maken over het beveiligen van deze hardware tegen diefstal en schade. Hoewel dit een cyberbeveiligingskwestie is, heeft het weinig te maken met cryptografie.


Een ander voorbeeld: **phishing-aanvallen** zijn een veelvoorkomend probleem in onze moderne tijd. Deze aanvallen proberen mensen te misleiden via een e-mail of een ander berichtmedium om gevoelige informatie zoals wachtwoorden of creditcardnummers af te staan. Hoewel cryptografie tot op zekere hoogte Address phishing-aanvallen kan helpen, is er voor een allesomvattende aanpak meer nodig dan alleen wat cryptografie.



**Noten:**


[3] Om precies te zijn, de belangrijkste toepassingen van cryptografische schema's hebben te maken met geheimhouding. Kinderen gebruiken bijvoorbeeld vaak eenvoudige cryptografische schema's voor de "lol". Geheimhouding is dan niet echt een probleem.


[4] Bruce Schneier, *Applied Cryptography*, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons), p. 2.


[5] Zie Jonathan Katz en Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), met name pp. 16-23, voor een goede beschrijving.


[6] Cf. Katz en Lindell, ibid., p. 3. Ik denk dat hun karakterisering enkele problemen heeft, dus presenteer ik hier een iets andere versie van hun verklaring.



## Open communicatie

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>


Moderne cryptografie is ontworpen om veiligheidswaarborgen te bieden in een **open communicatie** omgeving. Als ons communicatiekanaal zo goed beveiligd is dat afluisteraars geen kans hebben om onze berichten te manipuleren of zelfs maar te observeren, dan is cryptografie overbodig. De meeste van onze communicatiekanalen zijn echter niet zo goed beveiligd.


De ruggengraat van de communicatie in de moderne wereld is een enorm netwerk van glasvezelkabels. Telefoneren, televisie kijken en internetten in een modern huishouden is over het algemeen afhankelijk van dit netwerk van glasvezelkabels (een klein percentage vertrouwt uitsluitend op satellieten). Het is waar dat je verschillende dataverbindingen in huis kunt hebben, zoals coaxkabel, (asymmetrische) digitale abonneelijn en glasvezelkabel. Maar, tenminste in de ontwikkelde wereld, verbinden deze verschillende datamedia zich buiten je huis snel met een knooppunt in een enorm netwerk van glasvezelkabels dat de hele wereld met elkaar verbindt. Uitzonderingen zijn enkele afgelegen gebieden in de ontwikkelde wereld, zoals in de Verenigde Staten en Australië, waar dataverkeer nog steeds aanzienlijke afstanden kan afleggen via traditionele koperen telefoonkabels.


Het zou onmogelijk zijn om te voorkomen dat potentiële aanvallers fysiek toegang krijgen tot dit netwerk van kabels en de ondersteunende infrastructuur. In feite weten we al dat de meeste van onze gegevens worden onderschept door verschillende nationale inlichtingendiensten op cruciale kruispunten van het internet.[7] Dit omvat alles van Facebook-berichten tot website-adressen die je bezoekt.


Terwijl voor het afluisteren van gegevens op grote schaal een machtige tegenstander nodig is, zoals een nationale inlichtingendienst, kunnen aanvallers met weinig middelen eenvoudig proberen om op een meer lokale schaal af te luisteren. Hoewel dit kan gebeuren op het niveau van het aftappen van draden, is het veel eenvoudiger om alleen draadloze communicatie te onderscheppen.


De meeste van onze lokale netwerkgegevens - thuis, op kantoor of in een café - gaan tegenwoordig via radiogolven naar draadloze toegangspunten op all-in-one routers in plaats van via fysieke kabels. Een aanvaller heeft dus weinig middelen nodig om lokaal verkeer te onderscheppen. Dit is vooral verontrustend omdat de meeste mensen weinig doen om de gegevens die over hun lokale netwerk gaan te beschermen. Daarnaast kunnen potentiële aanvallers zich ook richten op onze mobiele breedbandverbindingen, zoals 3G, 4G en 5G. Al deze draadloze communicatie is een gemakkelijk doelwit voor aanvallers.


Daarom is het idee om communicatie geheim te houden door het communicatiekanaal te beschermen een hopeloos waanzinnig streven voor een groot deel van de moderne wereld. Alles wat we weten rechtvaardigt ernstige paranoia: je moet er altijd van uitgaan dat er iemand meeluistert. En cryptografie is het belangrijkste gereedschap dat we hebben om enige vorm van veiligheid te verkrijgen in deze moderne omgeving.



**Noten:**


[7] Zie bijvoorbeeld Olga Khazan, "The creepy, long-standing practice of undersea cable tapping", *The Atlantic*, 16 juli 2013 (beschikbaar op [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).



# Wiskundige grondslagen van cryptografie 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>



## Willekeurige variabelen

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>


Cryptografie is gebaseerd op wiskunde. En als je meer dan een oppervlakkig begrip van cryptografie wilt opbouwen, moet je vertrouwd zijn met die wiskunde.


Dit hoofdstuk introduceert de meeste basiswiskunde die je tegenkomt bij het leren van cryptografie. De onderwerpen omvatten random variabelen, modulo operaties, XOR operaties en pseudorandomheid. Je zou het materiaal in deze secties moeten beheersen voor een niet oppervlakkig begrip van cryptografie.


De volgende sectie gaat over getaltheorie, wat veel uitdagender is.


### Willekeurige variabelen


Een willekeurige variabele wordt meestal aangeduid met een niet-vetgedrukte hoofdletter. We kunnen het bijvoorbeeld hebben over een willekeurige variabele $X$, een willekeurige variabele $Y$ of een willekeurige variabele $Z$. Dit is de notatie die ik vanaf nu ook zal gebruiken.


Een **willekeurige variabele** kan twee of meer mogelijke waarden aannemen, elk met een bepaalde positieve waarschijnlijkheid. De mogelijke waarden staan in de **outcome set**.


Telkens wanneer je een willekeurige variabele **monstert**, trek je een bepaalde waarde uit de verzameling uitkomsten volgens de gedefinieerde waarschijnlijkheden.


Laten we een eenvoudig voorbeeld nemen. Stel dat een variabele X als volgt is gedefinieerd:



- X heeft de uitkomstverzameling ${1,2}$


$$
Pr[X = 1] = 0.5
$$


$$
Pr[X = 2] = 0.5
$$


Het is gemakkelijk om te zien dat $X$ een willekeurige variabele is. Ten eerste zijn er twee of meer mogelijke waarden die $X$ kan aannemen, namelijk $1$ en $2$. Ten tweede heeft elke mogelijke waarde een positieve kans om voor te komen wanneer je $X$ bemonstert, namelijk $0,5$.


Het enige dat een willekeurige variabele nodig heeft is een verzameling uitkomsten met twee of meer mogelijkheden, waarbij elke mogelijkheid een positieve kans heeft om voor te komen bij het nemen van de steekproef. In principe kan een willekeurige variabele dus abstract gedefinieerd worden, zonder enige context. In dit geval zou je "steekproeven" kunnen zien als het uitvoeren van een natuurlijk experiment om de waarde van de willekeurige variabele te bepalen.


De variabele $X$ hierboven is abstract gedefinieerd. Je zou de bovenstaande variabele $X$ dus kunnen zien als het opgooien van een eerlijke munt en "2" toekennen bij kop en "1" bij munt. Voor elke steekproef van $X$ gooi je de munt opnieuw op.


Als alternatief kun je ook denken aan een steekproef van $X$, als het gooien van een eerlijke dobbelsteen en een "2" toekennen als de dobbelsteen op $1$, $3$ of $4$ valt, en een "1" toekennen als de dobbelsteen op $2$, $5$ of $6$ valt. Elke keer dat je $X$ bemonstert, gooi je opnieuw met de dobbelsteen.


Echt, elk natuurlijk experiment waarmee je de waarschijnlijkheden van de mogelijke waarden van $X$ hierboven zou kunnen definiëren, kan je je voorstellen met betrekking tot de tekening.


Vaak worden willekeurige variabelen echter niet alleen abstract geïntroduceerd. In plaats daarvan heeft de verzameling van mogelijke uitkomstwaarden een expliciete betekenis in de echte wereld (in plaats van alleen als getallen). Bovendien kunnen deze uitkomstwaarden gedefinieerd worden aan de hand van een specifiek type experiment (in plaats van als een willekeurig natuurlijk experiment met die waarden).


Laten we nu een voorbeeld bekijken van variabele $X$ die niet abstract gedefinieerd is. X wordt als volgt gedefinieerd om te bepalen welk van twee teams een voetbalwedstrijd begint:



- $X$ heeft de uitkomstverzameling {rood trapt af, blauw trapt af}
- Gooi een bepaalde munt $C$ op: munt = "rood trapt af"; kop = "blauw trapt af"


$$
Pr [X = \text{red kicks off}] = 0.5
$$


$$
Pr [X = \text{blue kicks off}] = 0.5
$$


In dit geval krijgt de uitkomstenverzameling van X een concrete betekenis, namelijk welk team begint in een voetbalwedstrijd. Bovendien worden de mogelijke uitkomsten en hun bijbehorende waarschijnlijkheden bepaald door een concreet experiment, namelijk het opgooien van een bepaalde munt $C$.


In discussies over cryptografie worden willekeurige variabelen meestal geïntroduceerd tegen een resultaatverzameling met betekenis in de echte wereld. Dit kan de verzameling zijn van alle berichten die versleuteld kunnen worden, bekend als de berichtenruimte, of de verzameling van alle sleutels waaruit de partijen die de versleuteling gebruiken kunnen kiezen, bekend als de sleutelruimte.


Willekeurige variabelen in discussies over cryptografie worden echter meestal niet gedefinieerd tegen een specifiek natuurlijk experiment, maar tegen elk experiment dat de juiste kansverdelingen kan opleveren.


Willekeurige variabelen kunnen discrete of continue kansverdelingen hebben. Willekeurige variabelen met een **discrete kansverdeling** - dat wil zeggen discrete willekeurige variabelen - hebben een eindig aantal mogelijke uitkomsten. De willekeurige variabele $X$ in beide voorbeelden tot nu toe was discreet.


**Continue random variabelen** kunnen in plaats daarvan waarden aannemen in één of meer intervallen. Je zou bijvoorbeeld kunnen zeggen dat een willekeurige variabele bij bemonstering elke reële waarde tussen 0 en 1 aanneemt en dat elk reëel getal in dit interval even waarschijnlijk is. Binnen dit interval zijn er oneindig veel waarden mogelijk.


Voor cryptografische discussies hoef je alleen discrete willekeurige variabelen te begrijpen. Elke discussie over willekeurige variabelen vanaf hier moet daarom worden opgevat als een verwijzing naar discrete willekeurige variabelen, tenzij specifiek anders vermeld.



### Grafieken van willekeurige variabelen


De mogelijke waarden en bijbehorende waarschijnlijkheden voor een willekeurige variabele kunnen gemakkelijk gevisualiseerd worden door middel van een grafiek. Neem bijvoorbeeld de willekeurige variabele $X$ uit de vorige paragraaf met een uitkomstverzameling van ${1, 2}$, en $Pr [X = 1] = 0,5$ en $Pr [X = 2] = 0,5$. We geven zo'n willekeurige variabele meestal weer in de vorm van een staafdiagram zoals in *Figuur 1*.


*Figuur 1: Willekeurige variabele X*


![Figure 1: Random variable X.](assets/Figure2-1.webp)


De brede balken in *Figuur 1* zijn natuurlijk niet bedoeld om te suggereren dat de willekeurige variabele $X$ echt continu is. In plaats daarvan zijn de balken breed gemaakt om visueel aantrekkelijker te zijn (gewoon een lijn recht omhoog geeft een minder intuïtieve visualisatie).



### Uniforme variabelen


In de uitdrukking "willekeurige variabele" betekent de term "willekeurig" gewoon "probabilistisch". Met andere woorden, het betekent gewoon dat twee of meer mogelijke uitkomsten van de variabele zich met een bepaalde waarschijnlijkheid voordoen. Deze uitkomsten hoeven echter *niet* per se even waarschijnlijk te zijn (hoewel de term "willekeurig" wel degelijk die betekenis kan hebben in andere contexten).


Een **uniforme variabele** is een speciaal geval van een willekeurige variabele. Ze kan twee of meer waarden aannemen, allemaal met een gelijke waarschijnlijkheid. De willekeurige variabele $X$ in *Figuur 1* is duidelijk een uniforme variabele, want beide mogelijke uitkomsten komen voor met een kans van $0,5$. Er zijn echter veel willekeurige variabelen die geen uniforme variabele zijn.


Beschouw bijvoorbeeld de willekeurige variabele $Y$. Deze heeft een uitkomstverzameling {1, 2, 3, 8, 10} en de volgende kansverdeling:


$$
\Pr[Y = 1] = 0.25
$$


$$
\Pr[Y = 2] = 0.35
$$


$$
\Pr[Y = 3] = 0.1
$$


$$
\Pr[Y = 8] = 0.25
$$


$$
\Pr[Y = 10] = 0.05
$$



Hoewel twee mogelijke uitkomsten inderdaad een gelijke waarschijnlijkheid hebben, namelijk $1$ en $8$, kan $Y$ ook bepaalde waarden aannemen met een andere waarschijnlijkheid dan $0,25$ bij steekproeftrekking. Hoewel $Y$ dus inderdaad een willekeurige variabele is, is het geen uniforme variabele.


Een grafische voorstelling van $Y$ wordt gegeven in *Figuur 2*.


*Figuur 2: Willekeurige variabele Y*


![Figure 2: Random variable Y.](assets/Figure2-2.webp "Figure 2: Random variable Y")


Als laatste voorbeeld nemen we de willekeurige variabele Z. Deze heeft de uitkomstverzameling {1,3,7,11,12} en de volgende kansverdeling:


$$
\Pr[Z = 2] = 0.2
$$


$$
\Pr[Z = 3] = 0.2
$$


$$
\Pr[Z = 9] = 0.2
$$


$$
\Pr[Z = 11] = 0.2
$$


$$
\Pr[Z = 12] = 0.2
$$


Je ziet het afgebeeld in *Figuur 3*. De willekeurige variabele Z is, in tegenstelling tot Y, een uniforme variabele, omdat alle waarschijnlijkheden voor de mogelijke waarden bij bemonstering gelijk zijn.



*Figuur 3: Willekeurige variabele Z*


![Figure 3: Random variable Z.](assets/Figure2-3.webp "Figure 3: Random variable Z")



### Voorwaardelijke waarschijnlijkheid


Stel dat Bob van plan is om uniform een dag uit het laatste kalenderjaar te kiezen. Wat is de kans dat de geselecteerde dag in de zomer valt?


Zolang we denken dat Bob's proces inderdaad echt uniform zal zijn, moeten we concluderen dat er 1/4 kans is dat Bob een dag in de zomer selecteert. Dit is de **onvoorwaardelijke kans** dat de willekeurig gekozen dag in de zomer valt.


Stel nu dat Bob, in plaats van uniform een kalenderdag te trekken, alleen uniform kiest uit die dagen waarop de middagtemperatuur in Crystal Lake (New Jersey) 21 graden Celcius of hoger was. Gegeven deze extra informatie, wat kunnen we dan concluderen over de kans dat Bob een dag in de zomer kiest?


We zouden echt een andere conclusie moeten trekken dan voorheen, zelfs zonder verdere specifieke informatie (bijvoorbeeld de temperatuur op het middaguur van elke dag in het afgelopen kalenderjaar).


Aangezien Crystal Lake in New Jersey ligt, verwachten we zeker niet dat de temperatuur 's middags 21 graden Celsius of hoger is in de winter. In plaats daarvan is het veel waarschijnlijker dat het een warme dag in de lente of herfst is, of een dag ergens in de zomer. Als we dus weten dat de middagtemperatuur in Crystal Lake op de geselecteerde dag 21 graden Celsius of hoger was, wordt de kans dat de door Bob geselecteerde dag in de zomer valt veel groter. Dit is de **voorwaardelijke kans** dat de willekeurig gekozen dag in de zomer valt, gegeven dat de middagtemperatuur bij Crystal Lake 21 graden Celsius of hoger was.


In tegenstelling tot het vorige voorbeeld kunnen de waarschijnlijkheden van twee gebeurtenissen ook volledig ongerelateerd zijn. In dat geval zeggen we dat ze **onafhankelijk** zijn.


Stel bijvoorbeeld dat een bepaalde eerlijke munt op kop is gevallen. Gegeven dit feit, wat is dan de kans dat het morgen regent? De voorwaardelijke kans zou in dit geval hetzelfde moeten zijn als de onvoorwaardelijke kans dat het morgen regent, omdat een munt opgooien over het algemeen geen invloed heeft op het weer.


We gebruiken een "|" symbool voor het uitschrijven van voorwaardelijke waarschijnlijkheidsuitspraken. Bijvoorbeeld, de waarschijnlijkheid van gebeurtenis $A$ gegeven dat gebeurtenis $B$ heeft plaatsgevonden kan als volgt worden geschreven:


$$
Pr[A|B]
$$


Dus als twee gebeurtenissen, $A$ en $B$, onafhankelijk zijn, dan is:


$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$


De voorwaarde voor onafhankelijkheid kan als volgt worden vereenvoudigd:


$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$



Een belangrijk resultaat in de kansrekening staat bekend als **Bayes Theorem**. Deze stelling komt erop neer dat $Pr[A|B]$ als volgt herschreven kan worden:



$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$



In plaats van voorwaardelijke kansen te gebruiken bij specifieke gebeurtenissen, kunnen we ook kijken naar de voorwaardelijke kansen bij twee of meer willekeurige variabelen over een verzameling mogelijke gebeurtenissen. Stel dat er twee willekeurige variabelen zijn, $X$ en $Y$. We kunnen elke mogelijke waarde voor $X$ aanduiden met $x$ en elke mogelijke waarde voor $Y$ met $y$. We kunnen dan zeggen dat twee willekeurige variabelen onafhankelijk zijn als de volgende stelling geldt:


$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$


voor alle $x$ en $y$.


Laten we iets duidelijker zijn over wat deze uitspraak betekent.


Stel dat de uitkomstenverzamelingen voor $X$ en $Y$ als volgt gedefinieerd zijn: **X** = ${x_1, x_2, \ldots, x_i, \ldots, x_n}$ en **Y** = ${y_1, y_2, \ldots, y_i, \ldots, y_m}$. (Het is gebruikelijk om reeksen waarden aan te geven met vetgedrukte hoofdletters)


Stel nu dat je $Y$ bemonstert en $y_1$ waarneemt. De bovenstaande verklaring vertelt ons dat de kans dat we nu $x_1$ verkrijgen uit de steekproef van $X$ precies dezelfde is als wanneer we nooit $y_1$ hadden waargenomen. Dit geldt voor elke $y_i$ die we hadden kunnen trekken uit onze eerste steekproef van $Y$. Ten slotte geldt dit niet alleen voor $x_1$. Voor elke $x_i$ wordt de kans op voorkomen niet beïnvloed door de uitkomst van een steekproef van $Y$. Dit alles geldt ook voor het geval waarin $X$ eerst wordt bemonsterd.


Laten we onze discussie afsluiten met een iets filosofischer punt. In elke echte situatie wordt de waarschijnlijkheid van een bepaalde gebeurtenis altijd beoordeeld aan de hand van een bepaalde verzameling informatie. Er bestaat geen "onvoorwaardelijke waarschijnlijkheid" in de strikte zin van het woord.


Stel bijvoorbeeld dat ik je vraag naar de waarschijnlijkheid dat varkens zullen vliegen in 2030. Hoewel ik je geen verdere informatie geef, weet je duidelijk veel over de wereld die je oordeel kan beïnvloeden. Je hebt nog nooit varkens zien vliegen. Je weet dat de meeste mensen niet verwachten dat ze zullen vliegen. Je weet dat ze niet echt gebouwd zijn om te vliegen. En ga zo maar door.


Als we het dus hebben over een "onvoorwaardelijke waarschijnlijkheid" van een bepaalde gebeurtenis in een reële context, dan kan die term eigenlijk alleen betekenis hebben als we er zoiets mee bedoelen als "de waarschijnlijkheid zonder verdere expliciete informatie". Elk begrip van een "voorwaardelijke waarschijnlijkheid" moet dus altijd worden begrepen in relatie tot specifieke informatie.


Ik zou je bijvoorbeeld kunnen vragen naar de waarschijnlijkheid dat varkens zullen vliegen in 2030, nadat ik je bewijs heb gegeven dat sommige geiten in Nieuw-Zeeland hebben leren vliegen na een paar jaar training. In dat geval zul je waarschijnlijk je inschatting van de waarschijnlijkheid dat varkens zullen vliegen in 2030 bijstellen. Dus de waarschijnlijkheid dat varkens zullen vliegen in 2030 is afhankelijk van dit bewijs over geiten in Nieuw-Zeeland.



## De modulo-bewerking

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>


### Modulo


De meest elementaire uitdrukking met de **modulo-operatie** heeft de volgende vorm: $x \mod y$.


De variabele $x$ wordt het dividend genoemd en de variabele $y$ de deler. Om een modulo-operatie uit te voeren met een positief dividend en een positieve deler, bepaal je gewoon de rest van de deling.


Neem bijvoorbeeld de uitdrukking $25 \mod 4$. Het getal 4 gaat in totaal 6 keer over in het getal 25. De rest van die deling is 1. Dus is $25 mod 4$ gelijk aan 1. De rest van die deling is 1. Daarom is $25 \mod 4$ gelijk aan 1. Op dezelfde manier kunnen we de onderstaande uitdrukkingen berekenen:



- $29 {mod 30 = 29$ (omdat 30 in totaal 0 keer in 29 gaat en de rest 29 is)
- $42 {mod 2 = 0$ (omdat 2 in totaal 21 keer in 42 gaat en de rest 0 is)
- $12 {mod 5 = 2$ (omdat 5 in totaal 2 keer in 12 gaat en de rest 2 is)
- $20 {mod 8 = 4$ (omdat 8 in totaal 2 keer in 20 gaat en de rest 4 is)


Als het dividend of de deler negatief is, kunnen modulo-bewerkingen anders worden afgehandeld door programmeertalen.


Je zult zeker gevallen tegenkomen met een negatief dividend in cryptografie. In deze gevallen is de typische aanpak als volgt:



- Bepaal eerst de dichtstbijzijnde waarde *lager dan of gelijk aan* het dividend waarin de deler deelt met een rest van nul. Noem die waarde $p$.
- Als het dividend $x$ is, dan is het resultaat van de modulo-operatie de waarde van $x - p$.


Stel bijvoorbeeld dat het dividend $-20$ en de deler 3 is. De dichtstbijzijnde waarde lager dan of gelijk aan $-20$ waarin 3 gelijkmatig deelt is $-21$. De waarde van $x - p$ is in dit geval $-20 - (-21)$. Dit is gelijk aan 1 en dus is $-20mod 3$ gelijk aan 1. Op dezelfde manier kunnen we de onderstaande uitdrukkingen berekenen:



- $-8 = 5 = 2$
- $-19 √ 16 = 13$
- $-14 # 6 = 4$


Wat de notatie betreft, zul je meestal de volgende uitdrukkingen zien: $x = [y mod mod z]$. Door de haakjes geldt de modulo-operatie in dit geval alleen voor de rechterkant van de uitdrukking. Als $y$ bijvoorbeeld gelijk is aan 25 en $z$ gelijk is aan 4, dan is $x$ gelijk aan 1.


Zonder haakjes werkt de modulo bewerking op beide zijden van een uitdrukking. Stel bijvoorbeeld de volgende uitdrukking: $x = y \mod z$. Als $y$ gelijk is aan 25 en $z$ gelijk is aan 4, dan weten we alleen dat $x \mod 4$ gelijk is aan 1. Dit is consistent met elke waarde voor $x$ uit de verzameling ${\ldots,-7, -3, 1, 5, 9,\ldots}$.


De tak van wiskunde die modulo-bewerkingen op getallen en uitdrukkingen uitvoert, wordt **modulair rekenen** genoemd. Je kunt deze tak beschouwen als rekenen voor gevallen waarin de getallenlijn niet oneindig lang is. Hoewel we modulo-bewerkingen meestal tegenkomen voor (positieve) gehele getallen in cryptografie, kun je ook modulo-bewerkingen uitvoeren met alle reële getallen.


### Het verschuivingscijfer


De modulo-operatie komt vaak voor in cryptografie. Laten we ter illustratie eens kijken naar een van de beroemdste historische versleutelingsschema's: het shift cijfer.


Laten we het eerst definiëren. Stel dat er een woordenboek *D* is dat alle letters van het Engelse alfabet, in volgorde, gelijkstelt aan de verzameling getallen ${0, 1, 2, puntjes, 25}$. Ga uit van een berichtenruimte **M**. Het **shift cipher** is dan een versleutelingsschema dat als volgt gedefinieerd is:



- Selecteer uniform een sleutel $k$ uit de sleutelruimte **K**, waarbij **K** = ${0, 1, 2, \ldots, 25}$ [1]
- Versleutel een bericht $m in \mathbf{M}$ als volgt:
    - Verdeel $m$ in de afzonderlijke letters $m_0, m_1, \ldots, m_i, \ldots, m_l$
    - Converteer elke $m_i$ naar een getal volgens *D*
    - Voor elke $m_i$, $c_i = [(m_i + k) √ 26]$
    - Converteer elke $c_i$ naar een letter volgens *D*
    - Combineer dan $c_0, c_1, c_ldots, c_l$ om de cijfertekst $c$ te verkrijgen
- Ontcijfer een cijfertekst $c$ als volgt:
    - Converteer elke $c_i$ naar een getal volgens *D*
    - Voor elke $c_i$, $m_i = [(c_i - k) 26]$
    - Converteer elke $m_i$ naar een letter volgens *D*
    - Combineer dan $m_0, m_1, \ldots, m_l$ om het oorspronkelijke bericht $m$ te verkrijgen


De modulo operator in het shift cijfer zorgt ervoor dat letters omwikkeld worden, zodat alle cijfertekst letters gedefinieerd worden. Ter illustratie, bekijk de toepassing van het shift cijfer op het woord "DOG".


Stel dat je een sleutel uniform hebt geselecteerd om de waarde 17 te hebben. De letter "O" komt overeen met 15. Zonder de modulo-operatie zou de optelling van dit klaartekstgetal met de sleutel een cijfertekstgetal van 32 opleveren. Dit cijfertekstnummer kan echter niet worden omgezet in een cijfertekstletter, aangezien het Engelse alfabet slechts 26 letters telt. De modulo-operatie zorgt ervoor dat het cijfertekstgetal in werkelijkheid 6 is (het resultaat van $32 mod 26$), wat overeenkomt met de cijfertekstletter "G".


De volledige versleuteling van het woord "DOG" met een sleutelwaarde van 17 is als volgt:



- Bericht = DOG = D,O,G = 3,15,6
- $c_0 = [(3 + 17) \ 26] = [(20) \ 26] = 20 = U$
- $c_1 = [(15 + 17) \ 26] = [(32) \ 26] = 6 = G$
- $c_2 = [(6 + 17) \ 26] = [(23) \ 26] = 23 = X$
- $c = UGX$


Iedereen kan intuïtief begrijpen hoe het shift cijfer werkt en het waarschijnlijk zelf gebruiken. Om je kennis van cryptografie te vergroten is het echter belangrijk om meer vertrouwd te raken met formalisatie, aangezien de schema's veel moeilijker worden. Daarom zijn de stappen voor het shift cijfer geformaliseerd.



**Noten:**


[1] We kunnen deze uitspraak precies definiëren met behulp van de terminologie uit de vorige paragraaf. Laat een uniforme variabele $K$ $K$ hebben als zijn verzameling van mogelijke uitkomsten. Dus:


$$
Pr[K = 0] = \frac{1}{26}
$$


$$
Pr[K = 1] = \frac{1}{26}
$$


...enzovoort. Monster de uniforme variabele $K$ eenmaal om een bepaalde sleutel te verkrijgen.



## De XOR-bewerking

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>


Alle computergegevens worden verwerkt, opgeslagen en verzonden over netwerken op bitniveau. Alle cryptografische schema's die worden toegepast op computergegevens werken ook op bit-niveau.


Stel bijvoorbeeld dat je een e-mail hebt getypt in je e-mailprogramma. Elke versleuteling die je toepast, gebeurt niet rechtstreeks op de ASCII-tekens van je e-mail. In plaats daarvan wordt het toegepast op de bit-representatie van de letters en andere symbolen in je e-mail.


Een belangrijke wiskundige operatie om te begrijpen voor moderne cryptografie, naast de modulo operatie, is die van de **XOR operatie**, of "exclusive or" operatie. Deze bewerking heeft als invoer twee bits en als uitvoer een ander bit. De XOR-bewerking wordt simpelweg "XOR" genoemd. De uitkomst is 0 als de twee bits hetzelfde zijn en 1 als de twee bits verschillend zijn. Hieronder zie je de vier mogelijkheden. Het symbool $oplus$ staat voor "XOR":



- $0 \oplus 0 = 0$
- $0 \oplus 1 = 1$
- $1 \oplus 0 = 1$
- $1 \oplus 1 = 0$


Ter illustratie, stel dat je een bericht $m_1$ (01111001) en een bericht $m_2$ (01011001) hebt. De XOR-bewerking van deze twee berichten zie je hieronder.



- $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$


Het proces is eenvoudig. Eerst XOR je de meest linkse bits van $m_1$ en $m_2$. In dit geval is dat $0 \oplus 0 = 0$. Vervolgens XOR je het tweede paar bits van links. In dit geval is dat $1 \oplus 1 = 0$. Je gaat door met dit proces totdat je de XOR-bewerking op de meest rechtse bits hebt uitgevoerd.


Het is eenvoudig te zien dat de XOR-bewerking commutatief is, namelijk dat $m_1 \oplus m_2 = m_2 \oplus m_1$. Bovendien is de XOR operatie ook associatief. Dat wil zeggen, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.


Een XOR-bewerking op twee strings van verschillende lengtes kan verschillende interpretaties hebben, afhankelijk van de context. We zullen ons hier niet bezighouden met XOR-bewerkingen op strings van verschillende lengtes.


Een XOR-bewerking is gelijkwaardig aan het speciale geval van het uitvoeren van een modulo-bewerking op de optelling van bits als de deler 2 is. Je kunt de gelijkwaardigheid zien in de volgende resultaten:



- $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
- $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
- $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
- $(1 + 1) \mod 2 = 1 \oplus 1 = 0$


## Pseudorandomheid

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>


In onze bespreking van willekeurige en uniforme variabelen hebben we een specifiek onderscheid gemaakt tussen "willekeurig" en "uniform". Dat onderscheid wordt in de praktijk meestal gehandhaafd bij het beschrijven van willekeurige variabelen. In onze huidige context moet dit onderscheid echter worden weggelaten en worden "random" en "uniform" synoniem gebruikt. Ik zal aan het eind van dit hoofdstuk uitleggen waarom.


Om te beginnen kunnen we een binaire string met een lengte $n$ **willekeurig** (of **uniform**) noemen, als deze het resultaat is van het bemonsteren van een uniforme variabele $S$ die elke binaire string met een dergelijke lengte $n$ een gelijke selectiekans geeft.


Stel bijvoorbeeld de verzameling van alle binaire tekenreeksen met lengte 8: ${0000, 0000, 0001, punten, 1111, 1111}$. (Het is gebruikelijk om een 8-bits string in twee kwartetten te schrijven, elk een **nibble** genoemd) We noemen deze reeks strings **$S_8$**.


Volgens bovenstaande definitie kunnen we een bepaalde binaire string met lengte 8 willekeurig (of uniform) noemen als deze het resultaat is van een steekproef van een uniforme variabele $S$ die elke string in **$S_8$** een gelijke selectiekans geeft. Aangezien de verzameling **$S_8$** $2^8$ Elements bevat, zou de selectiekans bij bemonstering $1/2^8$ moeten zijn voor elke string in de verzameling.


Een belangrijk aspect van de willekeurigheid van een binaire string is dat deze gedefinieerd wordt aan de hand van het proces waarmee de string geselecteerd werd. De vorm van een bepaalde binaire string op zichzelf zegt daarom niets over de willekeurigheid bij selectie.


Veel mensen hebben bijvoorbeeld intuïtief het idee dat een tekenreeks als $1111$ niet willekeurig gekozen kan zijn. Maar dit is duidelijk onjuist.


Als je een uniforme variabele $S$ definieert over alle binaire strings met lengte 8, is de waarschijnlijkheid dat je $1111$ 1111$ selecteert uit de verzameling **$S_8$** hetzelfde als die van een string als $0111$ 0100$. Je kunt dus niets zeggen over de willekeurigheid van een tekenreeks door alleen de tekenreeks zelf te analyseren.


We kunnen ook spreken van willekeurige tekenreeksen zonder specifiek binaire tekenreeksen te bedoelen. We kunnen bijvoorbeeld spreken van een willekeurige hex-string $AF 02 82$. In dit geval zou de tekenreeks willekeurig gekozen zijn uit de verzameling van alle hex-tekenreeksen met lengte 6. Dit komt overeen met het willekeurig kiezen van een binaire tekenreeks met lengte 24, aangezien elk hex-cijfer 4 bits vertegenwoordigt.


Gewoonlijk verwijst de uitdrukking "een willekeurige tekenreeks", zonder kwalificatie, naar een tekenreeks die willekeurig gekozen is uit de verzameling van alle tekenreeksen met dezelfde lengte. Zo heb ik het hierboven beschreven. Een string met lengte $n$ kan natuurlijk ook willekeurig gekozen worden uit een andere verzameling. Bijvoorbeeld een set die slechts een deelverzameling is van alle strings met lengte $n$, of misschien een set die strings van verschillende lengte bevat. In die gevallen zouden we echter niet spreken van een "willekeurige tekenreeks", maar eerder van "een tekenreeks die willekeurig gekozen is uit een verzameling **S**".


Een sleutelbegrip in cryptografie is pseudorandomheid. Een **pseudo-willekeurige string** van lengte $n$ lijkt *alsof* het resultaat is van het bemonsteren van een uniforme variabele $S$ die elke string in **$S_n$** een gelijke selectiekans geeft. In feite is de string echter het resultaat van het bemonsteren van een uniforme variabele $S'$ die alleen een kansverdeling definieert - niet noodzakelijk een met gelijke kansen voor alle mogelijke uitkomsten op een deelverzameling van **$S_n$**. Het cruciale punt hier is dat niemand echt onderscheid kan maken tussen steekproeven uit $S$ en $S'$, zelfs als je er veel van neemt.


Veronderstel bijvoorbeeld een willekeurige variabele $S$. Zijn uitkomstverzameling is **$S_{256}$**, dit is de verzameling van alle binaire strings met lengte 256. Deze verzameling heeft $2^{256}$ Elements. Deze verzameling heeft $2^{256}$ Elements. Elk element heeft een gelijke selectiekans, $1/2^{256}$, bij bemonstering.


Stel bovendien dat er een willekeurige variabele $S'$ is. De verzameling uitkomsten bevat alleen binaire strings van lengte 256 $2^{128}$. Ze heeft een bepaalde kansverdeling over die strings, maar deze verdeling is niet noodzakelijk uniform.


Stel dat ik nu 1000 steekproeven uit $S$ en 1000 steekproeven uit $S'$ neem en de twee sets uitkomsten aan jou geef. Ik vertel je welke set uitkomsten bij welke willekeurige variabele hoort. Vervolgens neem ik een steekproef uit één van de twee willekeurige variabelen. Maar deze keer vertel ik je niet welke willekeurige variabele ik steek. Als $S'$ pseudo-willekeurig zou zijn, dan is het idee dat de kans dat jij juist raadt welke willekeurige variabele ik heb genomen praktisch niet groter is dan $1/2$.


Gewoonlijk wordt een pseudo-willekeurige tekenreeks met een lengte van $n$ geproduceerd door willekeurig een tekenreeks met een grootte van $n - x$ te selecteren, waarbij $x$ een positief geheel getal is, en deze te gebruiken als invoer voor een expansiealgoritme. Deze willekeurige string van grootte $n - x$ staat bekend als de **seed**.


Pseudorandom strings zijn een sleutelbegrip om cryptografie praktisch te maken. Neem bijvoorbeeld stream ciphers. Bij een streamcijfer wordt een willekeurig gekozen sleutel in een expansiealgoritme gestopt om een veel grotere pseudorandomreeks te produceren. Deze pseudorandomreeks wordt vervolgens gecombineerd met de klaartekst via een XOR-bewerking om een cijfertekst te produceren.


Als we niet in staat zouden zijn om dit soort pseudorandom strings te produceren voor een streamcipher, dan zouden we een sleutel nodig hebben die net zo lang is als het bericht om het te beveiligen. Dit is in de meeste gevallen geen praktische optie.


Het begrip pseudo-willekeurigheid dat in deze paragraaf wordt besproken kan formeler gedefinieerd worden. Het geldt ook voor andere contexten. Maar daar hoeven we hier niet op in te gaan. Het enige wat je intuïtief moet begrijpen voor een groot deel van cryptografie is het verschil tussen een willekeurige en een pseudo-willekeurige string. [2]


De reden voor het weglaten van het onderscheid tussen "random" en "uniform" in onze discussie zou nu ook duidelijk moeten zijn. In de praktijk gebruikt iedereen de term pseudo-willekeurig om een string aan te duiden die eruit ziet alsof hij het resultaat is van een steekproef van een uniforme variabele $S$. Strikt genomen zouden we zo'n string "pseudo-uniform" moeten noemen, onze taal van eerder overnemend. Omdat de term "pseudo-uniform" zowel onhandig is als door niemand gebruikt wordt, zullen we hem hier voor de duidelijkheid niet introduceren. In plaats daarvan laten we het onderscheid tussen "willekeurig" en "uniform" in de huidige context gewoon vallen.



**Noten**


[2] Als je geïnteresseerd bent in een meer formele uiteenzetting over deze zaken, kun je Katz en Lindell's *Introduction to Modern Cryptography* raadplegen, met name hoofdstuk 3.



# Wiskundige grondslagen van cryptografie 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>



## Wat is getaltheorie?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>


Dit hoofdstuk behandelt een meer geavanceerd onderwerp over de wiskundige grondslagen van cryptografie: getaltheorie. Hoewel getaltheorie belangrijk is voor symmetrische cryptografie (zoals in het Rijndael Cijfer), is het vooral belangrijk in de publieke sleutel cryptografische omgeving.


Als je de details van getaltheorie omslachtig vindt, zou ik aanraden om de eerste keer op hoog niveau te lezen. Je kunt er later altijd op terugkomen.


___


Je zou **getaltheorie** kunnen karakteriseren als de studie van de eigenschappen van gehele getallen en wiskundige functies die werken met gehele getallen.


Bedenk bijvoorbeeld dat twee getallen $a$ en $N$ **coprimes** (of **relatieve primes**) zijn als hun grootste gemene deler gelijk is aan 1. Stel nu een bepaald geheel getal $N$. Hoeveel gehele getallen kleiner dan $N$ zijn coprimes met $N$? Kunnen we algemene uitspraken doen over de antwoorden op deze vraag? Dit zijn de typische vragen die de getaltheorie probeert te beantwoorden.


De moderne getaltheorie maakt gebruik van de gereedschappen van de abstracte algebra. Het gebied van de **abstracte algebra** is een subdiscipline van de wiskunde waar de belangrijkste objecten van analyse abstracte objecten zijn, gekend als algebraïsche structuren. Een **algebraïsche structuur** is een verzameling Elements verbonden met één of meer bewerkingen, die voldoet aan bepaalde axioma's. Met algebraïsche structuren kunnen wiskundigen inzicht krijgen in specifieke wiskundige problemen door te abstraheren van de details.


Het gebied van de abstracte algebra wordt soms ook moderne algebra genoemd. Je kunt ook het begrip **abstracte wiskunde** (of **zuivere wiskunde**) tegenkomen. Deze laatste term is geen verwijzing naar abstracte algebra, maar betekent eerder de studie van wiskunde omwille van zichzelf, en niet alleen met het oog op mogelijke toepassingen.


De verzamelingen uit de abstracte algebra kunnen vele soorten objecten behandelen, van vormbehoudende transformaties op een gelijkzijdige driehoek tot behangpatronen. Voor getaltheorie beschouwen we alleen verzamelingen van Elements die gehele getallen bevatten of functies die met gehele getallen werken.



## Groepen

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>


Een basisconcept in de wiskunde is dat van een verzameling Elements. Een verzameling wordt meestal aangeduid met accoladetekens met de Elements gescheiden door komma's.


Bijvoorbeeld, de verzameling van alle gehele getallen is ${..., -2, -1, 0, 1, 2, ...}$. De ellipsen betekenen hier dat een bepaald patroon zich in een bepaalde richting voortzet. De verzameling van alle gehele getallen bevat dus ook $3, 4, 5, 6$ enzovoort, evenals $-3, -4, -5, -6$ enzovoort. Deze verzameling van alle gehele getallen wordt meestal aangeduid met $mathbb{Z}$.


Een ander voorbeeld van een verzameling is $mathbb{Z} \Mod 11$, ofwel de verzameling van alle gehele getallen modulo 11. In tegenstelling tot de gehele verzameling $\mathbb{Z}$ bevat deze verzameling slechts een eindig aantal Elements, namelijk $\{0, 1, \ldots, 9, 10}$.


Een veelgemaakte fout is te denken dat de verzameling $\mathbb{Z} \mod 11$ eigenlijk ${10, -9, \punten, 0, \punten, 9, 10}$ is. Maar dit is niet het geval, gezien de manier waarop we de modulo-operatie eerder hebben gedefinieerd. Alle negatieve gehele getallen gereduceerd door modulo 11 gaan naar $ 0, 1, \dots, 9, 10}$. Bijvoorbeeld, de uitdrukking $-2 \mod 11$ slaat op $9$, terwijl de uitdrukking $-27 \mod 11$ slaat op $5$.


Een ander basisbegrip in de wiskunde is dat van een binaire bewerking. Dit is elke bewerking die twee Elements gebruikt om een derde te produceren. Van basisrekenen en algebra ben je bijvoorbeeld bekend met vier fundamentele binaire bewerkingen: optellen, aftrekken, vermenigvuldigen en delen.


Deze twee wiskundige basisbegrippen, verzamelingen en binaire operaties, worden gebruikt om het begrip groep te definiëren, de meest essentiële structuur in abstracte algebra.


Stel dat er een binaire operatie $circ$ is. Stel bovendien dat een verzameling Elements **S** uitgerust is met die bewerking. Alles wat "uitgerust" hier betekent is dat de bewerking $circ$ kan worden uitgevoerd tussen twee Elements in de verzameling **S**.


De combinatie \langle \mathbf{S}, \circ \rangle$ is dan een **groep** als het voldoet aan vier specifieke voorwaarden, de zogenaamde groepsaxioma's.


1. Voor elke $a$ en $b$ die Elements zijn van $\mathbf{S}$ is $a \circ b$ ook een element van $\mathbf{S}$. Dit staat bekend als de **sluitingsvoorwaarde**.

2. Voor elke $a$, $b$ en $c$ die Elements zijn van $\mathbf{S}$ geldt dat $(a \circ b) \circ c = a \circ (b \circ c)$. Dit staat bekend als de **associativiteitsvoorwaarde**.

3. Er is een uniek element $e$ in $\mathbf{S}$, zodanig dat voor elk element $a$ in $\mathbf{S}$ de volgende vergelijking geldt: $e \circ a = a \circ e = a$. Omdat er maar één zo'n element $e$ is, wordt het het **identiteitselement** genoemd. Deze voorwaarde staat bekend als de **identiteitsvoorwaarde**.

4. Voor elk element $a$ in $\mathbf{S}$ bestaat er een element $b$ in $\mathbf{S}$, zodat de volgende vergelijking geldt: $a \circ b = b \circ a = e$, waarbij $e$ het identiteitselement is. Element $b$ staat hier bekend als het **inverse element**, en wordt gewoonlijk aangeduid als $a^{-1}$. Deze voorwaarde staat bekend als de **inverse voorwaarde** of de **inverteerbaarheidsvoorwaarde**.


Laten we groepen wat verder verkennen. Noem de verzameling van alle gehele getallen $mathbb{Z}$. Deze verzameling gecombineerd met standaardoptelling, oftewel $ \mathbb{Z}, + \rangle$, voldoet duidelijk aan de definitie van een groep, omdat het voldoet aan de vier axioma's hierboven.


1. Voor elke $x$ en $y$ die Elements zijn van $\mathbb{Z}$ is $x + y$ ook een element van $\mathbb{Z}$. Dus voldoet $\langle \mathbb{Z}, + \rangle$ aan de sluitingsvoorwaarde.

2. Voor elke $x$, $y$ en $z$ die Elements zijn van $\mathbb{Z}$ geldt dat $(x + y) + z = x + (y + z)$. Dus voldoet $\langle \mathbb{Z}, + \rangle$ aan de associativiteitsvoorwaarde.

3. Er is een identiteitselement in $\mathbb{Z}, + \rangle$, namelijk 0. Voor elke $x$ in $\mathbb{Z}$ geldt namelijk dat: $0 + x = x + 0 = x$. Dus voldoet $\langle \mathbb{Z}, + \rangle$ aan de identiteitsvoorwaarde.

4. Ten slotte is er voor elk element $x$ in $\mathbb{Z}$ een $y$ zodat $x + y = y + x = 0$. Als $x$ bijvoorbeeld 10 zou zijn, zou $y$ $-10$ zijn (in het geval dat $x$ 0 is, is $y$ ook 0). Dus $ \mathbb{Z}, + \rangle$ voldoet aan de inverse voorwaarde.


Belangrijk is dat het feit dat de verzameling gehele getallen met optelling een groep is niet betekent dat het een groep is met vermenigvuldiging. Je kunt dit controleren door $\langle \mathbb{Z}, \cdot \rangle$ te toetsen aan de vier groepsaxioma's (waarbij $\cdot$ standaard vermenigvuldiging betekent).


De eerste twee axioma's gelden uiteraard. Bovendien kan het element 1 bij vermenigvuldiging dienen als identiteitselement. Elk geheel getal $x$ vermenigvuldigd met 1 levert namelijk $x$ op. Echter, bij $ \mathbb{Z}, \cdot \rangle$ geldt de inverse voorwaarde niet. Dat wil zeggen, er is geen uniek element $y$ in $\mathbb{Z}$ voor elke $x$ in $\mathbb{Z}$, zodat $x cdot y = 1$.


Stel bijvoorbeeld dat $x = 22$. Welke waarde $y$ uit de verzameling $\mathbb{Z}$ vermenigvuldigd met $x$ zou het identiteitselement 1 opleveren? De waarde $1/22$ zou werken, maar die zit niet in de verzameling $\mathbb{Z}$. In feite loop je tegen dit probleem aan voor elk geheel getal $x$, behalve de waarden 1 en -1 (waarbij $y$ respectievelijk 1 en -1 zou moeten zijn).


Als we reële getallen toestaan voor onze verzameling, dan verdwijnen onze problemen grotendeels. Voor elk element $x$ in de verzameling levert vermenigvuldiging met $1/x$ 1 op. Omdat breuken deel uitmaken van de verzameling reële getallen, kan voor elk reëel getal een inverse worden gevonden. De uitzondering is nul, want een vermenigvuldiging met nul zal nooit het identiteitselement 1 opleveren. Daarom is de verzameling van reële getallen zonder nul, voorzien van vermenigvuldiging, inderdaad een groep.


Sommige groepen voldoen aan een vijfde algemene voorwaarde, bekend als de **commutativiteitsvoorwaarde**. Deze voorwaarde is als volgt:



- Veronderstel een groep $G$ met een verzameling **S** en een binaire operator $circ$. Stel dat $a$ en $b$ Elements van **S** zijn. Als het zo is dat $a \circ b = b \circ a$ voor elke twee Elements $a$ en $b$ in **S**, dan voldoet $G$ aan de commutativiteitsvoorwaarde.


Elke groep die voldoet aan de commutativiteitsvoorwaarde staat bekend als een **commutatieve groep**, of een **Abeliaanse groep** (naar Niels Henrik Abel). Het is eenvoudig na te gaan dat zowel de verzameling reële getallen over optelling als de verzameling gehele getallen over optelling Abeliaanse groepen zijn. De verzameling gehele getallen over vermenigvuldiging is helemaal geen groep, dus kan ipso facto geen Abeliaanse groep zijn. De verzameling van reële getallen zonder nul over vermenigvuldiging is daarentegen ook een Abeliaanse groep.


Je moet twee belangrijke notatieconventies in acht nemen. Ten eerste worden de tekens "+" of "×" vaak gebruikt om groepsbewerkingen te symboliseren, zelfs als de Elements in feite geen getallen zijn. In deze gevallen moet je deze tekens niet interpreteren als een standaard rekenkundige optelling of vermenigvuldiging. In plaats daarvan zijn het bewerkingen met slechts een abstracte gelijkenis met deze rekenkundige bewerkingen.


Tenzij je specifiek verwijst naar rekenkundige optellingen of vermenigvuldigingen, is het eenvoudiger om symbolen als $circ$ en $diamond$ te gebruiken voor groepsbewerkingen, omdat deze geen cultureel ingebakken connotaties hebben.


Ten tweede, om dezelfde reden dat "+" en "×" vaak gebruikt worden om niet-aritmetische operaties aan te duiden, worden de identiteit Elements van groepen vaak gesymboliseerd door "0" en "1", zelfs als de Elements in deze groepen geen getallen zijn. Tenzij je verwijst naar het identiteitselement van een groep met getallen, is het gemakkelijker om een neutraler symbool zoals "$e$" te gebruiken om het identiteitselement aan te duiden.


Veel verschillende en zeer belangrijke verzamelingen van waarden in de wiskunde die uitgerust zijn met bepaalde binaire operaties zijn groepen. Cryptografische toepassingen werken echter alleen met verzamelingen van gehele getallen of op zijn minst Elements die beschreven worden door gehele getallen, dus binnen het domein van de getaltheorie. Daarom worden verzamelingen met andere reële getallen dan gehele getallen niet gebruikt in cryptografische toepassingen.


Laten we afsluiten met een voorbeeld van Elements die "beschreven kunnen worden door gehele getallen", ook al zijn het geen gehele getallen. Een goed voorbeeld zijn de punten van elliptische krommen. Hoewel elk punt op een elliptische kromme duidelijk geen geheel getal is, wordt zo'n punt wel beschreven door twee gehele getallen.


Elliptische krommen zijn bijvoorbeeld cruciaal voor Bitcoin. Elk standaard Bitcoin private en publieke sleutelpaar wordt geselecteerd uit de verzameling punten die gedefinieerd wordt door de volgende elliptische kromme:


$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$


(dat het grootste priemgetal is dat kleiner is dan $2^{256}$).


Transacties in Bitcoin houden meestal in dat uitgangen op een of andere manier worden vergrendeld aan een of meer publieke sleutels. De waarde van deze transacties kan dan ontgrendeld worden door middel van digitale handtekeningen met de corresponderende private sleutels.




## Cyclische groepen

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>


Een belangrijk onderscheid dat we kunnen maken is tussen een **oneindige** en een **oneindige groep**. De eerste groep heeft een eindig aantal Elements, terwijl de laatste groep een oneindig aantal Elements heeft. Het aantal Elements in een eindige groep staat bekend als de **orde van de groep**. Alle praktische cryptografie waarbij groepen gebruikt worden, is gebaseerd op eindige (getaltheoretische) groepen.


Binnen de publieke cryptografie is een bepaalde klasse van eindige Abeliaanse groepen, bekend als cyclische groepen, bijzonder belangrijk. Om cyclische groepen te begrijpen, moeten we eerst het concept van groepselement exponentiëren begrijpen.


Stel dat er een groep $G$ is met een groepsoperatie $\circ$, en dat $a$ een element is van $G$. De uitdrukking $a^n$ moet dan geïnterpreteerd worden als het element $a$ dat in totaal $n - 1$ keer met zichzelf gecombineerd is. Bijvoorbeeld, $a^2$ betekent $a \circ a$, $a^3$ betekent $a \circ a$, enzovoort. (Merk op dat exponentiëren hier niet noodzakelijk exponentiëren is in de standaard rekenkundige zin)


Laten we een voorbeeld nemen. Stel dat $G = \mathbb{Z} \mod 7, + \rangle$, en dat onze waarde voor $a$ 4 is. In dat geval is $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Als alternatief zou $a^4$ staan voor $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.


Sommige Abeliaanse groepen hebben één of meer Elements, die alle andere groep Elements kunnen opleveren door voortdurende exponentiatie. Deze Elements worden **generatoren** of **primitieve Elements** genoemd.


Een belangrijke klasse van zulke groepen is $ \mathbb{Z}^* \mod N, \cdot \rangle$, waarbij $N$ een priemgetal is. De notatie $mathbb{Z}^*$ betekent dat de groep alle positieve gehele getallen kleiner dan $N$ bevat. Zo'n groep heeft dus altijd $N - 1$ Elements.


Neem bijvoorbeeld $G = \mathbb{Z}^* \mod 11, \cdot \rangle$. Deze groep heeft de volgende Elements: $1, 2, 3, 4, 5, 6, 7, 8, 9, 10}$. De orde van deze groep is 10 (wat inderdaad gelijk is aan $11 - 1$).


Laten we eens kijken hoe we het element 2 uit deze groep kunnen exponentiëren. De berekeningen tot $2^{12}$ worden hieronder getoond. Merk op dat aan de linkerkant van de vergelijking de exponent verwijst naar exponentiëren van groepselementen. In ons specifieke voorbeeld gaat het inderdaad om rekenkundige exponentiëring aan de rechterkant van de vergelijking (maar het had bijvoorbeeld ook om optellen kunnen gaan). Ter verduidelijking heb ik de herhaalde bewerking uitgeschreven, in plaats van de exponentvorm aan de rechterkant.



- $2^1 = 2 ^mod 11$
- $2^2 = 2 \dot 2 \mod 11 = 4 \mod 11$
- $2^3 = 2 \dot 2 \dot 2 \mod 11 = 8 \mod 11$
- $2^4 = 2 \dot 2 \dot 2 \dot 2 \dot 11 = 16 \dot 11 = 5 \dot 11$
- $2^5 = 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 11 = 32 \dot 11 = 10 \dot 11$
- $2^6 = 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 11 = 64 \dot 11 = 9 \dot 11$
- $2^7 = 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 11 = 128 \dot 11 = 7 \dot 11$
- $2^8 = 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 11 = 256 \dot 11 = 3 \dot 11$
- $2^9 = 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 11 = 512 \dot 11 = 6 \dot 11$
- $2^{10} = 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 11 = 1024 \dot 11 = 1 \dot 11$
- $2^{11} = 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 11 = 2048 \dot 11 = 2 \dot 11$
- $2^{12} = 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 2 \dot 11 = 4096 \dot 11 = 4 \dot 11$


Als je goed kijkt, zie je dat het uitvoeren van exponentiatie op het element 2 door alle Elements van $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ fietst in de volgende volgorde: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Na $2^{10}$ gaat de voortdurende exponentiatie van het element 2 weer door alle Elements en in dezelfde volgorde. Het element 2 is dus een generator in $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.


Hoewel $\mathbb{Z}^* \mod 11, \cdot \rangle$ meerdere generatoren heeft, zijn niet alle Elements van deze groep generatoren. Neem bijvoorbeeld het element 3. Het doorlopen van de eerste 10 exponentiaties, zonder de omslachtige berekeningen te tonen, geeft de volgende resultaten:



- $3^1 = 3 ^mod 11$
- $3^2 = 9 mod 11$
- $3^3 = 5 ^mod 11$
- $3^4 = 4 ^mod 11$
- $3^5 = 1 mod 11$
- $3^6 = 3 ^mod 11$
- $3^7 = 9 mod 11$
- $3^8 = 5 \mod 11$
- $3^9 = 4 ^mod 11$
- $3^{10} = 1 mud 11$


In plaats van alle waarden te doorlopen die in $\mathbb{Z}^* \mod 11, \cdot \rangle$ voorkomen, leidt exponentiëring van het element 3 slechts tot een deelverzameling van die waarden: 3, 9, 5, 4 en 1. Na de vijfde exponentiatie beginnen deze waarden zich te herhalen.


We kunnen nu een **cyclische groep** definiëren als elke groep met minstens één generator. Dat wil zeggen dat er minstens één groepselement is waaruit je alle andere groepen Elements kunt maken door exponentiëren.


Het is je misschien opgevallen dat in ons voorbeeld hierboven zowel $2^{10}$ als $3^{10}$ gelijk zijn aan $1 \mod 11$. Hoewel we de berekening niet uitvoeren, zal de exponentiatie met 10 van elk element in de groep $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ in feite $1 \mod 11$ opleveren. Waarom is dit het geval?


Dit is een belangrijke vraag, maar het kost wat werk om die te beantwoorden.


Stel om te beginnen twee positieve gehele getallen $a$ en $N$. Een belangrijke stelling in de getaltheorie stelt dat $a$ een multiplicatieve inverse modulo $N$ heeft (dat wil zeggen, een geheel getal $b$ zodat $a \cdot b = 1 \mod N$) als en slechts als de grootste gemene deler tussen $a$ en $N$ gelijk is aan 1. Dat wil zeggen als $a$ en $N$ coprimes zijn. Dat wil zeggen, als $a$ en $N$ coprimes zijn.


Dus, voor elke groep van gehele getallen uitgerust met vermenigvuldiging modulo $N$, zijn alleen de kleinere coprimes met $N$ inbegrepen in de verzameling. We kunnen deze verzameling aanduiden met $\mathbb{Z}^c \mod N$.


Stel bijvoorbeeld dat $N$ 10 is. Alleen de gehele getallen 1, 3, 7 en 9 zijn coprimes met 10. Dus de verzameling $\mathbb{Z}^c \mod 10$ bevat alleen ${1, 3, 7, 9}$. Je kunt geen groep met gehele vermenigvuldiging modulo 10 maken door andere gehele getallen tussen 1 en 10 te gebruiken. Voor deze specifieke groep zijn de inverses de paren 1 en 9 en 3 en 7.


In het geval dat $N$ zelf priem is, zijn alle gehele getallen van 1 tot en met $N - 1$ copriem met $N$. Zo'n groep heeft dus een orde van $N - 1$. Met onze eerdere notatie is $\mathbb{Z}^c \mod N$ gelijk aan $\mathbb{Z}^* \mod N$ als $N$ priem is. De groep die we gekozen hebben voor ons eerdere voorbeeld, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, is een bijzonder voorbeeld van deze klasse van groepen.


Vervolgens berekent de functie $\phi(N)$ het aantal coprimes tot een getal $N$, en staat bekend als **Euler's Phi functie**. [1] Volgens de stelling van **Euler** geldt dat wanneer twee gehele getallen $a$ en $N$ coprimes zijn:



- $a^{{\phi(N)} \mod N = 1 \mod N$


Dit heeft een belangrijke implicatie voor de klasse van groepen $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ waar $N$ priem is. Voor deze groepen staat groepselementexponentiatie voor rekenkundige exponentiatie. Dat wil zeggen, $a^{\phi(N)} \mod N$ vertegenwoordigt de rekenkundige bewerking $a^{\phi(N)} \mod N$. Omdat elk element $a$ in deze multiplicatieve groepen copriem is met $N$, betekent dit dat $a^{{\phi(N)} \mod N = a^{N - 1} \mod N = 1 \mod N$.


De stelling van Euler is een heel belangrijk resultaat. Om te beginnen impliceert het dat alle Elements in $\mathbb{Z}^* \mod N, \cdot \rangle$ alleen door een aantal waarden kunnen lopen door exponentiatie dat deelt in $N - 1$. In het geval van \mathbb{Z}^* \mod 11, \cdot \rangle$ betekent dit dat elk element alleen door 2, 5 of 10 Elements kan fietsen. De groepswaarden waar een element doorheen fietst bij exponentiëring staat bekend als de **volgorde van het element**. Een element met een orde gelijk aan de orde van een groep is een generator.


Verder impliceert de stelling van Euler dat we altijd het resultaat van $a^{N - 1} \mod N$ kunnen weten voor elke groep \mathbb{Z}^* \mod N, \cdot \rangle$ waar $N$ priem is. Dit is zo ongeacht hoe ingewikkeld de berekeningen zijn.


Bijvoorbeeld, stel onze groep is $\mathbb{Z}^* \mod 160,481,182$ (waar 160,481,182 inderdaad een priemgetal is). We weten dat alle gehele getallen 1 tot en met 160.481.181 Elements van deze groep moeten zijn, en dat dus $\phi(n) = 160.481.181$. Hoewel we niet alle rekenstappen kunnen uitvoeren, weten we dat uitdrukkingen als $514^{160,481,181}$, $2.005^{160,481,181}$, en $256.212^{160,481,181}$ allemaal moeten uitkomen op $1 \mod 160,481,182$.


**Noten:**


[1] De functie werkt als volgt. Elk geheel getal $N$ kan worden ontbonden in een product van priemgetallen. Stel dat een bepaalde $N$ als volgt is ontbonden in factoren: $p_1^{e1} \p_2^{e2} \waarbij alle $p$'s priemgetallen zijn en alle $e$'s gehele getallen groter dan of gelijk aan 1. Dan is:


$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$


De Phi-functieformule van Euler voor de priemfactorisatie van $N$.



## Velden

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>


Een groep is de basis algebraïsche structuur in abstracte algebra, maar er zijn er veel meer. De enige andere algebraïsche structuur die je moet kennen is die van een **veld**, meer bepaald die van een **eindig veld**. Dit type algebraïsche structuur wordt vaak gebruikt in cryptografie, zoals in de Advanced Encryption Standard. Dit laatste is het belangrijkste symmetrische encryptieschema dat je in de praktijk zult tegenkomen.


Een veld is afgeleid van het begrip groep. Een **veld** is een verzameling Elements **S** uitgerust met twee binaire operatoren $\circ$ en $\diamond$, die aan de volgende voorwaarden voldoet:


1. De verzameling **S** voorzien van $\circ$ is een Abeliaanse groep.

2. De verzameling **S** uitgerust met $\diamond$ is een Abeliaanse groep voor de "niet-nul" Elements.

3. De verzameling **S** uitgerust met de twee operatoren voldoet aan de zogenaamde distributieve voorwaarde: Stel dat $a$, $b$ en $c$ Elements van **S** zijn. Dan voldoet **S** voorzien van de twee operatoren aan de distributieve eigenschap als $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.


Merk op dat, net als bij groepen, de definitie van een veld erg abstract is. Er worden geen uitspraken gedaan over de typen Elements in **S**, of over de operaties $\circ$ en $\diamond$. Er staat alleen dat een veld elke verzameling van Elements is met twee operaties waarvoor de drie bovenstaande voorwaarden gelden. (Het "nul"-element in de tweede Abeliaanse groep kan abstract geïnterpreteerd worden)


Wat is dan een voorbeeld van een veld? Een goed voorbeeld is de verzameling $mathbb{Z} \mod 7$, of $0, 1, \ldots, 7}$ gedefinieerd over standaard optellen (in plaats van $circ$ hierboven) en standaard vermenigvuldigen (in plaats van $diamond$ hierboven).


Ten eerste voldoet $\mathbb{Z} \7$ aan de voorwaarde om een Abeliaanse groep over optelling te zijn, en het voldoet aan de voorwaarde om een Abeliaanse groep over vermenigvuldiging te zijn als je alleen de niet-nul Elements beschouwt. Ten tweede voldoet de combinatie van de verzameling met de twee operatoren aan de distributieve voorwaarde.


Het is didactisch de moeite waard om deze beweringen te onderzoeken aan de hand van enkele bijzondere waarden. Laten we de experimentele waarden 5, 2 en 3 nemen, willekeurig gekozen Elements uit de verzameling $mathbb{Z} \7$, om het veld $\langle \mathbb{Z} \7, +, \cdot \rangle$. We zullen deze drie waarden in volgorde gebruiken, al naar gelang de omstandigheden.


Laten we eerst onderzoeken of $\mathbb{Z} \7$ met optelling een Abeliaanse groep is.


1. **Sluitingsvoorwaarde**: Laten we 5 en 2 als waarden nemen. In dat geval is $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Dit is inderdaad een element van $\mathbb{Z} \mod 7$, dus het resultaat is in overeenstemming met de sluitingsvoorwaarde.

2. **Associatieve voorwaarde**: Laten we 5, 2 en 3 als waarden nemen. In dat geval is $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Dit komt overeen met de associativiteitsvoorwaarde.

3. **Identiteitsvoorwaarde**: Laten we 5 als waarde nemen. In dat geval is $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Dus 0 lijkt het identiteitselement voor optellen te zijn.

4. **Inverse voorwaarde**: Beschouw de inverse van 5. Het moet zo zijn dat $[5 + d] \mod 7 = 0$, voor een bepaalde waarde van $d$. In dit geval is de unieke waarde van $mathbb{Z} \7$ die aan deze voorwaarde voldoet 2.

5. **Commutativiteitsvoorwaarde**: Laten we 5 en 3 als waarden nemen. In dat geval is $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Dit komt overeen met de commutativiteitsvoorwaarde.


De verzameling $\mathbb{Z} \7$ met optelling blijkt duidelijk een Abeliaanse groep te zijn. Laten we nu onderzoeken of $\mathbb{Z} \7$ met vermenigvuldiging een Abeliaanse groep is voor alle Elements die niet nul zijn.


1. **Sluitingsvoorwaarde**: Laten we 5 en 2 als waarden nemen. In dat geval is $[5 \dot 2] \mod 7 = 10 \mod 7 = 3$. Dit is ook een element van $mathbb{Z} \mod 7$, dus het resultaat is in overeenstemming met de sluitingsvoorwaarde.

2. **Associatieve voorwaarde**: Laten we 5, 2 en 3 als waarden nemen. In dat geval is $[(5 \dot 2) \dot 3] \mod 7 = [5 \dot (2 \dot 3)] \mod 7 = 30 \mod 7 = 2$. Dit komt overeen met de associativiteitsvoorwaarde.

3. **Identiteitsvoorwaarde**: Laten we 5 als waarde nemen. In dat geval is $[5 \dot 1] \mod 7 = [1 \dot 5] \mod 7 = 5$. Dus 1 lijkt het identiteitselement voor vermenigvuldiging te zijn.

4. **Inverse voorwaarde**: Beschouw de inverse van 5. Het moet zo zijn dat $[5 \dot d] \mod 7 = 1$, voor een bepaalde waarde van $d$. De unieke waarde uit $mathbb{Z} \7$ die aan deze voorwaarde voldoet is 3. Dit komt overeen met de inverse voorwaarde.

5. **Commutativiteitsvoorwaarde**: Laten we 5 en 3 als waarden nemen. In dat geval is $[5 \dot 3] \mod 7 = [3 \dot 5] \mod 7 = 15 \mod 7 = 1$. Dit komt overeen met de commutativiteitsvoorwaarde.


De verzameling $\mathbb{Z} \module 7$ lijkt duidelijk te voldoen aan de regels om een Abeliaanse groep te zijn in combinatie met optellen of vermenigvuldigen over de niet-nul Elements.


Uiteindelijk lijkt deze verzameling in combinatie met beide operatoren te voldoen aan de distributieve voorwaarde. Laten we 5, 2 en 3 als waarden nemen. We zien dat $[5 \dot (2 + 3)] \mod 7 = [5 \dot 2 + 5 \dot 3] \mod 7 = 25 \mod 7 = 4$.


We hebben nu gezien dat $\mathbb{Z} \module 7$ uitgerust met optelling en vermenigvuldiging voldoet aan de axioma's voor een eindig veld bij het testen met bepaalde waarden. Natuurlijk kunnen we dat ook in het algemeen aantonen, maar dat zullen we hier niet doen.


Een belangrijk onderscheid is tussen twee soorten velden: eindige en oneindige velden.


Een **oneindig veld** is een veld waarvan de verzameling **S** oneindig groot is. De verzameling reële getallen $mathbb{R}$ uitgerust met optellen en vermenigvuldigen is een voorbeeld van een oneindig veld. Een **eindig veld**, ook wel een **Galoïsveld** genoemd, is een veld waarbij de verzameling **S** eindig is. Ons voorbeeld van $mathbb{Z} \is een eindig veld.


In cryptografie zijn we voornamelijk geïnteresseerd in eindige velden. In het algemeen kan worden aangetoond dat een eindig veld bestaat voor een verzameling Elements **S** als en slechts als het $p^m$ Elements heeft, waarbij $p$ een priemgetal is en $m$ een positief geheel getal groter dan of gelijk aan één. Met andere woorden, als de orde van een verzameling **S** een priemgetal is ($p^m$ waarbij $m = 1$) of een priemmacht ($p^m$ waarbij $m > 1$), dan kun je twee operatoren $\circ$ en $\diamond$ vinden zodat aan de voorwaarden voor een veld wordt voldaan.


Als een eindig veld een priemgetal Elements heeft, dan heet het een **priemgetalveld**. Als het aantal Elements in het eindige veld een priemmacht is, dan heet het veld een **extensieveld**. In cryptografie zijn we geïnteresseerd in zowel priem- als extensievelden. [2]


De belangrijkste priemvelden die van belang zijn voor cryptografie zijn die waar de verzameling van alle gehele getallen gemoduleerd is door een priemgetal en de operatoren standaard optellen en vermenigvuldigen zijn. Deze klasse van eindige velden omvat onder andere $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \module 5$, $mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \enzovoort. Voor elk priemveld $\mathbb{Z} \mod p$ is de verzameling gehele getallen van het veld als volgt: $0, 1, ijkpunten, p - 2, p - 1}$.


In cryptografie zijn we ook geïnteresseerd in uitbreidingsvelden, met name velden met $2^m$ Elements waarbij $m > 1$. Zulke eindige velden worden bijvoorbeeld gebruikt in het Rijndael-cijfer, dat de basis vormt van de Advanced Encryption Standard. Hoewel priemvelden relatief intuïtief zijn, zijn deze basis 2-uitbreidingsvelden waarschijnlijk niet geschikt voor iemand die niet bekend is met abstracte algebra.


Om te beginnen is het inderdaad zo dat aan elke verzameling gehele getallen met $2^m$ Elements twee operatoren kunnen worden toegekend die van hun combinatie een veld maken (zolang $m$ een positief geheel getal is). Maar het feit dat een veld bestaat, betekent niet noodzakelijk dat het gemakkelijk te ontdekken is of bijzonder praktisch voor bepaalde toepassingen.


Het blijkt dat de uitbreidingsvelden van $2^m$ die het meest van toepassing zijn in cryptografie, gedefinieerd zijn over bepaalde verzamelingen polynomiale uitdrukkingen, in plaats van over een verzameling gehele getallen.


Stel bijvoorbeeld dat we een uitbreidingsveld wilden met $2^3$ (dus 8) Elements in de verzameling. Hoewel er veel verschillende verzamelingen kunnen zijn die gebruikt kunnen worden voor velden van die grootte, bevat één zo'n verzameling alle unieke veeltermen van de vorm $a_2x^2 + a_1x + a_0$, waarbij elke coëfficiënt $a_i$ ofwel 0 of 1 is. Deze verzameling **S** bevat dus de volgende Elements:


1. $0$: Het geval waarin $a_2 = 0$, $a_1 = 0$, en $a_0 = 0$.

2. $1$: Het geval waarin $a_2 = 0$, $a_1 = 0$, en $a_0 = 1$.

3. $x$: Het geval waarin $a_2 = 0$, $a_1 = 1$, en $a_0 = 0$.

4. $x + 1$: Het geval waarin $a_2 = 0$, $a_1 = 1$, en $a_0 = 1$.

5. $x^2$: Het geval waarin $a_2 = 1$, $a_1 = 0$ en $a_0 = 0$.

6. $x^2 + 1$: Het geval waarin $a_2 = 1$, $a_1 = 0$ en $a_0 = 1$.

7. $x^2 + x$: Het geval waarin $a_2 = 1$, $a_1 = 1$, en $a_0 = 0$.

8. $x^2 + x + 1$: Het geval waarin $a_2 = 1$, $a_1 = 1$, en $a_0 = 1$.


Dus **S** is de verzameling ${0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1}$. Welke twee operaties kunnen over deze verzameling Elements gedefinieerd worden om te zorgen dat hun combinatie een veld is?


De eerste bewerking op de verzameling **S** ($\circ$) kan worden gedefinieerd als standaard polynoomoptelling modulo 2. Het enige wat je hoeft te doen is de veeltermen optellen zoals je normaal zou doen en dan de modulo 2 toepassen op elk van de coëfficiënten van de resulterende veelterm. Hier zijn enkele voorbeelden:



- $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
- $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
- $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$


De tweede bewerking op de verzameling **S** ($Diamond$) die nodig is om het veld te maken is ingewikkelder. Het is een soort vermenigvuldiging, maar geen standaard vermenigvuldiging uit de rekenkunde. In plaats daarvan moet je elk element zien als een vector en de bewerking begrijpen als de vermenigvuldiging van die twee vectoren modulo een irreducibele polynoom.


Laten we eerst eens kijken naar het idee van een irreducibele polynoom. Een **irreducibele veelterm** is een veelterm die niet ontbonden kan worden in factoren (net zoals een priemgetal niet ontbonden kan worden in andere componenten dan 1 en het priemgetal zelf). Voor ons doel zijn we geïnteresseerd in veeltermen die irreducibel zijn met betrekking tot de verzameling van alle gehele getallen. (Merk op dat je bepaalde veeltermen kunt ontbinden in factoren door bijvoorbeeld de reële of complexe getallen, zelfs als je ze niet kunt ontbinden in factoren met gehele getallen)


Neem bijvoorbeeld de veelterm $x^2 - 3x + 2$. Deze kan herschreven worden als $(x - 1)(x - 2)$. Deze is dus niet irreducibel. Beschouw nu de veelterm $x^2 + 1$. Door alleen gehele getallen te gebruiken, is er geen manier om deze uitdrukking verder te ontbinden in factoren. Dit is dus een irreducibele polynoom met betrekking tot de gehele getallen.


Laten we nu eens kijken naar het concept van vectorvermenigvuldiging. We zullen dit onderwerp niet uitdiepen, maar je moet gewoon een basisregel begrijpen: Elke vectordeling kan plaatsvinden zolang het dividend een graad heeft die hoger is dan of gelijk is aan die van de deler. Als het dividend een lagere graad heeft dan de deler, dan kan het dividend niet langer gedeeld worden door de deler.


Bekijk bijvoorbeeld de uitdrukking $x^6 + x + 1 \mod x^5 + x^2$. Dit vermindert duidelijk verder omdat de graad van het dividend, 6, hoger is dan de graad van de deler, 5. Bekijk nu de uitdrukking $x^5 + x + 1 \mod x^5 + x^2$. Dit wordt ook nog kleiner, want de graad van het dividend, 5, en de deler, 5, zijn gelijk.


Bekijk nu echter de uitdrukking $x^4 + x + 1 \mod x^5 + x^2$. Dit reduceert niet verder, omdat de graad van het dividend, 4, lager is dan de graad van de deler, 5.


Op basis van deze informatie zijn we nu klaar om onze tweede bewerking te vinden voor de verzameling ${0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1}$.


Ik heb al gezegd dat de tweede bewerking opgevat moet worden als vectorvermenigvuldiging modulo een irreducibele polynoom. Deze irreducibele polynoom moet ervoor zorgen dat de tweede operatie een Abeliaanse groep over **S** definieert en consistent is met de distributieve voorwaarde. Dus wat moet die irreducibele polynoom zijn?


Omdat alle vectoren in de verzameling graad 2 of lager zijn, moet de irreducibele veelterm graad 3 hebben. Als een vermenigvuldiging van twee vectoren in de verzameling een veelterm van graad 3 of hoger oplevert, weten we dat modulo van een veelterm van graad 3 altijd een veelterm van graad 2 of lager oplevert. Dit is het geval omdat elke veelterm van graad 3 of hoger altijd deelbaar is door een veelterm van graad 3. Bovendien moet de veelterm die als deler fungeert irreducibel zijn.


Het blijkt dat er verschillende onherleidbare veeltermen van graad 3 zijn die we kunnen gebruiken als deler. Elk van deze veeltermen definieert een ander veld in combinatie met onze verzameling **S** en optelling modulo 2. Dit betekent dat je meerdere opties hebt bij het gebruik van extensievelden $2^m$ in cryptografie.


Stel dat we voor ons voorbeeld de veelterm $x^3 + x + 1$ kiezen. Dit is inderdaad irreducibel, want je kunt het niet ontbinden in factoren met gehele getallen. Bovendien zorgt het ervoor dat elke vermenigvuldiging van twee Elements een veelterm van graad 2 of minder oplevert.


Laten we een voorbeeld van de tweede bewerking doornemen met de veelterm $x^3 + x + 1$ als deler om te illustreren hoe het werkt. Stel dat je de Elements $x^2 + 1$ vermenigvuldigt met $x^2 + x$ in onze verzameling **S**. We moeten dan de uitdrukking $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$ berekenen. Dit kan als volgt vereenvoudigd worden:



- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$


We weten dat $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ kan worden gereduceerd omdat het dividend een hogere graad (4) heeft dan de deler (3).


Om te beginnen kun je zien dat de uitdrukking $x^3 + x + 1$ in totaal $x^4 + x^3 + x^2 + x$ is. Je kunt dit controleren door $x^3 + x + 1$ te vermenigvuldigen met $x$, wat $x^4 + x^2 + x$ is. Omdat de laatste term van dezelfde graad is als het dividend, namelijk 4, weten we dat dit werkt. Je kunt de rest van deze deling door $x$ als volgt berekenen:



- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
- $[x^3] \mod x^3 + x + 1 =$
- $x^3$


Dus na het delen van $x^4 + x^3 + x^2 + x$ door $x^3 + x + 1$ hebben we een rest van $x^3$. Kan dit verder gedeeld worden door $x^3 + x + 1$?


Intuïtief zou het aantrekkelijk kunnen zijn om te zeggen dat $x^3$ niet langer gedeeld kan worden door $x^3 + x + 1$, omdat de laatste term groter lijkt. Denk echter aan onze eerdere discussie over vectordeling. Zolang het dividend een graad heeft die groter of gelijk is aan de deler, kan de uitdrukking verder worden gereduceerd. Concreet kan de uitdrukking $x^3 + x + 1$ precies 1 keer overgaan in $x^3$. De rest wordt als volgt berekend:


$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$


Je vraagt je misschien af waarom $(x^3) - (x^3 + x + 1)$ uitkomt op $x + 1$ en niet op $-x - 1$. Onthoud dat de eerste bewerking van ons veld modulo 2 gedefinieerd is. Daarom geeft het aftrekken van twee vectoren precies hetzelfde resultaat als het optellen van twee vectoren.


Om de vermenigvuldiging van $x^2 + 1$ en $x^2 + x$ samen te vatten: Als je die twee termen vermenigvuldigt, krijg je een graad 4 polynoom, $x^4 + x^3 + x^2 + x$, die moet worden gereduceerd modulo $x^3 + x + 1$. De graad 4 polynoom is deelbaar door $x^3 + x + 1$ precies $x + 1$ keer. De rest na het delen van $x^4 + x^3 + x^2 + x$ door $x^3 + x + 1$ precies $x + 1$ keer is $x + 1$. Dit is inderdaad een element in onze verzameling ${0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1}$.


Waarom zouden uitbreidingsvelden met basis 2 over verzamelingen van veeltermen, zoals in het voorbeeld hierboven, nuttig zijn voor cryptografie? De reden is dat je de coëfficiënten in de veeltermen van zulke verzamelingen, 0 of 1, kunt zien als Elements van binaire strings met een bepaalde lengte. De verzameling **S** in ons voorbeeld hierboven kan bijvoorbeeld worden gezien als een verzameling **S** die alle binaire strings met lengte 3 (000 tot en met 111) bevat. De bewerkingen op **S** kunnen dan ook gebruikt worden om bewerkingen op deze binaire tekenreeksen uit te voeren en een binaire tekenreeks van dezelfde lengte te produceren.


**Noten:**


[2] Extensievelden worden erg contra-intuïtief. In plaats van Elements van gehele getallen, hebben ze sets van veeltermen. Bovendien worden alle bewerkingen uitgevoerd modulo een irreducibele polynoom.



## Abstracte algebra in de praktijk

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>


Ondanks het formele taalgebruik en de abstractheid van de discussie, moet het concept van een groep niet al te moeilijk te begrijpen zijn. Het is gewoon een verzameling Elements samen met een binaire operatie, waarbij de uitvoering van die binaire operatie op die Elements voldoet aan vier algemene voorwaarden. Een Abeliaanse groep heeft alleen een extra voorwaarde die commutativiteit heet. Een cyclische groep is weer een speciaal soort Abeliaanse groep, namelijk een groep die een generator heeft. Een veld is slechts een complexere constructie van het basisbegrip groep.


Maar als je een praktisch ingesteld persoon bent, vraag je je nu misschien af: Wat maakt het uit? Heeft de wetenschap dat een verzameling van Elements met een operator een groep is, of zelfs een Abeliaanse of cyclische groep, enige relevantie in de echte wereld? Is weten dat iets een veld is?


Zonder al te veel in detail te treden, is het antwoord "ja". Groepen werden voor het eerst gecreëerd in de 19e eeuw door de Franse wiskundige Evariste Galois. Hij gebruikte ze om conclusies te trekken over het oplossen van veeltermvergelijkingen met een graad hoger dan vijf.


Sindsdien heeft het concept van een groep geholpen licht te werpen op een aantal problemen in de wiskunde en elders. Op basis hiervan kon de natuurkundige Murray-Gellman bijvoorbeeld het bestaan van een deeltje voorspellen voordat het daadwerkelijk werd waargenomen in experimenten. [3] Een ander voorbeeld: scheikundigen gebruiken de groepentheorie om de vormen van moleculen te classificeren. Wiskundigen hebben het concept van een groep zelfs gebruikt om conclusies te trekken over zoiets concreets als behangpapier!


Laten zien dat een verzameling Elements met een of andere operator een groep is, betekent in wezen dat wat je beschrijft een bepaalde symmetrie heeft. Geen symmetrie in de gewone zin van het woord, maar in een meer abstracte vorm. En dit kan substantiële inzichten opleveren in bepaalde systemen en problemen. De complexere begrippen uit de abstracte algebra geven ons alleen maar aanvullende informatie.


Het belangrijkste is dat je het belang van getaltheoretische groepen en velden in de praktijk zult zien door hun toepassing in cryptografie, in het bijzonder publieke sleutel cryptografie. In onze bespreking van velden hebben we bijvoorbeeld al gezien hoe extensievelden worden gebruikt in het Rijndael-cijfer. We zullen dat voorbeeld uitwerken in *Hoofdstuk 5*.


Voor verdere discussie over abstracte algebra raad ik de uitstekende videoserie over abstracte algebra van Socratica aan. [4] Ik zou in het bijzonder de volgende video's aanraden: "Wat is abstracte algebra?", "Groepsdefinitie (uitgebreid)", "Ringdefinitie (uitgebreid)", en "Velddefinitie (uitgebreid)" Deze vier video's geven je wat extra inzicht in veel van de bovenstaande discussie. (We hebben het niet over ringen gehad, maar een veld is gewoon een speciaal type ring)


Voor verdere discussie over moderne getaltheorie kun je veel geavanceerde discussies over cryptografie raadplegen. Jonathan Katz en Yehuda Lindell's Introduction to Modern Cryptography of Christof Paar en Jan Pelzl's Understanding Cryptography zijn suggesties voor verdere discussie. [5]


**Noten:**


[3] Bekijk [YouTube Video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)


[4] Socratica, [Abstracte Algebra] (https://www.socratica.com/subject/abstract-algebra)


[5] Katz en Lindell, *Introduction to Modern Cryptography*, 2nd edn, 2015 (CRC Press: Boca Raton, FL). Paar en Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlijn).




# Symmetrische cryptografie

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>



## Alice en Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>


Een van de twee hoofdtakken van cryptografie is symmetrische cryptografie. Het omvat zowel versleutelingsschema's als schema's die te maken hebben met authenticatie en integriteit. Tot de jaren 1970 bestond alle cryptografie uit symmetrische encryptiesystemen.


De hoofddiscussie begint met het bekijken van symmetrische encryptieschema's en het maken van het cruciale onderscheid tussen stream ciphers en block ciphers. Daarna komen de codes voor de authentificatie van berichten aan bod, die systemen zijn om de integriteit en authenticiteit van berichten te garanderen. Tot slot onderzoeken we hoe symmetrische versleutelingsschema's en berichtenauthenticatiecodes gecombineerd kunnen worden om veilige communicatie te garanderen.


Dit hoofdstuk bespreekt en passant verschillende symmetrische cryptografische schema's uit de praktijk. Het volgende hoofdstuk biedt een gedetailleerde uiteenzetting van encryptie met een streamcipher en een blokcipher uit de praktijk, namelijk respectievelijk RC4 en AES.


Voordat we beginnen met onze discussie over symmetrische cryptografie, wil ik kort enkele opmerkingen maken over de Alice en Bob illustraties in dit en volgende hoofdstukken.


___


Bij het illustreren van de principes van cryptografie wordt vaak gebruik gemaakt van voorbeelden met Alice en Bob. Dat zal ik ook doen.


Vooral als je nieuw bent in cryptografie, is het belangrijk te beseffen dat deze voorbeelden van Alice en Bob enkel bedoeld zijn als illustratie van cryptografische principes en constructies in een vereenvoudigde omgeving. De principes en constructies zijn echter toepasbaar op een veel breder scala van real-life contexten.


Hieronder volgen vijf belangrijke punten om in gedachten te houden over voorbeelden met Alice en Bob in cryptografie:


1. Ze kunnen gemakkelijk worden vertaald naar voorbeelden met andere soorten actoren, zoals bedrijven of overheidsorganisaties.

2. Ze kunnen gemakkelijk worden uitgebreid met drie of meer acteurs.

3. In de voorbeelden zijn Bob en Alice actieve deelnemers aan het creëren van elk bericht en aan het toepassen van cryptografische schema's op dat bericht. Maar in werkelijkheid is elektronische communicatie grotendeels geautomatiseerd. Wanneer je bijvoorbeeld een website bezoekt met Layer transportbeveiliging, wordt de cryptografie meestal allemaal afgehandeld door jouw computer en de webserver.

4. In de context van elektronische communicatie zijn de "berichten" die over een communicatiekanaal worden verzonden meestal TCP/IP pakketten. Deze kunnen horen bij een e-mail, een Facebook-bericht, een telefoongesprek, een bestandsoverdracht, een website, een software-upload, enzovoort. Het zijn geen berichten in de traditionele zin. Toch zullen cryptografen deze realiteit vaak vereenvoudigen door te stellen dat het bericht bijvoorbeeld een e-mail is.

5. De voorbeelden richten zich meestal op elektronische communicatie, maar ze kunnen ook worden uitgebreid naar traditionele vormen van communicatie zoals brieven.



## Symmetrische coderingssystemen

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>


We kunnen een **symmetrisch encryptieschema** losjes definiëren als elk cryptografisch schema met drie algoritmen:


1. Een **sleutelgeneratiealgoritme** dat een privésleutel genereert.

2. Een **encryptie-algoritme** dat de privésleutel en een klare tekst als invoer neemt en een cijfertekst weergeeft.

3. Een **decryptie-algoritme** dat de privésleutel en de cijfertekst als invoer neemt en de originele platte tekst weergeeft.


Meestal biedt een versleutelingsschema - symmetrisch of asymmetrisch - een sjabloon voor versleuteling op basis van een kernalgoritme, in plaats van een exacte specificatie.


Neem bijvoorbeeld Salsa20, een symmetrisch encryptieschema. Het kan worden gebruikt met zowel 128- als 256-bits sleutellengtes. De keuze van de sleutellengte heeft invloed op enkele kleine details van het algoritme (het aantal rondes in het algoritme om precies te zijn).


Maar je zou niet kunnen zeggen dat Salsa20 met een 128-bits sleutel een ander encryptieschema is dan Salsa20 met een 256-bits sleutel. Het kernalgoritme blijft hetzelfde. Alleen als het kernalgoritme verandert, kunnen we echt spreken van twee verschillende versleutelingsschema's.


Symmetrische versleutelingsschema's zijn typisch nuttig in twee soorten gevallen: (1) die waarin twee of meer agenten op afstand communiceren en de inhoud van hun communicatie geheim willen houden; en (2) die waarin één agent de inhoud van een bericht geheim wil houden in de tijd.


Je kunt een afbeelding van situatie (1) zien in *Figuur 1* hieronder. Bob wil een bericht $M$ naar Alice sturen over een afstand, maar wil niet dat anderen dat bericht kunnen lezen.


Bob versleutelt eerst het bericht $M$ met de privésleutel $K$. Vervolgens stuurt hij de cijfertekst $C$ naar Alice. Zodra Alice de cijfertekst heeft ontvangen, kan ze deze ontsleutelen met de sleutel $K$ en de klare tekst lezen. Met een goed versleutelingsschema zou een aanvaller die de cijfertekst $C$ onderschept, niets echt belangrijks te weten moeten kunnen komen over het bericht $M$.


Je kunt een afbeelding van situatie (2) zien in *Figuur 2* hieronder. Bob wil voorkomen dat anderen bepaalde informatie kunnen zien. Een typische situatie zou kunnen zijn dat Bob een werknemer is die gevoelige gegevens op zijn computer opslaat, die buitenstaanders noch zijn collega's mogen lezen.


Bob versleutelt het bericht $M$ op tijdstip $T_0$ met de sleutel $K$ om de cijfertekst $C$ te produceren. Op tijdstip $T_1$ heeft hij het bericht weer nodig en ontcijfert hij de cijfertekst $C$ met de sleutel $K$. Een aanvaller die in de tussentijd de cijfertekst $C$ is tegengekomen, kan hieruit niets significants over $M$ afleiden.



*Figuur 1: Geheimhouding in de ruimte*


![Figure 1: Secrecy across space](assets/Figure4-1.webp "Figure 1: Secrecy across space")



*Figuur 2: Geheimhouding in de tijd*



![Figure 2: Secrecy across time](assets/Figure4-2.webp "Figure 2: Secrecy across time")




## Een voorbeeld: Het verschuivingscijfer

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>


In Hoofdstuk 2 kwamen we het shift cijfer tegen, wat een voorbeeld is van een zeer eenvoudig symmetrisch versleutelingsschema. Laten we het hier nog eens bekijken.


Veronderstel een woordenboek *D* dat alle letters van het Engelse alfabet, in volgorde, gelijkstelt aan de verzameling getallen ${0,1,2,\dots,25}$. Ga uit van een reeks mogelijke berichten **M**. Het shift cijfer is dan een versleutelingsschema dat als volgt gedefinieerd is:



- Selecteer willekeurig een sleutel $k$ uit de verzameling mogelijke sleutels **K**, waarbij **K** = ${0,1,2,\dots,25}$
- Versleutel een bericht $m in **M** als volgt:
    - Verdeel $m$ in de afzonderlijke letters $m_0, m_1,\dots, m_i, \dots, m_l$
    - Converteer elke $m_i$ naar een getal volgens *D*
    - Voor elke $m_i$, $c_i = [(m_i + k) √ 26]$
    - Converteer elke $c_i$ naar een letter volgens *D*
    - Combineer dan $c_0, c_1, c_dots, c_l$ om de cijfertekst $c$ te verkrijgen
- Ontcijfer een cijfertekst $c$ als volgt:
    - Converteer elke $c_i$ naar een getal volgens *D*
    - Voor elke $c_i$, $m_i = [(c_i - k) 26]$
    - Converteer elke $m_i$ naar een letter volgens *D*
    - Combineer dan $m_0, m_1,\dots, m_l$ om het oorspronkelijke bericht $m$ te verkrijgen


Het verschuivingscijfer is een symmetrisch versleutelingsschema omdat dezelfde sleutel wordt gebruikt voor zowel de vercijfering als de ontcijfering. Stel bijvoorbeeld dat je het bericht "DOG" wilt vercijferen met het shift cijfer en dat je willekeurig "24" als sleutel hebt gekozen. Het bericht versleutelen met deze sleutel levert "BME" op. De enige manier om het originele bericht terug te krijgen is door dezelfde sleutel, "24", te gebruiken voor het ontcijferingsproces.


Dit Shift-cijfer is een voorbeeld van een **monoalfabetisch substitutiecijfer**: een vercijferingsschema waarbij het alfabet van de cijfertekst vast is (d.w.z. er wordt slechts één alfabet gebruikt). Ervan uitgaande dat het ontcijferingsalgoritme deterministisch is, kan elke symobl in de substitutiecijfertekst hoogstens betrekking hebben op één symbool in de klaartekst.


Tot de jaren 1700 waren veel toepassingen van vercijfering gebaseerd op monoalfabetische substitutiecijfers, hoewel deze vaak veel complexer waren dan het Shift cijfer. Je zou bijvoorbeeld willekeurig een letter uit het alfabet kunnen kiezen voor elke originele tekstletter onder de beperking dat elke letter slechts één keer voorkomt in het alfabet van de cijfertekst. Dat betekent dat je 26 mogelijke sleutels zou hebben, wat enorm was in het precomputertijdperk.


Merk op dat je de term **cipher** veel tegenkomt in cryptografie. Wees je ervan bewust dat deze term verschillende betekenissen heeft. Sterker nog, ik ken minstens vijf verschillende betekenissen van de term binnen de cryptografie.


In sommige gevallen verwijst de term naar een versleutelingsschema, zoals in Shift cipher en monoalfabetisch substitutiecijfer. De term kan echter ook specifiek verwijzen naar het versleutelingsalgoritme, de privésleutel of alleen de cijfertekst van zo'n versleutelingsschema.


Tot slot kan de term cijfer ook verwijzen naar een kernalgoritme waaruit je cryptografische schema's kunt construeren. Dit kunnen verschillende versleutelingsalgoritmen zijn, maar ook andere soorten cryptografische schema's. Deze betekenis van de term wordt relevant in de context van blokcijfers (zie de paragraaf "Blokcijfers" hieronder).


Je kunt ook de termen **ontcijferen** en **ontcijferen** tegenkomen. Deze termen zijn slechts synoniemen voor vercijfering en ontcijfering.



## Brute kracht aanvallen en het principe van Kerckhoff

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>


Het shift cijfer is een zeer onveilig symmetrisch versleutelingsschema, tenminste in de moderne wereld. [1] Een aanvaller kan elke cijfertekst proberen te ontcijferen met alle 26 mogelijke sleutels om te zien welk resultaat zinvol is. Dit type aanval, waarbij de aanvaller gewoon door de sleutels loopt om te zien wat werkt, staat bekend als een **brute force aanval** of **exhaustive key search**.


Een encryptiesysteem voldoet aan een minimaal veiligheidsbegrip als het een verzameling mogelijke sleutels, of **sleutelruimte**, heeft die zo groot is dat brute-force aanvallen niet mogelijk zijn. Alle moderne encryptiesystemen voldoen aan deze standaard. Dit staat bekend als het **sufficient key space principle**. Een soortgelijk principe geldt voor verschillende soorten cryptografische schema's.


Om een idee te krijgen van de enorme sleutelruimte in moderne encryptieprogramma's, stel dat een bestand is versleuteld met een 128-bits sleutel volgens de geavanceerde encryptiestandaard. Dit betekent dat een aanvaller een set van $2^{128}$ sleutels heeft die ze moet doorlopen voor een brute force aanval. Een kans van 0,78% op succes met deze strategie zou betekenen dat de aanvaller ongeveer $2,65 maal 10^{36}$ sleutels moet doorlopen.


Stel dat we optimistisch aannemen dat een aanvaller $10^{16}$ sleutels per seconde kan proberen (d.w.z. 10 quadriljoen sleutels per seconde). Om 0,78% van alle sleutels in de sleutelruimte te testen, zou haar aanval $2,65 maal 10^{20}$ seconden moeten duren. Dit is ongeveer 8,4 biljoen jaar. Dus zelfs een brute force aanval door een absurd sterke tegenstander is niet realistisch met een modern 128-bits encryptieschema. Dit is het principe van voldoende sleutelruimte.


Is het verschuivingscijfer veiliger als de aanvaller het versleutelingsalgoritme niet kent? Misschien, maar niet veel.


In ieder geval gaat de moderne cryptografie er altijd van uit dat de veiligheid van een symmetrisch encryptieschema alleen berust op het geheim houden van de privésleutel. Er wordt altijd aangenomen dat de aanvaller alle andere details kent, inclusief de berichtruimte, de sleutelruimte, de cijfertekstruimte, het sleutelselectiealgoritme, het encryptiealgoritme en het decryptiealgoritme.


Het idee dat de veiligheid van een symmetrisch versleutelingsschema alleen kan berusten op de geheimhouding van de privésleutel staat bekend als **Kerckhoffs' principe**.


Zoals oorspronkelijk bedoeld door Kerckhoffs, is het principe alleen van toepassing op symmetrische versleutelingssystemen. Een meer algemene versie van het principe is echter ook van toepassing op alle andere moderne soorten cryptografische schema's: Het ontwerp van een cryptografisch schema hoeft niet geheim te zijn om het veilig te maken; de geheimhouding kan zich alleen uitstrekken tot bepaalde informatiereeksen, meestal een privésleutel.


Het principe van Kerckhoffs staat centraal in de moderne cryptografie om vier redenen. [2] Ten eerste zijn er slechts een beperkt aantal cryptografische schema's voor bepaalde soorten toepassingen. De meeste moderne symmetrische versleutelingstoepassingen gebruiken bijvoorbeeld het Rijndael cijfer. Je geheimhouding over het ontwerp van een schema is dus zeer beperkt. Er is echter veel meer flexibiliteit in het geheim houden van een privésleutel voor het Rijndael cijfer.


Ten tweede is het makkelijker om een stukje informatie te vervangen dan een heel cryptografisch schema. Stel dat de werknemers van een bedrijf allemaal dezelfde encryptiesoftware hebben en dat elke twee werknemers een privésleutel hebben om vertrouwelijk te communiceren. Sleutelcompromittering is een gedoe in dit scenario, maar het bedrijf kan tenminste de software behouden met zulke veiligheidslekken. Als het bedrijf zou vertrouwen op de geheimhouding van het schema, dan zou bij elke inbreuk op die geheimhouding alle software vervangen moeten worden.


Ten derde maakt het principe van Kerckhoffs standaardisatie en compatibiliteit tussen gebruikers van cryptografische schema's mogelijk. Dit heeft enorme voordelen voor de efficiëntie. Het is bijvoorbeeld moeilijk voor te stellen hoe miljoenen mensen elke dag veilig verbinding kunnen maken met de webservers van Google, als die veiligheid vereist dat cryptografische schema's geheim blijven.


Ten vierde maakt het principe van Kerckhoff openbaar onderzoek van cryptografische schema's mogelijk. Dit type onderzoek is absoluut noodzakelijk om veilige cryptografische schema's te maken. Ter illustratie: het belangrijkste kernalgoritme in symmetrische cryptografie, het Rijndael cijfer, was het resultaat van een wedstrijd georganiseerd door het National Institute of Standards and Technology tussen 1997 en 2000.


Elk systeem dat probeert **security by obscurity** te bereiken is een systeem dat vertrouwt op het geheim houden van de details van het ontwerp en/of de implementatie. In cryptografie zou dit specifiek een systeem zijn dat vertrouwt op het geheim houden van de details van het ontwerp van het cryptografische schema. Beveiliging door vergetelheid staat dus in direct contrast met het principe van Kerckhoff.


Het vermogen van openheid om kwaliteit en veiligheid te versterken strekt zich ook breder uit tot de digitale wereld dan alleen cryptografie. Vrije en open source Linux distributies zoals Debian, bijvoorbeeld, hebben over het algemeen verschillende voordelen ten opzichte van hun Windows en MacOS tegenhangers in termen van privacy, stabiliteit, veiligheid en flexibiliteit. Hoewel dat meerdere oorzaken kan hebben, is het belangrijkste principe waarschijnlijk, zoals Eric Raymond het verwoordde in zijn beroemde essay "The Cathedral and the Bazaar", dat "gegeven genoeg ogen, alle bugs oppervlakkig zijn" [3] Het is dit wisdom of the crowds-principe dat Linux zijn grootste succes gaf.


Men kan nooit ondubbelzinnig stellen dat een cryptografisch schema "veilig" of "onveilig" is In plaats daarvan zijn er verschillende noties van veiligheid voor cryptografische schema's. Elke **definitie van cryptografische veiligheid** moet (1) veiligheidsdoelen specificeren, evenals (2) de mogelijkheden van een aanvaller. Het analyseren van cryptografische schema's aan de hand van één of meer specifieke begrippen van veiligheid geeft inzicht in hun toepassingen en beperkingen.


Hoewel we niet in alle details van de verschillende begrippen van cryptografische veiligheid zullen duiken, moet je weten dat twee aannames alomtegenwoordig zijn in alle moderne cryptografische begrippen van veiligheid die betrekking hebben op symmetrische en asymmetrische schema's (en in een bepaalde vorm op andere cryptografische primitieven):



- De kennis van de aanvaller over het schema voldoet aan het principe van Kerckhoffs.
- De aanvaller kan onmogelijk een brute force aanval uitvoeren op het systeem. De dreigingsmodellen van cryptografische beveiligingsconcepten staan brute force aanvallen meestal niet eens toe, omdat ze ervan uitgaan dat deze niet relevant zijn.



**Noten:**


[1] Volgens Seutonius werd een shift cijfer met een constante sleutelwaarde van 3 gebruikt door Julius Caesar in zijn militaire communicatie. Dus A werd altijd D, B altijd E, C altijd F, enzovoort. Deze specifieke versie van het verschuivingscijfer staat bekend als het **Caesar Cijfer** (hoewel het niet echt een cijfer is in de moderne betekenis van het woord, aangezien de sleutelwaarde constant is). Het Caesar cijfer kan veilig geweest zijn in de eerste eeuw voor Christus, als de vijanden van Rome niet vertrouwd waren met vercijfering. Maar in de moderne tijd zou het duidelijk geen erg veilig systeem zijn.


[2] Jonathan Katz en Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), p. 7f.


[3] Eric Raymond, "The Cathedral and the Bazaar," paper werd gepresenteerd op het Linux Kongress, Würzburg, Duitsland (27 mei 1997). Er zijn een aantal latere versies beschikbaar, evenals een boek. Mijn citaten komen van pagina 30 in het boek: Eric Raymond, _De kathedraal en de bazaar: Mijmeringen over Linux en Open Source door een toevallige revolutionair_, herziene uitgave. (2001), O'Reilly: Sebastopol, CA.



## Streamcijfers

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>


Symmetrische versleutelingsschema's zijn standaard onderverdeeld in twee types: **stroomcijfers** en **blokcijfers**. Dit onderscheid is echter wat lastig, omdat mensen deze termen op een inconsistente manier gebruiken. In de volgende secties zal ik het onderscheid uiteenzetten op de manier die mij het beste lijkt. Je moet je er echter van bewust zijn dat veel mensen deze termen op een iets andere manier zullen gebruiken dan ik heb uiteengezet.


Laten we eerst eens kijken naar stream ciphers. Een **stroomcijfer** is een symmetrisch versleutelingsschema waarbij de versleuteling uit twee stappen bestaat.


Eerst wordt een string met de lengte van de platte tekst gemaakt via een privésleutel. Deze string wordt de **keystream** genoemd.


Vervolgens wordt de keystream wiskundig gecombineerd met de klare tekst om een cijfertekst te produceren. Deze combinatie is meestal een XOR-bewerking. Voor ontcijfering kun je de operatie gewoon omkeren. (Merk op dat $A \oplus B = B \oplus A$, in het geval $A$ en $B$ bitstrings zijn. Dus de volgorde van een XOR operatie in een stream cipher maakt niet uit voor het resultaat. Deze eigenschap staat bekend als **commutativiteit**.)


Een typisch XOR-stroomcijfer is afgebeeld in *Figuur 3*. Je neemt eerst een privésleutel $K$ en gebruikt deze om generate een keystream te maken. De keystream wordt vervolgens gecombineerd met de klaartekst via een XOR operatie om de cijfertekst te produceren. Elke agent die de cijfertekst ontvangt, kan deze eenvoudig ontcijferen als hij de sleutel $K$ heeft. Het enige wat ze hoeft te doen is een keystream te maken die even lang is als de cijfertekst volgens de gespecificeerde procedure van het schema en deze te XOR-en met de cijfertekst.



*Afbeelding 3: Een XOR-stroomcijfer*


![Figure 3: An XOR stream cipher](assets/Figure4-3.webp "Figure 3: An XOR stream cipher")


Onthoud dat een encryptieschema meestal een sjabloon is voor encryptie met hetzelfde kernalgoritme, in plaats van een exacte specificatie. Bij uitbreiding is een streamcipher typisch een sjabloon voor encryptie waarin je sleutels van verschillende lengtes kunt gebruiken. Hoewel de sleutellengte van invloed kan zijn op enkele kleine details van het schema, heeft het geen invloed op de essentie ervan.


Het shift cijfer is een voorbeeld van een zeer eenvoudig en onveilig streamcijfer. Met behulp van een enkele letter (de privé-sleutel) kan een reeks letters met de lengte van het bericht worden gemaakt (de sleutelstroom). Deze keystream wordt vervolgens gecombineerd met de klaartekst via een modulo-operatie om een cijfertekst te produceren. (Deze modulo-operatie kan worden vereenvoudigd tot een XOR-operatie als de letters in bits worden weergegeven).


Een ander beroemd voorbeeld van een stroomcijfer is het **Vigenere cijfer**, naar Blaise de Vigenere die het volledig ontwikkelde aan het einde van de 16e eeuw (hoewel anderen al veel eerder werk hadden gedaan). Het is een voorbeeld van een **polyalfabetisch substitutiecijfer**: een encryptieschema waarbij het cijfertekstalfabet voor een klaartekstsymbool verandert afhankelijk van de positie in de tekst. In tegenstelling tot een monoalfabetisch substitutiecijfer kunnen cijfertekstsymbolen geassocieerd worden met meer dan één klaartekstsymbool.


Terwijl vercijfering aan populariteit won in het Europa van de Renaissance, nam ook **cryptanalyse** - het breken van cijferteksten - toe, in het bijzonder met behulp van **frequentieanalyse**. Dit laatste maakt gebruik van statistische regelmatigheden in onze taal om cijferteksten te breken en werd al in de negende eeuw ontdekt door Arabische geleerden. Het is een techniek die vooral goed werkt bij langere teksten. En zelfs de meest gesofisticeerde monoalfabetische substitiecijfers volstonden niet meer tegen frequentieanalyse in de jaren 1700 in Europa, vooral in militaire en veiligheidsomgevingen. Omdat het Vigenere cijfer een significante verbetering in veiligheid bood, werd het populair in deze periode en was het wijdverspreid aan het einde van de 17de eeuw.


Informeel werkt het versleutelingsschema als volgt:


1. Selecteer een woord van meerdere letters als privésleutel.

2. Pas voor elk bericht het shift cijfer toe op elke letter van het bericht met de corresponderende letter in het sleutelwoord als shift.

3. Als je het sleutelwoord hebt doorlopen maar de klare tekst nog steeds niet volledig hebt vercijferd, pas dan opnieuw de letters van het sleutelwoord toe als een shift vercijfering op de corresponderende letters in de rest van de tekst.

4. Ga door met dit proces totdat het hele bericht vercijferd is.


Ter illustratie, stel dat je privésleutel "GOUD" is en je wilt het bericht "CRYPTOGRAFIE" versleutelen. In dat geval zou je als volgt te werk gaan volgens het Vigenère-cijfer:



- $c_0 = [(2 + 6) 26] = 8 = I$
- $c_1 = [(17 + 14) \26] = 5 = F$
- $c_2 = [(24 + 11) √ 26] = 9 = J$
- $c_3 = [(15 + 3) 26] = 18 = S$
- $c_4 = [(19 + 6) √ 26] = 25 = Z$
- $c_5 = [(14 + 14) √ 26] = 2 = C$
- $c_6 = [(6 + 11) 26] = 17 = R$
- $c_7 = [(17 + 3) 26] = 20 = U$
- $c_8 = [(0 + 6) 26] = 6 = G$
- $c_9 = [(15 + 14) √ 26] = 3 = D$
- $c_{10} = [(7 + 11) mod 26] = 18 = S$
- $c_{11} = [(24 + 3) mod 26] = 1 = B$


De cijfertekst $c$ = "IFJSZCRUGDSB".


Een ander bekend voorbeeld van een stream cipher is het **one-time pad**. Met het one-time pad maak je gewoon een reeks willekeurige bits die even lang is als het bericht met de klaartekst en produceer je de cijfertekst via de XOR-bewerking. De private sleutel en de keystream zijn dus gelijkwaardig met een one-time pad.


Terwijl het Shift-cijfer en de Vigenere-cijfers erg onveilig zijn in het moderne tijdperk, is het one-time pad erg veilig als het correct gebruikt wordt. Waarschijnlijk de meest bekende toepassing van het one-time pad was, tenminste tot de jaren 1980, voor de **Washington-Moskou hotline**. [4]


De hotline is een directe communicatieverbinding tussen Washington en Moskou voor dringende zaken die werd geïnstalleerd na de Cubaanse Raketcrisis. De technologie voor de hotline is in de loop der jaren veranderd. Momenteel omvat het een directe glasvezelkabel en twee satellietverbindingen (voor redundantie), die e-mail en sms mogelijk maken. De verbinding eindigt op verschillende plaatsen in de VS. Het Pentagon, het Witte Huis en Raven Rock Mountain zijn bekende eindpunten. In tegenstelling tot wat vaak wordt gedacht, zijn er nooit telefoons bij de hotline betrokken geweest.


In essentie werkte het one-time pad schema als volgt. Zowel Washington als Moskou beschikten over twee sets willekeurige getallen. Eén reeks willekeurige getallen, gecreëerd door de Russen, had betrekking op het vercijferen en ontcijferen van berichten in de Russische taal. Eén set willekeurige getallen, gecreëerd door de Amerikanen, had betrekking op vercijfering en ontcijfering van berichten in de Engelse taal. Van tijd tot tijd werden er meer willekeurige getallen naar de andere kant gestuurd door betrouwbare koeriers.


Washington en Moskou konden toen in het geheim communiceren door deze willekeurige getallen te gebruiken voor het maken van one-time pads. Elke keer dat je moest communiceren, gebruikte je het volgende deel willekeurige getallen voor je bericht.


Hoewel het one-time pad zeer veilig is, kent het belangrijke praktische beperkingen: de sleutel moet even lang zijn als het bericht en geen enkel deel van een one-time pad kan hergebruikt worden. Dit betekent dat je moet bijhouden waar je bent in het one-time pad, een enorm aantal bits moet opslaan en van tijd tot tijd Exchange willekeurige bits met je tegenpartijen moet uitwisselen. Bijgevolg wordt het one-time pad in de praktijk niet vaak gebruikt.


In plaats daarvan zijn de meest gebruikte stream ciphers in de praktijk **pseudorandom stream ciphers**. Salsa20 en een nauw verwante variant genaamd ChaCha zijn voorbeelden van veelgebruikte pseudorandom streamcijfers.


Met deze pseudo-willekeurige stream ciphers kies je eerst willekeurig een sleutel K die korter is dan de lengte van de klare tekst. Zo'n willekeurige sleutel K wordt meestal door onze computer gemaakt op basis van onvoorspelbare gegevens die hij in de loop van de tijd verzamelt, zoals de tijd tussen netwerkberichten, muisbewegingen, enzovoort.


Deze willekeurige sleutel $K$ wordt dan ingevoegd in een uitbreidingsalgoritme dat een pseudo-willekeurige sleutelstroom creëert die even lang is als het bericht. Je kunt precies aangeven hoe lang de sleutelstroom moet zijn (bijvoorbeeld 500 bits, 1000 bits, 1200 bits, 29.117 bits, enzovoort).


Een pseudo-willekeurige sleutelstroom lijkt *alsof* hij volledig willekeurig gekozen werd uit de verzameling van alle strings met dezelfde lengte. Vandaar dat vercijfering met een pseudorandom keystream lijkt alsof het gedaan is met een one-time pad. Maar dat is natuurlijk niet het geval.


Aangezien onze privésleutel korter is dan de sleutelstroom en ons expansiealgoritme deterministisch moet zijn om het versleutelings-/ontsleutelingsproces te laten werken, kan niet elke sleutelstroom van die specifieke lengte als uitvoer van onze expansiebewerking zijn gebruikt.


Stel bijvoorbeeld dat onze privésleutel een lengte heeft van 128 bits en dat we deze kunnen invoegen in een uitbreidingsalgoritme om een veel langere sleutelstroom te maken, bijvoorbeeld van 2.500 bits. Aangezien ons uitbreidingsalgoritme deterministisch moet zijn, kan ons algoritme maximaal $1/2^{128}$ strings selecteren met een lengte van 2.500 bits. Een dergelijke sleutelstroom kan dus nooit volledig willekeurig worden geselecteerd uit alle strings van dezelfde lengte.


Onze definitie van een streamcipher heeft twee aspecten: (1) een keystream die net zo lang is als de klare tekst wordt gegenereerd met behulp van een privésleutel; en (2) deze keystream wordt gecombineerd met de klare tekst, meestal via een XOR-bewerking, om de cijfertekst te produceren.


Soms definiëren mensen voorwaarde (1) strikter, door te beweren dat de sleutelstroom specifiek pseudorandom moet zijn. Dit betekent dat noch het shift cijfer, noch het one-time pad beschouwd worden als stream ciphers.


Naar mijn mening biedt een bredere definitie van voorwaarde (1) een eenvoudigere manier om versleutelingssystemen te organiseren. Bovendien betekent dit dat we niet hoeven te stoppen om een bepaald versleutelingsschema een stream cipher te noemen alleen omdat we leren dat het niet afhankelijk is van pseudorandom keystreams.


**Noten:**


[4] Crypto Museum, "Washington-Moskou hotline," 2013, beschikbaar op [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).




## Blokcijfers

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>


De eerste manier waarop een **blokcijfer** gewoonlijk wordt begrepen is als iets primitievers dan een streamcijfer: Een kernalgoritme dat een lengtebehoudende transformatie uitvoert op een string van een geschikte lengte met behulp van een sleutel. Dit algoritme kan worden gebruikt voor het maken van versleutelingsschema's en misschien andere soorten cryptografische schema's.


Vaak kan een blokcijfer invoerstrings van verschillende lengtes aannemen, zoals 64, 128 of 256 bits, evenals sleutels van verschillende lengtes, zoals 128, 192 of 256 bits. Hoewel sommige details van het algoritme kunnen veranderen afhankelijk van deze variabelen, verandert het kernalgoritme niet. Als dat wel zo was, zouden we spreken van twee verschillende blokcijfers. Merk op dat het gebruik van de terminologie van het kernalgoritme hier hetzelfde is als voor versleutelingsschema's.


In *Figuur 4* hieronder is te zien hoe een bloksleutel werkt. Een bericht $M$ met lengte $L$ en een sleutel $K$ dienen als invoer voor het blokcijfer. Het resultaat is een bericht $M$ met een lengte van $L$. De sleutel hoeft niet noodzakelijk dezelfde lengte te hebben als $M$ en $M'$ voor de meeste blokcijfers.


*Afbeelding 4: Een blokcijfer*


![Figure 4: A block cipher](assets/Figure4-4.webp "Figure 4: A block cipher")


Een blokcijfer op zichzelf is geen versleutelingsschema. Maar een blokcijfer kan gebruikt worden met verschillende **modi** om verschillende versleutelingsschema's te maken. Een modus voegt simpelweg wat extra operaties toe buiten het blokcijfer.


Om te illustreren hoe dit werkt, stellen we een blokcijfer (BC) voor dat een 128-bits invoerreeks en een 128-bits privésleutel vereist. Figuur 5 hieronder laat zien hoe dat blokcijfer gebruikt kan worden met **elektronische codeboekmodus** (**ECB-modus**) om een versleutelingsschema te maken. (De ellipsen aan de rechterkant geven aan dat je dit patroon zo lang als nodig kunt herhalen).


*Afbeelding 5: Een blokcijfer met ECB-modus*


![Figure 5: A block cipher with ECB mode](assets/Figure4-5.webp "Figure 5: A block cipher with ECB mode")


Het proces voor elektronische codeboekvercijfering met het blokcijfer is als volgt. Kijk of u uw klaartekstbericht kunt verdelen in blokken van 128 bits. Zo niet, voeg dan **padding** toe aan het bericht, zodat het resultaat gelijkmatig kan worden gedeeld door de blokgrootte van 128 bits. Dit zijn de gegevens die worden gebruikt voor het versleutelingsproces.


Splits nu de gegevens op in stukken van 128-bits strings ($M_1$, $M_2$, $M_3$, enzovoort). Laat elke 128-bits string door het blokcijfer lopen met uw 128-bits sleutel om 128-bits stukken cijfertekst te produceren ($C_1$, $C_2$, $C_3$, enzovoort). Deze stukken vormen samen de volledige cijfertekst.


Ontcijfering is precies het omgekeerde proces, hoewel de ontvanger een herkenbare manier nodig heeft om opvulling van de ontcijferde gegevens te verwijderen om het originele bericht met platte tekst te produceren.


Hoewel relatief eenvoudig, is een blokcijfer met elektronische codeboekmodus niet veilig. Dit komt omdat het leidt tot **deterministische encryptie**. Twee identieke 128-bits strings van gegevens worden op exact dezelfde manier versleuteld. Die informatie kan worden misbruikt.


In plaats daarvan zou elk encryptieschema dat is opgebouwd uit een blokcijfer **probabilistisch** moeten zijn: dat wil zeggen dat de encryptie van elk bericht $M$, of elk specifiek stuk van $M$, over het algemeen elke keer een ander resultaat zou moeten opleveren. [5]


De **cipher block chaining mode** (**CBC mode**) is waarschijnlijk de meest gebruikte modus met een blokcijfer. De combinatie levert, als het goed gedaan wordt, een probabilistisch encryptieschema op. U kunt een afbeelding van deze modus zien in *Figuur 6* hieronder.


*Afbeelding 6: Een blokcijfer met CBC-modus*


![Figure 6: A block cipher with CBC mode](assets/Figure4-6.webp "Figure 6: A block cipher with CBC mode")


Stel dat de blokgrootte weer 128 bits is. Om te beginnen moet je er dus opnieuw voor zorgen dat je originele plaintext bericht de nodige padding krijgt.


Vervolgens wordt het eerste 128-bits deel van de klaartekst ge-XOR't met een **initialisatievector** van 128-bits. Het resultaat wordt in het blokversleutelingsprogramma geplaatst om een cijfertekst voor het eerste blok te maken. Voor het tweede blok van 128 bits wordt eerst de klaartekst ge-XOR't met de cijfertekst van het eerste blok, voordat deze in het blokcijfer wordt geplaatst. Je gaat door met dit proces totdat je het volledige bericht hebt versleuteld.


Als je klaar bent, stuur je het versleutelde bericht samen met de onversleutelde initialisatievector naar de ontvanger. De ontvanger moet de initialisatievector kennen, anders kan ze de cijfertekst niet ontsleutelen.


Bij correct gebruik is deze constructie veel veiliger dan de elektronische codeboekmodus. Ten eerste moet je ervoor zorgen dat de initialisatievector een willekeurige of pseudo-willekeurige string is. Daarnaast moet je elke keer dat je dit versleutelingsschema gebruikt een andere initialisatievector gebruiken.


Met andere woorden, de initialisatievector moet een willekeurige of pseudo-willekeurige Nonce zijn, waarbij een **Nonce** staat voor "een getal dat maar één keer gebruikt wordt" Als je deze gewoonte aanhoudt, dan zorgt CBC modus met een blokcijfer ervoor dat twee identieke klaartekstblokken elke keer anders versleuteld worden.


Laten we tot slot onze aandacht richten op de **output feedback mode** (**OFB mode**). Je kunt een afbeelding van deze modus zien in *Figuur 7*.


*Afbeelding 7: Een blokcijfer met OFB-modus*


![Figure 7: A block cipher with OFB mode](assets/Figure4-7.webp "Figure 7: A block cipher with OFB mode")


Met OFB-modus selecteert u ook een initialisatievector. Maar hier wordt de initialisatievector voor het eerste blok direct in het blokcijfer ingevoegd met uw sleutel. De resulterende 128 bits worden dan behandeld als een sleutelstroom. Deze sleutelstroom wordt ge-XORed met de klaartekst om de cijfertekst voor het blok te produceren. Voor volgende blokken gebruikt u de keystream van het vorige blok als invoer in het blokversleutelingsprogramma en herhaalt u de stappen.


Als je goed kijkt, is wat hier eigenlijk is gemaakt van het blokcijfer met OFB-modus een streamcijfer. Je generate keystream-porties van 128 bits totdat je de lengte van de klaartekst hebt (waarbij je de bits die je niet nodig hebt van het laatste 128-bits keystream-portie weggooit). Vervolgens wordt de keystream ge-XOR't met de klaartekst om de cijfertekst te verkrijgen.


In de vorige paragraaf over stream ciphers heb ik gezegd dat je een keystream maakt met behulp van een privésleutel. Om precies te zijn, het hoeft niet alleen gemaakt te worden met een privésleutel. Zoals je kunt zien in OFB-modus, wordt de keystream geproduceerd met behulp van zowel een privésleutel als een initialisatievector.


Net als bij de CBC-modus is het belangrijk om een pseudo-willekeurig of willekeurig Nonce te selecteren voor de initialisatievector elke keer dat u een blokcijfer in OFB-modus gebruikt. Anders zal dezelfde 128-bit berichtstring die in verschillende communicaties wordt verzonden op dezelfde manier worden versleuteld. Dit is één manier om probabilistische versleuteling te creëren met een streamcipher.


Sommige stream ciphers gebruiken alleen een private sleutel om een keystream te creëren. Voor deze stream ciphers is het belangrijk dat je een willekeurige Nonce gebruikt om de private sleutel te selecteren voor elke communicatie. Anders zullen de resultaten van encryptie met deze stream ciphers ook deterministisch zijn, wat leidt tot veiligheidsproblemen.


Het populairste moderne blokcijfer is het **Rijndael cijfer**. Het was de winnende inzending uit vijftien inzendingen voor een wedstrijd gehouden door het National Institute of Standards and Technology (NIST) tussen 1997 en 2000 om een oudere encryptiestandaard, de **data encryption standard** (**DES**), te vervangen.


Het Rijndael-cijfer kan worden gebruikt met verschillende specificaties voor sleutellengtes en blokgroottes, en in verschillende werkingsmodi. Het comité voor de NIST competitie heeft een beperkte versie van het Rijndael cijfer aangenomen, namelijk een versie die blokgroottes van 128 bits en sleutellengtes van 128 bits, 192 bits of 256 bits vereist, als onderdeel van de **advanced encryption standard** (**AES**). Dit is echt de belangrijkste standaard voor symmetrische versleutelingstoepassingen. Het is zo veilig dat zelfs de NSA het blijkbaar wil gebruiken met 256-bits sleutels voor topgeheime documenten. [6]


Het AES blokcijfer wordt in detail uitgelegd in *Hoofdstuk 5*.



**Noten:**


[5] Het belang van probabilistische versleuteling werd voor het eerst benadrukt door Shafi Goldwasser en Silvio Micali, "Probabilistic encryption," _Journal of Computer and System Sciences_, 28 (1984), 270-99.


[6] Zie NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).




## De verwarring ophelderen

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>


De verwarring over het onderscheid tussen blokcijfers en streamcijfers ontstaat omdat mensen soms de term blokcijfer opvatten als een specifieke verwijzing naar een *blokcijfer met een blokmodus van encryptie*.


Neem de ECB en CBC modi uit de vorige sectie. Deze vereisen specifiek dat de gegevens voor encryptie deelbaar zijn door de blokgrootte (wat betekent dat je opvulling moet gebruiken voor het originele bericht). Bovendien worden de gegevens in deze modi ook direct bewerkt door het blokcijfer (en niet alleen gecombineerd met het resultaat van een blokcijferbewerking zoals in OFB-modus).


Als alternatief kun je dus een **bloksleutel** definiëren als elk versleutelingsschema dat werkt op blokken van een bericht met een vaste lengte per keer (waarbij elk blok langer moet zijn dan een byte, anders valt het uiteen in een streamsleutel). Zowel de gegevens voor versleuteling als de cijfertekst moeten gelijkmatig verdeeld zijn over deze blokgrootte. Meestal is de blokgrootte 64, 128, 192 of 256 bits lang. Daarentegen kan een streamcipher alle berichten versleutelen in brokken van één bit of byte per keer.


Met dit meer specifieke begrip van blokcijfers kun je inderdaad stellen dat moderne versleutelingsschema's ofwel stream ofwel blokcijfers zijn. Vanaf nu zal ik de term blokcijfers in de meer algemene zin gebruiken, tenzij anders aangegeven.


De discussie over de OFB-modus in de vorige sectie brengt ook een ander interessant punt naar voren. Sommige streamcijfers zijn opgebouwd uit blokcijfers, zoals Rijndael met OFB. Sommige zoals Salsa20 en ChaCha zijn niet opgebouwd uit blokcijfers. Deze laatste zou je **primitieve stroomcijfers** kunnen noemen. (Er is niet echt een gestandaardiseerde term om naar zulke stream ciphers te verwijzen)


Als mensen het hebben over de voor- en nadelen van stream ciphers en block ciphers, dan vergelijken ze meestal primitieve stream ciphers met encryptieschema's gebaseerd op block ciphers.


Hoewel je altijd gemakkelijk een streamcipher kunt construeren vanuit een blokcijfer, is het meestal erg moeilijk om een soort constructie met een blokmodus van encryptie (zoals met CBC-modus) te bouwen vanuit een primitief streamcijfer.


Na deze discussie zou je nu *Figuur 8* moeten begrijpen. Het geeft een overzicht van symmetrische encryptieschema's. We gebruiken drie soorten versleutelingsschema's: primitieve stream ciphers, block cipher stream ciphers en block ciphers in een blokmodus (ook wel "blokcijfers" genoemd in het diagram).


*Figuur 8: Overzicht van symmetrische versleutelingsschema's*


![Figure 8: Overview of symmetric encryption schemes](assets/Figure4-8.webp "Figure 8: Overview of symmetric encryption schemes")



## Codes voor berichtverificatie

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>


Encryptie houdt zich bezig met geheimhouding. Maar cryptografie houdt zich ook bezig met bredere thema's, zoals berichtintegriteit, authenticiteit en onweerlegbaarheid. Zogenaamde **berichtauthenticatiecodes** (MAC's) zijn symmetrische cryptografische sleutelschema's die authenticiteit en integriteit in communicatie ondersteunen.


Waarom is er iets anders nodig dan geheimhouding in communicatie? Stel dat Bob Alice een bericht stuurt met behulp van praktisch onbreekbare encryptie. Een aanvaller die dit bericht onderschept, zal niet in staat zijn om belangrijke inzichten over de inhoud te verkrijgen. De aanvaller heeft echter nog minstens twee andere aanvalsvectoren tot haar beschikking:


1. Ze kon de cijfertekst onderscheppen, de inhoud wijzigen en de gewijzigde cijfertekst naar Alice sturen.

2. Ze kon Bob's bericht volledig blokkeren en haar eigen gemaakte cijfertekst versturen.


In beide gevallen heeft de aanvaller misschien geen inzicht in de inhoud van cijferteksten (1) en (2). Toch kan ze op deze manier aanzienlijke schade aanrichten. Dit is waar berichtenauthenticatiecodes belangrijk worden.


Authenticatiecodes voor berichten worden losjes gedefinieerd als symmetrische cryptografische schema's met drie algoritmen: een sleutelgeneratiealgoritme, een taggeneratiealgoritme en een verificatiealgoritme. Een veilige MAC zorgt ervoor dat tags **existentieel niet te vervalsen** zijn voor een aanvaller-dat wil zeggen dat ze niet met succes een tag kunnen maken op het bericht dat verifieert, tenzij ze de privésleutel hebben.


Bob en Alice kunnen de manipulatie van een bepaald bericht tegengaan met behulp van een MAC. Stel dat ze zich niet druk maken om geheimhouding. Ze willen er alleen zeker van zijn dat het bericht dat Alice heeft ontvangen inderdaad van Bob afkomstig is en op geen enkele manier is veranderd.


Het proces wordt afgebeeld in *Figuur 9*. Om een **MAC** (Message Authentication Code) te gebruiken, zouden ze eerst generate een privésleutel $K$ geven die ze samen delen. Bob maakt een tag $T$ voor het bericht met behulp van de privésleutel $K$. Vervolgens stuurt hij het bericht en de tag voor het bericht naar Alice. Zij kan dan verifiëren dat Bob inderdaad de tag heeft gemaakt, door de private sleutel, het bericht en de tag door een verificatiealgoritme te laten lopen.


*Figuur 9: Overzicht van symmetrische versleutelingsschema's*


![Figure 9: Overview of symmetric encryption schemes](assets/Figure4-9.webp "Figure 9: Overview of symmetric encryption schemes")


Vanwege **existentiële onvervalsbaarheid** kan een aanvaller het bericht $M$ op geen enkele manier wijzigen of een eigen bericht met een geldige tag maken. Dit is zo, zelfs als de aanvaller de tags observeert van vele berichten tussen Bob en Alice die dezelfde private sleutel gebruiken. Een aanvaller kan hooguit Alice verhinderen het bericht $M$ te ontvangen (een probleem dat cryptografie niet kan Address).


Een MAC garandeert dat een bericht werkelijk door Bob werd gemaakt. Deze authenticiteit impliceert automatisch berichtintegriteit-dat wil zeggen, als Bob een bericht heeft gemaakt, dan is het ipso facto op geen enkele manier gewijzigd door een aanvaller. Dus vanaf hier moet elke zorg voor authenticatie automatisch begrepen worden als een zorg voor integriteit.


Hoewel ik in mijn discussie een onderscheid heb gemaakt tussen authenticiteit en integriteit van berichten, is het ook gebruikelijk om deze termen als synoniemen te gebruiken. Ze verwijzen dan naar het idee van berichten die door een bepaalde afzender zijn gemaakt en op geen enkele manier zijn gewijzigd. In deze geest worden authenticatiecodes voor berichten vaak ook integriteitcodes** voor berichten genoemd.



## Geverifieerde encryptie

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>


Normaal gesproken wil je zowel geheimhouding als authenticiteit garanderen in communicatie en daarom worden versleutelingsschema's en MAC-schema's meestal samen gebruikt.


Een **geauthenticeerd encryptieschema** is een schema dat encryptie combineert met een MAC op een zeer veilige manier. Specifiek moet het voldoen aan de standaarden voor existentiële onvervalsbaarheid evenals aan een zeer sterke notie van geheimhouding, namelijk één die bestand is tegen **gekozen-coderingstekst aanvallen**. [7]


Opdat een encryptieschema bestand zou zijn tegen "chosen-ciphertext"-aanvallen, moet het voldoen aan de normen voor **non-malleability**: dat wil zeggen dat elke wijziging van een cijfertekst door een aanvaller ofwel een ongeldige cijfertekst moet opleveren ofwel een tekst die ontcijfert naar een klaartekst die geen verband houdt met de originele. [8]


Aangezien een geauthenticeerd versleutelingsschema ervoor zorgt dat een cijfertekst gemaakt door een aanvaller altijd ongeldig is (omdat de tag niet geverifieerd wordt), voldoet het aan de normen voor weerstand tegen chosen-ciphertext aanvallen. Interessant genoeg kun je bewijzen dat een geauthenticeerd versleutelingsschema altijd kan worden gemaakt uit de combinatie van een existentieel onvervalsbare MAC en een versleutelingsschema dat voldoet aan een minder sterk begrip van veiligheid, bekend als **gekozen-plaintext-aanvalbeveiliging**.


We zullen niet ingaan op alle details van het construeren van geauthenticeerde encryptie schema's. Maar het is belangrijk om twee details van hun constructie te weten.


Ten eerste zorgt een geauthenticeerd encryptieschema eerst voor de encryptie en creëert dan een tag op de cijfertekst. Het blijkt dat andere benaderingen, zoals het combineren van de cijfertekst met een tag op de klaartekst, of eerst een tag maken en dan zowel de klaartekst als de tag versleutelen, onveilig zijn. Bovendien hebben beide bewerkingen hun eigen willekeurig gekozen privésleutel, anders is de beveiliging ernstig in gevaar.


Het bovenstaande principe geldt meer in het algemeen: *je moet altijd verschillende sleutels gebruiken bij het combineren van basis cryptografische schema's*.


Een geauthenticeerd encryptieschema wordt afgebeeld in *Figuur 10*. Bob maakt eerst een cijfertekst $C$ van het bericht $M$ met behulp van een willekeurig gekozen sleutel $K_C$. Vervolgens maakt hij een berichttag $T$ door de cijfertekst en een andere willekeurig gekozen sleutel $K_T$ door het algoritme voor het genereren van tags te laten lopen. Zowel de cijfertekst als de berichttag worden naar Alice gestuurd.


Alice controleert nu eerst of de tag geldig is gegeven de cijfertekst $C$ en de sleutel $K_T$. Als deze geldig is, kan ze het bericht ontcijferen met de sleutel $K_C$. Niet alleen is ze verzekerd van een zeer sterke notie van geheimhouding in hun communicatie, maar ze weet ook dat het bericht gemaakt is door Bob.


*Figuur 10: Een geauthenticeerd versleutelingsschema*


![Figure 10: An authenticated encryption scheme](assets/Figure4-10.webp "Figure 10: An authenticated encryption scheme")


Hoe worden MAC's aangemaakt? Hoewel MAC's op verschillende manieren aangemaakt kunnen worden, is een gebruikelijke en efficiënte manier om ze aan te maken ** via cryptografische Hash functies**.


We zullen cryptografische Hash functies uitgebreider introduceren in *Hoofdstuk 6*. Voor nu is het voldoende te weten dat een **Hash functie** een efficiënt berekenbare functie is die invoer van willekeurige grootte neemt en uitvoer met een vaste lengte oplevert. Bijvoorbeeld, de populaire Hash functie **SHA-256** (veilig Hash algoritme 256) genereert altijd een 256-bit uitvoer, ongeacht de grootte van de invoer. Sommige Hash functies, zoals SHA-256, hebben nuttige toepassingen in cryptografie.


Het meest voorkomende type tag dat geproduceerd wordt met een cryptografische Hash functie is de **Hash-gebaseerde berichtauthenticatiecode** (HMAC). Het proces wordt afgebeeld in *Figuur 11*. Een partij maakt twee verschillende sleutels van een privésleutel $K$, de binnensleutel $K_1$ en de buitensleutel $K_2$. De klare tekst $M$ of cijfertekst $C$ wordt vervolgens gehashed met de binnenste sleutel. Het resultaat $T'$ wordt vervolgens gehasht met de buitenste sleutel om de message tag $T$ te produceren.


Er is een palet aan Hash functies die gebruikt kunnen worden om een HMAC te maken. De meest gebruikte Hash-functie is SHA-256.



*Afbeelding 11: HMAC*


![Figure 11: HMAC](assets/Figure4-11.webp "Figure 11: HMAC")


**Noten:**


[7] De specifieke resultaten die in deze paragraaf worden besproken, komen uit Katz en Lindell, pp. 131-47.


[8] Technisch gezien is de definitie van "chosen cipher text attacks" anders dan het begrip "non-malleability". Maar je kunt aantonen dat deze twee noties van veiligheid gelijkwaardig zijn.




## Beveiligde communicatiesessies

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>


Stel dat twee partijen in een communicatiesessie zitten en dus meerdere berichten heen en weer sturen.


Een geauthenticeerd versleutelingsschema stelt een ontvanger van een bericht in staat om te verifiëren dat het is gemaakt door haar partner in de communicatiesessie (zolang de privésleutel niet is uitgelekt). Dit werkt goed genoeg voor een enkel bericht. Normaal gesproken sturen twee partijen echter berichten heen en weer in een communicatiesessie. En in die setting schiet een gewoon geauthenticeerd encryptieschema zoals beschreven in de vorige sectie tekort in het bieden van veiligheid.


De belangrijkste reden hiervoor is dat een geauthenticeerd encryptieschema geen garanties biedt dat het bericht daadwerkelijk ook verstuurd is door de agent die het gemaakt heeft binnen een communicatiesessie. Beschouw de volgende drie aanvalsvectoren:


1. **Replay-aanval**: Een aanvaller verstuurt een cijfertekst en een tag die ze op een eerder moment tussen twee partijen heeft onderschept opnieuw.

2. **Herschikkingsaanval**: Een aanvaller onderschept twee berichten op verschillende tijdstippen en stuurt ze in omgekeerde volgorde naar de ontvanger.

3. **Reflectie aanval**: Een aanvaller observeert een bericht dat van A naar B wordt gestuurd, en stuurt dat bericht ook naar A.


Hoewel de aanvaller geen kennis heeft van de cijfertekst en geen vervalste cijferteksten kan maken, kunnen de bovenstaande aanvallen nog steeds aanzienlijke schade aanrichten in de communicatie.


Stel bijvoorbeeld dat een bepaald bericht tussen de twee partijen de overdracht van financiële middelen betreft. Een replay aanval zou het geld een tweede keer kunnen overmaken. Een vanille geauthenticeerd encryptie schema heeft geen verdediging tegen zulke aanvallen.


Gelukkig kunnen dit soort aanvallen eenvoudig worden gemitigeerd in een communicatiesessie door **identifiers** en **relatieve tijdsindicatoren** te gebruiken.


Identifiers kunnen worden toegevoegd aan het bericht voordat het wordt versleuteld. Dit zou alle reflectieaanvallen verhinderen. Een relatieve tijdsindicator kan bijvoorbeeld een volgnummer zijn in een bepaalde communicatiesessie. Elke partij voegt een volgnummer toe aan een bericht voordat het wordt versleuteld, zodat de ontvanger weet in welke volgorde de berichten zijn verzonden. Dit elimineert de mogelijkheid van herordeningsaanvallen. Het elimineert ook replay-aanvallen. Elk bericht dat een aanvaller naar beneden stuurt, heeft een oud volgnummer en de ontvanger weet dat hij het bericht niet opnieuw moet verwerken.


Om te illustreren hoe beveiligde communicatiesessies werken, stel opnieuw Alice en Bob. Ze sturen in totaal vier berichten heen en weer. Je kunt hieronder in *Figuur 11* zien hoe een geauthenticeerd encryptieschema met identifiers en volgnummers zou werken.


De communicatiesessie begint met Bob die een cijfertekst $C_{0,B}$ naar Alice stuurt met een berichttag $T_{0,B}$. De cijfertekst bevat het bericht, evenals een identificator (Bob) en een volgnummer (0). De tag $T_{0,B}$ wordt gemaakt over de gehele cijfertekst. In hun volgende communicatie onderhouden Alice en Bob dit protocol, waarbij ze de velden waar nodig bijwerken.



*Afbeelding 12: Een beveiligde communicatiesessie*


![Figure 12: A secure communication session](assets/Figure4-12.webp "Figure 12: A secure communication sessesion")







# RC4 en AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>





## Het RC4-stroomcijfer

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>


In dit hoofdstuk bespreken we de details van een encryptieschema met een modern primitief streamcijfer, RC4 (of "Rivest cipher 4"), en een modern blokcijfer, AES. Terwijl het RC4 cijfer in onbruik is geraakt als versleutelingsmethode, is AES de standaard voor moderne symmetrische versleuteling. Deze twee voorbeelden geven een beter idee van hoe symmetrische encryptie onder de motorkap werkt.


___


Om een idee te krijgen van hoe moderne pseudorandom stream ciphers werken, zal ik me richten op het RC4 stream cipher. Het is een pseudorandom streamcijfer dat gebruikt werd in de WEP en WAP beveiligingsprotocollen voor draadloze toegangspunten en in TLS. Omdat RC4 veel bewezen zwakheden heeft, is het in ongenade gevallen. De Internet Engineering Task Force verbiedt nu zelfs het gebruik van RC4 suites door client en server applicaties in alle gevallen van TLS. Desondanks werkt het goed als voorbeeld om te illustreren hoe een primitief streamcijfer werkt.


Om te beginnen zal ik eerst laten zien hoe je een klaartekst bericht kunt versleutelen met een baby RC4 cijfer. Stel dat ons bericht "SOUP" is De versleuteling met ons RC4 baby versleutelingsprogramma verloopt dan in vier stappen.


### Stap 1


Definieer eerst een array **S** met $S[0] = 0$ tot $S[7] = 7$. Een array betekent hier eenvoudigweg een veranderlijke verzameling van waarden georganiseerd door een index, ook wel een lijst genoemd in sommige programmeertalen (bijvoorbeeld Python). In dit geval loopt de index van 0 tot en met 7, en de waarden lopen ook van 0 tot en met 7. Dus **S** is als volgt:



- $S = [0, 1, 2, 3, 4, 5, 6, 7]$


De waarden hier zijn geen ASCII-nummers, maar de decimale waardevoorstellingen van 1-byte strings. De waarde 2 zou dus gelijk zijn aan $0000 \ 0011$. De lengte van array **S** is dus 8 bytes.


### Stap 2


Ten tweede definieer je een sleutelarray **K** met een lengte van 8 bytes door een sleutel te kiezen tussen 1 en 8 bytes (geen fracties van bytes toegestaan). Aangezien elke byte 8 bits is, kunt u elk getal tussen 0 en 255 kiezen voor elke byte van uw sleutel.


Stel dat we onze sleutel **k** kiezen als $[14, 48, 9]$, zodat deze een lengte heeft van 3 bytes. Elke index van onze sleutelarray wordt dan ingesteld volgens de decimale waarde voor dat specifieke element van de sleutel, in volgorde. Als je de hele sleutel doorloopt, begin je weer bij het begin, totdat je alle 8 vakjes van de sleutelarray hebt gevuld. Onze sleutelarray ziet er dus als volgt uit:



- $K = [14, 48, 9, 14, 48, 9, 14, 48]$


### Stap 3


Ten derde transformeren we de array **S** met behulp van de sleutelarray **K**, in een proces dat bekend staat als **key scheduling**. Het proces ziet er in pseudocode als volgt uit:



- Maak variabelen **j** en **i** aan
- Stel de variabele $j = 0$ in
- Voor elke $i$ van 0 tot 7:
    - Stel $j = (j + S[i] + K[i]) √mod 8$
    - Verwissel $S[i]$ en $S[j]$


De transformatie van array **S** wordt weergegeven in *Tabel 1*.


Om te beginnen kun je de begintoestand van **S** zien als $[0, 1, 2, 3, 4, 5, 6, 7]$ met een beginwaarde van 0 voor **j**. Dit wordt getransformeerd met behulp van de sleutelarray $[14, 48, 9, 14, 48, 9, 14, 48]$.


De for-lus begint met $i = 0$. Volgens onze pseudocode hierboven wordt de nieuwe waarde van **j** 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Door het verwisselen van $S[0]$ en $S[6]$ wordt de toestand van **S** na 1 ronde $[6, 1, 2, 3, 4, 5, 0, 7]$.


In de volgende rij is $i = 1$. Door de for-lus opnieuw te doorlopen, krijgt **j** een waarde van 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Het verwisselen van $S[1]$ en $S[7]$ van de huidige staat van **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, levert $[6, 7, 2, 3, 4, 5, 0, 1]$ op na ronde 2.


We gaan door met dit proces totdat we de laatste rij onderaan hebben voor de matrix **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.



*Tabel 1: Belangrijke planningstabel*


| Round   | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Initial |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Stap 4


Als vierde stap produceren we de **keystream**. Dit is de pseudo-willekeurige string met een lengte die gelijk is aan het bericht dat we willen verzenden. Deze wordt gebruikt om het originele bericht "SOUP" te versleutelen Aangezien de keystream even lang moet zijn als het bericht, hebben we er een nodig van 4 bytes.


De keystream wordt geproduceerd door de volgende pseudocode:



- Maak de variabelen **j**, **i** en **t**.
- Stel $j = 0$ in.
- Voor elke $i$ van de platte tekst, te beginnen met $i = 1$ en doorlopend tot $i = 4$, wordt elke byte van de keystream als volgt geproduceerd:
    - $j = (j + S[i]) 8$
    - Verwissel $S[i]$ en $S[j]$.
    - $t = (S[i] + S[j]) mod 8$
    - De $i^{e}$ byte van de sleutelstroom = $S[t]$


Je kunt de berekeningen volgen in *Tabel 2*.


De begintoestand van **S** is $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Als we $i = 1$ instellen, wordt de waarde van **j** 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). We verwisselen dan $S[1]$ en $S[4]$ om de transformatie van **S** in de tweede rij te krijgen, $[6, 3, 1, 0, 4, 7, 5, 2]$. De waarde van **t** is dan 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Tenslotte is de byte voor de keystream $S[7]$, oftewel 2.


We gaan dan verder met het produceren van de andere bytes totdat we de volgende vier bytes hebben: 2, 6, 3 en 7. Elk van deze bytes kan dan worden gebruikt om elke letter van de klare tekst, "SOUP", te versleutelen.


Om te beginnen kunnen we met behulp van een ASCII-tabel zien dat "SOUP" gecodeerd door de decimale waarden van de onderliggende bytestrings "83 79 85 80" is. Combinatie met de keystream "2 6 3 7" levert "85 85 88 87" op, wat hetzelfde blijft na een modulo 256 bewerking. In ASCII is de cijfertekst "85 85 88 87" gelijk aan "UUXW".


Wat gebeurt er als het te versleutelen woord langer zou zijn dan de array **S**? In dat geval blijft de array **S** gewoon transformeren op de hierboven weergegeven manier voor elke byte **i** van de klaartekst, totdat we een aantal bytes in de keystream hebben dat gelijk is aan het aantal letters in de klaartekst.



*Tabel 2: Sleutelstroom generatie*


| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     |     |     |           |      |      |      |      |      |      |      |      |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |
| 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Het voorbeeld dat we zojuist hebben besproken is slechts een afgezwakte versie van het **RC4 stream cipher**. Het echte RC4 stream cipher heeft een **S** array van 256 bytes lang, niet 8 bytes, en een sleutel die tussen 1 en 256 bytes kan zijn, niet tussen 1 en 8 bytes. De sleutelarray en de keystreams worden dan allemaal geproduceerd rekening houdend met de 256 bytes lengte van de **S** array. De berekeningen worden enorm complexer, maar de principes blijven hetzelfde. Met dezelfde sleutel, [14,48,9], en het standaard RC4-cijfer wordt de klaartekst "SOUP" versleuteld als 67 02 ed df in hexadecimaal formaat.


Een streamcipher waarbij de keystream onafhankelijk van het bericht of de cijfertekst wordt bijgewerkt is een **synchroon streamcipher**. De sleutelstroom is alleen afhankelijk van de sleutel. RC4 is duidelijk een voorbeeld van een synchroon streamcijfer, aangezien de keystream geen relatie heeft met de klaartekst of cijfertekst. Al onze primitieve stroomcijfers uit het vorige hoofdstuk, waaronder het shift cijfer, het Vigenère cijfer en het one-time pad, waren ook synchroon.


Een **asynchroon streamcijfer** heeft daarentegen een keystream die geproduceerd wordt door zowel de sleutel als de vorige Elements van de cijfertekst. Dit type cijfer wordt ook wel een **zelf-synchroniserend cijfer** genoemd.


Belangrijk is dat de keystream die geproduceerd wordt met RC4 behandeld moet worden als een one-time pad, en je kunt de keystream de volgende keer niet op precies dezelfde manier produceren. In plaats van de sleutel elke keer te veranderen, is de praktische oplossing om de sleutel te combineren met een **Nonce** om de bytestream te produceren.




## AES met een 128-bits sleutel

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>


Zoals vermeld in het vorige hoofdstuk, hield het National Institute of Standards and Technology (NIST) tussen 1997 en 2000 een wedstrijd om een nieuwe symmetrische encryptiestandaard te bepalen. Het **Rijndael cijfer** bleek de winnende inzending te zijn. De naam is een woordspeling op de namen van de Belgische makers, Vincent Rijmen en Joan Daemen.


Het Rijndael-cijfer is een **blokcijfer**, wat betekent dat er een kernalgoritme is dat kan worden gebruikt met verschillende specificaties voor sleutellengtes en blokgroottes. U kunt het dus met verschillende werkwijzen gebruiken om versleutelingsschema's te construeren.


Het comité voor de NIST-competitie heeft een beperkte versie van het Rijndael-cijfer aangenomen - namelijk een versie die blokgroottes van 128 bits en sleutellengtes van 128 bits, 192 bits of 256 bits vereist - als onderdeel van de **Advanced Encryption Standard (AES)**. Deze beperkte versie van het Rijndael-cijfer kan ook worden gebruikt onder meerdere werkingsmodi. De specificatie voor de standaard staat bekend als de **Advanced Encryption Standard (AES)**.


Om te laten zien hoe het Rijndael-cijfer werkt, de kern van AES, zal ik het proces illustreren voor vercijfering met een 128-bits sleutel. De sleutelgrootte heeft invloed op het aantal versleutelingsronden voor elk blok. Voor sleutels van 128 bits zijn 10 rondes nodig. Met 192 bits en 256 bits zouden dat respectievelijk 12 en 14 rondes zijn.


Daarnaast zal ik aannemen dat AES wordt gebruikt in **ECB-mode**. Dit maakt de uiteenzetting iets eenvoudiger en maakt niet uit voor het Rijndael algoritme. ECB mode is in de praktijk niet veilig omdat het leidt tot deterministische encryptie. De meest gebruikte veilige modus met AES is **CBC** (Cipher Block Chaining).


Laten we de sleutel $K_0$ noemen. De constructie met bovenstaande parameters ziet er dan uit als in *Figuur 1*, waarbij $M_i$ staat voor een deel van de klaartekst van 128 bits en $C_i$ voor een deel van de cijfertekst van 128 bits. Padding wordt toegevoegd aan de klaartekst voor het laatste blok, als de klaartekst niet gelijkmatig kan worden gedeeld door de blokgrootte.



*Figuur 1: AES-ECB met een 128-bits sleutel*


![Figure 1: AES-ECB with a 128-bit key](assets/Figure5-1.webp "Figure 1: AES-ECB with a 128-bit key")


Elk 128-bits tekstblok doorloopt tien rondes in het Rijndael versleutelingsschema. Dit vereist een aparte rondesleutel voor elke ronde ($K_1$ tot $K_{10}$). Deze worden voor elke ronde gemaakt van de originele 128-bits sleutel $K_0$ met behulp van een **sleuteluitbreidingsalgoritme**. Voor elk blok tekst dat moet worden versleuteld, gebruiken we dus de oorspronkelijke sleutel $K_0$ en tien afzonderlijke rondesleutels. Merk op dat dezelfde 11 sleutels worden gebruikt voor elk blok platte tekst van 128 bits dat moet worden versleuteld.


Het sleuteluitbreidingsalgoritme is lang en complex. Het doornemen ervan heeft weinig didactisch nut. U kunt het sleuteluitbreidingsalgoritme zelf doornemen als u dat wilt. Zodra de ronde sleutels zijn gemaakt, manipuleert het Rijndael-cijfer het eerste 128-bits blok platte tekst, $M_1$, zoals te zien is in *Figuur 2*. We zullen nu deze stappen doorlopen.


*Figuur 2: De manipulatie van $M_1$ met het Rijndael-cijfer:*


**Ronde 0:**


- XOR $M_1$ en $K_0$ om $S_0$ te produceren


---

**Rond n voor n = {1,...,9}:**


- XOR $S_{n-1}$ en $K_n$
- Byte Substitutie
- Rijen verschuiven
- Kolommen mengen
- XOR $S$ en $K_n$ om $S_n$ te produceren


---

**Ronde 10:**


- XOR $S_9$ en $K_{10}$
- Byte Substitutie
- Rijen verschuiven
- XOR $S$ en $K_{10}$ om $S_{10}$ te produceren
- $S_{10}$ = $C_1$



### Ronde 0


Ronde 0 van het Rijndael-cijfer is eenvoudig. Een matrix $S_0$ wordt geproduceerd door een XOR-bewerking tussen de 128-bits klaartekst en de privésleutel. Dat wil zeggen,



- $S_0 = M_1 ≥ K_0$


### Ronde 1


In ronde 1 wordt de array $S_0$ eerst gecombineerd met de ronde sleutel $K_1$ door middel van een XOR operatie. Dit levert een nieuwe toestand $S$ op.


Ten tweede wordt de **byte substitutie** uitgevoerd op de huidige status van $S$. Het werkt door elke byte van de 16-byte $S$ array te nemen en deze te vervangen door een byte van een array genaamd **Rijndael's S-box**. Elke byte heeft een unieke transformatie en als resultaat wordt een nieuwe toestand van $S$ geproduceerd. Rijndael's S-box wordt weergegeven in *Figuur 3*.


*Afbeelding 3: De S-Box van Rijndael*


|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
| 50  | 53  | D1  | 00  | ED  | 20  | FC  | B1  | 5B  | 6A  | CB  | BE  | 39  | 4A  | 4C  | 58  | CF  |
| 60  | D0  | EF  | AA  | FB  | 43  | 4D  | 33  | 85  | 45  | F9  | 02  | 7F  | 50  | 3C  | 9F  | A8  |
| 70  | 51  | A3  | 40  | 8F  | 92  | 9D  | 38  | F5  | BC  | B6  | DA  | 21  | 10  | FF  | F3  | D2  |
| 80  | CD  | 0C  | 13  | EC  | 5F  | 97  | 44  | 17  | C4  | A7  | 7E  | 3D  | 64  | 5D  | 19  | 73  |
| 90  | 60  | 81  | 4F  | DC  | 22  | 2A  | 90  | 88  | 46  | EE  | B8  | 14  | DE  | 5E  | 0B  | DB  |
| A0  | E0  | 32  | 3A  | 0A  | 49  | 06  | 24  | 5C  | C2  | D3  | AC  | 62  | 91  | 95  | E4  | 79  |
| B0  | E7  | C8  | 37  | 6D  | 8D  | D5  | 4E  | A9  | 6C  | 56  | F4  | EA  | 65  | 7A  | AE  | 08  |
| C0  | BA  | 78  | 25  | 2E  | 1C  | A6  | B4  | C6  | E8  | DD  | 74  | 1F  | 4B  | BD  | 8B  | 8A  |
| D0  | 70  | 3E  | B5  | 66  | 48  | 03  | F6  | 0E  | 61  | 35  | 57  | B9  | 86  | C1  | 1D  | 9E  |
| E0  | E1  | F8  | 98  | 11  | 69  | D9  | 8E  | 94  | 9B  | 1E  | 87  | E9  | CE  | 55  | 28  | DF  |
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |


Deze S-Box is één plaats waar abstracte algebra een rol speelt in het Rijndael cijfer, specifiek **Galois velden**.


Om te beginnen definieer je elk mogelijk byte-element 00 tot en met FF als een 8-bits vector. Elk van die vectoren is een element van het **Galoisveld GF(2^8)** waar de onherleidbare polynoom voor de modulo-operatie $x^8 + x^4 + x^3 + x + 1$ is. Het Galoisveld met deze specificaties wordt ook wel **Rijndael's Eindige Veld** genoemd.


Vervolgens maken we voor elk mogelijk element in het veld een zogenaamde **Nyberg S-Box**. In deze box wordt elke byte gekoppeld aan zijn **multiplicatieve inverse** (zodat het product gelijk is aan 1). Vervolgens brengen we deze waarden van de Nyberg S-Box over naar de S-Box van Rijndael met behulp van de **affiene transformatie**.


De derde bewerking op de **S** array is de **shift rows** bewerking. Deze neemt de status van **S** en zet alle zestien bytes in een matrix. Het vullen van de matrix begint linksboven en werkt rond door van boven naar beneden te gaan en dan, elke keer als een kolom gevuld is, een kolom naar rechts en naar boven te verschuiven.


Zodra de matrix van **S** geconstrueerd is, worden de vier rijen verschoven. De eerste rij blijft hetzelfde. De tweede rij schuift één naar links. De derde rij schuift twee naar links. De vierde verschuift er drie naar links. Een voorbeeld van dit proces wordt gegeven in *Figuur 4*. De oorspronkelijke toestand van **S** wordt bovenaan getoond, en de resulterende toestand na de shift rijen operatie wordt eronder getoond.


*Afbeelding 4: Verplaatsing van rijen*


| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |
| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


In de vierde stap verschijnen de **Galois-velden** weer. Om te beginnen wordt elke kolom van de **S** matrix vermenigvuldigd met de kolom van de 4 x 4 matrix uit *Figuur 5*. Maar in plaats van een gewone matrixvermenigvuldiging is het een vectorvermenigvuldiging **modulo een irreducibele polynoom**, $x^8 + x^4 + x^3 + x + 1$. De resulterende vectorcoëfficiënten vertegenwoordigen de individuele bits van een byte.


*Afbeelding 5: Matrix mixkolommen*


| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   |
| 03   | 01   | 01   | 02   |

Vermenigvuldiging van de eerste kolom van de **S** matrix met de bovenstaande 4 x 4 matrix geeft het resultaat in *Figuur 6*.


*Figuur 6: Vermenigvuldiging van de eerste kolom:*


$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$


Als volgende stap moeten alle termen in de matrix worden omgezet in veeltermen. Bijvoorbeeld, F1 vertegenwoordigt 1 byte en wordt $x^7 + x^6 + x^5 + x^4 + 1$, en 03 vertegenwoordigt 1 byte en wordt $x + 1$.


Alle vermenigvuldigingen worden dan **modulo** $x^8 + x^4 + x^3 + x + 1$ uitgevoerd. Dit resulteert in de optelling van vier veeltermen in elk van de vier cellen van de kolom. Na het uitvoeren van deze optellingen **modulo 2**, krijg je vier veeltermen. Elk van deze veeltermen vertegenwoordigt een 8-bits string, of 1 byte, van **S**. We zullen hier niet al deze berekeningen uitvoeren op de matrix in *Figuur 6*, omdat ze veelomvattend zijn.


Zodra de eerste kolom verwerkt is, worden de andere drie kolommen van de **S** matrix op dezelfde manier verwerkt. Uiteindelijk levert dit een matrix op met zestien bytes die kan worden omgezet in een array.


Als laatste stap wordt de matrix **S** opnieuw gecombineerd met de ronde sleutel in een **XOR** operatie. Dit levert de toestand $S_1$ op. Dat wil zeggen,



- $S_1 = S \oplus K_0$


### Ronde 2 tot en met 10


Rondes 2 tot en met 9 zijn gewoon een herhaling van ronde 1, *mutatis mutandis*. De laatste ronde lijkt erg op de vorige rondes, behalve dat de stap **kolommen mengen** is geëlimineerd. Dat wil zeggen, ronde 10 wordt als volgt uitgevoerd:



- $S_9 \oplus K_{10}$
- Byte Substitutie
- Rijen verschuiven
- $S_{10} = S Soplus K_{10}$


De toestand $S_{10}$ is nu ingesteld op $C_1$, de eerste 128 bits van de cijfertekst. Doorgaan met de resterende blokken van 128 bits levert de volledige cijfertekst **C** op.


### De bewerkingen van het Rijndael-cijfer


Wat is de redenering achter de verschillende operaties in het Rijndael-cijfer?


Zonder in details te treden, worden versleutelingsschema's beoordeeld op basis van de mate waarin ze verwarring en verspreiding creëren. Als het encryptiesysteem een hoge mate van **verwarring** heeft, betekent dit dat de cijfertekst er drastisch anders uitziet dan de klare tekst. Als het versleutelingsschema een hoge mate van **verwarring** heeft, betekent dit dat elke kleine verandering aan de klaartekst een drastisch andere cijfertekst oplevert.


De redenering achter de operaties achter het Rijndael cijfer is dat ze zowel een hoge mate van verwarring als diffusie produceren. De verwarring wordt veroorzaakt door de Byte substitutie operatie, terwijl de diffusie wordt veroorzaakt door de shift rijen en mix kolommen operaties.


# Asymmetrische cryptografie

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>



## Het distributie- en beheerprobleem van sleutels

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>


Net als bij symmetrische cryptografie kunnen asymmetrische schema's worden gebruikt om zowel geheimhouding als authenticatie te garanderen. Deze schema's gebruiken echter twee sleutels in plaats van één: een private en een publieke sleutel.


We beginnen ons onderzoek met de ontdekking van asymmetrische cryptografie, in het bijzonder de problemen die de aanleiding waren. Vervolgens bespreken we hoe asymmetrische schema's voor vercijfering en authenticatie op een hoog niveau werken. Daarna introduceren we Hash functies, die de sleutel zijn tot het begrijpen van asymmetrische authenticatieschema's en ook relevant zijn in andere cryptografische contexten, zoals voor de Hash-gebaseerde berichtauthenticatiecodes die we bespraken in Hoofdstuk 4.


___



Stel dat Bob een nieuwe regenjas wil kopen bij Jim's Sporting Goods, een online sportartikelenwinkel met miljoenen klanten in Noord-Amerika. Dit wordt zijn eerste aankoop en hij wil zijn creditcard gebruiken. Bob moet dus eerst een account aanmaken bij Jim's Sporting Goods, waarvoor hij persoonlijke gegevens zoals zijn Address en creditcardgegevens moet opsturen. Daarna kan hij de stappen doorlopen die nodig zijn om de regenjas te kopen.


Bob en Jim's Sporting Goods zullen ervoor willen zorgen dat hun communicatie tijdens dit proces veilig is, aangezien het internet een open communicatiesysteem is. Ze zullen er bijvoorbeeld voor willen zorgen dat geen enkele potentiële aanvaller Bob's creditcard- en Address-gegevens kan achterhalen en dat geen enkele potentiële aanvaller zijn aankopen kan herhalen of nepaankopen in zijn naam kan doen.


Een geavanceerd geauthenticeerd encryptieschema zoals besproken in het vorige hoofdstuk zou de communicatie tussen Bob en Jim's Sporting Goods zeker veilig kunnen maken. Maar er zijn duidelijk praktische obstakels om zo'n schema te implementeren.


Om deze praktische obstakels te illustreren, stel dat we in een wereld leefden waarin alleen de instrumenten van symmetrische cryptografie bestonden. Wat zouden Jim's Sporting Goods en Bob dan kunnen doen om veilige communicatie te garanderen?


Onder die omstandigheden zouden ze te maken krijgen met aanzienlijke kosten om veilig te communiceren. Aangezien het internet een open communicatiesysteem is, kunnen ze niet zomaar Exchange een set sleutels via het internet maken. Daarom moeten Bob en een vertegenwoordiger van Jim's Sporting Goods persoonlijk een Exchange sleutel maken.


Eén mogelijkheid is dat Jim's Sporting Goods speciale Exchange-sleutellocaties creëert, waar Bob en andere nieuwe klanten een set sleutels kunnen ophalen voor beveiligde communicatie. Dit zou uiteraard aanzienlijke organisatorische kosten met zich meebrengen en de efficiëntie waarmee nieuwe klanten aankopen kunnen doen sterk verminderen.


Als alternatief kan Jim's Sporting Goods Bob een paar sleutels opsturen met een zeer vertrouwde koerier. Dit is waarschijnlijk efficiënter dan het organiseren van Exchange sleutellocaties. Maar dit zou nog steeds aanzienlijke kosten met zich meebrengen, vooral als veel klanten slechts één of enkele aankopen doen.


Vervolgens dwingt een symmetrisch schema voor geauthenticeerde encryptie Jim's Sporting Goods ook om verschillende sets sleutels op te slaan voor al hun klanten. Dit zou een grote praktische uitdaging zijn voor duizenden klanten, laat staan miljoenen.


Om dit laatste punt te begrijpen, stel dat Jim's Sporting Goods elke klant hetzelfde sleutelpaar geeft. Hierdoor zou elke klant - of iemand anders die dit sleutelpaar zou kunnen bemachtigen - alle communicatie tussen Jim's Sporting Goods en zijn klanten kunnen lezen en zelfs manipuleren. Je kunt dan net zo goed helemaal geen cryptografie gebruiken in je communicatie.


Zelfs het herhalen van een set sleutels voor slechts enkele klanten is een verschrikkelijke veiligheidspraktijk. Elke potentiële aanvaller zou kunnen proberen om die eigenschap van het systeem te misbruiken (vergeet niet dat aanvallers verondersteld worden alles te weten over een systeem behalve de sleutels, in overeenstemming met het principe van Kerckhoffs)


Jim's Sporting Goods zou dus voor elke klant een sleutelpaar moeten opslaan, ongeacht hoe deze sleutelparen worden verdeeld. Dit levert duidelijk verschillende praktische problemen op.



- Jim's Sporting Goods zou miljoenen sleutelparen moeten opslaan, één set voor elke klant.
- Deze sleutels zouden goed beveiligd moeten worden, omdat ze een zeker doelwit voor hackers zouden zijn. Elke inbreuk op de beveiliging zou een kostbare sleuteluitwisseling vereisen, hetzij op speciale Exchange locaties of per koerier.
- Elke klant van Jim's Sporting Goods zou thuis een paar sleutels veilig moeten opbergen. Verliezen en diefstallen komen voor, waardoor de sleutels steeds opnieuw moeten worden uitgewisseld. Klanten zouden dit proces ook moeten doorlopen voor andere online winkels of andere entiteiten waarmee ze willen communiceren en transacties doen via het internet.


Deze twee zojuist beschreven uitdagingen waren tot het einde van de jaren 1970 zeer fundamentele zorgen. Ze stonden bekend als respectievelijk het **sleuteldistributieprobleem** en het **sleutelbeheerprobleem**.


Deze problemen hebben natuurlijk altijd bestaan en zorgden in het verleden vaak voor hoofdpijn. Militairen moesten bijvoorbeeld voortdurend en tegen hoge risico's en kosten boeken met sleutels voor beveiligde communicatie uitdelen aan personeel in het veld. Maar deze problemen werden erger naarmate de wereld steeds meer overging op digitale communicatie over lange afstanden, vooral voor niet-gouvernementele entiteiten.


Als deze problemen in de jaren 1970 niet waren opgelost, zou efficiënt en veilig winkelen bij Jim's Sporting Goods waarschijnlijk niet hebben bestaan. In feite zou het grootste deel van onze moderne wereld met praktisch en veilig e-mailen, online bankieren en winkelen waarschijnlijk slechts een verre fantasie zijn. Alles wat ook maar lijkt op Bitcoin zou helemaal niet hebben bestaan.


Wat gebeurde er in de jaren 1970? Hoe is het mogelijk dat we direct online aankopen kunnen doen en veilig op het World Wide Web kunnen surfen? Hoe is het mogelijk dat we onmiddellijk Bitcoins over de hele wereld kunnen versturen vanaf onze smartphones?



## Nieuwe richtingen in cryptografie

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>


Tegen de jaren 1970 hadden de problemen van sleuteldistributie en sleutelbeheer de aandacht getrokken van een groep Amerikaanse academische cryptografen: Whitfield Diffie, Martin Hellman en Ralph Merkle. Ondanks de ernstige scepsis van de meerderheid van hun collega's, waagden ze het om er een oplossing voor te bedenken.


Een van de belangrijkste drijfveren voor hun onderneming was de vooruitziende blik dat open computercommunicatie onze wereld ingrijpend zou beïnvloeden. Zoals Diffie en Helmann in 1976 opmerkten,


> De ontwikkeling van computergestuurde communicatienetwerken belooft moeiteloos en goedkoop contact tussen mensen of computers aan weerszijden van de wereld, waardoor de meeste post en veel uitstapjes vervangen worden door telecommunicatie. Voor veel toepassingen moeten deze contacten beveiligd worden tegen zowel afluisteren als het inbrengen van onwettige berichten. Op dit moment loopt de oplossing van beveiligingsproblemen echter ver achter op andere gebieden van communicatietechnologie. *De huidige cryptografie is niet in staat om aan de eisen te voldoen, in die zin dat het gebruik ervan zulke ernstige ongemakken voor de gebruikers van het systeem met zich mee zou brengen, dat veel van de voordelen van teleprocessing zouden verdwijnen.* [1]

De vasthoudendheid van Diffie, Hellman en Merkle wierp zijn vruchten af. De eerste publicatie van hun resultaten was een artikel van Diffie en Helmann in 1976 getiteld "New Directions in Cryptography" Hierin presenteerden ze twee originele manieren om Address de sleuteldistributie en sleutelbeheer problemen op te lossen.


De eerste oplossing die ze aanboden was een *key-Exchange protocol* op afstand, dat wil zeggen een set regels voor de Exchange van één of meer symmetrische sleutels over een onveilig communicatiekanaal. Dit protocol staat nu bekend als *Diffie-Helmann sleutel Exchange* of *Diffie-Helmann-Merkle sleutel Exchange*. [2]


Met de Diffie-Helmann sleutel Exchange geven twee partijen eerst Exchange informatie vrij op een onveilig kanaal zoals het Internet. Op basis van die informatie maken ze vervolgens onafhankelijk van elkaar een symmetrische sleutel (of een paar symmetrische sleutels) voor veilige communicatie. Hoewel beide partijen hun sleutels onafhankelijk aanmaken, zorgt de informatie die ze publiekelijk hebben gedeeld ervoor dat dit sleutelaanmaakproces voor beiden hetzelfde resultaat oplevert.


Belangrijk is dat, terwijl iedereen de informatie kan waarnemen die publiekelijk wordt uitgewisseld door de partijen via het onveilige kanaal, alleen de twee partijen die betrokken zijn bij de informatie Exchange er symmetrische sleutels van kunnen maken.


Dit klinkt natuurlijk volledig contra-intuïtief. Hoe kunnen twee partijen Exchange informatie openbaar maken waardoor alleen zij symmetrische sleutels kunnen maken? Waarom zou iemand anders die de informatie Exchange observeert niet in staat zijn om dezelfde sleutels te maken?


Het berust natuurlijk op prachtige wiskunde. De Diffie-Helmann sleutel Exchange werkt via een eenrichtingsfunctie met een valluik. Laten we achtereenvolgens de betekenis van deze twee termen bespreken.


Stel dat je een functie $f(x)$ krijgt en het resultaat $f(a) = y$, waarbij $a$ een bepaalde waarde voor $x$ is. We zeggen dat $f(x)$ een **eenrichtingsfunctie** is als het gemakkelijk is om de waarde $y$ te berekenen wanneer $a$ en $f(x)$ gegeven zijn, maar het rekenkundig niet mogelijk is om de waarde $a$ te berekenen wanneer $y$ en $f(x)$ gegeven zijn. De naam **eenrichtingsfunctie** komt natuurlijk van het feit dat het praktisch is om zo'n functie maar in één richting te berekenen.


Sommige eenrichtingsfuncties hebben een zogenaamde **trapdoor**. Hoewel het praktisch onmogelijk is om $a$ te berekenen met alleen $y$ en $f(x)$, is er een bepaald stukje informatie $Z$ dat het berekenen van $a$ uit $y$ berekenbaar maakt. Dit stukje informatie $Z$ staat bekend als de **trapdoor**. Eenrichtingsfuncties met een valluik worden **valluikfuncties** genoemd.


We zullen hier niet in detail treden over de Diffie-Helmann sleutel Exchange. Maar in essentie creëert elke deelnemer wat informatie, waarvan een deel publiekelijk wordt gedeeld en een deel geheim blijft. Elke partij gebruikt vervolgens zijn geheime stukje informatie en de openbare informatie die door de andere partij is gedeeld om een privésleutel te maken. En wonder boven wonder hebben beide partijen uiteindelijk dezelfde privésleutel.


Elke partij die alleen de publiekelijk gedeelde informatie tussen de twee partijen in een Diffie Helmann sleutel Exchange bekijkt, kan deze berekeningen niet repliceren. Ze zouden daarvoor de privé-informatie van één van de twee partijen nodig hebben.


Hoewel de basisversie van Diffie-Helmann sleutel Exchange, gepresenteerd in de paper uit 1976, niet erg veilig is, worden geavanceerde versies van het basisprotocol vandaag de dag nog steeds gebruikt. Het belangrijkste is dat elk Exchange sleutelprotocol in de laatste versie van het transport Layer beveiligingsprotocol (versie 1.3) in wezen een verrijkte versie is van het protocol dat in 1976 door Diffie en Hellman werd gepresenteerd. Het transport Layer beveiligingsprotocol is het belangrijkste protocol voor het veilig uitwisselen van informatie geformatteerd volgens het hypertext transfer protocol (http), de standaard voor het uitwisselen van webinhoud.


Belangrijk is dat de Diffie-Helmann sleutel Exchange geen asymmetrisch schema is. Strikt genomen behoort het tot het domein van de symmetrische cryptografie. Maar omdat zowel de Diffie-Helmann sleutel Exchange als asymmetrische cryptografie gebaseerd zijn op eenrichtingsgetaltheoretische functies met valdeuren, worden ze meestal samen besproken.


De tweede manier die Diffie en Helmann aanboden om Address het sleuteldistributie- en beheerprobleem op te lossen in hun paper uit 1976 was natuurlijk via asymmetrische cryptografie.


In tegenstelling tot hun presentatie van de Diffie-Hellman sleutel Exchange, gaven ze alleen de algemene contouren van hoe asymmetrische cryptografische schema's aannemelijk gemaakt zouden kunnen worden. Ze boden geen enkele eenrichtingsfunctie die specifiek zou voldoen aan de voorwaarden die nodig zijn voor redelijke veiligheid in dergelijke schema's.


Een praktische implementatie van een asymmetrisch schema werd echter een jaar later gevonden door drie verschillende academische cryptografen en wiskundigen: Ronald Rivest, Adi Shamir en Leonard Adleman. [3] Het cryptosysteem dat ze introduceerden werd bekend als het **RSA cryptosysteem** (naar hun achternamen).


De trapdoor functies die gebruikt worden in asymmetrische cryptografie (en Diffie Helmann sleutel Exchange) zijn allemaal gerelateerd aan twee belangrijke **computationeel Hard problemen**: priemfactorisatie en de berekening van discrete logaritmen.


**Prime factorization** vereist, zoals de naam al zegt, het opsplitsen van een geheel getal in zijn priemfactoren. Het RSA probleem is veruit het bekendste voorbeeld van een cryptosysteem gerelateerd aan priemfactorisatie.


Het **discrete logaritme probleem** is een probleem dat voorkomt in cyclische groepen. Gegeven een generator in een bepaalde cyclische groep, moet de unieke exponent berekend worden die nodig is om uit de generator een ander element in de groep te produceren.


Schema's op basis van discrete logaritmen zijn gebaseerd op twee belangrijke soorten cyclische groepen: vermenigvuldigingsgroepen van gehele getallen en groepen die de punten op elliptische krommen bevatten. De originele Diffie Helmann-sleutel Exchange zoals gepresenteerd in "New Directions in Cryptography" werkt met een cyclische vermenigvuldigingsgroep van gehele getallen. Het digitale handtekeningalgoritme van Bitcoin en het recent geïntroduceerde Schnorr-handtekeningenschema (2021) zijn beide gebaseerd op het discrete logaritmeprobleem voor een bepaalde cyclische groep van elliptische krommen.


Vervolgens zullen we een overzicht geven van geheimhouding en authenticatie in de asymmetrische omgeving. Voordat we dat doen, moeten we echter een korte historische opmerking maken.


Het lijkt nu aannemelijk dat een groep Britse cryptografen en wiskundigen die voor het Government Communications Headquarters (GCHQ) werkten een paar jaar eerder onafhankelijk van elkaar de bovengenoemde ontdekkingen hadden gedaan. Deze groep bestond uit James Ellis, Clifford Cocks en Malcolm Williamson.


Volgens hun eigen verklaringen en die van GCHQ was het James Ellis die in 1969 als eerste het concept van public key cryptografie bedacht. Vervolgens ontdekte Clifford Cocks het RSA cryptografisch systeem in 1973 en Malcolm Williamson het concept van de Diffie Helmann sleutel Exchange in 1974. [4] Hun ontdekkingen werden echter naar verluidt pas in 1997 onthuld, gezien de geheime aard van het werk bij GCHQ.



**Noten:**


[1] Whitfield Diffie en Martin Hellman, "New directions in cryptography," _IEEE Transactions on Information Theory_ IT-22 (1976), pp. 644-654, op p. 644.


[2] Ralph Merkle bespreekt ook een belangrijk Exchange protocol in "Secure communications over insecure channels", _Communications of the Association for Computing Machinery_, 21 (1978), 294-99. Hoewel Merkle dit paper eigenlijk voor het paper van Diffie en Hellman indiende, werd het later gepubliceerd. Hoewel Merkle dit artikel eerder indiende dan het artikel van Diffie en Hellman, werd het later gepubliceerd. Merkle's oplossing is niet exponentieel veilig, in tegenstelling tot die van Diffie-Hellman.


[3] Ron Rivest, Adi Shamir, en Leonard Adleman, "A method for obtaining digital signatures and public-key cryptosystems", _Communications of the Association for Computing Machinery_, 21 (1978), pp. 120-26.


[4] Een goede geschiedenis van deze ontdekkingen wordt gegeven door Simon Singh, _The Code Book_, Fourth Estate (Londen, 1999), Hoofdstuk 6.





## Asymmetrische encryptie en authenticatie

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>


Een overzicht van **asymmetrische encryptie** met behulp van Bob en Alice wordt gegeven in *Figuur 1*.


Alice maakt eerst een sleutelpaar aan, bestaande uit een publieke sleutel ($K_P$) en een privésleutel ($K_S$), waarbij de "P" in $K_P$ staat voor "publiek" en de "S" in $K_S$ voor "geheim". Vervolgens verspreidt ze deze openbare sleutel vrij onder anderen. We zullen later terugkomen op de details van dit distributieproces. Maar voor nu, neem aan dat iedereen, inclusief Bob, veilig de publieke sleutel $K_P$ van Alice kan verkrijgen.


Op een later tijdstip wil Bob een bericht $M$ aan Alice schrijven. Omdat het gevoelige informatie bevat, wil hij dat de inhoud geheim blijft voor iedereen behalve Alice. Dus versleutelt Bob eerst zijn bericht $M$ met $K_P$. Vervolgens stuurt hij de resulterende cijfertekst $C$ naar Alice, die $C$ decodeert met $K_S$ om het oorspronkelijke bericht $M$ te produceren.


*Afbeelding 1: Asymmetrische codering*


![Figure 1: Asymmetric encryption](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")



Elke tegenstander die meeluistert met de communicatie van Bob en Alice kan $C$ observeren. Ze kent ook $K_P$ en het versleutelingsalgoritme $E(\cdot)$. Belangrijk is echter dat de aanvaller met deze informatie de cijfertekst $C$ niet kan ontcijferen. Voor ontcijfering is namelijk $K_S$ nodig, die de aanvaller niet bezit.


Symmetrische versleutelingsschema's moeten over het algemeen beveiligd zijn tegen een aanvaller die geldige klaartekstberichten kan versleutelen (bekend als beveiliging tegen "chosen-ciphertext attack"). Het is echter niet ontworpen met het expliciete doel om het creëren van zulke geldige cijferteksten door een aanvaller of iemand anders toe te staan.


Dit staat in schril contrast met een asymmetrisch encryptiesysteem, waarbij het de bedoeling is dat iedereen, inclusief aanvallers, geldige cijferteksten kan maken. Asymmetrische versleutelingssystemen kunnen daarom worden bestempeld als **meervoudige toegangssleutels**.


Om beter te begrijpen wat er gebeurt, stel je voor dat Bob in plaats van een bericht elektronisch te versturen, een fysieke brief in het geheim wilde versturen. Een manier om geheimhouding te garanderen, zou zijn dat Alice een beveiligd hangslot naar Bob stuurt, maar de sleutel om het te ontgrendelen zelf bewaart. Na het schrijven van zijn brief kon Bob de brief in een doos doen en deze afsluiten met Alice's hangslot. Vervolgens kan hij de afgesloten doos met het bericht naar Alice sturen, die de sleutel heeft om het slot te openen.


Hoewel Bob het hangslot kan vergrendelen, kan noch hij, noch iemand anders die de doos onderschept, het hangslot ongedaan maken als het inderdaad beveiligd is. Alleen Alice kan het ontgrendelen en de inhoud van Bob's brief zien, omdat zij de sleutel heeft.


Een asymmetrisch versleutelingsschema is grofweg een digitale versie van dit proces. Het hangslot is vergelijkbaar met de publieke sleutel en de hangslotsleutel is vergelijkbaar met de privésleutel. Omdat het hangslot echter digitaal is, is het voor Alice veel gemakkelijker en niet zo duur om het te verspreiden onder iedereen die geheime berichten naar haar zou willen sturen.


Voor authenticatie in de asymmetrische setting gebruiken we **digitale handtekeningen**. Deze hebben dus dezelfde functie als berichtauthenticatiecodes in de symmetrische omgeving. Een overzicht van digitale handtekeningen wordt gegeven in *Figuur 2*.


Bob maakt eerst een sleutelpaar aan, bestaande uit de publieke sleutel ($K_P$) en de private sleutel ($K_S$), en verdeelt zijn publieke sleutel. Wanneer hij een geauthenticeerd bericht naar Alice wil sturen, neemt hij eerst zijn bericht $M$ en zijn private sleutel om een **digitale handtekening** $D$ te maken. Bob stuurt Alice dan zijn bericht samen met de digitale handtekening.


Alice voegt het bericht, de openbare sleutel en de digitale handtekening in een **verificatiealgoritme** in. Dit algoritme produceert ofwel **waar** voor een geldige handtekening, of **onwaar** voor een ongeldige handtekening.


Een digitale handtekening is, zoals de naam duidelijk aangeeft, het digitale equivalent van een geschreven handtekening op brieven, contracten, enzovoort. In feite is een digitale handtekening meestal veel veiliger. Met enige moeite kun je een geschreven handtekening vervalsen; een proces dat gemakkelijker wordt gemaakt door het feit dat geschreven handtekeningen vaak niet nauwkeurig worden gecontroleerd. Een veilige digitale handtekening is echter, net als een veilige berichtauthenticatiecode, **existentieel niet te vervalsen**: dat wil zeggen, met een veilig digitaal handtekeningschema kan niemand een handtekening maken voor een bericht dat door de verificatieprocedure komt, tenzij ze de privésleutel hebben.


*Afbeelding 2: Asymmetrische authenticatie*


![Figure 2: Asymmetric authentication](assets/Figure6-2.webp "Figure 2: Asymmetric authentication")



Net als bij asymmetrische encryptie zien we een interessant contrast tussen digitale handtekeningen en verificatiecodes voor berichten. Bij de laatste kan het verificatiealgoritme alleen worden gebruikt door een van de partijen die toegang heeft tot de beveiligde communicatie. Hiervoor is namelijk een privésleutel nodig. In de asymmetrische setting kan echter iedereen een digitale handtekening $S$ gemaakt door Bob verifiëren.


Dit alles maakt digitale handtekeningen tot een uiterst krachtig hulpmiddel. Het vormt bijvoorbeeld de basis voor het maken van handtekeningen op contracten die geverifieerd kunnen worden voor juridische doeleinden. Als Bob een handtekening had gezet op een Contract in de Exchange hierboven, kan Alice het bericht $M$, de Contract en de handtekening $S$ aan een rechtbank tonen. De rechtbank kan dan de handtekening verifiëren met de publieke sleutel van Bob. [5]


Een ander voorbeeld: digitale handtekeningen zijn een belangrijk aspect van veilige distributie van software en software-updates. Dit type openbare verifieerbaarheid kan nooit worden gecreëerd met alleen berichtauthenticatiecodes.


Als laatste voorbeeld van de kracht van digitale handtekeningen kunnen we Bitcoin bekijken. Een van de meest voorkomende misvattingen over Bitcoin, vooral in de media, is dat transacties versleuteld zijn: dat is niet zo. In plaats daarvan werken Bitcoin transacties met digitale handtekeningen om de veiligheid te garanderen.


Bitcoins bestaan in batches die ongebruikte transactie-uitgangen (of **UTXO's**) worden genoemd. Stel dat je drie betalingen ontvangt op een bepaalde Bitcoin Address voor elk 2 bitcoins. Technisch gezien heb je nu geen 6 bitcoins op die Address. In plaats daarvan heb je drie batches van 2 bitcoins die vergrendeld zijn door een cryptografisch probleem dat verbonden is aan die Address. Voor elke betaling die je doet, kun je één, twee of alle drie deze batches gebruiken, afhankelijk van hoeveel je nodig hebt voor de transactie.


Het bewijs van Ownership over onuitgegeven transactie-uitgangen wordt gewoonlijk getoond via een of meer digitale handtekeningen. Bitcoin werkt precies omdat geldige digitale handtekeningen op onuitgegeven transactie-uitgangen rekenkundig niet haalbaar zijn om te maken, tenzij je in het bezit bent van de geheime informatie die nodig is om ze te maken.


Op dit moment bevatten Bitcoin transacties transparant alle informatie die geverifieerd moet worden door deelnemers in het netwerk, zoals de herkomst van de ongebruikte transactie-uitgangen die gebruikt zijn in de transactie. Hoewel het mogelijk is om een deel van die informatie te verbergen en toch verificatie toe te staan (zoals sommige alternatieve cryptocurrencies zoals Monero doen), creëert dit ook bepaalde veiligheidsrisico's.


Er ontstaat soms verwarring over digitale handtekeningen en digitaal vastgelegde schriftelijke handtekeningen. In het laatste geval maak je een afbeelding van je geschreven handtekening en plak je die op een elektronisch document zoals een Contract. Dit is echter geen digitale handtekening in cryografische zin. Dit is echter geen digitale handtekening in cryptografische zin. Dit is gewoon een lang nummer dat alleen kan worden geproduceerd als je in het bezit bent van een privésleutel.


Net als bij de symmetrische sleutel kun je ook asymmetrische encryptie- en authenticatieschema's samen gebruiken. Hiervoor gelden dezelfde principes. Ten eerste moet je verschillende private-publieke sleutelparen gebruiken voor encryptie en het maken van digitale handtekeningen. Daarnaast moet je een bericht eerst versleutelen en dan authenticeren.


Belangrijk is dat asymmetrische cryptografie in veel toepassingen niet gedurende het hele communicatieproces wordt gebruikt. In plaats daarvan wordt het meestal alleen gebruikt om *Exchange symmetrische sleutels* te maken tussen de partijen waarmee ze daadwerkelijk communiceren.


Dit is bijvoorbeeld het geval wanneer je online goederen koopt. Als je de publieke sleutel van de verkoper kent, kan ze je digitaal ondertekende berichten sturen die je op echtheid kunt controleren. Op basis hiervan kun je een van de vele protocollen volgen voor het uitwisselen van symmetrische sleutels om veilig te communiceren.


De belangrijkste reden voor de frequentie van de bovengenoemde aanpak is dat asymmetrische cryptografie veel minder efficiënt is dan symmetrische cryptografie in het produceren van een bepaald beveiligingsniveau. Dit is een van de redenen waarom we nog steeds symmetrische cryptografie nodig hebben naast openbare cryptografie. Daarnaast is symmetrische cryptografie veel natuurlijker in bepaalde toepassingen, zoals een computergebruiker die zijn eigen gegevens versleutelt.


Hoe kunnen digitale handtekeningen en publieke sleutelversleuteling Address de problemen met sleuteldistributie en sleutelbeheer oplossen?


Er is hier niet één antwoord. Asymmetrische cryptografie is een hulpmiddel en er is niet één manier om dat hulpmiddel te gebruiken. Maar laten we ons eerdere voorbeeld van Jim's Sporting Goods nemen om te laten zien hoe de problemen typisch zouden worden aangepakt in dit voorbeeld.


Om te beginnen zou Jim's Sporting Goods waarschijnlijk een **certificaatautoriteit** benaderen, een organisatie die ondersteuning biedt bij de distributie van publieke sleutels. De certificaatautoriteit registreert een aantal gegevens over Jim's Sporting Goods en kent het een publieke sleutel toe. Vervolgens stuurt de certificeringsinstantie Jim's Sporting Goods een certificaat, een zogenaamd **TLS/SSL-certificaat**, met de openbare sleutel van Jim's Sporting Goods digitaal ondertekend met de openbare sleutel van de certificeringsinstantie zelf. Op deze manier bevestigt de certificeringsinstantie dat een bepaalde openbare sleutel inderdaad toebehoort aan Jim's Sporting Goods.


De sleutel tot het begrijpen van dit proces met TLS/SSL-certificaten is dat, hoewel je over het algemeen de openbare sleutel van Jim's Sporting Goods nergens op je computer hebt opgeslagen, de openbare sleutels van erkende certificeringsinstanties wel degelijk in je browser of in je besturingssysteem zijn opgeslagen. Deze worden opgeslagen in zogenaamde **root certificaten**.


Wanneer Jim's Sporting Goods je dus zijn TLS/SSL-certificaat verstrekt, kun je de digitale handtekening van de certificeringsinstantie controleren via een rootcertificaat in je browser of besturingssysteem. Als de handtekening geldig is, kun je er relatief zeker van zijn dat de openbare sleutel op het certificaat inderdaad toebehoort aan Jim's Sporting Goods. Op basis hiervan kun je eenvoudig een protocol opzetten voor beveiligde communicatie met Jim's Sporting Goods.


De distributie van sleutels is nu veel eenvoudiger geworden voor Jim's Sporting Goods. Het is niet Hard om te zien dat het sleutelbeheer ook enorm vereenvoudigd is. In plaats van duizenden sleutels op te slaan, hoeft Jim's Sporting Goods alleen maar een privésleutel op te slaan waarmee handtekeningen kunnen worden gezet onder de openbare sleutel van zijn SSL-certificaat. Elke keer dat een klant naar de site van Jim's Sporting Goods komt, kan hij een beveiligde communicatiesessie opzetten met deze openbare sleutel. Klanten hoeven ook geen informatie op te slaan (behalve de openbare sleutels van erkende certificeringsinstanties in hun besturingssysteem en browser).


**Noten:**


[5] Elk schema dat onweerlegbaarheid probeert te bereiken, het andere thema dat we in hoofdstuk 1 hebben besproken, zal aan de basis digitale handtekeningen moeten bevatten.




## Hash functies

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>


Hash functies zijn alomtegenwoordig in cryptografie. Ze zijn geen symmetrische of asymmetrische schema's, maar vallen in een cryptografische categorie op zichzelf.


We kwamen Hash functies al tegen in Hoofdstuk 4 met het aanmaken van Hash gebaseerde authenticatieberichten. Ze zijn ook belangrijk in de context van digitale handtekeningen, zij het om een iets andere reden: Digitale handtekeningen worden namelijk meestal gemaakt over de Hash waarde van een of ander (versleuteld) bericht, in plaats van het eigenlijke (versleutelde) bericht. In deze sectie zal ik een meer diepgaande introductie geven van Hash functies.


Laten we beginnen met het definiëren van een Hash functie. Een **Hash functie** is elke efficiënt berekenbare functie die invoer van willekeurige grootte neemt en uitvoer van vaste lengte oplevert.


Een **cryptografische Hash functie** is gewoon een Hash functie die nuttig is voor toepassingen in de cryptografie. De uitvoer van een cyptografische Hash functie wordt meestal de **Hash**, **Hash-waarde**, of **bericht digest** genoemd.


In de context van cryptografie verwijst een "Hash functie" gewoonlijk naar een cryptografische Hash functie. Vanaf nu zal ik die praktijk overnemen.


Een voorbeeld van een populaire Hash functie is **SHA-256** (veilig Hash algoritme 256). Ongeacht de grootte van de invoer (bijvoorbeeld 15 bits, 100 bits of 10.000 bits), zal deze functie een 256-bits Hash waarde opleveren. Hieronder zie je een paar voorbeelduitgangen van de SHA-256 functie.


"Hallo": `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`


"52398": `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`


"Cryptografie is leuk": `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`


Alle uitgangen zijn precies 256 bits, uitgeschreven in hexadecimaal formaat (elk hexadecimaal cijfer kan worden weergegeven door vier binaire cijfers). Dus zelfs als je Tolkien's *The Lord of the Rings* boek in de SHA-256 functie had gestopt, zou de uitvoer nog steeds 256 bits zijn.


Hash functies zoals SHA-256 worden gebruikt voor verschillende doeleinden in de cryptografie. Welke eigenschappen vereist zijn van een Hash functie hangt echt af van de context van een bepaalde toepassing. Er zijn twee belangrijke eigenschappen die over het algemeen gewenst zijn voor Hash functies in cryptografie: [6]


1.	Botsbestendigheid

2.	Verbergen


Van een Hash functie $H$ wordt gezegd dat deze **collision-resistant** is als het niet mogelijk is om twee waarden, $x$ en $y$, te vinden zodanig dat $x \neq y$, maar toch $H(x) = H(y)$.


Botsingsbestendige Hash functies zijn bijvoorbeeld belangrijk bij de verificatie van software. Stel dat je de Windows versie van Bitcoin Core 0.21.0 (een servertoepassing voor het verwerken van Bitcoin netwerkverkeer) wilde downloaden. De belangrijkste stappen die je zou moeten nemen om de legitimiteit van de software te verifiëren, zijn de volgende:


1.	Je moet eerst de publieke sleutels van één of meer bijdragers Bitcoin Core downloaden en importeren in software die digitale handtekeningen kan verifiëren (bijv. Kleopetra). Je kunt deze publieke sleutels [hier] vinden (https://github.com/Bitcoin/Bitcoin/blob/master/contrib/builder-keys/keys.txt). Het wordt aanbevolen om de Bitcoin Core software te verifiëren met de publieke sleutels van meerdere bijdragers.

2.	Vervolgens moet je de publieke sleutels die je hebt geïmporteerd verifiëren. Ten minste één stap die je moet nemen is controleren of de publieke sleutels die je gevonden hebt dezelfde zijn als die gepubliceerd zijn op verschillende andere locaties. Je zou bijvoorbeeld de persoonlijke webpagina's, Twitter-pagina's of Github-pagina's kunnen raadplegen van de mensen van wie je de publieke sleutels hebt geïmporteerd. Meestal wordt deze vergelijking van publieke sleutels gedaan door een korte Hash van de publieke sleutel te vergelijken, ook wel bekend als een vingerafdruk.

3.	Vervolgens moet je de executable voor Bitcoin Core downloaden van hun [website] (www.bitcoincore.org). Er zijn pakketten beschikbaar voor Linux, Windows en MAC besturingssystemen.

4.	Vervolgens moet je twee release bestanden vinden. Het eerste bevat de officiële SHA-256 Hash voor het uitvoerbare bestand dat je hebt gedownload, samen met de hashes van alle andere pakketten die zijn uitgebracht. Een ander releasebestand bevat de handtekeningen van verschillende bijdragers over het releasebestand met de hashes van de pakketten. Beide release bestanden zouden zich op de Bitcoin Core website moeten bevinden.

5.	 Vervolgens moet je de SHA-256 Hash berekenen van de executable die je hebt gedownload van de Bitcoin Core website op je eigen computer. Vergelijk vervolgens dit resultaat met dat van het officiële Hash pakket voor de executable. Ze zouden hetzelfde moeten zijn.

6.	Tenslotte zou je moeten controleren of één of meer van de digitale handtekeningen over het releasebestand met de officiële hashes van het pakket inderdaad overeenkomt met één of meer publieke sleutels die je geïmporteerd hebt (releases van Bitcoin Core worden niet altijd door iedereen ondertekend). Je kunt dit doen met een applicatie als Kleopetra.


Dit proces van softwareverificatie heeft twee belangrijke voordelen. Ten eerste zorgt het ervoor dat er geen fouten zijn opgetreden tijdens het downloaden van de Bitcoin Core-website. Ten tweede zorgt het ervoor dat aanvallers u geen gewijzigde, kwaadaardige code kunnen laten downloaden, hetzij door de Bitcoin Core-website te hacken, hetzij door verkeer te onderscheppen.


Hoe beschermt het bovenstaande softwareverificatieproces precies tegen deze problemen?


Als u de publieke sleutels die u geïmporteerd hebt zorgvuldig geverifieerd hebt, dan kunt u er vrij zeker van zijn dat deze sleutels echt van hen zijn en niet gecompromitteerd zijn. Gezien het feit dat digitale handtekeningen existentieel onvervalsbaar zijn, weet je dat alleen deze medewerkers een digitale handtekening konden zetten op de officiële hashes van het pakket in het releasebestand.


Stel dat de handtekeningen op het gedownloade releasebestand kloppen. Je kunt nu de Hash waarde die je lokaal hebt berekend voor de Windows executable die je hebt gedownload vergelijken met die in het correct ondertekende releasebestand. Zoals u weet is de SHA-256 Hash functie collion resistant, een overeenkomst betekent dat uw uitvoerbare bestand precies hetzelfde is als het officiële uitvoerbare bestand.


Laten we het nu hebben over de tweede algemene eigenschap van Hash functies: **verbergen**. Van een Hash functie $H$ wordt gezegd dat deze de eigenschap van verbergen heeft als het voor een willekeurig gekozen $x$ uit een zeer groot bereik niet mogelijk is $x$ te vinden als alleen $H(x)$ gegeven wordt.


Hieronder zie je de SHA-256 uitvoer van een bericht dat ik geschreven heb. Om voldoende willekeur te garanderen, bevatte het bericht een willekeurig gegenereerde tekenreeks aan het einde. Aangezien SHA-256 de eigenschap heeft om te verbergen, zou niemand dit bericht kunnen ontcijferen.



- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`


Maar ik laat je niet in spanning totdat SHA-256 zwakker wordt. Het oorspronkelijke bericht dat ik schreef was als volgt:



- "Dit is een heel willekeurig bericht, of nou ja een soort van willekeurig. Dit begin is dat niet, maar ik zal eindigen met een aantal relatief willekeurige tekens om een zeer onvoorspelbaar bericht te garanderen. XLWz4dVG3BxUWm7zQ9qS".


Een veel voorkomende manier waarop Hash functies met de eigenschap verbergen worden gebruikt, is in wachtwoordbeheer (botsingsweerstand is ook belangrijk voor deze toepassing). Elke fatsoenlijke online account-gebaseerde dienst zoals Facebook of Google zal je wachtwoorden niet direct opslaan om de toegang tot je account te beheren. In plaats daarvan slaan ze alleen een Hash van dat wachtwoord op. Elke keer dat je je wachtwoord invult op een browser, wordt er eerst een Hash berekend. Alleen die Hash wordt naar de server van de serviceprovider gestuurd en vergeleken met de Hash die is opgeslagen in de back-end database. De verborgen eigenschap kan ervoor zorgen dat aanvallers de Hash waarde niet kunnen achterhalen.


Wachtwoordbeheer via hashes werkt natuurlijk alleen als gebruikers daadwerkelijk moeilijke wachtwoorden kiezen. De eigenschap verbergen veronderstelt dat x willekeurig gekozen wordt uit een zeer groot bereik. Het kiezen van wachtwoorden zoals "1234", "mypassword", of je verjaardagsdatum zal geen echte veiligheid bieden. Er bestaan lange lijsten met veelgebruikte wachtwoorden en hun hashes die aanvallers kunnen gebruiken als ze ooit de Hash van je wachtwoord bemachtigen. Dit soort aanvallen staan bekend als **woordenboekaanvallen**. Als aanvallers een aantal van je persoonlijke gegevens kennen, kunnen ze ook proberen een geïnformeerde gok te doen. Daarom heb je altijd lange, veilige wachtwoorden nodig (bij voorkeur lange, willekeurige reeksen uit een wachtwoordmanager).


Soms heeft een toepassing een Hash functie nodig die zowel botsingsweerstand heeft als verbergt. Maar zeker niet altijd. Het softwareverificatieproces dat we hebben besproken, vereist bijvoorbeeld alleen dat de Hash functie botsingsweerstand heeft, verbergen is niet belangrijk.


Hoewel botsingsbestendigheid en verbergen de belangrijkste eigenschappen zijn die gezocht worden van Hash functies in cryptografie, kunnen in bepaalde toepassingen ook andere soorten eigenschappen wenselijk zijn.



**Noten:**


[6] De terminologie "verbergen" is geen gebruikelijke taal, maar komt specifiek uit Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller en Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Hoofdstuk 1.



# Het RSA cryptosysteem

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>




## Het factorprobleem

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>


Terwijl symmetrische cryptografie meestal vrij intuïtief is voor de meeste mensen, is dit meestal niet het geval met asymmetrische cryptografie. Hoewel je waarschijnlijk vertrouwd bent met de beschrijving op hoog niveau uit de vorige secties, vraag je je waarschijnlijk af wat eenrichtingsfuncties precies zijn en hoe ze precies gebruikt worden om asymmetrische schema's te construeren.


In dit hoofdstuk zal ik wat van het mysterie rond asymmetrische cryptografie wegnemen, door dieper in te gaan op een specifiek voorbeeld, namelijk het RSA cryptosysteem. In de eerste paragraaf introduceer ik het factorisatieprobleem waarop het RSA-probleem is gebaseerd. Daarna zullen we een aantal belangrijke resultaten uit de getaltheorie behandelen. In de laatste paragraaf zullen we deze informatie samenvoegen om het RSA probleem uit te leggen, en hoe dit gebruikt kan worden voor het maken van asymmetrische cryptografische schema's.


Het is niet eenvoudig om deze diepgang aan onze discussie toe te voegen. Het vereist de introductie van heel wat getaltheoretische stellingen. Maar laat de wiskunde je niet afschrikken. Het doorwerken van deze discussie zal je begrip van wat ten grondslag ligt aan asymmetrische cryptografie aanzienlijk verbeteren en is een investering die de moeite waard is.


Laten we nu eerst kijken naar het factorprobleem.


___



Wanneer je twee getallen vermenigvuldigt, bijvoorbeeld $a$ en $b$, noemen we de getallen $a$ en $b$ **factoren**, en het resultaat het **product**. Een getal $N$ proberen om te zetten in een vermenigvuldiging van twee of meer factoren noemen we **factoriseren** of **factoren**. [1] Elk probleem dat dit vereist, kun je een **factorisatieprobleem** noemen.


Ongeveer 2500 jaar geleden ontdekte de Griekse wiskundige Euclides van Alexandrië een belangrijke stelling over de factorisatie van gehele getallen. Deze stelling wordt gewoonlijk de **unieke factorisatiestelling** genoemd en stelt het volgende:


**Stelling 1**. Elk geheel getal $N$ dat groter is dan 1 is ofwel een priemgetal, of kan worden uitgedrukt als een product van priemfactoren.


Het laatste deel van deze bewering betekent alleen dat je elk niet-priem geheel getal $N$ groter dan 1 kunt nemen en het kunt uitschrijven als een vermenigvuldiging van priemgetallen. Hieronder staan verschillende voorbeelden van niet-priem gehele getallen geschreven als het product van priemfactoren.



- $18 = 2 \dot 3 \dot 3 = 2 \dot 3^2$
- $84 = 2 \dot 2 \dot 3 \dot 7 = 2^2 \dot 3 \dot 7$
- $144 = 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$


Voor alle drie de bovenstaande gehele getallen is het berekenen van hun priemfactoren relatief eenvoudig, zelfs als je slechts $N$ krijgt. Je begint met het kleinste priemgetal, namelijk 2, en kijkt hoeveel keer het gehele getal $N$ hierdoor deelbaar is. Vervolgens test je de deelbaarheid van $N$ door 3, 5, 7, enzovoort. Je gaat door met dit proces totdat je gehele getal $N$ geschreven is als het product van alleen priemgetallen.


Neem bijvoorbeeld het gehele getal 84. Hieronder zie je het proces voor het bepalen van de priemfactoren. Bij elke stap halen we de kleinste resterende priemfactor eruit (aan de linkerkant) en bepalen we de restterm die we moeten ontbinden in factoren. We gaan door totdat de restterm ook een priemgetal is. Bij elke stap wordt de huidige factorisatie van 84 helemaal rechts weergegeven.



- Prime factor = 2: restterm = 42 ($84 = 2 \cdot 42$)
- Prime factor = 2: restterm = 21 ($84 = 2 \dot 2 \dot 21$)
- Prime factor = 3: restterm = 7 ($84 = 2 \dot 2 \dot 3 \dot 7$)
- Omdat 7 een priemgetal is, is het resultaat $2 \dot 2 \dot 3 \dot 7$, of $2^2 \dot 3 \dot 7$.


Stel nu dat $N$ heel groot is. Hoe moeilijk zou het zijn om $N$ te reduceren tot zijn priemfactoren?


Dat hangt echt af van $N$. Stel bijvoorbeeld dat $N$ 50.450.400 is. Hoewel dit getal intimiderend lijkt, zijn de berekeningen niet zo ingewikkeld en kunnen ze gemakkelijk met de hand worden uitgevoerd. Net als hierboven begin je gewoon met 2 en werk je zo verder. Hieronder zie je het resultaat van dit proces op een vergelijkbare manier als hierboven.



- 2: 25.225.200 ($50.450.400 = 2 $25.225.200$)
- 2: 12.612.600 ($50.450.400 = 2^2 \cdot 12.612.600$)
- 2: 6.306.300 ($50.450.400 = 2^3 ≤ 6.306.300$)
- 2: 3.153.150 ($50.450.400 = 2^4 \dot 3.153.150$)
- 2: 1.576.575 ($50.450.400 = 2^5 ≤ 1.576.575$)
- 3: 525.525 ($50.450.400 = 2^5 \dot 3 \dot 525.525$)
- 3: 175.175 ($50.450.400 = 2^5 \dot 3^2 \dot 175.175$)
- 5: 35.035 ($50.450.400 = 2^5 \dot 3^2 \dot 5 \dot 35.035$)
- 5: 7.007 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7.007$)
- 7: 1.001 ($50.450.400 = 2^5 \dot 3^2 \dot 5^2 \dot 7 \dot 1.001$)
- 7: 143 ($50.450.400 = 2^5 \dot 3^2 \dot 5^2 \dot 7^2 \dot 143$)
- 11: 13 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- Omdat 13 een priemgetal is, is het resultaat $2^5 \dot 3^2 \dot 5^2 \dot 7^2 \dot 11 \dot 13$.


Dit probleem met de hand oplossen kost tijd. Een computer kan dit natuurlijk allemaal in een fractie van een seconde. Een computer kan zelfs vaak extreem grote gehele getallen ontbinden in factoren in een fractie van een seconde.


Er zijn echter bepaalde uitzonderingen. Stel dat we eerst willekeurig twee zeer grote priemgetallen kiezen. Het is gebruikelijk om deze $p$ en $q$ te labelen, en ik zal die conventie hier overnemen.


Laten we voor de duidelijkheid zeggen dat $p$ en $q$ allebei 1024-bits priemgetallen zijn en dat ze inderdaad minstens 1024 bits nodig hebben om te worden weergegeven (dus het eerste bit moet 1 zijn). Dus bijvoorbeeld 37 kan geen priemgetal zijn. Je kunt 37 zeker weergeven met 1024 bits. Maar het is duidelijk dat *je* niet zoveel bits nodig hebt om het voor te stellen. Je kunt 37 weergeven met elke tekenreeks die 6 bits of meer heeft. (In 6 bits zou 37 worden weergegeven als $100101$).


Het is belangrijk om te weten hoe groot $p$ en $q$ zijn als ze onder de bovenstaande voorwaarden worden geselecteerd. Als voorbeeld heb ik hieronder een willekeurig priemgetal gekozen dat minstens 1024 bits nodig heeft voor representatie.



- 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589


Stel nu dat we na het willekeurig kiezen van priemgetallen $p$ en $q$, deze met elkaar vermenigvuldigen om een geheel getal $N$ te verkrijgen. Dit laatste gehele getal is dus een getal van 2048 bits dat minstens 2048 bits nodig heeft voor zijn representatie. Het is veel, veel groter dan $p$ of $q$.


Stel dat je een computer alleen $N$ geeft en hem vraagt om de twee 1024 bit priemfactoren van $N$ te vinden. De kans dat de computer $p$ en $q$ ontdekt is extreem klein. Je kunt zeggen dat het praktisch gezien onmogelijk is. Dit is zo, zelfs als je een supercomputer of zelfs een netwerk van supercomputers zou inzetten.


Stel om te beginnen dat de computer het probleem probeert op te lossen door 1024 bitgetallen te doorlopen en telkens te testen of ze priem zijn en of ze factoren van $N$ zijn. De verzameling priemgetallen die getest moet worden is dan ongeveer $1,265 \cdot 10^{305}$. [2]


Zelfs als je alle computers op aarde op deze manier 1024-bits priemgetallen laat proberen te vinden en testen, zou een kans van 1 op een miljard om een priemfactor van $N$ te vinden een rekenperiode vergen die veel langer is dan de leeftijd van het heelal.


Nu kan een computer het in de praktijk beter doen dan de zojuist beschreven ruwe procedure. Er bestaan verschillende algoritmen die de computer kan toepassen om sneller tot een factorisatie te komen. Het punt is echter dat zelfs met deze efficiëntere algoritmen, de taak van de computer nog steeds rekenkundig onuitvoerbaar is. [3]


Belangrijk is dat de moeilijkheid van de factorisatie onder de zojuist beschreven voorwaarden berust op de aanname dat er geen rekenkundig efficiënte algoritmen bestaan voor het berekenen van priemfactoren. We kunnen niet bewijzen dat er geen efficiënt algoritme bestaat. Toch is deze aanname zeer aannemelijk: ondanks uitgebreide inspanningen gedurende honderden jaren, hebben we nog steeds niet zo'n rekenkundig efficiënt algoritme gevonden.


Daarom kan het factorisatieprobleem, onder bepaalde omstandigheden, aannemelijk worden gemaakt als een Hard probleem. Meer bepaald, wanneer $p$ en $q$ zeer grote priemgetallen zijn, is hun product $N$ niet moeilijk te berekenen; maar factorisatie alleen gegeven $N$ is praktisch onmogelijk.



**Noten:**


[1] Factoriseren kan ook belangrijk zijn voor het werken met andere typen wiskundige objecten dan getallen. Het kan bijvoorbeeld nuttig zijn om veeltermuitdrukkingen zoals $x^2 - 2x + 1$ te ontbinden in factoren. In onze discussie zullen we ons alleen richten op de ontbinding in factoren van getallen, in het bijzonder gehele getallen.


[2] Volgens het **priemgetaltheorema** is het aantal priemgetallen kleiner dan of gelijk aan $N$ ongeveer $N/LN(N)$. Dit betekent dat je het aantal priemgetallen met een lengte van 1024 bits kunt benaderen door:


$$ \frac{2^{1024}}{\LN(2^{1024})} - \frac{2^{1023}}{\LN(2^{1023})} $$


...wat overeenkomt met ongeveer $1,265 maal 10^{305}$.


[3] Hetzelfde geldt voor discrete logaritmische problemen. Daarom werken asymmetrische constructies met veel grotere sleutels dan symmetrische cryptografische constructies.




## Getaltheoretische resultaten

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>


Helaas kan het factorprobleem niet direct gebruikt worden voor asymmetrische cryptografische schema's. We kunnen hiervoor echter wel een complexer maar gerelateerd probleem gebruiken: het RSA probleem.


Om het RSA probleem te begrijpen, moeten we een aantal stellingen en stellingen uit de getaltheorie begrijpen. Deze worden in deze sectie in drie subsecties gepresenteerd: (1) de orde van N, (2) inverteerbaarheid modulo N en (3) de stelling van Euler.


Een deel van het materiaal in de drie subsecties is al geïntroduceerd in *Hoofdstuk 3*. Maar voor het gemak zal ik dat materiaal hier herhalen.



### De volgorde van N


Een geheel getal $a$ is **coprime** of een **relatieve priem** met een geheel getal $N$, als de grootste gemene deler tussen hen 1 is. Hoewel 1 volgens conventie geen priemgetal is, is het een coprime van elk geheel getal (net als $-1$).


Neem bijvoorbeeld het geval dat $a = 18$ en $N = 37$. Dit zijn duidelijk coprimes. Het grootste gehele getal dat deelt in zowel 18 als 37 is 1. Neem daarentegen het geval waarin $a = 42$ en $N = 16$. Dit zijn duidelijk geen coprimes. Beide getallen zijn deelbaar door 2, wat groter is dan 1.


We kunnen nu de orde van $N$ als volgt definiëren. Stel dat $N$ een geheel getal groter dan 1 is. De **orde van N** is dan het aantal van alle coprimes met $N$ zodanig dat voor elke coprime $a$ de volgende voorwaarde geldt: $1 \leq a < N$.


Bijvoorbeeld, als $N = 12$, dan zijn 1, 5, 7 en 11 de enige coprimes die aan bovenstaande voorwaarde voldoen. De orde van 12 is dus gelijk aan 4.


Stel dat $N$ een priemgetal is. Dan is elk geheel getal kleiner dan $N$ maar groter of gelijk aan 1 er copriem mee. Dit omvat alle Elements in de volgende verzameling: ${1,2,3,....,N - 1}$. Als $N$ priem is, is de orde van $N$ dus $N - 1$. Dit staat in stelling 1, waarbij $phi(N)$ de orde van $N$ is.


**Stelling 1. $phi(N) = N - 1$ als $N$ priem is


Stel dat $N$ geen priemgetal is. Je kunt dan de orde berekenen met **Eulers Phi-functie**. Terwijl het berekenen van de orde van een klein geheel getal relatief eenvoudig is, wordt de Phi-functie van Euler vooral belangrijk voor grotere gehele getallen. De stelling van de Phi-functie van Euler staat hieronder.


**Stelling 2**. Laat $N$ gelijk zijn aan $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \cdot p_n^{e_n}$, waarbij de verzameling ${p_i}$ bestaat uit alle verschillende priemfactoren van $N$ en elke $e_i$ aangeeft hoe vaak de priemfactor $p_i$ voorkomt voor $N$. Dan geldt,


$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$


**Stelling 2** laat zien dat als je een willekeurige niet-priem $N$ hebt opgesplitst in zijn verschillende priemfactoren, het eenvoudig is om de orde van $N$ te berekenen.


Stel bijvoorbeeld dat $N = 270$. Dit is duidelijk geen priemgetal. Als je $N$ uitsplitst in priemfactoren krijg je de uitdrukking: $2 \3 \5$. Volgens de Phi-functie van Euler is de orde van $N$ dan als volgt:


$$$$phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$


Stel nu dat $N$ een product is van twee priemgetallen, $p$ en $q$. **Stelling 2** hierboven stelt dan dat de orde van $N$ als volgt is:


$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$


Dit is een belangrijk resultaat voor het RSA probleem in het bijzonder, en staat in **Stelling 2** hieronder.


**Stelling 2**. Als $N$ het product is van twee priemgetallen, $p$ en $q$, dan is de orde van $N$ het product $(p - 1) ▶ (q - 1)$.


Stel ter illustratie dat $N = 119$. Dit gehele getal kan worden ontbonden in twee priemgetallen, namelijk 7 en 17. De Phi-functie van Euler suggereert dus dat de orde van 119 als volgt is:


$$phi(119) = (7 - 1) \dot (17 - 1) = 6 \dot 16 = 96$$


Met andere woorden, het gehele getal 119 heeft 96 coprimes in de reeks van 1 tot 119. In feite bevat deze verzameling alle gehele getallen van 1 tot 119 die geen veelvoud zijn van 7 of 17.


Vanaf hier noemen we de verzameling coprimes die de volgorde van $N$ bepaalt $C_N$. Voor ons voorbeeld met $N = 119$ is de verzameling $C_{119}$ veel te groot om volledig op te noemen. Maar enkele van de Elements zijn als volgt:


$$C_{119} = \{1, 2, \dots 6, 8, \dots 13, 15, 16, 18, \dots 33, 35, \dots 96}$$


### Inverteerbaarheid modulo N


We kunnen zeggen dat een geheel getal $a$ **inverteerbaar is modulo N**, als er ten minste één geheel getal $b$ bestaat zodat $a \cdot b \mod N = 1 \mod N$. Zo'n geheel getal $b$ wordt een **inverse** (of **multiplicatieve inverse**) van $a$ genoemd, gegeven reductie door modulo $N$.


Stel bijvoorbeeld dat $a = 5$ en $N = 11$. Er zijn veel gehele getallen waarmee je 5 kunt vermenigvuldigen, zodat $5 \dot b \mod 11 = 1 \mod 11$. Neem bijvoorbeeld de gehele getallen 20 en 31. Het is eenvoudig te zien dat deze beide gehele getallen invers zijn van 5 voor reductie modulo 11.



- $5 \dot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
- $5 \dot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$


Terwijl 5 veel inverses reductie modulo 11 heeft, kun je laten zien dat er maar één positieve inverse van 5 bestaat die kleiner is dan 11. In feite is dit niet uniek voor ons specifieke voorbeeld, maar een algemeen resultaat.


**Stelling 3**. Als het gehele getal $a$ inverteerbaar is modulo $N$, moet het zo zijn dat precies één positieve inverse van $a$ kleiner is dan $N$. (Deze unieke inverse van $a$ moet dus uit de verzameling ${1, \dots, N - 1}$ komen).


Laten we de unieke inverse van $a$ uit **stelling 3** aanduiden als $a^{-1}$. Voor het geval dat $a = 5$ en $N = 11$ kun je zien dat $a^{-1} = 9$, gegeven dat $5 \dot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.


Merk op dat je de waarde 9 voor $a^{-1}$ in ons voorbeeld ook kunt verkrijgen door eenvoudigweg elke andere inverse van $a$ te verminderen met modulo 11. Bijvoorbeeld, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Dus als een geheel getal $a > N$ inverteerbaar is modulo $N$, dan moet $a \mod N$ ook inverteerbaar zijn modulo $N$.


Het is niet noodzakelijk zo dat er een inverse van $a$ bestaat reductie modulo $N$. Stel bijvoorbeeld dat $a = 2$ en $N = 8$. Er is geen $b$, of een $a^{-1}$ in het bijzonder, zodat $2 \cdot b \mod 8 = 1 \mod 8$. Dit komt omdat elke waarde van $b$ altijd een veelvoud van 2 oplevert, dus een deling door 8 kan nooit een rest opleveren die gelijk is aan 1.


Hoe weten we precies of een bepaald geheel getal $a$ een inverse heeft voor een gegeven $N$? Zoals je misschien hebt gemerkt in het voorbeeld hierboven, is de grootste gemene deler tussen 2 en 8 hoger dan 1, namelijk 2. En dit is eigenlijk illustratief voor het volgende algemene resultaat:


**Stelling 4**. Er bestaat een inverse van een geheel getal $a$ gegeven reductie modulo $N$, en in het bijzonder een unieke positieve inverse kleiner dan $N$, als en slechts als de grootste gemene deler tussen $a$ en $N$ 1 is (dat wil zeggen, als het coprimes zijn).


Voor het geval dat $a = 5$ en $N = 11$ concludeerden we dat $a^{-1} = 9$, gegeven dat $5 \dot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Het is belangrijk op te merken dat het omgekeerde ook waar is. Dat wil zeggen, als $a = 9$ en $N = 11$, is het zo dat $a^{-1} = 5$.



### Stelling van Euler


Voordat we verder gaan met het RSA probleem, moeten we nog een cruciale stelling begrijpen, namelijk de stelling van **Euler**. Deze stelling luidt als volgt:


**Stelling 3**. Stel dat twee gehele getallen $a$ en $N$ coprimes zijn. Dan is $a^{{\phi(N)} \mod N = 1 \mod N$.


Dit is een opmerkelijk resultaat, maar een beetje verwarrend in het begin. Laten we een voorbeeld nemen om het te begrijpen.


Stel dat $a = 5$ en $N = 7$. Dit zijn inderdaad coprimes zoals de stelling van Euler vereist. We weten dat de orde van 7 gelijk is aan 6, gegeven dat 7 een priemgetal is (zie **Stelling 1**).


De stelling van Euler stelt nu dat $5^6 \mod 7$ gelijk moet zijn aan $1 \mod 7$. Hieronder staan de berekeningen om aan te tonen dat dit inderdaad waar is.



- $5^6 \mod 7 = 15.625 \mod 7 = 1 \mod N$


Het gehele getal 7 deelt in totaal 2.233 keer door 15.624. De rest van het delen van 16.625 door 7 is dus 1.


Vervolgens kun je met behulp van de Phi-functie van Euler, **stelling 2**, **stelling 5** hieronder afleiden.


**Stelling 5. $ \phi(a \cdot b) = \phi(a) \cdot \phi(b)$ voor willekeurige positieve gehele getallen $a$ en $b$.


We zullen niet laten zien waarom dit zo is. Merk alleen op dat je het bewijs voor deze stelling al gezien hebt door het feit dat $ \phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ als $p$ en $q$ priemgetallen zijn, zoals staat in **Stelling 2**.


De stelling van Euler in combinatie met **Stelling 5** heeft belangrijke implicaties. Kijk bijvoorbeeld wat er gebeurt in de onderstaande uitdrukkingen, waarbij $a$ en $N$ coprimes zijn.



- $a^{2 \dot \phi(N)} \mod N = a^{\phi(N)} \dot a^{\phi(N)} \mod N = 1 \dot 1 \mod N = 1 \mod N$
- $a^{{\phi(N) + 1} \mod N = a^{{\phi(N)} \mod a^1 \mod N = 1 \mod a^1 \mod N = a \mod N$
- $a^{8 \dot \phi(N) + 3} \mod N = a^{8 \dot \phi(N)} \dot a^3 \mod N = 1 \dot a^3 \mod N = a^3 \mod N$


De combinatie van de stelling van Euler en **Stelling 5** stelt ons dus in staat om eenvoudig een aantal uitdrukkingen te berekenen. In het algemeen kunnen we het inzicht samenvatten zoals in **Stelling 6**.


** Stelling 6**. $a^x \mod N = a^{x \mod \phi(N)}$


Nu moeten we alles samenvoegen in een lastige laatste stap.


Net zoals $N$ een orde $\phi(N)$ heeft die de Elements van de verzameling $C_N$ omvat, weten we dat het gehele getal $\phi(N)$ op zijn beurt ook een orde en een verzameling coprimes moet hebben. Laten we stellen dat $C_N$ = R$. Dan weten we dat er ook een waarde is voor $\phi(R)$ en een verzameling coprimes $C_R$.


Stel dat we nu een geheel getal $e$ kiezen uit de verzameling $C_R$. We weten uit **Stelling 3** dat dit gehele getal $e$ slechts één unieke positieve inverse heeft kleiner dan $R$. Dat wil zeggen, $e$ heeft één unieke inverse uit de verzameling $C_R$. Laten we deze inverse $d$ noemen. Gegeven de definitie van een inverse betekent dit dat $e \dot d = 1 \mod R$.


We kunnen dit resultaat gebruiken om een uitspraak te doen over ons oorspronkelijke gehele getal $N$. Dit is samengevat in **Stelling 7**.


**Stelling 7. Stel dat $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Dan geldt voor elk element $a$ van de verzameling $C_N$ dat $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.


We hebben nu alle getaltheoretische resultaten die nodig zijn om het RSA probleem duidelijk te stellen.



## Het RSA cryptosysteem

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>


We zijn nu klaar om het RSA probleem op te lossen. Stel dat je een verzameling variabelen maakt bestaande uit $p$, $q$, $N$, $\phi(N)$, $e$, $d$ en $y$. Noem deze verzameling $Pi$. Deze wordt als volgt gemaakt:


1. generate twee willekeurige priemgetallen $p$ en $q$ van gelijke grootte en bereken hun product $N$.

2. Bereken de orde van $N$, $\phi(N)$, door het volgende product: $(p - 1) \cdot (q - 1)$.

3. Kies een $e > 2$ zo dat deze kleiner is en coprime met $\phi(N)$.

4. Bereken $d$ door $e \dot d \mod \phi(N) = 1$.

5. Kies een willekeurige waarde $y$ die kleiner en coprime is met $N$.


Het RSA-probleem bestaat uit het vinden van een $x$ zodanig dat $x^e = y$, terwijl slechts een deelverzameling van informatie over $\Pi$ wordt gegeven, namelijk de variabelen $N$, $e$ en $y$. Als $p$ en $q$ erg groot zijn, meestal is het aan te raden dat ze 1024 bits groot zijn, wordt het RSA-probleem als Hard beschouwd. Je kunt nu zien waarom dit het geval is, gezien de voorgaande discussie.


Een eenvoudige manier om $x$ te berekenen als $x^e \mod N = y \mod N$ is door eenvoudig $y^d \mod N$ te berekenen. We weten dat $y^d \mod N = x \mod N$ door de volgende berekeningen:


$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$


Het probleem is dat we de waarde $d$ niet weten, omdat die niet in het probleem gegeven is. We kunnen dus niet direct $y^d \mod N$ berekenen om $x \mod N$ te krijgen.


We kunnen echter misschien indirect $d$ berekenen uit de orde van $N$, $\phi(N)$, omdat we weten dat $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Maar door aanname geeft het probleem ook geen waarde voor $phi(N)$.


Tenslotte zou de volgorde indirect berekend kunnen worden met de priemfactoren $p$ en $q$, zodat we uiteindelijk $d$ kunnen berekenen. Maar door aanname zijn de waarden $p$ en $q$ ook niet aan ons verstrekt.


Strikt genomen, zelfs als het factorprobleem binnen een RSA probleem Hard is, kunnen we niet bewijzen dat het RSA probleem ook Hard is. Er kunnen namelijk andere manieren zijn om het RSA probleem op te lossen dan door te factoriseren. Het is echter algemeen aanvaard en aangenomen dat als het factorprobleem binnen het RSA probleem Hard is, dat het RSA probleem zelf ook Hard is.


Als het RSA-probleem inderdaad Hard is, dan produceert het een eenrichtingsfunctie met een valluik. De functie hier is $f(g) = g^e \mod N$. Met kennis van $f(g)$ kan iedereen gemakkelijk een waarde $y$ berekenen voor een bepaalde $g = x$. Het is echter praktisch onmogelijk om een bepaalde waarde $x$ te berekenen door alleen de waarde $y$ en de functie $f(g)$ te kennen. De uitzondering is wanneer je een stukje informatie $d$ krijgt, het valluik. In dat geval kun je eenvoudig $y^d$ berekenen om $x$ te krijgen.


Laten we een specifiek voorbeeld bekijken om het RSA probleem te illustreren. Ik kan geen RSA probleem selecteren dat als Hard beschouwd zou worden onder de bovenstaande voorwaarden, omdat de getallen dan onhandig zouden zijn. In plaats daarvan is dit voorbeeld alleen bedoeld om te illustreren hoe het RSA probleem in het algemeen werkt.


Om te beginnen, stel dat je twee willekeurige priemgetallen 13 en 31 kiest. Dus $p = 13$ en $q = 31$. Het product $N$ van deze twee priemgetallen is gelijk aan 403. We kunnen eenvoudig de orde van 403 berekenen. Dit komt overeen met $(13 - 1) ≤ (31 - 1) = 360$.


Vervolgens moeten we, zoals voorgeschreven in stap 3 van het RSA probleem, een coprime voor 360 kiezen die groter is dan 2 en kleiner dan 360. We hoeven deze waarde niet willekeurig te kiezen. We hoeven deze waarde niet willekeurig te kiezen. Stel dat we 103 kiezen. Dit is een coprime van 360 omdat de grootste gemene deler met 103 1 is.


Stap 4 vereist nu dat we een waarde $d$ berekenen zodat $103 \dot d \mod 360 = 1$. Dit is niet eenvoudig met de hand als de waarde voor $N$ groot is. Hiervoor moeten we een procedure gebruiken die het **uitgebreide algoritme van Euclides** heet.


Hoewel ik de procedure hier niet laat zien, levert het de waarde 7 op als $e = 103$. Je kunt controleren of het paar waarden 103 en 7 inderdaad voldoet aan de algemene voorwaarde $e \dot d \mod \phi(n) = 1$ door middel van onderstaande berekeningen.



- $103 \dot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$


Belangrijk is dat we, gegeven *stelling 4*, weten dat geen enkel ander geheel getal tussen 1 en 360 voor $d$ het resultaat geeft dat $103 \dot d = 1 \mod 360$. Bovendien impliceert de stelling dat een andere waarde voor $e$ een andere unieke waarde voor $d$ oplevert.


In stap 5 van het RSA-probleem moeten we een positief geheel getal $y$ kiezen dat een kleinere coprime is van 403. Stel dat we $y = 2^{103}$ kiezen. Exponentiëren van 2 door 103 geeft het onderstaande resultaat.



- $2^{103} \mod 403 = 10.141.204.801.825.835.211.973.625.643.008 \mod 403 = 349 \mod 403$


Het RSA-probleem in dit specifieke voorbeeld ziet er nu als volgt uit: Je krijgt $N = 403$, $e = 103$ en $y = 349 \mod 403$. Je moet nu $x$ zo berekenen dat $x^{103} = 349 \mod 403$. Dat wil zeggen dat je moet vinden dat de oorspronkelijke waarde vóór de exponentiatie met 103$ 2 was.


Het zou gemakkelijk zijn (voor een computer tenminste) om $x$ te berekenen als we wisten dat $d = 7$. In dat geval zou je gewoon $x$ kunnen bepalen zoals hieronder.



- $x = y^7 \mod 403 = 349^7 \mod 403 = 630.634.881.591.804.949 \mod 403 = 2 \mod 403$


Het probleem is dat je niet de informatie hebt gekregen dat $d = 7$. Je zou natuurlijk $d$ kunnen berekenen uit het feit dat $103 \dot d = 1 \mod 360$. Het probleem is dat je ook niet de informatie hebt gekregen dat de orde van $N = 360$. Tenslotte zou je ook de volgorde van 403 kunnen berekenen door het volgende product te berekenen: $(p - 1) \cdot (q - 1)$. Maar je krijgt ook niet te horen dat $p = 13$ en $q = 31$.


Natuurlijk kan een computer het RSA probleem voor dit voorbeeld nog steeds relatief eenvoudig oplossen, omdat de priemgetallen in kwestie niet groot zijn. Maar als de priemgetallen erg groot worden, wordt het een praktisch onmogelijke taak.


We hebben nu het RSA probleem gepresenteerd, een set voorwaarden waaronder het Hard is en de onderliggende wiskunde. Hoe helpt dit alles bij asymmetrische cryptografie? Meer specifiek, hoe kunnen we de hardheid van het RSA probleem onder bepaalde voorwaarden omzetten in een versleutelingsschema of een schema voor digitale handtekeningen?


Eén benadering is om het RSA probleem te nemen en schema's te bouwen op een eenvoudige manier. Stel bijvoorbeeld dat je een set variabelen $\Pi$ hebt gegenereerd zoals beschreven in het RSA probleem en dat $p$ en $q$ voldoende groot zijn. U stelt uw openbare sleutel gelijk aan $(N, e)$ en deelt deze informatie met de wereld. Zoals hierboven beschreven, houdt u de waarden voor $p$, $q$, $\phi(n)$ en $d$ geheim. In feite is $d$ uw privésleutel.


Iemand die jou een bericht $m$ wil sturen dat een element is van $C_N$ kan dit eenvoudig als volgt versleutelen: $c = m^e \mod N$. (De cijfertekst $c$ is hier gelijk aan de waarde $y$ in het RSA-probleem.) Je kunt dit bericht eenvoudig ontcijferen door gewoon $c^d \mod N$ te berekenen.


Je zou op dezelfde manier een digitaal handtekeningschema kunnen maken. Stel dat je iemand een bericht $m$ wilt sturen met een digitale handtekening $S$. Je kunt dan gewoon $S = m^d \mod N$ instellen en het paar $(m,S)$ naar de ontvanger sturen. Iedereen kan de digitale handtekening verifiëren door te controleren of $S^e \mod N = m \mod N$. Een aanvaller zou het echter erg moeilijk hebben om een geldige $S$ voor een bericht te maken, aangezien hij geen $d$ bezit.


Helaas is het omzetten van wat op zichzelf een Hard probleem is, het RSA probleem, in een cryptografisch schema niet zo eenvoudig. Voor het eenvoudige versleutelingsschema kun je alleen kopiemgetallen van $N$ kiezen als berichten. Dan blijven er niet veel mogelijke berichten over, zeker niet genoeg voor standaard communicatie. Bovendien moeten deze berichten willekeurig gekozen worden. Dat lijkt wat onpraktisch. Tenslotte zal elk bericht dat twee keer gekozen wordt exact dezelfde cijfertekst opleveren. Dit is zeer onwenselijk in elk encryptieschema en voldoet aan geen enkele strenge moderne standaardopvatting van veiligheid in encryptie.


De problemen worden nog groter voor ons eenvoudige digitale handtekeningschema. Zoals het er nu voor staat, kan elke aanvaller gemakkelijk digitale handtekeningen vervalsen door eerst een coprime van $N$ te kiezen als handtekening en dan het overeenkomstige originele bericht te berekenen. Dit breekt duidelijk de eis van existentiële onvervalsbaarheid.


Desalniettemin kan het RSA probleem met een beetje slimme complexiteit gebruikt worden om een veilig openbaar sleutel encryptie schema en een veilig digitaal handtekening schema te maken. We zullen hier niet ingaan op de details van dergelijke constructies. [4] Belangrijk is echter dat deze extra complexiteit niets verandert aan het fundamentele onderliggende RSA probleem waarop deze schema's zijn gebaseerd.



**Noten:**


[4] Zie bijvoorbeeld Jonathan Katz en Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), pp. 410-32 over RSA-encryptie en pp. 444-41 voor RSA digitale handtekeningen.




# Laatste Sectie

<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>


## Beoordelingen

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>

<isCourseReview>true</isCourseReview>

## Eindexamen

<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusie

<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>

<isCourseConclusion>true</isCourseConclusion>