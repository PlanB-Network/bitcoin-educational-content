---
name: RGB
description: Introduktion och skapande av tillgångar på RGB
---

![RGB vs Ethereum](assets/0.webp)


## inledning


Den 3 januari 2009 lanserade Satoshi Nakamoto den första Bitcoin-noden, från det ögonblicket anslöt sig nya noder och Bitcoin började bete sig som om det var en ny livsform, en livsform som inte har slutat utvecklas, lite i taget har det blivit det säkraste nätverket i världen till följd av dess unika design, mycket väl genomtänkt av Satoshi eftersom det genom ekonomiska incitament lockar användare som vanligtvis kallas miners att investera i energi och datorkraft vilket bidrar till nätverkssäkerhet.


När Bitcoin fortsätter sin tillväxt och adoption står det inför skalbarhetsproblem, Bitcoin-nätverket tillåter att ett nytt block med transaktioner bryts på en ungefärlig tid av 10 minuter, förutsatt att vi har 144 block på en dag med maximala värden på 2700 transaktioner per block, skulle Bitcoin ha tillåtit endast 4,5 transaktioner per sekund, Satoshi var medveten om denna begränsning, vi kan se det i ett e-postmeddelande1 som skickades till Mike Hearn i mars 2011 där han förklarar hur det vi idag känner som en betalningskanal fungerar. mikrobetalningar snabbt och säkert utan att vänta på bekräftelser. Det är här off-chain-protokollen kommer in i bilden.


Enligt Christian Decker2 är off-chain-protokoll vanligtvis system där användare använder data från en Blockchain och hanterar den utan att röra själva Blockchain förrän i sista minuten. Baserat på detta koncept föddes Lightning Network, ett nätverk som använder off-chain-protokoll för att göra det möjligt att göra Bitcoin-betalningar nästan omedelbart och eftersom inte alla dessa operationer skrivs på blockkedjan tillåter det tusentals transaktioner per sekund och skala Bitcoin.


Forskning och utveckling inom området off-chain-protokoll på Bitcoin har öppnat en pandoras låda, idag vet vi att vi kan uppnå mycket mer än värdeöverföring på ett decentraliserat sätt, den ideella LNP/BP Standards Association fokuserar på utveckling av Layer 2 och 3 protokoll på Bitcoin och Lightning Network, bland dessa projekt sticker RGB ut.


## Vad är RGB?


RGB har uppstått ur Peter Todds3 forskning om engångsförseglingar och validering på klientsidan, som myntades 2016-2019 av Giacomo Zucco och samhället till ett bättre tillgångsprotokoll för Bitcoin och Lightning Network. Ytterligare utveckling av dessa idéer ledde till en utveckling av RGB till ett fullfjädrat Smart contract-system av Maxim Orlovsky, som leder dess implementering sedan 2019 med deltagande av samhället.


Vi kan definiera RGB som en uppsättning protokoll med öppen källkod som gör det möjligt för oss att utföra komplexa smarta kontrakt på ett skalbart och konfidentiellt sätt. Det är inte ett särskilt nätverk (som Bitcoin eller Lightning); varje Smart contract är bara en uppsättning Contract-deltagare som kan interagera med hjälp av olika kommunikationskanaler (som standard Lightning Network). RGB använder Bitcoin Blockchain som en Layer av tillstånd Commitment och upprätthåller koden för Smart contract och data off-chain, vilket gör den skalbar, och utnyttjar Bitcoin-transaktioner (och Script) som ett Ownership-kontrollsystem för smarta kontrakt; medan utvecklingen av Smart contract definieras av ett off-chain-system, är det slutligen viktigt att notera att allt valideras på klientsidan.


Enkelt uttryckt är RGB ett system som gör det möjligt för användaren att granska en Smart contract, utföra den och verifiera den individuellt när som helst utan att ha en extra kostnad eftersom det för detta inte använder en Blockchain som "traditionella" system gör, komplexa smarta kontraktssystem var banbrytande av Ethereum men på grund av att det kräver att användaren spenderar betydande mängder gas för varje operation uppnådde de aldrig den skalbarhet de lovade och följaktligen var det aldrig ett alternativ att banka de användare som uteslutits från det nuvarande finansiella systemet.


För närvarande främjar Blockchain-industrin att både koden för smarta kontrakt och data måste lagras i Blockchain och exekveras av varje nod i nätverket, oavsett den överdrivna ökningen i storlek eller missbruk av beräkningsresurser. Det system som föreslås av RGB är mycket mer intelligent och effektivt eftersom det bryter med Blockchain-paradigmet genom att ha smarta kontrakt och data separerade från Blockchain och därmed undviker mättnaden av nätverket som ses i andra plattformar, i sin tur tvingar det inte varje nod att exekvera varje Contract utan snarare de inblandade parterna vilket ger konfidentialitet till en nivå som aldrig sett tidigare.


![RGB vs Ethereum](assets/1.webp)


## Smarta kontrakt i RGB


I RGB definierar Smart contract-utvecklaren ett schema som specificerar regler för hur Contract utvecklas över tiden. Schemat är standarden för konstruktionen av smarta kontrakt i RGB, och både en emittent när han definierar en Contract för utfärdande och en Wallet eller Exchange måste följa ett visst schema mot vilket de måste validera Contract. Endast om valideringen är korrekt kan varje part acceptera förfrågningar och arbeta med tillgången.


En Smart contract i RGB är en Directed Acyclic Graph (DAG) av tillståndsändringar, där endast en del av grafen alltid är känd och det inte finns någon tillgång till resten. RGB-schemat är en grundläggande uppsättning regler för utvecklingen av denna graf som Smart contract börjar med. Varje Contract Participant kan lägga till dessa regler (om detta tillåts av Schema) och den resulterande grafen byggs från den iterativa tillämpningen av dessa regler.


## Fungibla tillgångar


De fungibla tillgångarna i RGB följer LNPBP RGB-20-specifikationen4 , när en RGB-20 definieras distribueras tillgångsdata som kallas "Genesis-data" genom Lightning Network, som innehåller vad som krävs för att använda tillgången. Den mest grundläggande formen av tillgångar tillåter inte sekundär utgivning, token-bränning, renominering eller ersättning.


Ibland kommer emittenten att behöva emittera fler tokens i framtiden, dvs. stablecoins som USDT, vilket håller värdet på varje token knutet till värdet på en inflationsvaluta som USD. För att uppnå detta finns mer komplexa RGB-20-schema, och utöver Genesis-data kräver de att emittenten producerar sändningar, som också kommer att cirkulera i Lightning Network; med denna information kan vi veta tillgångens totala cirkulerande Supply. Detsamma gäller för att bränna tillgångar eller ändra dess namn.


Informationen om tillgången kan vara offentlig eller privat: om emittenten kräver konfidentialitet kan han/hon välja att inte dela information om token och utföra transaktioner i absolut avskildhet, men vi har också det motsatta fallet där emittenten och innehavarna vill att hela processen ska vara transparent. Detta uppnås genom att token-data delas.


## RGB-20 procedurer


Brännproceduren inaktiverar polletter, brända polletter kan inte användas längre.


Ersättningsförfarandet inträffar när tokens bränns och en ny mängd av samma token skapas. Detta bidrar till att minska storleken på tillgångens historiska data, vilket är viktigt för att upprätthålla tillgångens hastighet.


För att stödja användningsfallet där det är möjligt att bränna tillgångar utan att behöva ersätta dem, används ett underschema av RGB-20 som endast tillåter bränning av tillgångar.


## Icke fungibla tillgångar


De icke-förstörbara tillgångarna i RGB följer LNPBP RGB-21 specifikationen5, när vi arbetar med NFT:er har vi också ett huvudschema och ett underschema. Dessa system har en gravyrprocedur, som gör att vi kan bifoga anpassade data från en del av token-ägaren, det vanligaste exemplet vi ser i NFT idag är digital konst kopplad till token. token-utfärdaren kan förbjuda denna datagravering genom att använda RGB-21-underschemat. Till skillnad från andra NFT Blockchain-system gör RGB det möjligt att distribuera stora token-data i media på ett helt decentraliserat och censurresistent sätt genom att använda utvidgningen till Lightning P2P-nätverket som kallas Bifrost, som också används för att bygga många andra former av RGB-specifika Smart contract-funktioner.


Utöver fungibla tillgångar och NFT:er kan RGB och Bifrost användas för att producera andra former av smarta kontrakt, inklusive DEX:er, likviditetspooler, algoritmiska stabila mynt etc, som vi kommer att ta upp i framtida artiklar.


## NFT från RGB jämfört med NFT från andra plattformar



- Inget behov av dyrbar Blockchain-lagring
- IPFS behövs inte, ett Lightning Network-tillägg (kallat Bifrost) används istället (och det är helt end-to-end-krypterat)
- Inget behov av en särskild lösning för datahantering - även här tar Bifrost den rollen
- Inget behov av att lita på webbplatser för att upprätthålla data för NFT-tokens eller om emissionstillgångar / Contract ABIs
- Inbyggd DRM-kryptering och Ownership-hantering
- Infrastruktur för säkerhetskopiering med hjälp av Lightning Network (Bifrost)
- Sätt att tjäna pengar på innehåll (inte bara sälja själva NFT:n, utan även tillgång till innehållet, flera gånger)


## Slutsatser


Sedan lanseringen av Bitcoin för nästan 13 år sedan har det förekommit mycket forskning och experiment inom området, både framgångarna och misstagen har gjort det möjligt för oss att förstå lite mer hur decentraliserade system beter sig i praktiken, vad som gör dem verkligen decentraliserade och vilka åtgärder som tenderar att leda dem till centralisering, allt detta har lett oss till slutsatsen att verklig decentralisering är ett sällsynt och svårt fenomen att uppnå, verklig decentralisering har endast uppnåtts av Bitcoin och det är av den anledningen som vi fokuserar våra ansträngningar på att bygga vidare på det.


RGB har sitt eget kaninhål inom Bitcoin-kaninhålet, medan jag faller ner genom dem kommer jag att publicera vad jag har lärt mig, i nästa artikel kommer vi att ha en introduktion till LNP- och RGB-noderna och hur man använder dem.



- 1 https://plan99.net/~mike/Satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# RGB-nod handledning


## Inledning


I denna handledning förklarar vi hur man använder RGB-nod för att skapa en fungibel token och hur man överför den, detta dokument är baserat på RGB-node demo och skiljer sig åt genom att denna handledning använder riktiga Testnet-data och för det måste vi bygga våra egna Partially Signed Bitcoin Transaction, PSBT från och med nu.


## Krav och önskemål


Användningen av en Linux-distribution rekommenderas, denna handledning skrevs med Pop!OS, som är baserat på Ubuntu och du behöver:



- last
- Bitcoin kärna
- git


För att skilja på vad användaren skriver och det svar han får i terminalen inkluderar vi $ som symboliserar bash-prompten.


Du måste installera vissa beroenden:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


Bygga och köra


RGB-node är work in progress (WIP), det är därför vi måste lokalisera oss i en specifik commit (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) för att kunna kompilera och använda den korrekt, för detta utför vi följande kommandon.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


Nu kompilerar vi den, glöm inte att använda --locked flaggan eftersom det finns en brytande ändring införd på en version av clap.


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


Enligt Rust-kompilatorn kopierades binärfilerna till katalogen $HOME/.cargo/bin, men om din kompilator kopierade dem till en annan plats måste du se till att den katalogen ingår i $PATH.


Bland de installerade binärerna kan vi se tre daemoner eller tjänster (filerna som slutar på d) och en CLI (kommandorad Interface), CLI tillåter oss att interagera med huvud rgbd daemon. Eftersom vi i den här handledningen kommer att köra två noder behöver vi också två klienter, var och en måste ansluta till sin egen nod, för det skapar vi två alias.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


Vi kan bara köra alias eller lägga till dem i slutet av filen $HOME/.bashrc och köra källkod $HOME/.bashrc.

Förutsättningar


RGB-noden hanterar inte någon form av Wallet-relaterad funktionalitet, den utför bara RGB-specifika uppgifter på de data som kommer att tillhandahållas av en extern Wallet som Bitcoin-kärnan. För att demonstrera ett grundläggande arbetsflöde med utfärdande och överföring behöver vi i synnerhet:



- En issuance_utxo till vilken RGB-node-0 kommer att binda den nyemitterade tillgången
- En receive_utxo där RGB-nod-1 tar emot tillgången
- En change_utxo där RGB-node-0 tar emot förändringen av tillgången
- En Partially Signed Bitcoin Transaction (tx.PSBT), vars publika nyckel för utdata kommer att justeras för att inkludera en Commitment i överföringen.


Vi kommer att använda Bitcoin-kärnan CLI, vi måste ha bitcoind daemon som körs på Testnet, detta kommer att ge oss interoperabilitet och i slutet kommer vi att kunna skicka våra egna tillgångar till andra RGB-användare som följde denna handledning.


För enkelhetens skull lägger vi till detta alias i slutet av vår ~/.bashrc-fil.


```
alias bcli="bitcoin-cli -testnet"
```


Låt oss lista våra outnyttjade utmatningstransaktioner och välja två, den ena kommer att vara issuance_utxo och den andra change_utxo, det spelar ingen roll vilken som är vilken, det viktiga är att emittenten har kontroll över dessa två UTXO.


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


Innan vi går vidare måste vi prata om utpunkter, en enda transaktion kan innehålla flera utgångar, utpunkten innehåller både en 32-byte txid och ett 4-byte utgångsindexnummer (vout) för att hänvisa till specifik utgång separerad med ett kolon :. I vår listunspent-utgång kan vi hitta två UTXO: er, på var och en kan vi se txid och vout, det är våra utgångar issuance_utxo och change_utxo.


receive_utxo är en UTXO som kontrolleras av mottagaren, i det här fallet använder vi e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 som är en outpoint från en annan Wallet.



- utfärdande_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


Vi ska nu skapa en delvis signerad transaktion (tx.PSBT) vars utdata kommer att justeras för att inkludera ett åtagande att överföra, kom ihåg att ersätta txid och vout med dina egna, destinationen Address spelar egentligen ingen roll, den kan vara din eller den kan vara från en annan person, det spelar ingen roll vart dessa Sats går, det som är viktigt är att vi använder issuance_utxo.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


Utmatningen gav oss en PSBT i base64-kodning som vi kommer att använda för att skapa tx.PSBT.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


Låt oss skapa en ny katalog som heter rgbdata där datakatalogen för varje nod lagras.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


Redan i $HOME/rgbdata startar vi varje nod i olika terminaler, där ~/.cargo/bin är den katalog där cargo kopierade alla binärfiler efter installationen av RGB-noden.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## Utfärdande


För att emittera en tillgång kör vi rgb0-CLI med underkommandona för fungibel emission, sedan argumenten, tickern USDT, namnet "USD Tether" och i tilldelningen kommer vi att använda det emitterande beloppet och issuance_utxo som vi ser nedan:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


Tillgång framgångsrikt utfärdad. Använd denna information för delning:

Information om tillgångar:


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


Vi får assetId, vi behöver det för att överföra tillgången.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## generate blinded UTXO


För att ta emot den nya USDT behöver RGB-nod-1 generate en blinded UTXO som motsvarar receive_utxo för att hålla tillgången.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


För att kunna acceptera överföringar relaterade till denna UTXO behöver vi den ursprungliga receive_utxo och blinding_factor.


## Överföring


För att överföra en del av tillgången till RGB-nod-1 måste vi skicka den till blinded UTXO, RGB-nod-0 måste skapa en Consignment och ett offentliggörande, och överföra det till en Bitcoin-transaktion. Sedan behöver vi en PSBT som vi modifierar för att inkludera commiten. Dessutom tillåter alternativen -i och -a oss att tillhandahålla en input outpoint som skulle vara tillgångens ursprung och en allokering där vi kommer att ta emot förändringen, vi måste ange det på följande sätt @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


Detta kommer att skriva tre nya filer, Consignment, avslöjande och PSBT inklusive tweak, denna PSBT kallas Witness Transaction, Consignment skickas till RGB-nod-1.


## Vittne


Witness Transaction ska signeras och sändas ut, för detta behöver vi base64-koda den tillbaka.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


Signera den med underkommandot walletprocesspsbt.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


Nu slutför du det och får hexen.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## Sändning


Sänd den med hjälp av underkommandot sendrawtransaction för att få den bekräftad i Blockchain.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## Acceptera


För att acceptera en inkommande överföring ska RGB-nod-1 ha tagit emot Consignment-filen från RGB-nod-0, ha receive_utxo och motsvarande blinding_factor genererad under blinding UTXO-generering.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


Vi kan nu se (i fältet knownAllocations) den nya tilldelningen av 100 tillgångsenheter i <receive_utxo> genom att köra:


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


Eftersom receive_utxo var blinded när överföringen gjordes har betalaren RGB-node-0 ingen information om vart de 100 USDT skickades, så platsen visas inte i knownAllocations .


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


Men som du kan se kan RGB-node-0 inte se förändringen på 900 tillgångar som vi gav till transfer-kommandot med argumentet -a. För att registrera förändringen måste RGB-node-0 acceptera offentliggörandet.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


Om RGB-node-0 lyckades kan du se ändringen genom att lista tillgången.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


## Slutsatser


Vi har kunnat skapa en fungibel tillgång och flytta den från en transaktion till en annan på ett privat sätt, om vi kontrollerar den bekräftade transaktionen i en Block explorer skulle vi inte hitta något som skiljer sig från vanlig transaktion, detta är tack vare det faktum att RGB använder engångsförseglingar för att justera transaktionerna, I det här inlägget gör jag en introduktion till hur RGB fungerar.


Det här inlägget kan ha buggar, om du hittar något, vänligen meddela mig för att förbättra den här guiden, förslag och kritik är också välkomna, glad hacking! 🖖