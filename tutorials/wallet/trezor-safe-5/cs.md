---
name: Trezor Safe 5
description: Konfigurace a používání modulu Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Image credit: [Trezor.io](https://trezor.io/)*



Trezor Safe 5 je nejnovější generace Hardware Wallet navržená společností SatoshiLabs a uvedená na trh v roce 2024. Je umístěn jako špičková verze modelu Safe 3 se zaměřením na ergonomii a odolnost. Využívá stejných bezpečnostních pokroků jako jeho předchůdce Safe 3, ve srovnání s modely One a T.



Za cenu 169 EUR se Safe 5 řadí do kategorie high-end Hardware Wallet a konkuruje modelům jako Coldcard, Ledger Nano X a Flex, Jade Plus, Passport a Bitbox.



Trezor 5 se vyznačuje 1,54palcovým barevným dotykovým displejem chráněným sklem *Gorilla Glass 3*, které je odolné proti nárazům a poškrábání. Je také vybaven haptickým motorem *Trezor Touch*, který při dotyku vydává drobné vibrace. Stejně jako Safe 3 obsahuje Secure Element a funguje prostřednictvím připojení USB-C, navíc s portem Micro SD.



Hlavní rozdíl mezi zařízením Safe 3 a Safe 5 spočívá kromě bezpečnostních aspektů v kvalitě zařízení. Výrazně se zlepšuje uživatelský zážitek díky plynulejšímu ovládání a pohodlnějšímu displeji. Z hlediska bezpečnosti je rovnocenný.



![Image](assets/fr/01.webp)



Safe 5 má všechny základní funkce, které očekáváte od dobrého Hardware Wallet, včetně vynikající integrace passphrase BIP39. Zatím však nepodporuje Miniscript.



Tento model je vhodný zejména pro začátečníky a středně pokročilé uživatele. Na druhou stranu nemusí splnit všechna očekávání pokročilých uživatelů, kteří hledají specifičtější funkce dostupné v zařízeních, jako je Coldcard. Nicméně pokud tyto pokročilé možnosti nepotřebujete, může být Trezor Safe 5 vynikající volbou.



## Bezpečnostní model Trezor Safe 5



Stejně jako Trezor Safe 3 je i Trezor Safe 5 vybaven **bezpečným prvkem** s certifikací EAL6+, což je výrazný pokrok oproti dřívějším modelům, jako je Model One a Model T. Jedná se o čip OPTIGA Trust M V3, který neukládá přímo kód seed, ale funguje jako kryptografický prvek pro zabezpečení přístupu k němu. Zabezpečený prvek uchovává tajemství, k němuž lze získat přístup pouze po správném zadání kódu PIN uživatelem. Toto tajemství se pak používá k dešifrování kódu seed, který je uložen zašifrovaný v hlavní paměti zařízení.



Tento hybridní bezpečnostní systém nabízí lepší fyzickou ochranu, zejména proti útokům extrakcí nebo invazivní analýze, což jsou problémy, na které byl model One náchylný, zejména při správě PIN. Tyto zranitelnosti jsou nyní obejity díky použití zabezpečeného prvku. Tento model také zachovává architekturu softwaru s otevřeným zdrojovým kódem: kód, který řídí generování a používání soukromých klíčů, zůstává plně přístupný a ověřitelný. Čip OPTIGA spravuje pouze kód PIN, což je prvek externí vůči správě klíčů Bitcoin Wallet. Omezuje se na uvolnění tajemství, které lze použít k dešifrování kódu seed. Čip OPTIGA Trust M V3 také těží z relativně volné licence, která opravňuje společnost SatoshiLabs k volnému zveřejňování potenciálních zranitelností (NDA-Free).



Tento model zabezpečení představuje podle mého názoru jeden z nejlepších kompromisů, které jsou dnes na trhu k dispozici. Kombinuje výhody zabezpečeného prvku se správou softwaru s otevřeným zdrojovým kódem. Dříve museli uživatelé volit mezi zvýšeným fyzickým zabezpečením pomocí čipu a transparentností pomocí otevřeného zdrojového kódu; s Trezor Safe je možné využívat výhod obojího.



V tomto návodu se dozvíte, jak bezpečně nakonfigurovat a používat zařízení Trezor Safe 5.



## Vybalení zařízení Trezor Safe 5



Po obdržení zařízení Safe 5 se ujistěte, že krabice a Seal jsou neporušené, abyste potvrdili, že balení nebylo otevřeno. Při pozdějším nastavování bude provedena také softwarová kontrola pravosti a neporušenosti zařízení.



Obsah krabice zahrnuje :




- Trezor Safe 5;
- Sáček obsahující karton k nahrání věty Mnemonic, samolepky a pokyny;
- Kabel USB-C na USB-C.



Trezor Safe 5 by měl být po otevření chráněn ochranným plastem a port USB-C by měl být zajištěn holografickým štítkem Seal. Ujistěte se, že tam je.



![Image](assets/fr/02.webp)



Navigace v zařízení je poměrně intuitivní:




- Chcete-li se posunout vpřed, dotkněte se spodní poloviny obrazovky;
- Posunutím dolů se vrátíte zpět ;
- Operaci potvrdíte stisknutím a podržením obrazovky.



## Předpoklady



V tomto návodu vám ukážu, jak používat Trezor Safe 5 se softwarem [Sparrow Wallet pro správu portfolia](https://sparrowwallet.com/download/). Pokud jste si tento software ještě nenainstalovali, učiňte tak nyní. Pokud potřebujete pomoc, máme také podrobný návod na konfiguraci Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Ke konfiguraci zařízení Safe 5, kontrole jeho pravosti a instalaci firmwaru budete potřebovat také software Trezor Suite. Tento software budeme používat pouze k tomuto účelu a poté bude potřeba pouze pro aktualizace firmwaru. Pro každodenní správu Wallet budeme používat výhradně Sparrow Wallet, protože je optimalizovaný pro Bitcoin a snadno se používá i pro začátečníky (Sparrow podporuje pouze Bitcoin, nikoli altcoiny).



[Stáhnout Trezor Suite z oficiálních stránek](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



U obou těchto programů důrazně doporučuji, abyste před instalací do počítače ověřili jejich pravost (pomocí GnuPG) i integritu (pomocí Hash). Pokud nevíte, jak to udělat, můžete postupovat podle tohoto dalšího návodu :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Spuštění systému Trezor Safe 5



Připojte zařízení Safe 5 k počítači, ve kterém jsou již nainstalovány aplikace Trezor Suite a Sparrow Wallet.



![Image](assets/fr/04.webp)



Otevřete sadu Trezor Suite a klikněte na "*Nastavení mého Trezoru*".



![Image](assets/fr/05.webp)



Vyberte možnost "*Bitcoin-only firmware*" a klikněte na "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite poté nainstaluje firmware do zařízení Safe 5. Během instalace vyčkejte.



![Image](assets/fr/07.webp)



Klikněte na "*Pokračovat*".



![Image](assets/fr/08.webp)



Poté přejděte k testu pravosti, abyste se ujistili, že váš Hardware Wallet není falešný nebo kompromitovaný.



![Image](assets/fr/09.webp)



Na zařízení Safe 5 stiskněte obrazovku a potvrďte.



![Image](assets/fr/10.webp)



Pokud je váš Trezor pravý, zobrazí se v aplikaci Trezor Suite potvrzovací zpráva.



![Image](assets/fr/11.webp)



Poté můžete přeskočit okna se základními pokyny k obsluze.



![Image](assets/fr/12.webp)



## Vytvoření portfolia Bitcoin



V aplikaci Trezor Suite klikněte na tlačítko "*Vytvořit nový Wallet*".



![Image](assets/fr/13.webp)



Chcete-li vytvořit standardní frázi Wallet BIP39, začněte výběrem možnosti "*Typy zálohování Wallet*" z rozevírací nabídky a poté vyberte mezi frází Mnemonic o 12 nebo 24 slovech (v současné době se doporučuje 12 slov). To vám umožní vytvořit klasické portfolio s jedním podpisem. Doporučuji vám, abyste se zde rozhodli pro parametry vyhovující BIP39, abyste usnadnili vyhledávání a vyhnuli se omezení na konkrétní prostředí. Pro dokončení klikněte na "*Vytvořit Wallet*".



Pokud se chcete dozvědět více o dalších možnostech zálohování, které jsou k dispozici v nástroji Trezor, včetně *Zálohování více sdílení*, doporučuji vám přečíst si také tento návod :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Přijměte podmínky používání na webu Hardware Wallet.



![Image](assets/fr/15.webp)



Stisknutím a podržením obrazovky vytvoříte nové portfolio.



![Image](assets/fr/16.webp)



V aplikaci Trezor Suite klikněte na "*Pokračovat v zálohování*".



![Image](assets/fr/17.webp)



Software poskytuje pokyny ke správě fráze Mnemonic.



Tato služba Mnemonic vám poskytuje plný a neomezený přístup ke všem vašim bitcoinům. Kdokoli, kdo má tuto frázi, může vaše prostředky ukrást, a to i bez fyzického přístupu k trezoru Trezor 5.



Fráze o 12 slovech obnoví přístup k vašim bitcoinům v případě ztráty, krádeže nebo rozbití vašeho Hardware Wallet. Je proto velmi důležité ji pečlivě uložit a uschovat na bezpečném místě.



Můžete jej napsat na karton dodávaný v krabici, nebo pro větší bezpečnost doporučuji vyrýt jej na podstavec z nerezové oceli, který jej ochrání před požárem, povodní nebo zřícením.



Potvrďte pokyny a klikněte na tlačítko "*Vytvořit zálohu Wallet*".



![Image](assets/fr/18.webp)



Aplikace Safe 5 vytvoří frázi Mnemonic pomocí generátoru náhodných čísel. Ujistěte se, že vás během této operace nikdo nesleduje. Zapište slova uvedená na obrazovce na vámi zvolené fyzické médium. V závislosti na vaší bezpečnostní strategii můžete zvážit vytvoření několika úplných fyzických kopií fráze (především ji však nedělte). Je důležité, aby byla slova očíslována a seřazena za sebou.



***Samozřejmě nesmíte tato slova nikdy sdílet na internetu, jak to dělám v tomto návodu. Tento příklad Wallet bude použit pouze na Testnet a na konci tutoriálu bude odstraněn



Pro více informací o správném způsobu ukládání a správy fráze Mnemonic vřele doporučuji tento další návod, zejména pokud jste začátečníci:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Chcete-li přejít na další slova, klikněte na spodní část obrazovky. Posunutím dolů se můžete vrátit zpět. Jakmile zapíšete všechna slova, podržte prst na obrazovce a přejděte k dalšímu kroku.



![Image](assets/fr/20.webp)



Vyberte slova ve větě Mnemonic podle jejich pořadí, abyste si ověřili, že jste je zapsali správně.



![Image](assets/fr/21.webp)



Po dokončení tohoto ověřovacího postupu pokračujte kliknutím na obrazovku.



![Image](assets/fr/22.webp)



## Nastavení kódu PIN



Poté následuje krok zadání kódu PIN. Kód PIN odemkne zařízení Trezor. Poskytuje tedy ochranu před neoprávněným fyzickým přístupem. Tento kód PIN se nepodílí na odvození kryptografických klíčů vašeho zařízení Wallet. Takže i bez přístupu ke kódu PIN vám vlastnictví vaší 12slovné fráze Mnemonic umožní znovu získat přístup k vašim bitcoinům.



V aplikaci Trezor Suite klikněte na tlačítko "*Pokračovat v zadávání kódu PIN*" a poté na tlačítko "*Zadat kód PIN*".



![Image](assets/fr/23.webp)



Potvrďte pomocí Safe 5.



![Image](assets/fr/24.webp)



Doporučujeme zvolit co nejnáhodnější kód PIN. Nezapomeňte tento kód uložit na jiné místo, než kde je uložen váš Trezor (např. do správce hesel). Kód PIN můžete definovat v rozsahu 8 až 50 číslic. Pro zvýšení bezpečnosti doporučuji zvolit co nejdelší kód PIN.



Pomocí dotykového panelu zadejte kód PIN.



![Image](assets/fr/25.webp)



Po dokončení klikněte vpravo dole na zaškrtávátko Green a podruhé potvrďte PIN.



![Image](assets/fr/26.webp)



Váš kód PIN byl zaregistrován.



![Image](assets/fr/27.webp)



V aplikaci Trezor Suite klikněte na tlačítko "*Dokončit nastavení*".



![Image](assets/fr/28.webp)



Konfigurace zařízení Safe 5 je nyní dokončena. Pokud chcete, můžete změnit název a domovskou stránku Hardware Wallet.



![Image](assets/fr/29.webp)



Software Trezor Suite již nebudeme potřebovat, s výjimkou pravidelných aktualizací firmwaru Hardware Wallet nebo pokud chcete provést test obnovení. Ke správě portfolia nyní budeme používat software Sparrow, protože tento software se dokonale hodí pro použití pouze s Bitcoin.



## Nastavení portfolia v systému Sparrow Wallet



Začněte stažením a instalací aplikace Sparrow Wallet [z oficiálních stránek](https://sparrowwallet.com/) do počítače, pokud jste tak ještě neučinili.



Po otevření programu Sparrow Wallet se ujistěte, že je software připojen k uzlu Bitcoin, což je označeno zatržítkem v pravém dolním rohu Interface. Pokud máte s připojením Sparrow potíže, doporučuji nahlédnout do začátku tohoto návodu:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klikněte na kartu "*File*" a poté na "*New Wallet*".



![Image](assets/fr/30.webp)



Pojmenujte své portfolio a klikněte na "*Vytvořit Wallet*".



![Image](assets/fr/31.webp)



V rozevírací nabídce "*Typ skriptu*" vyberte typ skriptu, který bude použit k zabezpečení vašich bitcoinů. Doporučuji "*Taproot*", případně "*Nativní SegWit*".



![Image](assets/fr/32.webp)



Klikněte na tlačítko "*Připojený Hardware Wallet*". Váš Safe 5 musí být samozřejmě připojen k počítači a odemčen.



Po připojení zařízení Safe 5 k počítači s otevřeným modulem Sparrow Wallet budete na obrazovce Hardware Wallet vyzváni k zadání kódu passphrase BIP39. Této pokročilé možnosti se budeme věnovat v některém z příštích tutoriálů. Prozatím můžete jednoduše kliknutím na zaškrtávací políčko Green v pravém horním rohu potvrdit, že si přejete používat prázdný passphrase (tj. bez passphrase). Chcete-li zabránit tomu, aby po vás Trezor při každém spuštění požadoval zadání passphrase, přejděte do aplikace Trezor Suite, vstupte do nastavení a změňte volbu v části "*Zařízení*" > "*Wallet default*" na "*Standard*" místo "*passphrase*".



![Image](assets/fr/33.webp)



Klikněte na tlačítko "*Scan*". Měl by se zobrazit váš program Safe 5. Klikněte na tlačítko "*Importovat úložiště klíčů*".



![Image](assets/fr/34.webp)



Nyní můžete zobrazit podrobnosti o svém účtu Wallet, včetně rozšířeného veřejného klíče prvního účtu. Klepnutím na tlačítko "*Použít*" dokončete vytvoření účtu Wallet.



![Image](assets/fr/35.webp)



Pro zabezpečení přístupu ke službě Sparrow Wallet zvolte silné heslo. Toto heslo zajistí bezpečný přístup k datům Sparrow Wallet a ochrání vaše veřejné klíče, adresy, štítky a historii transakcí před neoprávněným přístupem.



Doporučuji vám uložit toto heslo do správce hesel, abyste ho nezapomněli.



![Image](assets/fr/36.webp)



A nyní je vaše portfolio importováno do aplikace Sparrow Wallet!



![Image](assets/fr/37.webp)



Než obdržíte své první bitcoiny v Wallet, **důrazně vám doporučuji provést test obnovy prázdných bitcoinů**. Zapište si nějaké referenční informace, například svůj xpub, a poté resetujte svůj Trezor Safe 5, když je Wallet stále prázdný. Poté zkuste obnovit Wallet v zařízení Trezor pomocí papírových záloh. Zkontrolujte, zda se xpub vygenerovaný po obnovení shoduje s tím, který jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé.



Chcete-li se dozvědět více o tom, jak provést test obnovení, doporučuji vám prostudovat tento další návod:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Jak mohu přijímat bitcoiny pomocí Trezor Safe 5?



V aplikaci Sparrow klikněte na kartu "*Příjem*".



![Image](assets/fr/38.webp)



Než začnete používat Address navržený společností Sparrow Wallet, zkontrolujte jej na obrazovce zařízení Trezor. Tento postup vám umožní potvrdit, že Address zobrazený na Sparrow není podvodný a že Hardware Wallet skutečně obsahuje soukromý klíč potřebný k následnému utracení bitcoinů zajištěných tímto Address. Tímto způsobem se můžete vyhnout několika typům útoků.



Tuto kontrolu provedete kliknutím na tlačítko "*Zobrazit Address*".



![Image](assets/fr/39.webp)



Zkontrolujte, zda se číslo Address zobrazené na vašem zařízení Trezor shoduje s číslem Wallet na zařízení Sparrow. Tuto kontrolu je vhodné provést také těsně před sdělením Address odesílateli, abyste si byli jisti jeho platností. Pro potvrzení můžete stisknout obrazovku.



![Image](assets/fr/40.webp)



Poté můžete přidat "*Label*" a popsat zdroj bitcoinů, které budou tímto Address zabezpečeny. Jedná se o dobrý postup, který vám umožní lépe spravovat UTXO.



![Image](assets/fr/41.webp)



Pomocí tohoto účtu Address pak můžete přijímat bitcoiny.



![Image](assets/fr/42.webp)



## Jak mohu posílat bitcoiny pomocí Trezor Safe 5?



Nyní, když jste obdrželi první Satss na svůj Safe 5-secured Wallet, můžete je také utratit! Připojte Trezor k počítači, odemkněte jej kódem PIN, spusťte Sparrow Wallet a přejděte na záložku "*Odeslat*" pro vytvoření nové transakce.



![Image](assets/fr/43.webp)



Pokud chcete *Kontrolu mincí*, tj. vybrat konkrétně, které UTXO se mají v transakci spotřebovat, přejděte na kartu "*UTXO*". Vyberte UTXO, které si přejete utratit, a poté klikněte na tlačítko "*Odeslat vybrané*". Budete přesměrováni na stejnou obrazovku v záložce "*Odeslat*", ale s již vybranými UTXO pro transakci.



![Image](assets/fr/44.webp)



Zadejte cíl Address. Kliknutím na tlačítko "*+ Add*" můžete zadat i více adres.



![Image](assets/fr/45.webp)



Napište si "*název*", abyste si zapamatovali účel tohoto výdaje.



![Image](assets/fr/46.webp)



Vyberte částku, která má být zaslána na tento účet Address.



![Image](assets/fr/47.webp)



Upravte sazbu poplatků za transakci podle aktuálního trhu. Pro výběr vhodné sazby poplatku můžete například použít [Mempool.space](https://Mempool.space/).



Ujistěte se, že jsou všechny parametry transakce správné, a klikněte na tlačítko "*Vytvořit transakci*".



![Image](assets/fr/48.webp)



Pokud vám vše vyhovuje, klikněte na "*Finalizovat transakci pro podpis*".



![Image](assets/fr/49.webp)



Klikněte na "*Podepsat*".



![Image](assets/fr/50.webp)



Klikněte na "*Podepsat*" vedle svého zařízení Trezor Safe 5.



![Image](assets/fr/51.webp)



Zkontrolujte parametry transakce na obrazovce Hardware Wallet, včetně přijímajícího Address příjemce, odeslané částky a poplatku. Po ověření transakce na zařízení Trezor stiskněte a podržte obrazovku a podepište ji.



![Image](assets/fr/52.webp)



Vaše transakce je nyní podepsána. Naposledy zkontrolujte, zda je vše v pořádku, a kliknutím na "*Broadcast Transaction*" ji odvysílejte v síti Bitcoin.



![Image](assets/fr/53.webp)



Najdete ji na kartě "*Transakce*" v programu Sparrow Wallet.



![Image](assets/fr/54.webp)



Blahopřejeme, nyní jste se seznámili se základním používáním zařízení Trezor Safe 5 se Sparrow Wallet! Chcete-li se posunout o krok dál, doporučuji tento komplexní návod na použití Trezoru Hardware Wallet s passphrase BIP39 pro zvýšení vaší bezpečnosti:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Pokud vám tento návod přišel užitečný, budu vám vděčný, když mi níže zanecháte palec Green. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji vám mnohokrát!