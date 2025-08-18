---
name: Introduktion till formell kryptografi
goal: En djupdykning i kryptografins vetenskap och praktik.
objectives: 

  - Utforska Beale-chiffer och moderna kryptografiska metoder för att förstå grundläggande och historiska begrepp inom kryptografi.
  - Fördjupa dig i talteori, grupper och fält för att behärska viktiga matematiska begrepp som ligger till grund för kryptografi.
  - Studera RC4 stream cipher och AES med en 128-bitars nyckel för att lära dig mer om symmetriska kryptografiska algoritmer.
  - Undersök RSA-kryptosystemet, nyckeldistribution och Hash-funktioner för att utforska asymmetrisk kryptografi.


---
# Djupdykning i kryptografi


Det är svårt att hitta många material som erbjuder en bra medelväg i kryptografiutbildningen.


Å ena sidan finns det långa, formella avhandlingar som egentligen bara är tillgängliga för dem som har en stark bakgrund inom matematik, logik eller någon annan formell disciplin. Å andra sidan finns det introduktioner på mycket hög nivå som egentligen döljer alltför många detaljer för den som är åtminstone lite nyfiken.


Denna introduktion till kryptografi försöker fånga mellanvägen. Även om den bör vara relativt utmanande och detaljerad för alla som är nya inom kryptografi, är det inte kaninhålet i en typisk grundläggande avhandling.


+++

# Inledning

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>


## Kursöversikt

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Välkommen till kursen CYP302!


Denna bok ger en djupdykning i kryptografins vetenskap och praktik. Där det är möjligt fokuserar den på konceptuell snarare än formell framställning av materialet.


Detta pedagogiska innehåll är anpassat från boken och repot [JWBurgers] (https://github.com/JWBurgers/An_Introduction_to_Cryptography). Författaren har vänligen tillåtit att det används i utbildningssyfte, men alla immateriella rättigheter ligger kvar hos den ursprungliga skaparen.


**Motivation och mål**


Det är svårt att hitta många material som erbjuder en bra medelväg i kryptografiutbildningen.


Å ena sidan finns det långa, formella avhandlingar som egentligen bara är tillgängliga för dem som har en stark bakgrund inom matematik, logik eller någon annan formell disciplin. Å andra sidan finns det introduktioner på mycket hög nivå som egentligen döljer alltför många detaljer för den som är åtminstone lite nyfiken.


Denna introduktion till kryptografi försöker fånga mellanvägen. Även om den bör vara relativt utmanande och detaljerad för alla som är nya inom kryptografi, är det inte kaninhålet i en typisk grundläggande avhandling.



**Målgrupp**


Den här boken är användbar för alla som vill ha mer än en ytlig förståelse av kryptografi, från utvecklare till den intellektuellt nyfikne. Om ditt mål är att behärska kryptografiområdet är den här boken också en bra utgångspunkt.



**Läsriktlinjer**


Boken innehåller för närvarande sju kapitel: "Vad är kryptografi?" (kapitel 1), "Matematiska grunder för kryptografi I" (kapitel 2), "Matematiska grunder för kryptografi II" (kapitel 3), "Symmetrisk kryptografi" (kapitel 4), "RC4 och AES" (kapitel 5), "Asymmetrisk kryptografi" (kapitel 6) och "RSA-kryptosystemet" (kapitel 7). Ett sista kapitel, "Cryptography in Practice", kommer fortfarande att läggas till. Det fokuserar på olika kryptografiska tillämpningar, inklusive transport Layer-säkerhet, onion-routing och Bitcoin:s värde Exchange-system.


Om du inte har en stark bakgrund i matematik är talteori förmodligen det svåraste ämnet i den här boken. Jag ger en översikt över det i kapitel 3, och det förekommer också i redogörelsen för AES i kapitel 5 och RSA-kryptosystemet i kapitel 7.


Om du verkligen kämpar med de formella detaljerna i dessa delar av boken rekommenderar jag att du nöjer dig med att läsa dem på en hög nivå första gången.



**Acknowledgements**


Den mest inflytelserika boken för att forma denna har varit Jonathan Katz och Yehuda Lindells _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL), 2015. En tillhörande kurs finns tillgänglig på Coursera under namnet "Cryptography"


De viktigaste ytterligare källor som har varit till hjälp för att skapa översikten i den här boken är Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar och Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) och [en kurs baserad på boken av Paar som heter "Introduction to Cryptography"] (https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); och Bruce Schneier, Applied Cryptography, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons).


Jag kommer endast att citera mycket specifik information och resultat som jag hämtat från dessa källor, men vill här erkänna min allmänna tacksamhetsskuld till dem.


För de läsare som vill söka mer avancerad kunskap om kryptografi efter denna introduktion rekommenderar jag starkt Katz och Lindells bok. Katz kurs på Coursera är något mer lättillgänglig än boken.



**Bidrag**


Titta gärna på [bidragsfilen i arkivet] (https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) för riktlinjer om hur du kan stödja projektet.



**Notation**


**Nyckelbegrepp:**


Nyckelbegrepp i grundböckerna introduceras genom att de görs fetstilta. Till exempel skulle introduktionen av Rijndael-chiffret som en nyckelterm se ut på följande sätt: **Rijndael-chiffer**.


Nyckelbegrepp definieras uttryckligen, såvida de inte är egennamn eller deras betydelse framgår tydligt av diskussionen.


En definition ges vanligtvis i samband med att en nyckelterm introduceras, men ibland är det mer praktiskt att vänta med definitionen till ett senare tillfälle.



**Betonade ord och fraser: **


Ord och fraser betonas med kursiv stil. Till exempel skulle frasen "Kom ihåg ditt lösenord" se ut på följande sätt: *Kom ihåg ditt lösenord*.



**Formal notation:**


Den formella notationen gäller främst variabler, slumpmässiga variabler och mängder.



- Variabler: Dessa anges vanligtvis bara med en gemen bokstav (t.ex. "x" eller "y"). Ibland skrivs de med stor bokstav för tydlighetens skull (t.ex. "M" eller "K").
- Slumpmässiga variabler: Dessa anges alltid med en versal bokstav (t.ex. "X" eller "Y")
- Uppsättningar: Dessa anges alltid med fetstilta versaler (t.ex. **S**)


Är du redo att utforska kryptografins fascinerande värld? Då kör vi!


# Vad är kryptografi?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>


## Beale-chiffren

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>


Låt oss börja vår undersökning av kryptografin med en av de mer charmiga och underhållande episoderna i dess historia: Beale-chiffren. [1]


Historien om Beale-chiffren är enligt min mening mer sannolik att vara fiktion än verklighet. Men det påstås att det gick till på följande sätt.


Under både vintern 1820 och 1822 bodde en man vid namn Thomas J. Beale på ett värdshus som ägdes av Robert Morriss i Lynchburg (Virginia). I slutet av Beales andra vistelse överlämnade han till Morriss en järnlåda med värdefulla papper för säker förvaring.


Några månader senare fick Morriss ett brev från Beale daterat den 9 maj 1822. I brevet betonades det stora värdet av innehållet i järnlådan och Morriss fick några instruktioner: om varken Beale eller någon av hans medarbetare någonsin kom för att hämta lådan, skulle han öppna den exakt tio år efter brevets datum (dvs. den 9 maj 1832). Några av pappren i lådan skulle vara skrivna med vanlig text. Flera andra skulle dock vara "obegripliga utan hjälp av en nyckel" Denna "nyckel" skulle alltså levereras till Morriss av en icke namngiven vän till Beale i juni 1832.


Trots de tydliga instruktionerna öppnade Morriss inte lådan i maj 1832 och Beales mystiske vän dök aldrig upp i juni samma år. Det dröjde ända till 1845 innan värdshusägaren till slut bestämde sig för att öppna lådan. I den hittade Morriss en anteckning som förklarade hur Beale och hans medarbetare hittat guld och silver i väst och grävt ner det, tillsammans med några smycken, för att skydda det. Dessutom innehöll lådan tre **krypteringstexter**, det vill säga texter skrivna i kod som kräver en **kryptografisk nyckel**, eller en hemlighet, och en tillhörande algoritm för att låsas upp. Processen att låsa upp en chiffertext kallas **dekryptering**, medan låsningsprocessen kallas **kryptering**. (Som förklaras i kapitel 3 kan termen chiffer ha olika betydelser. I namnet "Beale ciphers" är det en förkortning av ciphertexts)


De tre chiffertexter som Morriss hittade i järnlådan består var och en av en serie siffror åtskilda av kommatecken. Enligt Beales anteckning innehåller dessa chiffertexter var för sig uppgifter om skattens läge, skattens innehåll och en lista med namn på rättmätiga arvtagare till skatten och deras andelar (den senare informationen är relevant om Beale och hans medarbetare aldrig skulle komma att göra anspråk på lådan).


Morris försökte dekryptera de tre chiffertexterna i tjugo år. Detta skulle ha varit enkelt med nyckeln. Men Morris hade inte nyckeln och misslyckades med sina försök att återfå originaltexterna, eller **plaintexts** som de brukar kallas inom kryptografin.


Morriss närmade sig slutet av sitt liv och överlämnade lådan till en vän 1862. Denne vän publicerade därefter en pamflett 1885 under pseudonymen J.B. Ward. Den innehöll en beskrivning av lådans (påstådda) historia, de tre chiffertexterna och en lösning som han hade hittat för den andra chiffertexten. (Tydligen finns det en nyckel för varje chiffertext, och inte en nyckel som fungerar på alla tre chiffertexterna som Beale ursprungligen verkar ha föreslagit i sitt brev till Morriss)


Du kan se den andra chiffertexten i *Figur 2* nedan. [2] Nyckeln till denna chiffertext är Förenta staternas självständighetsförklaring. Dekrypteringsproceduren kommer ner till att tillämpa följande två regler:



- För varje tal n i chiffertexten, lokalisera det n:te ordet i USA:s självständighetsförklaring
- Ersätt siffran n med den första bokstaven i det ord du hittade



*Figur 1: Beale-chiffer nr. 2*


![Figure 1: Beale cipher no 2.](assets/Figure1-1.webp "Figure 1: Beale cipher no. 2")



Det första talet i den andra chiffertexten är t.ex. 115. Det 115:e ordet i självständighetsförklaringen är "instituted", så den första bokstaven i klartexten är "i" Chiffertexten anger inte direkt ordavstånd och versaler. Men efter att ha dekrypterat de första orden kan man logiskt dra slutsatsen att det första ordet i klartexten helt enkelt var "I" (Klartexten börjar med frasen "Jag har deponerat i grevskapet Bedford.")


Efter dekryptering ger det andra meddelandet en detaljerad beskrivning av skattens innehåll (guld, silver och juveler) och antyder att den var nedgrävd i järnkrukor och täckt med stenar i Bedford County (Virginia). Folk älskar mysterier och därför har stora ansträngningar lagts ned på att dekryptera de två andra Beale-chiffren, särskilt det som beskriver var skatten finns. Till och med olika framstående kryptografer har försökt sig på dem. Men än så länge har ingen lyckats dekryptera de två andra chiffertexterna.



**Noteringar:**


[1] För en bra sammanfattning av historien, se Simon Singh, *The Code Book*, Fourth Estate (London, 1999), s. 82-99. En kortfilm om historien gjordes av Andrew Allen 2010. Du hittar filmen, "The Thomas Beale Cipher", [på dess webbplats](http://www.thomasbealecipher.com/).


[2] Denna bild finns på Wikipedia-sidan för Beale-chiffren.



## Modern kryptografi

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>


Färgstarka historier som den om Beale-chiffren är det som de flesta av oss förknippar med kryptografi. Men modern kryptografi skiljer sig på minst fyra viktiga sätt från den här typen av historiska exempel.


För det första har kryptografi historiskt sett bara handlat om **hemlighet** (eller konfidentialitet). [3] Chiffertexter skulle skapas för att säkerställa att endast vissa parter kunde ta del av informationen i klartexterna, som i fallet med Beale-chiffer. För att ett krypteringsschema ska tjäna detta syfte väl bör dekryptering av chiffertexten endast vara möjlig om du har nyckeln.


Modern kryptografi handlar om ett bredare spektrum av teman än bara sekretess. Dessa teman omfattar främst (1) **meddelandeintegritet** - det vill säga att säkerställa att ett meddelande inte har ändrats; (2) **meddelandeautenticitet** - det vill säga att säkerställa att ett meddelande verkligen har kommit från en viss avsändare; och (3) **icke-avvisning** - det vill säga att säkerställa att en avsändare inte senare falskeligen kan förneka att hon har skickat ett meddelande. [4]


En viktig distinktion att hålla i minnet är därför mellan ett **krypteringsschema** och ett **kryptografiskt schema**. Ett krypteringsschema handlar bara om sekretess. Även om ett krypteringsschema är ett kryptografiskt schema, är det omvända inte sant. Ett kryptografiskt system kan också tjäna de andra huvudtemana för kryptografi, inklusive integritet, äkthet och oavvislighet.


Integriteten och autenticiteten är lika viktiga teman som sekretessen. Våra moderna kommunikationssystem skulle inte kunna fungera utan garantier för kommunikationens integritet och äkthet. Oavvislighet är också en viktig fråga, t.ex. för digitala kontrakt, men behövs inte lika ofta i kryptografiska tillämpningar som sekretess, integritet och autenticitet.


För det andra involverar klassiska krypteringssystem som Beale-chiffren alltid en nyckel som delas mellan alla berörda parter. Många moderna kryptografiska system involverar dock inte bara en, utan två nycklar: en **privat** och en **offentlig nyckel**. Medan den förstnämnda bör förbli privat i alla tillämpningar, är den sistnämnda vanligtvis allmänt känd (därav deras respektive namn). När det gäller kryptering kan den offentliga nyckeln användas för att kryptera meddelandet, medan den privata nyckeln kan användas för dekryptering.


Den del av kryptografin som handlar om system där alla parter delar en nyckel kallas **symmetrisk kryptografi**. Den enda nyckeln i ett sådant system kallas vanligtvis för **privat nyckel** (eller hemlig nyckel). Den gren av kryptografin som behandlar system som kräver ett privat-offentligt nyckelpar kallas **asymmetrisk kryptografi**. Dessa grenar kallas ibland också **kryptografi med privat nyckel** respektive **kryptografi med offentlig nyckel** (detta kan dock skapa förvirring eftersom kryptografiska system med offentlig nyckel också har privata nycklar).


Tillkomsten av asymmetrisk kryptografi i slutet av 1970-talet har varit en av de viktigaste händelserna i kryptografins historia. Utan den skulle de flesta av våra moderna kommunikationssystem, inklusive Bitcoin, inte vara möjliga, eller åtminstone mycket opraktiska.


Det är viktigt att notera att modern kryptografi inte enbart är en studie av kryptografiska system med symmetriska och assymetriska nycklar (även om det täcker en stor del av området). Kryptografi handlar till exempel också om Hash-funktioner och pseudorandomtalsgeneratorer, och du kan bygga applikationer på dessa primitiver som inte är relaterade till symmetrisk eller assymetrisk nyckelkryptografi.


För det tredje var klassiska krypteringsscheman, som de som användes i Beale-chiffren, mer konst än vetenskap. Deras upplevda säkerhet baserades till stor del på intuitioner om deras komplexitet. De patchades vanligtvis när man lärde sig en ny attack mot dem, eller släpptes helt och hållet om attacken var särskilt allvarlig. Modern kryptografi är dock en rigorös vetenskap med ett formellt, matematiskt tillvägagångssätt för både utveckling och analys av kryptografiska system. [5]


Specifikt är modern kryptografi inriktad på formella **säkerhetsbevis**. Varje bevis på säkerhet för ett kryptografiskt system sker i tre steg:


1.	En **kryptografisk definition av säkerhet**, dvs. en uppsättning säkerhetsmål och det hot som angriparen utgör.

2.	En redogörelse för eventuella matematiska antaganden om systemets beräkningskomplexitet. Ett kryptografiskt system kan t.ex. innehålla en generator för pseudotillfälliga tal. Även om vi inte kan bevisa att dessa existerar, kan vi anta att de gör det.

3.	En redogörelse för ett matematiskt **bevis på säkerhet** för systemet på grundval av det formella säkerhetsbegreppet och eventuella matematiska antaganden.


För det fjärde har kryptografi historiskt sett främst använts i militära sammanhang, men har kommit att genomsyra våra dagliga aktiviteter i den digitala tidsåldern. Oavsett om du gör bankärenden på nätet, postar inlägg på sociala medier, köper en produkt från Amazon med ditt kreditkort eller ger en vän Bitcoin i dricks är kryptografi en nödvändig förutsättning för vår digitala tidsålder.


Med tanke på dessa fyra aspekter av modern kryptografi kan vi beskriva modern **kryptografi** som den vetenskap som handlar om formell utveckling och analys av kryptografiska system för att säkra digital information mot angrepp från motståndare. [6] Säkerhet bör här förstås i vid bemärkelse som att förhindra attacker som skadar sekretess, integritet, autentisering och/eller oavvislighet i kommunikationer.


Kryptografi ses bäst som en underdisciplin till **cybersäkerhet**, som handlar om att förhindra stöld, skada och missbruk av datorsystem. Observera att många cybersäkerhetsproblem har liten eller endast delvis koppling till kryptografi.


Om ett företag t.ex. har dyra servrar lokalt kan det vara viktigt att skydda hårdvaran från stöld och skador. Även om detta är en cybersäkerhetsfråga har det lite att göra med kryptografi.


Ett annat exempel är **phishing-attacker** som är ett vanligt problem i vår moderna tid. Med dessa attacker försöker man lura människor via e-post eller något annat medium att lämna ifrån sig känslig information, t.ex. lösenord eller kreditkortsnummer. Kryptografi kan i viss mån hjälpa Address att motverka nätfiskeattacker, men en heltäckande strategi kräver mer än att bara använda lite kryptografi.



**Noteringar:**


[3] För att vara exakt har de viktigaste tillämpningarna av kryptografiska system handlat om sekretess. Barn använder t.ex. ofta enkla kryptografiska system för "skojs skull". I dessa fall är sekretess egentligen inget problem.


[4] Bruce Schneier, *Applied Cryptography*, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons), s. 2.


[5] Se Jonathan Katz och Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), särskilt s. 16-23, för en bra beskrivning.


[6] Jfr Katz och Lindell, ibid, s. 3. Jag tycker att deras beskrivning har vissa problem och presenterar därför en något annorlunda version av deras uttalande här.



## Öppen kommunikation

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>


Modern kryptografi är utformad för att ge säkerhetsgarantier i en miljö med **öppen kommunikation**. Om vår kommunikationskanal är så väl skyddad att tjuvlyssnare inte har någon chans att manipulera eller ens bara observera våra meddelanden, är kryptografi överflödigt. De flesta av våra kommunikationskanaler är dock knappast så välbevakade.


Ryggraden för kommunikation i den moderna världen är ett massivt nätverk av fiberoptiska kablar. Att ringa telefonsamtal, titta på TV och surfa på nätet i ett modernt hushåll är i allmänhet beroende av detta nätverk av fiberoptiska kablar (en liten andel kan vara helt beroende av sateliter). Det är sant att du kan ha olika dataförbindelser i ditt hem, t.ex. koaxialkabel, (asymmetrisk) digital abonnentlinje och fiberoptisk kabel. Men, åtminstone i den utvecklade världen, ansluts dessa olika datamedier snabbt utanför ditt hus till en nod i ett massivt nätverk av fiberoptiska kablar som förbinder hela världen. Undantag är vissa avlägsna områden i den utvecklade världen, t.ex. i USA och Australien, där datatrafiken fortfarande kan färdas långa sträckor via traditionella koppartelefonledningar.


Det skulle vara omöjligt att hindra potentiella angripare från att fysiskt komma åt detta kabelnätverk och dess stödjande infrastruktur. Faktum är att vi redan vet att de flesta av våra data fångas upp av olika nationella underrättelsetjänster vid viktiga korsningar på internet[7]. Det gäller allt från Facebook-meddelanden till webbadresser som du besöker.


Medan övervakning av data i stor skala kräver en kraftfull motståndare, till exempel en nationell underrättelsetjänst, kan angripare med endast små resurser enkelt försöka snoka på en mer lokal skala. Även om detta kan ske genom avlyssning av kablar är det mycket enklare att bara avlyssna trådlös kommunikation.


De flesta av våra lokala nätverksdata - oavsett om vi befinner oss hemma, på kontoret eller på ett kafé - färdas nu via radiovågor till trådlösa åtkomstpunkter på allt-i-ett-routrar, snarare än via fysiska kablar. En angripare behöver alltså inte mycket resurser för att fånga upp någon av dina lokala trafikflöden. Detta är särskilt oroande eftersom de flesta människor gör väldigt lite för att skydda de data som skickas över deras lokala nätverk. Dessutom kan potentiella angripare också rikta in sig på våra mobila bredbandsanslutningar, som 3G, 4G och 5G. All denna trådlösa kommunikation är ett enkelt mål för angripare.


Idén om att hålla kommunikationen hemlig genom att skydda kommunikationskanalen är därför en hopplöst illusorisk strävan för en stor del av den moderna världen. Allt vi vet berättigar till allvarlig paranoia: du bör alltid anta att någon lyssnar. Och kryptografi är det viktigaste verktyget vi har för att uppnå någon form av säkerhet i denna moderna miljö.



**Noteringar:**


[7] Se t.ex. Olga Khazan, "The creepy, long-standing practice of undersea cable tapping", *The Atlantic*, 16 juli 2013 (tillgänglig på [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).



# Matematiska grunder för kryptografi 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>



## Slumpmässiga variabler

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>


Kryptografi är beroende av matematik. Och om du vill bygga mer än en ytlig förståelse för kryptografi måste du vara bekväm med den matematiken.


I det här kapitlet introduceras de flesta av de grundläggande matematiska ämnen som du kommer att stöta på när du lär dig kryptografi. Ämnena inkluderar slumpmässiga variabler, modulooperationer, XOR-operationer och pseudotillfällighet. Du bör behärska materialet i dessa avsnitt för att få en förståelse av kryptografi som inte är ytlig.


Nästa avsnitt handlar om talteori, som är en mycket större utmaning.


### Slumpmässiga variabler


En slumpmässig variabel betecknas vanligtvis med en versal bokstav som inte är fet. Så till exempel kan vi prata om en slumpmässig variabel $X$, en slumpmässig variabel $Y$ eller en slumpmässig variabel $Z$. Detta är den notation som jag också kommer att använda från och med nu.


En **slumpvariabel** kan anta två eller flera möjliga värden, vart och ett med en viss positiv sannolikhet. De möjliga värdena anges i **utfallsuppsättningen**.


Varje gång du **samplar** en slumpmässig variabel drar du ett visst värde från dess utfallsuppsättning enligt de definierade sannolikheterna.


Låt oss ta ett enkelt exempel. Antag en variabel X som definieras på följande sätt:



- X har utfallsmängden $\{1,2\}$$


$$
Pr[X = 1] = 0.5
$$


$$
Pr[X = 2] = 0.5
$$


Det är lätt att se att $X$ är en slumpmässig variabel. För det första finns det två eller flera möjliga värden som $X$ kan anta, nämligen $1$ och $2$. För det andra har varje möjligt värde en positiv sannolikhet att inträffa när du gör ett stickprov på $X$, nämligen $0,5$.


Allt som krävs för en slumpmässig variabel är en utfallsuppsättning med två eller flera möjligheter, där varje möjlighet har en positiv sannolikhet att inträffa vid urvalet. I princip kan alltså en slumpmässig variabel definieras abstrakt, utan något sammanhang. I det här fallet kan man tänka sig att "provtagning" innebär att man genomför ett naturligt experiment för att fastställa värdet på den slumpmässiga variabeln.


Variabeln $X$ ovan definierades abstrakt. Du kan därför tänka dig att provtagning av variabeln $X$ ovan är som att singla slant och tilldela "2" för krona och "1" för klave. För varje urval av $X$ singlar du slant igen.


Alternativt kan du också tänka på att göra ett urval av $X$ som att kasta en rättvis tärning och tilldela "2" om tärningen landar på $1$, $3$ eller $4$, och tilldela "1" om tärningen landar på $2$, $5$ eller $6$. Varje gång du gör ett urval på $X$ kastar du tärningen igen.


Egentligen kan alla naturliga experiment som skulle göra det möjligt för dig att definiera sannolikheterna för de möjliga värdena på $X$ ovan föreställas med avseende på ritningen.


Ofta introduceras dock slumpmässiga variabler inte bara abstrakt. Istället har uppsättningen av möjliga utfallsvärden en uttrycklig betydelse i verkligheten (snarare än bara som siffror). Dessutom kan dessa utfallsvärden definieras mot någon specifik typ av experiment (snarare än som ett naturligt experiment med dessa värden).


Låt oss nu ta ett exempel på variabeln $X$ som inte är abstrakt definierad. X definieras på följande sätt för att avgöra vilket av två lag som startar en fotbollsmatch:



- $X$ har utfallsmängden {röd sparkar av,blå sparkar av}
- Vänd ett visst mynt $C$: klave = "röd sparkar av"; krona = "blå sparkar av"


$$
Pr [X = \text{red kicks off}] = 0.5
$$


$$
Pr [X = \text{blue kicks off}] = 0.5
$$


I det här fallet ges utfallsuppsättningen X en konkret innebörd, nämligen vilket lag som startar i en fotbollsmatch. Dessutom bestäms de möjliga utfallen och deras tillhörande sannolikheter av ett konkret experiment, nämligen att singla slant med ett visst mynt $C$.


I diskussioner om kryptografi introduceras slumpmässiga variabler vanligtvis mot en resultatuppsättning med verklig betydelse. Det kan vara uppsättningen av alla meddelanden som kan krypteras, det så kallade meddelandeutrymmet, eller uppsättningen av alla nycklar som parterna som använder krypteringen kan välja mellan, det så kallade nyckelutrymmet.


Slumpmässiga variabler i diskussioner om kryptografi definieras dock vanligtvis inte mot något specifikt naturligt experiment, utan mot alla experiment som kan ge rätt sannolikhetsfördelning.


Slumpvariabler kan ha diskreta eller kontinuerliga sannolikhetsfördelningar. Slumpvariabler med en **diskret sannolikhetsfördelning** - det vill säga diskreta slumpvariabler - har ett begränsat antal möjliga utfall. Den slumpmässiga variabeln $X$ i båda exemplen hittills var diskret.


**Kontinuerliga slumpvariabler** kan istället anta värden i ett eller flera intervall. Man kan t.ex. säga att en slumpmässig variabel vid urvalet kommer att anta vilket verkligt värde som helst mellan 0 och 1, och att varje verkligt tal i detta intervall är lika sannolikt. Inom detta intervall finns det oändligt många möjliga värden.


För kryptografiska diskussioner behöver du bara förstå diskreta slumpvariabler. Alla diskussioner om slumpvariabler hädanefter bör därför förstås som hänvisningar till diskreta slumpvariabler, om inte annat uttryckligen anges.



### Grafisk framställning av slumpmässiga variabler


De möjliga värdena och tillhörande sannolikheter för en slumpmässig variabel kan enkelt visualiseras med hjälp av en graf. Tänk till exempel på den slumpmässiga variabeln $X$ från föregående avsnitt med en utfallsuppsättning på $\{1, 2\}$ och $Pr [X = 1] = 0,5$ och $Pr [X = 2] = 0,5$. Vi skulle vanligtvis visa en sådan slumpmässig variabel i form av ett stapeldiagram som i *Figur 1*.


*Figur 1: Slumpmässig variabel X*


![Figure 1: Random variable X.](assets/Figure2-1.webp)


De breda staplarna i *Figur 1* antyder uppenbarligen inte att den slumpmässiga variabeln $X$ faktiskt är kontinuerlig. Istället har staplarna gjorts breda för att vara mer visuellt tilltalande (bara en linje rakt upp ger en mindre intuitiv visualisering).



### Enhetliga variabler


I uttrycket "slumpmässig variabel" betyder termen "slumpmässig" bara "probabilistisk". Med andra ord betyder det bara att två eller flera möjliga utfall av variabeln inträffar med vissa sannolikheter. Dessa utfall behöver dock *inte nödvändigtvis* vara lika sannolika (även om termen "slumpmässig" faktiskt kan ha den betydelsen i andra sammanhang).


En **uniform variabel** är ett specialfall av en slumpmässig variabel. Den kan anta två eller flera värden som alla har samma sannolikhet. Den slumpmässiga variabeln $X$ som visas i *Figur 1* är helt klart en enhetlig variabel, eftersom båda de möjliga utfallen inträffar med sannolikheten $0,5$. Det finns dock många slumpmässiga variabler som inte är instanser av enhetliga variabler.


Tänk till exempel på den slumpmässiga variabeln $Y$. Den har en utfallsuppsättning {1, 2, 3, 8, 10} och följande sannolikhetsfördelning:


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



Även om två möjliga utfall har lika stor sannolikhet att inträffa, nämligen $1$ och $8$, kan $Y$ också anta vissa värden med andra sannolikheter än $0,25$ vid stickprov. Även om $Y$ är en slumpmässig variabel är den alltså inte en enhetlig variabel.


En grafisk beskrivning av $Y$ finns i *Figure 2*.


*Figur 2: Slumpmässig variabel Y*


![Figure 2: Random variable Y.](assets/Figure2-2.webp "Figure 2: Random variable Y")


Som ett sista exempel kan vi betrakta den slumpmässiga variabeln Z. Den har utfallsuppsättningen {1,3,7,11,12} och följande sannolikhetsfördelning:


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


Du kan se den avbildad i *Figur 3*. Den slumpmässiga variabeln Z är, till skillnad från Y, en enhetlig variabel, eftersom alla sannolikheter för de möjliga värdena vid urvalet är lika stora.



*Figur 3: Slumpmässig variabel Z*


![Figure 3: Random variable Z.](assets/Figure2-3.webp "Figure 3: Random variable Z")



### Villkorlig sannolikhet


Antag att Bob har för avsikt att på ett enhetligt sätt välja en dag från det senaste kalenderåret. Hur stor är sannolikheten för att den valda dagen infaller under sommaren?


Så länge vi tror att Bob:s process verkligen kommer att vara helt enhetlig, bör vi dra slutsatsen att det finns en 1/4 sannolikhet för att Bob väljer en dag på sommaren. Detta är den **ovillkorliga sannolikheten** för att den slumpmässigt valda dagen infaller under sommaren.


Antag nu att Bob istället för att enhetligt välja en kalenderdag, endast väljer enhetligt bland de dagar då middagstemperaturen vid Crystal Lake (New Jersey) var 21 grader Celcius eller högre. Med tanke på denna ytterligare information, vad kan vi då dra för slutsats om sannolikheten för att Bob väljer en dag under sommaren?


Vi borde egentligen dra en annan slutsats än tidigare, även utan någon ytterligare specifik information (t.ex. temperaturen vid middagstid varje dag förra kalenderåret).


Med tanke på att Crystal Lake ligger i New Jersey skulle vi verkligen inte förvänta oss att temperaturen vid middagstid är 21 grader Celsius eller högre på vintern. Istället är det mycket mer troligt att det är en varm dag på våren eller hösten, eller en dag någonstans på sommaren. Om man vet att middagstemperaturen vid Crystal Lake den valda dagen var 21 grader Celsius eller högre, blir sannolikheten för att den dag som Bob väljer är på sommaren mycket högre. Detta är den **villkorliga sannolikheten** för att den slumpmässigt valda dagen är på sommaren, givet att middagstemperaturen vid Crystal Lake var 21 grader Celsius eller högre.


Till skillnad från i det föregående exemplet kan sannolikheterna för två händelser också vara helt oberoende av varandra. I så fall säger vi att de är **oberoende**.


Antag t.ex. att ett visst rättvist mynt har slagit krona. Vad är då sannolikheten för att det kommer att regna i morgon, givet detta faktum? Den villkorliga sannolikheten i detta fall bör vara densamma som den ovillkorliga sannolikheten för att det ska regna i morgon, eftersom en slantsingling i allmänhet inte har någon inverkan på vädret.


Vi använder en "|"-symbol för att skriva ut villkorliga sannolikhetssatser. Till exempel kan sannolikheten för händelse $A$ givet att händelse $B$ har inträffat skrivas på följande sätt:


$$
Pr[A|B]
$$


Så, när två händelser, $A$ och $B$, är oberoende, då:


$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$


Villkoret för oberoende kan förenklas på följande sätt:


$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$



Ett viktigt resultat inom sannolikhetsteorin är känt som **Bayes teorem**. Den säger i princip att $Pr[A|B]$ kan skrivas om enligt följande:



$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$



I stället för att använda villkorliga sannolikheter för specifika händelser kan vi också titta på de villkorliga sannolikheter som gäller för två eller flera slumpmässiga variabler över en uppsättning möjliga händelser. Antag två slumpmässiga variabler, $X$ och $Y$. Vi kan beteckna alla möjliga värden för $X$ med $x$ och alla möjliga värden för $Y$ med $y$. Vi kan då säga att två slumpmässiga variabler är oberoende om följande påstående gäller:


$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$


för alla $x$ och $y$.


Låt oss vara lite tydligare med vad detta påstående innebär.


Antag att utfallsuppsättningarna för $X$ och $Y$ definieras enligt följande: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ och **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Det är vanligt att ange uppsättningar av värden med fetstilta versaler)


Anta nu att du gör ett urval på $Y$ och observerar $y_1$. Uttalandet ovan säger oss att sannolikheten för att nu få $x_1$ från provtagningen $X$ är exakt densamma som om vi aldrig hade observerat $y_1$. Detta gäller för alla $y_i$ som vi kunde ha dragit från vår ursprungliga provtagning av $Y$. Slutligen gäller detta inte bara för $x_1$. För alla $x_i$ påverkas sannolikheten för att de inträffar inte av resultatet av en provtagning av $Y$. Allt detta gäller också för det fall där $X$ samplas först.


Låt oss avsluta vår diskussion på en lite mer filosofisk punkt. I alla situationer i den verkliga världen bedöms sannolikheten för en viss händelse alltid mot bakgrund av en viss uppsättning information. Det finns ingen "ovillkorlig sannolikhet" i någon mycket strikt mening av ordet.


Anta till exempel att jag frågar dig om sannolikheten för att grisar kommer att flyga år 2030. Även om jag inte ger dig någon ytterligare information vet du uppenbarligen en hel del om världen som kan påverka din bedömning. Du har aldrig sett grisar flyga. Du vet att de flesta människor inte förväntar sig att de ska flyga. Du vet att de egentligen inte är byggda för att flyga. Och så vidare.


När vi talar om en "ovillkorlig sannolikhet" för någon händelse i ett verkligt sammanhang kan den termen därför bara ha betydelse om vi tolkar den som något i stil med "sannolikheten utan någon ytterligare explicit information". Varje förståelse av en "villkorlig sannolikhet" bör därför alltid förstås mot bakgrund av någon specifik information.


Jag kan till exempel fråga dig om sannolikheten för att grisar kommer att flyga 2030, efter att ha gett dig bevis för att vissa getter i Nya Zeeland har lärt sig flyga efter några års träning. I så fall kommer du förmodligen att justera din bedömning av sannolikheten för att grisar kommer att flyga år 2030. Sannolikheten för att grisar kommer att flyga år 2030 är alltså villkorad av detta bevis om getter i Nya Zeeland.



## Modulooperationen

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>


### Modulo


Det mest grundläggande uttrycket med **modulo-operationen** är av följande form: $x \mod y$.


Variabeln $x$ kallas dividend och variabeln $y$ divisor. För att utföra en modulooperation med en positiv dividend och en positiv divisor, bestämmer du bara resten av divisionen.


Tänk till exempel på uttrycket $25 \mod 4$. Talet 4 går in i talet 25 totalt 6 gånger. Återstoden av den divisionen är 1. Därför är $25 \ mod 4$ lika med 1. På liknande sätt kan vi utvärdera uttrycken nedan:



- $29 \mod 30 = 29$ (eftersom 30 går in i 29 totalt 0 gånger och återstoden är 29)
- 42 $ \mod 2 = 0 $ (eftersom 2 går in i 42 totalt 21 gånger och återstoden är 0)
- 12 $ \mod 5 = 2 $ (eftersom 5 går in i 12 totalt 2 gånger och återstoden är 2)
- 20 $ \ mod 8 = 4 $ (eftersom 8 går in i 20 totalt 2 gånger och återstoden är 4)


När dividenden eller divisorn är negativ kan modulooperationer hanteras på olika sätt i olika programspråk.


Du kommer definitivt att stöta på fall med en negativ utdelning i kryptografi. I dessa fall är det typiska tillvägagångssättet följande:



- Bestäm först det närmaste värdet som är *lägre än eller lika med* dividenden och som divisorn delar med en rest på noll. Kalla det värdet $p$.
- Om utdelningen är $x$, är resultatet av modulooperationen värdet av $x - p$.


Anta till exempel att utdelningen är $-20$ och divisorn 3. Det närmaste värde som är lägre än eller lika med $-20$ och som 3 delar jämnt i är $-21$. Värdet av $x - p$ är i detta fall $-20 - (-21)$. Detta är lika med 1 och därmed är $-20 \mod 3$ lika med 1. På liknande sätt kan vi utvärdera uttrycken nedan:



- $-8 \mod 5 = 2$
- $-19 \mod 16 = 13$
- $-14 \mod 6 = 4$


När det gäller notation kommer du vanligtvis att se följande typer av uttryck: $x = [y \mod z]$. På grund av parenteserna gäller modulo-operationen i det här fallet endast höger sida av uttrycket. Om $y$ är lika med 25 och $z$ är lika med 4, till exempel, så utvärderas $x$ till 1.


Utan parenteser verkar modulo-operationen på *båda sidor* av ett uttryck. Antag till exempel följande uttryck: $x = y \mod z$. Om $y$ är lika med 25 och $z$ är lika med 4, så vet vi bara att $x \mod 4$ utvärderas till 1. Detta är förenligt med alla värden för $x$ från uppsättningen $\{\ldots,-7, -3, 1, 5, 9,\ldots\}$.


Den gren av matematiken som omfattar modulooperationer på tal och uttryck kallas **modulär aritmetik**. Du kan se den här grenen som aritmetik för fall där tallinjen inte är oändligt lång. Även om vi vanligtvis stöter på modulooperationer för (positiva) heltal inom kryptografi, kan du också utföra modulooperationer med alla reella tal.


### Skiftchiffer


Modulo-operationen förekommer ofta inom kryptografi. För att illustrera detta kan vi titta på ett av de mest kända historiska krypteringssystemen: skiftchiffret.


Låt oss först definiera det. Antag en ordbok *D* som likställer alla bokstäver i det engelska alfabetet, i ordningsföljd, med taluppsättningen $\{0, 1, 2, \ldots, 25\}$. Antag ett meddelandeutrymme **M**. **shift-chiffer** är då ett krypteringsschema som definieras enligt följande:



- Välj enhetligt en nyckel $k$ ur nyckelrymden **K**, där **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Kryptera ett meddelande $m \in \mathbf{M}$, enligt följande:
    - Dela upp $m$ i dess enskilda bokstäver $m_0, m_1, \ldots, m_i, \ldots, m_l$
    - Konvertera varje $m_i$ till ett tal enligt *D*
    - För varje $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Konvertera varje $c_i$ till en bokstav enligt *D*
    - Kombinera sedan $c_0, c_1, \ldots, c_l$ för att få fram chiffertexten $c$
- Dekryptera en chiffertext $c$ enligt följande:
    - Konvertera varje $c_i$ till ett tal enligt *D*
    - För varje $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Omvandla varje $m_i$ till en bokstav enligt *D*
    - Kombinera sedan $m_0, m_1, \ldots, m_l$ för att få fram det ursprungliga meddelandet $m$


Modulooperatorn i skiftchiffret säkerställer att bokstäverna omsluter varandra, så att alla chiffertextbokstäver definieras. För att illustrera, överväg tillämpningen av skiftchiffret på ordet "DOG".


Antag att du på ett enhetligt sätt har valt en nyckel med värdet 17. Bokstaven "O" motsvarar 15. Utan modulo-operationen skulle tillägget av detta klartextnummer med nyckeln uppgå till ett chiffertextnummer på 32. Detta chiffertextnummer kan dock inte omvandlas till en chiffertextbokstav, eftersom det engelska alfabetet bara har 26 bokstäver. Modulooperationen säkerställer att chiffertextnumret faktiskt är 6 (resultatet av $32 \mod 26$), vilket motsvarar chiffertextbokstaven "G".


Hela krypteringen av ordet "DOG" med ett nyckelvärde på 17 är som följer:



- Meddelande = DOG = D,O,G = 3,15,6
- $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
- $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
- $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
- $c = UGX$$


Alla kan intuitivt förstå hur skiftchiffret fungerar och förmodligen använda det själva. För att utveckla din kunskap om kryptografi är det dock viktigt att börja bli mer bekväm med formalisering, eftersom systemen blir mycket svårare. Därför formaliserades stegen för skiftchiffret.



**Noteringar:**


[1] Vi kan definiera detta påstående exakt med hjälp av terminologin från föregående avsnitt. Låt en enhetlig variabel $K$ ha $K$ som sin uppsättning av möjliga utfall. I så fall


$$
Pr[K = 0] = \frac{1}{26}
$$


$$
Pr[K = 1] = \frac{1}{26}
$$


...och så vidare. Provta den enhetliga variabeln $K$ en gång för att få fram en viss nyckel.



## XOR-operationen

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>


Alla datauppgifter bearbetas, lagras och skickas över nätverk på bitnivå. Alla kryptografiska system som används för att kryptera datauppgifter fungerar också på bitnivå.


Anta t.ex. att du har skrivit ett e-postmeddelande i din e-postapplikation. Den kryptering du använder sker inte direkt på ASCII-tecknen i ditt e-postmeddelande. Istället tillämpas den på bit-representationen av bokstäverna och andra symboler i ditt e-postmeddelande.


En viktig matematisk operation att förstå för modern kryptografi, förutom modulo-operationen, är **XOR-operationen**, eller "exklusiv eller"-operationen. Denna operation tar som input två bitar och ger som output en annan bit. XOR-operationen benämns helt enkelt "XOR". Den ger 0 om de två bitarna är desamma och 1 om de två bitarna är olika. Du kan se de fyra möjligheterna nedan. Symbolen $\oplus$ representerar "XOR" :



- $0 \oplus 0 = 0$
- 0 $ \oplus 1 = 1 $
- $1 \oplus 0 = 1$
- $1 \oplus 1 = 0$


För att illustrera detta, anta att du har ett meddelande $m_1$ (01111001) och ett meddelande $m_2$ (01011001). XOR-operationen för dessa två meddelanden kan ses nedan.



- $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$


Processen är okomplicerad. Du XOR först de längst till vänster bitarna i $m_1 $ och $m_2 $. I det här fallet är det $0 \oplus 0 = 0$. Du XOR sedan det andra paret av bitar från vänster. I det här fallet är det $1 \oplus 1 = 0$. Du fortsätter denna process tills du har utfört XOR-operationen på bitarna längst till höger.


Det är lätt att se att XOR-operationen är kommutativ, nämligen att $m_1 \oplus m_2 = m_2 \oplus m_1$. Dessutom är XOR-operationen också associativ. Det vill säga $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.


En XOR-operation på två strängar av olika längd kan tolkas på olika sätt beroende på sammanhanget. Vi kommer här inte att beröra några XOR-operationer på strängar av olika längd.


En XOR-operation är likvärdig med specialfallet att utföra en modulooperation på addition av bitar när divisorn är 2. Du kan se likvärdigheten i följande resultat:



- $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
- $(1 + 0) \mod 2 = 1 \oplus 0 = 1$$
- $(0 + 1) \mod 2 = 0 \oplus 1 = 1$$
- $(1 + 1) \mod 2 = 1 \oplus 1 = 0$$


## Pseudorandomlighet

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>


I vår diskussion om slumpmässiga och enhetliga variabler gjorde vi en specifik åtskillnad mellan "slumpmässig" och "enhetlig". Denna distinktion upprätthålls vanligtvis i praktiken när man beskriver slumpmässiga variabler. I vårt nuvarande sammanhang måste dock denna distinktion tas bort och "slumpmässig" och "enhetlig" används synonymt. Jag kommer att förklara varför i slutet av avsnittet.


Till att börja med kan vi kalla en binär sträng med längden $n$ för **slumpmässig** (eller **uniform**) om den är resultatet av ett urval av en uniform variabel $S$ som ger varje binär sträng med längden $n$ samma sannolikhet att väljas.


Antag till exempel mängden av alla binära strängar med längden 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Det är typiskt att skriva en 8-bitars sträng i två kvartetter, var och en kallad **nibble**) Låt oss kalla denna uppsättning strängar **$S_8$**.


Enligt definitionen ovan kan vi kalla en viss binär sträng med längden 8 slumpmässig (eller enhetlig) om den är resultatet av ett urval av en enhetlig variabel $S$ som ger varje sträng i **$S_8$** lika stor sannolikhet att väljas. Med tanke på att uppsättningen **$S_8$** innehåller $2^8$ Elements, måste sannolikheten för urval vid provtagning vara $1/2^8$ för varje sträng i uppsättningen.


En viktig aspekt av slumpmässigheten hos en binär sträng är att den definieras med hänvisning till den process genom vilken den valdes ut. Formen på en viss binär sträng i sig avslöjar därför ingenting om dess slumpmässighet vid urvalet.


Många människor har till exempel den intuitiva uppfattningen att en sträng som $1111\ 1111$ inte kan ha valts slumpmässigt. Men detta är helt klart felaktigt.


Om man definierar en enhetlig variabel $S$ över alla binära strängar med längden 8, är sannolikheten att välja $1111\ 1111$ från uppsättningen **$S_8$** densamma som för en sträng som $0111\ 0100$. Det går alltså inte att säga något om en strängs slumpmässighet bara genom att analysera själva strängen.


Vi kan också tala om slumpmässiga strängar utan att specifikt mena binära strängar. Vi kan t.ex. tala om en slumpmässig hex-sträng $AF\ 02\ 82$. I det här fallet skulle strängen ha valts ut slumpmässigt från uppsättningen av alla hexsträngar med längden 6. Detta motsvarar att slumpmässigt välja en binär sträng med längden 24, eftersom varje hexsiffra representerar 4 bitar.


Vanligtvis avser uttrycket "en slumpmässig sträng", utan förbehåll, en sträng som slumpmässigt valts ut från mängden av alla strängar med samma längd. Det är så jag har beskrivit det ovan. En sträng med längden $n$ kan naturligtvis också slumpmässigt väljas från en annan uppsättning. En som till exempel bara utgör en delmängd av alla strängar med längden $n$, eller kanske en uppsättning som innehåller strängar av varierande längd. I dessa fall skulle vi dock inte tala om en "slumpmässig sträng", utan snarare om "en sträng som slumpmässigt valts ur någon uppsättning **S**".


Ett nyckelbegrepp inom kryptografi är pseudotillfällighet. En **pseudorandom sträng** av längden $n$ ser ut *som* den är resultatet av ett urval av en enhetlig variabel $S$ som ger varje sträng i **$S_n$** lika stor sannolikhet att väljas. I själva verket är dock strängen resultatet av ett urval av en enhetlig variabel $S'$ som endast definierar en sannolikhetsfördelning - inte nödvändigtvis en med lika sannolikheter för alla möjliga utfall - på en delmängd av **$S_n$**. Den avgörande punkten här är att ingen egentligen kan skilja mellan prov från $S$ och $S'$, även om du tar många av dem.


Antag till exempel en slumpmässig variabel $S$. Dess utfallsmängd är **$S_{256}$**, vilket är mängden av alla binära strängar med längden 256. Denna uppsättning har $2^{256}$ Elements. Varje element har en lika stor sannolikhet att väljas, $1/2^{256}$, vid urvalet.


Antag dessutom en slumpmässig variabel $S'$. Dess utfallsuppsättning innehåller endast $2^{128}$ binära strängar med längden 256. Den har en viss sannolikhetsfördelning över dessa strängar, men denna fördelning är inte nödvändigtvis enhetlig.


Anta att jag nu tar 1000-tals stickprov från $S$ och 1000-tals stickprov från $S'$ och ger dig de två uppsättningarna av utfall. Jag berättar vilken uppsättning utfall som är associerad med vilken slumpmässig variabel. Därefter tar jag ett prov från en av de två slumpmässiga variablerna. Men den här gången berättar jag inte vilken slumpmässig variabel jag tar ett stickprov från. Om $S'$ var pseudoslumpmässig är tanken att sannolikheten för att du ska gissa rätt om vilken slumpmässig variabel jag har valt ut praktiskt taget inte är bättre än $1/2$.


En pseudorandomsträng med längden $n$ produceras vanligtvis genom att slumpmässigt välja en sträng med storleken $n - x$, där $x$ är ett positivt heltal, och använda den som indata för en expansionsalgoritm. Denna slumpmässiga sträng av storleken $n - x$ kallas **seed**.


Pseudorandomsträngar är ett nyckelbegrepp för att göra kryptografi praktiskt. Tänk till exempel på strömchiffer. Med ett strömchiffer kopplas en slumpmässigt vald nyckel till en expansionsalgoritm för att producera en mycket större pseudotillfällig sträng. Denna pseudorandomsträng kombineras sedan med klartexten via en XOR-operation för att producera en chiffertext.


Om vi inte skulle kunna producera den här typen av pseudotillfälliga strängar för ett strömchiffer skulle vi behöva en nyckel som är lika lång som meddelandet för att det ska vara säkert. Detta är inte ett särskilt praktiskt alternativ i de flesta fall.


Begreppet pseudotillfällighet som diskuteras i detta avsnitt kan definieras mer formellt. Det kan också användas i andra sammanhang. Men vi behöver inte fördjupa oss i den diskussionen här. Allt du egentligen behöver förstå intuitivt för en stor del av kryptografin är skillnaden mellan en slumpmässig och en pseudo-slumpmässig sträng. [2]


Anledningen till att vi inte längre skiljer mellan "slumpmässig" och "enhetlig" i vår diskussion bör nu också vara tydlig. I praktiken använder alla termen pseudoslumpmässig för att beteckna en sträng som ser ut **som** den är resultatet av ett urval av en enhetlig variabel $S$. Strängt taget borde vi kalla en sådan sträng för "pseudouniform" och använda vårt språkbruk från tidigare. Eftersom termen "pseudouniform" är både klumpig och inte används av någon, kommer vi inte att introducera den här för tydlighetens skull. Istället släpper vi bara distinktionen mellan "slumpmässig" och "enhetlig" i det aktuella sammanhanget.



**Noter**


[2] Om du är intresserad av en mer formell redogörelse för dessa frågor kan du läsa Katz och Lindells *Introduction to Modern Cryptography *, särskilt kapitel 3.



# Matematiska grunder för kryptografi 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>



## Vad är talteori?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>


Detta kapitel behandlar ett mer avancerat ämne inom kryptografins matematiska grunder: talteori. Även om talteori är viktig för symmetrisk kryptografi (t.ex. i Rijndael-chiffret) är den särskilt viktig i kryptografi med publik nyckel.


Om du tycker att detaljerna i talteorin är besvärliga skulle jag rekommendera att du läser på en hög nivå första gången. Du kan alltid återkomma till det vid ett senare tillfälle.


___


Man kan beskriva **nummersteori** som studiet av egenskaperna hos heltal och matematiska funktioner som arbetar med heltal.


Tänk till exempel på att två tal $a$ och $N$ är **koprimtal** (eller **relativa primtal**) om deras största gemensamma divisor är lika med 1. Antag nu ett visst heltal $N$. Hur många heltal mindre än $N$ är coprim med $N$? Kan vi göra allmänna uttalanden om svaren på den här frågan? Det här är typiska frågor som talteorin försöker besvara.


Modern talteori förlitar sig på verktygen inom abstrakt algebra. Fältet **abstrakt algebra** är en underdisciplin inom matematiken där de huvudsakliga analysobjekten är abstrakta objekt som kallas algebraiska strukturer. En **algebraisk struktur** är en uppsättning Elements förenade med en eller flera operationer, som uppfyller vissa axiom. Genom algebraiska strukturer kan matematiker få insikter i specifika matematiska problem genom att abstrahera från deras detaljer.


Fältet abstrakt algebra kallas ibland också modern algebra. Du kanske också stöter på begreppet **abstrakt matematik** (eller **ren matematik**). Den senare termen är inte en referens till abstrakt algebra, utan betyder snarare att man studerar matematik för dess egen skull, och inte bara med tanke på potentiella tillämpningar.


Mängderna från abstrakt algebra kan hantera många typer av objekt, från formbevarande transformationer på en liksidig triangel till tapetmönster. För talteori tar vi bara hänsyn till uppsättningar av Elements som innehåller heltal eller funktioner som arbetar med heltal.



## Grupper

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>


Ett grundläggande begrepp inom matematiken är en uppsättning av Elements. En uppsättning betecknas vanligen med accoladtecken med Elements åtskilda av kommatecken.


Till exempel är uppsättningen av alla heltal $\{..., -2, -1, 0, 1, 2, ...\}$. Ellipserna här betyder att ett visst mönster fortsätter i en viss riktning. I uppsättningen av alla heltal ingår alltså även $3, 4, 5, 6$ och så vidare, liksom $-3, -4, -5, -6$ och så vidare. Denna mängd av alla heltal betecknas vanligen med $\mathbb{Z}$.


Ett annat exempel på en uppsättning är $\mathbb{Z} \mod 11$, eller mängden av alla heltal modulo 11. I motsats till hela mängden $\mathbb{Z}$ innehåller denna mängd endast ett ändligt antal Elements, nämligen $\{0, 1, \ldots, 9, 10\}$.


Ett vanligt misstag är att tro att mängden $\mathbb{Z} \mod 11$ faktiskt är $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Men detta är inte fallet, med tanke på hur vi definierade moduloperationen tidigare. Alla negativa heltal som reduceras med modulo 11 går in i $\{0, 1, \ldots, 9, 10\}$. Till exempel omsluter uttrycket $-2 \mod 11$ till $9$, medan uttrycket $-27 \mod 11$ omsluter till $5$.


Ett annat grundläggande begrepp inom matematiken är binär operation. Detta är en operation som tar två Elements för att producera en tredje. Från grundläggande aritmetik och algebra känner du till exempel till fyra grundläggande binära operationer: addition, subtraktion, multiplikation och division.


Dessa två grundläggande matematiska begrepp, mängder och binära operationer, används för att definiera begreppet grupp, den mest grundläggande strukturen i abstrakt algebra.


Antag närmare bestämt en binär operation $\circ$. Antag dessutom en uppsättning Elements **S** som är utrustad med den operationen. Allt "utrustad" betyder här är att operationen $\circ$ kan utföras mellan två valfria Elements i mängden **S**.


Kombinationen $\langle \mathbf{S}, \circ \rangle$ är alltså en **grupp** om den uppfyller fyra specifika villkor, de s.k. gruppaxiomen.


1. För alla $a$ och $b$ som är Elements i $\mathbf{S}$, är $a \circ b$ också ett element i $\mathbf{S}$. Detta är känt som **slutningsvillkoret**.

2. För alla $a$, $b$ och $c$ som är Elements av $\mathbf{S}$ gäller att $(a \circ b) \circ c = a \circ (b \circ c)$. Detta är känt som **associativitetsvillkoret**.

3. Det finns ett unikt element $e$ i $\mathbf{S}$, så att för varje element $a$ i $\mathbf{S}$ gäller följande ekvation: $e \circ a = a \circ e = a$. Eftersom det bara finns ett sådant element $e$ kallas det **identitetselement**. Detta villkor är känt som **identitetsvillkoret**.

4. För varje element $a$ i $\mathbf{S}$ finns det ett element $b$ i $\mathbf{S}$, så att följande ekvation gäller: $a \circ b = b \circ a = e$, där $e$ är identitetselementet. Elementet $b$ kallas här för det **inversa elementet**, och det betecknas vanligen som $a^{-1}$. Detta villkor är känt som det **inversa villkoret** eller **invertibilitetsvillkoret**.


Låt oss utforska grupper lite närmare. Beteckna uppsättningen av alla heltal med $\mathbb{Z}$. Denna mängd kombinerad med standardaddition, eller $\langle \mathbb{Z}, + \rangle$, passar tydligt in i definitionen av en grupp, eftersom den uppfyller de fyra axiomen ovan.


1. För alla $x$ och $y$ som är Elements i $\mathbb{Z}$, är $x + y$ också ett element i $\mathbb{Z}$. Så $\langle \mathbb{Z}, + \rangle$ uppfyller slutningsvillkoret.

2. För alla $x$, $y$ och $z$ som är Elements i $\mathbb{Z}$ gäller $(x + y) + z = x + (y + z)$. Så $\langle \mathbb{Z}, + \rangle$ uppfyller associativitetsvillkoret.

3. Det finns ett identitetselement i $\langle \mathbb{Z}, + \rangle$, nämligen 0. För varje $x$ i $\mathbb{Z}$ gäller nämligen att: $0 + x = x + 0 = x$. Så $\langle \mathbb{Z}, + \rangle$ uppfyller identitetsvillkoret.

4. Slutligen, för varje element $x$ i $\mathbb{Z}$, finns det ett $y$ så att $x + y = y + x = 0$. Om $x$ är 10, till exempel, skulle $y$ vara $-10$ (om $x$ är 0, är $y$ också 0). Så $\langle \mathbb{Z}, + \rangle$ uppfyller det inversa villkoret.


Det är viktigt att notera att det faktum att mängden heltal med addition utgör en grupp inte betyder att den utgör en grupp med multiplikation. Du kan verifiera detta genom att testa $\langle \mathbb{Z}, \cdot \rangle$ mot de fyra gruppaxiomen (där $\cdot$ betyder standardmultiplikation).


De två första axiomen gäller uppenbarligen. Vid multiplikation kan dessutom elementet 1 fungera som identitetselement. Varje heltal $x$ multiplicerat med 1 ger nämligen $x$. Men $\langle \mathbb{Z}, \cdot \rangle$ uppfyller inte det inversa villkoret. Det vill säga, det finns inte ett unikt element $y$ i $\mathbb{Z}$ för varje $x$ i $\mathbb{Z}$, så att $x \cdot y = 1$.


Antag till exempel att $x = 22$. Vilket värde $y$ från uppsättningen $\mathbb{Z}$ multiplicerat med $x$ skulle ge identitetselementet 1? Värdet $1/22$ skulle fungera, men det finns inte i uppsättningen $\mathbb{Z}$. Faktum är att du stöter på det här problemet för alla heltal $x$, förutom värdena 1 och -1 (där $y$ måste vara 1 respektive -1).


Om vi tillåter reella tal för vår uppsättning försvinner våra problem i stort sett. För varje element $x$ i uppsättningen ger multiplikation med $1/x$ 1. Eftersom bråk ingår i uppsättningen av reella tal kan en invers hittas för varje reellt tal. Undantaget är noll, eftersom multiplikation med noll aldrig kommer att ge identitetselementet 1. Mängden reella tal som inte är noll och som är utrustade med multiplikation är alltså en grupp.


Vissa grupper uppfyller ett femte allmänt villkor, det s.k. **kommutativitetsvillkoret**. Detta villkor är som följer:



- Antag en grupp $G$ med en mängd **S** och en binär operator $\circ$. Antag att $a$ och $b$ är Elements av **S**. Om det är så att $a \circ b = b \circ a$ för två valfria Elements $a$ och $b$ i **S**, så uppfyller $G$ kommutativitetsvillkoret.


En grupp som uppfyller kommutativitetsvillkoret kallas en **kommutativ grupp** eller en **Abelsk grupp** (efter Niels Henrik Abel). Det är lätt att verifiera att både mängden reella tal över addition och mängden heltal över addition är abelska grupper. Mängden heltal över multiplikation är inte alls en grupp och kan därför ipso facto inte vara en abelsk grupp. Mängden reella tal utan noll över multiplikation är däremot också en abelsk grupp.


Du bör ta hänsyn till två viktiga konventioner för notation. För det första kommer tecknen "+" eller "×" ofta att användas för att symbolisera gruppoperationer, även när Elements i själva verket inte är tal. I dessa fall ska du inte tolka dessa tecken som vanlig aritmetisk addition eller multiplikation. Istället är de operationer som endast har en abstrakt likhet med dessa aritmetiska operationer.


Om du inte specifikt hänvisar till aritmetisk addition eller multiplikation är det lättare att använda symboler som $\circ$ och $\diamond$ för gruppoperationer, eftersom dessa inte har särskilt kulturellt ingrodda konnotationer.


För det andra, av samma anledning som "+" och "×" ofta används för att ange icke-aritmetiska operationer, symboliseras identitets-Elements i grupper ofta med "0" och "1", även när Elements i dessa grupper inte är tal. Om du inte hänvisar till identitetselementet i en grupp med siffror är det lättare att använda en mer neutral symbol som "$e$" för att ange identitetselementet.


Många olika och mycket viktiga värdemängder inom matematiken som är utrustade med vissa binära operationer är grupper. Kryptografiska tillämpningar arbetar dock endast med mängder av heltal eller åtminstone Elements som beskrivs av heltal, det vill säga inom området för talteori. Mängder med andra reella tal än heltal används därför inte i kryptografiska tillämpningar.


Låt oss avsluta med att ge ett exempel på Elements som kan "beskrivas av heltal", trots att de inte är heltal. Ett bra exempel är punkterna på elliptiska kurvor. Även om varje punkt på en elliptisk kurva uppenbarligen inte är ett heltal, så beskrivs en sådan punkt faktiskt av två heltal.


Elliptiska kurvor är t.ex. avgörande för Bitcoin. Varje standardpar av privata och offentliga nycklar från Bitcoin väljs från den uppsättning punkter som definieras av följande elliptiska kurva:


$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$


(det största primtal som är mindre än $2^{256}$). Koordinaten $x$ är den privata nyckeln och koordinaten $y$ är din offentliga nyckel.


Transaktioner i Bitcoin innebär vanligtvis att utgångar låses till en eller flera publika nycklar på något sätt. Värdet från dessa transaktioner kan sedan låsas upp genom att göra digitala signaturer med motsvarande privata nycklar.




## Cykliska grupper

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>


En viktig distinktion vi kan göra är mellan en **ändlig** och en **oändlig grupp**. Den förstnämnda har ett ändligt antal Elements, medan den sistnämnda har ett oändligt antal Elements. Antalet Elements i en ändlig grupp kallas för gruppens **ordning**. All praktisk kryptografi som involverar användning av grupper förlitar sig på ändliga (talteoretiska) grupper.


Inom kryptografi med offentliga nycklar är en viss klass av ändliga abelska grupper, så kallade cykliska grupper, särskilt viktiga. För att förstå cykliska grupper måste vi först förstå begreppet exponentiering av gruppelement.


Antag en grupp $G$ med en gruppoperation $\circ$, och att $a$ är ett element i $G$. Uttrycket $a^n$ ska då tolkas som att elementet $a$ kombineras med sig själv totalt $n - 1$ gånger. Till exempel betyder $a^2$ $a \circ a$, $a^3$ betyder $a \circ a \circ a$, och så vidare. (Observera att exponentiering här inte nödvändigtvis är exponentiering i den vanliga aritmetiska bemärkelsen)


Låt oss ta ett exempel. Antag att $G = \langle \mathbb{Z} \mod 7, + \rangle$, och att vårt värde för $a$ är lika med 4. I detta fall är $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativt skulle $a^4$ representera $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.


Vissa abelska grupper har en eller flera Elements, som kan ge alla andra gruppers Elements genom fortsatt exponentiering. Dessa Elements kallas **generatorer** eller **primitiva Elements**.


En viktig klass av sådana grupper är $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, där $N$ är ett primtal. Notationen $\mathbb{Z}^*$ betyder här att gruppen innehåller alla positiva heltal utan noll som är mindre än $N$. En sådan grupp har därför alltid $N - 1$ Elements.


Betrakta till exempel $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Denna grupp har följande Elements: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Ordningsföljden för denna grupp är 10 (vilket faktiskt är lika med $11 - 1$).


Låt oss utforska exponentiering av elementet 2 från den här gruppen. Beräkningarna upp till $2^{12}$ visas nedan. Observera att exponenten på vänster sida av ekvationen hänvisar till exponentiering av gruppelement. I vårt speciella exempel handlar det faktiskt om aritmetisk exponentiering på höger sida av ekvationen (men det kunde också ha handlat om t.ex. addition). För att förtydliga har jag skrivit ut den upprepade operationen, snarare än exponentformen på höger sida.



- $2^1 = 2 \mod 11$$
- $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$$
- $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
- $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
- $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
- $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
- $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$$
- $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
- $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
- $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
- $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$


Om du tittar noga kan du se att exponentiering av elementet 2 cyklar genom alla Elements i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ i följande ordning: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Efter $2^{10}$ cyklar fortsatt exponentiering av elementet 2 genom alla Elements igen och i samma ordning. Därför är elementet 2 en generator i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.


Även om $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ har flera generatorer, så är inte alla Elements i denna grupp generatorer. Tänk till exempel på elementet 3. Om man går igenom de första 10 exponentieringarna, utan att visa de besvärliga beräkningarna, får man följande resultat:



- $3^1 = 3 \mod 11$
- $3^2 = 9 \mod 11$$
- $3^3 = 5 \mod 11$
- $3^4 = 4 \mod 11$
- $3^5 = 1 \mod 11$
- $3^6 = 3 \mod 11$
- $3^7 = 9 \mod 11$
- $3^8 = 5 \mod 11$
- $3^9 = 4 \mod 11$
- $3^{10} = 1 \mod 11$


Istället för att cykla igenom alla värden i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, leder exponentiering av elementet 3 bara till en delmängd av dessa värden: 3, 9, 5, 4 och 1. Efter den femte exponentieringen börjar dessa värden upprepas.


Vi kan nu definiera en **cyklisk grupp** som en grupp med minst en generator. Det vill säga, det finns minst ett gruppelement från vilket du kan producera alla andra grupp-Elements genom exponentiering.


Du kanske har lagt märke till i vårt exempel ovan att både $2^{10}$ och $3^{10}$ är lika med $1 \mod 11$. Faktum är, även om vi inte kommer att utföra beräkningarna, att exponentiering med 10 av alla element i gruppen $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ kommer att ge $1 \mod 11$. Varför är detta fallet?


Det är en viktig fråga, men det krävs en del arbete för att besvara den.


Till att börja med antar vi två positiva heltal $a$ och $N$. Ett viktigt teorem inom talteorin säger att $a$ har en multiplikativ invers modulo $N$ (det vill säga ett heltal $b$ så att $a \cdot b = 1 \mod N$) om och endast om den största gemensamma divisorn mellan $a$ och $N$ är lika med 1. Det vill säga om $a$ och $N$ är koprim.


Så för varje grupp av heltal som är utrustad med multiplikation modulo $N$ ingår endast de mindre coprimerna med $N$ i mängden. Vi kan beteckna denna uppsättning med $\mathbb{Z}^c \mod N$.


Anta till exempel att $N$ är 10. Endast heltalen 1, 3, 7 och 9 är koprim med 10. Mängden $\mathbb{Z}^c \mod 10$ innehåller alltså bara $\{1, 3, 7, 9\}$. Det går inte att skapa en grupp med heltalsmultiplikation modulo 10 med något annat heltal mellan 1 och 10. För just den här gruppen är inverserna paren 1 och 9 samt 3 och 7.


I det fall $N$ självt är primtal, är alla heltal från 1 till och med $N - 1$ coprimtal med $N$. En sådan grupp har alltså en ordning av $N - 1$. Med hjälp av vår tidigare notation är $\mathbb{Z}^c \mod N$ lika med $\mathbb{Z}^* \mod N$ när $N$ är primtal. Den grupp som vi valde för vårt tidigare exempel, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, är ett särskilt fall av denna klass av grupper.


Därefter beräknar funktionen $\phi(N)$ antalet koprim upp till ett tal $N$, och är känd som **Eulers Phi-funktion**. [1] Enligt **Eulers teorem** gäller följande när två heltal $a$ och $N$ är koprimtal:



- $a^{\phi(N)} \mod N = 1 \mod N$


Detta har en viktig implikation för klassen av grupper $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ där $N$ är primtal. För dessa grupper representerar exponentiering av gruppelement aritmetisk exponentiering. Det vill säga, $a^{\phi(N)} \mod N$ representerar den aritmetiska operationen $a^{\phi(N)} \mod N$. Eftersom varje element $a$ i dessa multiplikativa grupper är coprim med $N$, betyder det att $a^{\phi(N)} \mod N = a^{N - 1} \mod N = 1 \mod N$.


Eulers teorem är ett mycket viktigt resultat. Till att börja med innebär det att alla Elements i $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ bara kan cykla genom ett antal värden genom exponentiering som delar sig i $N - 1$. I fallet med $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ betyder detta att varje element bara kan cykla genom 2, 5 eller 10 Elements. De gruppvärden som ett element kan cykla igenom vid exponentiering kallas för elementets **ordning**. Ett element med en ordning som är likvärdig med ordningen i en grupp är en generator.


Vidare innebär Eulers sats att vi alltid kan veta resultatet av $a^{N - 1} \mod N$ för varje grupp $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ där $N$ är primtal. Detta gäller oavsett hur komplicerade de faktiska beräkningarna kan vara.


Anta till exempel att vår grupp är $\mathbb{Z}^* \mod 160,481,182$ (där 160,481,182 verkligen är ett primtal). Vi vet att alla heltal 1 till och med 160,481,181 måste vara Elements i denna grupp, och att $\phi(n) = 160,481,181$. Även om vi inte kan göra alla steg i beräkningarna, vet vi att uttryck som 514 $^{160,481,181}$, 2 005 $^{160,481,181}$ och 256 212 $^{160,481,181}$ alla måste utvärderas till 1 $ \mod 160,481,182$.


**Noteringar:**


[1] Funktionen fungerar på följande sätt. Varje heltal $N$ kan faktoriseras till en produkt av primtal. Antag att ett visst $N$ faktoreras på följande sätt: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ där alla $p$ är primtal och alla $e$ är heltal större än eller lika med 1. Då:


$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$


Eulers Phi-funktionsformel för primtalsfaktoriseringen av $N$.



## Fält

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>


En grupp är den grundläggande algebraiska strukturen i abstrakt algebra, men det finns många fler. Den enda andra algebraiska struktur som du behöver känna till är den för ett **fält**, särskilt för ett **ändligt fält**. Den här typen av algebraisk struktur används ofta inom kryptografi, t.ex. i Advanced Encryption Standard. Den senare är det huvudsakliga symmetriska krypteringsschemat som du kommer att stöta på i praktiken.


Ett fält är härlett från begreppet grupp. Specifikt är ett **fält** en uppsättning Elements **S** utrustad med två binära operatorer $\circ$ och $\diamond$, som uppfyller följande villkor:


1. Mängden **S** försedd med $\circ$ är en abelisk grupp.

2. Mängden **S** utrustad med $\diamond$ är en abelisk grupp för "icke-noll" Elements.

3. Mängden **S** som är utrustad med de två operatorerna uppfyller det så kallade distributiva villkoret: Antag att $a$, $b$ och $c$ är Elements av **S**. Då uppfyller **S** utrustad med de två operatorerna den distributiva egenskapen när $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.


Observera att definitionen av ett fält, precis som för grupper, är mycket abstrakt. Den gör inga påståenden om typerna av Elements i **S**, eller om operationerna $\circ$ och $\diamond$. Den säger bara att ett fält är varje uppsättning av Elements med två operationer för vilka de tre ovanstående villkoren gäller. (Elementet "noll" i den andra abelska gruppen kan tolkas abstrakt)


Så vad kan vara ett exempel på ett fält? Ett bra exempel är mängden $\mathbb{Z} \mod 7$, eller $\{0, 1, \ldots, 7\}$ definierad över standardaddition (i stället för $\circ$ ovan) och standardmultiplikation (i stället för $\diamond$ ovan).


För det första uppfyller $\mathbb{Z} \mod 7$ uppfylla villkoret för att vara en abelisk grupp över addition, och den uppfyller villkoret för att vara en abelisk grupp över multiplikation om man bara betraktar Elements som inte är noll. För det andra uppfyller kombinationen av mängden med de två operatörerna det distributiva villkoret.


Det är didaktiskt värdefullt att undersöka dessa påståenden genom att använda några särskilda värden. Låt oss ta de experimentella värdena 5, 2 och 3, några slumpmässigt utvalda Elements från uppsättningen $\mathbb{Z} \mod 7$, för att inspektera fältet $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Vi kommer att använda dessa tre värden i tur och ordning, efter behov för att undersöka särskilda förhållanden.


Låt oss först undersöka om $\mathbb{Z} \mod 7$ utrustad med addition är en abelisk grupp.


1. **Stängningsvillkor**: Låt oss ta 5 och 2 som våra värden. I så fall är $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Detta är verkligen ett element i $\mathbb{Z} \mod 7$, så resultatet är förenligt med stängningsvillkoret.

2. **Associativitetsvillkor**: Låt oss ta 5, 2 och 3 som våra värden. I så fall är $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Detta är förenligt med associativitetsvillkoret.

3. **Identitetsvillkor**: Låt oss ta 5 som vårt värde. I så fall blir $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Så 0 ser ut att vara identitetselementet för addition.

4. **Inversa villkor**: Betrakta inversen av 5. Det måste vara så att $[5 + d] \mod 7 = 0$, för ett visst värde på $d$. I det här fallet är det unika värdet från $\mathbb{Z} \mod 7$ som uppfyller detta villkor är 2.

5. **Kommutativitetsvillkor**: Låt oss ta 5 och 3 som våra värden. I så fall är $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Detta är förenligt med kommutativitetsvillkoret.


Mängden $\mathbb{Z} \mod 7$ utrustad med addition framstår tydligt som en abelisk grupp. Låt oss nu undersöka om $\mathbb{Z} \mod 7$ utrustad med multiplikation är en abelisk grupp för alla Elements som inte är noll.


1. **Stängningsvillkor**: Låt oss ta 5 och 2 som våra värden. I så fall är $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Detta är också ett element i $\mathbb{Z} \mod 7$, så resultatet är förenligt med stängningsvillkoret.

2. **Associativitetsvillkor**: Låt oss ta 5, 2 och 3 som våra värden. I så fall blir $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Detta är förenligt med associativitetsvillkoret.

3. **Identitetsvillkor**: Låt oss ta 5 som vårt värde. I så fall är $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Så 1 ser ut att vara identitetselementet för multiplikation.

4. **Inversa villkor**: Betrakta inversen av 5. Det måste vara så att $[5 \cdot d] \mod 7 = 1$, för något värde av $d$. Det unika värdet från $\mathbb{Z} \mod 7$ som uppfyller detta villkor är 3. Detta är förenligt med det inversa villkoret.

5. **Kommutativitetsvillkor**: Låt oss ta 5 och 3 som våra värden. I så fall blir $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Detta är förenligt med kommutativitetsvillkoret.


Mängden $\mathbb{Z} \mod 7$ verkar tydligt uppfylla reglerna för att vara en abelisk grupp när den kombineras med antingen addition eller multiplikation över Elements som inte är noll.


Slutligen verkar denna uppsättning kombinerad med båda operatörerna uppfylla det distributiva villkoret. Låt oss ta 5, 2 och 3 som våra värden. Vi kan se att $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.


Vi har nu sett att $\mathbb{Z} \mod 7$ utrustad med addition och multiplikation uppfyller axiomen för ett ändligt fält när vi testar med vissa värden. Naturligtvis kan vi också visa det generellt, men det gör vi inte här.


En viktig distinktion är mellan två typer av fält: ändliga och oändliga fält.


Ett **oändligt fält** innebär ett fält där mängden **S** är oändligt stor. Mängden reella tal $\mathbb{R}$ som är utrustade med addition och multiplikation är ett exempel på ett oändligt fält. Ett **ändligt fält**, även känt som ett **Galois-fält**, är ett fält där mängden **S** är ändlig. Vårt exempel ovan på $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ är ett ändligt fält.


Inom kryptografin är vi främst intresserade av ändliga fält. I allmänhet kan man visa att det finns ett finit fält för en viss uppsättning Elements **S** om och endast om den har $p^m$ Elements, där $p$ är ett primtal och $m$ ett positivt heltal större än eller lika med ett. Med andra ord, om ordningen för någon mängd **S** är ett primtal ($p^m$ där $m = 1$) eller någon primtalspotential ($p^m$ där $m > 1$), så kan du hitta två operatorer $\circ$ och $\diamond$ så att villkoren för ett fält uppfylls.


Om något finit fält har ett primtal av Elements, kallas det ett **primfält**. Om antalet Elements i det finita fältet är en primtalspotential kallas fältet för ett **extension field**. Inom kryptografi är vi intresserade av både primtals- och extensionsfält. [2]


De primtalsfält som är mest intressanta inom kryptografin är sådana där uppsättningen av alla heltal moduleras med något primtal och operatörerna är standardaddition och -multiplikation. Denna klass av finita fält skulle inkludera $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, och så vidare. För varje primtalsfält $\mathbb{Z} \mod p$ är fältets uppsättning av heltal enligt följande: $\{0, 1, \ldots, p - 2, p - 1\}$.


Inom kryptografin är vi också intresserade av utvidgningsfält, i synnerhet alla fält med $2^m$ Elements där $m > 1$. Sådana ändliga fält används t.ex. i Rijndael-chiffret, som utgör grunden för Advanced Encryption Standard. Medan primtalsfält är relativt intuitiva är dessa bas 2-tilläggsfält förmodligen inte något för den som inte är bekant med abstrakt algebra.


Till att börja med är det faktiskt sant att varje uppsättning heltal med $2^m$ Elements kan tilldelas två operatorer som skulle göra deras kombination till ett fält (så länge $m$ är ett positivt heltal). Men bara för att ett fält existerar betyder det inte nödvändigtvis att det är lätt att upptäcka eller särskilt praktiskt för vissa tillämpningar.


Det visar sig att särskilt tillämpliga utvidgningsfält för $2^m$ inom kryptografi är de som definieras över särskilda uppsättningar av polynomuttryck, snarare än någon uppsättning heltal.


Anta till exempel att vi ville ha ett utvidgningsfält med $2^3$ (dvs. 8) Elements i uppsättningen. Det kan finnas många olika uppsättningar som kan användas för fält av den storleken, men en sådan uppsättning innehåller alla unika polynom av formen $a_2x^2 + a_1x + a_0$, där varje koefficient $a_i$ är antingen 0 eller 1. Därför innehåller denna uppsättning **S** följande Elements:


1. $0$: Fallet där $a_2 = 0$, $a_1 = 0$ och $a_0 = 0$.

2. $1$: Fallet där $a_2 = 0$, $a_1 = 0$ och $a_0 = 1$.

3. $x$: Fallet där $a_2 = 0$, $a_1 = 1$ och $a_0 = 0$.

4. $x + 1$: Fallet där $a_2 = 0$, $a_1 = 1$ och $a_0 = 1$.

5. $x^2$: Fallet där $a_2 = 1$, $a_1 = 0$ och $a_0 = 0$.

6. $x^2 + 1$: Fallet där $a_2 = 1$, $a_1 = 0$ och $a_0 = 1$.

7. $x^2 + x$: Fallet där $a_2 = 1$, $a_1 = 1$ och $a_0 = 0$.

8. $x^2 + x + 1$: Fallet där $a_2 = 1$, $a_1 = 1$ och $a_0 = 1$.


Så **S** skulle vara mängden $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Vilka två operationer kan definieras över denna uppsättning Elements för att säkerställa att deras kombination är ett fält?


Den första operationen på uppsättningen **S** ($\circ$) kan definieras som standardpolynomaddition modulo 2. Allt du behöver göra är att addera polynomen som vanligt och sedan tillämpa modulo 2 på var och en av koefficienterna i det resulterande polynomet. Här är några exempel:



- $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$$
- $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
- $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$


Den andra operationen på uppsättningen **S** ($\diamond$) som behövs för att skapa fältet är mer komplicerad. Det är en sorts multiplikation, men inte den vanliga multiplikationen från aritmetiken. Istället måste man se varje element som en vektor och förstå operationen som multiplikationen av dessa två vektorer modulo ett irreducibelt polynom.


Låt oss först ta upp idén med ett irreducibelt polynom. Ett **irreducibelt polynom** är ett polynom som inte kan faktoriseras (precis som ett primtal inte kan faktoriseras till andra komponenter än 1 och primtalet självt). För våra syften är vi intresserade av polynom som är irreducibla med avseende på uppsättningen av alla heltal. (Observera att du kanske kan faktorisera vissa polynom med t.ex. de reella eller komplexa talen, även om du inte kan faktorisera dem med heltal)


Tänk till exempel på polynomet $x^2 - 3x + 2$. Detta kan skrivas om som $(x - 1)(x - 2)$. Därför är detta inte irreducibelt. Betrakta nu polynomet $x^2 + 1$. Om man bara använder heltal finns det inget sätt att ytterligare faktorisera detta uttryck. Därför är detta ett irreducibelt polynom med avseende på heltalen.


Låt oss nu gå vidare till begreppet vektormultiplikation. Vi kommer inte att utforska detta ämne på djupet, men du behöver bara förstå en grundläggande regel: Varje vektordivision kan äga rum så länge som dividenden har en grad som är högre än eller lika med divisorns. Om dividenden har en lägre grad än divisorn kan dividenden inte längre delas med divisorn.


Tänk till exempel på uttrycket $x^6 + x + 1 \mod x^5 + x^2$. Detta reduceras tydligt ytterligare eftersom graden av dividenden, 6, är högre än graden av divisorn, 5. Tänk nu på uttrycket $x^5 + x + 1 \mod x^5 + x^2$. Detta reduceras också ytterligare, eftersom graden av dividenden, 5, och divisorn, 5, är lika.


Men betrakta nu uttrycket $x^4 + x + 1 \mod x^5 + x^2$. Detta reduceras inte ytterligare, eftersom graden av dividenden, 4, är lägre än graden av divisorn, 5.


Utifrån denna information är vi nu redo att hitta vår andra operation för mängden $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.


Jag har redan sagt att den andra operationen bör förstås som vektormultiplikation modulo något irreducibelt polynom. Detta irreducibla polynom ska säkerställa att den andra operationen definierar en abelsk grupp över **S** och är förenlig med det distributiva villkoret. Så vad ska det irreducibla polynomet vara?


Eftersom alla vektorer i uppsättningen är av grad 2 eller lägre, bör det irreducibla polynomet vara av grad 3. Om varje multiplikation av två vektorer i uppsättningen ger ett polynom av grad 3 eller högre, vet vi att modulo ett polynom av grad 3 alltid ger ett polynom av grad 2 eller lägre. Detta är fallet eftersom varje polynom av grad 3 eller högre alltid är delbart med ett polynom av grad 3. Dessutom måste det polynom som fungerar som divisor vara irreducibelt.


Det visar sig att det finns flera irreducibla polynom av grad 3 som vi kan använda som vår divisor. Vart och ett av dessa polynom definierar ett annat fält i kombination med vår uppsättning **S** och addition modulo 2. Detta innebär att du har flera alternativ när du använder förlängningsfält $2^m$ i kryptografi.


I vårt exempel antar vi att vi väljer polynomet $x^3 + x + 1$. Detta är verkligen irreducibelt, eftersom du inte kan faktorisera det med heltal. Dessutom kommer det att säkerställa att varje multiplikation av två Elements kommer att ge ett polynom av grad 2 eller mindre.


Låt oss gå igenom ett exempel på den andra operationen med polynomet $x^3 + x + 1$ som divisor för att illustrera hur det fungerar. Antag att du multiplicerar Elements $x^2 + 1$ med $x^2 + x$ i vår uppsättning **S**. Vi måste då beräkna uttrycket $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Detta kan förenklas på följande sätt:



- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$$


Vi vet att $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ kan reduceras eftersom dividenden har en högre grad (4) än divisorn (3).


Till att börja med kan du se att uttrycket $x^3 + x + 1$ går in i $x^4 + x^3 + x^2 + x$ totalt $x$ gånger. Du kan verifiera detta genom att multiplicera $x^3 + x + 1$ med $x$, vilket är $x^4 + x^2 + x$. Eftersom den senare termen är av samma grad som utdelningen, nämligen 4, vet vi att detta fungerar. Du kan beräkna återstoden av denna division med $x$ enligt följande:



- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
- $[x^3] \mod x^3 + x + 1 =$
- $x^3$


Så efter att ha dividerat $x^4 + x^3 + x^2 + x$ med $x^3 + x + 1$ totalt $x$ gånger har vi en rest på $x^3$. Kan detta divideras ytterligare med $x^3 + x + 1$?


Intuitivt kan det vara tilltalande att säga att $x^3$ inte längre kan delas med $x^3 + x + 1$, eftersom den senare termen verkar större. Kom dock ihåg vår diskussion om vektordivision tidigare. Så länge dividenden har en grad som är större än eller lika med divisorn kan uttrycket reduceras ytterligare. Specifikt kan uttrycket $x^3 + x + 1$ gå in i $x^3$ exakt 1 gång. Resten beräknas på följande sätt:


$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$


Du kanske undrar varför $(x^3) - (x^3 + x + 1)$ utvärderas till $x + 1$ och inte $-x - 1$. Kom ihåg att den första operationen i vårt fält är definierad modulo 2. Därför ger subtraktionen av två vektorer exakt samma resultat som additionen av två vektorer.


För att sammanfatta multiplikationen av $x^2 + 1$ och $x^2 + x$: När du multiplicerar dessa två termer får du ett grad 4-polynom, $x^4 + x^3 + x^2 + x$, som måste reduceras modulo $x^3 + x + 1$. Polynomet av grad 4 är delbart med $x^3 + x + 1$ exakt $x + 1$ gånger. Återstoden efter att ha dividerat $x^4 + x^3 + x^2 + x$ med $x^3 + x + 1$ exakt $x + 1$ gånger är $x + 1$. Detta är verkligen ett element i vår mängd $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.


Varför skulle förlängningsfält med bas 2 över polynomuppsättningar, som i exemplet ovan, vara användbara för kryptografi? Anledningen är att man kan se koefficienterna i polynomen i sådana uppsättningar, antingen 0 eller 1, som Elements av binära strängar med en viss längd. Mängden **S** i vårt exempel ovan kan till exempel i stället ses som en mängd **S** som innehåller alla binära strängar med längden 3 (000 till 111). Operationerna på **S** kan då också användas för att utföra operationer på dessa binära strängar och producera en binär sträng av samma längd.


**Noteringar:**


[2] Tilläggsfält blir mycket kontraintuitiva. I stället för att ha Elements av heltal har de uppsättningar av polynom. Dessutom utförs alla operationer modulo något irreducibelt polynom.



## Abstrakt algebra i praktiken

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>


Trots det formella språket och abstraktionen i diskussionen bör konceptet med en grupp inte vara alltför svårt att förstå. Det är bara en uppsättning Elements tillsammans med en binär operation, där utförandet av den binära operationen på dessa Elements uppfyller fyra allmänna villkor. En abelisk grupp har bara ett extra villkor som kallas kommutativitet. En cyklisk grupp är i sin tur en speciell typ av abelsk grupp, nämligen en som har en generator. Ett fält är bara en mer komplex konstruktion av det grundläggande gruppbegreppet.


Men om du är en praktiskt lagd person kanske du undrar vid det här laget: Vem bryr sig? Har det någon verklig relevans att veta att en uppsättning Elements med en operator är en grupp, eller till och med en abelisk eller cyklisk grupp? Har det någon betydelse att veta att något är ett fält?


Utan att gå in på alltför många detaljer är svaret "ja". Grupper skapades för första gången på 1800-talet av den franske matematikern Evariste Galois. Han använde dem för att dra slutsatser om hur man löser polynomekvationer av en högre grad än fem.


Sedan dess har gruppbegreppet bidragit till att belysa en rad problem inom bland annat matematiken. Med hjälp av gruppteorin kunde t.ex. fysikern Murray-Gellman förutsäga existensen av en partikel innan den faktiskt observerades i experiment. [3] Ett annat exempel är kemister som använder gruppteori för att klassificera molekylers form. Matematiker har till och med använt gruppbegreppet för att dra slutsatser om något så konkret som väggpapper!


Att visa att en uppsättning Elements med någon operator är en grupp innebär i princip att det du beskriver har en viss symmetri. Inte en symmetri i ordets vanliga bemärkelse, utan i en mer abstrakt form. Och detta kan ge betydande insikter i särskilda system och problem. De mer komplexa begreppen från abstrakt algebra ger oss bara ytterligare information.


Viktigast av allt är att du kommer att se betydelsen av talteoretiska grupper och fält i praktiken genom deras tillämpning inom kryptografi, särskilt kryptografi med publik nyckel. Vi har redan sett i vår diskussion om fält, till exempel, hur förlängningsfält används i Rijndael-chiffret. Vi kommer att arbeta med det exemplet i *Kapitel 5*.


För vidare diskussion om abstrakt algebra rekommenderar jag den utmärkta videoserien om abstrakt algebra från Socratica. [4] Jag vill särskilt rekommendera följande videor: "Vad är abstrakt algebra?", "Gruppdefinition (utökad)", "Ringdefinition (utökad)" och "Fältdefinition (utökad)" Dessa fyra videor kommer att ge dig ytterligare insikt i mycket av diskussionen ovan. (Vi har inte diskuterat ringar, men ett fält är bara en speciell typ av ring)


För vidare diskussion om modern talteori kan du konsultera många avancerade diskussioner om kryptografi. Jag skulle vilja föreslå Jonathan Katz och Yehuda Lindell's Introduction to Modern Cryptography eller Christof Paar och Jan Pelzl's Understanding Cryptography för vidare diskussion. [5]


**Noteringar:**


[3] Se [YouTube Video] (https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)


[4] Socratica, [Abstrakt algebra] (https://www.socratica.com/subject/abstract-algebra)


[5] Katz och Lindell, *Introduction to Modern Cryptography*, 2nd edn, 2015 (CRC Press: Boca Raton, FL). Paar och Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlin).




# Symmetrisk kryptografi

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>



## Alice och Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>


En av de två huvudgrenarna inom kryptografin är symmetrisk kryptografi. Den omfattar såväl krypteringssystem som system för autentisering och integritet. Fram till 1970-talet bestod all kryptografi av symmetriska krypteringsscheman.


Huvuddiskussionen inleds med en genomgång av symmetriska krypteringssystem och den viktiga distinktionen mellan stream ciphers och block ciphers. Därefter behandlas koder för autentisering av meddelanden, som är system för att säkerställa meddelandets integritet och äkthet. Slutligen undersöker vi hur symmetriska krypteringssystem och koder för meddelandeautentisering kan kombineras för att garantera säker kommunikation.


I detta kapitel diskuteras i förbigående olika symmetriska kryptografiska system från praktiken. Nästa kapitel ger en detaljerad beskrivning av kryptering med ett strömchiffer och ett blockchiffer från praktiken, nämligen RC4 respektive AES.


Innan vi börjar diskutera symmetrisk kryptografi vill jag kortfattat kommentera illustrationerna Alice och Bob i detta och kommande kapitel.


___


När man ska illustrera principerna för kryptografi använder man sig ofta av exempel med Alice och Bob. Jag kommer också att göra det.


Särskilt om du är ny inom kryptografi är det viktigt att inse att dessa exempel på Alice och Bob endast är avsedda att tjäna som illustrationer av kryptografiska principer och konstruktioner i en förenklad miljö. Principerna och konstruktionerna är dock tillämpliga på ett mycket bredare spektrum av verkliga sammanhang.


Nedan följer fem viktiga punkter att tänka på när det gäller exempel som involverar Alice och Bob i kryptografi:


1. De kan lätt översättas till exempel med andra typer av aktörer som företag eller statliga organisationer.

2. De kan enkelt utökas till att omfatta tre eller fler aktörer.

3. I exemplen är Bob och Alice typiskt sett aktiva deltagare i skapandet av varje meddelande och i tillämpningen av kryptografiska system på det meddelandet. Men i verkligheten är elektronisk kommunikation till stor del automatiserad. När du t.ex. besöker en webbplats med Layer-transportsäkerhet hanteras kryptografin normalt av din dator och webbservern.

4. I samband med elektronisk kommunikation är de "meddelanden" som skickas över en kommunikationskanal vanligtvis TCP/IP-paket. Dessa kan tillhöra ett e-postmeddelande, ett Facebook-meddelande, ett telefonsamtal, en filöverföring, en webbplats, en programuppladdning och så vidare. De är inte meddelanden i traditionell mening. Ändå förenklar kryptografer ofta denna verklighet genom att ange att meddelandet är t.ex. ett e-postmeddelande.

5. Exemplen fokuserar vanligtvis på elektronisk kommunikation, men de kan också utvidgas till att omfatta traditionella kommunikationsformer som t.ex. brev.



## Symmetriska krypteringsscheman

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>


Vi kan fritt definiera ett **symmetriskt krypteringssystem** som ett kryptografiskt system med tre algoritmer:


1. En **nyckelgenereringsalgoritm** som genererar en privat nyckel.

2. En **krypteringsalgoritm** som tar den privata nyckeln och en klartext som indata och matar ut en chiffertext.

3. En **dekrypteringsalgoritm** som tar den privata nyckeln och chiffertexten som indata och matar ut den ursprungliga klartexten.


Ett krypteringsschema - oavsett om det är symmetriskt eller asymmetriskt - erbjuder vanligtvis en mall för kryptering baserad på en kärnalgoritm, snarare än en exakt specifikation.


Som exempel kan nämnas Salsa20, ett symmetriskt krypteringsschema. Det kan användas med både 128- och 256-bitars nyckellängder. Valet av nyckellängd påverkar vissa mindre detaljer i algoritmen (antalet rundor i algoritmen för att vara exakt).


Men man skulle inte kunna säga att Salsa20 med en 128-bitars nyckel är ett annat krypteringsschema än Salsa20 med en 256-bitars nyckel. Kärnalgoritmen förblir densamma. Först när kärnalgoritmen ändras skulle vi verkligen tala om två olika krypteringsscheman.


Symmetriska krypteringssystem är vanligtvis användbara i två typer av fall: (1) De där två eller flera agenter kommunicerar på avstånd och vill hålla innehållet i sin kommunikation hemligt; och (2) de där en agent vill hålla innehållet i ett meddelande hemligt över tiden.


Du kan se en beskrivning av situation (1) i *Figur 1* nedan. Bob vill skicka ett meddelande $M$ till Alice över ett avstånd, men vill inte att andra ska kunna läsa meddelandet.


Bob krypterar först meddelandet $M$ med den privata nyckeln $K$. Han skickar sedan chiffertexten $C$ till Alice. När Alice har tagit emot chiffertexten kan hon dekryptera den med nyckeln $K$ och läsa klartexten. Med ett bra krypteringssystem bör en angripare som avlyssnar chiffertexten $C$ inte kunna få reda på något av verklig betydelse om meddelandet $M$.


Du kan se en skildring av situation (2) i *Figur 2* nedan. Bob vill hindra andra från att se viss information. En typisk situation kan vara att Bob är en anställd som lagrar känsliga data på sin dator, som varken utomstående eller hans kollegor ska kunna läsa.


Bob krypterar meddelandet $M$ vid tidpunkten $T_0$ med nyckeln $K$ för att producera chiffertexten $C$. Vid tidpunkten $T_1$ behöver han meddelandet igen och dekrypterar chiffertexten $C$ med nyckeln $K$. En angripare som kan ha kommit över chiffertexten $C$ under tiden borde inte ha kunnat härleda något väsentligt om $M$ från den.



*Figur 1: Sekretess i rymden*


![Figure 1: Secrecy across space](assets/Figure4-1.webp "Figure 1: Secrecy across space")



*Figur 2: Sekretess över tid*



![Figure 2: Secrecy across time](assets/Figure4-2.webp "Figure 2: Secrecy across time")




## Ett exempel: Skiftchiffer

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>


I kapitel 2 gick vi igenom skiftchiffret, som är ett exempel på ett mycket enkelt symmetriskt krypteringsschema. Låt oss titta på det igen här.


Antag en ordbok *D* som likställer alla bokstäver i det engelska alfabetet, i ordningsföljd, med taluppsättningen $\{0,1,2,\dots,25\}$. Antag en uppsättning möjliga meddelanden **M**. Skiftchiffret är då ett krypteringsschema som definieras enligt följande:



- Välj slumpmässigt en nyckel $k$ ur uppsättningen möjliga nycklar **K**, där **K** = $\{0,1,2,\dots,25\}$$
- Kryptera ett meddelande $m \in$ **M**, enligt följande:
    - Dela upp $m$ i sina enskilda bokstäver $m_0, m_1,\dots, m_i, \dots, m_l$
    - Konvertera varje $m_i$ till ett tal enligt *D*
    - För varje $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Konvertera varje $c_i$ till en bokstav enligt *D*
    - Kombinera sedan $c_0, c_1,\dots, c_l$ för att få fram chiffertexten $c$
- Dekryptera en chiffertext $c$ enligt följande:
    - Konvertera varje $c_i$ till ett tal enligt *D*
    - För varje $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Omvandla varje $m_i$ till en bokstav enligt *D*
    - Kombinera sedan $m_0, m_1,\dots, m_l$ för att få fram det ursprungliga meddelandet $m$


Det som gör skiftchiffret till ett symmetriskt krypteringsschema är att samma nyckel används för både kryptering och dekryptering. Anta t.ex. att du vill kryptera meddelandet "DOG" med skiftchiffer och att du slumpmässigt har valt "24" som nyckel. Om du krypterar meddelandet med den här nyckeln får du "BME". Det enda sättet att återfå det ursprungliga meddelandet är att använda samma nyckel, "24", för dekrypteringsprocessen.


Detta Shift-chiffer är ett exempel på ett **monoalfabetiskt substitutionschiffer**: ett krypteringsschema där chiffertextens alfabet är fast (dvs. endast ett alfabet används). Om man antar att dekrypteringsalgoritmen är deterministisk kan varje symbol i substitutionschiffertexten som mest hänföra sig till en symbol i klartexten.


Fram till 1700-talet var många krypteringstillämpningar starkt beroende av monoalfabetiska substitutionschiffer, även om dessa ofta var mycket mer komplexa än Shift-chiffret. Man kunde t.ex. slumpmässigt välja en bokstav från alfabetet för varje bokstav i originaltexten under förutsättning att varje bokstav bara förekommer en gång i chiffertextens alfabet. Det innebär att man skulle ha 26 faktoriella möjliga privata nycklar, vilket var enormt på den tid då man inte hade datorer.


Observera att du ofta kommer att stöta på termen **cipher** inom kryptografi. Var medveten om att denna term har olika betydelser. Faktum är att jag känner till minst fem olika betydelser av termen inom kryptografi.


I vissa fall syftar det på ett krypteringsschema, som i Shift cipher och monoalphabetic substitution cipher. Termen kan emellertid också avse specifikt krypteringsalgoritmen, den privata nyckeln eller bara chiffertexten i ett sådant krypteringssystem.


Slutligen kan termen chiffer också avse en kärnalgoritm från vilken man kan konstruera kryptografiska scheman. Dessa kan inkludera olika krypteringsalgoritmer, men också andra typer av kryptografiska scheman. Denna innebörd av termen blir relevant i samband med blockchiffer (se avsnittet "Blockchiffer" nedan).


Du kanske också stöter på termerna att **encipher** eller att **decipher**. Dessa termer är bara synonymer för kryptering och dekryptering.



## Brute force-attacker och Kerckhoffs princip

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>


Skiftchiffret är ett mycket osäkert symmetriskt krypteringsschema, åtminstone i den moderna världen. [1] En angripare kan bara försöka dekryptera valfri chiffertext med alla 26 möjliga nycklar för att se vilket resultat som är vettigt. Den här typen av attack, där angriparen bara går igenom nycklar för att se vad som fungerar, kallas för en **brute force-attack** eller **uttömmande nyckelsökning**.


För att ett krypteringssystem ska uppfylla en minimal säkerhetsnorm måste det ha en uppsättning möjliga nycklar, eller **nyckelrymd**, som är så stor att det inte går att utföra en brute-force-attack. Alla moderna krypteringssystem uppfyller denna standard. Det är känt som **principen om tillräckligt nyckelutrymme**. En liknande princip gäller vanligtvis i olika typer av kryptografiska system.


För att få en känsla för det enorma nyckelutrymmet i moderna krypteringssystem kan vi anta att en fil har krypterats med en 128-bitars nyckel med hjälp av den avancerade krypteringsstandarden. Detta innebär att en angripare har en uppsättning nycklar på $2^{128}$ som hon måste gå igenom för en brute force-attack. En chans på 0,78% att lyckas med den här strategin skulle kräva att angriparen går igenom ungefär $2,65 gånger 10^{36}$ nycklar.


Anta att vi optimistiskt antar att en angripare kan försöka sig på 10^{16}$ nycklar per sekund (dvs. 10 kvadriljoner nycklar per sekund). För att testa 0,78% av alla nycklar i nyckelrymden skulle hennes attack behöva pågå i 2,65 gånger 10^{20}$ sekunder. Detta är ungefär 8,4 biljoner år. Så inte ens en brute force-attack av en absurt kraftfull motståndare är realistisk med ett modernt 128-bitars krypteringsschema. Detta är principen om tillräckligt nyckelutrymme som gäller.


Är shift-chiffret säkrare om angriparen inte känner till krypteringsalgoritmen? Kanske, men inte mycket.


I alla händelser förutsätter modern kryptografi alltid att säkerheten för alla symmetriska krypteringsscheman endast är beroende av att den privata nyckeln hålls hemlig. Angriparen antas alltid känna till alla andra detaljer, inklusive meddelandeutrymmet, nyckelutrymmet, chiffertextutrymmet, algoritmen för nyckelval, krypteringsalgoritmen och dekrypteringsalgoritmen.


Idén att säkerheten i ett symmetriskt krypteringssystem endast kan baseras på att den privata nyckeln är hemlig kallas för **Kerckhoffs princip**.


Som Kerckhoffs ursprungligen avsåg gäller principen endast symmetriska krypteringsscheman. En mer allmän version av principen gäller dock även för alla andra moderna typer av kryptografiska system: Ett kryptografiskt system behöver inte vara hemligt för att vara säkert, utan hemligheten kan endast omfatta vissa informationssträngar, vanligtvis en privat nyckel.


Kerckhoffs princip är central för modern kryptografi av fyra skäl. [2] För det första finns det bara ett begränsat antal kryptografiska system för vissa typer av tillämpningar. Till exempel använder de flesta moderna symmetriska krypteringsapplikationer Rijndael-krypteringen. Så din sekretess när det gäller ett systems design är bara mycket begränsad. Det finns dock mycket mer flexibilitet när det gäller att hålla en privat nyckel för Rijndael-krypteringen hemlig.


För det andra är det lättare att byta ut en informationssträng än ett helt kryptografiskt system. Anta att alla anställda på ett företag har samma krypteringsprogram och att varannan anställd har en privat nyckel för att kommunicera konfidentiellt. Nyckelkompromisser är besvärliga i det här scenariot, men företaget kan åtminstone behålla programvaran med sådana säkerhetsbrister. Om företaget förlitar sig på att systemet är hemligt måste all programvara bytas ut om hemligheten skulle brytas.


För det tredje möjliggör Kerckhoffs princip standardisering och kompatibilitet mellan användare av kryptografiska system. Detta har enorma fördelar för effektiviteten. Det är t.ex. svårt att föreställa sig hur miljontals människor skulle kunna ansluta säkert till Googles webbservrar varje dag, om säkerheten krävde att kryptografiska scheman hölls hemliga.


För det fjärde innebär Kerckhoffs princip att kryptografiska system kan granskas offentligt. Denna typ av granskning är absolut nödvändig för att uppnå säkra kryptografiska system. Som exempel kan nämnas att den viktigaste kärnalgoritmen inom symmetrisk kryptografi, Rijndael-chiffret, var resultatet av en tävling som anordnades av National Institute of Standards and Technology mellan 1997 och 2000.


Ett system som försöker uppnå **security by obscurity** är ett system som förlitar sig på att detaljerna i dess utformning och/eller implementering hålls hemliga. Inom kryptografi skulle detta specifikt vara ett system som förlitar sig på att hålla designdetaljerna i det kryptografiska schemat hemliga. Security by obscurity står alltså i direkt motsats till Kerckhoffs princip.


Öppenhetens förmåga att stärka kvalitet och säkerhet sträcker sig också längre i den digitala världen än bara till kryptografi. Linuxdistributioner med fri och öppen källkod, som Debian, har till exempel i allmänhet flera fördelar jämfört med Windows- och MacOS-distributioner när det gäller integritet, stabilitet, säkerhet och flexibilitet. Även om det kan ha flera orsaker är den viktigaste principen förmodligen, som Eric Raymond formulerade det i sin berömda essä "The Cathedral and the Bazaar", att "med tillräckligt många ögonbollar är alla buggar ytliga" [3] Det är denna princip om folkmassornas visdom som gav Linux dess mest betydande framgång.


Man kan aldrig entydigt säga att ett kryptografiskt system är "säkert" eller "osäkert" Istället finns det olika uppfattningar om säkerhet för kryptografiska system. Varje **definition av kryptografisk säkerhet** måste specificera (1) säkerhetsmål samt (2) en angripares kapacitet. Genom att analysera kryptografiska system mot en eller flera specifika säkerhetsdefinitioner får man insikter om deras tillämpningar och begränsningar.


Vi kommer inte att gå in på alla detaljer i de olika begreppen inom kryptografisk säkerhet, men du bör veta att två antaganden är allestädes närvarande i alla moderna kryptografiska säkerhetsbegrepp som rör symmetriska och asymmetriska system (och i någon form i andra kryptografiska primitiver):



- Angriparens kunskap om systemet överensstämmer med Kerckhoffs princip.
- Angriparen kan inte rimligen utföra en brute force-attack på systemet. Hotmodellerna för kryptografiska säkerhetsuppfattningar tillåter vanligtvis inte ens brute force-attacker, eftersom de utgår från att sådana inte är relevanta.



**Noteringar:**


[1] Enligt Seutonius använde Julius Caesar ett skiftchiffer med ett konstant nyckelvärde på 3 i sin militära kommunikation. Så A skulle alltid bli D, B alltid E, C alltid F, och så vidare. Den här speciella versionen av skiftchiffret har därför blivit känt som **Caesar-chiffret** (även om det egentligen inte är ett chiffer i ordets moderna bemärkelse, eftersom nyckelvärdet är konstant). Caesars chiffer kan ha varit säkert under det första århundradet f.Kr. om Roms fiender var mycket ovana vid kryptering. Men det är uppenbart att det inte skulle vara ett särskilt säkert system i modern tid.


[2] Jonathan Katz och Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 7f.


[3] Eric Raymond, "The Cathedral and the Bazaar", ett dokument som presenterades vid Linuxkongressen i Würzburg, Tyskland (27 maj 1997). Det finns ett antal efterföljande versioner tillgängliga samt en bok. Mina citat är från sidan 30 i boken: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, reviderad utgåva. (2001), O'Reilly: Sebastopol, Kalifornien.



## Stream chiffer

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>


Symmetriska krypteringsscheman delas vanligtvis in i två typer: **strömchiffer** och **blockchiffer**. Denna distinktion är dock något besvärlig, eftersom människor använder dessa termer på ett inkonsekvent sätt. I de kommande avsnitten kommer jag att redogöra för distinktionen på det sätt som jag tycker är bäst. Du bör dock vara medveten om att många människor kommer att använda dessa termer något annorlunda än vad jag anger.


Låt oss först gå över till streamchiffer. Ett **strömchiffer** är ett symmetriskt krypteringsschema där krypteringen består av två steg.


Först produceras en sträng som är lika lång som klartexten med hjälp av en privat nyckel. Denna sträng kallas **keystream**.


Därefter kombineras nyckelströmmen matematiskt med klartexten för att producera en chiffertext. Denna kombination är vanligtvis en XOR-operation. För dekryptering kan du bara vända på operationen. (Observera att $A \oplus B = B \oplus A$, i det fall $A$ och $B$ är bitsträngar. Ordningen på en XOR-operation i ett strömchiffer spelar alltså ingen roll för resultatet. Denna egenskap är känd som **kommutativitet**)


Ett typiskt XOR-strömchiffer visas i *Figur 3*. Du tar först en privat nyckel $K$ och använder den för att generate en nyckelström. Nyckelströmmen kombineras sedan med klartexten via en XOR-operation för att producera chiffertexten. Alla agenter som tar emot chiffertexten kan enkelt dekryptera den om de har nyckeln $K$. Allt hon behöver göra är att skapa en nyckelström som är lika lång som chiffertexten enligt den specificerade proceduren i schemat och XOR den med chiffertexten.



*Figur 3: Ett XOR-strömchiffer*


![Figure 3: An XOR stream cipher](assets/Figure4-3.webp "Figure 3: An XOR stream cipher")


Tänk på att ett krypteringsschema vanligtvis är en mall för kryptering med samma kärnalgoritm, snarare än en exakt specifikation. I förlängningen är ett strömchiffer typiskt en mall för kryptering där du kan använda nycklar av olika längd. Även om nyckellängden kan påverka vissa mindre detaljer i schemat, kommer den inte att påverka dess grundläggande form.


Skiftchiffret är ett exempel på ett mycket enkelt och osäkert strömchiffer. Med hjälp av en enda bokstav (den privata nyckeln) kan du producera en sträng med bokstäver som är lika lång som meddelandet (nyckelströmmen). Denna nyckelström kombineras sedan med klartexten via en modulooperation för att producera en chiffertext. (Denna moduloperation kan förenklas till en XOR-operation när bokstäverna representeras i bitar).


Ett annat känt exempel på ett strömchiffer är **Vigenerechiffret**, efter Blaise de Vigenere som utvecklade det fullt ut i slutet av 1500-talet (även om andra hade gjort mycket tidigare arbete). Det är ett exempel på ett **polyalfabetiskt substitutionschiffer**: ett krypteringsschema där chiffertextens alfabet för en klartextsymbol ändras beroende på dess position i texten. Till skillnad från ett monoalfabetiskt substitutionschiffer kan chiffertextsymboler associeras med mer än en klartextsymbol.


I takt med att kryptering blev alltmer populärt i renässansens Europa, blev även **krypteringsanalys** - det vill säga brytandet av chiffertexter - populärt, särskilt med hjälp av **frekvensanalys**. Den senare utnyttjar statistiska regelbundenheter i vårt språk för att knäcka chiffertexter, och upptäcktes av arabiska lärda redan på 800-talet. Det är en teknik som fungerar särskilt bra med längre texter. Och även de mest sofistikerade monoalfabetiska substitionschiffer var inte längre tillräckliga mot frekvensanalys på 1700-talet i Europa, särskilt i militära och säkerhetsmässiga miljöer. Eftersom Vigenere-chiffret innebar en betydande säkerhetsförbättring blev det populärt under denna period och var utbrett i slutet av 1700-talet.


Informellt sett fungerar krypteringsschemat på följande sätt:


1. Välj ett ord med flera bokstäver som privat nyckel.

2. För ett valfritt meddelande tillämpas skiftchiffer på varje bokstav i meddelandet med motsvarande bokstav i nyckelordet som skift.

3. Om du har gått igenom nyckelordet men fortfarande inte har krypterat klartexten helt och hållet, använder du nyckelordets bokstäver som skiftchiffer på motsvarande bokstäver i resten av texten.

4. Fortsätt denna process tills hela meddelandet har krypterats.


För att illustrera, anta att din privata nyckel är "GOLD" och att du vill kryptera meddelandet "CRYPTOGRAPHY". I så fall skulle du gå tillväga på följande sätt enligt Vigenère-krypteringen:



- $c_0 = [(2 + 6) \mod 26] = 8 = I$
- $c_1 = [(17 + 14) \mod 26] = 5 = F$$
- $c_2 = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$


Således är chiffertexten $c$ = "IFJSZCRUGDSB".


Ett annat känt exempel på ett strömchiffer är **one-time pad**. Med en one-time pad skapar man helt enkelt en sträng med slumpmässiga bitar som är lika lång som klartextmeddelandet och producerar chiffertexten via XOR-operationen. Den privata nyckeln och nyckelströmmen är alltså likvärdiga med ett engångschiffer.


Medan Shift-chiffret och Vigenere-chiffren är mycket osäkra i modern tid, är one-time pad mycket säkert om det används korrekt. Den förmodligen mest kända tillämpningen av engångskoden var, åtminstone fram till 1980-talet, för **Washington-Moskva hotline**. [4]


Hotline är en direkt kommunikationslänk mellan Washington och Moskva för brådskande ärenden som installerades efter Kubakrisen. Tekniken för hotlinen har förändrats under årens lopp. För närvarande omfattar den en direkt fiberoptisk kabel samt två satellitlänkar (för redundans), som möjliggör e-post och textmeddelanden. Länken slutar på olika platser i USA. Pentagon, Vita huset och Raven Rock Mountain är kända ändpunkter. I motsats till vad många tror har hotlinen aldrig involverat telefoner.


I huvudsak fungerade systemet med engångspaddar på följande sätt. Både Washington och Moskva skulle ha två uppsättningar slumptal. En uppsättning slumptal, skapad av ryssarna, gällde kryptering och dekryptering av meddelanden på ryska. En uppsättning slumptal, skapade av amerikanerna, gällde kryptering och dekryptering av alla meddelanden på engelska. Från tid till annan skulle fler slumptal levereras till den andra sidan av betrodda kurirer.


Washington och Moskva kunde alltså kommunicera i hemlighet genom att använda dessa slumptal för att skapa engångskoder. Varje gång man behövde kommunicera använde man nästa del av slumptalen för sitt meddelande.


One-time pad är visserligen mycket säkert, men har betydande praktiska begränsningar: nyckeln måste vara lika lång som meddelandet och ingen del av en one-time pad kan återanvändas. Det innebär att du måste hålla reda på var du befinner dig i engångspadden, lagra ett stort antal bitar och Exchange slumpmässiga bitar med dina motparter då och då. Som en följd av detta används inte one-time pad särskilt ofta i praktiken.


Istället är de dominerande strömchiffer som används i praktiken **pseudorandomströmchiffer**. Salsa20 och en närbesläktad variant som heter ChaCha är exempel på vanligt förekommande pseudotillfälliga strömchiffer.


Med dessa pseudorandom stream ciphers väljer du först slumpmässigt en nyckel K som är kortare än längden på klartexten. En sådan slumpmässig nyckel K skapas vanligtvis av vår dator på grundval av oförutsägbara data som den samlar in över tiden, t.ex. tiden mellan nätverksmeddelanden, musrörelser och så vidare.


Denna slumpmässiga nyckel $K$ sätts sedan in i en expansionsalgoritm som skapar en pseudorandom nyckelström som är lika lång som meddelandet. Du kan ange exakt hur lång nyckelströmmen måste vara (t.ex. 500 bitar, 1000 bitar, 1200 bitar, 29 117 bitar och så vidare).


En pseudorandom nyckelström ser ut *som* om den valts helt slumpmässigt från uppsättningen av alla strängar med samma längd. Därför ser kryptering med en pseudorandom nyckelström ut som om den hade gjorts med en one-time pad. Men så är naturligtvis inte fallet.


Eftersom vår privata nyckel är kortare än nyckelströmmen och vår expansionsalgoritm måste vara deterministisk för att krypterings-/dekrypteringsprocessen ska fungera, kan inte alla nyckelströmmar av den specifika längden ha resulterat som en utgång från vår expansionsoperation.


Antag t.ex. att vår privata nyckel har en längd på 128 bitar och att vi kan infoga den i en expansionsalgoritm för att skapa en mycket längre nyckelström, t.ex. på 2 500 bitar. Eftersom vår expansionsalgoritm måste vara deterministisk kan vår algoritm högst välja $1/2^{128}$ strängar med en längd på 2 500 bitar. En sådan nyckelström kan alltså aldrig väljas helt slumpmässigt från alla strängar med samma längd.


Vår definition av ett strömchiffer har två aspekter: (1) en nyckelström som är lika lång som klartexten genereras med hjälp av en privat nyckel; och (2) denna nyckelström kombineras med klartexten, vanligtvis via en XOR-operation, för att producera chiffertexten.


Ibland definieras villkor (1) mer strikt genom att hävda att nyckelströmmen måste vara pseudorandomisk. Detta innebär att varken skiftchiffer eller engångschiffer skulle betraktas som strömchiffer.


Enligt min mening innebär en bredare definition av villkor (1) ett enklare sätt att organisera krypteringssystem. Dessutom innebär det att vi inte behöver sluta kalla ett visst krypteringssystem för ett strömchiffer bara för att vi lär oss att det faktiskt inte förlitar sig på pseudotillfälliga nyckelströmmar.


**Noteringar:**


[4] Crypto Museum, "Washington-Moscow hotline", 2013, tillgänglig på [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).




## Blockera chiffer

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>


Det första sättet som ett **blockchiffer** vanligtvis förstås på är som något mer primitivt än ett streamchiffer: En kärnalgoritm som utför en längdbevarande transformation på en sträng av lämplig längd med hjälp av en nyckel. Denna algoritm kan användas för att skapa krypteringsscheman och kanske andra typer av kryptografiska scheman.


Ofta kan ett blockchiffer ta in strängar av varierande längd, t.ex. 64, 128 eller 256 bitar, samt nycklar av varierande längd, t.ex. 128, 192 eller 256 bitar. Även om vissa detaljer i algoritmen kan ändras beroende på dessa variabler, ändras inte kärnalgoritmen. Om den gjorde det skulle vi tala om två olika blockchiffer. Observera att användningen av terminologin för kärnalgoritmen här är densamma som för krypteringsscheman.


En bild av hur ett blockchiffer fungerar visas i *Figur 4* nedan. Ett meddelande $M$ med längden $L$ och en nyckel $K$ fungerar som ingångar till blockchiffret. Det matar ut ett meddelande $M'$ med längden $L$. Nyckeln behöver inte nödvändigtvis vara lika lång som $M$ och $M'$ för de flesta blockchiffer.


*Figur 4: Ett blockchiffer*


![Figure 4: A block cipher](assets/Figure4-4.webp "Figure 4: A block cipher")


Ett blockchiffer i sig är inte ett krypteringsschema. Men ett blockchiffer kan användas med olika **modes of operation** för att producera olika krypteringsscheman. Ett driftsätt lägger helt enkelt till några ytterligare operationer utanför blockchiffret.


För att illustrera hur detta fungerar kan vi anta ett blockchiffer (BC) som kräver en 128-bitars inmatningssträng och en 128-bitars privat nyckel. Figur 5 nedan visar hur detta blockchiffer kan användas med **electronic code book mode** (**ECB mode**) för att skapa ett krypteringsschema. (Ellipserna till höger visar att du kan upprepa detta mönster så länge det behövs).


*Figur 5: Ett blockchiffer med ECB-läge*


![Figure 5: A block cipher with ECB mode](assets/Figure4-5.webp "Figure 5: A block cipher with ECB mode")


Så här går du tillväga för att kryptera en elektronisk kodbok med blockchiffer. Se om du kan dela upp ditt klartextmeddelande i 128-bitarsblock. Om inte, lägg till **padding** till meddelandet, så att resultatet kan delas jämnt med blockstorleken på 128 bitar. Detta är dina data som används för krypteringsprocessen.


Dela nu upp data i bitar av 128-bitars strängar ($M_1$, $M_2$, $M_3$, och så vidare). Kör varje 128-bitarssträng genom blockchiffret med din 128-bitarsnyckel för att producera 128-bitars bitar av chiffertext ($C_1$, $C_2$, $C_3$, och så vidare). När dessa bitar kombineras igen bildar de den fullständiga chiffertexten.


Dekryptering är bara den omvända processen, även om mottagaren behöver något igenkännbart sätt att ta bort eventuella utfyllnader från de dekrypterade uppgifterna för att få fram det ursprungliga meddelandet i klartext.


Även om det är relativt enkelt saknar ett blockchiffer med elektroniskt kodboksläge säkerhet. Detta beror på att det leder till **deterministisk kryptering**. Två identiska 128-bitars datasträngar krypteras på exakt samma sätt. Den informationen kan utnyttjas.


Istället bör alla krypteringsscheman som konstrueras från ett blockchiffer vara **probabilistiska**: det vill säga krypteringen av alla meddelanden $M$, eller någon specifik del av $M$, bör i allmänhet ge ett annat resultat varje gång. [5]


**CBC-läget** (**cipher block chaining mode**) är förmodligen det vanligaste läget som används med ett blockchiffer. Kombinationen, om den görs på rätt sätt, ger ett probabilistiskt krypteringsschema. Du kan se en bild av detta arbetssätt i *Figur 6* nedan.


*Figur 6: Ett blockchiffer med CBC-läge*


![Figure 6: A block cipher with CBC mode](assets/Figure4-6.webp "Figure 6: A block cipher with CBC mode")


Anta att blockstorleken återigen är 128 bitar. För att börja måste du alltså återigen försäkra dig om att ditt ursprungliga klartextmeddelande får den nödvändiga utfyllnaden.


Sedan XOR:ar du den första 128-bitarsdelen av din klartext med en **initialiseringsvektor** på 128 bitar. Resultatet placeras i blockchiffret för att producera en chiffertext för det första blocket. För det andra blocket på 128 bitar XOR:ar du först klartexten med chiffertexten från det första blocket, innan du sätter in den i blockchiffret. Så fortsätter du tills du har krypterat hela ditt klartextmeddelande.


När du är klar skickar du det krypterade meddelandet tillsammans med den okrypterade initialiseringsvektorn till mottagaren. Mottagaren måste känna till initialiseringsvektorn, annars kan hon inte dekryptera chiffertexten.


Denna konstruktion är mycket säkrare än elektronisk kodboksläge när den används korrekt. Du bör först och främst se till att initialiseringsvektorn är en slumpmässig eller pseudoslumpmässig sträng. Dessutom bör du använda en annan initialiseringsvektor varje gång du använder det här krypteringsschemat.


Med andra ord bör din initialiseringsvektor vara en slumpmässig eller pseudorandom Nonce, där en **Nonce** står för "ett tal som bara används en gång" Om du följer denna praxis säkerställer CBC-läget med ett blockchiffer att två identiska klartextblock i allmänhet kommer att krypteras olika varje gång.


Slutligen ska vi titta närmare på **output feedback mode** (**OFB mode**). Du kan se en bild av detta läge i *Figur 7*.


*Figur 7: Ett blockchiffer med OFB-läge*


![Figure 7: A block cipher with OFB mode](assets/Figure4-7.webp "Figure 7: A block cipher with OFB mode")


I OFB-läget väljer du också en initialiseringsvektor. Men här, för det första blocket, sätts initialiseringsvektorn direkt in i blockchiffret med din nyckel. De 128 bitarna som blir resultatet behandlas sedan som en nyckelström. Denna nyckelström XOR:as med klartexten för att producera chiffertexten för blocket. För efterföljande block använder du nyckelströmmen från det föregående blocket som en ingång till blockchiffret och upprepar stegen.


Om du tittar noga är det som faktiskt har skapats här från blockchiffret med OFB-läge ett strömchiffer. Du gör generate nyckelströmsdelar på 128 bitar tills du har längden på klartexten (kasta bort de bitar du inte behöver från den sista 128-bitars nyckelströmsdelen). Sedan XOR:ar du nyckelströmmen med ditt klartextmeddelande för att få fram chiffertexten.


I det föregående avsnittet om strömchiffer konstaterade jag att man skapar en nyckelström med hjälp av en privat nyckel. För att vara exakt behöver den inte bara skapas med en privat nyckel. Som du kan se i OFB-läget produceras nyckelströmmen med stöd av både en privat nyckel och en initialiseringsvektor.


Observera att precis som i CBC-läget är det viktigt att välja en pseudo- eller slumpmässig Nonce för initialiseringsvektorn varje gång du använder ett blockchiffer i OFB-läget. Annars kommer samma 128-bitars meddelandesträng som skickas i olika kommunikationer att krypteras på samma sätt. Detta är ett sätt att skapa probabilistisk kryptering med ett streamchiffer.


Vissa strömchiffer använder endast en privat nyckel för att skapa en nyckelström. För dessa stream ciphers är det viktigt att du använder en slumpmässig Nonce för att välja den privata nyckeln för varje kommunikationstillfälle. Annars kommer resultatet av kryptering med dessa strömchiffer också att vara deterministiskt, vilket leder till säkerhetsproblem.


Det mest populära moderna blockchiffret är **Rijndael-chiffret**. Det var det vinnande bidraget av femton bidrag till en tävling som hölls av National Institute of Standards and Technology (NIST) mellan 1997 och 2000 i syfte att ersätta en äldre krypteringsstandard, **data encryption standard** (**DES**).


Rijndael-chiffret kan användas med olika specifikationer för nyckellängder och blockstorlekar, samt i olika driftlägen. Kommittén för NIST-tävlingen antog en begränsad version av Rijndael-chiffret - nämligen en som kräver 128-bitars blockstorlekar och nyckellängder på antingen 128 bitar, 192 bitar eller 256 bitar - som en del av **advanced encryption standard** (**AES**). Det här är verkligen huvudstandarden för symmetriska krypteringsapplikationer. Den är så säker att till och med NSA tydligen är villig att använda den med 256-bitarsnycklar för topphemliga dokument. [6]


Blockchiffret AES förklaras i detalj i *Kapitel 5*.



**Noteringar:**


[5] Betydelsen av probabilistisk kryptering betonades först av Shafi Goldwasser och Silvio Micali, "Probabilistic encryption", _Journal of Computer and System Sciences_, 28 (1984), 270-99.


[6] Se NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).




## Uppklarning av förvirringen

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>


Förvirringen kring skillnaden mellan blockchiffer och streamchiffer beror på att människor ibland uppfattar termen blockchiffer som en specifik hänvisning till ett *blockchiffer med en blockmetod för kryptering*.


Tänk på ECB- och CBC-lägena i föregående avsnitt. Dessa kräver specifikt att data som ska krypteras är delbara med blockstorleken (vilket innebär att du kan behöva använda utfyllnad för det ursprungliga meddelandet). Dessutom bearbetas data i dessa lägen direkt av blockchiffret (och kombineras inte bara med resultatet av en blockchifferoperation som i OFB-läget).


Därför kan man alternativt definiera ett **blockchiffer** som ett krypteringsschema som arbetar med block med fast längd av meddelandet åt gången (där varje block måste vara längre än en byte, annars kollapsar det till ett strömchiffer). Både data för kryptering och chiffertext måste dela sig jämnt i denna blockstorlek. Vanligtvis är blockstorleken 64, 128, 192 eller 256 bitar lång. Ett strömchiffer kan däremot kryptera alla meddelanden i bitar om en bit eller byte åt gången.


Med denna mer specifika förståelse av blockchiffer kan du verkligen hävda att moderna krypteringsscheman är antingen ström- eller blockchiffer. Hädanefter kommer jag att använda termen blockchiffer i den mer allmänna betydelsen om inget annat anges.


Diskussionen om OFB-läge i föregående avsnitt ger också upphov till en annan intressant punkt. Vissa strömchiffer är uppbyggda av blockchiffer, som Rijndael med OFB. Andra, som Salsa20 och ChaCha, är inte skapade från blockchiffer. Man kan kalla de senare för **primitiva strömchiffer**. (Det finns egentligen ingen standardiserad term för att hänvisa till sådana strömchiffer)


När man talar om fördelar och nackdelar med stream ciphers och block ciphers jämför man vanligen primitiva stream ciphers med krypteringsscheman som bygger på block ciphers.


Medan man alltid enkelt kan konstruera ett streamchiffer från ett blockchiffer, är det normalt mycket svårt att bygga någon typ av konstruktion med blockkryptering (t.ex. med CBC-läge) från ett primitivt streamchiffer.


Från den här diskussionen bör du nu förstå *Figur 8*. Den ger en översikt över symmetriska krypteringsscheman. Vi använder tre typer av krypteringsscheman: primitiva stream ciphers, block cipher stream ciphers och block ciphers i blockläge (kallas även "block ciphers" i diagrammet).


*Figur 8: Översikt över symmetriska krypteringssystem*


![Figure 8: Overview of symmetric encryption schemes](assets/Figure4-8.webp "Figure 8: Overview of symmetric encryption schemes")



## Autentiseringskoder för meddelanden

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>


Kryptering handlar om sekretess. Men kryptografi handlar också om bredare teman, t.ex. meddelandets integritet, autenticitet och oavvislighet. Så kallade **message authentication codes** (MAC) är kryptografiska system med symmetrisk nyckel som stöder autenticitet och integritet i kommunikationer.


Varför behövs något annat än sekretess vid kommunikation? Anta att Bob skickar Alice ett meddelande med praktiskt taget obrytbar kryptering. En angripare som snappar upp detta meddelande kommer inte att kunna få några betydande insikter om innehållet. Angriparen har dock fortfarande minst två andra attackvektorer till sitt förfogande:


1. Hon kunde avlyssna chiffertexten, ändra dess innehåll och skicka den ändrade chiffertexten vidare till Alice.

2. Hon kan blockera Bob:s meddelande helt och hållet och skicka sin egen skapade chiffertext.


I båda dessa fall kanske angriparen inte har någon insikt i innehållet i chiffertexterna (1) och (2). Men hon kan ändå orsaka betydande skada på detta sätt. Det är här autentiseringskoder för meddelanden blir viktiga.


Message Authentication Codes definieras löst som symmetriska kryptografiska system med tre algoritmer: en nyckelgenereringsalgoritm, en tagggenereringsalgoritm och en verifieringsalgoritm. En säker MAC säkerställer att taggar är **existentiellt oförfalskbara** för alla angripare, dvs. de kan inte framgångsrikt skapa en tagg på det meddelande som verifieras, såvida de inte har den privata nyckeln.


Bob och Alice kan bekämpa manipuleringen av ett visst meddelande med hjälp av en MAC. Anta för tillfället att de inte bryr sig om sekretess. De vill bara försäkra sig om att det meddelande som Alice tar emot verkligen kommer från Bob och inte har ändrats på något sätt.


Processen beskrivs i *Figur 9*. För att använda en **MAC** (Message Authentication Code) måste de först generate en privat nyckel $K$ som delas mellan dem båda. Bob skapar en tagg $T$ för meddelandet med hjälp av den privata nyckeln $K$. Han skickar sedan meddelandet samt meddelandetaggen till Alice. Hon kan sedan verifiera att Bob verkligen har skapat taggen genom att köra den privata nyckeln, meddelandet och taggen genom en verifieringsalgoritm.


*Figur 9: Översikt över symmetriska krypteringssystem*


![Figure 9: Overview of symmetric encryption schemes](assets/Figure4-9.webp "Figure 9: Overview of symmetric encryption schemes")


På grund av **existentiell oförfalskbarhet** kan en angripare inte ändra meddelandet $M$ på något sätt eller skapa ett eget meddelande med en giltig tagg. Detta gäller även om angriparen observerar taggarna för många meddelanden mellan Bob och Alice som använder samma privata nyckel. På sin höjd kan en angripare blockera Alice från att ta emot meddelandet $M$ (ett problem som kryptografi inte kan lösa Address).


En MAC garanterar att ett meddelande faktiskt har skapats av Bob. Denna autenticitet innebär automatiskt meddelandets integritet - det vill säga, om Bob har skapat ett meddelande, så har det ipso facto inte ändrats på något sätt av en angripare. Så från och med nu bör varje fråga om autentisering automatiskt uppfattas som en fråga om integritet.


Även om jag i min diskussion har gjort en åtskillnad mellan meddelandets autenticitet och integritet, är det också vanligt att använda dessa termer som synonymer. De hänvisar då till idén om meddelanden som både skapats av en viss avsändare och inte ändrats på något sätt. I denna anda kallas koder för meddelandeautentisering ofta också **koder för meddelandeintegritet**.



## Autentiserad kryptering

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>


Vanligtvis vill man garantera både sekretess och autenticitet i kommunikationen och därför används krypteringsscheman och MAC-scheman vanligtvis tillsammans.


Ett **autentiserat krypteringssystem** är ett system som kombinerar kryptering med en MAC på ett mycket säkert sätt. Det måste särskilt uppfylla standarderna för existentiell oförfalskbarhet samt en mycket stark uppfattning om sekretess, nämligen en som är resistent mot **attacker med vald chiffertext**. [7]


För att ett krypteringssystem ska vara motståndskraftigt mot attacker med vald chiffertext måste det uppfylla kraven på **icke-malleabilitet**: det vill säga att varje ändring av en chiffertext av en angripare ska ge antingen en ogiltig chiffertext eller en som dekrypteras till en klartext som inte har någon relation till den ursprungliga. [8]


Eftersom ett autentiserat krypteringsschema säkerställer att en chiffertext som skapas av en angripare alltid är ogiltig (eftersom taggen inte kommer att verifieras), uppfyller det standarderna för motståndskraft mot attacker med vald chiffertext. Intressant nog kan man bevisa att ett autentiserat krypteringsschema alltid kan skapas från kombinationen av en existentiellt oförfalskbar MAC och ett krypteringsschema som uppfyller ett mindre starkt säkerhetsbegrepp, känt som **chosen-plaintext-attack security**.


Vi kommer inte att gå in på alla detaljer i konstruktionen av autentiserade krypteringsscheman. Men det är viktigt att känna till två detaljer i deras konstruktion.


Ett autentiserat krypteringsschema hanterar först krypteringen och skapar sedan en meddelandetagg på chiffertexten. Det visar sig att andra tillvägagångssätt - som att kombinera chiffertexten med en tagg på klartexten, eller att först skapa en tagg och sedan kryptera både klartexten och taggen - är osäkra. Dessutom har båda operationerna sin egen slumpmässigt valda privata nyckel, annars äventyras din säkerhet allvarligt.


Ovanstående princip gäller mer generellt: *du bör alltid använda olika nycklar när du kombinerar grundläggande kryptografiska system*.


Ett autentiserat krypteringsschema visas i *Figur 10*. Bob skapar först en chiffertext $C$ från meddelandet $M$ med hjälp av en slumpmässigt vald nyckel $K_C$. Han skapar sedan en meddelandetagg $T$ genom att köra chiffertexten och en annan slumpmässigt vald nyckel $K_T$ genom algoritmen för tagggenerering. Både chiffertexten och meddelandetaggen skickas till Alice.


Alice kontrollerar nu först om taggen är giltig med tanke på chiffertexten $C$ och nyckeln $K_T$. Om den är giltig kan hon sedan dekryptera meddelandet med hjälp av nyckeln $K_C$. Hon är inte bara försäkrad om en mycket stark sekretess i deras kommunikation, utan hon vet också att meddelandet skapades av Bob.


*Figur 10: Ett autentiserat krypteringsschema*


![Figure 10: An authenticated encryption scheme](assets/Figure4-10.webp "Figure 10: An authenticated encryption scheme")


Hur skapas MAC:er? MAC kan skapas på flera olika sätt, men ett vanligt och effektivt sätt är att skapa dem via **kryptografiska Hash-funktioner**.


Vi kommer att introducera kryptografiska Hash-funktioner mer ingående i *Kapitel 6*. För tillfället ska du bara veta att en **Hash-funktion** är en effektivt beräkningsbar funktion som tar inmatningar av godtycklig storlek och ger utmatningar med fast längd. Till exempel genererar den populära Hash-funktionen **SHA-256** (secure Hash algorithm 256) alltid en 256-bitars utdata oavsett storleken på indata. Vissa Hash-funktioner, t.ex. SHA-256, har användbara tillämpningar inom kryptografi.


Den vanligaste typen av tagg som produceras med en kryptografisk Hash-funktion är den **Hash-baserade meddelandeautentiseringskoden** (HMAC). Processen beskrivs i *Figur 11*. En part producerar två distinkta nycklar från en privat nyckel $K$, den inre nyckeln $K_1$ och den yttre nyckeln $K_2$. Klartexten $M$ eller chiffertexten $C$ hashas sedan tillsammans med den inre nyckeln. Resultatet $T'$ hashas sedan med den yttre nyckeln för att producera meddelandetaggen $T$.


Det finns en palett av Hash-funktioner som kan användas för att skapa en HMAC. Den vanligast förekommande Hash-funktionen är SHA-256.



*Bild 11: HMAC*


![Figure 11: HMAC](assets/Figure4-11.webp "Figure 11: HMAC")


**Noteringar:**


[7] De specifika resultat som diskuteras i detta avsnitt är hämtade från Katz och Lindell, s. 131-47.


[8] Tekniskt sett är definitionen av angrepp med vald chiffertext annorlunda än begreppet icke-malleabilitet. Men du kan visa att dessa två säkerhetsbegrepp är likvärdiga.




## Säkra kommunikationssessioner

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>


Anta att två parter befinner sig i en kommunikationssession, så att de skickar flera meddelanden fram och tillbaka.


Ett autentiserat krypteringssystem gör det möjligt för en mottagare av ett meddelande att verifiera att det har skapats av hennes partner i kommunikationssessionen (så länge den privata nyckeln inte har läckt ut). Detta fungerar tillräckligt bra för ett enda meddelande. Vanligtvis är det dock två parter som skickar meddelanden fram och tillbaka under en kommunikationssession. I det läget räcker det inte med ett enkelt autentiserat krypteringsschema enligt beskrivningen i föregående avsnitt för att ge säkerhet.


Det främsta skälet är att ett autentiserat krypteringssystem inte ger några garantier för att meddelandet faktiskt också skickades av den agent som skapade det inom en kommunikationssession. Betrakta följande tre attackvektorer:


1. **Replay-attack**: En angripare skickar på nytt en chiffertext och en tagg som hon avlyssnat mellan två parter vid ett tidigare tillfälle.

2. **Omordningsattack**: En angripare snappar upp två meddelanden vid olika tidpunkter och skickar dem till mottagaren i omvänd ordning.

3. **Reflektionsattack**: En angripare observerar ett meddelande som skickas från A till B och skickar även detta meddelande till A.


Även om angriparen inte har någon kännedom om chiffertexten och inte kan skapa falska chiffertexter, kan attackerna ovan ändå orsaka betydande skador i kommunikationen.


Anta t.ex. att ett visst meddelande mellan de två parterna handlar om överföring av finansiella medel. En replay-attack kan överföra pengarna en andra gång. Ett vanligt autentiserat krypteringssystem har inget försvar mot sådana attacker.


Lyckligtvis kan den här typen av attacker enkelt motverkas i en kommunikationssession med hjälp av **identifierare** och **relativa tidsindikatorer**.


Identifierare kan läggas till i klartextmeddelandet före kryptering. Detta skulle hindra alla reflektionsattacker. En relativ tidsindikator kan t.ex. vara ett sekvensnummer i en viss kommunikationssession. Varje part lägger till ett sekvensnummer till ett meddelande före kryptering, så att mottagaren vet i vilken ordning meddelandena skickades. Detta eliminerar möjligheten till omordningsattacker. Det eliminerar också replay-attacker. Varje meddelande som en angripare skickar vidare kommer att ha ett gammalt sekvensnummer, och mottagaren vet att meddelandet inte ska behandlas igen.


För att illustrera hur säkra kommunikationssessioner fungerar, anta återigen Alice och Bob. De skickar totalt fyra meddelanden fram och tillbaka. Du kan se hur ett autentiserat krypteringsschema med identifierare och sekvensnummer skulle fungera nedan i *Figur 11*.


Kommunikationssessionen börjar med att Bob skickar en chiffertext $C_{0,B}$ till Alice med en meddelandetagg $T_{0,B}$. Chiffertexten innehåller meddelandet samt en identifierare (Bob) och ett sekvensnummer (0). Taggen $T_{0,B}$ är gjord över hela chiffertexten. I sina efterföljande kommunikationer upprätthåller Alice och Bob detta protokoll och uppdaterar fält vid behov.



*Figur 12: En säker kommunikationssession*


![Figure 12: A secure communication session](assets/Figure4-12.webp "Figure 12: A secure communication sessesion")







# RC4 och AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>





## RC4-strömchiffer

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>


I det här kapitlet kommer vi att diskutera detaljerna i ett krypteringsschema med ett modernt primitivt strömchiffer, RC4 (eller "Rivest cipher 4"), och ett modernt blockchiffer, AES. Medan RC4-chiffret har fallit i onåd som krypteringsmetod är AES standarden för modern symmetrisk kryptering. Dessa två exempel bör ge en bättre uppfattning om hur symmetrisk kryptering fungerar under huven.


___


För att få en känsla för hur moderna pseudotillfälliga strömchiffer fungerar kommer jag att fokusera på RC4-strömchiffret. Det är ett pseudotillfälligt strömchiffer som användes i säkerhetsprotokollen WEP och WAP för trådlösa accesspunkter samt i TLS. Eftersom RC4 har många bevisade svagheter har det fallit i onåd. Faktum är att Internet Engineering Task Force nu förbjuder användning av RC4-sviter av klient- och serverapplikationer i alla TLS-instanser. Ändå fungerar det bra som ett exempel för att illustrera hur ett primitivt strömchiffer fungerar.


Till att börja med ska jag visa hur man krypterar ett klartextmeddelande med ett RC4-chiffer. Anta att vårt klartextmeddelande är "SOUP" Kryptering med vårt RC4-chiffer för barn sker då i fyra steg.


### Steg 1


Definiera först en matris **S** med $S[0] = 0$ till $S[7] = 7$. En array betyder här helt enkelt en föränderlig samling värden som organiseras av ett index, även kallad en lista i vissa programmeringsspråk (t.ex. Python). I det här fallet går indexet från 0 till 7, och värdena går också från 0 till 7. Så **S** är som följer:



- $S = [0, 1, 2, 3, 4, 5, 6, 7]$


Värdena här är inte ASCII-nummer, utan decimalvärdesrepresentationer av strängar på 1 byte. Så värdet 2 skulle vara lika med $0000 \ 0011$. Längden på matrisen **S** är alltså 8 byte.


### Steg 2


För det andra definierar du en nyckelarray **K** på 8 byte genom att välja en nyckel mellan 1 och 8 byte (inga bråkdelar av byte tillåts). Eftersom varje byte är 8 bitar kan du välja ett tal mellan 0 och 255 för varje byte i din nyckel.


Anta att vi väljer vår nyckel **k** som $[14, 48, 9]$, så att den har en längd på 3 byte. Varje index i vår nyckelarray sätts då i enlighet med decimalvärdet för det specifika elementet i nyckeln, i tur och ordning. Om du går igenom hela nyckeln, börja om från början, tills du har fyllt de 8 platserna i nyckelmatrisen. Vår nyckeluppsättning ser alltså ut enligt följande:



- $K = [14, 48, 9, 14, 48, 9, 14, 48]$


### Steg 3


För det tredje ska vi omvandla matrisen **S** med hjälp av nyckelmatrisen **K**, i en process som kallas **nyckelschemaläggning**. Processen går till på följande sätt i pseudokod:



- Skapa variablerna **j** och **i**
- Ställ in variabeln $j = 0$
- För varje $i$ från 0 till 7:
    - Ställ in $j = (j + S[i] + K[i]) \mod 8$
    - Byt $S[i]$ och $S[j]$ mot varandra


Omvandlingen av matrisen **S** visas i *Tabell 1*.


Till att börja med kan du se det initiala tillståndet för **S** som $[0, 1, 2, 3, 4, 5, 6, 7]$ med ett initialt värde på 0 för **j**. Detta kommer att omvandlas med hjälp av nyckelmatrisen $[14, 48, 9, 14, 48, 9, 14, 48]$.


For-slingan börjar med $i = 0$. Enligt vår pseudokod ovan blir det nya värdet av **j** 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Genom att byta ut $S[0]$ och $S[6]$ blir tillståndet för **S** efter 1 runda $[6, 1, 2, 3, 4, 5, 0, 7]$.


I nästa rad är $i = 1$. Genom att gå igenom for-slingan igen får **j** värdet 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Byte av $S[1]$ och $S[7]$ från det aktuella tillståndet för **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, ger $[6, 7, 2, 3, 4, 5, 0, 1]$ efter rond 2.


Vi fortsätter med denna process tills vi får fram den sista raden längst ner för matrisen **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.



*Tabell 1: Tabell över viktiga schemaläggningar*


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

### Steg 4


Som ett fjärde steg producerar vi **keystream**. Detta är en pseudoandomsträng med en längd som är lika med det meddelande vi vill skicka. Den kommer att användas för att kryptera det ursprungliga meddelandet "SOUP" Eftersom nyckelströmmen måste vara lika lång som meddelandet behöver vi en som har 4 byte.


Nyckelströmmen produceras med följande pseudokod:



- Skapa variablerna **j**, **i** och **t**.
- Ställ in $j = 0$.
- För varje $i$ i klartexten, från och med $i = 1$ till och med $i = 4$, produceras varje byte i nyckelströmmen på följande sätt:
    - $j = (j + S[i]) \mod 8$ $j = (j + S[i])
    - Byt $S[i]$ och $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$ $t = (S[i] + S[j])
    - Den $i^{th}$ byten i nyckelströmmen = $S[t]$


Du kan följa beräkningarna i *Tabell 2*.


Initialtillståndet för **S** är $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Med $i = 1$ blir värdet på **j** 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Vi byter sedan $S[1]$ och $S[4]$ för att få transformationen av **S** i den andra raden, $[6, 3, 1, 0, 4, 7, 5, 2]$. Värdet på **t** är då 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Slutligen är byten för nyckelströmmen $S[7]$, eller 2.


Vi fortsätter sedan att producera de andra bytena tills vi har följande fyra byte: 2, 6, 3 och 7. Var och en av dessa bytes kan sedan användas för att kryptera varje bokstav i klartexten, "SOUP".


Till att börja med kan vi med hjälp av en ASCII-tabell se att "SOUP" kodat med decimalvärdena för de underliggande bytesträngarna är "83 79 85 80". Kombinationen med nyckelströmmen "2 6 3 7" ger "85 85 88 87", vilket förblir detsamma efter en modulo 256-operation. I ASCII är chiffertexten "85 85 88 87" lika med "UUXW".


Vad händer om ordet som ska krypteras är längre än matrisen **S**? I så fall fortsätter matrisen **S** bara att transformeras på det sätt som visas ovan för varje byte **i** i klartexten, tills vi har ett antal byte i nyckelströmmen som är lika med antalet bokstäver i klartexten.



*Tabell 2: Keystream-generering*


| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     |     |     |           |      |      |      |      |      |      |      |      |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |
| 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Exemplet som vi just diskuterade är bara en urvattnad version av **RC4 stream cipher**. Det faktiska RC4-strömchiffret har en **S**-array på 256 byte i längd, inte 8 byte, och en nyckel som kan vara mellan 1 och 256 byte, inte mellan 1 och 8 byte. Nyckelarrayen och nyckelströmmarna produceras sedan alla med hänsyn till 256-byte-längden på **S**-arrayen. Beräkningarna blir oerhört mycket mer komplexa, men principerna förblir desamma. Genom att använda samma nyckel, [14,48,9], med standardchiffret RC4, krypteras klartextmeddelandet "SOUP" som 67 02 ed df i hexadecimalt format.


Ett streamchiffer där nyckelströmmen uppdateras oberoende av klartextmeddelandet eller chiffertexten är ett **synkront streamchiffer**. Nyckelströmmen är endast beroende av nyckeln. RC4 är uppenbarligen ett exempel på ett synkront strömchiffer, eftersom nyckelströmmen inte har någon relation till klartexten eller chiffertexten. Alla våra primitiva strömchiffer som nämndes i föregående kapitel, inklusive skiftchiffret, Vigenèrechiffret och engångschiffret, var också av den synkrona varianten.


Däremot har ett **asynkront strömchiffer** en nyckelström som produceras av både nyckeln och tidigare Elements av chiffertexten. Denna typ av chiffer kallas också för **självsynkroniserande chiffer**.


Det är viktigt att den nyckelström som produceras med RC4 behandlas som en engångskod, och du kan inte producera nyckelströmmen på exakt samma sätt nästa gång. I stället för att ändra nyckeln varje gång är den praktiska lösningen att kombinera nyckeln med en **Nonce** för att producera bytestreamen.




## AES med en 128-bitars nyckel

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>


Som nämndes i föregående kapitel anordnade National Institute of Standards and Technology (NIST) mellan 1997 och 2000 en tävling för att ta fram en ny standard för symmetrisk kryptering. **Rijndael-chiffret** visade sig vara det vinnande bidraget. Namnet är en ordlek på namnen på de belgiska upphovsmännen Vincent Rijmen och Joan Daemen.


Rijndael-chiffret är ett **blockchiffer**, vilket innebär att det finns en kärnalgoritm som kan användas med olika specifikationer för nyckellängder och blockstorlekar. Du kan sedan använda den med olika driftsätt för att konstruera krypteringsscheman.


Kommittén för NIST-tävlingen antog en begränsad version av Rijndael-chiffret - nämligen en som kräver 128-bitars blockstorlekar och nyckellängder på antingen 128 bitar, 192 bitar eller 256 bitar - som en del av **Advanced Encryption Standard (AES)**. Denna begränsade version av Rijndael-chiffret kan också användas i flera olika driftlägen. Specifikationen för standarden är den s.k. **Advanced Encryption Standard (AES)**.


För att visa hur Rijndael-krypteringen fungerar, kärnan i AES, ska jag illustrera processen för kryptering med en 128-bitars nyckel. Nyckelstorleken påverkar antalet rundor som hålls för varje krypteringsblock. För 128-bitarsnycklar krävs 10 rundor. Med 192 bitar och 256 bitar skulle det ha varit 12 respektive 14 rundor.


Dessutom kommer jag att anta att AES används i **ECB-läge**. Detta gör framställningen något enklare och spelar ingen roll för Rijndael-algoritmen. ECB-läget är förvisso inte säkert i praktiken eftersom det leder till deterministisk kryptering. Det säkra läge som oftast används med AES är **CBC** (Cipher Block Chaining).


Låt oss kalla nyckeln för $K_0$. Konstruktionen med ovanstående parametrar ser då ut som i *Figur 1*, där $M_i$ står för en del av klartextmeddelandet på 128 bitar och $C_i$ för en del av chiffertexten på 128 bitar. Padding läggs till i klartexten för det sista blocket, om klartexten inte kan delas jämnt med blockstorleken.



*Bild 1: AES-ECB med en 128-bitars nyckel*


![Figure 1: AES-ECB with a 128-bit key](assets/Figure5-1.webp "Figure 1: AES-ECB with a 128-bit key")


Varje 128-bitars textblock går igenom tio rundor i Rijndael-krypteringsschemat. Detta kräver en separat rundnyckel för varje runda ($K_1$ till $K_{10}$). Dessa skapas för varje omgång från den ursprungliga 128-bitarsnyckeln $K_0$ med hjälp av en **nyckelexpansionsalgoritm**. För varje textblock som ska krypteras använder vi alltså originalnyckeln $K_0$ samt tio separata rundnycklar. Observera att samma 11 nycklar används för varje 128-bitarsblock med klartext som ska krypteras.


Algoritmen för nyckelexpansion är lång och komplex. Att arbeta igenom den har liten didaktisk nytta. Du kan titta igenom nyckelexpansionsalgoritmen på egen hand om du vill. När de runda nycklarna har producerats kommer Rijndael-krypteringen att manipulera det första 128-bitarsblocket med klartext, $M_1$, som visas i *Figur 2*. Vi kommer nu att gå igenom dessa steg.


*Figur 2: Manipulering av $M_1$ med Rijndael-chiffer:*


**Runda 0:**


- XOR $M_1$ och $K_0$ för att producera $S_0$


---

**Runda n för n = {1,...,9}:**


- XOR $S_{n-1}$ och $K_n$
- Byte-substitution
- Skifta rader
- Mixa kolumner
- XOR $S$ och $K_n$ för att producera $S_n$


---

**Runda 10:**


- XOR $S_9$ och $K_{10}$
- Byte-substitution
- Skifta rader
- XOR $S$ och $K_{10}$ för att producera $S_{10}$
- $S_{10}$ = $C_1$



### Omgång 0


Rond 0 i Rijndael-krypteringen är enkel. En matris $S_0$ produceras genom en XOR-operation mellan 128-bitars klartext och den privata nyckeln. Det vill säga,



- $S_0 = M_1 \oplus K_0$


### Omgång 1


I runda 1 kombineras först matrisen $S_0$ med rundans nyckel $K_1$ med hjälp av en XOR-operation. Detta ger ett nytt tillstånd för $S$.


För det andra utförs operationen **byte substitution** på det aktuella tillståndet för $S$. Den fungerar genom att ta varje byte i 16-byte $S$-arrayen och ersätta den med en byte från en array som kallas **Rijndaels S-box**. Varje byte har en unik omvandling och ett nytt tillstånd för $S$ produceras som ett resultat. Rijndaels S-box visas i *Figur 3*.


*Bild 3: Rijndaels S-box*


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


Denna S-Box är en plats där abstrakt algebra spelar in i Rijndael-chiffret, särskilt **Galois-fält**.


Till att börja med definierar du varje möjligt byteelement 00 till FF som en 8-bitars vektor. Varje sådan vektor är ett element i **Galoisfältet GF(2^8)** där det irreducibla polynomet för moduloperationen är $x^8 + x^4 + x^3 + x + 1$. Galoisfältet med dessa specifikationer kallas också **Rijndaels finita fält**.


Därefter skapar vi för varje möjligt element i fältet vad som kallas **Nyberg S-Box**. I den här boxen mappas varje byte till sin **multiplikativa invers** (dvs. så att deras produkt är lika med 1). Vi mappar sedan dessa värden från Nybergs S-box till Rijndaels S-box med hjälp av **affintransformationen**.


Den tredje operationen på **S**-arrayen är operationen **shift rows**. Den tar tillståndet för **S** och listar alla de sexton byte i en matris. Fyllningen av matrisen börjar längst upp till vänster och arbetar sig runt genom att gå från topp till botten och sedan, varje gång en kolumn fylls, skifta en kolumn till höger och till toppen.


När matrisen för **S** har konstruerats flyttas de fyra raderna. Den första raden förblir oförändrad. Den andra raden flyttas en över till vänster. Den tredje flyttar två över till vänster. Den fjärde flyttar tre över till vänster. Ett exempel på denna process visas i *Figur 4*. Det ursprungliga tillståndet för **S** visas överst, och det resulterande tillståndet efter shift rows-operationen visas under det.


*Bild 4: Skifta till rad-operation*


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


I det fjärde steget dyker **Galois-fälten** upp igen. Till att börja med multipliceras varje kolumn i **S**-matrisen med kolumnen i 4 x 4-matrisen som ses i *Figur 5*. Men istället för att vara vanlig matrismultiplikation är det vektormultiplikation **modulo ett irreducibelt polynom**, $x^8 + x^4 + x^3 + x + 1$. De resulterande vektorkoefficienterna representerar de enskilda bitarna i en byte.


*Bild 5: Matris för blandningskolumner*


| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   |
| 03   | 01   | 01   | 02   |

Multiplikation av den första kolumnen i **S**-matrisen med 4 x 4-matrisen ovan ger resultatet i *Figur 6*.


*Figur 6: Multiplikation av den första kolumnen:*


$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$


Som ett nästa steg måste alla termer i matrisen omvandlas till polynom. Till exempel representerar F1 1 byte och skulle bli $x^7 + x^6 + x^5 + x^4 + 1$, och 03 representerar 1 byte och skulle bli $x + 1$.


Alla multiplikationer utförs sedan **modulo** $x^8 + x^4 + x^3 + x + 1$. Detta resulterar i en addition av fyra polynom i var och en av de fyra cellerna i kolumnen. Efter att ha utfört dessa additioner **modulo 2** får du fyra polynom. Vart och ett av dessa polynom representerar en 8-bitars sträng, eller 1 byte, av **S**. Vi kommer inte att utföra alla dessa beräkningar här på matrisen i *Figur 6* eftersom de är omfattande.


När den första kolumnen har bearbetats, bearbetas de tre andra kolumnerna i **S**-matrisen på samma sätt. Så småningom får man en matris med sexton bytes som kan omvandlas till en array.


Som ett sista steg kombineras matrisen **S** med den runda nyckeln igen i en **XOR**-operation. Detta ger tillståndet $S_1$. Det vill säga,



- $S_1 = S \oplus K_0$$


### Omgång 2 till 10


Runda 2 till 9 är bara en upprepning av runda 1, *mutatis mutandis*. Den sista omgången är mycket lik de föregående omgångarna, förutom att steget **mixa kolumner** elimineras. Det vill säga, omgång 10 utförs på följande sätt:



- $S_9 \oplus K_{10}$$
- Byte-substitution
- Skifta rader
- $S_{10} = S \oplus K_{10}$


Tillståndet $S_{10}$ är nu inställt på $C_1$, de första 128 bitarna av chiffertexten. Genom att fortsätta genom de återstående 128-bitars klartextblocken erhålls den fullständiga chiffertexten **C**.


### Rijndael-krypteringens operationer


Vad är resonemanget bakom de olika operationer som förekommer i Rijndael-chiffret?


Utan att gå in på detaljer bedöms krypteringssystem utifrån i vilken utsträckning de skapar förvirring och spridning. Om krypteringssystemet har en hög grad av **förvirring** innebär det att chiffertexten ser drastiskt annorlunda ut än klartexten. Om krypteringssystemet har en hög grad av **diffusion** innebär det att varje liten förändring av klartexten ger en drastiskt annorlunda chiffertext.


Anledningen till operationerna bakom Rijndael-chiffret är att de ger upphov till både en hög grad av förvirring och spridning. Förvirringen produceras av operationen Byte substitution, medan spridningen produceras av operationerna shift rows och mix columns.


# Asymmetrisk kryptografi

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>



## Problem med distribution och hantering av nycklar

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>


Precis som med symmetrisk kryptografi kan asymmetriska system användas för att säkerställa både sekretess och autentisering. I dessa system används dock två nycklar i stället för en: en privat och en offentlig nyckel.


Vi inleder vår undersökning med upptäckten av asymmetrisk kryptografi, i synnerhet de problem som ledde fram till den. Därefter diskuterar vi hur asymmetriska system för kryptering och autentisering fungerar på en hög nivå. Sedan introducerar vi Hash-funktioner, som är viktiga för att förstå asymmetriska autentiseringssystem och som även har relevans i andra kryptografiska sammanhang, t.ex. för de Hash-baserade meddelandeautentiseringskoder som vi diskuterade i kapitel 4.


___



Anta att Bob vill köpa en ny regnjacka från Jim's Sporting Goods, en onlineåterförsäljare av sportartiklar med miljontals kunder i Nordamerika. Det här blir hans första köp från dem och han vill använda sitt kreditkort. Så Bob måste först skapa ett konto hos Jim's Sporting Goods, vilket kräver att han skickar över personuppgifter som sin Address och kreditkortsinformation. Därefter kan han gå igenom de steg som krävs för att köpa regnkappan.


Bob och Jim's Sporting Goods kommer att vilja säkerställa att deras kommunikation är säker under hela denna process, med tanke på att Internet är ett öppet kommunikationssystem. De vill till exempel säkerställa att ingen potentiell angripare kan få reda på Bob:s kreditkorts- och Address-uppgifter, och att ingen potentiell angripare kan upprepa hans inköp eller skapa falska inköp för hans räkning.


Ett avancerat krypteringssystem med autentisering, som diskuterades i föregående kapitel, skulle säkert kunna göra kommunikationen mellan Bob och Jim's Sporting Goods säker. Men det finns helt klart praktiska hinder för att implementera ett sådant system.


För att illustrera dessa praktiska hinder kan vi anta att vi levde i en värld där det bara fanns verktyg för symmetrisk kryptografi. Vad skulle Jim's Sporting Goods och Bob då kunna göra för att garantera säker kommunikation?


Under dessa omständigheter skulle de stå inför betydande kostnader för att kommunicera säkert. Eftersom Internet är ett öppet kommunikationssystem kan de inte bara Exchange en uppsättning nycklar över det. Därför kommer Bob och en representant för Jim's Sporting Goods att behöva göra en nyckel Exchange personligen.


En möjlighet är att Jim's Sporting Goods skapar särskilda nyckelplatser för Exchange, där Bob och andra nya kunder kan hämta en uppsättning nycklar för säker kommunikation. Detta skulle naturligtvis medföra betydande organisatoriska kostnader och kraftigt minska effektiviteten med vilken nya kunder kan göra inköp.


Alternativt kan Jim's Sporting Goods skicka Bob ett par nycklar med en mycket pålitlig kurir. Detta är förmodligen mer effektivt än att organisera nyckel Exchange platser. Men det skulle fortfarande medföra betydande kostnader, särskilt om många kunder bara gör ett eller ett fåtal inköp.


Vidare tvingar ett symmetriskt system för autentiserad kryptering också Jim's Sporting Goods att lagra separata uppsättningar nycklar för alla sina kunder. Detta skulle vara en betydande praktisk utmaning för tusentals kunder, för att inte tala om miljoner.


För att förstå den senare punkten kan man anta att Jim's Sporting Goods ger varje kund samma nyckelknippa. Detta skulle göra det möjligt för varje kund - eller någon annan som kan få tag på detta nyckelpar - att läsa och till och med manipulera all kommunikation mellan Jim's Sporting Goods och dess kunder. Då kan man lika gärna inte använda kryptografi alls i sin kommunikation.


Även att upprepa en uppsättning nycklar för endast vissa kunder är en fruktansvärd säkerhetspraxis. Alla potentiella angripare kan försöka utnyttja den funktionen i systemet (kom ihåg att angripare antas veta allt om ett system utom nycklarna, i enlighet med Kerckhoffs princip)


Jim's Sporting Goods skulle alltså behöva lagra ett nyckelpar för varje kund, oavsett hur dessa nyckelpar distribueras. Detta innebär uppenbarligen flera praktiska problem.



- Jim's Sporting Goods skulle behöva lagra miljontals nyckelpar, en uppsättning för varje kund.
- Dessa nycklar måste vara ordentligt skyddade, eftersom de skulle vara ett säkert mål för hackare. Eventuella säkerhetsbrister skulle kräva upprepade kostsamma nyckelutbyten, antingen på speciella Exchange-platser eller via kurir.
- Alla kunder hos Jim's Sporting Goods måste förvara ett par nycklar på ett säkert sätt hemma. Förluster och stölder kommer att inträffa, vilket kräver en upprepning av nyckelutbyten. Kunderna skulle också behöva gå igenom denna process för alla andra onlinebutiker eller andra typer av enheter som de vill kommunicera och göra transaktioner med via Internet.


De två huvudutmaningarna som beskrivs ovan var mycket grundläggande fram till slutet av 1970-talet. De var kända som **nyckeldistributionsproblemet** respektive **nyckelhanteringsproblemet**.


Dessa problem hade naturligtvis alltid funnits och ofta skapat huvudbry i det förflutna. Militära styrkor, till exempel, var tvungna att ständigt distribuera böcker med nycklar för säker kommunikation till personal i fält till stora risker och kostnader. Men problemen blev allt värre i takt med att världen alltmer övergick till digital kommunikation på långa avstånd, särskilt för icke-statliga organisationer.


Om dessa problem inte hade lösts på 1970-talet hade det sannolikt inte funnits någon effektiv och säker shopping på Jim's Sporting Goods. Faktum är att större delen av vår moderna värld med praktisk och säker e-post, internetbank och shopping förmodligen bara skulle vara en avlägsen fantasi. Något som ens liknar Bitcoin skulle inte ha kunnat existera överhuvudtaget.


Så vad hände på 1970-talet? Hur är det möjligt att vi omedelbart kan göra inköp online och säkert surfa på World Wide Web? Hur är det möjligt att vi omedelbart kan skicka Bitcoins över hela världen från våra smarta telefoner?



## Nya riktningar inom kryptografi

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>


På 1970-talet hade problemen med nyckeldistribution och nyckelhantering fångat uppmärksamheten hos en grupp amerikanska akademiska kryptografer: Whitfield Diffie, Martin Hellman och Ralph Merkle. Trots att de flesta av deras kollegor var mycket skeptiska vågade de sig på att ta fram en lösning på problemet.


Åtminstone ett av de främsta motiven för deras satsning var att de förutsåg att öppen datakommunikation skulle komma att påverka vår värld på ett genomgripande sätt. Som Diffie och Helmann noterade 1976,


> Utvecklingen av datorstyrda kommunikationsnätverk utlovar enkel och billig kontakt mellan människor eller datorer på motsatta sidor av jorden, vilket ersätter det mesta av post och många utflykter med telekommunikation. För många tillämpningar måste dessa kontakter göras säkra mot både avlyssning och inmatning av illegitima meddelanden. För närvarande ligger dock lösningen av säkerhetsproblemen långt efter andra områden inom kommunikationstekniken. *Nutida kryptografi kan inte uppfylla kraven, eftersom dess användning skulle medföra så stora olägenheter för systemanvändarna att många av fördelarna med teleprocessing skulle försvinna.* [1]

Diffies, Hellmans och Merkles ihärdighet gav resultat. Den första publiceringen av deras resultat var en artikel av Diffie och Hellman 1976 med titeln "New Directions in Cryptography" Där presenterade de två nya sätt att lösa problemen med nyckeldistribution och nyckelhantering (Address).


Den första lösningen de erbjöd var ett fjärrprotokoll *key-Exchange*, det vill säga en uppsättning regler för Exchange av en eller flera symmetriska nycklar via en osäker kommunikationskanal. Detta protokoll är nu känt som *Diffie-Helmann-nyckel Exchange* eller *Diffie-Helmann-Merkle-nyckel Exchange*. [2]


Med Diffie-Helmann-nyckeln Exchange gör två parter först Exchange viss information offentlig på en osäker kanal, t.ex. Internet. På grundval av denna information skapar de sedan oberoende av varandra en symmetrisk nyckel (eller ett par symmetriska nycklar) för säker kommunikation. Båda parter skapar sina nycklar oberoende av varandra, men den information som de delade offentligt säkerställer att processen för att skapa nycklar ger samma resultat för dem båda.


Det är viktigt att notera att även om alla kan observera den information som utbyts offentligt av parterna via den osäkra kanalen, kan endast de två parter som deltar i informationen Exchange skapa symmetriska nycklar från den.


Detta låter naturligtvis helt kontraintuitivt. Hur kan två parter Exchange offentliggöra viss information som gör att bara de kan skapa symmetriska nycklar av den? Varför skulle någon annan som observerar informationen Exchange inte kunna skapa samma nycklar?


Det bygger naturligtvis på en del vacker matematik. Diffie-Helmann-nyckeln Exchange fungerar via en envägsfunktion med en fallucka. Låt oss diskutera innebörden av dessa två termer i tur och ordning.


Antag att du får en funktion $f(x)$ och resultatet $f(a) = y$, där $a$ är ett visst värde för $x$. Vi säger att $f(x)$ är en **envägsfunktion** om det är lätt att beräkna värdet $y$ när man får $a$ och $f(x)$, men det är beräkningsmässigt omöjligt att beräkna värdet $a$ när man får $y$ och $f(x)$. Namnet **envägsfunktion** kommer naturligtvis från det faktum att en sådan funktion bara är praktisk att beräkna i en riktning.


Vissa envägsfunktioner har vad som kallas en **trapdoor**. Även om det är praktiskt taget omöjligt att beräkna $a$ givet endast $y$ och $f(x)$, finns det en viss information $Z$ som gör det möjligt att beräkna $a$ från $y$. Denna information $Z$ är känd som **trapdoor**. Envägsfunktioner som har en fallucka kallas **trapdoor-funktioner**.


Vi kommer inte att gå in på detaljerna i Diffie-Helmann-nyckeln Exchange här. Men i huvudsak skapar varje deltagare viss information, varav en del delas offentligt och en del förblir hemlig. Varje part tar sedan sin hemliga information och den offentliga information som delas av den andra parten för att skapa en privat nyckel. Och på något mirakulöst sätt kommer båda parter att sluta med samma privata nyckel.


En part som bara observerar den offentligt delade informationen mellan de två parterna i en Diffie Helmann-nyckel Exchange kan inte replikera dessa beräkningar. De skulle behöva den privata informationen från en av de två parterna för att kunna göra det.


Även om den grundläggande versionen av Diffie-Helmann-nyckeln Exchange som presenterades i rapporten från 1976 inte är särskilt säker, används sofistikerade versioner av det grundläggande protokollet fortfarande i dag. Viktigast av allt är att varje nyckel Exchange-protokoll i den senaste versionen av transport Layer-säkerhetsprotokollet (version 1.3) i huvudsak är en berikad version av det protokoll som presenterades av Diffie och Hellman 1976. Säkerhetsprotokollet transport Layer är det dominerande protokollet för säkert utbyte av information som formaterats enligt http (Hypertext Transfer Protocol), standarden för utbyte av webbinnehåll.


Det är viktigt att notera att Diffie-Helmann-nyckeln Exchange inte är ett asymmetriskt system. Strängt taget kan man hävda att den tillhör symmetrisk nyckelkryptografi. Men eftersom både Diffie-Helmann-nyckeln Exchange och asymmetrisk kryptografi förlitar sig på enkelriktade talteoretiska funktioner med falluckor diskuteras de vanligtvis tillsammans.


Det andra sättet som Diffie och Helmann erbjöd Address för att lösa problemet med distribution och hantering av nycklar i sin artikel från 1976 var naturligtvis asymmetrisk kryptografi.


Till skillnad från deras presentation av Diffie-Hellman-nyckeln Exchange gav de bara de allmänna konturerna av hur asymmetriska kryptografiska system rimligen kan konstrueras. De erbjöd inte någon envägsfunktion som specifikt skulle kunna uppfylla de villkor som krävs för rimlig säkerhet i sådana system.


En praktisk implementering av ett asymmetriskt system hittades dock ett år senare av tre olika akademiska kryptografer och matematiker: Ronald Rivest, Adi Shamir och Leonard Adleman. [3] Kryptosystemet som de introducerade blev känt som **RSA-kryptosystemet** (efter deras efternamn).


De falluckefunktioner som används i asymmetrisk kryptografi (och Diffie Helmann-nyckeln Exchange) är alla relaterade till två huvudsakliga **beräkningsmässiga Hard-problem**: primfaktorisering och beräkning av diskreta logaritmer.


**Primfaktorisering** kräver, som namnet antyder, att ett heltal bryts ned i sina primfaktorer. RSA-problemet är det absolut mest välkända exemplet på ett kryptosystem som är relaterat till primtalsfaktorisering.


Det **diskreta logaritmproblemet** är ett problem som uppstår i cykliska grupper. Givet en generator i en viss cyklisk grupp kräver det att man beräknar den unika exponent som behövs för att producera ett annat element i gruppen från generatorn.


Diskreta logaritmbaserade system förlitar sig på två huvudtyper av cykliska grupper: multiplikativa grupper av heltal och grupper som inkluderar punkterna på elliptiska kurvor. Den ursprungliga Diffie Helmann-nyckeln Exchange som presenterades i "New Directions in Cryptography" arbetar med en cyklisk multiplikativ grupp av heltal. Bitcoin:s digitala signaturalgoritm och det nyligen introducerade Schnorr-signaturschemat (2021) är båda baserade på det diskreta logaritmproblemet för en viss cyklisk grupp på elliptiska kurvor.


Därefter följer en översiktlig genomgång av sekretess och autentisering i asymmetriska sammanhang. Innan vi gör det måste vi dock göra en kort historisk notering.


Det verkar nu troligt att en grupp brittiska kryptografer och matematiker som arbetade för Government Communications Headquarters (GCHQ) oberoende av varandra hade gjort de ovan nämnda upptäckterna några år tidigare. Denna grupp bestod av James Ellis, Clifford Cocks och Malcolm Williamson.


Enligt deras egna och GCHQ:s uppgifter var det James Ellis som först utvecklade konceptet med kryptografi med offentlig nyckel 1969. Det påstås att Clifford Cocks sedan upptäckte det kryptografiska systemet RSA 1973 och Malcolm Williamson konceptet Diffie Helmann-nyckeln Exchange 1974. [4] Deras upptäckter ska dock inte ha avslöjats förrän 1997, med tanke på den hemliga karaktären hos det arbete som utfördes på GCHQ.



**Noteringar:**


[1] Whitfield Diffie och Martin Hellman, "New directions in cryptography", _IEEE Transactions on Information Theory_ IT-22 (1976), s. 644-654, på s. 644.


[2] Ralph Merkle diskuterar också ett viktigt Exchange-protokoll i "Secure communications over insecure channels", _Communications of the Association for Computing Machinery_, 21 (1978), 294-99. Även om Merkle faktiskt skickade in denna artikel före artikeln av Diffie och Hellman, publicerades den senare. Merkles lösning är inte exponentiellt säker, till skillnad från Diffie-Hellmans.


[3] Ron Rivest, Adi Shamir och Leonard Adleman, "A method for obtaining digital signatures and public-key cryptosystems", _Communications of the Association for Computing Machinery_, 21 (1978), s. 120-26.


[4] En bra historik över dessa upptäckter ges av Simon Singh, _The Code Book_, Fourth Estate (London, 1999), kapitel 6.





## Asymmetrisk kryptering och autentisering

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>


En översikt över **asymmetrisk kryptering** med hjälp av Bob och Alice ges i *Figur 1*.


Alice skapar först ett nyckelpar som består av en offentlig nyckel ($K_P$) och en privat nyckel ($K_S$), där "P" i $K_P$ står för "offentlig" och "S" i $K_S$ för "hemlig". Hon delar sedan ut den publika nyckeln fritt till andra. Vi kommer att återkomma till detaljerna i denna distributionsprocess lite senare. Men nu antar vi att vem som helst, inklusive Bob, på ett säkert sätt kan få tag på Alice:s publika nyckel $K_P$.


Vid ett senare tillfälle vill Bob skriva ett meddelande $M$ till Alice. Eftersom det innehåller känslig information vill han att innehållet ska förbli hemligt för alla utom Alice. Därför krypterar Bob först sitt meddelande $M$ med hjälp av $K_P$. Han skickar sedan den resulterande chiffertexten $C$ till Alice, som dekrypterar $C$ med $K_S$ för att producera det ursprungliga meddelandet $M$.


*Figur 1: Asymmetrisk kryptering*


![Figure 1: Asymmetric encryption](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")



En motståndare som avlyssnar Bob:s och Alice:s kommunikation kan observera $C$. Hon känner också till $K_P$ och krypteringsalgoritmen $E(\cdot)$. Det är dock viktigt att påpeka att denna information inte gör det möjligt för angriparen att dekryptera chiffertexten $C$. Dekryptering kräver specifikt $K_S$, som angriparen inte har.


Symmetriska krypteringssystem måste i allmänhet vara säkra mot en angripare som kan kryptera klartextmeddelanden på ett giltigt sätt (s.k. chosen-ciphertext attack security). Det är dock inte utformat med det uttryckliga syftet att tillåta att en angripare eller någon annan skapar sådana giltiga chiffertexter.


Detta står i skarp kontrast till ett asymmetriskt krypteringssystem, där hela syftet är att tillåta vem som helst, inklusive angripare, att producera giltiga chiffertexter. Asymmetriska krypteringsscheman kan därför kallas **chiffer med flera åtkomstmöjligheter**.


För att bättre förstå vad som händer kan man föreställa sig att Bob i stället för att skicka ett meddelande elektroniskt vill skicka ett fysiskt brev i hemlighet. Ett sätt att säkerställa sekretessen skulle kunna vara att Alice skickar ett säkert hänglås till Bob, men behåller nyckeln till att låsa upp det. Efter att ha skrivit sitt brev kunde Bob lägga brevet i en låda och stänga den med Alice:s hänglås. Han kan sedan skicka den låsta lådan med meddelandet till Alice som har nyckeln till att låsa upp den.


Bob kan visserligen låsa hänglåset, men varken han eller någon annan person som tar emot lådan kan bryta upp hänglåset om det verkligen är säkert. Endast Alice kan låsa upp det och se innehållet i Bob:s brev eftersom hon har nyckeln.


Ett asymmetriskt krypteringssystem är, grovt sett, en digital version av denna process. Hänglåset kan liknas vid den publika nyckeln och hänglåsnyckeln kan liknas vid den privata nyckeln. Eftersom hänglåset är digitalt är det dock mycket enklare och inte så kostsamt för Alice att distribuera det till alla som kan tänkas vilja skicka hemliga meddelanden till henne.


För autentisering i den asymmetriska miljön använder vi **digitala signaturer**. Dessa har alltså samma funktion som meddelandeautentiseringskoder i den symmetriska inställningen. En översikt över digitala signaturer ges i *Figur 2*.


Bob skapar först ett nyckelpar, bestående av den offentliga nyckeln ($K_P$) och den privata nyckeln ($K_S$), och distribuerar sin offentliga nyckel. När han vill skicka ett autentiserat meddelande till Alice tar han först sitt meddelande $M$ och sin privata nyckel för att skapa en **digital signatur** $D$. Bob skickar sedan Alice sitt meddelande tillsammans med den digitala signaturen.


Alice lägger in meddelandet, den publika nyckeln och den digitala signaturen i en **verifieringsalgoritm**. Denna algoritm producerar antingen **true** för en giltig signatur, eller **false** för en ogiltig signatur.


En digital signatur är, som namnet tydligt antyder, den digitala motsvarigheten till en skriftlig signatur på brev, kontrakt och så vidare. Faktum är att en digital signatur oftast är mycket säkrare. Med lite ansträngning kan du förfalska en skriftlig signatur, en process som underlättas av det faktum att skriftliga signaturer ofta inte är noggrant verifierade. En säker digital signatur är dock, precis som en säker autentiseringskod för meddelanden, **existentiellt oförfalskbar**: det vill säga, med ett säkert digitalt signaturschema kan ingen skapa en signatur för ett meddelande som klarar verifieringsproceduren, såvida de inte har den privata nyckeln.


*Figur 2: Asymmetrisk autentisering*


![Figure 2: Asymmetric authentication](assets/Figure6-2.webp "Figure 2: Asymmetric authentication")



Precis som med asymmetrisk kryptering ser vi en intressant kontrast mellan digitala signaturer och koder för meddelandeautentisering. I det senare fallet kan verifieringsalgoritmen endast användas av en av de parter som har insyn i den säkra kommunikationen. Detta beror på att den kräver en privat nyckel. I den asymmetriska inställningen kan dock vem som helst verifiera en digital signatur $S$ gjord av Bob.


Allt detta gör digitala signaturer till ett mycket kraftfullt verktyg. Det utgör till exempel grunden för att skapa signaturer på kontrakt som kan verifieras för juridiska ändamål. Om Bob hade gjort en signatur på en Contract i Exchange ovan, kan Alice visa meddelandet $M$, Contract och signaturen $S$ för en domstol. Domstolen kan sedan verifiera signaturen med hjälp av Bob:s publika nyckel. [5]


Ett annat exempel är digitala signaturer, som är en viktig aspekt av säker distribution av programvara och programuppdateringar. Denna typ av offentlig verifierbarhet skulle aldrig kunna skapas med hjälp av enbart autentiseringskoder för meddelanden.


Som ett sista exempel på kraften i digitala signaturer kan vi ta Bitcoin. En av de vanligaste missuppfattningarna om Bitcoin, särskilt i media, är att transaktionerna är krypterade: det är de inte. Istället arbetar Bitcoin-transaktioner med digitala signaturer för att garantera säkerheten.


Bitcoins finns i satser som kallas outnyttjade transaktionsutgångar (eller **UTXO:s**). Anta att du får tre betalningar på en viss Bitcoin Address för 2 bitcoins vardera. Tekniskt sett har du nu inte 6 bitcoins på den Address. Istället har du tre satser med 2 bitcoins som är låsta av ett kryptografiskt problem som är associerat med den Address. För varje betalning du gör kan du använda en, två eller alla tre av dessa batcher, beroende på hur mycket du behöver för transaktionen.


Beviset för Ownership över outnyttjade transaktionsutgångar visas vanligtvis via en eller flera digitala signaturer. Bitcoin fungerar just eftersom giltiga digitala signaturer på oanvända transaktionsutgångar är beräkningsmässigt omöjliga att göra, såvida du inte har tillgång till den hemliga information som krävs för att göra dem.


För närvarande innehåller Bitcoin-transaktioner transparent all information som måste verifieras av deltagare i nätverket, till exempel ursprunget till de outnyttjade transaktionsutgångar som används i transaktionen. Även om det är möjligt att dölja en del av denna information och ändå tillåta verifiering (som vissa alternativa kryptovalutor som Monero gör), skapar detta också särskilda säkerhetsrisker.


Det uppstår ibland förvirring kring digitala signaturer och skriftliga signaturer som fångas digitalt. I det senare fallet tar du en bild av din skriftliga underskrift och klistrar in den i ett elektroniskt dokument, t.ex. en anställning Contract. Detta är dock inte en digital signatur i kryptografisk mening. Den senare är bara ett långt nummer som bara kan produceras genom att man har en privat nyckel.


Precis som i inställningen för symmetrisk nyckel kan du också använda asymmetriska krypterings- och autentiseringsscheman tillsammans. Liknande principer gäller. Först och främst bör du använda olika privat-offentliga nyckelpar för kryptering och för att skapa digitala signaturer. Dessutom bör du först kryptera ett meddelande och sedan autentisera det.


I många tillämpningar används asymmetrisk kryptografi inte under hela kommunikationsprocessen. Istället används den vanligtvis bara för att *Exchange symmetriska nycklar* mellan de parter som de faktiskt kommer att kommunicera med.


Detta gäller t.ex. när du köper varor på nätet. Genom att känna till säljarens publika nyckel kan hon skicka digitalt signerade meddelanden till dig som du kan verifiera äktheten på. På grundval av detta kan du följa ett av flera protokoll för utbyte av symmetriska nycklar för att kommunicera på ett säkert sätt.


Det främsta skälet till att denna metod används så ofta är att asymmetrisk kryptografi är mycket mindre effektiv än symmetrisk kryptografi när det gäller att uppnå en viss säkerhetsnivå. Detta är en av anledningarna till att vi fortfarande behöver symmetrisk kryptografi vid sidan av offentlig kryptografi. Dessutom är symmetrisk kryptografi mycket mer naturlig i vissa tillämpningar, t.ex. när en datoranvändare krypterar sina egna data.


Så exakt hur löser digitala signaturer och kryptering med publik nyckel Address problemen med nyckeldistribution och nyckelhantering?


Det finns inte bara ett svar här. Asymmetrisk kryptografi är ett verktyg och det finns inte ett sätt att använda det verktyget. Men låt oss ta vårt tidigare exempel från Jim's Sporting Goods för att visa hur frågorna vanligtvis skulle hanteras i det här exemplet.


Till att börja med skulle Jim's Sporting Goods förmodligen vända sig till en **certifikatutfärdare**, en organisation som stöder distribution av offentliga nycklar. Certifikatutfärdaren skulle registrera vissa uppgifter om Jim's Sporting Goods och ge den en publik nyckel. Den skulle sedan skicka Jim's Sporting Goods ett certifikat, ett så kallat **TLS/SSL-certifikat**, med Jim's Sporting Goods publika nyckel digitalt signerad med certifikatutfärdarens egen publika nyckel. På så sätt bekräftar certifikatutfärdaren att en viss publik nyckel verkligen tillhör Jim's Sporting Goods.


Nyckeln till att förstå denna process med TLS/SSL-certifikat är att även om du i allmänhet inte har Jim's Sporting Goods offentliga nyckel lagrad någonstans på din dator, lagras de offentliga nycklarna för erkända certifikatmyndigheter faktiskt i din webbläsare eller i ditt operativsystem. Dessa lagras i vad som kallas **rotcertifikat**.


När Jim's Sporting Goods förser dig med sitt TLS/SSL-certifikat kan du därför verifiera certifikatutfärdarens digitala signatur via ett rotcertifikat i din webbläsare eller ditt operativsystem. Om signaturen är giltig kan du vara relativt säker på att den publika nyckeln på certifikatet verkligen tillhör Jim's Sporting Goods. På grundval av detta är det enkelt att ställa in ett protokoll för säker kommunikation med Jim's Sporting Goods.


Nyckeldistributionen har nu blivit mycket enklare för Jim's Sporting Goods. Det är inte Hard att se att nyckelhanteringen också har blivit mycket förenklad. Istället för att behöva lagra tusentals nycklar behöver Jim's Sporting Goods bara lagra en privat nyckel som gör det möjligt att göra signaturer för den publika nyckeln på sitt SSL-certifikat. Varje gång en kund kommer till Jim's Sporting Goods webbplats kan de upprätta en säker kommunikationssession från den här publika nyckeln. Kunderna behöver inte heller lagra någon information (förutom de offentliga nycklarna till erkända certifikatutfärdare i operativsystemet och webbläsaren).


**Noteringar:**


[5] Alla system som försöker uppnå oavvislighet, det andra temat som vi diskuterade i kapitel 1, kommer i grunden att behöva involvera digitala signaturer.




## Hash funktioner

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>


Hash-funktioner är vanligt förekommande inom kryptografi. De är varken symmetriska eller asymmetriska system, utan faller inom en egen kryptografisk kategori.


Vi stötte redan på Hash-funktioner i kapitel 4 i samband med skapandet av Hash-baserade autentiseringsmeddelanden. De är också viktiga i samband med digitala signaturer, men av en något annorlunda anledning: Digitala signaturer görs nämligen vanligtvis över Hash-värdet för ett visst (krypterat) meddelande, snarare än det faktiska (krypterade) meddelandet. I det här avsnittet kommer jag att ge en mer ingående introduktion av Hash-funktioner.


Låt oss börja med att definiera en Hash-funktion. En **Hash-funktion** är en effektivt beräkningsbar funktion som tar indata av godtycklig storlek och ger utdata med fast längd.


En **kryptografisk Hash-funktion** är bara en Hash-funktion som är användbar för tillämpningar inom kryptografi. Utdata från en kryptografisk Hash-funktion kallas vanligtvis **Hash**, **Hash-värde** eller **meddelandesammanställning**.


I kryptografisammanhang avser en "Hash-funktion" vanligtvis en kryptografisk Hash-funktion. Jag kommer att anta den praxisen från och med nu.


Ett exempel på en populär Hash-funktion är **SHA-256** (secure Hash algorithm 256). Oavsett storleken på indata (t.ex. 15 bitar, 100 bitar eller 10 000 bitar) kommer denna funktion att ge ett 256-bitars Hash-värde. Nedan kan du se några exempel på utdata från SHA-256-funktionen.


"Hello": `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`


"52398": `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`


"Kryptografi är kul": `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`


Alla utdata är exakt 256 bitar utskrivna i hexadecimalt format (varje hexsiffra kan representeras av fyra binära siffror). Så även om du hade lagt in Tolkiens bok "Sagan om ringen" i SHA-256-funktionen skulle utmatningen fortfarande vara 256 bitar.


Hash-funktioner som SHA-256 används för olika ändamål inom kryptografi. Vilka egenskaper som krävs av en Hash-funktion beror på sammanhanget för en viss tillämpning. Det finns två huvudsakliga egenskaper som generellt önskas av Hash-funktioner inom kryptografi: [6]


1.	Motståndskraft mot kollisioner

2.	Gömd


En Hash-funktion $H$ sägs vara **kollisionsresistent** om det är omöjligt att hitta två värden, $x$ och $y$, så att $x \neq y$, men ändå $H(x) = H(y)$.


Kollisionsresistenta Hash-funktioner är viktiga t.ex. vid verifiering av programvara. Anta att du vill ladda ner Windows-versionen av Bitcoin Core 0.21.0 (ett serverprogram för bearbetning av Bitcoin-nätverkstrafik). De viktigaste stegen du skulle behöva ta för att verifiera programvarans legitimitet är följande:


1.	Du måste först ladda ner och importera de offentliga nycklarna för en eller flera bidragsgivare Bitcoin Core till programvara som kan verifiera digitala signaturer (t.ex. Kleopetra). Du kan hitta dessa publika nycklar [här](https://github.com/Bitcoin/Bitcoin/blob/master/contrib/builder-keys/keys.txt). Vi rekommenderar att du verifierar programvaran Bitcoin Core med de publika nycklarna från flera bidragsgivare.

2.	Därefter måste du verifiera de offentliga nycklar som du importerade. Åtminstone ett steg du bör ta är att verifiera att de offentliga nycklar du hittade är desamma som publicerats på olika andra platser. Du kan till exempel konsultera de personliga webbsidorna, Twitter-sidorna eller Github-sidorna för de personer vars offentliga nycklar du importerade. Vanligtvis görs denna jämförelse av publika nycklar genom att jämföra en kort Hash av den publika nyckeln, ett så kallat fingeravtryck.

3.	Därefter måste du ladda ner den körbara filen för Bitcoin Core från deras [webbplats] (www.bitcoincore.org). Det kommer att finnas paket tillgängliga för operativsystemen Linux, Windows och MAC.

4.	Därefter måste du leta reda på två releasefiler. Den första innehåller den officiella SHA-256 Hash för den körbara filen du laddade ner tillsammans med hasharna över alla andra paket som släpptes. En annan releasefil kommer att innehålla signaturerna från olika bidragsgivare över releasefilen med paketets hash. Båda dessa utgivningsfiler bör finnas på Bitcoin Core-webbplatsen.

5.	 Därefter måste du beräkna SHA-256 Hash för den körbara filen som du laddade ner från Bitcoin Core-webbplatsen på din egen dator. Du jämför sedan detta resultat med det för det officiella paketet Hash för den körbara filen. De bör vara desamma.

6.	Slutligen måste du verifiera att en eller flera av de digitala signaturerna över utgivningsfilen med de officiella pakethasharna verkligen motsvarar en eller flera offentliga nycklar som du importerade (utgåvor av Bitcoin Core signeras inte alltid av alla). Du kan göra detta med ett program som Kleopetra.


Denna process för programvaruverifiering har två huvudfördelar. För det första säkerställs att det inte förekom några överföringsfel vid nedladdning från Bitcoin Cores webbplats. För det andra säkerställer det att ingen angripare kan ha fått dig att ladda ner modifierad, skadlig kod, antingen genom att hacka Bitcoin Core-webbplatsen eller genom att avlyssna trafik.


Exakt hur skyddar verifieringsprocessen för programvara ovan mot dessa problem?


Om du noggrant verifierade de offentliga nycklar du importerade, kan du vara ganska säker på att dessa nycklar faktiskt är deras och inte har äventyrats. Med tanke på att digitala signaturer har existentiell oförfalskbarhet vet du att endast dessa bidragsgivare kunde ha gjort en digital signatur över de officiella pakethasharna i utgivningsfilen.


Anta att signaturerna på releasefilen som du hämtade har checkat ut. Du kan nu jämföra Hash-värdet som du beräknade lokalt för den Windows-körbara filen som du laddade ner med det som ingår i den korrekt signerade releasefilen. Som du vet är SHA-256 Hash-funktionen kollitionsresistent, en matchning innebär att din körbara fil är exakt densamma som den officiella körbara filen.


Låt oss nu gå vidare till den andra gemensamma egenskapen för Hash-funktioner: **döljande**. En Hash-funktion $H$ sägs ha egenskapen att gömma sig om det för en slumpmässigt vald $x$ från ett mycket stort intervall är omöjligt att hitta $x$ när man bara får $H(x)$.


Nedan kan du se SHA-256-utdata från ett meddelande som jag skrev. För att säkerställa tillräcklig slumpmässighet innehöll meddelandet en slumpmässigt genererad teckensträng i slutet. Eftersom SHA-256 har en döljande egenskap skulle ingen kunna dechiffrera det här meddelandet.



- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`


Men jag kommer inte att lämna dig i ovisshet tills SHA-256 blir svagare. Det ursprungliga meddelandet jag skrev var som följer:



- "Det här är ett mycket slumpmässigt meddelande, eller i alla fall ganska slumpmässigt. Den här inledande delen är inte det, men jag kommer att avsluta med några relativt slumpmässiga tecken för att säkerställa ett mycket oförutsägbart meddelande. XLWz4dVG3BxUWm7zQ9qS".


Ett vanligt sätt att använda Hash-funktioner med den dolda egenskapen är i lösenordshantering (kollisionsmotstånd är också viktigt för denna applikation). Alla anständiga kontobaserade onlinetjänster som Facebook eller Google lagrar inte dina lösenord direkt för att hantera åtkomst till ditt konto. Istället lagrar de bara en Hash av det lösenordet. Varje gång du fyller i ditt lösenord i en webbläsare beräknas först en Hash. Endast denna Hash skickas till tjänsteleverantörens server och jämförs med den Hash som lagras i back-end-databasen. Den dolda egenskapen kan bidra till att säkerställa att angripare inte kan återställa den från Hash-värdet.


Lösenordshantering via hash fungerar naturligtvis bara om användarna faktiskt väljer svåra lösenord. Den dolda egenskapen förutsätter att x väljs slumpmässigt från ett mycket stort intervall. Att välja lösenord som "1234", "mypassword" eller ditt födelsedatum ger inte någon verklig säkerhet. Det finns långa listor med vanliga lösenord och deras hashvärden som angripare kan utnyttja om de någonsin får tag på Hash av ditt lösenord. Den här typen av attacker kallas **ordboksattacker**. Om angriparna känner till några av dina personuppgifter kan de också försöka sig på några kvalificerade gissningar. Därför behöver du alltid långa, säkra lösenord (helst långa, slumpmässiga strängar från en lösenordshanterare).


Ibland kan en applikation behöva en Hash-funktion som har både kollisionsmotstånd och döljande egenskaper. Men absolut inte alltid. Den verifieringsprocess för programvara som vi diskuterade kräver till exempel bara att Hash-funktionen visar kollisionsmotstånd, döljande är inte viktigt.


Kollisionsmotstånd och döljande är de viktigaste egenskaperna för Hash-funktioner inom kryptografi, men i vissa tillämpningar kan även andra typer av egenskaper vara önskvärda.



**Noteringar:**


[6] Terminologin "dölja" är inte vanligt språkbruk, utan hämtad specifikt från Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller och Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), kapitel 1.



# RSA-kryptosystemet

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>




## Faktoriseringsproblemet

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>


Medan symmetrisk kryptografi vanligtvis är ganska intuitiv för de flesta människor, är detta vanligtvis inte fallet med asymmetrisk kryptografi. Även om du troligen känner dig bekväm med beskrivningen på hög nivå i de tidigare avsnitten undrar du förmodligen vad envägsfunktioner är och hur de används för att konstruera asymmetriska system.


I det här kapitlet kommer jag att skingra en del av mystiken kring asymmetrisk kryptografi genom att titta närmare på ett specifikt exempel, nämligen RSA-kryptosystemet. I det första avsnittet kommer jag att introducera faktoriseringsproblemet som RSA-problemet bygger på. Därefter följer ett antal viktiga resultat från talteorin. I det sista avsnittet sammanställer vi denna information för att förklara RSA-problemet och hur detta kan användas för att skapa asymmetriska kryptografiska system.


Det är ingen lätt uppgift att ge vår diskussion detta djup. Det kräver att man introducerar en hel del talteoretiska satser och teorem. Men låt inte matematiken avskräcka dig. Att arbeta igenom denna diskussion kommer avsevärt att förbättra din förståelse för vad som ligger till grund för asymmetrisk kryptografi och är en värdefull investering.


Låt oss nu först gå över till faktoriseringsproblemet.


___



När du multiplicerar två tal, t.ex. $a$ och $b$, kallar vi talen $a$ och $b$ för **faktorer** och resultatet för **produkt**. Försök att skriva ett tal $N$ till multiplikationen av två eller flera faktorer kallas **faktorisering** eller **faktorisering**. [1] Du kan kalla alla problem som kräver detta för ett **faktoriseringsproblem**.


För cirka 2.500 år sedan upptäckte den grekiske matematikern Euklides av Alexandria en viktig sats om faktorisering av heltal. Den kallas allmänt för **den unika faktoriseringssatsen** och säger följande:


**Sats 1**. Varje heltal $N$ som är större än 1 är antingen ett primtal eller kan uttryckas som en produkt av primfaktorer.


Allt den senare delen av detta påstående innebär är att du kan ta vilket icke-primtal heltal $N$ som helst som är större än 1 och skriva ut det som en multiplikation av primtal. Nedan följer flera exempel på heltal som inte är primtal och som skrivs som produkten av primtalsfaktorer.



- $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$$
- $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$$
- $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$$


För alla de tre heltalen ovan är det relativt enkelt att beräkna deras primfaktorer, även om du bara får $N$. Man börjar med det minsta primtalet, nämligen 2, och ser hur många gånger heltalet $N$ är delbart med det. Sedan går man vidare och testar hur många gånger $N$ är delbart med 3, 5, 7 och så vidare. Du fortsätter denna process tills ditt heltal $N$ är skrivet som produkten av endast primtal.


Ta till exempel heltalet 84. Nedan ser du hur vi går tillväga för att bestämma dess primfaktorer. I varje steg tar vi ut den minsta återstående primfaktorn (till vänster) och bestämmer den restterm som ska faktoriseras. Vi fortsätter tills resttermen också är ett primtal. Vid varje steg visas den aktuella faktoriseringen av 84 längst till höger.



- Primfaktor = 2: restterm = 42 ($84 = 2 \cdot 42$)
- Primfaktor = 2: restterm = 21 ($84 = 2 \cdot 2 \cdot 21$)
- Primfaktor = 3: restterm = 7 ($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
- Eftersom 7 är ett primtal blir resultatet $2 \cdot 2 \cdot 3 \cdot 7$, eller $2^2 \cdot 3 \cdot 7$.


Antag nu att $N$ är mycket stort. Hur svårt skulle det vara att reducera $N$ till dess primfaktorer?


Det beror verkligen på $N$. Anta till exempel att $N$ är 50 450 400. Även om detta antal ser skrämmande ut är beräkningarna inte så komplicerade och kan enkelt göras för hand. Som ovan börjar du bara med 2 och arbetar dig framåt. Nedan kan du se resultatet av denna process på ett liknande sätt som ovan.



- 2: 25 225 200 (50 450 400 $ = 2 \cdot 25 225 200 $)
- 2: 12 612 600 (50 450 400 $ = 2^2 \cdot 12 612 600 $)
- 2: 6 306 300 (50 450 400 $ = 2^3 \cdot 6 306 300 $)
- 2: 3 153 150 (50 450 400 $ = 2^4 \cdot 3 153 150 $)
- 2: 1 576 575 (50 450 400 $ = 2^5 \cdot 1 576 575 $)
- 3: 525,525 ($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
- 3: 175 175 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 175 175 $)
- 5: 35 035 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 5 \cdot 35 035$)
- 5: 7 007 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 007 $)
- 7: 1 001 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1 001 $)
- 7: 143 ($50 450 400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
- 11: 13 (50 450 400 dollar = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- Eftersom 13 är ett primtal blir resultatet $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.


Att räkna ut detta problem för hand tar en viss tid. En dator skulle naturligtvis kunna göra allt detta på en bråkdel av en sekund. Faktum är att en dator ofta till och med kan faktorisera extremt stora heltal på en bråkdel av en sekund.


Det finns dock vissa undantag. Antag att vi först slumpmässigt väljer två mycket stora primtal. Det är vanligt att kalla dessa $p$ och $q$, och jag kommer att använda mig av det här.


Låt oss för konkretionens skull säga att $p$ och $q$ båda är 1024-bitars primtal, och att de verkligen kräver minst 1024 bitar för att kunna representeras (så den första biten måste vara 1). Så till exempel 37 kan inte vara ett av primtalen. Du kan förvisso representera 37 med 1024 bitar. Men det är uppenbart att *du inte behöver* så många bitar för att representera det. Du kan representera 37 med vilken sträng som helst som har 6 bitar eller mer. (I 6 bitar skulle 37 representeras som $100101$).


Det är viktigt att förstå hur stora $p$ och $q$ är om de väljs enligt villkoren ovan. Som ett exempel har jag valt ett slumpmässigt primtal som behöver minst 1024 bitar för representation nedan.



- 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589


Antag nu att vi efter att slumpmässigt ha valt primtalen $p$ och $q$ multiplicerar dem för att få ett heltal $N$. Detta senare heltal är därför ett 2048-bitars tal som kräver minst 2048 bitar för sin representation. Det är mycket, mycket större än både $p$ och $q$.


Antag att du bara ger en dator $N$ och ber den att hitta de två 1024-bitars primfaktorerna till $N$. Sannolikheten för att datorn upptäcker $p$ och $q$ är extremt liten. Man kan säga att det är omöjligt för alla praktiska ändamål. Detta gäller även om man skulle använda en superdator eller till och med ett nätverk av superdatorer.


Till att börja med antar vi att datorn försöker lösa problemet genom att cykla genom 1024 bitnummer och i varje fall testa om de är primtal och om de är faktorer av $N$. Den uppsättning primtal som ska testas är då ungefär $1,265 \cdot 10^{305}$. [2]


Även om man tar alla datorer på planeten och låter dem försöka hitta och testa 1024-bitars primtal på det här sättet, skulle en chans på 1 på en miljard att lyckas hitta en primfaktor av $N$ kräva en beräkningsperiod som är mycket längre än universums ålder.


Nu kan en dator i praktiken göra bättre ifrån sig än den grova procedur som just beskrivits. Det finns flera algoritmer som datorn kan tillämpa för att snabbare komma fram till en faktorisering. Poängen är dock att även om man använder dessa effektivare algoritmer är datorns uppgift fortfarande beräkningsmässigt ogenomförbar. [3]


Det är viktigt att påpeka att svårigheten med faktoriseringen under de förhållanden som just beskrivits vilar på antagandet att det inte finns några beräkningseffektiva algoritmer för att beräkna primfaktorer. Vi kan faktiskt inte bevisa att det inte finns någon effektiv algoritm. Ändå är detta antagande mycket rimligt: trots omfattande ansträngningar under hundratals år har vi ännu inte hittat en sådan beräkningseffektiv algoritm.


Därför kan faktoriseringsproblemet, under vissa omständigheter, rimligen antas vara ett Hard-problem. När $p$ och $q$ är mycket stora primtal är deras produkt $N$ inte svår att beräkna; men faktorisering endast givet $N$ är praktiskt taget omöjligt.



**Noteringar:**


[1] Faktorisering kan också vara viktigt för att arbeta med andra typer av matematiska objekt än tal. Till exempel kan det vara användbart att faktorisera polynomuttryck som $x^2 - 2x + 1$. I vår diskussion kommer vi bara att fokusera på faktorisering av tal, särskilt heltal.


[2] Enligt **primtalsteoremet** är antalet primtal som är mindre än eller lika med $N$ ungefär $N/\LN(N)$. Detta innebär att du kan uppskatta antalet primtal av längden 1024 bitar genom att:


$$ \frac{2^{1024}}{\LN(2^{1024})} - \frac{2^{1023}}{\LN(2^{1023})} $$


...vilket motsvarar ungefär 1,265 gånger 10^{305}$.


[3] Detsamma gäller för diskreta logaritmproblem. Det är därför asymmetriska konstruktioner fungerar med mycket större nycklar än symmetriska kryptografiska konstruktioner.




## Antalsteoretiska resultat

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>


Tyvärr kan faktoriseringsproblemet inte användas direkt för asymmetriska kryptografiska system. Vi kan dock använda ett mer komplext men relaterat problem för detta ändamål: RSA-problemet.


För att förstå RSA-problemet måste vi förstå ett antal teorem och satser från talteorin. Dessa presenteras i detta avsnitt i tre underavsnitt: (1) N:s ordning, (2) invertibilitet modulo N och (3) Eulers sats.


En del av materialet i de tre underavsnitten har redan presenterats i *Kapitel 3*. Men för enkelhetens skull kommer jag här att återge det materialet.



### Ordningsföljden för N


Ett heltal $a$ är ett **koprimtal** eller ett **relativt primtal** till ett heltal $N$, om den största gemensamma divisorn mellan dem är 1. Även om 1 enligt konvention inte är ett primtal, är det ett koprimtal till varje heltal (liksom $-1$).


Tänk till exempel på fallet när $a = 18$ och $N = 37$. Dessa är helt klart coprimes. Det största heltal som delar sig i både 18 och 37 är 1. Tänk däremot på fallet när $a = 42$ och $N = 16$. Dessa är helt klart inte coprimes. Båda talen är delbara med 2, som är större än 1.


Vi kan nu definiera ordningen för $N$ på följande sätt. Antag att $N$ är ett heltal större än 1. **Ordningen av N** är då antalet av alla koprim med $N$ som är sådana att för varje koprim $a$ gäller följande villkor: $1 \leq a < N$.


Om till exempel $N = 12$ är 1, 5, 7 och 11 de enda coprimes som uppfyller kravet ovan. Därför är ordningen av 12 lika med 4.


Antag att $N$ är ett primtal. Då är varje heltal som är mindre än $N$ men större än eller lika med 1 coprim med det. Detta inkluderar alla Elements i följande uppsättning: $\{1,2,3,....,N - 1\}$. När $N$ är primtal är alltså ordningen på $N$ $N - 1$. Detta framgår av sats 1, där $\phi(N)$ betecknar ordningen av $N$.


**Proposition 1**. $\phi(N) = N - 1$ när $N$ är primtal


Antag att $N$ inte är primtal. Du kan då beräkna dess ordning med hjälp av **Eulers Phi-funktion**. Medan det är relativt enkelt att beräkna ordningen för ett litet heltal, blir Eulers Phi-funktion särskilt viktig för större heltal. Nedan följer ett förslag till förklaring av Eulers Phi-funktion.


**Sats 2**. Låt $N$ vara lika med $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, där mängden $\{p_i\}$ består av alla distinkta primfaktorer för $N$ och varje $e_i$ anger hur många gånger primfaktorn $p_i$ förekommer för $N$. I så fall..,


$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$


**Sats 2** visar att när man har delat upp ett icke-primtal $N$ i dess olika primtalsfaktorer, är det lätt att beräkna ordningen på $N$.


Anta till exempel att $N = 270$. Detta är uppenbarligen inte ett primtal. Om man bryter ner $N$ i sina primfaktorer får man uttrycket: $2 \cdot 3^3 \cdot 5$. Enligt Eulers Phi-funktion är ordningen på $N$ då enligt följande:


$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$$


Antag vidare att $N$ är en produkt av två primtal, $p$ och $q$. **Sats 2** ovan säger då att ordningen på $N$ är enligt följande:


$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$$


Detta är ett viktigt resultat för RSA-problemet i synnerhet, och det framgår av **Proposition 2** nedan.


**Proposition 2**. Om $N$ är produkten av två primtal, $p$ och $q$, är ordningen av $N$ produkten $(p - 1) \cdot (q - 1)$.


För att illustrera, anta att $N = 119$. Detta heltal kan delas upp i två primtal, nämligen 7 och 17. Därför antyder Eulers Phi-funktion att ordningen på 119 är enligt följande:


$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$$


Med andra ord har heltalet 119 96 coprimes i intervallet från 1 till 119. I själva verket innehåller denna uppsättning alla heltal från 1 till 119, som inte är multiplar av antingen 7 eller 17.


Från och med nu betecknar vi den uppsättning koprimtal som bestämmer ordningen på $N$ som $C_N$. För vårt exempel där $N = 119$ är uppsättningen $C_{119}$ alldeles för stor för att kunna listas fullständigt. Men några av Elements är följande:


$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$$


### Invertibilitet modulo N


Vi kan säga att ett heltal $a$ är **invertibelt modulo N**, om det finns minst ett heltal $b$ som är sådant att $a \cdot b \mod N = 1 \mod N$. Varje sådant heltal $b$ kallas en **invers** (eller **multiplikativ invers**) av $a$ givet reduktion genom modulo $N$.


Antag till exempel att $a = 5$ och $N = 11$. Det finns många heltal som du kan multiplicera 5 med, så att $5 \cdot b \mod 11 = 1 \mod 11$. Tänk t.ex. på heltalen 20 och 31. Det är lätt att se att båda dessa heltal är inverser av 5 för reduktion modulo 11.



- 5 $ \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11 $
- 5 $ \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11 $


Även om 5 har många inverser som reduceras modulo 11, kan du visa att det bara finns en enda positiv invers av 5 som är mindre än 11. Detta är faktiskt inte unikt för just vårt exempel, utan ett allmänt resultat.


**Proposition 3**. Om heltalet $a$ är invertibelt modulo $N$, måste det vara så att exakt en positiv invers av $a$ är mindre än $N$. (Denna unika invers av $a$ måste alltså komma från mängden $\{1, \dots, N - 1\}$).


Låt oss beteckna den unika inversen av $a$ från **Proposition 3** som $a^{-1}$. För fallet när $a = 5$ och $N = 11$, kan du se att $a^{-1} = 9$, givet att $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.


Observera att du också kan få värdet 9 för $a^{-1}$ i vårt exempel genom att helt enkelt reducera någon annan invers av $a$ med modulo 11. Till exempel $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Så när ett heltal $a > N$ är inverterbart modulo $N$, så måste $a \mod N$ också vara inverterbart modulo $N$.


Det är inte nödvändigtvis så att en invers av $a$ existerar reduktion modulo $N$. Antag till exempel att $a = 2$ och $N = 8$. Det finns inget $b$, eller något $a^{-1}$ specifikt, som är sådant att $2 \cdot b \mod 8 = 1 \mod 8$. Detta beror på att varje värde på $b$ alltid kommer att ge en multipel av 2, så ingen division med 8 kan någonsin ge en rest som är lika med 1.


Hur vet vi exakt om ett heltal $a$ har en invers för ett givet $N$? Som du kanske har märkt i exemplet ovan är den största gemensamma divisorn mellan 2 och 8 högre än 1, nämligen 2. Och detta är faktiskt en illustration av följande allmänna resultat:


**Proposition 4**. Det finns en invers för ett heltal $a$ givet reduktion modulo $N$, och specifikt en unik positiv invers mindre än $N$, om och endast om den största gemensamma divisorn mellan $a$ och $N$ är 1 (det vill säga om de är koprim).


För fallet när $a = 5$ och $N = 11$ drog vi slutsatsen att $a^{-1} = 9$, givet att $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Det är viktigt att notera att det omvända också är sant. Det vill säga, när $a = 9$ och $N = 11$, är det så att $a^{-1} = 5$.



### Eulers sats


Innan vi går vidare med RSA-problemet måste vi förstå ytterligare ett viktigt teorem, nämligen **Eulers teorem**. Den säger följande:


**Sats 3**. Antag att två heltal $a$ och $N$ är koprim. Då är $a^{\phi(N)} \mod N = 1 \mod N$.


Detta är ett anmärkningsvärt resultat, men lite förvirrande till en början. Låt oss ta ett exempel för att förstå det.


Antag att $a = 5$ och $N = 7$. Dessa är verkligen koprim som Eulers sats kräver. Vi vet att ordningen på 7 är lika med 6, eftersom 7 är ett primtal (se **Proposition 1**).


Vad Eulers sats nu säger är att $5^6 \mod 7$ måste vara lika med $1 \mod 7$. Nedan följer beräkningarna för att visa att detta verkligen är sant.



- $5^6 \mod 7 = 15 625 \mod 7 = 1 \mod N$


Heltalet 7 divideras med 15 624 totalt 2 233 gånger. Återstoden av 16 625 dividerat med 7 är alltså 1.


Därefter kan man med hjälp av Eulers Phi-funktion, **Sats 2**, härleda **Proposition 5** nedan.


**Proposition 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ för alla positiva heltal $a$ och $b$.


Vi kommer inte att visa varför det är så. Men notera bara att du redan har sett bevis för denna proposition genom det faktum att $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ när $p$ och $q$ är primtal, som anges i **Proposition 2**.


Eulers sats i kombination med **Proposition 5** har viktiga implikationer. Se vad som händer till exempel i uttrycken nedan, där $a$ och $N$ är koprim.



- $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
- $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
- $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$


Kombinationen av Eulers sats och **Proposition 5** gör det därför möjligt för oss att enkelt beräkna ett antal uttryck. I allmänhet kan vi sammanfatta insikten som i **Proposition 6**.


**Proposition 6**. $a^x \mod N = a^{x \mod \phi(N)}$$


Nu måste vi sätta ihop allt i ett sista knepigt steg.


Precis som $N$ har en ordning $\phi(N)$ som inkluderar Elements i mängden $C_N$, vet vi att heltalet $\phi(N)$ i sin tur också måste ha en ordning och en uppsättning koprim. Låt oss sätta $\phi(N) = R$. Då vet vi att det också finns ett värde för $\phi(R)$ och en uppsättning koprimtal $C_R$.


Antag att vi nu väljer ett heltal $e$ från uppsättningen $C_R$. Vi vet från **Proposition 3** att detta heltal $e$ bara har en unik positiv invers som är mindre än $R$. Det vill säga, $e$ har en unik invers från uppsättningen $C_R$. Låt oss kalla denna invers för $d$. Med tanke på definitionen av en invers betyder detta att $e \cdot d = 1 \mod R$.


Vi kan använda detta resultat för att göra ett uttalande om vårt ursprungliga heltal $N$. Detta sammanfattas i **Proposition 7**.


**Proposition 7**. Antag att $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Då måste det för varje element $a$ i mängden $C_N$ vara så att $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.


Vi har nu alla de talteoretiska resultat som behövs för att RSA-problemet ska bli tydligt.



## RSA-kryptosystemet

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>


Vi är nu redo att redogöra för RSA-problemet. Antag att du skapar en uppsättning variabler som består av $p$, $q$, $N$, $\phi(N)$, $e$, $d$ och $y$. Kalla denna uppsättning för $\Pi$. Den skapas på följande sätt:


1. generate två slumpmässiga primtal $p$ och $q$ av samma storlek och beräkna deras produkt $N$.

2. Beräkna ordningen på $N$, $\phi(N)$, med följande produkt: $(p - 1) \cdot (q - 1)$.

3. Välj ett $e > 2$ så att det är mindre och coprime till $\phi(N)$.

4. Beräkna $d$ genom att ställa in $e \cdot d \mod \phi(N) = 1$.

5. Välj ett slumpmässigt värde $y$ som är mindre och coprime till $N$.


RSA-problemet består i att hitta ett $x$ så att $x^e = y$, samtidigt som man bara får en delmängd information om $\Pi$, nämligen variablerna $N$, $e$ och $y$. När $p$ och $q$ är mycket stora, typiskt sett rekommenderas att de är 1024 bitar stora, anses RSA-problemet vara Hard. Du kan nu se varför detta är fallet med tanke på den föregående diskussionen.


Ett enkelt sätt att beräkna $x$ när $x^e \mod N = y \mod N$ är helt enkelt genom att beräkna $y^d \mod N$. Vi vet att $y^d \mod N = x \mod N$ genom följande beräkningar:


$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$$


Problemet är att vi inte känner till värdet $d$, eftersom det inte anges i problemet. Därför kan vi inte direkt beräkna $y^d \mod N$ för att producera $x \mod N$.


Vi kanske dock indirekt skulle kunna beräkna $d$ från ordningen på $N$, $\phi(N)$, eftersom vi vet att $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Men genom antagandet ger problemet inte heller något värde för $\phi(N)$.


Slutligen kan ordningen beräknas indirekt med hjälp av primfaktorerna $p$ och $q$, så att vi så småningom kan beräkna $d$. Men genom antagandet fick vi inte heller tillgång till värdena $p$ och $q$.


Strängt taget, även om faktoriseringsproblemet inom ett RSA-problem är Hard, kan vi inte bevisa att RSA-problemet också är Hard. Det kan nämligen finnas andra sätt att lösa RSA-problemet än genom faktorisering. Det är dock allmänt accepterat och antaget att om faktoriseringsproblemet inom RSA-problemet är Hard, så är RSA-problemet i sig också Hard.


Om RSA-problemet verkligen är Hard, så producerar det en envägsfunktion med en fallucka. Funktionen här är $f(g) = g^e \mod N$. Med kunskap om $f(g)$ kan vem som helst enkelt beräkna ett värde $y$ för ett visst $g = x$. Det är dock praktiskt taget omöjligt att beräkna ett visst värde $x$ bara genom att känna till värdet $y$ och funktionen $f(g)$. Undantaget är när du får en bit information $d$, falluckan. I det fallet kan du helt enkelt beräkna $y^d$ för att få $x$.


Låt oss gå igenom ett specifikt exempel för att illustrera RSA-problemet. Jag kan inte välja ett RSA-problem som skulle betraktas som Hard enligt villkoren ovan, eftersom siffrorna skulle bli otympliga. Istället är detta exempel bara för att illustrera hur RSA-problemet i allmänhet fungerar.


Till att börja med antar vi att du väljer två slumpmässiga primtal 13 och 31. Så $p = 13$ och $q = 31$. Produkten $N$ av dessa två primtal är lika med 403. Vi kan enkelt beräkna ordningen på 403. Den är ekvivalent med $(13 - 1) \cdot (31 - 1) = 360$$.


Därefter måste vi, enligt steg 3 i RSA-problemet, välja ett coprime för 360 som är större än 2 och mindre än 360. Vi behöver inte välja detta värde slumpmässigt. Anta att vi väljer 103. Detta är ett coprime till 360 eftersom dess största gemensamma divisor med 103 är 1.


Steg 4 kräver nu att vi beräknar ett värde $d$ så att $103 \cdot d \mod 360 = 1$. Detta är inte en lätt uppgift för hand när värdet för $N$ är stort. Det kräver att vi använder en procedur som kallas **utökad euklidisk algoritm**.


Även om jag inte visar proceduren här, ger den värdet 7 när $e = 103$. Du kan verifiera att värdeparet 103 och 7 verkligen uppfyller det allmänna villkoret $e \cdot d \mod \phi(n) = 1$ genom beräkningarna nedan.



- $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$$


Det är viktigt att notera att givet *Proposition 4* vet vi att inget annat heltal mellan 1 och 360 för $d$ kommer att ge resultatet att $103 \cdot d = 1 \mod 360$. Dessutom innebär förslaget att om man väljer ett annat värde för $e$, kommer det att ge ett annat unikt värde för $d$.


I steg 5 av RSA-problemet måste vi välja något positivt heltal $y$ som är ett mindre coprime av 403. Antag att vi sätter $y = 2^{103}$. Exponentiering av 2 med 103 ger resultatet nedan.



- $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$


RSA-problemet i detta speciella exempel är nu som följer: Du får $N = 403$, $e = 103$ och $y = 349 \mod 403$. Du måste nu beräkna $x$ så att $x^{103} = 349 \mod 403$. Det vill säga, du måste komma fram till att det ursprungliga värdet före exponentiering med 103 var 2.


Det skulle vara lätt (åtminstone för en dator) att beräkna $x$ om vi visste att $d = 7$. I så fall kan du bara bestämma $x$ enligt nedan.



- $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$


Problemet är att du inte har fått informationen om att $d = 7$. Du kan naturligtvis beräkna $d$ från det faktum att $103 \cdot d = 1 \mod 360$. Problemet är att du inte heller har fått information om att ordningen på $N = 360$. Slutligen kan du också beräkna ordningen på 403 genom att beräkna följande produkt: $(p - 1) \cdot (q - 1)$. Men du får inte heller veta att $p = 13$ och $q = 31$.


Naturligtvis kan en dator fortfarande lösa RSA-problemet för det här exemplet relativt enkelt, eftersom de primtal som är inblandade inte är stora. Men när primtalen blir mycket stora står den inför en praktiskt taget omöjlig uppgift.


Vi har nu presenterat RSA-problemet, en uppsättning villkor under vilka det är Hard och den underliggande matematiken. Hur kan något av detta hjälpa till med asymmetrisk kryptografi? Mer specifikt, hur kan vi omvandla RSA-problemets svårighetsgrad under vissa förhållanden till ett krypteringsschema eller ett digitalt signaturschema?


Ett tillvägagångssätt är att utgå från RSA-problemet och bygga upp system på ett enkelt sätt. Anta till exempel att du genererade en uppsättning variabler $\Pi$ som beskrivs i RSA-problemet och se till att $p$ och $q$ är tillräckligt stora. Du sätter din publika nyckel lika med $(N, e)$ och delar denna information med världen. Som beskrivits ovan håller du värdena för $p$, $q$, $\phi(n)$ och $d$ hemliga. I själva verket är $d$ din privata nyckel.


Den som vill skicka ett meddelande $m$ till dig som är ett element i $C_N$ kan helt enkelt kryptera det enligt följande: $c = m^e \mod N$. (Chiffertexten $c$ här är ekvivalent med värdet $y$ i RSA-problemet.) Du kan enkelt dekryptera detta meddelande genom att bara beräkna $c^d \mod N$.


Du kan försöka skapa ett system för digitala signaturer på samma sätt. Anta att du vill skicka ett meddelande $m$ till någon med en digital signatur $S$. Du kan bara ställa in $S = m^d \mod N$ och skicka paret $(m,S)$ till mottagaren. Vem som helst kan verifiera den digitala signaturen bara genom att kontrollera om $S^e \mod N = m \mod N$. En angripare skulle dock ha mycket svårt att skapa en giltig $S$ för ett meddelande, eftersom de inte har $d$.


Tyvärr är det inte så enkelt att omvandla det som i sig är ett Hard-problem, RSA-problemet, till ett kryptografiskt system. För det enkla krypteringsschemat kan du bara välja coprimes av $N$ som dina meddelanden. Det ger oss inte många möjliga meddelanden, absolut inte tillräckligt för standardkommunikation. Dessutom måste dessa meddelanden väljas slumpmässigt. Det verkar något opraktiskt. Slutligen kommer varje meddelande som väljs två gånger att ge exakt samma chiffertext. Detta är extremt oönskat i alla krypteringssystem och uppfyller inte någon rigorös modern standard för säkerhet i kryptering.


Problemen blir ännu värre för vårt enkla system för digitala signaturer. Som det ser ut nu kan en angripare enkelt förfalska digitala signaturer genom att först välja ett koprim av $N$ som signatur och sedan beräkna motsvarande originalmeddelande. Detta bryter helt klart mot kravet på existentiell oförfalskbarhet.


Genom att lägga till lite smart komplexitet kan RSA-problemet ändå användas för att skapa ett säkert krypteringssystem med publik nyckel samt ett säkert system för digital signatur. Vi kommer inte att gå in på detaljerna i sådana konstruktioner här. [4] Det är dock viktigt att notera att denna ytterligare komplexitet inte ändrar det grundläggande RSA-problem som dessa system bygger på.



**Noteringar:**


[4] Se till exempel Jonathan Katz och Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 410-32 om RSA-kryptering och s. 444-41 om digitala RSA-signaturer.




# Sista avsnittet

<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>


## Recensioner & betyg

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>

<isCourseReview>true</isCourseReview>

## Slutlig tentamen

<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>

<isCourseExam>true</isCourseExam>

## Slutsats

<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>

<isCourseConclusion>true</isCourseConclusion>