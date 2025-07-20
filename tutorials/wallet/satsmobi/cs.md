---
name: Sats.mobi

description: A Telegram-accessible custodial Wallet
---

![cover](assets/cover.webp)


_Tento návod napsal_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi je Wallet, který funguje na platformě Telegram a má všechny funkce Lightning Network (správcovské) Wallet a řadu velmi zábavných funkcí. Vznikl z Fork již ukončeného LightningTipBota, zdědil všechny jeho funkce a zároveň přidal další aktuální, čímž se stal modernějším. Stejně jako LNTipBot i Sats.Mobi se hlásí k filozofii open-source. Wallet lze konfigurovat a spravovat samostatně naklonováním z tohoto [repozitáře](https://github.com/massmux/SatsMobiBot).


Pokud jej chcete používat jednoduše, spuštěním chatu na Telegramu zjistíte, že se jedná o bota.


## Nastavení

Ve vyhledávacím řádku Telegramu vyhledejte "satsmobi" a zobrazí se odkaz na [bot](@SatsMobiBot).


**Upozornění**: Pokud si nejste jisti, zda chcete vyhledávat přes Telegram, získejte bezpečný přístup k botovi pomocí následujícího [odkazu](https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Vše, co musíte udělat, abyste mohli začít, je stisknout tlačítko _START_


![image](assets/it/02.webp)


Chcete-li prozkoumat aplikaci Wallet, můžete vlevo dole vybrat možnost _Menu_.


![image](assets/it/03.webp)


Nyní mezi hlavními příkazy zvolte _/help_.


![image](assets/it/04.webp)


Sats.Mobi nás přivítá zobrazením zprávy s výčtem všech hlavních funkcí. Při spuštění bot také vytvořil LN Address, propojený se zvoleným handle na Telegramu (který je ve výchozím nastavení jedinečný). Jsou vidět příkazy pro odesílání a přijímání Sats s tímto Wallet, stejně jako další funkce, které uvidíme později. Zajímavé je také podívat se do nabídky _/rozšířené_


![image](assets/it/05.webp)


Je pozoruhodné, že Sats.Mobi vytvořil také anonymní LN Address, který slouží k získání soukromí. Bot pracuje s příkazy: stačí kliknout na příslušné slovo nebo napsat lomítko "/" do panelu zpráv a následně příkaz, který chcete provést. I když byl právě vytvořen Wallet, zvolte například _/transakce_


![image](assets/it/06.webp)


Tento příkaz zobrazí seznam posledních transakcí, v tomto konkrétním případě se rovná nule.


![image](assets/it/07.webp)


## Příjem Sats

Příkaz pro vytvoření Invoice a přijetí Sats je _/invoice_. Sats.Mobi pracuje výhradně v Satoshi, nejmenší jednotce Bitcoin; proto je pro vytvoření Invoice nutné napsat částku v Sats do lišty zpráv a poté ji odeslat v chatu s botem.

![image](assets/it/08.webp)


V následujícím příkladu byla zvolena částka 210 Sats.


![cover](assets/it/09.webp)


Po několika okamžicích čekání na přípravu kódu Invoice je k dispozici v textové podobě a ve formě kódu QR. Po zaplacení Invoice se na displeji Wallet zobrazí zůstatek. Pokud se z nějakého důvodu celková částka neaktualizuje, napište _/balance_ a stiskněte klávesu `enter`.


![image](assets/it/10.webp)


## Odesílání Sats


Ačkoli jsou Sats nesmírně cenným majetkem, s nímž by se člověk neměl loučit lehkovážně, Sats.Mobi činí tuto část atraktivní, provedení několika krátkých testů (tj. pár zkušebních transakcí) nebude problém.


### Platba společnosti Invoice


Nejjednodušší způsob, jak zaplatit Invoice, je zkopírovat řetězec zprávy `lnbc1xxxxx` a vložit jej do řádku zpráv po zadání příkazu _/pay_. **Správná syntaxe** vyžaduje ponechání mezery za příkazem.


![image](assets/it/11.webp)


Přístroj Wallet odešle zprávu s žádostí o potvrzení. Po kliknutí na _Pay_ je Invoice zaplacen.


![image](assets/it/12.webp)


Sats.Mobi se může spolehnout na efektivní a dobře propojený uzel Lightning, platby selžou jen zřídka, protože se mu vždy podaří najít správné směrování.


### Pohodlné placení z mobilu


Prohlížení na Telegramu, Sats.Mobi je k dispozici také v mobilu. Nejpohodlnější funkcí pro placení mobilem je skenování QR kódu, ale to Wallet postrádá z podstaty věci, protože se nejedná o samostatnou aplikaci, ale je obsažena v sociální síti. Aplikace Sats.Mobi je proto naprogramována tak, aby co nejvíce usnadnila práci s mobilem: skutečně dokáže dekódovat obrázek, jako je fotografie pořízená QR kódem Invoice, kterým chcete zaplatit.


Předpokládejme například, že chcete zaplatit Invoice ve výši 50 Sats.


![image](assets/it/20.webp)


Když se nám zobrazí, můžeme vyfotografovat příslušný kód QR.


![image](assets/it/21.webp)


Poté otevřeme Telegram na mobilu a v chatu s Sats.Mobi připojíme právě pořízenou fotografii QR kódu


![cover](assets/it/22.webp)


Po výběru ji odešleme botovi:


![image](assets/it/23.webp)

Sats.Mobi dekóduje fotografii a **prodleně předloží žádost o platbu** se správným popisem. Chat si vyžádá potvrzení, pro pokračování je třeba stisknout tlačítko _/platit_

![image](assets/it/24.webp)


Chvíli prosím počkejte, aby se platba mohla zpracovat.


![image](assets/it/25.webp)


Invoice za 50 Sats bylo zaplaceno, čehož bylo dosaženo bez použití kamery a její integrované funkce skenování.


### Sats.Mobi v Telegram Groups


![image](assets/it/27.webp)


Mezi funkcemi, které proslavily LNTipBot a které Sats.Mobi přináší do Telegramu, je i ta, která dělá zážitek pro členy skupiny zábavným a interaktivním.

Majitelé mohou bota pozvat, aby se připojil ke skupinovému chatu, a poté nominovat Sats.Mobi jako správce. Od tohoto okamžiku začíná zábava, protože členové mohou začít odměňovat ostatní uživatele za jejich přínos skupině.


- _/tip_ přidá tip odpovědí na zprávu;
- _/send_ odešle prostředky, přičemž jako příjemce uvede LN Address nebo handle Telegramu;
- _/faucet_ (v nabídce _/advanced_) umožňuje vytvořit řadu tipů, které mohou nejrychlejší členové skupiny sbírat kliknutím na _/collect_;
- _/tipjar_ (v nabídce _/rozšířené_) vytvoří další typ rozesílání, který lze odeslat uživatelům ve skupině.


Každý z těchto příkazů má svou syntaxi, která je vysvětlena v hlavní nabídce příkazů.


A pokud nejsme vlastníkem skupiny? Žádný problém: stačí požádat zakladatele o pozvání Sats.Mobi, přidat ho jako správce skupiny a máte vystaráno!


## Prodejní místa (POS)


Při prvním spuštění služby Sats.Mobi vytvoří bot pro uživatele také další funkci: **POS**. Toto "zařízení" aktivuje uživatel příkazem _/pos_ nebo kliknutím na příslušné tlačítko z konzoly vpravo dole. POS je vlastně webová aplikace, která se otevře jako vyskakovací okno na chatu Telegramu


![image](assets/it/14.webp)


Na displeji Interface se v levém horním rohu zobrazuje osobní rukojeť Telegramu uživatele a používá se jednoduše jako všechny pokladny: zadáním částky na klávesnici. Předpokládejme, že nyní chceme vybrat 21 eurocentů za službu. S vědomím, že Sats.Mobi nativně spravuje pouze Sats, není snadné provést přepočet v hlavě. Naopak, pokladna zobrazuje euro jako zúčtovací jednotku a zároveň ukazuje ekvivalent v Satoshi.


![image](assets/it/15.webp)

Kliknutím na _/OK_ se zobrazí účet Invoice, který lze zákazníkovi zobrazit prostřednictvím kódu QR nebo jej lze odeslat jako řetězec prostřednictvím rychlých zpráv, aby bylo možné jej zaplatit.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Pokladna je samozřejmě k dispozici i na mobilních telefonech, kde se k ní přistupuje stejným způsobem, jak bylo uvedeno výše.


![image](assets/it/18.webp)


Dobře se zobrazuje i na displeji mobilního telefonu:


![image](assets/it/19.webp)


## Další funkce


Existují i další funkce, které doplňují nabídku Sats.Mobi Wallet, který, jak jsme viděli, rozšiřuje koncept Wallet nad rámec operací přijímání a odesílání plateb:


- _/nostr_: pro připojení Wallet k vašemu vlastnímu uživateli Nostr pro příjem zaps;
- _/cashback_: zobrazuje kód, který lze předložit obchodníkovi a získat tak zpět peníze z nákupu;
- _/buy_: spustí řízený postup v rámci bota, který umožňuje nákup Sats za eura;
- _/activatecard_: žádost o aktivaci debetní karty NFC, kterou lze dobíjet prostřednictvím zařízení Sats.Mobi Wallet a pro kterou lze aktivovat oznámení;
- _/link_: vytvoří odkaz na váš vlastní Zeus nebo Blue Wallet, který lze použít jako dálkové ovládání pro tento Wallet.


## Závěr

Sats.Mobi je příjemný a zábavný Wallet, který vám připomene zážitky z LNTipBota s využitím pokročilejších funkcí LNBits. Je však třeba mít na paměti, že **je to služba správcovská**. Proto by měl být používán k držení velmi malého počtu Sats, není to hlavní Wallet pro vaše fondy Lightning Network. Existuje také vlastní kapacitní limit, který se rovná 500 000 Sats, což je limit, který se doporučuje nepřekračovat.


Pokud hledáte peněženky Lightning Network, které nejsou opatřeny ochranným pouzdrem, je rozhodně vhodné podívat se na jiné produkty.


---
### Dokumentace


- [Github](https://github.com/massmux/SatsMobiBot)
- Seznam přehrávání [videí](https://www.youtube.com/results?search_query=Sats.mobi) demo