---
name: Trezor Model One
description: Nastavení a používání modelu Hardware Wallet One
---
![cover](assets/cover.webp)



*Image credit: [Trezor.io](https://trezor.io/)*



Trezor Model One je vůbec prvním modelem Hardware Wallet, který společnost SatoshiLabs uvedla na trh v roce 2014. I po více než deseti letech své existence zůstává zajímavou volbou, zejména pro uživatele, kteří hledají technicky i rozpočtově dostupný model Hardware Wallet. Na oficiálních stránkách Trezoru se totiž prodává za 49 eur. Je to jedna z mála hardwarových peněženek v této cenové relaci. Leží uprostřed mezi zařízeními základní úrovně za přibližně 20 EUR, jako je Tapsigner, které často postrádají obrazovku, a zařízeními střední třídy za přibližně 80 EUR, jako je Ledger Nano S Plus nebo Trezor Safe 3.



Model One má 0,96palcový monochromatický displej OLED a dvě fyzická tlačítka. Funguje bez baterie, k napájení a přenosu dat využívá pouze připojení micro-USB Exchange.



![Image](assets/fr/01.webp)



Hlavní nevýhodou modelu One je absence zabezpečovacího prvku, což jej činí zranitelným vůči různým fyzickým útokům, z nichž některé je poměrně snadné provést. Tyto útoky mohou zahrnovat analýzu pomocných kanálů za účelem zjištění kódu PIN zařízení nebo pokročilejší techniky k získání zašifrovaného kódu seed za účelem jeho pozdějšího vylákání hrubou silou. Všimněte si, že tyto útoky vyžadují fyzický přístup k zařízení. Tuto zranitelnost však lze značně omezit použitím pevného BIPu passphrase39. Pokud se rozhodnete pro tento Hardware Wallet, důrazně vám doporučuji nakonfigurovat passphrase.



Model One nabízí dvě důležité výhody:




- Je založen na zcela otevřené architektuře. Na rozdíl od novějších modelů se Secure Element jsou všechny hardwarové a softwarové komponenty modelu One auditovatelné;
- Je vybaven obrazovkou. Pokud vím, je to jediný Hardware Wallet na trhu v této cenové kategorii s displejem. To je velmi důležitá vlastnost, protože umožňuje ověřit podepsané informace a adresy příjmu, a tím zabránit mnoha digitálním útokům.



Trezor Model One proto může představovat rozumnou volbu pro začátečníky a středně pokročilé uživatele s omezeným rozpočtem. Je však důležité mít na paměti jeho omezení, pokud jde o fyzickou ochranu, a to kvůli absenci prvku Secure Element. Pokud je váš rozpočet omezený, jedná se o dobrou volbu, ale pokud si můžete dovolit zvolit lepší model, například Trezor Safe 3 za 79 EUR, je vhodnější, protože obsahuje Secure Element.



## Vybalení modelu Trezor One



Po obdržení modelu One se ujistěte, že krabice a Seal jsou neporušené, abyste potvrdili, že balíček nebyl otevřen. Při pozdějším nastavování zařízení bude rovněž provedeno softwarové ověření jeho pravosti a neporušenosti.



Obsah krabice zahrnuje :




- Trezor Model One;
- Karton k zaznamenání věty Mnemonic, samolepky a pokyny;
- Kabel USB-A na micro-USB.



![Image](assets/fr/02.webp)



Navigace v zařízení je velmi jednoduchá:




- Kliknutím pravým tlačítkem myši potvrďte a přejděte k dalším krokům;
- Pro návrat zpět použijte levé tlačítko.



## Předpoklady



V tomto návodu vám ukážu, jak používat Trezor Model One se softwarem [Sparrow Wallet pro správu portfolia](https://sparrowwallet.com/download/). Pokud jste si tento software ještě nenainstalovali, učiňte tak nyní. Pokud potřebujete pomoc, máme také podrobný návod na konfiguraci softwaru Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Ke konfiguraci modelu One, kontrole jeho pravosti a instalaci firmwaru budete potřebovat také software Trezor Suite. Tento software budeme používat pouze k tomuto účelu a poté bude potřeba pouze pro aktualizace firmwaru. Pro každodenní správu Wallet budeme používat výhradně Sparrow Wallet, protože je optimalizovaný pro Bitcoin a snadno se používá i pro začátečníky (Sparrow podporuje pouze Bitcoin, nikoli altcoiny).



[Stáhnout Trezor Suite z oficiálních stránek](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



U obou těchto programů důrazně doporučuji, abyste před instalací do počítače ověřili jejich pravost (pomocí GnuPG) i integritu (pomocí Hash). Pokud nevíte, jak to udělat, můžete postupovat podle tohoto dalšího návodu :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Spuštění modelu Trezor One



Připojte model One k počítači, kde jsou již nainstalovány aplikace Trezor Suite a Sparrow Wallet.



![Image](assets/fr/04.webp)



Otevřete sadu Trezor Suite a klikněte na "*Nastavení mého Trezoru*".



![Image](assets/fr/05.webp)



Vyberte možnost "*Bitcoin-only firmware*" a klikněte na "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Aplikace Trezor Suite poté nainstaluje firmware do vašeho modelu One. Během instalace vyčkejte.



![Image](assets/fr/07.webp)



Klikněte na "*Pokračovat*".



![Image](assets/fr/08.webp)



## Vytvoření portfolia Bitcoin



V aplikaci Trezor Suite klikněte na tlačítko "*Vytvořit nový Wallet*".



![Image](assets/fr/09.webp)



Přijměte podmínky používání na webu Hardware Wallet.



![Image](assets/fr/10.webp)



V aplikaci Trezor Suite klikněte na "*Pokračovat v zálohování*".



![Image](assets/fr/11.webp)



Software poskytuje pokyny ke správě fráze Mnemonic.



Tato služba Mnemonic vám poskytuje plný a neomezený přístup ke všem vašim bitcoinům. Kdokoli, kdo má tuto frázi, může vaše prostředky ukrást, a to i bez fyzického přístupu k vašemu Trezoru Model One.



Fráze o 24 slovech obnoví přístup k vašim bitcoinům v případě ztráty, krádeže nebo rozbití vašeho Hardware Wallet. Je proto velmi důležité ji pečlivě uložit a uschovat na bezpečném místě.



Můžete jej napsat na karton dodávaný v krabici, nebo pro větší bezpečnost doporučuji vyrýt jej na podstavec z nerezové oceli, který jej ochrání před požárem, povodní nebo zřícením.



Potvrďte pokyny a klikněte na tlačítko "*Vytvořit zálohu Wallet*".



![Image](assets/fr/12.webp)



Model One vytvoří frázi Mnemonic pomocí generátoru náhodných čísel. Ujistěte se, že vás během této operace nikdo nesleduje. Zapište slova uvedená na obrazovce na vámi zvolené fyzické médium. V závislosti na vaší bezpečnostní strategii můžete zvážit vytvoření několika úplných fyzických kopií fráze (především ji však nedělte). Je důležité, aby byla slova očíslována a seřazena za sebou.



***Samozřejmě nesmíte tato slova nikdy sdílet na internetu, jak to dělám v tomto návodu. Tento příklad Wallet bude použit pouze na Testnet a na konci tutoriálu bude odstraněn



Pro více informací o správném způsobu ukládání a správy fráze Mnemonic vřele doporučuji tento další návod, zejména pokud jste začátečníci:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Chcete-li přejít na další slova, klikněte pravým tlačítkem myši. Po zapsání všech slov přejdete na další krok opět kliknutím pravým tlačítkem myši.



![Image](assets/fr/13.webp)



Váš Hardware Wallet opět ukazuje všechna vaše slova. Zkontrolujte, zda jste je všechna zapsali.



![Image](assets/fr/14.webp)



## Nastavení kódu PIN



Poté následuje krok zadání kódu PIN. Kód PIN odemkne zařízení Trezor. Poskytuje tedy ochranu před neoprávněným fyzickým přístupem. Tento kód PIN se nepodílí na odvození kryptografických klíčů vašeho zařízení Wallet. Takže i bez přístupu ke kódu PIN vám vlastnictví vaší 12slovné fráze Mnemonic umožní získat zpět přístup k vašim bitcoinům.



V aplikaci Trezor Suite klikněte na tlačítko "*Pokračovat v zadávání kódu PIN*" a poté na tlačítko "*Zadat kód PIN*".



![Image](assets/fr/15.webp)



Potvrďte u modelu One.



![Image](assets/fr/16.webp)



Doporučujeme zvolit co nejnáhodnější kód PIN. Nezapomeňte tento kód uložit na jiné místo, než kde je uložen váš Trezor (např. do správce hesel). Kód PIN můžete definovat v rozsahu 8 až 50 číslic. Pro zvýšení bezpečnosti doporučuji zvolit co nejdelší kód PIN.



Kód PIN je třeba zadat v aplikaci Trezor Suite v počítači kliknutím na tečky odpovídající číslicím podle konfigurace klávesnice zobrazené na zařízení Trezor Model One.



Tento specifický způsob zadání kódu PIN je vyžadován při každém odemknutí zařízení Trezor Model One, ať už prostřednictvím sady Trezor Suite nebo Sparrow Wallet.



![Image](assets/fr/17.webp)



Po dokončení klikněte na tlačítko "*Zadat PIN*".



![Image](assets/fr/18.webp)



Pro potvrzení znovu napište PIN.



![Image](assets/fr/19.webp)



V aplikaci Trezor Suite klikněte na tlačítko "*Dokončit nastavení*".



![Image](assets/fr/20.webp)



Konfigurace modelu One je nyní dokončena. Pokud chcete, můžete změnit název a domovskou stránku Hardware Wallet.



![Image](assets/fr/21.webp)



Software Trezor Suite již nebudeme potřebovat, s výjimkou pravidelných aktualizací firmwaru Hardware Wallet nebo pokud chcete provést test obnovení. Ke správě portfolia nyní budeme používat software Sparrow, protože tento software se dokonale hodí pouze pro použití s Bitcoin.



## Nastavení portfolia v aplikaci Sparrow Wallet



Začněte stažením a instalací aplikace Sparrow Wallet [z oficiálních stránek](https://sparrowwallet.com/) do počítače, pokud jste tak ještě neučinili.



Po otevření programu Sparrow Wallet se ujistěte, že je software připojen k uzlu Bitcoin, který je označen zaškrtnutím v pravém dolním rohu Interface. Pokud máte s připojením Sparrow potíže, doporučuji nahlédnout do začátku tohoto návodu:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klikněte na kartu "*Soubor*" a poté na "*Nový Wallet*".



![Image](assets/fr/22.webp)



Pojmenujte své portfolio a klikněte na "*Vytvořit Wallet*".



![Image](assets/fr/23.webp)



V rozevírací nabídce "*Typ skriptu*" vyberte typ skriptu, který bude použit k zabezpečení vašich bitcoinů. Doporučuji "*Taproot*", případně "*Nativní SegWit*".



![Image](assets/fr/24.webp)



Klikněte na tlačítko "*Připojený Hardware Wallet*". Model One musí být samozřejmě připojen k počítači.



![Image](assets/fr/25.webp)



Klikněte na tlačítko "*Scan*". Měl by se zobrazit váš model One.



Po připojení modelu One k počítači s otevřenou aplikací Sparrow Wallet budete vyzváni k zadání kódu passphrase BIP39 do aplikace Sparrow. Této pokročilé možnosti se budeme věnovat v některém z příštích tutoriálů. Prozatím můžete jednoduše zvolit možnost "*Přepnout passphrase vypnuto*", abyste zabránili tomu, aby vás Trezor při každém spuštění vyzval k zadání passphrase.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Klikněte na "*Importovat úložiště klíčů*".



![Image](assets/fr/27.webp)



Nyní můžete zobrazit podrobnosti o svém účtu Wallet, včetně rozšířeného veřejného klíče prvního účtu. Kliknutím na tlačítko "*Použít*" dokončete vytvoření účtu Wallet.



![Image](assets/fr/28.webp)



Pro zabezpečení přístupu ke službě Sparrow Wallet zvolte silné heslo. Toto heslo zajistí bezpečný přístup k datům Sparrow Wallet a ochrání vaše veřejné klíče, adresy, štítky a historii transakcí před neoprávněným přístupem.



Doporučuji vám uložit toto heslo do správce hesel, abyste ho nezapomněli.



![Image](assets/fr/29.webp)



A nyní je vaše portfolio importováno do aplikace Sparrow Wallet!



![Image](assets/fr/30.webp)



Než obdržíte své první bitcoiny do Wallet, **důrazně vám doporučuji provést test obnovy prázdného účtu**. Zapište si nějaké referenční informace, například svůj xpub, a poté resetujte svůj Trezor Model One, zatímco je Wallet stále prázdný. Poté se pokuste obnovit Wallet na Trezoru pomocí papírových záloh. Zkontrolujte, zda se xpub vygenerovaný po obnovení shoduje s tím, který jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé.



Chcete-li se dozvědět více o tom, jak provést test obnovení, doporučuji vám prostudovat tento další návod:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Jak přijímat bitcoiny pomocí zařízení Trezor Model One?



V aplikaci Sparrow klikněte na kartu "*Příjem*".



![Image](assets/fr/31.webp)



Než začnete používat Address navržený společností Sparrow Wallet, zkontrolujte jej na obrazovce zařízení Trezor. Tento postup vám umožní potvrdit, že Address zobrazený na Sparrow není podvodný a že Hardware Wallet skutečně obsahuje soukromý klíč potřebný k následnému utrácení bitcoinů zajištěných tímto Address. Tímto způsobem se můžete vyhnout několika typům útoků.



Tuto kontrolu provedete kliknutím na tlačítko "*Zobrazit Address*".



![Image](assets/fr/32.webp)



Zkontrolujte, zda se číslo Address zobrazené na vašem zařízení Trezor shoduje s číslem Wallet na zařízení Sparrow. Tuto kontrolu je vhodné provést také těsně před sdělením Address odesílateli, abyste si byli jisti jeho platností. Potvrzení můžete provést stisknutím pravého tlačítka.



![Image](assets/fr/33.webp)



Můžete také přidat "*Label*" a popsat zdroj bitcoinů, které budou tímto Address zabezpečeny. Jedná se o dobrý postup, který vám umožní lépe spravovat UTXO.



![Image](assets/fr/34.webp)



Pomocí tohoto účtu Address pak můžete přijímat bitcoiny.



![Image](assets/fr/35.webp)



## Jak posílat bitcoiny pomocí zařízení Trezor Model One?



Nyní, když jste obdrželi své první Satsy ve svém modelu Wallet, můžete je také utratit! Připojte Trezor k počítači, spusťte Sparrow Wallet a přejděte na kartu "*Odeslat*", kde vytvoříte novou transakci.



![Image](assets/fr/36.webp)



Pokud chcete *Kontrolu mincí*, tj. vybrat konkrétně, které UTXO se mají v transakci spotřebovat, přejděte na kartu "*UTXO*". Vyberte UTXO, které si přejete utratit, a poté klikněte na tlačítko "*Odeslat vybrané*". Budete přesměrováni na stejnou obrazovku v záložce "*Odeslat*", ale s již vybranými UTXO pro transakci.



![Image](assets/fr/37.webp)



Zadejte cíl Address. Kliknutím na tlačítko "*+ Add*" můžete zadat i více adres.



![Image](assets/fr/38.webp)



Napište si "*název*", abyste si zapamatovali účel tohoto výdaje.



![Image](assets/fr/39.webp)



Vyberte částku, která má být odeslána na tento účet Address.



![Image](assets/fr/40.webp)



Upravte sazbu poplatků za transakci podle aktuálního trhu. Pro výběr vhodné sazby poplatku můžete například použít [Mempool.space](https://Mempool.space/).



Ujistěte se, že jsou všechny parametry transakce správné, a klikněte na tlačítko "*Vytvořit transakci*".



![Image](assets/fr/41.webp)



Pokud vám vše vyhovuje, klikněte na "*Finalizovat transakci pro podpis*".



![Image](assets/fr/42.webp)



Klikněte na "*Podepsat*".



![Image](assets/fr/43.webp)



Klikněte na "*Podepsat*" vedle svého modelu Trezor One.



![Image](assets/fr/44.webp)



Zkontrolujte parametry transakce na obrazovce Hardware Wallet, včetně přijímajícího Address příjemce, odeslané částky a poplatku. Po ověření transakce na Trezoru ji podepište kliknutím pravým tlačítkem myši.



![Image](assets/fr/45.webp)



Vaše transakce je nyní podepsána. Naposledy zkontrolujte, zda je vše v pořádku, a kliknutím na "*Broadcast Transaction*" ji odvysílejte v síti Bitcoin.



![Image](assets/fr/46.webp)



Najdete ji na kartě "*Transakce*" v aplikaci Sparrow Wallet.



![Image](assets/fr/47.webp)



Blahopřejeme, nyní jste se seznámili se základním používáním Trezoru Model One se Sparrow Wallet! Chcete-li se posunout o krok dál, doporučuji vám tento komplexní návod na používání Trezoru Hardware Wallet s BIP39 passphrase, který posílí vaši bezpečnost :



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Pokud pro vás byl tento návod užitečný, budu vám vděčný, když níže zanecháte palec Green. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji vám mnohokrát!