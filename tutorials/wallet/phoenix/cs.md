---
name: Phoenix

description: Nastavení vaší peněženky Phoenix
---

![phoenix](assets/cover.webp)

## Úvod

Phoenix je nevlastnická lightning peněženka vytvořená týmem Acinq, který stojí za implementací Lightning Eclair.

Mějte na paměti, že Phoenix je mobilní aplikace zaměřená na Lightning platby, ale podporuje i platby na řetězci prostřednictvím integrovaných swapů. To znamená, že jakýkoliv vklad na řetězci do Phoenixu, bude okamžitě převeden do Lightning kanálu.

Pokud také chcete poslat na adresu na řetězci, Phoenix provede swap interně z vašeho LN kanálu na cílovou adresu na řetězci. Buďte si vědomi, že všechny tyto swapy mají svou cenu, protože zahrnují poplatek na řetězci.

Níže v sekci "Průvodce začátkem" vás provedeme procesem nastavení a také vysvětlíme více o tom, jak spravovat likviditu lightning s Phoenixem.

## Důležité zdroje
- Oficiální webová stránka Phoenix - [https://phoenix.acinq.co](https://phoenix.acinq.co)
- Dokumentace / FAQ stránka - [https://phoenix.acinq.co/faq](https://phoenix.acinq.co/faq)
- [Github stránka](https://github.com/ACINQ/phoenix/) | [Stránka Github Releases](https://github.com/ACINQ/phoenix/releases) (přímé stažení apk)
- [Podpora a diskuse](https://github.com/ACINQ/phoenix/discussions)
- [Blog Acinq](https://acinq.co/blog) - oznámení

## Video návod

![Phoenix: Bitcoin Lightning Wallet Tutorial](https://youtu.be/cbtAmevYpdM?si=zctujxtI0hI-jKpC)

## Průvodce začátkem

Zde je krok za krokem návod, jak začít s Phoenixem, nastavit, provádět / přijímat platby, spravovat likviditu, proces zálohování / obnovy.

### Stažení & Nastavení
Phoenix si můžete stáhnout a nainstalovat z: [App Store](https://apps.apple.com/us/app/phoenix-wallet/id1544097028) | [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet) | [Přímé stažení apk](https://github.com/ACINQ/phoenix/releases)

Postupujte podle instrukcí začínajících na úvodní obrazovce, krok za krokem.

![](assets/screenshot2.webp)

Budete informováni o automatickém vytváření lightning kanálů.
Od verze v2.0 je to velká aktualizace, která přináší "splicing" do Phoenixu:
- jediný dynamický kanál,
- žádný 1% poplatek za příchozí likviditu
- lepší předvídatelnost a kontrola
- trustless swapy

Pro více detailů se podívejte na [příspěvek na blogu Phoenix](https://acinq.co/blog/phoenix-splicing-update), zejména na nový model poplatků.

![](assets/screenshot3.webp)

### Rychlý průvodce likviditou

Jakmile tedy do této peněženky přijmete / vložíte satoshi, automaticky se otevřou kanály s uzlem ACINQ. Obvykle bude velikost kanálů o něco větší než částka, kterou jste vložili. Takže vždy budete mít nový kanál pro každý vklad, kromě případů, kdy jste kanál zcela nevyčerpali a přijmete menší platbu, která bude doplněna.

Pro likviditu Phoenix Lightning bychom navrhli následující scénář:

S novou verzí v0.2.0 přichází nová funkce LN splicing. To znamená, že odteď se už nebudete muset zabývat spoustou nových malých kanálů pro každou přijatou platbu.

Pokud nebude dostatek příchozí likvidity, Phoenix zvětší velikost vašeho počátečního kanálu, ale to stále znamená poplatek na řetězci. Tento poplatek můžete stejně nastavit v nastavení Phoenixu, možnosti platby a poplatky.
Doporučujeme začít používat Phoenix s velkým kanálem, jako je 1-3-5M sats. Vaše poplatky za commit budou v porovnání s velikostí kanálu nepatrné a příliš vás neovlivní. Také místo placení 4-5krát (nebo kolikrát jen budete vkládat malé částky) minimálního poplatku 3000 sats za každý vklad, zaplatíte pouze jednou poplatek za otevření kanálu.
Pokud začnete z tohoto kanálu utrácet, neutraťte vše, protože Phoenix ho zavře.

Pokud v kanálu necháte nějaké sats a provedete další doplnění z jiné LN peněženky / zdroje vkladu, máme dvě situace k zvážení:
- s novou částkou vkladu větší než je kapacita vašeho kanálu, Phoenix přizpůsobí velikost kanálu a vy zaplatíte extra poplatek.
- s novou částkou vkladu menší než je kapacita vašeho kanálu, nebudou žádné poplatky.

Takže se snažte nastavit kapacitu vašeho počátečního kanálu podle vašich osobních potřeb pro utrácení. Utrácení a doplňování v rámci limitů kanálu již nezpůsobí žádné další poplatky a zkušenost s používáním této aplikace peněženky bude plynulá.

### Záloha
Na následující obrazovce budete informováni, že aplikace Phoenix vygeneruje frázi seed jako zálohu pro vaši peněženku. Později tyto seed slova MUSÍTE uložit na bezpečné místo!

![](assets/screenshot4.webp)

Následující obrazovka ukazuje, zda chcete vytvořit novou peněženku nebo obnovit předchozí peněženku z fráze seed.

![](assets/screenshot5.webp)

Jakmile je nová peněženka vytvořena, budete upozorněni, že byste měli provést zálohu fráze seed. Klikněte na tlačítko "Zálohovat peněženku".

![](assets/screenshot6.webp)

Budete upozorněni, že tyto slova z fráze seed jsou velmi důležitá a citlivá a měli byste je udržovat v soukromí.

![](assets/screenshot7.webp)

Tato seed slova MUSÍTE uložit na bezpečné místo, jako je správce hesel ([KeePass](https://keepass.info/) nebo [Bitwarden](https://bitwarden.com/)), přičemž databázi tohoto správce hesel uchovávejte na offline USB šifrovaném disku pro úplnou bezpečnost.

![](assets/screenshot8.webp)

### Přijímání plateb

Předtím, než začnete přijímat, prosím, přečtěte si předchozí kapitolu "Rychlý průvodce likviditou".

Takže nyní jste připraveni přijímat sats do vaší peněženky Phoenix!

![](assets/screenshot9.webp)

Pro přijetí platby v Phoenixu máte následující možnosti:
- použitím zobrazeného QR kódu, který představuje "prázdnou" Lightning fakturu
- úpravou Lightning faktury (viz tlačítko úprav pod QR kódem), kde můžete přidat částku sats, přidat komentář zobrazený plátci
- použitím / skenováním QR kódu LNURL-withdraw
- generováním on-chain Bitcoinové adresy z vaší peněženky Phoenix. Pamatujte, že tato platba bude "převedena" na nový Lightning kanál (pokud jste ještě žádný neotevřeli) nebo na změnu velikosti stávajícího Lightning kanálu.

![](assets/screenshot10.webp)

Obrazovka zobrazená pro úpravu nové Lightning faktury a generování nového QR kódu pro ni:

![](assets/screenshot11.webp)

Toto je obrazovka, kde můžete generovat on-chain BTC adresu a bude vás informováno, že platba na tuto adresu bude "převedena" na lightning likviditu a zahrne nějaké poplatky.

![](assets/screenshot12.webp)

Jakmile byla platba provedena, zobrazí se obrazovka s potvrzením, vše hotovo!

![](assets/screenshot13.webp)
Volitelně můžete ke každé přijaté platbě přidat osobní poznámku. Tyto poznámky nejsou uloženy nikde jinde, jsou uchovávány pouze ve vašem zařízení. Pokud obnovíte svou peněženku Phoenix, tyto poznámky nebudou obnoveny. Tato funkce je užitečná pro sledování vašich odeslaných a přijatých plateb.
![](assets/screenshot14.webp)

### Odesílání plateb

Odeslání plateb je poměrně jednoduchý proces, stačí kliknout na tlačítko na hlavní obrazovce "Odeslat"

![](assets/screenshot15.webp)

Budete vyzváni, abyste povolili aplikaci Phoenix přístup k fotoaparátu zařízení, aby bylo možné skenovat QR kódy.

![](assets/screenshot16.webp)

Na obrazovce platby máte 3 možnosti:
- naskenovat QR kód z faktury příjemce Lightning / LNURL
- ručně zadat (vložit), vstup Lightning Address nebo kód LNURL-pay
- načíst QR obrázek z lokálního disku

![](assets/screenshot17.webp)

Jak můžete vidět na této obrazovce, požadavek na platbu byl naskenován a detaily jsou již vyplněny. Stačí jen stisknout tlačítko "Zaplatit".

![](assets/screenshot18.webp)

Jakmile je platba odeslána a potvrzena, zobrazí se obrazovka s potvrzením s krátkými detaily platby, včetně zaplaceného poplatku. Pokud chcete vidět více detailů o platbě, klikněte na tlačítko "Detaily".

![](assets/screenshot19.webp)

Na obrazovce s detaily můžete vidět technické detaily platby, včetně: hash platby a požadavek, preimage, cílový uzel a dobu trvání. Někdy jsou tyto detaily užitečné pro sledování plateb, ladění nebo identifikaci konkrétní platby s příjemcem.

![](assets/screenshot20.webp)

### Nastavení

V menu Nastavení není moc co dělat, Phoenix jde cestou jednoduchosti. Ale jeden důležitý aspekt zde je menu pro správu platebních kanálů a poplatků, kde si můžete nastavit požadované úrovně poplatků. Mějte na paměti, že v prostředí s vysokými poplatky v mempoolu byste neměli používat velmi nízké poplatky, jinak vaše platby a otevírání kanálů budou narušeny a/nebo selžou.

Další možnosti v menu Nastavení:
- Zobrazení - pro přepnutí na různé barevné motivy
- Electrum server - pro kontrolu stavu serveru Electrum, ke kterému jste připojeni, nebo specifikovat jeden
- Tor - pokud chcete používat Phoenix za sítí Tor
- Nastavení přístupu aplikace - nastavit oprávnění pro Phoenix k určitým službám zařízení
- Fráze pro obnovu - pokud chcete zkontrolovat slova semínka a/nebo provést novou zálohu
- Seznam kanálů - zobrazit stav vašich Lightning kanálů a dostupnou likviditu (vstup/výstup)
- Logy - zobrazit logy pro ladění
- Zavřít všechny kanály - Nebezpečná možnost, která by měla být použita POUZE v případě, že chcete trvale ukončit provoz vašeho uzlu Phoenix a získat zpět prostředky na vaši onchain adresu. Tuto adresu lze později načíst pomocí peněženky Electrum s použitím vaší fráze pro obnovu Phoenix.

![](assets/screenshot21.webp)

### Reset

Pokud se ocitnete v situaci, kdy vaše aplikace Phoneix má problémy (nevykonává platby, nepřipojuje se k serverům Electrum, nemůže přijímat platby) nebo jednoduše chcete přesunout ji na jiné zařízení, MUSÍTE si být jisti dvěma aspekty:
- máte zálohu vaší fráze pro obnovu
- zastavte aplikaci ve vašem zařízení - přejděte na detaily aplikace a vynuťte zastavení služby
- odinstalujte ji ze starého zařízení, pokud ji chcete přesunout na nové
- NESPUŠTĚJTE stejnou peněženku Phoenix na více zařízeních!

![](assets/screenshot22.webp)

Jakmile ji znovu nainstalujete nebo nainstalujete na nová zařízení, klikněte na tlačítko "Obnovit" a postupujte podle pokynů

![](assets/screenshot23.webp)
Nemůžete použít jiný typ seedu, který byl generován z jiných peněženkových aplikací. [Zde naleznete více informací](https://walletsrecovery.org/) o dalších typech peněženek, jejich typech seedu a cestě derivace. Ne všechny jsou kompatibilní!
![](assets/screenshot24.webp)

Musíte zadat slova seedu, která jste předtím uložili, jedno po druhém, ve specifickém pořadí. Jakmile dokončíte zadávání 12 slov, klikněte na tlačítko "Importovat" a hotovo.

![](assets/screenshot25.webp)

Během několika okamžiků uvidíte zobrazený váš předchozí zůstatek. Také se vám zobrazí upozornění na zálohování vašeho seedu. Pokud jste to již udělali, můžete jít do menu a vybrat "Zálohu jsem uložil".

![](assets/screenshot26.webp)

Hotovo! Příjemné bleskové transakce!