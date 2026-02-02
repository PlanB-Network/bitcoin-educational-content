---
name: BitcoinVoucherBot P2P
description: Jak nakupovat a prodávat Bitcoin P2P pomocí BitcoinVoucherBot
---

![image](assets/cover.webp)



Stále slyšíme o BitcoinVoucherBot, bot Telegram vytvořený k nákupu Bitcoin bez [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) prostřednictvím bankovního převodu SEPA. Bohužel od listopadu 2025 již BitcoinVoucherBot ve své centralizované podobě není jako služba bez KYC k dispozici.



V této příručce se podíváme na to, jak funguje nová implementace, která umožňuje uživatelům nakupovat a prodávat Bitcoin přímo na novém tržišti P2P (Peer-To-Peer), tedy bez KYC. Aby vývojáři čelili novým omezením, která stále více ohrožují digitální svobodu a soukromí, vytvořili toto rozšíření, které uživatelům dává možnost nakupovat a prodávat Bitcoin s vysokou mírou anonymity prostřednictvím P2P (Peer-To-Peer). Pojďme se společně podívat, jak tento nový způsob výměny funguje.



Chcete-li službu využívat, musíte provést převody prostřednictvím služby Lightning Network. Ujistěte se tedy, že máte zařízení wallet, které tento protokol podporuje a umožňuje používat k přijímání a odesílání prostředků "LNURL" nebo "Lightning Address".



Mezi podporovanými peněženkami najdeme:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Údržba)
- [Wallet Z Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (opatrovnictví s výměnou za neopatrovnictví)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Nebo jakýkoli wallet, který má "Lightning Address" a generuje fakturu Bolt11. peněženky, které generate fakturu Bolt12, nejsou v současné době podporovány. Další informace naleznete v definici [Bolt](https://planb.academy/resources/glossary/bolt).



V tomto výukovém programu budeme vzhledem k jeho snadnému okamžitému použití používat Wallet of Satoshi.



**Upozornění**: Wallet of Satoshi je sice oblíbený mezi začátečníky, ale je opatrovnický, s omezenou kontrolou nad prostředky; používejte jej pouze přechodně, pro plnou suverenitu okamžitě přejděte na jiný než opatrovnický. Od října 2025 obsahuje celosvětově stabilní self-custodial režim na iOS/Android (aktualizujte aplikaci), s autonomními privátními klíči, přepínáním mezi režimy, vlastními Lightning adresami a zálohou 12 slov seed. Zůstává však prozatímním řešením do konsolidace, pro dlouhodobou správu dává přednost necustodialní vyspělosti wallet.



Velmi dobře! Nyní můžeme začít naši cestu, která vás krok za krokem provede vytvořením účtu, správou nákupních a prodejních shod a používáním vyhrazené oblasti.



## Wallet a zápis



Nejprve si stáhněte aplikaci Wallet of Satoshi, pokud ji ještě nemáte nainstalovanou ve svém smartphonu.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Pokud jste Wallet of Satoshi nikdy nepoužívali a chcete pochopit, jak funguje, doporučuji vám postupovat podle tohoto návodu, abyste jej mohli správně aktivovat a bezpečně zálohovat.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Nyní, když je váš wallet připraven, můžete začít posílat malé množství sats. Mějte na paměti, že pro dokončení registrace do platformy P2P (Peer-To-Peer) budete muset odeslat 1000 sats jako kontrolní opatření: to má vytvořit bariéru proti případným útokům typu phantom match (podvod) a zabránit tak registraci kohokoli bez spamového filtru.



![image](assets/it/02.webp)



Nyní můžeme otevřít platformu P2P (Peer-To-Peer) a pokračovat v zápisu. Přihlásit se můžete ze stolních počítačů nebo prohlížečů na chytrých telefonech, prostřednictvím Telegram BitcoinVoucherBot nebo prostřednictvím odkazů .onion, které poskytují ještě vyšší úroveň soukromí.



pokud se rozhodnete použít odkaz Tor .onion, doporučuji také "Tor Browser". Pokud ji ještě neznáte, můžete se o ní dozvědět více na tomto odkazu:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Nyní zvolte, jakým způsobem se chcete na platformu dostat.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Budete přesměrováni na hlavní stránku.



stiskněte tlačítko "Get Starter" a začněte ihned



![image](assets/it/03.webp)



Na další obrazovce je třeba zvolit a zadat heslo (pole A) a poté jej zopakovat (pole B). Doporučuji, abyste si toto heslo ihned uložili na záložní médium, které může být na zabezpečeném digitálním zařízení, například "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

nebo si heslo uložte na papírové médium (**pozor**: toto není dobré řešení, ale je v pořádku, pokud je zamýšleno jako dočasné řešení).



Zaškrtněte ověřovací políčko, ve kterém uvádíte, že nejste robot (políčko C). Upozornění Nepovolujte šifrování RSA, pokud přesně nevíte, co to je a jak funguje. V této fázi nemusíte dělat nic. Klepněte na tlačítko "Generate Avatar" ("Generovat avatar") (pole D).



![image](assets/it/04.webp)



Nyní musíte zaplatit 1000 sats za dokončení zápisu.



1. Začněte shora a nejprve si prohlédněte náhodně vygenerované a nesmírně důležité "ID Avatara" Pečlivě si ho uložte, stejně jako jsem vám poradil, abyste to udělali s heslem.


2. Poté musíte do níže uvedeného pole zadat svůj kód "Lightning Address". To vám umožní přijímat platby, pokud si zakoupíte Bitcoin, nebo získávat náhrady. Pokud používáte Wallet Z Satoshi, budete moci zkopírovat svůj Address kliknutím na tlačítko obdržet.


3. Zaškrtněte ověřovací políčko, ve kterém uvádíte, že nejste robot.


4. Zaplaťte 1000 sats a získejte přístup do vyhrazené oblasti. Pokud ji nemůžete zarámovat, klikněte na ni myší (na počítači) nebo na ni klepněte prstem (na chytrých telefonech Browser/Telegram), abyste si zkopírovali adresu, kterou musíte vložit do Wallet of Satoshi a dokončit platbu faktury.



![image](assets/it/05.webp)



Toto je váš LNURL Address.



![image](assets/it/06.webp)



Gratulujeme!!! Vytvořili jste si svůj Avatar natrvalo a zde si můžete prohlédnout jeho shrnutí. Ještě jednou doporučuji, abyste si pečlivě uložili jak Avatar, tak heslo, jak jsem již dříve navrhoval.



Klikněte na `Uložil jsem své pověření, pokračujte` (v překladu: "Uložil jsem své pověření, pokračujte")



![image](assets/it/07.webp)



Nyní se nacházíte v centru platformy, kde si můžete prohlédnout všechny obchodní shody s jejich podrobnostmi. Pro lepší přehlednost si níže prohlédněte obrázky, které k webu neodmyslitelně patří ze stolních počítačů.





- "Typ" ("Type") určuje, zda se jedná o prodej ("Sell") nebo nákup ("Buy")
- "Částka" ("Amount"): udává, kolik sats uživatel prodává, pokud je shoda typu "Prodej", nebo kolik Bitcoin je uživatel ochoten koupit, pokud je shoda typu "Nákup".
- "Cena BTC s marží" ("Cena BTC s marží"): zobrazuje cenu se zohledněním marže uplatněné nad označenou hodnotou.
- "Marže" ("Margin") je procento, které se použije k tržní ceně, Se znaménkem minus (-) získáte slevu z tržní ceny, Se znaménkem plus (+) se k tržní ceně použije prémie.
- "Metoda" ("Method") označuje, jakou metodu uživatel preferuje.
- "Creator" je jedinečný avatar, který uživatel na platformě používá.
- "Rep" (Reputace) Úroveň reputace uživatele se pohybuje od -5 nespolehlivý po +5 extrémně spolehlivý.
- "Status" ("Stav"): označuje stav shody. Na ukázkovém snímku obrazovky se všechny shody zobrazují jako "Open" ("Otevřené").
- "Expirace" ("Vypršení platnosti"): ukazuje, kolik času zbývá do vypršení platnosti zápasu a jeho zrušení, pokud si jej nikdo nevybral.



![image](assets/it/08.webp)



Vpravo nahoře klikněte na svůj avatar, čímž získáte přístup ke svému profilu.



![image](assets/it/09.webp)



Zde můžete vidět své jméno Avatar, ID uživatele, datum vytvoření a reputaci, která se pozitivně nebo negativně projeví na vašem chování při vyjednávání.



![image](assets/it/10.webp)



V části Nastavení si můžete zobrazit svůj "Lightning Address" zadaný při registraci a v případě potřeby jej změnit. Máte také možnost vytvořit veřejný klíč, který, jak již bylo zmíněno, byste měli nastavit pouze v případě, že máte odpovídající dovednosti. Slouží k šifrování zpráv, které si budete vyměňovat se svým protějškem přímo z počítače.



Důrazně doporučujeme funkci Telegram Notification. Po její aktivaci se zobrazí QR kód, který si můžete zarámovat pomocí aplikace Telegram. Tímto způsobem budete dostávat oznámení o všech akcích souvisejících s vašimi zápasy v reálném čase přímo v chatu bota na Telegram.



![image](assets/it/11.webp)



Nakonec najdete sekci s výdělky generovanými uživateli, které jste pozvali. Odtud můžete pomocí tlačítka sdílet svůj odkaz nebo QR kód a o kousek níže zobrazit seznam shod, kde můžete sledovat svou reputaci spolu s odpovídajícím skóre.



![image](assets/it/12.webp)



## Vytvořit objednávku na nákup Bitcoin



Vstup do Marketplace: na hlavním navigačním panelu klikněte na symbol košíku "Marketplace" ("Tržiště"), čímž otevřete knihu objednávek. poté spusťte novou objednávku: stiskněte tlačítko "Nová objednávka" ("Nová objednávka"), čímž zahájíte proces.



![image](assets/it/13.webp)





- Nastavte podrobnosti objednávky:
- Vyberte možnost "Buy Bitcoin" ("Koupit Bitcoin").
- Zadejte požadované množství sats.
- Definujte cenové rozpětí (v rozmezí -20 % až +20 % od tržní hodnoty).
- Zvolte způsob platby (okamžitá SEPA atd.).
- Označuje preferovanou měnu.
- Potvrzení objednávky: kliknutím na "Create Order" ("Potvrdit objednávku") přejdete do fáze podání.



![image](assets/it/14.webp)



Požadovaná záloha: pro aktivaci objednávky je nutné složit zálohu ve výši 10 % z celkové částky a poplatek za služby.




- Platba zálohy: při vytvoření objednávky systém automaticky vygeneruje bleskovou fakturu. Záloha je pouze dočasná a je vrácena po dokončení objednávky.
- Hlavní funkce:
- Záloha: 10 % hodnoty objednávky.
- Poplatek za službu: náklady na používání platformy.
- Časový limit: Na provedení platby máte 5 minut, jinak transakce vyprší.



![image](assets/it/15.webp)



Po úspěšné platbě se objednávka objeví v knize a bude viditelná pro všechny uživatele, kteří si ji mohou vybrat a přijmout. Pro vytvoření prodejního příkazu stačí kliknout na "Sell Bitcoin" ("Prodej Bitcoin"), zadat množství satoshi, které chcete prodat, nastavit marži, zvolit způsob platby a měnu a poté pokračovat 10% zálohou jako jistotou. Po dokončení bude vaše shoda viditelná v seznamu.



![image](assets/it/16.webp)



## Jak přijmout objednávku



1. Prodejci mohou v knize vidět seznam všech dostupných objednávek.


2. Zkontrolujte podrobnosti: u každé objednávky jsou uvedeny tyto informace:




  - Množství Bitcoin,
  - Cenová marže,
  - Způsob platby,
  - Pověst uživatele.



![image](assets/it/17.webp)



3. Kliknutím na objednávku otevřete celý list se všemi informacemi.


4. Stisknutím tlačítka "Sell Bitcoin" ("Prodej Bitcoin") návrh přijmete.



![image](assets/it/18.webp)



## Záloha požadovaná prodávajícím



Po přijetí objednávky systém vygeneruje fakturu k úhradě. Záloha zahrnuje:



- Celková částka objednávky,



- služební komise.



Platba zálohy musí být provedena ve stanovené lhůtě, jinak nebude transakce potvrzena.



![image](assets/it/19.webp)



## Zasílání platebních pokynů



Po provedení vkladu se transakce zobrazí na osobním panelu prodávajícího, který musí poskytnout údaje kupujícímu, aby mohl dokončit platbu ve fiat měně.



1. Prodávající zobrazí aktivní transakci na svém panelu.


2. Klikněte na "Odeslat pokyny k platbě"


3. Zadejte všechny potřebné údaje pro fiat platbu (IBAN, příjemce, adresu, důvod platby atd.).


4. Kliknutím na "Send Message" ("Odeslat zprávu") odešlete údaje kupujícímu.



![image](assets/it/20.webp)



## Postup platby



Kupující obdrží v chatu platformy zprávu se všemi údaji potřebnými k provedení platby ve fiat měně:




- Bankovní údaje: IBAN se jménem a adresou majitele účtu prodávajícího.
- Přesná částka: přesná částka ve fiat, která má být převedena.
- Příčinná souvislost/popis: text, který se uvede v transakci.
- Lhůta: lhůta, do které je třeba platbu provést.



Převod probíhá mimo systém P2P a musí být proveden prostřednictvím bankovní instituce.



⚠️ **Důležité upozornění:** potvrzení na platformě by mělo být provedeno až poté, co jste skutečně zařídili převod nebo platbu fiatem prostřednictvím své banky.



![image](assets/it/21.webp)



## Potvrzení platby fiat



Tento krok je pro kupujícího zásadní a měl by být proveden až po ověření, že platba byla skutečně odeslána.



1. Přijaté údaje: kupující obdržel od prodávajícího pokyny k platbě.


2. Provedení platby: fiat převod se provádí z bankovního účtu.


3. Ověření: kontrola správného provedení operace.


4. Potvrzení na platformě: klikněte na "Confirm fiat payment" ("Potvrdit platbu fiat") na stránce obchodu.


Tlačítko "Potvrdit platbu fiat" se zobrazí v sekci transakce a mělo by být použito až po ověření, že platba byla skutečně odeslána.



![image](assets/it/22.webp)



Posledním krokem v tomto procesu je potvrzení přijetí platby ve formě fiatů ze strany prodávajícího, po kterém jsou saty uvolněny kupujícímu.



![image](assets/it/23.webp)



## Závěr



Doufáme, že vám tento návod pomůže využít novou metodu obchodování s bitcoiny nebo je dokonce jen koupit, ať už pro vlastní úložiště hodnoty, nebo pro zahájení každodenních plateb. Stále však zůstávají dveře, které je třeba prozkoumat, abychom se vyrovnali s tím, co se v našem digitálním světě chystá.



Smyčka spuštěná orgány, které nás ovládají, se utahuje, aby dala vzniknout stále více kontrolovanému internetu. Zakoupením P2P zachováte své nákupy v naprosté anonymitě, nezanecháte žádné stopy a žádné následné důsledky ze strany třetích stran.