# En kort introduktion till RGB-protokollen

![RGB vs Ethereum](assets/0.png)

## Introduktion

Den 3 januari 2009 lanserade Satoshi Nakamoto den första Bitcoin-noden. Från och med den dagen har nya noder anslutit sig och Bitcoin har börjat bete sig som om det vore en ny form av liv, en form av liv som ständigt utvecklas. Det har gradvis blivit världens säkraste nätverk tack vare sin unika och väl genomtänkta design av Satoshi. Genom ekonomiska incitament lockar det användare, vanligtvis kallade gruvarbetare, att investera i energi och beräkningskraft, vilket bidrar till nätverkets säkerhet.

Medan Bitcoin fortsätter att växa och bli mer populärt står det inför skalbarhetsproblem. Bitcoin-nätverket tillåter att en ny block med transaktioner bryts ungefär var 10:e minut. Om vi antar att vi har 144 block per dag med maximalt 2700 transaktioner per block, skulle Bitcoin bara tillåta 4,5 transaktioner per sekund. Satoshi var medveten om denna begränsning, vilket vi kan se i ett e-postmeddelande1 som skickades till Mike Hearn i mars 2011 där han förklarar hur det som vi idag känner till som betalningskanal fungerar. Detta möjliggör snabba och säkra mikrobetalningar utan att behöva vänta på bekräftelser. Det är här off-chain-protokoll kommer in i bilden.

Enligt Christian Decker2 är off-chain-protokoll vanligtvis system där användare använder data från en blockchain och hanterar den utan att röra själva blockchainen förrän sista minuten. Baserat på denna idé föddes Lightning Network, ett nätverk som använder off-chain-protokoll för att möjliggöra nästan omedelbara Bitcoin-betalningar och eftersom alla dessa transaktioner inte skrivs på blockkedjan kan det hantera tusentals transaktioner per sekund och skala Bitcoin.

Forskning och utveckling inom området off-chain-protokoll på Bitcoin har öppnat en Pandoras ask, idag vet vi att vi kan uppnå mycket mer än bara decentraliserad värdeöverföring. Den ideella organisationen LNP/BP Standards fokuserar på utvecklingen av lager 2- och 3-protokoll på Bitcoin och Lightning Network, och bland dessa projekt utmärker sig RGB.

## Vad är RGB?

RGB uppstod från Peter Todds3 forskning om enkelslutna sigill och klientvalidering, vilket formulerades mellan 2016 och 2019 av Giacomo Zucco och gemenskapen till ett bättre tillgångsprotokoll för Bitcoin och Lightning Network. Vidareutvecklingen av dessa idéer har lett till utvecklingen av RGB till ett fullständigt smart kontraktssystem av Maxim Orlovsky, som har ansvarat för implementeringen sedan 2019 med gemenskapens medverkan.
Vi kan definiera RGB som en uppsättning öppen källkod som gör det möjligt för oss att köra komplexa smarta kontrakt på ett skalbart och konfidentiellt sätt. Det är inte en specifik nätverkstyp (som Bitcoin eller Lightning); varje smart kontrakt är helt enkelt en grupp kontraktsdeltagare som kan interagera med varandra genom olika kommunikationskanaler (standardmässigt genom Lightning-nätverket). RGB använder Bitcoin-blockkedjan som en tillståndsengagemangslager och lagrar smarta kontraktskoden och data utanför kedjan, vilket gör det skalbart genom att utnyttja Bitcoin-transaktioner (och Script) som ägandekontrollsystem för smarta kontrakt. Medan smarta kontraktets utveckling definieras av ett off-chain-schema, är det viktigt att notera att allt valideras på klientens sida.

Förenklat uttryckt är RGB ett system som gör det möjligt för användaren att granska, köra och verifiera ett smart kontrakt individuellt när som helst utan extra kostnad, eftersom det inte använder en blockkedja som "traditionella" system gör. Komplexa smarta kontrakt har tidigare introducerats av Ethereum, men på grund av användarens behov av att spendera stora mängder gas för varje operation har de aldrig uppnått den utlovade skalbarheten, vilket gör dem till en orealistiskt alternativ för användare som är exkluderade från det nuvarande finansiella systemet.

För närvarande främjar blockkedjeindustrin att smarta kontraktskod och data ska lagras i blockkedjan och köras av varje nod i nätverket, oavsett den ökade storleken eller missbruket av datorresurser. RGB:s föreslagna schema är mycket smartare och effektivare eftersom det bryter med blockkedjeparadigmet genom att separera smarta kontrakt och data från blockkedjan, vilket undviker nätverksöverbelastning som observerats på andra plattformar. Dessutom tvingar det inte varje nod att köra varje kontrakt, utan bara de inblandade parterna, vilket ger en sekretessnivå som aldrig tidigare skådats.

![RGB vs Ethereum](assets/1.png)

## Smarta kontrakt i RGB

I RGB definierar utvecklaren av smarta kontrakt ett schema som specificerar reglerna enligt vilka kontraktet utvecklas över tiden. Schemat är standarden för att bygga smarta kontrakt i RGB, och både en utfärdare vid kontraktets definition för utfärdande och en plånbok eller börs måste följa ett specifikt schema för att validera kontraktet. Endast om valideringen är korrekt kan varje part acceptera förfrågningar och arbeta med tillgången.
En RGB är en smart kontrakt en riktad acyklisk graf (DAG) av tillståndsändringar, där endast en del av grafen är känd och det finns ingen åtkomst till resten. RGB-schema är en uppsättning grundregler för utvecklingen av denna graf som smarta kontraktet startar med. Varje deltagare i kontraktet kan lägga till dessa regler (om det tillåts av schemat) och den resulterande grafen byggs upp genom att tillämpa dessa regler iterativt.
## Utbytbara tillgångar

Utbytbara tillgångar i RGB följer specifikationen LNPBP RGB-20, när RGB-20 definieras distribueras tillgångsdata, känd som "genesisdata", via Lightning-nätverket, vilket innehåller det som behövs för att använda tillgången. Den mest grundläggande formen av tillgångar tillåter inte sekundär emission, förstörelse av tokens, omdöpning eller ersättning.

Ibland kan utfärdaren behöva utfärda fler tokens i framtiden, till exempel stabila mynt som USDT, som håller värdet av varje token kopplat till värdet av en inflationsvaluta som den amerikanska dollarn. För detta finns det mer komplexa RGB-20-scheman, och förutom genesisdata kräver de att utfärdaren producerar sändningar, som också kommer att cirkulera i Lightning-nätverket; med denna information kan vi känna till den totala cirkulerande tillgångsmängden. Samma sak gäller för brännande tillgångar eller för att ändra deras namn.

Informationen om tillgången kan vara offentlig eller privat: om utfärdaren kräver sekretess kan de välja att inte dela information om token och genomföra operationer i absolut sekretess, men vi har också det motsatta fallet där utfärdaren och innehavarna behöver att hela processen är transparent. Detta uppnås genom att dela token-data.

## RGB-20-procedurer

Förstöringsproceduren inaktiverar tokens, brända tokens kan inte längre användas.

Ersättningsproceduren inträffar när tokens bränns och en ny mängd av samma token skapas. Detta gör det möjligt att minska storleken på tillgångens historiska data, vilket är viktigt för att bibehålla tillgångens snabbhet.

För att stödja användningsfall där det är möjligt att bränna tillgångar utan att behöva ersätta dem används en underkategori av RGB-20 som endast tillåter att bränna tillgångar.

## Icke-utbytbara tillgångar
Icke-fungibla tillgångar (NFT) inom RGB följer specifikationen LNPBP RGB-21. När vi arbetar med NFT har vi också en huvudschema och en under-schema. Dessa scheman har en bränningsteknik som gör det möjligt att bifoga anpassade data till ägaren av token. Det vanligaste exemplet på NFT vi ser idag är digital konst kopplad till token. Tokenutfärdaren kan förbjuda denna bränning av data genom att använda under-schemat RGB-21. Till skillnad från andra NFT-blockchainsystem kan RGB distribuera stora mängder multimedia-token-data på ett decentraliserat och censurbeständigt sätt genom att använda en utökning av P2P-nätverket Lightning som kallas Bifrost. Bifrost används också för att bygga många andra specifika funktioner för smarta kontrakt inom RGB.

Förutom fungibla tillgångar och NFT kan RGB och Bifrost användas för att producera andra former av smarta kontrakt, inklusive DEX, likviditetspooler, algoritmiska stablecoins, etc., vilket vi kommer att behandla i framtida artiklar.

## RGB-NFT vs NFT på andra plattformar

- Ingen dyr lagring på blockchain krävs
- Ingen IPFS krävs, istället används en utökning av Lightning-nätverket (kallad Bifrost) (och den är helt krypterad från ände till ände)
- Ingen speciell datalagringslösning krävs - återigen tar Bifrost den rollen
- Ingen tillit till webbplatser för att hantera NFT-data eller tillgångar/kontrakts-ABI krävs
- Inbyggd DRM-kryptering och äganderättshantering
- Säkerhetskopieringsinfrastruktur med hjälp av Lightning-nätverket (Bifrost)
- Möjlighet att monetarisera innehållet (inte bara försäljningen av själva NFT utan också åtkomst till innehållet, flera gånger)

## Slutsatser

Sedan lanseringen av Bitcoin för nästan 13 år sedan har det varit mycket forskning och experiment inom detta område. Framgångar och misstag har hjälpt oss att förstå beteendet hos decentraliserade system i praktiken, vad som verkligen gör dem decentraliserade och vilka åtgärder som tenderar att leda dem mot centralisering. Allt detta har lett oss till slutsatsen att verklig decentralisering är ett sällsynt och svårt att uppnå fenomen. Verklig decentralisering har bara uppnåtts av Bitcoin, och det är därför vi fokuserar våra ansträngningar på att bygga på det.

RGB har sin egen grav i Bitcoin-kaninhålet, och när jag faller genom dem kommer jag att dela med mig av vad jag har lärt mig. I nästa artikel kommer vi att få en introduktion till LNP-noder och RGB och hur man använder dem.

- 1 https://plan99.net/~mike/satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-June/012773.html- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md

- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md

# RGB-node handledning

## Introduktion

I denna handledning förklarar vi hur man använder RGB-node för att skapa en fungibel token och hur man överför den. Denna dokumentation är baserad på RGB-node-demo och skiljer sig genom att denna handledning använder riktiga testnätsdata och för detta behöver vi bygga vår egen delvis signerade Bitcoin-transaktion (PSBT), psbt från och med nu.

## Krav

Det rekommenderas att använda en Linux-distribution, denna handledning är skriven med användning av Pop!/\_OS, som är baserad på Ubuntu, och du kommer att behöva:

- cargo
- Bitcoin core
- git

Observera: Denna handledning visar kommandon som körs i en Linux-terminal, för att skilja vad användaren skriver och svaret som visas i terminalen inkluderar vi symbolen $ som symboliserar bash-kommandotolken.

Du måste installera vissa beroenden:

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

Kompilering och körning

RGB-node är under utveckling (WIP), därför måste vi ställa in oss på en specifik commit (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) för att kunna kompilera och använda den korrekt, för detta kör vi följande kommandon.

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

Nu kompilerar vi den, glöm inte att använda flaggan --locked eftersom det har gjorts en stor förändring i en version av clap.

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

Som Rust-kompilatorn indikerar har binärerna kopierats till katalogen $HOME/.cargo/bin, om din kompilator har kopierat dem någon annanstans måste du se till att den katalogen är inkluderad i $PATH.
Bland de installerade binärerna kan vi se tre demoner eller tjänster (filer som slutar med d) och en kommandoradsgränssnitt (cli), cli låter oss interagera med huvuddemonen rgbd. Eftersom vi kommer att köra två noder i den här handledningen behöver vi också två klienter, var och en måste ansluta till sin egen nod, så vi skapar två alias.
```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

Vi kan helt enkelt köra aliasen eller lägga till dem i slutet av filen $HOME/.bashrc och köra source $HOME/.bashrc.
Förutsättning

RGB-node hanterar inga plånboksfunktioner, den utför bara RGB-specifika uppgifter på data som kommer att tillhandahållas av en extern plånbok som bitcoin core. Specifikt, för att visa en grundläggande arbetsflöde med utfärdande och överföring, behöver vi:

- En issuance_utxo som rgb-node-0 kommer att binda till den nyutgivna tillgången
- En receive_utxo där rgb-node-1 tar emot tillgången
- En change_utxo där rgb-node-0 tar emot växel för tillgången
- En delvis signerad bitcoin-transaktion (tx.psbt), vars utgångs publika nyckel kommer att justeras för att inkludera en överföringsförbindelse.
  Vi kommer att använda bitcoin core cli, vi måste ha bitcoind-demonen igång på testnet, detta ger oss interoperabilitet och på slutet kommer vi att kunna skicka våra egna tillgångar till andra RGB-användare som har följt denna handledning.
  För att förenkla saken kommer vi att lägga till detta alias i slutet av vår fil ~/.bashrc.

```
alias bcli="bitcoin-cli -testnet"
```

Vi listar våra obefintliga utgående transaktioner och väljer två, en kommer att vara issuance_utxo och den andra change_utxo, det spelar ingen roll vilken som är vilken, det viktiga är att utfärdaren har kontroll över båda UTXO:erna.

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
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",    "safe": true
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

Innan vi går vidare måste vi prata om outpoints. En enda transaktion kan inkludera flera utgångar. Outpointen inkluderar både en 32-byte TXID och en 4-byte utgångsindex (vout) för att referera till en specifik utgång, separerade med ett kolon ":". I vår listunspent-utgång kan vi hitta två UTXO:er, på var och en kan vi se txid och vout, dessa är utgångarna issuance_utxo och change_utxo.
'receive_utxo' är en UTXO som kontrolleras av mottagaren. I det här fallet kommer vi att använda e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 som är en outpoint från en annan plånbok.

- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Nu kommer vi att skapa en delvis signerad transaktion (tx.psbt) där utgången kommer att justeras för att inkludera en överföringsförbindelse. Kom ihåg att byta ut txid och vout med dina egna. Mottagaradressen spelar inte så stor roll, den kan vara din egen eller någon annans, det spelar ingen roll vart dessa sats går, det viktiga är att vi använder issuance_utxo.
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0'
```

Den här delen gav oss en psbt-kodad i base64 som vi kommer att använda för att skapa tx.psbt.
Skapa en ny katalog som heter rgbdata där datakatalogerna för varje nod lagras.

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

Redan i $HOME/rgbdata startar vi varje nod i olika terminaler, där ~/.cargo/bin är katalogen där cargo har kopierat alla binärer efter installationen av rgb-node.

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## Emission

För att utfärda en tillgång kör vi rgb0-cli med underkommandon för utsläpp av fungibla tillgångar, sedan argumenten, USDT-ticker, namnet "USD Tether" och i tilldelningen använder vi utsläppsmängden och issuance_utxo som visas nedan:

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

Tillgång utfärdad framgångsrikt. Använd denna information för att dela:
Information om tillgången:
Vi får assetId, vilket vi behöver för att överföra tillgången.

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

## Generera en blindad UTXO

För att ta emot de nya USDT måste rgb-node-1 generera en blindad UTXO som matchar receive_utxo för att innehålla tillgången.
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0
Förblindad utpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Förblindningshemlighet för utpoint: 1679197189805229975

För att kunna acceptera överföringar relaterade till denna UTXO behöver vi den ursprungliga receive_utxo och förblindningsfaktorn.

## Överföring

För att överföra en viss mängd tillgångar till rgb-node-1 måste vi skicka dem till den förblindade UTXO:n. rgb-node-0 måste skapa en sändning och en avslöjande, och validera dem i en bitcoin-transaktion. Sedan behöver vi en psbt som vi kommer att ändra för att inkludera åtagandet. Dessutom tillåter alternativen -i och -a oss att ange en inmatningsutpoint som skulle vara ursprunget för tillgången och en tilldelning där vi kommer att få växelmynt, vi måste ange det på följande sätt @<change_utxo>.

```
'$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
Överföringen lyckades, sändningar och avslöjanden är skrivna i "consignment.rgb" och "disclosure.rgb", den delvis signerade vittnesbördstransaktionen i "witness.psbt".'
Data att dela: consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
Detta kommer att skapa tre nya filer, consignment, disclosure och psbt inklusive tweak, denna psbt kallas witness transaction, consignment skickas till rgb-node-1.

## Witness

Witness-transaktionen måste signeras och sändas, för detta måste vi koda den i base64.

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

Signera den med underkommandot walletprocesspsbt.
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="{'
'"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",  "complete": true}'
'$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}
```

## Sprid

Sprid det genom att använda underkommandot sendrawtransaction för att få det bekräftat i blockchainen.
## Acceptera

För att acceptera en inkommande överföring måste rgb-node-1 ha mottagit konsignationsfilen från rgb-node-0, ha receive_utxo och motsvarande blinding_factor som genererades vid skapandet av borttagnings-UTXO.

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Tillgångsöverföring accepterad framgångsrikt.
```

Vi kan nu se (i knownAllocations-fältet) den nya tilldelningen av 100 enheter av tillgången i <receive_utxo> genom att köra:

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT'
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

Eftersom receive_utxo var förblindad när överföringen gjordes har betalaren rgb-node-0 ingen information om var de 100 USDT skickades, så platsen visas inte i knownAllocations.

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

Men som ni kan se kan rgb-node-0 inte se ändringen av tillgången på 900 som vi har tillhandahållit till överföringskommandot med argumentet -a. För att registrera ändringen måste rgb-node-0 acceptera avslöjandet.

```
$ rgb0-cli fungible enclose disclosure.rgb

Data för avslöjande framgångsrikt inkluderat.
```

Om rgb-node-0 lyckades kan du se ändringen genom att lista tillgången.

```
$ rgb0-cli fungible list -l
- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
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
## Slutsatser
Vi har kunnat skapa en utbytbar tillgång och flytta den från en transaktion till en annan på ett privat sätt. Om vi kontrollerar den bekräftade transaktionen i en blockutforskare kommer vi inte att hitta något annorlunda jämfört med en vanlig transaktion, detta beror på att RGB använder engångssigill för att justera transaktioner. I den här artikeln presenterar jag en introduktion till hur RGB fungerar.

Denna artikel kan innehålla buggar, om du hittar några, vänligen låt mig veta för att förbättra denna guide. Förslag och kritik är också välkomna, lycklig hacking! 🖖