---
name: Blitz Wallet
description: Najjednoduchsia Bitcoin penazenka.
---

![cover](assets/cover.webp)

Pouzivatelsky zazitok je jednym z rozhodujucich faktorov pri vybere Bitcoin penazenky. V tomto navode vam predstavujeme Blitz Wallet, penazenku, ktora stavia jednoduchost do centra svojho pristupu: vdaka integracii protokolu **Spark** vam Blitz ponuka jednu z najjednoduchsich a najkompletnejsich Bitcoin penazeniek na trhu, s okamzitymi platbami a bez technickej spravy.

## Co je Blitz Wallet?

Blitz Wallet je **self-custodial** a **open source** Bitcoin penazenka, ktora stavla na vasu suverenitu a plynuly a intuitivny pouzivatelsky zazitok.

[Blitz Wallet](https://blitz-wallet.com/) je mobilna aplikacia dostupna na Android (Play Store) a iOS (App Store).

Na rozdiel od tradicnych Lightning penazeniek, ktore vyzaduju spravu platobnych kanalov a prichadzajucej likvidity, Blitz Wallet sa opiera o **protokol Spark** na eliminovanie tychto technickych zlozitosti. Vysledok: okamzite platby od prveho prijateho satoshiho, bez akejkolvek predchadzajucej konfiguracie. Cielom Blitz je urobit platby v bitcoine rovnako jednoduche ako klasicka platobna aplikacia, bez toho, aby sa niekedy ohrozila self-custody vasich prostriedkov.

Blitz Wallet tiez podporuje **citatelne adresy** vo formate `pouzivatel@domena.com` (cez LNURL), co umoznuje posielat bitcoiny rovnako jednoducho ako e-mail, bez nutnosti manipulovat s dlhymi invoices alebo QR codes pri kazdej transakcii.

## Pochopenie protokolu Spark

Pred prechodom k praxi je uzitocne pochopit technologiu, ktora pokreuje Blitz Wallet pod kapotou: **protokol Spark**.

### Co je Spark?

Spark je open source protokol nadstavbovej vrstvy postaveny na Bitcoine, vyvinuty timom Lightspark. Umoznuje vykonavat okamzite transakcie s nizkymi nakladmi, pricom zachovava self-custody vasich bitcoinov.

Na rozdiel od Lightning Network, ktory sa opiera o **platobne kanaly** medzi dvoma stranami, Spark pouziva technologiu nazyvanu **statechain** (retazec stavov). Zakladny princip je nasledovny: namiesto presuvana bitcoinov na blockchaine pri kazdej transakcii, Spark prenasa **pravo minutia** z jedneho pouzivatela na druheho, bez on-chain pohybu.

### Ako to funguje?

Aby ste pochopili Spark intuitvnym sposobom, predstavte si, ze minutie bitcoinu na Spark-u vyzaduje dokoncenie puzzle z dvoch kusov:
- Jeden kus drzi pouzivatel (napriklad Alice).
- Druhy kus drzi skupina operatorov nazyvana **Spark Entity (SE)**.

Iba kombinacia dvoch zodpovedajucich kusov umoznuje minut bitcoiny.

Ked Alice chce poslat svoje bitcoiny Bobovi, stane sa toto: novy puzzle sa spolocne vytvori medzi Bobom a SE. Puzzle si zachova rovnaky tvar, ale kusy, ktore ho tvoria, sa zmenia. Odteraz Bobov kus zodpoveda kusu SE. Stary kus Alice sa stane nepouzitelnym, pretoze SE znicil svoj zodpovedajuci kus. Vlastnictvo bitcoinov zmenilo ruky, **bez akejkolvek transakcie na blockchaine**.

Bob potom moze zopakovat rovnaky proces na odoslanie tychto bitcoinov Carol, a tak dalej. Kazdy prevod funguje vymenou kusov puzzle, nie pohybom prostriedkov on-chain.

### Preco je to bezpecne?

Legitimna otazka vyvstava: co sa stane, ak SE v skutocnosti neznici svoj stary kus?

Spark Entity nie je jedina entita: je to skupina nezavislych operatorov. Kus SE nikdy nedrzi jediny operator. Vymena puzzle vyzaduje spolupracu viacerych operatorov. Staci, aby **jediny operator bol cestny** pocas prevodu, aby sa zabranilo reaktivacii stareho puzzle. Ziadny izolovany operator nemoze tajne uchovat stary aktivny puzzle alebo ho neskor znovu vytvorit.

Okrem toho Spark integruje mechanizmus jednostranneho vystupu: vzdy mozete ziskat svoje bitcoiny on-chain bez spoluprace SE. Tento zalohovaci mechanizmus je nedielnou sucastou architektury Spark a zarucuje, ze nikdy nie ste zavisli od siete na pristup k vasim prostriedkom.

### Spark vs Lightning Network

Spark a Lightning si nekonkuruju: su **komplementarne**. Blitz Wallet integruje oba, co vam umoznuje vyuzivat vyhody kazdeho z nich.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Technologia**               | Statechains (retazce stavov) | Platobne kanaly       |
| **Sprava kanalov**            | Nevyzadovana                 | Vyzadovana            |
| **Prichadzajuca likvidita**   | Nevyzadovana                 | Vyzadovana            |
| **Okamzite transakcie**       | Ano                          | Ano                   |
| **Self-custody**              | Ano                          | Ano                   |
| **Kompatibilita s Lightning** | Ano (cez atomic swaps)       | Nativna               |

Lightning Network zostava vybornym protokolom pre okamzite platby, ale kladie technicke obmedzenia (sprava kanalov, prichadzajuca likvidita, uzol online...), ktore mozu odradit zaciatocnikov. Spark tieto obmedzenia odstrannuje a zaroven zostava kompatibilny s Lightning.

## Instalacia a konfiguracia

V tomto navode vychadzame z verzie Blitz Wallet pre Android, ale vsetky procesy prezentovane nizsie platia aj pre iOS.

![installation](assets/fr/01.webp)

Kedze Blitz Wallet je self-custody penazenka, mate na vyber medzi **vytvorenim novej penazenky** alebo **importom fraxy na obnovenie** (12 alebo 24 slov) z existujucej penazenky.

Tu zacneme vytvorenim novej penazenky. Nizsie najdete nase odporucania na zalohovanie vasej fraxy na obnovenie:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **DOLEZITE**: Tychto 12 alebo 24 slov na obnovenie je **jediny kluc na pristup k vasim bitcoinom**. Blitz je self-custodial penazenka: ani Blitz ani Spark nemaju pristup k vasej fraze na obnovenie ani k vasim prostriedkom. Ak tieto slova stratite, navzdy stratite pristup k vasim bitcoinom. Nezdielate ich s nikym: ktokolvek, kto ich vlastni, moze minut vase bitcoiny.

Potom vytvorte **PIN** na zabezpecenie pristupu k vasej penazenke.

![setup-wallet](assets/fr/02.webp)

## Zaciatok s Blitz

Vykonavanie transakcii s Blitz je intuitvnejsie nez vo vacsine ostatnych Bitcoin penazeniek. Rozhranie je minimalisticke a zamerane na tri hlavne akcie: odoslat, naskenovat a prijat.

### Prijimanie bitcoinov

Ak chcete prijat bitcoiny na vasu Blitz penazenku, kliknite na ikonu **"Sipka nadol"** (↓), zadajte sumu v satoshioch, ktoru chcete prijat, pridajte volitelny popis a penazenka vygeneruje invoice, ktoru mozete zdielat s odosielatelom.

⚠️ **POZNAMKA**: Satoshi (alebo "sat") je najmensou jednotkou bitcoinu: **1 bitcoin = 100 000 000 satoshiov**.

Jednou z osobitosti Blitz Wallet je, ze podporuje viacero sieti a protokolov ekosystemu Bitcoin:

- **Lightning Network**: Jedna z nadstavbovych vrstiev Bitcoinu, ktora umoznuje okamzite mikroplatby s velmi nizkymi poplatkami. Idealny pre male dennne sumy.

- **Bitcoin (on-chain)**: Hlavny blockchain protokolu Bitcoin, vhodny pre transakcie vacsich sum, kde je prioritou maximalna bezpecnost a finalita.

- **Liquid Network**: Sidechain (paralelny retazec) Bitcoinu vyvinuty spolocnostou Blockstream, ktory umoznuje rychle a doverne transakcie pomocou Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Standardne Blitz generuje Lightning invoice, ale mozete si vybrat siet, na ktorej chcete prijat svoje satoshie, kliknutim na tlacidlo **"Choose format"**.

![receive-sats](assets/fr/03.webp)

### Vytvaranie kontaktov

Blitz Wallet zjednodusuje opakujuce sa odosielanie bitcoinov vdaka svojmu systemu kontaktov.

V menu **Contacts** mozete registrovat pouzivatelske mena Blitz alebo Lightning adresy (LNURL), s ktorymi casto komunikujete.

Takto mozete posielat satoshie na tieto adresy na par kliknuti, bez nutnosti skenovat QR code alebo manualne zadavat adresu zakazdym.

### Odosielanie bitcoinov

Okrem klasickych metod odosielania bitcoinu (skenovanie QR code, manualne zadanie adresy) Blitz ponuka niekolko praktickych moznosti:

- **Z obrazka** (*From Image*): Importujte QR code z vasej fotogalerie.
- **Zo schranky** (*From Clipboard*): Prilepte predtym skopirovanu adresu alebo invoice.
- **Manualne zadanie** (*Manual Input*): Priamo zadajte Bitcoin adresu, Lightning invoice alebo citatelnu adresu (napriklad `pouzivatel@walletofsatoshi.com`).
- **Z vasich kontaktov**: Vyberte vopred registrovaneho prijemcu na odoslanie na par kliknuti.

V menu **Wallet** kliknite na tlacidlo **"Sipka nahor"** (↑), vyberte svoju metodu odoslania, zadajte sumu na odoslanie, pridajte popis a potvrdte transakciu.

Minimalna suma na vykonanie odoslania je v sucasnosti **1 000 satoshiov**.

![send-bitcoin](assets/fr/05.webp)

## Obchod Blitz

Okrem operacii prevodu bitcoinov Blitz Wallet integruje obchod, v ktorom mozete minut svoje bitcoiny na nakup digitalnych sluzieb priamo z aplikacie.

Z hlavneho menu kliknite na kartu **Store** pre pristup do obchodu. Najdete tam aj pristup k platforme **Bitrefill**, ktora umoznuje nakup darcekovych kariet od tisicov obchodnikov po celom svete, priamo v bitcoine.

- **Umela inteligencia**: Pristupte k najnovsim generativnym AI modelom (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) a platte svoje kredity priamo v satoshioch. K dispozicii je niekolko balikov podla vasich potrieb (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonymne SMS**: Posielajte a prijimajte SMS po celom svete bez odhalenia vasho osobneho cisla telefonu. Sluzba je uctovana v satoshioch za kazdu odoslanu spravu.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Chrante svoje sukromie online prihlasenim sa na VPN WireGuard (tyzdenne, mesacne alebo stvrtrocne), platitelne v bitcoine priamo z obchodu Blitz. Staci si stiahnut klientsku aplikaciu WireGuard na vase zariadenie a mozete ju pouzivat.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet v zakulisi: ist dalej

Za jednoduchostou pouzivania Blitz Wallet sa skryva dobre premyslena technicka architektura, ktora kombinuje viacero vrstiev ekosystemu Bitcoin.

### Rozdelenie vasho zostatku

Blitz Wallet spravuje vas zostatok transparentne, rozdelujuc vase prostriedky medzi rozne protokoly podla potrieb. Ked je vas zostatok nizsi ako 500 000 satoshiov, Blitz pouziva **Liquid Network** a atomic swaps, aby vam poskytol plynuly zazitok a umoznil transakcie na Lightning Network aj s malymi sumami.

Tento pristup zarucuje jednoduche zavedenie pre novych pouzivatelov, bez nutnosti pochopit zakladne mechanizmy. Rozdelenie vasho zostatku medzi rozne vrstvy si mozete pozriet v menu **Nastavenia > Balance Info**.

![balance](assets/fr/09.webp)

### Rezim Lightning (volitelny)

Standardne Blitz Wallet pouziva Liquid Network a protokol Spark, aby vam poskytla plynuly zazitok bez technickej konfiguracie. Blitz vam vsak dava moznost aktivovat **rezim Lightning**, ktory automaticky otvori platobny kanal, ked dosiahnete zostatok **500 000 satoshiov** (0,005 BTC).

Na aktivaciu rezimu Lightning prejdite do **Nastaveni**, potom v sekcii **Technicke nastavenia** kliknite na moznost **Node Info**.

![enable-lightning](assets/fr/10.webp)

Vdaka protokolu Spark je tato aktivacia **volitelna**: Spark uz umoznuje vykonavat platby kompatibilne s Lightning bez nutnosti otvarania kanala alebo spravy prichadzajucej likvidity. Nativny rezim Lightning zostava uzitocny pre pokrocilych pouzivatelov, ktori chcu mat vlastny Lightning uzol integrovany v aplikacii.

### Predajne miesto (PoS)

Blitz Wallet integruje funkcionalitu **predajneho miesta**, ktora umoznuje obchodnikom prijimat platby v bitcoine priamo z aplikacie.

V menu **Nastavenia > Point-of-sale** mozete nakonfigurovat:

- Jedinecny identifikator vasho obchodu
- Lokalnu fiat menu na zobrazenie cien
- Pokyny pre vasich zamestnancov
- Moznost prepitneho pre vasich zakaznikov

Vasi zakaznici musia iba naskenovat vygenerovany QR code na vykonanie svojej platby v bitcoine, okamzite.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Zdroje pouzite na napisanie tohto navodu:
- Blog [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
