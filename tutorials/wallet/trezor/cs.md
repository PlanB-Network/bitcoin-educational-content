---
name: Trezor model One
description: Nastavení a používání Trezoru modelu One
---

![cover](assets/cover.webp)

Studená hardwarová peněženka – 60€ – Začátečník – Bezpečná pro částky mezi 2 000€ a 50 000€.

Jako studená fyzická peněženka je Trezor ideální pro začátek s Bitcoinem. Je snadno použitelný, není příliš drahý a je funkční.

Už jsme vytvořili tutoriály, jak jej používat:

1. Jeho nastavení
2. Obnova bitcoinů
3. Používání, odesílání a přijímání bitcoinů

Chtěli byste mít také svůj vlastní Trezor?
Můžete přispět k projektu kliknutím níže!

nastavení -https://www.youtube.com/watch?v=q-BlT6R4_bE

obnova: https://www.youtube.com/watch?v=3n4d4egjiFM

použití : https://www.youtube.com/watch?v=syouZjLC1zY

## průvodce psaním

průvodce navržený https://armantheparman.com/trezor/

## Nastavení Trezoru

Trezor je dodáván s vlastním mikro USB kabelem. Ujistěte se, že používáte tento a ne jen nějaký starý kabel, co máte po ruce. Některé USB kabely slouží pouze k napájení. Tento přenáší data I napájení. Pokud použijete zařízení s USB kabelem pro nabíjení telefonu, zařízení se nemusí spojit.

Připojte jej k počítači a zařízení se zapne. Objeví se zpráva, která říká „Přejděte na Trezor.io/start“. Udělejte to a stáhněte si Trezor Suite do svého počítače.

![image](assets/0.webp)

Klikněte na tlačítko ke stažení („Get Desktop App“)

![image](assets/1.webp)

Všimněte si odkazů na Podpis a Klíč pro podepisování. Pro ověření stažení (zkontrolujte, že vaše stažení nebylo manipulováno), existují další kroky, které jsou volitelné, pokud začínáte, ale POVINNÉ, pokud máte významné bohatství k zabezpečení. Instrukce k tomu jsou v Příloze A (konec průvodce)

Připojte Trezor k počítači pomocí mikro USB kabelu a nainstalujte a spusťte program. Takto to vypadá na Macu:

![image](assets/2.webp)

Po spuštění programu dostanete hloupé varování, prostě pokračujte:

![image](assets/3.webp)

Klikněte na Nastavit Trezor

![image](assets/4.webp)

Pokud je firmware zastaralý, dovolte Trezoru aktualizovat firmware.

Dále můžete vytvořit nové seed nebo obnovit peněženku z jiného zařízení se seedem, který již máte. Projdu si vytvoření nového seedu.

![image](assets/5.webp)

Klikněte na „Vytvořit novou peněženku“ – a potvrďte, že to chcete udělat na samotném zařízení kliknutím na tlačítko potvrzení.

Poté klikněte na jedinou možnost „Standardní záloha seedu“

![image](assets/6.webp)

Poté klikněte na „vytvořit zálohu“

![image](assets/7.webp)

Klikněte na tři zaškrtávací políčka, aby se zbarvila zeleně (samozřejmě si přečtěte každou zprávu), a poté klikněte na „začít zálohu“.

![image](assets/8.webp)

Dále uvidíte toto:

![image](assets/9.webp)

Váš Trezor vám zobrazí vaši mnemotechnickou frázi složenou z 12 slov. **Tato mnemotechnická fráze poskytuje plný a neomezený přístup ke všem vašim bitcoinům**. Každý, kdo tuto frázi získá, může vaše prostředky odcizit, i když nemá fyzický přístup k vašemu Trezoru. Tato 12slovná fráze umožňuje obnovit přístup k vašim bitcoinům v případě ztráty, krádeže nebo poškození vašeho hardwarového peněženky. Je proto velmi důležité ji pečlivě uložit a uchovávat na bezpečném místě.

Můžete ji zapsat na kartonový papír dodaný v balení, nebo pro vyšší bezpečnost doporučuji ji vyrýt na nerezový ocelový podklad, aby byla chráněna proti požárům, povodním nebo zřícení.

Pro více informací o správném způsobu zálohování a správy vaší mnemotechnické fráze vám důrazně doporučuji sledovat tento další návod, zejména pokud jste začátečník:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![image](assets/10.webp)

Následuje krok nastavení PIN kódu. PIN kód slouží k odemknutí vašeho Trezoru. Jedná se tedy o ochranu proti neoprávněnému fyzickému přístupu. Tento PIN kód však nehraje roli při odvozování kryptografických klíčů vaší peněženky. To znamená, že i bez přístupu k tomuto PIN kódu vám vlastnictví vaší mnemotechnické fráze složené z 12 nebo 24 slov umožní znovu získat přístup k vašim bitcoinům.

Doporučuje se zvolit co nejvíce náhodný PIN kód. Ujistěte se také, že tento PIN kód uložíte na jiné místo než váš Trezor (například v správci hesel).

Můžete si zvolit PIN kód až o 9 číslicích. Doporučuji, aby byl co nejdelší.


![image](assets/11.webp)
Máte možnost přidat do své peněženky shitcoiny – naléhavě vás žádám, abyste to nedělali, a šetřili pouze v Bitcoinu, jak vysvětluji zde (proč bitcoin) a zde (proč pouze bitcoin).
![image](assets/12.webp)

Pojmenujte svou peněženku a klikněte na „Přístup k Suite“:

![image](assets/13.webp)

Než budete pokračovat, můžete, pokud chcete, přidat passphrase BIP39. Passphrase BIP39 je volitelné heslo, které si můžete libovolně zvolit a které se přidává k vaší mnemotechnické frázi, aby se zvýšila bezpečnost vaší peněženky. S aktivovanou touto funkcí bude přístup k vaší Bitcoin peněžence vyžadovat jak mnemotechnickou frázi, tak passphrase. Bez jedné nebo druhé nebude možné peněženku obnovit.

Před nastavením této možnosti na vašem Trezoru se důrazně doporučuje přečíst si tento článek, abyste dobře pochopili teoretické fungování passphrase a předešli chybám, které by mohly vést ke ztrátě vašich bitcoinů:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Pro její aktivaci je třeba vybrat možnost „Hidden wallet“ a poznamenat si ji do příslušného pole. Pokaždé, když budete přistupovat ke své peněžence prostřednictvím Trezor Suite, bude vám položena otázka, zda chcete passphrase použít nebo ne.


![image](assets/14.webp)

Je také důležité dobře zálohovat tuto passphrase, stejně jako mnemotechnickou frázi. Její ztráta se rovná ztrátě přístupu k bitcoinům. Důrazně vám nedoporučuji spoléhat se pouze na zapamatování této passphrase, protože to neúměrně zvyšuje riziko její ztráty. Ideální je zapsat si ji na fyzický nosič (papír nebo kov) oddělený od mnemotechnické fráze. Tuto zálohu je samozřejmě nutné uložit na jiném místě než mnemotechnickou frázi, aby nebyly ohroženy současně.

Aby byla efektivní, musíte si vybrat silnou, náhodnou passphrase, která zahrnuje všechny typy znaků a je dostatečně dlouhá (jako silné heslo).


![image](assets/15.webp)

Líbí se mi, že se tomu říká „skrytá“ peněženka, protože to částečně vysvětluje, jak heslové fráze fungují.

Potvrďte heslovou frázi na zařízení.

Protože tato peněženka je prázdná, byl jsem požádán, abych potvrdil, že heslová fráze je správná:

![image](assets/16.webp)

Poté vás budou dotazovat, zda si přejete povolit označování. Něco, co jsem neprozkoumal, ale zní to jako způsob, jak můžete označovat své transakce a ukládat data do svého počítače nebo cloudu.

![image](assets/17.webp)

Nakonec bude vaše peněženka dostupná:

![image](assets/18.webp)

To, co máte na svém počítači, se nazývá „sledovací peněženka“, protože obsahuje vaše veřejné klíče (a adresy), ale ne vaše soukromé klíče. K utrácení (podepisováním transakcí soukromými klíči) potřebujete soukromé klíče. Způsob, jak to udělat, je připojením hardwarové peněženky. Smyslem hardwarové peněženky je, že transakce mohou být předávány tam a zpět mezi počítačem a Trezorem, podpis může být aplikován uvnitř Trezoru a soukromý klíč vždy zůstává uvnitř zařízení (pro ochranu proti počítačovým malware).

Trezor Suite je pro různé důvody špatná sledovací peněženka. Pro základní potřeby to stačí, ale pokud chcete pokročit, čtěte dál a naučte se, jak zařízení připojit k Sparrow Bitcoin Wallet.

## Sledovací peněženka

V předchozích článcích jsem vysvětlil, jak stáhnout a ověřit Sparrow Bitcoin Wallet a jak jej připojit k vlastnímu uzlu nebo veřejnému uzlu. Můžete postupovat podle těchto návodů:

- Nainstalujte Bitcoin Core
- Nainstalujte Sparrow Bitcoin Wallet
- Připojte Sparrow Bitcoin Wallet k Bitcoin Core

Alternativou k použití Sparrow Bitcoin Wallet je Electrum Desktop Wallet, ale budu pokračovat ve vysvětlování Sparrow Bitcoin Wallet, protože ho považuji za nejlepší pro většinu lidí. Pokročilí uživatelé mohou jako alternativu použít Electrum (viz můj návod).

Nyní Sparrow načteme a připojíme Trezor (s výchozí frází, ale nyní s heslovou frází). Tato peněženka nikdy nebyla vystavena Trezor Suite, protože bude vytvořena PO připojení zařízení k Trezor Suite. Ujistěte se, že ji k Trezor Suite nikdy znovu nepřipojíte, abyste nevystavili svou novou peněženku. (Můžete ji připojit bez heslové fráze, protože to může být vaše návnadová peněženka).

Vytvořte novou peněženku:

![image](assets/19.webp)

Pojmenujte ji nějak pěkně

![image](assets/20.webp)

Klikněte na „Připojená hardwarová peněženka“.

![image](assets/21.webp)

![image](assets/22.webp)
Klikněte na „Scan“ a poté na další obrazovce na „set passphrase“, abyste vytvořili zcela novou peněženku (použijte zcela novou heslovou frázi, například starou heslovou frázi s číslem na konci by to mělo fungovat). Poté „send passphrase“, poté to potvrďte na zařízení.
![image](assets/23.webp)

Poté klikněte na „import keystore“.

Na další obrazovce není co upravovat, Trezor to za vás vyplnil. Klikněte na „Apply“

![image](assets/24.webp)

Další obrazovka vám umožní přidat heslo. Nepřekládejte to s „passphrase“; mnoho lidí to udělá. Název je bohužel nešťastný. Heslo vám umožní zamknout tuto peněženku na vašem počítači. Je specifické pro tento software na tomto počítači. Není součástí vašeho soukromého klíče Bitcoinu.

Klikněte na „Apply“

![image](assets/25.webp)

Po pauze, kdy počítač přemýšlí, uvidíte, že tlačítka vlevo změní barvu z šedé na modrou. Gratulujeme, vaše peněženka je nyní připravena k použití. Provádějte a odesílejte transakce, jak jen chcete.

![image](assets/26.webp)

Přijímání

Chcete-li přijmout nějaké bitcoiny, přejděte na kartu Adresy vlevo a vyberte jednu z adres pro přijetí. Stačí kliknout pravým tlačítkem na adresu, kterou chcete, a vybrat „copy address“. Poté přejděte na burzu, odkud se peníze posílají, a vložte ji tam. Nebo můžete adresu poskytnout zákazníkovi, který ji může použít k zaplacení.

Při prvním použití peněženky byste měli přijmout velmi malou částku, zkuste ji utratit na jinou adresu, buď v rámci peněženky nebo zpět na burzu, abyste ověřili, že peněženka funguje podle očekávání.

Jakmile to uděláte, musíte zálohovat slova, která jste si zapsali. Jedna kopie nestačí. Mějte alespoň dvě papírové kopie (kov je lepší) a uchovávejte je na dvou různých, dobře zabezpečených místech. To snižuje riziko, že přírodní katastrofa zničí vaše HWW a papírovou zálohu v jednom incidentu. Viz „Používání hardwarových peněženek Bitcoin“ pro úplnou diskusi na toto téma.

## Odesílání

![image](assets/27.webp)

Při provádění platby musíte do pole „Pay to“ vložit adresu, na kterou platíte. Ve skutečnosti nemůžete pole Label nechat prázdné, je to jen pro záznamy vaší vlastní peněženky, ale Sparrow to nedovolí – stačí zadat cokoli (uvidí to jen vy). Zadejte částku a můžete také ručně upravit poplatek, který chcete.

Peněženka nemůže transakci podepsat, pokud není HWW připojeno. To je úkol HWW – přijmout transakci, podepsat ji a vrátit ji podepsanou. Ujistěte se, že když podepisujete na zařízení, vizuálně kontrolujete, že adresa, na kterou platíte, je stejná na zařízení a na obrazovce počítače, a fakturu, kterou obdržíte (např. jste mohli obdržet e-mail s platbou na určitou adresu).

Také si dejte pozor, pokud se rozhodnete použít minci, která je větší než částka platby, pak zbytek bude odeslán zpět na jednu z vašich adres pro změnu peněženky. Někteří lidé to nevěděli a vyhledali svou transakci na veřejném blockchainu a mysleli si, že nějaké bitcoiny byly odeslány na adresu útočníka, ale ve skutečnosti to byla jejich vlastní adresa pro změnu.
Firmware

Pro aktualizaci firmware potřebujete připojit k Trezor Suite. Pokud to chcete udělat, ujistěte se, že máte k dispozici záložní slova a heslovou frázi pro obnovení zařízení, pro případ, že by se zařízení resetovalo.
Závěr
Tento článek vám ukázal, jak používat Trezor HWW bezpečněji a soukroměji, než je inzerováno – ale tento článek sám o sobě není dostatečný. Jak jsem řekl na začátku, měli byste jej kombinovat s informacemi poskytnutými v "Používání Bitcoin Hardware Peněženek".

## Příloha A - Ověření stažení softwaru

![obrázek](assets/28 .webp)

Stáhněte si Podpis (textový soubor) a Klíč pro podepisování (textový soubor) a zaznamenejte si názvy souborů a místo, kam jste soubor stáhli.

Dále pro Mac budete potřebovat stáhnout GPG Suite (viz instrukce zde).

Pro Windows budete potřebovat GPG4win (viz instrukce zde).

Pro Linux je GPG již součástí každého balíčku. Pokud jej nemáte, získejte jej příkazem: sudo apt-get install gpg

Dále pro Mac/Windows nebo Linux otevřete terminál a zadejte příkaz:

```bash
gpg –import XXXXXXXXXX
```

kde XXXXXXXXXX je úplná cesta k souboru s klíčem pro podepisování (úplná cesta znamená adresář a název souboru, kde se soubor nachází). Měli byste vidět potvrzení o úspěšném importu klíče.

Poté

```bash
gpg –verify ZZZZZZZZZZ WWWWWWWWWW
```

kde ZZZZZZZZZZ je úplná cesta k souboru s podpisem a WWWWWWWWWW je úplná cesta k programu Trezor Suite, který jste stáhli.

Měli byste vidět zprávu „Good signature from SatoshiLabs“ někde ve výstupu. Na konci je varování, které je bezpečné ignorovat.