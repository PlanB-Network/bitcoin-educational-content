---
name: Seed Signer

description: Nastavení vašeho Seed signeru
---

![cover](assets/cover.webp)

## Materiál:

1. Raspberry Pi Zero (verze 1.3)

Raspberry Pi Zero

Pro úplně izolované řešení se ujistěte, že používáte verzi 1.3 bez možnosti WiFi nebo Bluetooth, ale jakýkoliv model Raspberry Pi 2/3/4 nebo Zero bude fungovat.

Poznámka: Raspberry Pi obvykle nepřichází s připojenými piny; piny buď musí být připájeny, nebo lze použít něco, co se nazývá "GPIO Hammer".
GPIO Hammer

Pokud vaše pájení není úplně na úrovni, nebo ještě nemáte páječku, pak můžete jako alternativu k pájení použít "GPIO Hammer".

2. Chapeau LCD WaveShare 1,3 palce s rozlišením 240 × 240 pixelů

WaveShare LCD Hat

Waveshare 1.3″ 240×240 px LCD

Poznámka: Vyberte si Waveshare displej pečlivě; ujistěte se, že kupujete model s rozlišením 240×240 pixelů.
více informací

3. Modul kamery kompatibilní s Pi Zero

Raspberry Pi Camera

Aokin / AuviPal 5MP 1080p s video kamerovým modulem OV5647 Sensor; ostatní značky s modulem senzoru OV5647 by také měly fungovat, ale nemusí být kompatibilní s pouzdrem Orange Pill.

Poznámka: Budete potřebovat kabel kamerové pásky specificky kompatibilní s Raspberry Pi Zero.

4. MicroSD karta s kapacitou alespoň 4 GB

rozsáhlé zdroje: https://seedsigner.com/explainers/

## Software:

Instalace softwaru

1. Stáhněte si nejnovější soubor “seedsigner_x_x_x.img.zip”
   nejnovější verze

2. Rozbalte soubor “seedsigner_x_x_x.img.zip”

3. Použijte Balena Etcher nebo podobný nástroj k zápisu rozbaleného .img souboru na microsd kartu
   BALENA ETCHER

4. Instalujte microsd kartu do SeedSigneru.
   Veřejný klíč SeedSigneru GPG
   seedsigner_pubkey.gpg

## Video tutoriál

_návod převzat od Southerbitcoiner, vytvořil Cole_

### Sbírka video návodů pokrývající SeedSigner: open source, DIY Hardware Wallet/Signing zařízení

![image](assets/1.webp)

SeedSigner je Bitcoin Signing Device, který si můžete postavit od nuly. Zní to obtížně, ale tato čtyřdílná série by vám měla pomoci :) Doporučuji sledovat část 1 a 2, poté se rozhodněte, zda chcete použít desktop (sledujte část 3) nebo mobilní zařízení (sledujte část 4).

Vše, co potřebujete vědět, bude níže. Další užitečné odkazy zahrnují webové stránky SeedSigneru, jejich Github, Keybase, nejnovější verzi a požadavky na hardware.

### Část 1: Jak postavit SeedSigner:

V tomto videu vám ukážu, jak stáhnout a ověřit software SeedSigner, jaké díly jsou potřebné a jak sestavit váš SeedSigner.

![video](https://youtu.be/mGmNKYOXtxY)

### Část 2: Testování vašeho SeedSigneru
Předtím, než jsem začal používat svůj SeedSigner, provedl jsem několik testů, abych se ujistil, že nedělá nic škodlivého. Myslel jsem, že bych se o tento krok také podělil. Zde je návod, jak ověřit, že váš SeedSigner exportuje správnou peněženku (xpub), jak ověřit matematiku házení kostkami SeedSigneru a jak ověřit dětská semena bip-85 od SeedSigneru.
![video](https://youtu.be/34W1IyTyXZE)

### Část 3: Jak používat SeedSigner se Sparrow Wallet (desktop)

SeedSigner je schopen generovat semena a podepisovat bitcoinové transakce. Sám o sobě však není schopen sestavovat transakce. Potřebujete použít "koordinátor" peněženky se svým SeedSignerem. Takto můžete použít Sparrow Wallet se svým SeedSignerem:

![video](https://youtu.be/IQb8dh-VTOg)

Část 4: Jak používat SeedSigner s Blue Wallet (mobilní)

SeedSigner je schopen generovat semena a podepisovat bitcoinové transakce. Sám o sobě však není schopen vytvářet transakce. Potřebujete použít "koordinátor" peněženky se svým SeedSignerem. Takto můžete použít Blue Wallet se svým SeedSignerem:

![video](https://youtu.be/x0Ee35Ct0r4)

To jsou zatím všechny návody pro SeedSigner! Dejte mi vědět, pokud si myslíte, že mi něco chybí. Tyto mám na seznamu pro potenciální videa:

> Celková recenze SeedSigneru. Je to dobrá volba pro zařízení pro podepisování? Klady/zápory?

> Jak používat Bip-85 se SeedSignerem
> Jak být strýcem Jimem se SeedSignerem

Považujete tyto informace za cenné? Zvažte poslání spropitného, abyste pomohli financovat budoucí videa:
https://www.southernbitcoiner.com/donate/