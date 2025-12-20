---
name: RGB
description: Въведение и създаване на активи в RGB
---

![cover](assets/cover.webp)


## въведение


На 3 януари 2009 г. Satoshi Nakamoto стартира първия възел на Bitcoin, от този момент нататък към него се присъединяват нови възли и Bitcoin започва да се държи така, сякаш е нова форма на живот, форма на живот, която не спира да се развива, малко по малко тя се превръща в най-сигурната мрежа в света в резултат на уникалния си дизайн, много добре обмислен от Satoshi, тъй като чрез икономически стимули привлича потребителите, наричани миньори, да инвестират в енергия и изчислителна мощ, което допринася за сигурността на мрежата.


Тъй като Bitcoin продължава да расте и да се приема, тя се сблъсква с проблеми с мащабируемостта, мрежата на Bitcoin позволява нов блок с транзакции да бъде добит за приблизително 10 минути, ако приемем, че имаме 144 блока за един ден с максимални стойности от 2700 транзакции на блок, Bitcoin би позволила само 4,5 транзакции в секунда, Satoshi е била наясно с това ограничение, можем да го видим в имейл1 , изпратен до Майк Хърн през март 2011 г., където той обяснява как работи това, което познаваме днес като канал за плащане. микроплащания бързо и безопасно, без да се чака потвърждение. Именно тук се появяват протоколите на off-chain.


Според Кристиан Декер2 протоколите извън веригата обикновено са системи, в които потребителите използват данни от дадена блокчейн и ги управляват, без да докосват самата блокчейн до последния момент. Въз основа на тази концепция се ражда Lightning Network - мрежа, която използва протоколи off-chain, за да позволи почти мигновено извършване на плащания Bitcoin и тъй като не всички тези операции се записват в блокчейн, тя позволява хиляди трансакции в секунда и мащабиране на Bitcoin.


Изследванията и разработките в областта на протоколите off-chain на Bitcoin отвориха кутията на Пандора, днес знаем, че можем да постигнем много повече от прехвърляне на стойност по децентрализиран начин, Асоциацията с нестопанска цел за стандарти LNP/BP се фокусира върху разработването на протоколи на ниво 2 и 3 на Bitcoin и Lightning Network, сред тези проекти се откроява RGB.


## Какво представлява RGB?


RGB се появява от изследванията на Питър Тод3 за печатите за еднократна употреба и валидирането от страна на клиента, което е създадено през 2016-2019 г. от Джакомо Дзуко и общността в по-добър протокол за активи за Bitcoin и мрежата Lightning. По-нататъшната еволюция на тези идеи доведе до разработването на RGB в пълноценна система за интелигентни договори от Максим Орловски, който ръководи нейното изпълнение от 2019 г. с участието на общността.


Можем да определим RGB като набор от протоколи с отворен код, който ни позволява да изпълняваме сложни интелигентни договори по мащабируем и конфиденциален начин. Това не е конкретна мрежа (като Bitcoin или Lightning); всеки интелигентен договор е просто набор от участници в договора, които могат да си взаимодействат, използвайки различни комуникационни канали (по подразбиране мрежата Lightning). RGB използва блокчейн на Bitcoin като слой за ангажиране на състоянието и поддържа кода на интелигентния договор и данните на off-chain, което го прави мащабируем, използвайки транзакциите на Bitcoin (и Script) като система за контрол на собствеността на интелигентните договори; докато еволюцията на интелигентния договор се определя от схема на off-chain, накрая е важно да се отбележи, че всичко се валидира от страна на клиента.


С прости думи, RGB е система, която позволява на потребителя да одитира интелигентен договор, да го изпълни и да го провери индивидуално по всяко време, без да има допълнителни разходи, тъй като за това не използва блокчейн, както правят "традиционните" системи, сложни системи за интелигентни договори бяха въведени от Етериум, но поради това, че изисква от потребителя да изразходва значителни количества газ за всяка операция, те никога не са постигнали мащабируемостта, която обещаха, вследствие на което никога не е била опция за банкиране на потребителите, изключени от настоящата финансова система.


Понастоящем блокчейн индустрията насърчава това, че както кодът на интелигентните договори, така и данните трябва да се съхраняват в блокчейн и да се изпълняват от всеки възел на мрежата, независимо от прекомерното увеличаване на размера или злоупотребата с изчислителни ресурси. Схемата, предложена от RGB, е много по-интелигентна и ефективна, тъй като оборва парадигмата на блокчейн, като интелигентните договори и данните са отделени от блокчейн и по този начин се избягва насищането на мрежата, наблюдавано в други платформи, на свой ред тя не принуждава всеки възел да изпълнява всеки договор, а участващите страни, което добавя поверителност на невиждано досега ниво.


![RGB vs Ethereum](assets/1.webp)


## Умни договори в RGB


В RGB разработчикът на интелигентни договори дефинира схема, определяща правилата за развитие на договора във времето. Схемата е стандартът за конструиране на интелигентни договори в RGB и както емитентът, когато дефинира договор за емитиране, така и wallet или борсата трябва да се придържат към определена схема, по която трябва да валидират договора. Само ако валидирането е правилно, всяка от страните може да приема заявки и да работи с актива.


Интелигентният договор в RGB е насочен ацикличен граф (DAG) от промени в състоянието, като само част от графа е винаги известна, а до останалата част няма достъп. Схемата на RGB е основен набор от правила за еволюцията на този граф, с който започва интелигентният договор. Всеки участник в договора може да добавя към тези правила (ако това е разрешено от схемата) и полученият граф се изгражда от итеративното прилагане на тези правила.


## Дълготрайни активи


Заменяемите активи в RGB следват спецификацията на LNPBP RGB-204, когато се дефинира RGB-20, данните за актива, известни като "генезисни данни", се разпространяват чрез мрежата Lightning, която съдържа това, което е необходимо за използването на актива. Най-основната форма на активите не позволява вторично издаване, изгаряне на token, реноминиране или замяна.


Понякога емитентът ще трябва да емитира повече токени в бъдеще, т.е. стабилни монети като USDT, което поддържа стойността на всеки token обвързана със стойността на инфлационна валута като щатския долар. За да се постигне това, съществуват по-сложни схеми на RGB-20, като в допълнение към данните за генезиса те изискват от емитента да произвежда партиди, които също ще циркулират в мрежата на светкавиците; с тази информация можем да знаем общото циркулиращо предлагане на актива. Същото важи и за изгарянето на активи или за промяната на името им.


Информацията, свързана с актива, може да бъде публична или частна: ако емитентът изисква поверителност, той може да избере да не споделя информация за token и да извършва операциите при пълна конфиденциалност, но имаме и обратния случай, при който емитентът и притежателите се нуждаят от прозрачност на целия процес. Това се постига чрез споделяне на данните за token.


## Процедури RGB-20


Процедурата за изгаряне деактивира токените, като изгорените токени вече не могат да се използват.


Процедурата за замяна се извършва, когато се изгарят жетони и се създава ново количество от същия token. Това спомага за намаляване на размера на историческите данни на актива, което е важно за поддържане на скоростта на актива.


За да се подкрепи случаят на използване, при който е възможно да се изгарят активи, без да се налага да се заменят, се използва подсхема на RGB-20, която позволява само изгаряне на активи.


## Незаменими активи


Нетъргуемите активи в RGB следват спецификацията на LNPBP RGB-215 , като при работа с НФТ също имаме основна схема и подсхема. Тези схеми имат процедура за гравиране, която ни позволява да прикачваме потребителски данни от част от собственика на token, като най-честият пример, който виждаме в НФТ днес, е дигитално изкуство, свързано с token. Издателят на token може да забрани това гравиране на данни, като използва подсхемата RGB-21. За разлика от други блокчейн системи на НФТ, RGB позволява да се разпространяват големи по размер медийни данни token по напълно децентрализиран и устойчив на цензура начин, като се използва разширение на мрежата P2P Lightning, наречено Bifrost, което се използва и за изграждане на много други форми на специфични за RGB функционалности на интелигентни договори.


В допълнение към заменимите активи и НФТ, RGB и Bifrost могат да се използват за създаване на други форми на интелигентни договори, включително DEXs, ликвидни пулове, алгоритмични стабилни монети и т.н., които ще разгледаме в бъдещи статии.


## NFT от RGB спрямо NFT от други платформи



- Няма нужда от скъпо съхранение на блокчейн
- Няма нужда от IPFS, вместо това се използва мрежово разширение на Lightning (наречено Bifrost) (и то е напълно криптирано от край до край)
- Няма нужда от специално решение за управление на данни - отново Bifrost поема тази роля
- Не е необходимо да се доверявате на уебсайтове, които поддържат данни за токени NFT или за активи на емисии / ABI на договори
- Вградено криптиране на DRM и управление на собствеността
- Инфраструктура за резервни копия с помощта на Lightning Network (Bifrost)
- Начини за монетизиране на съдържанието (не само продажба на самия NFT, но и достъп до съдържанието, няколко пъти)


## Заключения


От стартирането на Bitcoin преди почти 13 години бяха проведени много изследвания и експерименти в тази област, както успехите, така и грешките ни позволиха да разберем малко повече как децентрализираните системи се държат на практика, какво ги прави наистина децентрализирани и кои действия са склонни да ги доведат до централизация, всичко това ни доведе до заключението, че истинската децентрализация е рядко и трудно постижимо явление, истинската децентрализация е постигната само от Bitcoin и поради тази причина ние съсредоточаваме усилията си да надграждаме върху нея.


RGB има своя собствена заешка дупка в рамките на заешката дупка на Bitcoin, докато падам надолу през тях, ще публикувам това, което научих, в следващата статия ще имаме въведение в LNP и RGB възли и как да ги използваме.



- 1 https://plan99.net/~mike/satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# Урок за RGB-възел


## Въведение


В този урок обясняваме как да използваме RGB-възел за създаване на заменяем token и как да го прехвърлим, този документ се основава на демонстрацията на RGB-възел и се различава по това, че този урок използва реални данни от тестовата мрежа и за това трябва да изградим собствен Partially Signed Bitcoin Transaction, psbt от сега нататък.


## Изисквания


Препоръчва се използването на дистрибуция на Linux, този урок е написан с Pop!OS, която се основава на Ubuntu и ще ви е необходима:



- товари
- Bitcoin core
- git


Забележка: Този урок показва изпълнението на команди в терминал на Linux, като за да разграничим написаното от потребителя и отговора, който той получава в терминала, включваме символа $, символизиращ подкана bash.


Ще трябва да инсталирате някои зависимости:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


Изграждане и изпълнение


RGB-възелът е в процес на разработка (WIP), затова трябва да се намираме в конкретен ангажимент (3f3c520c19d84c66d430e76f0fc68c5a66d79c84), за да можем да го компилираме и използваме правилно, за което изпълняваме следните команди.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


Сега го компилираме, като не забравяте да използвате флага --locked, тъй като във версията на clap е въведена прекъсваща промяна.


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


Както ни казва компилаторът rust, двоичните файлове са копирани в директорията $HOME/.cargo/bin, ако вашият компилатор ги е копирал на друго място, трябва да се уверите, че тази директория е включена в $PATH.


Сред инсталираните двоични файлове можем да видим три демона или услуги (файловете, които завършват на d) и cli (интерфейс на командния ред), cli ни позволява да взаимодействаме с основния rgbd daemon. Тъй като в този урок ще работим с два възела, ще ни трябват и два клиента, като всеки от тях трябва да се свърже със своя възел, за което създаваме два псевдонима.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


Можем просто да стартираме псевдонимите или да ги добавим в края на файла $HOME/.bashrc и да стартираме source $HOME/.bashrc.

Предпоставка


RGB-възелът не се занимава с никаква функционалност, свързана с wallet, а само изпълнява специфични за RGB задачи върху данните, които ще бъдат предоставени от външен wallet, например ядрото на биткойн. По-специално, за да демонстрираме основен работен процес с издаване и прехвърляне, ще ни е необходимо:



- Issuance_utxo, към който rgb-node-0 ще свърже новоиздадения актив
- A receive_utxo, при което rgb-възел-1 получава актива
- A change_utxo, където rgb-node-0 получава промяната на актива
- Частично подписана транзакция с биткойни (tx.psbt), чийто изходен публичен ключ ще бъде променен, за да включва ангажимент за прехвърляне.


Ще използваме клип на ядрото на биткойн, трябва да имаме bitcoind daemon, работещ в тестовата мрежа, това ще ни даде оперативна съвместимост и в края ще можем да изпратим собствените си активи на друг потребител на RGB, който е следвал този урок.


За по-голяма простота ще добавим този псевдоним в края на файла ~/.bashrc.


```
alias bcli="bitcoin-cli -testnet"
```


Нека изведем списъка с неизплатените изходни транзакции и изберем две, едната ще бъде issuance_utxo, а другата change_utxo, няма значение коя е тя, важното е, че издателят има контрол върху тези две UTXO.


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


Преди да продължим, трябва да поговорим за изходните точки, една транзакция може да включва множество изходи, изходната точка включва както 32-байтово TXID, така и 4-байтово индексно число на изхода (vout), за да се отнесе към конкретен изход, разделени с двоеточие :. В нашия изход listunspent можем да намерим два UTXO, на всеки от тях можем да видим txid и vout, това са изходните точки issuance_utxo и change_utxo.


receive_utxo е UTXO, контролиран от приемника, в този случай ще използваме e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0, което е изходна точка от друг wallet.



- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


Сега ще създадем частично подписана транзакция (tx.psbt), чийто изход ще бъде променен, за да включва ангажимент за прехвърляне, не забравяйте да замените txid и vout с вашите собствени, адресът на местоназначението няма значение, може да е ваш или от друг човек, няма значение къде отива този sats, важното е да използваме issuance_utxo.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


Изходът ни даде psbt в base64 кодиране, което ще използваме за създаване на tx.psbt.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


Нека създадем нова директория, наречена rgbdata, в която се съхраняват данните на всеки възел.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


Вече разположени в $HOME/rgbdata, стартираме всеки възел в различни терминали, където ~/.cargo/bin е директорията, в която cargo е копирал всички двоични файлове след инсталирането на rgb-възела.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## Издаване


За да издадем актив, стартираме rgb0-cli с подкомандите за издаване на заменими активи, след това аргументите, тикера USDT, името "USD Tether" и в разпределението ще използваме сумата за издаване и issuance_utxo, както виждаме по-долу:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


Активът е успешно издаден. Използвайте тази информация за споделяне:

Информация за активите:


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


Получаваме assetId, който ни е необходим, за да прехвърлим актива.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## Генериране на blinded UTXO


За да получи новия USDT, rgb-възел-1 трябва да generate blinded UTXO, съответстващ на receive_utxo, за да държи актива.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


За да можем да приемаме трансфери, свързани с този UTXO, ще ни трябват оригиналният receive_utxo и blinding_factor.


## Трансфер


За да прехвърлим някаква сума от актива на rgb-възел-1, трябва да я изпратим на blinded UTXO, rgb-възел-0 трябва да създаде консигнация и оповестяване и да ги ангажира в транзакция с биткойни. След това ще ни е необходим psbt, който ще модифицираме, за да включим предаването. Освен това опциите -i и -a ни позволяват да предоставим входна изходна точка, която ще бъде произходът на актива, и разпределение, където ще получим промяната, като трябва да я посочим по следния начин @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


Това ще напише три нови файла, пратка, разкриване и psbt, включително tweak, този psbt се нарича свидетел транзакция, пратката се изпраща на rgb-възел-1.


## Свидетел


Свидетелската транзакция трябва да бъде подписана и излъчена, като за целта трябва да я кодираме обратно с base64.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


Подпишете го с подкомандата walletprocesspsbt.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


Сега го финализирайте и вземете шестоъгълника.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## Предавания


Изпратете я чрез подкомандата sendrawtransaction, за да я потвърдите в блокчейна.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## Приемане на


За да приеме входящ трансфер, rgb-възел-1 трябва да е получил файла с пратката от rgb-възел-0, да има receive_utxo и съответния blinding_factor, генерирани по време на генерирането на Blinding UTXO.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


Сега можем да видим (в полето knownAllocations) новото разпределение от 100 единици активи в <receive_utxo>, като стартираме:


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


Тъй като receive_utxo е бил blinded, когато е направен трансферът, платецът rgb-node-0 няма информация за това къде са изпратени 100 USDT, така че местоположението не е показано в knownAllocations .


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


Но както можете да видите, rgb-възел-0 не може да види промяната на актива 900, която предоставихме на командата за прехвърляне с аргумента -a. За да регистрира промяната, rgb-node-0 трябва да приеме разкриването.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


Ако rgb-node-0 е бил успешен, можете да видите промяната, като изведете актива.


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


## Заключения


Ние сме били в състояние да се създаде заменим актив и да го премести от една транзакция в друга в частен начин, ако проверим потвърдената транзакция в блок изследовател ние няма да намерите нищо различно от редовен транзакция, това е благодарение на факта, че RGB използва еднократна употреба печати да се подобри на транзакциите, В този пост, Аз правя интро как RGB работи.


Този пост може да има грешки, ако откриете нещо, моля, уведомете ме, за да се подобри това ръководство, предложения, и критики също са добре дошли, щастлив хакерство! 🖖