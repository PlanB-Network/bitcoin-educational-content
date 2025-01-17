---
name: BitBox02

description: Nastavení a používání BitBox02
---

![cover](assets/cover.webp)

BitBox02 (https://bitbox.swiss/) je švýcarská fyzická peněženka speciálně navržená pro zabezpečení vašich Bitcoinů. Mezi její klíčové vlastnosti patří snadné zálohování a obnovení pomocí microSD karty, minimalistický a diskrétní design a komplexní podpora pro Bitcoin.

![device](assets/1.webp)

Nabízí špičkové bezpečnostní řešení vyvinuté odborníky, včetně dvojčipového designu s bezpečnostním čipem. Její zdrojový kód byl plně auditován bezpečnostními výzkumníky a je zcela open-source. BitBox02 je dodáván s jednoduchou, avšak výkonnou aplikací BitBoxApp, která poskytuje bezpečnou správu vašich Bitcoinů. Podporuje plný uzel pro Bitcoin a zajišťuje šifrovanou komunikaci od konce ke konci mezi aplikací a zařízením. Vyrobeno ve Švýcarsku, BitBox02 si vysloužil pozitivní reputaci mezi svými uživateli.

![video](https://youtu.be/sB4b2PbYaj0)

> Specifikace
>
> - Připojení: USB-C
> - Kompatibilita: Windows 7 a novější, macOS 10.13 a novější, Linux, Android
> - Vstup: Kapacitní dotykové senzory
> - Mikrokontrolér: ATSAMD51J20A; 120 MHz 32-bit Cortex-M4F; Generátor náhodných čísel
> - Bezpečnostní čip: ATECC608B; Generátor náhodných čísel (NIST SP 800-90A/B/C)
> - Displej: 128 x 64 px bílý OLED
> - Materiál: Polycarbonát
> - Velikost: 54,5 x 25,4 x 9,6 mm včetně USB-C konektoru
> - Hmotnost: Zařízení 12g; s balením a příslušenstvím 160g

Stáhněte si datové listy na jejich webových stránkách https://bitbox.swiss/bitbox02/

## Jak používat hardwarovou peněženku BitBox02

### Nastavení BitBox02

BitBox02 má připojení USB-C připevněné k pouzdru. Pokud váš počítač používá standardní USB port, budete muset použít adaptér, který je součástí balení zařízení.

Připojte jej k počítači a zařízení se zapne (zatím to nedělejte).

Má senzory nahoře a dole a vyzve vás, abyste se dotkli horního nebo dolního senzoru, aby se obrazovka orientovala podle vašich představ.

![image](assets/2.webp)

### Stáhněte si aplikaci BitBox02

Navštivte https://shiftcrypto.ch/ a klikněte na odkaz „App“ nahoře, abyste se dostali na stránku ke stažení:

![image](assets/3.webp)

Klikněte na modré tlačítko Stáhnout:

![image](assets/4.webp)

Pro ověření stažení (přidává to složitost, ale doporučuje se, zejména pokud ukládáte hodně bitcoinů), viz Příloha A.

Po stažení můžete soubor rozbalit. Na Macu stačí dvakrát kliknout na stažený soubor a v adresáři stažených souborů se objeví ikona aplikace BitBox. Můžete ji přetáhnout na plochu (nebo kamkoli) pro snadný přístup.

Dvakrát klikněte na aplikaci, aby se spustila (není „instalována“).

Na Macu vám počítačová nápověda zobrazí varování. Ignorujte jej a klikněte na „otevřít“:

![image](assets/5.webp)

Poté uvidíte toto:

![image](assets/6.webp)

Pokračujte a připojte zařízení k počítači.

Zobrazí se vám párovací kód. Zkontrolujte, zda se shodují, a poté se dotkněte senzoru, abyste vybrali zaškrtávací značku. Poté se na obrazovce stane dostupným tlačítko pokračovat.

![image](assets/7.webp)
Poté budete mít možnost vytvořit nové seed nebo obnovit seed. Ukážu vám, jak vytvořit nový seed (Je důležité také obnovit seed, který jste vytvořili, abyste otestovali kvalitu vaší zálohy, než na peněženku naložíte jakékoli bitcoiny).
![image](assets/8.webp)

Zařízení bylo dodáno s microSD kartou. Pokud ji ještě nemáte vloženou, udělejte to.

![image](assets/9.webp)

Pojmenujte své zařízení a klikněte na pokračovat, poté potvrďte na zařízení.

![image](assets/10.webp)

Poté budete vyzváni k nastavení hesla pro zařízení. To není součástí vašeho seedu. To také není heslová fráze (ta je součástí vašeho seedu). Je to prostě heslo k zamčení zařízení. Když zařízení zapnete, budete vždy vyzváni k zadání tohoto hesla. Máte povoleno 10 po sobě jdoucích neúspěšných pokusů, než se zařízení samo vymaže ze všech pamětí, takže buďte opatrní. Animace na obrazovce vás naučí, jak používat ovládání zařízení k nastavení hesla.

![image](assets/11.webp)

Přečtěte si další obrazovku, zaškrtněte každé políčko a pokračujte.

![image](assets/12.webp)
![image](assets/13.webp)
![image](assets/14.webp)

A takhle peněženka vypadá, až je připravena k použití.

![image](assets/15.webp)

### NE TAK RYCHLE!!

Je to trochu zvláštní, ale BitBox02 nám říká, že zařízení je připraveno k použití, ale nevyzvalo nás k zapsání seed slov! JEDINOU zálohou, kterou máme, je soubor uložený na microSD kartě. To je nedostatečné. Tyto úložné zařízení nevydrží navěky (kvůli "bit rot"). Potřebujeme papírovou zálohu a její kopie, uložené v trezoru (jak je vysvětleno v obecném návodu k používání hardwarových peněženek)

Abyste získali svou seed frázi a zapsali ji, přejděte na záložku "spravovat zařízení" vlevo a poté klikněte na "zobrazit obnovovací slova"

![image](assets/16.webp)

Poté můžete projít potvrzením a zařízení vám představí slova. Pečlivě si je zapište a nikdy nikomu nedovolte, aby slova viděl.

![image](assets/17.webp)

Poté můžete kliknout na záložku Bitcoin vlevo, abyste získali své přijímací adresy.

![image](assets/18.webp)

Zobrazuje se jedna po druhé, ale alespoň vám to umožní vybrat, kterou adresu z prvních 20 použít:

![image](assets/19.webp)

Kliknutím na modré tlačítko se zobrazí celá adresa a budete vyzváni, abyste ověřili, že adresa odpovídá zobrazení na obrazovce. Je to dobrá praxe, abyste potvrdili, že žádný malware ve vašem počítači vás neklame k poslání bitcoinů na adresu útočníka.

![image](assets/20.webp)

Pokud chcete poslat bitcoiny do této peněženky, můžete adresu zkopírovat a vložit ji na stránku pro výběr na burze, kde máte své mince. Doporučuji poslat nejprve malé testovací množství, poté si vyzkoušet jeho utrácení zpět na burzu nebo na druhou adresu ve vaší peněžence.

Pro větší částky doporučuji vytvořit heslovou frázi (viz níže). Původní peněženka (bez heslové fráze) může být použita jako vaše návnadová peněženka (měla by obsahovat rozumné množství, aby byla věrohodná).

### Připojení k uzlu

BitBox02 se automaticky připojí k uzlu. Podívejme se, kam se připojuje. Klikněte na záložku nastavení vlevo a poté na "připojit vlastní úplný uzel".

![image](assets/21.webp)
A zde vidíme, že se to připojuje k uzlu společnosti shiftcrypto. Není to ideální. Vyzradili jsme jim všechny naše bitcoinové adresy a naši IP adresu (samozřejmě ne seed; mohou vidět naše adresy/zůstatky, ale nemohou je utratit). Na této stránce můžeme zadat údaje o vlastním uzlu (což přesahuje rámec tohoto konkrétního průvodce), nebo můžeme použít lepší software jako Sparrow Bitcoin Wallet, Electrum Desktop Wallet nebo Specter Desktop. Sparrow Bitcoin Wallet předvedu později v průvodci.
![obrázek](assets/22.webp)

Přidání heslové fráze

Nyní, když jsme zařízení nastavili s aplikací BitBox02 (a odhalili naše adresy, což je s tímto konkrétním hardwarovým peněženkou nevyhnutelné), můžeme k naší seed frázi přidat heslovou frázi. To nám umožní vytvořit novou peněženku pomocí stejného seedu a ShiftCrypto už nikdy neuvidí naše nové adresy. Tuto peněženku budeme připojovat pouze k našemu vlastnímu softwaru.

### Povolení heslové fráze

Nyní pokračujte a "povolte" funkci heslové fráze (ale zatím nenastavujeme heslovou frázi). Přejděte na kartu "spravovat zařízení" a klikněte na "povolit heslovou frázi" (červený kruh níže).

![obrázek](assets/23.webp)

Přečtěte si kroky...

![obrázek](assets/24.webp)
![obrázek](assets/25.webp)
![obrázek](assets/26.webp)

Nyní odpojte zařízení a vypněte aplikaci BitBox02

KONEC sekce bitbox02 od Parmana.

Vaše zařízení je nyní plně připraveno k použití na jakémkoli desktopovém řešení, jako je specter, sparrow a používání rozhraní bitbox.