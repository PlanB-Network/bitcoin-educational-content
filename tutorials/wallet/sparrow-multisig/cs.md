---
name: Sparrow Wallet - Multisig
description: Vytvoření peněženky s více podpisy v Sparrow
---
![cover](assets/cover.webp)


Peněženka s více podpisy (často nazývaná "*Multisig*") je struktura bitcoinové peněženky, která k autorizaci výdaje vyžaduje několik kryptografických podpisů z různých klíčů. Na rozdíl od běžné peněženky ("*singlesig*"), kde k odemčení UTXO stačí jediný soukromý klíč, staví Multisig na modelu **m-of-n**: z _n_ klíčů přiřazených k peněžence musí každou transakci nutně spolupodepsat _m_ klíčů.


Tento mechanismus umožňuje sdílet kontrolu nad peněženkou mezi několika subjekty nebo zařízeními. Například v konfiguraci 2-of-3 se vygenerují tři nezávislé sady klíčů, ale k uvolnění prostředků stačí jen dvě. Tato architektura výrazně snižuje rizika spojená s kompromitací nebo ztrátou klíče: zloděj, který získá přístup k jedinému klíči, peněženku nevyprázdní, a uživatel, který o jeden klíč přijde, se ke svým prostředkům stále dostane pomocí zbývajících dvou.


![Image](assets/fr/01.webp)


Tato vyšší bezpečnost s sebou ale nese větší složitost. Nastavení peněženky Multisig vyžaduje zabezpečit několik mnemotechnických frází (jednu na každý podpisový faktor) a rozšířené veřejné klíče ("*xpub*"). Pokud totiž používáte peněženku Multisig 2-of-3, musíte pro její obnovení mít buď všechny tři mnemotechnické fráze, nebo alespoň dvě ze tří. Pokud však máte jen dvě fráze ze tří, potřebujete navíc přístup ke třem *xpub*, bez nichž nebude možné získat veřejné klíče nutné pro přístup k bitcoinům, které chrání.


Shrnuto, pro obnovení peněženky Multisig musíte:


- Buď mít přístup ke všem mnemotechnickým frázím spojeným s jednotlivými podpisovými faktory;
- Nebo mít minimální počet mnemotechnických frází vyžadovaný prahem pro podpis a zároveň mít přístup k xpub všech faktorů, abyste získali potřebné veřejné klíče.


![Image](assets/fr/02.webp)


Správu záloh peněženek Multisig usnadňují *Output Script Descriptors*, které sdružují všechna veřejná data potřebná pro přístup k prostředkům. Tato funkce však zatím není implementována ve všech programech pro správu peněženek.


Multisig se hodí zejména bitcoinářům, kteří hledají vyšší bezpečnost nebo kolektivní správu prostředků: firmám, spolkům, rodinám nebo jednotlivcům držícím významné množství bitcoinů. Umožňuje vytvářet decentralizovaná schémata správy, například rozdělit podpisovou pravomoc mezi několik vedoucích pracovníků nebo členů týmu.


V tomto návodu se naučíme vytvořit a používat klasickou peněženku s více podpisy pomocí **Sparrow Wallet**. Pokud chcete vytvořit peněženku s více podpisy na míru s časovými zámky, doporučuji místo toho použít Lianu:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Předpoklady


V tomto návodu vám ukážu, jak vytvořit Multisig pomocí [softwaru pro správu peněženek Sparrow Wallet](https://sparrowwallet.com/download/). Pokud tento software ještě nemáte nainstalovaný, udělejte to nyní. Pokud potřebujete pomoc, máme také podrobný návod na konfiguraci Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Pro nastavení peněženky s více podpisy budete potřebovat různé hardwarové peněženky. Například pro Multisig 2-of-3 byste mohli použít:


- Trezor Model One;
- Ledger Flex;
- Passport Core.


![Image](assets/fr/03.webp)


V konfiguraci Multisig je dobré použít hardwarové peněženky různých značek. Zajistíte tím, že pokud se u konkrétního modelu objeví vážný problém, neohrozí to celkovou bezpečnost vašeho Multisigu. Navíc tak využijete specifických výhod každého zařízení. Například v mé konfiguraci:



- Trezor Model One je zcela open-source, což umožňuje ověřit generování seedu. Protože však není vybaven prvkem Secure Element, zůstává zranitelný vůči fyzickým útokům;



- Ledger Flex naproti tomu používá neověřitelný proprietární firmware, ale obsahuje Secure Element, který nabízí vynikající fyzickou ochranu;



- Passport Core kombinuje plně open-source firmware, Secure Element a air-gapped výměnu dat pomocí QR kódů. Je nezávislým třetím podepisujícím zařízením, které dokáže ověřovat adresy a podepisovat PSBT bez datového připojení přes USB.


Než začnete konfigurovat peněženku Multisig, ujistěte se, že je každá hardwarová peněženka správně nastavena (vygenerování a záloha mnemotechnické fráze, nastavení PINu). Podrobné pokyny najdete v našich návodech ke každé hardwarové peněžence, například:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Jak uvidíme dále v tomto návodu, do konfigurace Multisig lze zapojit i faktor, který není spojen s hardwarovou peněženkou, ale jehož soukromé klíče jsou uloženy ve vašem počítači. Tento postup je pochopitelně méně bezpečný než výhradní použití hardwarových peněženek, ale v některých případech může dávat smysl. Například u Multisig 2-of-3 byste mohli zvolit dvě hardwarové peněženky a jednu softwarovou peněženku.

> ⚠️ **Bezpečnostní upozornění ke Coldcard MK3:** nevytvářejte nový seed na zařízení MK3 s firmwarem starším než 4.2.0. Seedy vygenerované na starším firmwaru je nutné nahradit a prostředky přesunout. Tento návod proto používá jako referenční air-gapped podpisové zařízení Passport Core.


## Vytvoření peněženky Multisig


Otevřete Sparrow Wallet, klikněte na kartu "*File*" a poté vyberte "*New Wallet*".


![Image](assets/fr/04.webp)


Pojmenujte svou peněženku s více podpisy a potvrďte kliknutím na "*Create Wallet*".


![Image](assets/fr/05.webp)


V rozbalovací nabídce "*Policy Type*" vyberte možnost "*Multi Signature*".


![Image](assets/fr/06.webp)


Vpravo nahoře nyní můžete určit celkový počet klíčů ve svém Multisigu a také počet spolupodepisujících, kteří jsou potřeba k autorizaci výdaje. V mém příkladu jde o schéma 2-of-3.


![Image](assets/fr/07.webp)


Ve spodní části okna zobrazuje Sparrow Wallet tři "*Keystore*". Každý představuje jednu sadu klíčů. Zde používám tři hardwarové peněženky, takže každý "*Keystore*" odpovídá jedné z nich. Nyní je nakonfigurujeme.


Začnu s Passport Core. Na kartě "*Keystore 1*" vyberu možnost "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Na Passportu otevřete účet, který chcete použít, a vyberte "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport zobrazí animovaný QR kód s informacemi o svém veřejném klíči.

V Sparrow vyberte "*Scan...*" vedle "*Passport*" a naskenujte tento animovaný QR kód webkamerou počítače. Porovnejte otisk hlavního klíče zobrazený v Sparrow s otiskem na displeji Passportu a poté keystore importujte.

Xpub vašeho Passportu je nyní importován. Zopakujte odpovídající postup pro Ledger Flex a Trezor Model One.


U Ledger Flex vyberu "*Keystore 2*" a poté kliknu na "*Connected Hardware Wallet*". Ujistěte se, že je Ledger připojen k počítači, odemčen a že je v něm otevřená aplikace Bitcoin.


![Image](assets/fr/15.webp)


Poté klikněte na tlačítko "*Scan...*".


![Image](assets/fr/16.webp)


Vedle názvu své hardwarové peněženky klikněte na "*Import Keystore*".


![Image](assets/fr/17.webp)


Druhý podepisující je nyní v Sparrow Wallet správně zaregistrován.


![Image](assets/fr/18.webp)


Přesně stejný postup zopakuji s Trezorem One a dokončím tak konfiguraci Multisigu.


![Image](assets/fr/19.webp)


V mé konfiguraci tento případ neřešíme, ale pokud chcete do svého Multisigu zahrnout podpis přes softwarovou peněženku v Sparrow (hot wallet), stačí kliknout na tlačítko "*New or Imported Software Wallet*".


Nyní, když jsou všechna vaše podpisová zařízení importována do Sparrow Wallet, můžete dokončit vytvoření Multisigu kliknutím na "*Apply*".


![Image](assets/fr/20.webp)


Zvolte silné heslo, které zabezpečí přístup k vaší peněžence v Sparrow Wallet. Toto heslo chrání vaše veřejné klíče, adresy, štítky a historii transakcí před neoprávněným přístupem.


Nezapomeňte si toto heslo uložit na bezpečné místo, například do správce hesel, abyste o něj nepřišli.


![Image](assets/fr/21.webp)


## Zálohování peněženky Multisig


Nyní uložíme *Output Script Descriptor* na nezávislé médium a vytvoříme z něj několik kopií.


*Deskriptor* obsahuje všechny xpub vaší peněženky Multisig a také odvozovací cesty použité pro generování klíčů. Vzpomeňte si na to, co jsme viděli v první části: pro obnovení peněženky Multisig musíte mít buď **všechny** mnemotechnické fráze, nebo jen minimální počet potřebný k dosažení podpisového prahu. V druhém případě je však nezbytné mít také **xpub** chybějících podepisujících. *Deskriptor* obsahuje všechny xpub vašeho Multisigu.


Pokud to není jasné, zapamatujte si jen toto: k obnovení Multisigu potřebujete minimální počet mnemotechnických frází jednotlivých použitých hardwarových peněženek podle prahu (v mém případě 2 fráze) a k tomu *Deskriptor*.


Tento *Deskriptor* neobsahuje žádné soukromé klíče, pouze veřejné. Neumožňuje tedy přístup k prostředkům. Není proto tak kritický jako mnemotechnické fráze, které dávají plný přístup k vašim bitcoinům. Riziko spojené s *Deskriptorem* se týká výhradně soukromí: pokud unikne, třetí strana by mohla sledovat všechny vaše transakce, ale nemohla by vaše prostředky utratit.


Důrazně doporučuji vytvořit si několik kopií tohoto *Deskriptoru* a uchovávat je u každého podpisového zařízení svého Multisigu. Já například *Deskriptor* vytisknu na papír a jednu kopii uložím k Passportu, druhou k Trezoru a třetí k Ledgeru. Tentýž *Deskriptor* si také uložím jako soubor PDF na tři USB klíče, z nichž každý je uložen u jedné z hardwarových peněženek. Maximalizuji tím šanci, že o *Deskriptor* nikdy nepřijdu, a mám jistotu, že u každého zařízení mám dvě kopie (jednu fyzickou a jednu digitální).


Jakmile je vaše peněženka Multisig vytvořena, Sparrow vám tento *Deskriptor* automaticky nabídne. Kliknutím na tlačítko "*Save PDF...*" jej uložíte v textové podobě i jako QR kód.


![Image](assets/fr/22.webp)


Toto PDF pak můžete vytisknout a zkopírovat na své USB klíče.


![Image](assets/fr/23.webp)


Passport používá konfiguraci multisig importovanou ze Sparrow k zobrazení a ověření příslušných informací o klíčích během párování a podepisování pomocí QR kódů. *Deskriptor* si uchovávejte nezávisle na tom: zůstává nezbytný pro obnovení peněženky, pokud jedno z podpisových zařízení není k dispozici.


Kromě zálohy *Deskriptoru* nezapomeňte věnovat zvláštní pozornost zálohování mnemotechnických frází každého z vašich podpisových zařízení. Pokud s tím teprve začínáte, vřele doporučuji přečíst si tento další návod, abyste se naučili je správně zálohovat a spravovat:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Než na svůj Multisig přijmete první bitcoiny, **důrazně doporučuji provést test obnovy naprázdno**. Poznamenejte si referenční údaje, například první přijímací adresu, a poté své hardwarové peněženky resetujte, dokud je peněženka ještě prázdná. Následně zkuste peněženku Multisig obnovit na hardwarových peněženkách pomocí papírových záloh mnemotechnických frází a poté v Sparrow pomocí *Deskriptoru*. Zkontrolujte, že první adresa vygenerovaná po obnovení odpovídá té, kterou jste si původně zapsali. Pokud ano, můžete si být jisti, že jsou vaše papírové zálohy spolehlivé.


Chcete-li se dozvědět více o tom, jak provést test obnovy, doporučuji přečíst si tento další návod:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Příjem bitcoinů na váš Multisig


Vaše peněženka je nyní připravena přijímat bitcoiny. V Sparrow klikněte na kartu "*Receive*".


![Image](assets/fr/30.webp)


Než použijete adresu vygenerovanou v Sparrow Wallet, věnujte čas její kontrole přímo na displeji svých hardwarových peněženek. Ověříte tak, že adresa nebyla pozměněna a že vaše zařízení skutečně drží soukromé klíče potřebné k utracení souvisejících prostředků. To vás chrání před řadou vektorů útoku.


Klikněte proto na "*Display Address*", aby se adresa zobrazila na vašem Trezoru nebo Ledgeru připojeném kabelem.


![Image](assets/fr/31.webp)


U Passportu vyberte účet multisig a zvolte "*Verify Address*". Naskenujte QR kód přijímací adresy zobrazený v Sparrow. Passport na svém displeji potvrdí, zda adresa patří k peněžence multisig.


Zkontrolujte, že adresa zobrazená na každé hardwarové peněžence přesně odpovídá té v Sparrow Wallet. Je vhodné to udělat těsně před sdílením adresy s plátcem, abyste měli jistotu její integrity.


Této adrese pak můžete přiřadit "*Label*", který označí původ přijatých bitcoinů. Je to dobrý způsob, jak si zorganizovat správu svých UTXO.


![Image](assets/fr/34.webp)


Jakmile je to ověřeno, můžete adresu použít k příjmu bitcoinů.


![Image](assets/fr/35.webp)


## Odesílání bitcoinů z vašeho Multisigu


Teď, když jste na svou peněženku Multisig přijali první satoši, můžete je také utratit! V Sparrow přejděte na kartu "*Send*" a sestavte novou transakci.


![Image](assets/fr/36.webp)


Pokud chcete použít *Coin Control*, tedy ručně vybrat UTXO, která chcete utratit, přejděte na kartu "*UTXOs*". Vyberte UTXO, která chcete utratit, a klikněte na "*Send Selected*". Budete automaticky přesměrováni na kartu "*Send*" s již předvyplněnými UTXO.


![Image](assets/fr/37.webp)


Zadejte cílovou adresu. Kliknutím na "*+ Add*" lze přidat více adres.


![Image](assets/fr/38.webp)


Přidejte "*Label*", který popíše účel tohoto výdaje, abyste své transakce mohli snadněji sledovat.


![Image](assets/fr/39.webp)


Zadejte částku, která se má na vybranou adresu odeslat.


![Image](assets/fr/40.webp)


Upravte sazbu poplatků podle aktuálního stavu sítě. Vhodnou výši poplatku můžete zvolit například podle [Mempool.space](https://Mempool.space/).


Po kontrole všech parametrů transakce klikněte na "*Create Transaction*".


![Image](assets/fr/41.webp)


Pokud je vše v pořádku, klikněte na "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


V dolní části obrazovky uvidíte, že Sparrow čeká na 2 podpisy. To je normální: použitá peněženka je Multisig 2-of-3.


![Image](assets/fr/43.webp)


Podepisování začnu svým Passportem. V Sparrow klikněte na "*Show QR*", aby se PSBT (*Partially Signed Bitcoin Transaction*) zobrazila jako animované QR kódy. Na Passportu vyberte účet multisig, zvolte "*Sign with QR Code*" a naskenujte QR kód zobrazený v Sparrow.


Na displeji hardwarové peněženky pečlivě zkontrolujte parametry transakce: adresu příjemce, odesílanou částku a poplatky. Jakmile transakci ověříte, potvrďte ji a přejděte k podpisu.


Po schválení transakce zobrazí Passport podepsanou PSBT jako animované QR kódy. V Sparrow klikněte na "*Scan QR*" a naskenujte tyto kódy webkamerou. Podpis Passportu se tím přidá. Pro druhý požadovaný podpis nyní použiji Ledger: připojím jej, odemknu a v Sparrow kliknu na "*Sign*".


![Image](assets/fr/48.webp)


Klikněte na "*Sign*" vedle názvu své hardwarové peněženky.


![Image](assets/fr/49.webp)


Při prvním použití Ledgeru s tímto Multisigem vás Sparrow vyzve k ověření rozšířených veřejných klíčů (xpub) spolupodepisujících. Stejně jako u Passportu vám tento krok zabrání v tom, abyste později podepisovali naslepo. Pro ověření těchto údajů porovnejte xpub zobrazený na displeji Ledgeru s těmi, které vám přímo poskytnou ostatní hardwarové peněženky.


![Image](assets/fr/50.webp)


Zkontrolujte adresu příjemce, převáděnou částku a poplatek za transakci a poté transakci podepište.


![Image](assets/fr/51.webp)


Stisknutím displeje transakci podepíšete.


![Image](assets/fr/52.webp)


Sparrow nyní má oba podpisy potřebné k uvolnění prostředků z peněženky Multisig. Zkontrolujte transakci naposledy, a pokud je vše v pořádku, klikněte na "*Broadcast Transaction*" a odešlete ji do sítě.


![Image](assets/fr/53.webp)


Tuto transakci najdete v Sparrow Wallet na kartě "*Transactions*".


![Image](assets/fr/54.webp)


Gratulujeme, nyní víte, jak v Sparrow nastavit a používat peněženku s více podpisy. Pokud vám byl tento návod užitečný, budu rád, když níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Díky za sdílení!


Pokud chcete jít dál, doporučuji vám tento návod na další metodu zvýšení bezpečnosti vaší bitcoinové peněženky – passphrase BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
