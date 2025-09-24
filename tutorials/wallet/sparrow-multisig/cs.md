---
name: Sparrow Wallet - Multisig
description: Vytvoření portfolia s více podpisy v aplikaci Sparrow
---
![cover](assets/cover.webp)



Vícepodpisová struktura Wallet (často nazývaná "*Multisig*") je struktura Bitcoin Wallet, která k autorizaci výdaje vyžaduje několik kryptografických podpisů z různých klíčů. Na rozdíl od konvenčního ("*singlesig*") Wallet, kde k odemčení UTXO stačí jediný soukromý klíč, je Multisig založen na modelu **m-of-n**: z _n_ klíčů přidružených ke Wallet musí _m_ povinně spolupodepsat každou transakci.



Tento mechanismus umožňuje sdílet řízení portfolia mezi několika subjekty nebo zařízeními. Například v konfiguraci 2 ze 3 jsou generovány tři nezávislé sady klíčů, ale k uvolnění prostředků jsou potřeba pouze dvě. Tato architektura výrazně snižuje rizika spojená s kompromitací nebo ztrátou klíče: zloděj, který má přístup pouze k jednomu klíči, nemůže vyprázdnit Wallet a uživatel, který jeden klíč ztratí, má stále přístup ke svým prostředkům pomocí zbývajících dvou.



![Image](assets/fr/01.webp)



Toto vyšší zabezpečení je však spojeno s větší složitostí. Nastavení Multisig Wallet vyžaduje zabezpečení několika frází Mnemonic (jedna pro každý podpisový faktor) a rozšířených veřejných klíčů ("*xpub*"). Pokud totiž používáte Multisig 2-of-3 Wallet, musíte mít pro získání Wallet buď všechny tři fráze Mnemonic, nebo alespoň dvě ze tří frází. Pokud však máte pouze dvě ze tří frází, potřebujete také přístup ke třem *xpub*, bez nichž nebude možné získat veřejné klíče potřebné k přístupu k bitcoinům, které chrání.



Abychom to shrnuli, k obnově portfolia Multisig je třeba :




- Nebo získejte přístup ke všem frázím Mnemonic přiřazeným k jednotlivým signaturním faktorům;
- Buď máte minimální počet frází Mnemonic požadovaný prahovou hodnotou, abyste mohli podepisovat, a také máte přístup k xpubům všech faktorů, abyste mohli získat potřebné veřejné klíče.



![Image](assets/fr/02.webp)



Tuto správu záloh portfolia Multisig usnadňují *Output Script Descriptors*, které seskupují všechna veřejná data potřebná pro přístup k fondům. Tato funkce však zatím není implementována ve všech programech pro správu portfolia.



Služba Multisig je vhodná zejména pro uživatele bitcoinů, kteří hledají lepší zabezpečení nebo kolektivní správu finančních prostředků: společnosti, sdružení, rodiny nebo jednotlivé uživatele, kteří drží značné množství bitcoinů. Lze jej použít k vytvoření decentralizovaných schémat správy, například k rozdělení podpisových pravomocí mezi několik manažerů nebo členů týmu.



V tomto tutoriálu se naučíme vytvořit a používat klasický vícepodpis Wallet pomocí **Sparrow Wallet**. Pokud chcete vytvořit vlastní portfolio s více podpisy a časovými zámky, doporučuji místo toho použít Liana:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Předpoklady



V tomto tutoriálu vám ukážu, jak vytvořit Multisig pomocí [softwaru pro správu portfolia Sparrow Wallet](https://sparrowwallet.com/download/). Pokud jste si tento software ještě nenainstalovali, učiňte tak nyní. Pokud potřebujete pomoc, máme také podrobný návod na konfiguraci Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

K nastavení vícepodpisové služby Wallet budete potřebovat různé hardwarové peněženky. Například pro Multisig 2-de-3 můžete použít :




- Trezor model One;
- Ledger Flex;
- Karta Coldcard MK3.



![Image](assets/fr/03.webp)



V konfiguraci Multisig je dobré používat různé značky Hardware Wallet. Tím zajistíte, že pokud se u určitého modelu vyskytne závažný problém, neovlivní to celkovou bezpečnost vašeho modelu Multisig. Navíc vám to umožní využívat specifické výhody každého zařízení. Například v mé konfiguraci :





- Trezor Model One je zcela otevřený, což umožňuje ověřit generaci seed. Protože však není vybaven zabezpečeným prvkem, zůstává zranitelný vůči fyzickým útokům;





- Naproti tomu model Ledger Flex využívá neověřitelný proprietární firmware, ale obsahuje zabezpečený prvek, který nabízí vynikající fyzickou ochranu;





- Karta Coldcard je vybavena zabezpečeným prvkem a její kód lze prohledávat. Je to zajímavá volba pro naši konfiguraci, protože nabízí ověřovací funkce, které nejsou u jiných modelů k dispozici.



Před konfigurací Multisig Wallet se ujistěte, že je každý Hardware Wallet správně nakonfigurován (generování a ukládání Mnemonic, definice PIN). Podrobné pokyny naleznete v našich návodech pro jednotlivé Hardware Wallet, například :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Jak uvidíme později v tomto návodu, je možné do konfigurace Multisig začlenit také faktor, který není spojen s Hardware Wallet, ale jehož soukromé klíče jsou uloženy v počítači. Tento způsob je samozřejmě méně bezpečný než výhradní použití hardwarových peněženek, ale v určitých případech může mít význam. Například pro konfiguraci Multisig 2-de-3 můžete zvolit dvě hardwarové peněženky a jednu Software Wallet.



## Vytvoření portfolia Multisig



Otevřete program Sparrow Wallet, klikněte na kartu "*Soubor*" a vyberte možnost "*Nový Wallet*".



![Image](assets/fr/04.webp)



Přiřaďte svému portfoliu s více podpisy název a potvrďte kliknutím na "*Vytvořit Wallet*".



![Image](assets/fr/05.webp)



V rozevírací nabídce "*Typ politiky*" vyberte možnost "*Více podpisů*".



![Image](assets/fr/06.webp)



V pravém horním rohu nyní můžete definovat celkový počet klíčů v Multisig a také počet spolupodepisujících osob, které jsou nutné k autorizaci výdaje. V mém příkladu se jedná o schéma 2 ze 3.



![Image](assets/fr/07.webp)



V dolní části okna Sparrow Wallet se zobrazí tři "*Keystore*". Každý z nich představuje sadu klíčů. Zde používám tři hardwarová portfolia, takže každý "*Keystore*" odpovídá jednomu z nich. Nyní je budeme konfigurovat.



Začínám kartou Coldcard. Na kartě "*Keystore 1*" vyberu možnost "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Na kartě Coldcard po odemknutí zařízení přejdu do nabídky "*Nastavení*" a poté do nabídky "*Multisig Peněženky*".



![Image](assets/fr/09.webp)



Tato nabídka umožňuje spravovat portfolia Multisig, kterých se karta Coldcard účastní. Chci vytvořit nové, a proto zvolím "*Export XPUB*".



![Image](assets/fr/10.webp)



Pokud spravujete pouze jeden účet, můžete pole "*Číslo účtu*" ponechat prázdné a potvrdit jej přímo stisknutím potvrzovacího tlačítka.



![Image](assets/fr/11.webp)



Karta Coldcard pak vytvoří soubor generate obsahující váš xpub, uložený na kartě Micro SD.



![Image](assets/fr/12.webp)



Vložte tuto kartu Micro SD do počítače. V aplikaci Sparrow Wallet klikněte na tlačítko "*Import File...*" vedle položky "*Coldcard Multisig*" a vyberte soubor vytvořený kartou Coldcard na kartě.



![Image](assets/fr/13.webp)



Váš xpub byl úspěšně importován. Nyní zopakujeme postup s dalšími dvěma hardwarovými peněženkami.



![Image](assets/fr/14.webp)



U zařízení Ledger Flex vyberu možnost "*Keystore 2*" a poté kliknu na možnost "*Připojené Hardware Wallet*". Ujistěte se, že je zařízení Ledger připojeno k počítači, odemčeno a že je otevřena aplikace Bitcoin.



![Image](assets/fr/15.webp)



Poté klikněte na tlačítko "*Scan...*".



![Image](assets/fr/16.webp)



Vedle názvu hardwarového portfolia klikněte na "*Importovat úložiště klíčů*".



![Image](assets/fr/17.webp)



Druhý signatář je nyní správně zaregistrován v aplikaci Sparrow Wallet.



![Image](assets/fr/18.webp)



Přesně stejný postup zopakuji i u zařízení Trezor One, abych dokončil konfiguraci Multisig.



![Image](assets/fr/19.webp)



V mé konfiguraci se tímto případem nezabýváme, ale pokud chcete do svého Multisig zahrnout podpis prostřednictvím Software Wallet ve Sparrow (Hot Wallet), jednoduše klikněte na tlačítko "*Nový nebo importovaný Software Wallet*".



Nyní, když jsou všechna vaše podpisová zařízení importována do aplikace Sparrow Wallet, můžete dokončit vytvoření Multisig kliknutím na tlačítko "*Použít*".



![Image](assets/fr/20.webp)



Zvolte si silné heslo pro zabezpečení přístupu k zařízení Sparrow Wallet Wallet. Toto heslo chrání vaše veřejné klíče, adresy, štítky a historii transakcí před neoprávněným přístupem.



Nezapomeňte toto heslo uložit na bezpečné místo, například do správce hesel, abyste ho neztratili.



![Image](assets/fr/21.webp)



## Zálohování portfolia Multisig



Nyní uložíme náš *Output Script Descriptor* na kartu Coldcard (to se týká pouze uživatelů s kartou Coldcard v systému Multisig) a především si budeme uchovávat jeho zálohu na nezávislém médiu.



*Deskriptor* obsahuje všechny xpuby v portfoliu Multisig a také odvozovací cesty použité pro klíče generate. Vzpomeňte si, co jsme viděli v části 1: abyste mohli obnovit portfolio Multisig, musíte mít buď **všechny** fráze Mnemonic, nebo jen minimální počet potřebný k dosažení prahové hodnoty podpisu. V druhém případě je však nezbytné mít také **předpisy** chybějících signatářů. *Popis* obsahuje všechny xpuby vašeho Multisig.



Pokud vám to není jasné, zapamatujte si toto: pro získání Multisig potřebujete minimální počet frází Mnemonic pro každou použitou Hardware Wallet v závislosti na prahové hodnotě (v mém případě: 2 fráze) a také *Deskriptor*.



Tento *Deskriptor* neobsahuje žádné soukromé klíče, pouze veřejné. To znamená, že neumožňuje přístup k finančním prostředkům. Není proto tak kritický jako fráze Mnemonic, které poskytují plný přístup k vašim bitcoinům. Riziko u *Descriptoru* se týká výhradně důvěrnosti: v případě kompromitace by třetí strana mohla sledovat všechny vaše transakce, ale nemohla by utratit vaše prostředky.



Důrazně doporučuji, abyste si vytvořili několik kopií tohoto *Deskriptoru* a uchovávali je u každého podepisovacího zařízení Multisig. V mém případě si například vytisknu *Descriptor* na papír a jednu kopii si ponechám u karty Coldcard, druhou u Trezoru a třetí u Ledger. Tento *Deskriptor* také ukládám jako soubor PDF na tři paměti USB, z nichž každá je uložena u jednoho z hardwarových portfolií. Tímto způsobem maximalizuji své šance, že tento *Descriptor* nikdy neztratím, a mám jistotu, že budu mít dvě kopie (jednu fyzickou a jednu digitální) u každého zařízení.



Po vytvoření portfolia Multisig vám Sparrow automaticky poskytne tento *Deskriptor*. Klepnutím na tlačítko "*Uložit PDF...*" jej uložíte jako text i jako QR kód.



![Image](assets/fr/22.webp)



Tento soubor PDF si pak můžete vytisknout a zkopírovat na paměťové zařízení USB.



![Image](assets/fr/23.webp)



Tento *Deskriptor* zaregistrujeme také v kartě Coldcard (pokud ji v konfiguraci používáte). To umožní kartě Coldcard ověřit, že každá později podepsaná transakce odpovídá původnímu Wallet: správné xpuby, správný formát Address, správná odvozovací cesta... Bez tohoto importovaného *Deskriptoru* nemůže Coldcard potvrdit, že adresy Exchange nebyly uneseny nebo že s PSBT nebylo manipulováno.



Právě proto je karta Coldcard v Multisig tak zajímavá: nabízí dodatečné kontroly proti některým sofistikovaným útokům, které jiné hardwarové peněženky neumožňují (samozřejmě za předpokladu, že ji používáte k podepisování).



V aplikaci Sparrow otevřete nabídku "*Nastavení*" a klikněte na "*Exportovat...*".



![Image](assets/fr/24.webp)



Vedle možnosti "*Coldcard Multisig*" klikněte na "*Export File...*" a uložte textový soubor na kartu Micro SD.



![Image](assets/fr/25.webp)



Poté vložte kartu do zařízení Coldcard. Přejděte do nabídky "*Nastavení*", poté do nabídky "*Peněženky Multisig*" a vyberte možnost "*Importovat z SD*".



![Image](assets/fr/26.webp)



Vyberte příslušný soubor a potvrďte import.



![Image](assets/fr/27.webp)



Klikněte na název nově importované jednotky Multisig.



![Image](assets/fr/28.webp)



Zkontrolujte konfigurační parametry Multisig a potvrďte registraci.



![Image](assets/fr/29.webp)



Vaše karta Multisig je nyní správně uložena na kartě Coldcard. Pokud máte v jedné kartě Multisig více karet Coldcard, opakujte tento postup pro každou z nich.



Kromě uložení *Deskriptoru* nezapomeňte věnovat zvláštní pozornost uložení frází Mnemonic pro každé z vašich podpisových zařízení. Pokud s ukládáním teprve začínáte, vřele doporučuji prostudovat tento další návod, kde se dozvíte, jak je správně ukládat a spravovat:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Před obdržením prvních bitcoinů na Multisig vám **důrazně doporučuji provést test obnovení prázdného účtu**. Zaznamenejte si některé referenční informace, například první příjem Address, a poté resetujte hardwarové peněženky, dokud je Wallet stále prázdný. Poté zkuste obnovit Multisig Wallet na hardwarových peněženkách pomocí papírových záloh fráze Mnemonic a poté na Sparrow pomocí *Deskriptoru*. Zkontrolujte, zda první Address vygenerovaný po obnovení odpovídá tomu, který jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé.



Chcete-li se dozvědět více o tom, jak provést test obnovení, doporučuji vám prostudovat tento další návod:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Přijímání bitcoinů na vašem Multisig



Váš Wallet je nyní připraven přijímat bitcoiny. V aplikaci Sparrow klikněte na kartu "*Příjem*".



![Image](assets/fr/30.webp)



Než začnete používat Address vygenerovaný Sparrow Wallet, věnujte čas jeho kontrole přímo na obrazovce své hardwarové peněženky. Tím se ujistíte, že Address nebyl pozměněn a že vaše zařízení obsahují soukromé klíče potřebné k utrácení souvisejících finančních prostředků. To vám pomůže chránit se před řadou vektorů útoku.



Chcete-li to provést, klikněte na "*Zobrazit Address*", čímž zobrazíte Address na zařízení Trezor nebo Ledger, pokud je připojeno kabelem.



![Image](assets/fr/31.webp)



Pomocí karty Coldcard lze toto ověření provést bez jakékoli interakce s aplikací Sparrow. Stačí otevřít nabídku "*Address Explorer*" a úplně dole vybrat svůj Multisig.



![Image](assets/fr/32.webp)



Poté se zobrazí adresy příjmu generované zařízením Multisig.



![Image](assets/fr/33.webp)



Zkontrolujte, zda číslo Address zobrazené na každém štítku Hardware Wallet přesně odpovídá číslu Wallet ve Sparrow. Je vhodné to provést těsně před sdílením Address s plátcem, abyste si byli jisti jeho neporušeností.



Tomuto účtu Address pak můžete přiřadit "*Label*", který označuje původ přijatých bitcoinů. Jedná se o dobrý způsob organizace správy vašich UTXO.



![Image](assets/fr/34.webp)



Po ověření můžete pomocí Address přijímat bitcoiny.



![Image](assets/fr/35.webp)



## Posílání bitcoinů pomocí Multisig



Nyní, když jste obdrželi své první saty na Multisig Wallet, můžete je také utratit! Ve Vrabci přejděte na kartu "*Odeslat*" a vytvořte novou transakci.



![Image](assets/fr/36.webp)



Pokud chcete použít *Coin Control*, tj. ručně vybrat UTXO, které chcete utratit, přejděte na kartu "*UTXO*". Vyberte UTXO, které si přejete utratit, a poté klikněte na tlačítko "*Odeslat vybrané*". Budete automaticky přesměrováni na záložku "*Odeslat*" s již předvyplněnými UTXO.



![Image](assets/fr/37.webp)



Zadejte cílové číslo Address. Více adres lze přidat kliknutím na "*+ Add*".



![Image](assets/fr/38.webp)



Přidejte "*Label*", který popisuje účel tohoto výdaje, abyste mohli snadněji sledovat své transakce.



![Image](assets/fr/39.webp)



Zadejte částku, která má být odeslána na vybraný účet Address.



![Image](assets/fr/40.webp)



Upravte rychlost nabíjení podle aktuálních podmínek v síti. Pro výběr vhodné úrovně nabíjení nahlédněte například do [Mempool.space](https://Mempool.space/).



Po zaškrtnutí všech parametrů transakce klikněte na tlačítko "*Vytvořit transakci*".



![Image](assets/fr/41.webp)



Pokud jste se vším spokojeni, klikněte na "*Finalizovat transakci pro podpis*".



![Image](assets/fr/42.webp)



V dolní části obrazovky uvidíte, že Sparrow čeká na 2 podpisy. To je normální: zde použitý Wallet je Multisig 2-de-3.



![Image](assets/fr/43.webp)



Začínám se podepisovat kartou Coldcard. To provedu tak, že vložím kartu Micro SD do počítače a kliknu na "*Uložit transakci*".



![Image](assets/fr/44.webp)



Existují tři způsoby, jak přenést transakci, která má být podepsána, do zařízení Hardware Wallet a následně ji načíst ze služby Sparrow. Prvním je použití karty Micro SD, jak to uděláme zde pro kartu Coldcard. Druhý způsob je prostřednictvím kabelového připojení, který použijeme pro druhý podpis (Ledger a Trezor). A konečně je možné použít komunikaci pomocí QR kódu, a to u zařízení vybavených fotoaparátem, jako je Coldcard Q, Jade Plus nebo Passport V2.



Po uložení PSBT (*Partially Signed Bitcoin Transaction*) na Micro SD ji vložím do karty Coldcard MK3 a vyberu nabídku "*Připraveno k podpisu*".



![Image](assets/fr/45.webp)



Na obrazovce Hardware Wallet pečlivě zkontrolujte parametry transakce: číslo Address příjemce, odeslanou částku a poplatky. Po potvrzení transakce ji potvrďte a přejděte k podpisu.



![Image](assets/fr/46.webp)



Poté vraťte paměť Micro SD do počítače a klikněte na "*Načíst transakci*" v aplikaci Sparrow. Ze svých souborů vyberte PSBT podepsanou kartou Coldcard.



![Image](assets/fr/47.webp)



Vidíte, že byl přidán podpis Coldcard. Nyní použiji druhé zařízení, v tomto případě Ledger, k provedení druhého požadovaného podpisu. Připojím jej, odemknu a poté kliknu na tlačítko "*Podepsat*" v aplikaci Sparrow.



![Image](assets/fr/48.webp)



Klikněte na "*Podepsat*" vedle názvu Hardware Wallet.



![Image](assets/fr/49.webp)



Při prvním použití Ledger s tímto Multisig vás Sparrow požádá o ověření rozšířených veřejných klíčů (xpubs) spolupodepisujících osob. Stejně jako u karty Coldcard tento krok zabrání pozdějšímu podepisování naslepo. Chcete-li tyto informace ověřit, porovnejte xpub zobrazené na obrazovce Ledger s těmi, které poskytly přímo vaše ostatní hardwarové peněženky.



![Image](assets/fr/50.webp)



Zkontrolujte kód Address příjemce, převáděnou částku a poplatek za transakci a poté transakci podepište.



![Image](assets/fr/51.webp)



Stisknutím obrazovky se podepíšete.



![Image](assets/fr/52.webp)



Společnost Sparrow má nyní dva podpisy potřebné k uvolnění prostředků z portfolia Multisig. Naposledy zkontrolujte transakci, a pokud je vše v pořádku, klikněte na "*Vysílat transakci*", čímž ji odvysíláte po síti.



![Image](assets/fr/53.webp)



Tuto transakci najdete na kartě "*Transakce*" v programu Sparrow Wallet.



![Image](assets/fr/54.webp)



Gratulujeme, nyní víte, jak nastavit a používat vícepodpisový modul Wallet v aplikaci Sparrow. Pokud pro vás byl tento návod užitečný, budu vám vděčný, když níže zanecháte palec Green. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji za sdílení!



Chcete-li jít dále, doporučuji vám prostudovat tento návod na další metodu zvýšení zabezpečení vašeho zařízení Bitcoin Wallet, passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7