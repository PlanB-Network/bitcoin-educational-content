---
name: COLDCARD Mk

description: Vytváření, zálohování a používání Bitcoinového soukromého klíče s zařízením Coldcard a Bitcoin Core
---

![obálka](assets/cover.webp)

Vytváření, zálohování a používání Bitcoinového soukromého klíče s zařízením Coldcard a Bitcoin Core

## Kompletní průvodce generováním soukromého klíče pomocí Coldcardu a jeho používáním prostřednictvím rozhraní vašeho uzlu Bitcoin Core!

V jádru využívání sítě Bitcoin leží koncept asymetrické kryptografie: pár klíčů - jeden soukromý a jeden veřejný - které šifrují a dešifrují data, koncept zajišťující důvěrnost komunikace.

V případě Bitcoinu, generováním takového páru soukromého a veřejného klíče, jsme schopni ukládat bitcoiny (UTXO nebo Nepoužitý Transakční Výstup) a podepisovat transakce k jejich utracení.

Dnes existuje mnoho nástrojů usnadňujících náhodné generování soukromého klíče a jeho zálohování v textové formě pomocí BIP 39 - standardu, který určuje, jak peněženky spojují mnemonickou frázi (seed phrase) s šifrovacími klíči. Často se mnemonická fráze skládá z 12 nebo 24 slov, která musí být bezpečně zálohována, aby bylo možné peněženku a její bitcoiny později obnovit.

V tomto článku se naučíme, jak generovat soukromý klíč pomocí Coldcardu Mk4, jednoho z nejrozšířenějších a nejbezpečnějších zařízení ve světě Bitcoinu, použitím metody hodu kostkou pro zajištění maximální entropie, a jak jej používat s Bitcoin Core v režimu bez připojení k síti!

> 🧰| Pro postup podle průvodce si připravte následující nástroje:
>
> - Zařízení Coldcard (Mk3 nebo Mk4)
> - MicroSD kartu (4GB stačí)
> - Napájecí magnetický USB kabel (mini-usb pro Mk3, usb-c pro Mk4)
> - Jednu nebo více kvalitních kostek

## Generování nové mnemonické fráze s Coldcardem

Začneme proces vytváření soukromého klíče od nuly, předpokládáme čerstvě rozbalený Coldcard, na kterém už byl nastaven PIN (postupujte podle kroků na Coldcardu během inicializace zařízení).

> 🚨 | Pro reset soukromého klíče již nakonfigurovaného Coldcardu postupujte podle těchto kroků:
> Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed> ✓
> _Pozor_: Coldcard po těchto krocích zapomene soukromý klíč. Ujistěte se, že jste správně zálohovali svou mnemonickou frázi, pokud ji chcete později obnovit.

## Krok za krokem:

Připojte se k Coldcardu s PINem > New Seed Words > 24 Word Dice Roll

Proveďte 100 hodů kostkou, zaznamenávejte výsledek získaný od 1 do 6 na Coldcardu po každém hodu. Tímto způsobem vytvoříte 256 bajtů entropie, čímž podpoříte vytvoření zcela náhodného soukromého klíče. Coinkite také poskytuje potřebnou dokumentaci pro nezávislou verifikaci jejich systému generování entropie.

![Vizuální snímek obrazovky Cold Card](assets/guide-agora/1.webp)

Jakmile dokončíte 100 hodů kostkou, stiskněte ✓ a poté si zapište získaných 24 slov v pořadí. Dvakrát ověřte a stiskněte ✓. Nakonec už zbývá jen dokončit ověřovací test 24 slov na Coldcardu, a voilà, váš nový soukromý klíč je vytvořen!

Dále si vyberte, zda aktivovat funkce NFC (Mk4) a USB podle zobrazených kroků. Až se ocitnete v hlavním menu, je nyní čas aktualizovat firmware zařízení. Přejděte na Advanced/Tools > Upgrade Firmware > Show Version a na oficiálních webových stránkách ověřte a stáhněte nejnovější dostupnou verzi. Aktualizace Coldcardu je doporučena pro zajištění maximální bezpečnosti.
Před pokračováním se doporučuje si poznamenat otisk hlavního klíče (Master Key Fingerprint, XFP) spojený s privátním klíčem. Tato data umožňují rychlou validaci, zda jste ve správné peněžence v případě obnovy, například. Přejděte na Pokročilé/Nástroje > Zobrazit identitu > Otisk hlavního klíče (XFP) a zapište si získanou sérii osmi alfanumerických znaků. XFP může být poznamenán na stejném místě jako mnemonická fráze, nejedná se o citlivá data.
> 💡 Doporučuje se otestovat zálohu vaší mnemonické fráze v jiném softwaru. Pro bezpečné provedení se poraďte s naším článkem Ověření zálohy Bitcoinové peněženky s Tails za méně než 5 minut.

## Bezpečnostní bonus: "Tajná fráze" (volitelné)

'Tajná fráze (passphrase) je skvělý prvek, který lze přidat do konfigurace peněženky, aby se zvýšila úroveň bezpečnosti a chránily vaše bitcoiny. Tajná fráze působí jako jakýsi 25. slovo k mnemonické frázi. Po přidání je vytvořena zcela nová peněženka spolu s privátním klíčem a přidruženou mnemonickou frází. Není nutné zapisovat novou mnemonickou frázi, protože k této peněžence lze přistupovat kombinací původní mnemonické fráze s vybranou tajnou frází.

Cílem je poznamenat si tajnou frázi odděleně od mnemonické fráze, protože útočník, který má přístup k oběma položkám, bude mít přístup k prostředkům. Na druhou stranu, útočník, který má přístup pouze k jedné z těchto položek, nebude mít přístup k prostředkům, a právě toto specifické výhoda optimalizuje úroveň bezpečnosti konfigurace peněženky.

![Přidání tajné fráze vede k úplně odlišné peněžence](assets/guide-agora/2.webp)

## Kroky pro přidání tajné fráze s Coldcard:

Tajná fráze > Přidat slova (doporučeno) > Použít. Zařízení zobrazí XFP nově vytvořené peněženky s tajnou frází, který by měl být zaznamenán spolu s tajnou frází z těch samých důvodů, které byly zmíněny dříve.

> 💡 Další zdroje související s tajnou frází:

    https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af
    https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/
    https://armantheparman.com/passphrase/

## Export peněženky do Bitcoin Core

Peněženka je nyní připravena k exportu do softwaru za účelem interakce s Bitcoinovou sítí. V tomto průvodci použijeme Bitcoin Core (v24.1).

Viz naše průvodce instalací a konfigurací pro Bitcoin Core:

> Spuštění vlastního uzlu s Bitcoin Core - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Konfigurace Tor pro uzel Bitcoin Core - https://agora256.com/configuration-tor-bitcoin-core/

Nejprve vložte micro SD kartu do Coldcard, poté exportujte peněženku pro Bitcoin Core následujícími kroky: Pokročilé/Nástroje > Export peněženky > Bitcoin Core. Na micro SD kartu budou zapsány dva soubory: bitcoin-core.sig & bitcoin-core.txt. Vložte micro SD kartu do počítače, kde je nainstalován Bitcoin Core, a otevřete soubor .txt. Uvidíte řádek "Pro peněženku s otiskem hlavního klíče." Ověřte, že osmimístný XFP odpovídá tomu, který jste si poznamenali při vytváření vašeho privátního klíče.
Před tím, než budete následovat pokyny v souboru, začněme přípravou peněženky v rozhraní Bitcoin Core následujícími kroky: přejděte na záložku Soubor > Vytvořit peněženku. Vyberte název pro vaši peněženku (výraz zaměnitelný s "porte-monnaie" v Core) a zaškrtněte možnosti Zakázat soukromé klíče, Vytvořit prázdnou peněženku a Popisovače peněženky, jak je ukázáno na obrázku níže. Poté stiskněte tlačítko Vytvořit.
![vytvořit peněženku](assets/guide-agora/3.webp)

Jakmile je peněženka vytvořena v Bitcoin Core, přejděte na záložku Okno > Konzola a ujistěte se, že vybraná peněženka na vrchu stránky zobrazuje název té, kterou jste vytvořili.

Nyní, v .txt souboru vygenerovaném dříve Coldcardem, zkopírujte řádek začínající s importdescriptors, poté jej vložte do konzoly Bitcoin Core. Měla by být vrácena odpověď obsahující řádek "success": true.

![okno uzlů](assets/guide-agora/4.webp)

Pokud odpověď obsahuje "message": "Ranged descriptors should not have a label", vymažte v zkopírovaném řádku z .txt souboru záznam "label": "Coldcard xxxx0000", poté celý řádek znovu vložte do konzoly Bitcoin Core.

Pomoc: [https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md)

## Ověření importu peněženky do Bitcoin Core

Abychom zajistili, že operace byla úspěšná, je nutné ověřit, že požadovaná peněženka byla importována do Bitcoin Core. Jednoduchý způsob, jak to potvrdit, je ověřit, že adresy generované v Coldcardu odpovídají adresám generovaným v Bitcoin Core.

Bitcoin Core: Přijmout > Vytvořit novou přijímací adresu
Coldcard: Prohlížeč adres > Vyberte adresu začínající na bc1q. Adresa Coldcardu 'bc1q' by měla odpovídat adrese zobrazené v Bitcoin Core.
Přijímání a odesílání transakcí v režimu 'air-gapped'

Přijetí transakce je extrémně jednoduché; stačí stisknout Přijmout, označit transakci (volitelné, ale doporučené) a Vytvořit novou přijímací adresu. Poté už jen stačí sdílet adresu s odesílatelem.

Nyní, klíčovým prvkem tohoto nastavení Coldcard + Bitcoin Core je odesílání transakcí bez toho, aby byl Coldcard a jeho soukromý klíč připojen k internetu, metodou nazývanou air-gapped, která využívá funkci TBSP (PSBT - Partially Signed Bitcoin Transactions) Bitcoinu.
V podstatě používáme rozhraní Bitcoin Core k sestavení transakce, kterou poté exportujeme prostřednictvím micro SD karty do Coldcardu k podpisu, a poté vrátíme podepsaný soubor transakce do Bitcoin Core a odesíláme transakci do sítě. Musíme to dělat tímto způsobem, protože peněženka importovaná do Bitcoin Core nemá soukromý klíč, pouze veřejný klíč (který nám umožňuje generovat naše přijímací adresy), takže je pro nás nemožné přímo v softwaru podepsat transakci k utracení našich bitcoinů.

Před pokračováním se ujistěte, že následující možnosti jsou povoleny v Nastavení > Peněženka:

> - Povolit funkce kontroly mincí
> - Utrácet nepotvrzené mince (Volitelné)
> - Povolit kontroly TBPS

![možnost](assets/guide-agora/5.webp)

### Kroky k odeslání v režimu air-gapped:
Odeslat > Vstupy > vyberte požadovaný utxo, poté zadejte adresu příjemce do pole Platba na. Poplatek za transakci: Vyberte... > Vlastní > Zadejte poplatek za transakci (Bitcoin Core počítá v sats/kilobajtu místo sat/byte jako většina alternativních řešení peněženek. Takže 4000 sats/kilobajt = 4 sats/byte). Vytvořte nepodepsanou transakci > uložte soubor na vaši micro SD kartu a vložte ji do Coldcardu.
V Coldcardu stiskněte Připraven k podpisu, ověřte detaily transakce, poté stiskněte ✓ a po vygenerování podepsaných souborů vložte micro SD kartu zpět do počítače.

Zpět v Bitcoin Core jděte na záložku Soubor > Načíst TBSP ze souboru a zadejte soubor podepsané transakce .psbt. Na obrazovce se objeví okno Operace PSBT, potvrzující, že transakce je plně podepsaná a připravena k odeslání. Nyní už zbývá jen stisknout Odeslat transakci.

![Operace PSBT](assets/guide-agora/6.webp)

### Závěr

Kombinace zařízení Coldcard s Bitcoin Core, na kterém provozujete vlastní uzel, je silná. K tomu přidejte soukromý klíč generovaný 100 hodmi kostkami a tajnou frázi, a vaše konfigurace peněženky se stane sofistikovanou a robustní pevností.

Neváhejte nás kontaktovat, abyste sdíleli své komentáře a otázky! Naším cílem je sdílet znalosti a den za dnem prohlubovat naše porozumění.