---
name: Trezor Safe 3
description: Konfigurace a používání modulu Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*Image credit: [Trezor.io](https://trezor.io/)*



Trezor Safe 3 je Hardware Wallet navržený společností SatoshiLabs a vytvořený v roce 2023. Jedná se o velmi kompaktní a lehký model (14 gramů) určený pro začátečníky i středně pokročilé uživatele. Jedná se o nástupce slavného modelu One s významnými doplňky, přičemž si zachovává otevřený přístup značky, který jej odlišuje od jeho hlavního konkurenta Ledger. Cena modelu Safe 3 je 79 EUR. Je tedy umístěn v segmentu střední třídy Hardware Wallet a přímo konkuruje modelu Ledger Nano S Plus.



Trezor Safe 3 nemá baterii a funguje výhradně prostřednictvím připojení USB-C, které slouží k napájení i komunikaci. Je vybaven malým 0,96palcovým monochromatickým displejem OLED a dvěma fyzickými tlačítky.



![Image](assets/fr/01.webp)



Safe 3 nabízí všechny základní funkce, které se od dobrého Hardware Wallet očekávají, včetně vynikající integrace passphrase BIP39. Zatím však nepodporuje Miniscript.



Tento model je vhodný zejména pro začátečníky a mohl by být dokonce modelem Hardware Wallet, který bych doporučil začínajícím uživatelům. Je také vhodný pro středně pokročilé uživatele. Na druhou stranu nemusí splnit všechna očekávání pokročilých uživatelů, kteří hledají specifičtější funkce, jež jsou k dispozici u zařízení, jako je Coldcard. Nicméně pokud tyto pokročilé možnosti nepotřebujete, může být Trezor Safe 3 vynikající volbou.



## Bezpečnostní model Trezor Safe 3



Trezor Safe 3 je nyní vybaven **bezpečným prvkem** s certifikací EAL6+, což je výrazný pokrok oproti předchozím modelům, jako je Model One a Model T. Jedná se o čip OPTIGA Trust M V3, který neukládá přímo kód seed, ale funguje jako kryptografický prvek pro zabezpečení přístupu k němu. Zabezpečený prvek uchovává tajemství, k němuž lze získat přístup pouze po správném zadání kódu PIN uživatelem. Toto tajemství se pak používá k dešifrování kódu seed, který je uložen zašifrovaný v hlavní paměti zařízení.



Tento hybridní bezpečnostní systém nabízí lepší fyzickou ochranu, zejména proti útokům extrakcí nebo invazivní analýze, což jsou problémy, na které byl model One náchylný, zejména při správě PIN. Tyto zranitelnosti jsou nyní obejity díky použití zabezpečeného prvku. Tento model také zachovává architekturu softwaru s otevřeným zdrojovým kódem: kód, který řídí generování a používání soukromých klíčů, zůstává plně přístupný a ověřitelný. Čip OPTIGA spravuje pouze kód PIN, což je prvek externí vůči správě klíčů Bitcoin Wallet. Uvolňuje pouze tajemství, které lze použít k dešifrování kódu seed. Čip OPTIGA Trust M V3 také těží z relativně volné licence, která opravňuje společnost SatoshiLabs k volnému zveřejňování potenciálních zranitelností.



Tento model zabezpečení představuje podle mého názoru jeden z nejlepších kompromisů, které jsou dnes na trhu k dispozici. Kombinuje výhody zabezpečeného prvku se správou softwaru s otevřeným zdrojovým kódem. Dříve museli uživatelé volit mezi zvýšeným fyzickým zabezpečením pomocí čipu a transparentností pomocí otevřeného zdrojového kódu; s Trezor Safe 3 je možné využívat výhod obojího.



V tomto návodu vám ukážeme, jak bezpečně nastavit a používat zařízení Trezor Safe 3.



## Rozbalení zařízení Trezor Safe 3



Po obdržení zařízení Safe 3 se ujistěte, že krabice a Seal jsou neporušené, abyste potvrdili, že balíček nebyl otevřen. Při pozdějším nastavení zařízení bude rovněž provedeno softwarové ověření jeho pravosti a neporušenosti.



Obsah krabice zahrnuje :




- Trezor Safe 3;
- Sáček obsahující karton k nahrání věty Mnemonic, samolepky a pokyny;
- Kabel USB-C na USB-C.



![Image](assets/fr/02.webp)



Trezor Safe 3 by měl být po otevření chráněn ochranným plastem a port USB-C by měl být zajištěn holografickým štítkem Seal. Ujistěte se, že tam je.



![Image](assets/fr/03.webp)



Navigace v zařízení je jednoduchá: pravým tlačítkem se posouváte doprava a levým tlačítkem doleva. Akci potvrdíte současným stisknutím obou tlačítek.



![Image](assets/fr/04.webp)



## Předpoklady



V tomto návodu vám ukážu, jak používat Trezor Safe 3 se softwarem [Sparrow Wallet pro správu portfolia](https://sparrowwallet.com/download/). Pokud jste si tento software ještě nenainstalovali, učiňte tak nyní. Pokud potřebujete pomoc, máme také podrobný návod na konfiguraci Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Ke konfiguraci zařízení Safe 3, kontrole jeho pravosti a instalaci firmwaru budete potřebovat také software Trezor Suite. Tento software budeme používat pouze k tomuto účelu a poté bude potřeba pouze pro aktualizace firmwaru. Pro každodenní správu Wallet budeme používat výhradně Sparrow Wallet, protože je optimalizován pro Bitcoin a snadno se používá i pro začátečníky (Sparrow podporuje pouze Bitcoin, nikoli altcoiny).



[Stáhnout Trezor Suite z oficiálních stránek](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



U obou těchto programů důrazně doporučuji, abyste před instalací do počítače ověřili jejich pravost (pomocí GnuPG) i integritu (pomocí Hash). Pokud nevíte, jak to udělat, můžete postupovat podle tohoto dalšího návodu :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Spuštění aplikace Trezor Safe 3



Připojte zařízení Safe 3 k počítači, ve kterém jsou již nainstalovány aplikace Trezor Suite a Sparrow Wallet.



![Image](assets/fr/06.webp)



Otevřete sadu Trezor Suite a klikněte na "*Nastavení mého Trezoru*".



![Image](assets/fr/07.webp)



Vyberte možnost "*Bitcoin-only firmware*" a klikněte na "*Install Bitcoin-only*".



![Image](assets/fr/08.webp)



Trezor Suite poté nainstaluje firmware do zařízení Safe 3. Během instalace vyčkejte.



![Image](assets/fr/09.webp)



Klikněte na "*Pokračovat*".



![Image](assets/fr/10.webp)



Poté přejděte k testu pravosti, abyste se ujistili, že váš Hardware Wallet není falešný nebo kompromitovaný.



![Image](assets/fr/11.webp)



Na zařízení Safe 3 potvrďte stisknutím pravého tlačítka.



![Image](assets/fr/12.webp)



Pokud je váš Trezor pravý, zobrazí se v aplikaci Trezor Suite potvrzovací zpráva.



![Image](assets/fr/13.webp)



Poté můžete přeskočit okna se základními pokyny k obsluze.



![Image](assets/fr/14.webp)



## Vytvoření portfolia Bitcoin



V aplikaci Trezor Suite klikněte na tlačítko "*Vytvořit nový Wallet*".



![Image](assets/fr/15.webp)



Pro standardní portfolio můžete zvolit výchozí typ zálohy. Tím se vytvoří klasické portfolio s jedním signálem a 12 slovy Mnemonic. Klikněte na "*Vytvořit Wallet*".



Pokud se chcete dozvědět více o dalších možnostech zálohování, které jsou k dispozici v nástroji Trezor, včetně *Zálohování více sdílení*, doporučuji vám přečíst si také tento návod :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Přijměte podmínky používání na webu Hardware Wallet.



![Image](assets/fr/17.webp)



Dalším stisknutím pravého tlačítka vytvoříte nové portfolio.



![Image](assets/fr/18.webp)



V aplikaci Trezor Suite klikněte na "*Pokračovat v zálohování*".



![Image](assets/fr/19.webp)



Software poskytuje pokyny ke správě fráze Mnemonic.



Tato služba Mnemonic vám poskytuje plný a neomezený přístup ke všem vašim bitcoinům. Kdokoli, kdo má tuto frázi, může vaše prostředky ukrást, a to i bez fyzického přístupu k trezoru Trezor 3.



Fráze o 12 slovech obnoví přístup k vašim bitcoinům v případě ztráty, krádeže nebo rozbití vašeho Hardware Wallet. Je proto velmi důležité ji pečlivě uložit a uschovat na bezpečném místě.



Můžete jej napsat na karton dodávaný v krabici, nebo pro větší bezpečnost doporučuji vyrýt jej na podstavec z nerezové oceli, který jej ochrání před požárem, povodní nebo zřícením.



Potvrďte pokyny a klikněte na tlačítko "*Vytvořit zálohu Wallet*".



![Image](assets/fr/20.webp)



Program Safe 3 vytvoří frázi Mnemonic pomocí generátoru náhodných čísel. Ujistěte se, že vás během této operace nikdo nesleduje. Zapište slova uvedená na obrazovce na vámi zvolené fyzické médium. V závislosti na vaší bezpečnostní strategii můžete zvážit vytvoření několika úplných fyzických kopií fráze (především ji však nedělte). Je důležité, aby byla slova očíslována a seřazena za sebou.



***Samozřejmě nesmíte tato slova nikdy sdílet na internetu, jak to dělám v tomto návodu. Tento příklad Wallet bude použit pouze na Testnet a na konci tutoriálu bude odstraněn



Pro více informací o správném způsobu ukládání a správy fráze Mnemonic vřele doporučuji tento další návod, zejména pokud jste začátečníci:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Chcete-li přejít na další slova, klikněte pravým tlačítkem myši. Zpět se můžete vrátit kliknutím na levé tlačítko. Jakmile zapíšete všechna slova, podržením pravého tlačítka přejdete na další krok.



![Image](assets/fr/22.webp)



Vyberte slova ve větě Mnemonic podle jejich pořadí, abyste si ověřili, že jste je zapsali správně. Pomocí tlačítek vlevo a vpravo se pohybujte mezi návrhy a poté vyberte správné slovo klepnutím na obě tlačítka současně.



![Image](assets/fr/23.webp)



Po dokončení tohoto ověřovacího postupu klikněte na tlačítko vpravo.



![Image](assets/fr/24.webp)



## Nastavení kódu PIN



Poté následuje krok zadání kódu PIN. Kód PIN odemkne zařízení Trezor. Poskytuje tedy ochranu před neoprávněným fyzickým přístupem. Tento kód PIN se nepodílí na odvození kryptografických klíčů vašeho zařízení Wallet. Takže i bez přístupu ke kódu PIN vám vlastnictví vaší 12slovné fráze Mnemonic umožní znovu získat přístup k vašim bitcoinům.



V aplikaci Trezor Suite klikněte na tlačítko "*Pokračovat v zadávání kódu PIN*" a poté na tlačítko "*Zadat kód PIN*".



![Image](assets/fr/25.webp)



Potvrďte pomocí Safe 3.



![Image](assets/fr/26.webp)



Doporučujeme zvolit co nejnáhodnější kód PIN. Nezapomeňte tento kód uložit na jiné místo, než kde je uložen váš Trezor (např. do správce hesel). Kód PIN můžete definovat v rozsahu 8 až 50 číslic. Pro zvýšení bezpečnosti doporučuji zvolit co nejdelší kód PIN.



Pomocí tlačítek vlevo a vpravo vyberte jednotlivé číslice. Chcete-li potvrdit volbu a přejít na další číslici, stiskněte současně obě tlačítka.



![Image](assets/fr/27.webp)



Po dokončení klikněte na zaškrtávací políčko "*ENTER*" na začátku číslic a podruhé potvrďte PIN.



![Image](assets/fr/28.webp)



Váš kód PIN byl zaregistrován.



![Image](assets/fr/29.webp)



V aplikaci Trezor Suite klikněte na tlačítko "*Dokončit nastavení*".



![Image](assets/fr/30.webp)



Konfigurace zařízení Safe 3 je nyní dokončena. Pokud chcete, můžete změnit název a domovskou stránku Hardware Wallet.



![Image](assets/fr/31.webp)



Software Trezor Suite již nebudeme potřebovat, s výjimkou pravidelných aktualizací firmwaru Hardware Wallet nebo pokud chcete provést test obnovení. Ke správě portfolia nyní budeme používat software Sparrow, protože tento software se dokonale hodí pro použití pouze pro Bitcoin.



## Nastavení portfolia v aplikaci Sparrow Wallet



Začněte stažením a instalací aplikace Sparrow Wallet [z oficiálních stránek](https://sparrowwallet.com/) do počítače, pokud jste tak ještě neučinili.



Po otevření programu Sparrow Wallet se ujistěte, že je software připojen k uzlu Bitcoin, což je indikováno zaškrtnutím v pravém dolním rohu Interface. Pokud máte s připojením Sparrow potíže, doporučuji přečíst si začátek tohoto návodu:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klikněte na kartu "*File*" a poté na "*New Wallet*".



![Image](assets/fr/32.webp)



Pojmenujte své portfolio a klikněte na "*Vytvořit Wallet*".



![Image](assets/fr/33.webp)



V rozevírací nabídce "*Typ skriptu*" vyberte typ skriptu, který bude použit k zabezpečení vašich bitcoinů. Doporučuji "*Taproot*", případně "*Nativní SegWit*".



![Image](assets/fr/34.webp)



Klikněte na tlačítko "*Připojený Hardware Wallet*". Váš Safe 3 musí být samozřejmě připojen k počítači a odemčen.



![Image](assets/fr/35.webp)



Klikněte na tlačítko "*Scan*". Měl by se zobrazit váš program Safe 3. Klikněte na "*Importovat úložiště klíčů*".



![Image](assets/fr/36.webp)



Nyní můžete zobrazit podrobnosti o svém účtu Wallet, včetně rozšířeného veřejného klíče prvního účtu. Kliknutím na tlačítko "*Použít*" dokončíte vytvoření účtu Wallet.



![Image](assets/fr/37.webp)



Pro zabezpečení přístupu ke službě Sparrow Wallet zvolte silné heslo. Toto heslo zajistí bezpečný přístup k datům Sparrow Wallet a ochrání vaše veřejné klíče, adresy, štítky a historii transakcí před neoprávněným přístupem.



Doporučuji vám uložit toto heslo do správce hesel, abyste ho nezapomněli.



![Image](assets/fr/38.webp)



A nyní bylo vaše portfolio importováno do Sparrow Wallet!



![Image](assets/fr/39.webp)



Než obdržíte své první bitcoiny do Wallet, **důrazně vám doporučuji provést test obnovy prázdného účtu**. Zapište si nějaké referenční informace, například svůj xpub, a poté resetujte svůj Trezor Safe 3, když je Wallet stále prázdný. Poté se pokuste obnovit Wallet na Trezoru pomocí papírových záloh. Zkontrolujte, zda se xpub vygenerovaný po obnovení shoduje s tím, který jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé.



Chcete-li se dozvědět více o tom, jak provést test obnovení, doporučuji vám prostudovat tento další návod:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Jak mohu přijímat bitcoiny pomocí Trezor Safe 3?



V aplikaci Sparrow klikněte na kartu "*Příjem*".



![Image](assets/fr/40.webp)



Než začnete používat Address navržený společností Sparrow Wallet, zkontrolujte jej na obrazovce svého zařízení Trezor. Tento postup vám umožní potvrdit, že Address zobrazený na Sparrow není podvodný a že Hardware Wallet skutečně obsahuje soukromý klíč potřebný k následnému utracení bitcoinů zajištěných tímto Address. Tímto způsobem se můžete vyhnout několika typům útoků.



Tuto kontrolu provedete kliknutím na tlačítko "*Zobrazit Address*".



![Image](assets/fr/41.webp)



Zkontrolujte, zda se číslo Address zobrazené na vašem zařízení Trezor shoduje s číslem Wallet na zařízení Sparrow. Tuto kontrolu je vhodné provést také těsně před sdělením Address odesílateli, abyste si byli jisti jeho platností. K potvrzení můžete použít tlačítka .



![Image](assets/fr/42.webp)



Poté můžete přidat "*Label*" a popsat zdroj bitcoinů, které budou tímto Address zabezpečeny. Jedná se o dobrý postup, který vám umožní lépe spravovat UTXO.



![Image](assets/fr/43.webp)



Pomocí tohoto účtu Address pak můžete přijímat bitcoiny.



![Image](assets/fr/44.webp)



## Jak mohu posílat bitcoiny pomocí Trezor Safe 3?



Nyní, když jste obdrželi své první Satss na svůj Safe 3-secured Wallet, můžete je také utratit! Připojte Trezor k počítači, odemkněte jej pomocí kódu PIN, spusťte Sparrow Wallet a přejděte na záložku "*Odeslat*" pro vytvoření nové transakce.



![Image](assets/fr/45.webp)



Pokud chcete *Kontrolu mincí*, tj. vybrat konkrétně, které UTXO se mají v transakci spotřebovat, přejděte na kartu "*UTXO*". Vyberte UTXO, které si přejete utratit, a poté klikněte na tlačítko "*Odeslat vybrané*". Budete přesměrováni na stejnou obrazovku v záložce "*Odeslat*", ale s již vybranými UTXO pro transakci.



![Image](assets/fr/46.webp)



Zadejte cílové číslo Address. Kliknutím na tlačítko "*+ Add*" můžete zadat i více adres.



![Image](assets/fr/47.webp)



Napište si "*název*", abyste si zapamatovali účel tohoto výdaje.



![Image](assets/fr/48.webp)



Zvolte částku, která má být zaslána na tento účet Address.



![Image](assets/fr/49.webp)



Upravte sazbu poplatků za transakci podle aktuálního trhu. Pro výběr vhodné sazby poplatku můžete například použít [Mempool.space](https://Mempool.space/).



Ujistěte se, že jsou všechny parametry transakce správné, a klikněte na tlačítko "*Vytvořit transakci*".



![Image](assets/fr/50.webp)



Pokud vám vše vyhovuje, klikněte na "*Finalizovat transakci pro podpis*".



![Image](assets/fr/51.webp)



Klikněte na "*Podepsat*".



![Image](assets/fr/52.webp)



Klikněte na "*Podepsat*" vedle svého zařízení Trezor Safe 3.



![Image](assets/fr/53.webp)



Zkontrolujte parametry transakce na obrazovce Hardware Wallet, včetně přijímacího Address příjemce, odeslané částky a poplatku. Po ověření transakce na Trezoru ji podepište současným kliknutím na obě tlačítka.



![Image](assets/fr/54.webp)



Vaše transakce je nyní podepsána. Naposledy zkontrolujte, zda je vše v pořádku, a kliknutím na "*Broadcast Transaction*" ji odvysílejte v síti Bitcoin.



![Image](assets/fr/55.webp)



Najdete ji na kartě "*Transakce*" v aplikaci Sparrow Wallet.



![Image](assets/fr/56.webp)



Blahopřejeme, nyní jste se seznámili se základním používáním zařízení Trezor Safe 3 se Sparrow Wallet! Chcete-li se posunout o krok dál, doporučuji tento komplexní návod na použití Trezoru Hardware Wallet s BIP39 passphrase, který zvýší vaši bezpečnost:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Pokud pro vás byl tento návod užitečný, budu vám vděčný, když níže zanecháte palec Green. Neváhejte tento článek sdílet na svých sociálních sítích. Moc vám děkuji!