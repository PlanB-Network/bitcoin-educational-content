---
name: JoinMarket

description: Guide och handledning om hur man använder JoinMarket för att göra CoinJoin över Bitcoin via kommandoraden
---

![cover](assets/cover.webp)



---

Om du hittade den här sidan genom att söka online efter "JoinTmarket" har du min uppriktiga uppskattning. Du har dock snubblat över en guide som handlar om ett helt annat, men extremt intressant ämne! 🚬🍁



Syftet med denna handledning är att illustrera den teoretiska och praktiska driften av JoinMarket, via kommandoraden. 🐢 💚



## JoinMarket Teoretisk definition



Vi kan definiera JoinMarket som ett verktyg, eller en Wallet, som möjliggör CoinJoin med andra användare på ett helt Trustless sätt och utan någon central samordnare.



Eftersom hela den teoretiska delen av det här verktyget är extremt bred bestämde jag mig för att Address det i ett specifikt avsnitt av min podcast. För dem som kan förstå italienska rekommenderar jag starkt att fortsätta läsa efter att ha lyssnat på avsnittet, så att du bättre kan tillgodogöra dig de grundläggande begreppen för att använda det här programmet på rätt sätt.



Du kan ta del av avsnittet via dessa direktlänkar:




- [Spotify] (https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast] (https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (här kan du lyssna på det direkt från webbläsaren).
- [Antenna pod](https://antennapod.org/) är en gratis podcasthanterare med öppen källkod som inte kräver registrering. För att hitta avsnittet ladda ner appen, lägg till min podcast manuellt genom att klistra in [den här länken](https://Anchor.fm/s/bd5d5b20/podcast/rss) i avsnittet _feed rss_ och sök sedan efter avsnittet tillägnad JoinMarket.



## Installation



Operativsystem:





- Raspiblitz
- Paraply
- MyNode
- Raspibolt



## Konfigurationsfiler



JoinMarket är en anpassningsbar programvara med ett oändligt antal inställningar; dessa inställningar anges i en konfigurationsfil som finns i huvudprogramkatalogen som heter `Joinmarket.cfg`.



I det här avsnittet går vi igenom några fält som du kan tycka är intressanta att utforska och/eller ändra, beroende på dina behov. Jag vill understryka att alla ändringar som anges nedan är bra att känna till för att kunna anpassa programvarans funktion till personliga behov, men att de inte är obligatoriska.



Låt oss först flytta till mappen `joinmarket/scripts` och köra kommandot:



```bash
python wallet-tool.py generate
```


I det här läget borde vi få ett felmeddelande, men om vi gör det kommer programmet att skicka generate till en förinställd inställningsfil åt oss. Vi kan gå och redigera inställningsfilen från terminalen med:



```bash
nano joinmarket.cfg
```



eller:



```bash
vim joinmarket.cfg
```



när vi har öppnat den kommer vi att märka många rader med olika inställningar och deras förklaring på engelska. Specifikt kommer vi att analysera nedan de mest intressanta variablerna:





- `merge_algorithm` ifall vi gör som en maker detta fält justerar hur aggressivt programvaran kommer att konsolidera outnyttjade Outputs. Om vi har många UTXO:er att konsolidera kan det vara vettigt att byta från _gradual_ till _greedy_
- `tx_fees` justerar som en taker avgifterna för att betala transaktionen, det är mycket användbart att ändra den här inställningen om du använder tumblern ofta (vi kommer att prata om detta senare) för om det finns en ökning av avgifterna under genomförandet av den senare, om vi inte ställer in det här fältet korrekt, riskerar vi att spendera mycket Sats för CoinJoin. Genom att ställa in värden i tusental (t.ex. 2000) kommer detta att motsvara 2 Sats/vBytes, 3500 till 3,5 Sats/vBytes, och så vidare. Jag skulle rekommendera ett tal mellan 1500 och 6000 beroende på dina behov.
- `max_cj_fee_abs` används för att ange hur mycket vi är villiga att betala i absoluta termer för de makers vi väljer under CoinJoin. Som standard är detta fält för makers 200 Sats, ett bra alternativ kan vara ett nummer som sträcker sig från 200 till 1000 Sats per motpart (detta baseras på hur mycket du vill spendera och hur mycket anon-set du vill ha för dina CoinJoins)
- `max_cj_fee_rel` har samma funktion som fältet ovan men anger de relativa avgifter (procent) som vi är villiga att betala till varje motpart. Eftersom detta är ett "procentvärde", var försiktig så att du inte sätter höga värden för att undvika höga kostnader i CoinJoins med stora belopp. Standardvärdet för makers är _0,00002_, jag rekommenderar ett liknande eller något högre värde.
- `minimum_makers` är det fält som anger hur många andra motparter vi gör CoinJoin med, som standard väljer joinMarket alltid mellan 4 och 9 motparter, om vi vill, för mer integritet, kan vi höja detta värde till 5 eller 6 (det kommer dock att göra transaktionerna dyrare).
- `cjfee_a` anger, om vi agerar som en maker, hur många Sats i absoluta tal vi vill samla in för att hyra vår likviditet. Detta fält är helt subjektivt, standardvärdet är redan mycket bra (vi kommer därmed att ha bättre integritet som maker), vi kan överväga att ta det till 0 om vi vill tjäna mer CoinJoin på kortare tid.
- `cjfee_r` samma som ovanstående fält men i procentuella termer och inte absoluta. Även här rekommenderar jag att du behåller standardvärdet eller sänker det för att locka fler användare.
- `ordertype` med detta fält väljer vi från tillverkaren om vi ska debitera absolut (absoffer) eller procentuellt (reloffer). Vanligtvis föredrar tagare absoluta bud för ekonomiska frågor.
- `minsize` om vi som tillverkare inte vill att UTXO ska vara för litet kan vi ange minsta CoinJoin för att delta. Detta fält uttrycks i Satoshi och är helt subjektivt. Vi kan lämna detta fält på 0 eller öka till 500000 (Sats), 1000000 (Sats), och så vidare.



Var mycket försiktig så att du inte redigerar fel fält, vissa av variablerna i filen joinmarket.cfg om de ställs in felaktigt kan äventyra programvarans funktionalitet eller helt utplåna din integritet, ögon öppna och försiktighet till max!



## Inställning av arbetsmiljön



Vissa noder ställer automatiskt in de korrekta värdena för dessa fält i filen joinmarket.cfg, men jag rekommenderar att du kontrollerar manuellt:





- `rpc_user = dittanvändarnamn-som-i-Bitcoin.conf`
- `rpc_password = ditt lösenord-som-i-Bitcoin.conf`
- `rpc_host = localhost #default vanligtvis korrekt`
- `rpc_port = 8332 # standard för Mainnet`



Vid denna punkt kan vi fortsätta med skapandet av vår Wallet inom JoinMarket:



```bash
python wallet-tool.py generate
```



Detta kommando kommer att få oss att ange ett lösenord för att kryptera Wallet och det namn vi vill ge det, när det frågar dig om du vill stödja trohetsobligationer eller inte rekommenderar jag att du använder alternativet _yes_, utmatningen som returneras kommer att se ut så här:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


om ett fel visas är det troligt att vi har ställt in de 4 RPC-fälten som anges ovan felaktigt. I så fall kan det hjälpa att följa [denna guide] (https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) som finns i den ursprungliga JoinMarket-dokumentationen.



Nu är vår arbetsmiljö färdiginställd och vi kan börja utforska de kommandon som kommer att vara mest användbara för oss. Alla skript som vi kommer att diskutera kan startas i konsolen följt av `--help` för en djupgående förklaring.



Vi kan nu försöka starta:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



detta kommando kommer att visa dig alla de olika Wallet mixdjupen med de olika adresserna kategoriserade som:




- Ny (Address aldrig använd)
- Change-out (återstoden av en tidigare transaktion)
- Cj-out (utmatning från en CoinJoin)



här är ett praktiskt exempel på resultatet:



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Nu kan vi fortsätta att sätta in våra första Satoshis inom en eller flera adresser och komma ihåg att oavsett tillverkare eller tagare kommer programvaran aldrig att gå och konsolidera UTXO i olika mixdjup direkt, på detta sätt kan vi hålla Satss med olika sekretessnivåer separata inom Wallet.



## Skicka Bitcoin med CoinJoin Enstaka



Vi kan nu flytta våra Satoshis. Ett av huvudkommandona i den här programvaran är skriptet:



```bash
pyhton sendpayment.py
```


vilket gör att vi kan skicka transaktioner till andra adresser med eller utan CoinJoin. Låt oss gå igenom hur det fungerar och några praktiska exempel. Som standard är formateringen av kommandot (kom ihåg att ersätta texten som är innesluten av symbolerna < och >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



ett grundläggande exempel på användning kan vara:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


i det här fallet ska vi skicka till Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0,05 Btc dvs. 5000000 Satoshi från vårt mixdjup 0 (standard) genom att välja mellan 4 och 9 motparter för CoinJoin (standardalternativ).



För att få mer kontroll över hur och vilka UTXO:er som ska spenderas kan vi gå igenom de ytterligare alternativen till detta kommando:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


i det här exemplet har vi lagt till två specifikationer: -N anger hur många motparter vi ska mixa med, -m mixdjupet från vilket vi ska ta ut medel. Faktum är att vi har skickat 100 000 000 Sats (1 btc) till Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c med pengarna i mixdjup 1 och mixat med 5 motparter.



Om vi anger 0 som sändningsvärde genom att ange en mixdjup, kommer joinMarket att utföra en så kallad `sweep`, det vill säga, den kommer att skicka alla fonder i den mixdjupet genom att konsolidera dem med varandra:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



här skickade vi alla medel från mixdjup 0 (vi kunde inte ha angett det eftersom det är standard) och blandade med 7 motparter.



Kommandot sendpayment används för att flytta pengar från joinMarket till externa Wallet eller för att skicka Satoshi till en person genom att lägga till en Layer av sekretess mellan oss och honom. För att få en tillräcklig sekretessnivå på våra UTXO:er är det lämpligare att använda kommandot tumbler.py som vi kommer att förklara senare i den här guiden.



## Att vara en skapare



Det skript som vi kommer att behandla i detta avsnitt är:



```bash
yg-privacyenhanced.py
```



Detta program används för att agera som en maker i joinMarket. Programvaran kommer att ansluta till vår Bitcoin-nod och till plattformens interna marknadsplats där makers presenterar sig själva som likviditetsbudgivare och takers letar efter motparter. Om du vill använda en trohetsgaranti kan du skapa en med denna formatering:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



till exempel:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



den utgång som kommer att returneras till oss kommer att vara en Bitcoin Address (dvs. den som du måste sätta in de medel du vill allokera till fidelity på).



** Försiktighet**: Det finns två saker du måste vara uppmärksam på om du ska skapa en Fidelity Bond (a.k.a. FB);





- när medlen har satts in kan de inte flyttas igen förrän det löper ut. Var uppmärksam på hur många Satss du skickar till Address och hur du formaterar datumet. Fel är inte tillåtna!
- Den trohetsbindning är lätt igenkännlig påchain, så det är lämpligt att sätta in pengar genom en CoinJoin och med ett ursprung som inte är relaterat till din identitet. Samma sak är också lämpligt att göra när du vill flytta den utgångna trohetsbindning ut ur JoinMarket.



Det är viktigt att komma ihåg att det är möjligt att ladda om trohetsobligationen med endast en transaktion, i händelse av UTXO-multiplar kommer endast den största att betraktas som giltig för FB.



Låt oss nu ta itu med det skript som nämns i början av detta stycke, när vi har skapat trohetsobligationen (som vi kommer ihåg är valfri) är vi redo att köra den körbara filen för att fungera som en maker på joinMarket. När Satss har deponerats på de olika adresserna och mixdjupet kan vi köra kommandot:



```bash
python yg-privacyenhanced.py <wallet name>
```



Från och med nu (efter några minuters anslutning till nätverket) och tills vi stoppar skriptet kommer vår JoinMarket-klient att visas på listan över aktiva makers på protokollet och erbjuda vår likviditet till olika motparter för att göra CoinJoin. Förvänta dig inte dussintals CoinJoins per dag (såvida du inte har enorm fidlity och stor likviditet deponerad på Wallet), kom också ihåg att faktorer som avgifter som krävs och Satoshis deponerade påverkar hur ofta du kommer att vara en maker.



Genom att köra kommandot nedan kommer du att kunna se historiken för alla transaktioner som gjorts på Wallet och eventuell vinst (om du är en maker) eller avgiftskostnad (om du är en taker) som du har haft under Wallet:s livstid.



```bash
python wallet-tool.py <wallet name> history
```



När dina Satoshis gör CoinJoins kommer de att flytta från mixdjup till mixdjup tills de når det sista. När de har passerat den fjärde kommer de att återgå till mixdjup 0, det är upp till dig hur mycket integritet du vill få innan du flyttar dem till en Cold Wallet, det är tillrådligt att avsluta en hel Wallet cykel.



## Tumbler



Här är vi äntligen på den saftigaste delen av JoinMarket, tumlaren! Om du har lyssnat på podcasten vet du redan vad det handlar om. En rekommendation innan vi sätter igång: **Kom ihåg att ställa in gränserna i filen joinmarket.cfg (som förklarades i början) och överväga att köra programmet endast när onchain-avgifterna är relativt låga (under 10 Sats/vB).



För att starta tumlaren är det nödvändigt att ha stoppat skriptet från maker (om det var aktivt), efter det kan vi köra kommandot:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Det är viktigt att ange **mindst** 3 utgångsadresser för tumblern: detta för att säkerställa god integritet och inte skapa uppenbara länkar mellan UTXO:er under hela processen. Som vanligt kan man lägga till "help" till kommandot för att se alla ytterligare detaljer. Låt oss gå för att se ett mer komplext exempel med avancerade regler:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



I det här fallet har vi lanserat ett tumblingskript som inte kommer att använda standardantalet counterparts (parametern -N anger att vi behöver 7 counterparts med en maximal varians på 2, så ett slumpmässigt antal makers från 5 till 9) och med ett större antal CoinJoin per mixdjup (som standard gör detta skript ett slumpmässigt antal CoinJoin per sektion av Wallet som sträcker sig från 1 till 3, med kommandot -c 3 1 blir det istället från 2 till 4). På så sätt kommer vi att spendera mer Sats i avgifter men ha en större anonymitetsuppsättning.



Du kan också lägga till så många utdataadresser som du vill (minst 3, det finns inget maximum annat än sunt förnuft). Av integritetsskäl är det dock inte möjligt att bestämma hur Satoshi ska distribueras mellan de adresser som anges som utdata.



Tumbler är en medvetet lång process, ibland kan det hända att något slutar fungera, i de flesta fall kommer detta att lösa sig inom några timmar. I händelse av en total krasch kan vi försöka starta om den med kommandot:



```bash
python tumbler.py --restart
```



Eller starta helt enkelt om ett nytt tumlingskommando. Detta kommer inte att starta schemaläggningen av den föregående tumblern utan kommer att starta en ny blandningscykel. Om SSH-terminalen till din nod också stoppar skriptet kan du dra nytta av programmet `TMUX` som kan installeras med kommandot:



```bash
sudo apt install tmux
```



Om du startar den från skalet genom att skriva `tmux` öppnas en terminal åt dig som förblir aktiv i bakgrunden även om du stänger fjärranslutningen. När du återansluter till din nod med kommandot: `tmux attach` kommer du att öppna skalet igen som förblev aktivt i bakgrunden.



## Slutsats



JoinMarket är gränslös och anpassningsbar programvara. I den här guiden har vi upptäckt de viktigaste funktionerna så att det är möjligt för alla (eller åtminstone jag har försökt, jag inser att använda denna programvara är inte en promenad i parken) att använda den. Ett av de största problemen med JoinMarket är just det: antalet personer som använder det och vara en maker. Om få användare drar nytta av denna programvara, den övergripande integriteten (anon-set) sänks. Det är därför jag hoppas att den här guiden kommer att stimulera användningen och övertyga dig om att ladda ner och installera min favoritprogramvara för att göra CoinJoin. Om du vill gå ännu djupare in i vissa aspekter rekommenderar jag att du läser de olika djupgående dokumenten på github, de är mycket välgjorda och du hittar dem här.



Lycklig blandning av sköldpaddor!🐢 💚



[Här] (https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) kan du stödja Turtlecute