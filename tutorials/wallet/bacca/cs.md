---
name: Bacca
description: Konfigurace účetní knihy bez softwaru Ledger Live
---
![cover](assets/cover.webp)

Pokud používáte Ledger, pravděpodobně jste zjistili, že musíte projít softwarem Ledger Live, alespoň pro počáteční konfiguraci zařízení, zkontrolovat jeho pravost a nainstalovat do něj aplikaci Bitcoin. Po této konfiguraci však mnoho bitcoinářů raději používá specializovaný software pro správu bitcoinových peněženek, jako je Sparrow nebo Liana, než Ledger Live. Ačkoli Ledger vyrábí vynikající hardwarové peněženky, které rychle zahrnují nejnovější funkce Bitcoinu, jejich software nemusí být nutně přizpůsoben specifickým potřebám bitcoinářů. Ledger Live totiž obsahuje mnoho funkcí určených pro altcoiny, zatímco možnosti určené pro správu bitcoinových peněženek jsou omezené. Problémem Sparrow a Liana (prozatím) je však to, že neumožňují nainstalovat aplikaci pro Bitcoin na Ledger.

Chcete-li se vyhnout nutnosti používat službu Ledger Live při počáteční konfiguraci systému Ledger, můžete použít nástroj Bacca (nebo "Instalátor systému Ledger"). Tento software umožňuje nainstalovat a aktualizovat aplikaci Bitcoin, ověřit pravost Ledgeru a dokonce později aktualizovat firmware zařízení. Bacca vytvořil Antoine Poinsot (Darosior), vývojář Bitcoin Core v Chaincode Labs, spoluzakladatel [Revault a Liana](https://wizardsardine.com/) a Pythcoiner.

V tomto návodu vám ukážu, jak tento nástroj používat, abyste se mohli nadobro obejít bez softwaru Ledger Live a přitom si užívat zařízení Ledger. Funguje na všech zařízeních: Nano S Classic, Nano S Plus, Nano X, Flex a Stax.

---
*Upozorňujeme, že tento nástroj je poměrně nový a jeho vývojáři uvádějí, že je stále **ve fázi testování**. Doporučují jej používat pouze pro testovací účely, nikoliv pro zařízení určené k umístění skutečné peněženky Bitcoin, i když je to možné. V tomto ohledu doporučuji řídit se doporučeními vývojářů tohoto nástroje, která jsou uvedena [v README jejich repozitáře GitHub](https://github.com/darosior/ledger_installer).*

---
## Předpoklady

V počítači potřebujete dva nástroje, abyste mohli používat aplikaci Bacca:


- Git ;
- Rez.

Pokud jste je již nainstalovali, můžete tento krok přeskočit.

**Linux:**

V distribucích Linuxu je systém Git obvykle předinstalován. Chcete-li zkontrolovat, zda je Git ve vašem systému nainstalován, můžete v terminálu zadat následující příkaz :

```bash
git --version
```

Pokud nemáte v systému nainstalovaný systém Git, zde je příkaz pro jeho instalaci v systému Debian :

```bash
sudo apt install git
```

Chcete-li nainstalovat vývojové prostředí Rust, použijte příkaz :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Okna:**

Chcete-li nainstalovat systém Git, přejděte na [oficiální webové stránky projektu](https://git-scm.com/). Stáhněte si software a postupujte podle pokynů k instalaci.

![BACCA](assets/fr/01.webp)

Stejným způsobem postupujte při instalaci Rustu z [oficiální webové stránky](https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

Pokud systém Git ještě není nainstalován, otevřete terminál a spusťte následující příkaz pro jeho instalaci:

```bash
git --version
```

Pokud v systému nemáte nainstalovaný systém Git, otevře se okno s nabídkou instalace aplikace Xcode, která obsahuje systém Git. Jednoduše postupujte podle pokynů na obrazovce a pokračujte v instalaci.

Chcete-li nainstalovat program Rust, spusťte následující příkaz:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Instalace Bacca

Otevřete terminál, přejděte do složky, kam chcete software uložit, a spusťte následující příkaz:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Přejděte do adresáře softwaru:

```bash
cd ledger_installer
```

Poté pomocí nástroje Cargo zkompilujte projekt a spusťte grafické uživatelské rozhraní Bacca:

```bash
cargo run -p ledger_manager_gui
```

Nyní máte přístup k rozhraní softwaru.

![BACCA](assets/fr/03.webp)

## Konfigurace účetní knihy

Pokud je váš Ledger nový, ujistěte se, že jste nastavili kód PIN a uložili frázi pro obnovení. Pro tyto úvodní kroky nepotřebujete Ledger Live. Jednoduše připojte Ledger přes USB kabel a napájejte jej. Pokud si nejste jisti, jak postupovat v těchto dvou krocích, můžete se podívat na začátek návodu specifického pro váš model:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Použití Bacca

Připojte Ledger k počítači a odemkněte jej pomocí nastaveného kódu PIN. Bacca by měla automaticky detekovat váš Ledger.

![BACCA](assets/fr/04.webp)

Chcete-li potvrdit pravost své účetní knihy, klikněte na tlačítko "*Zkontrolovat*". Abyste mohli pokračovat, je třeba autorizovat připojení na zařízení Ledger.

![BACCA](assets/fr/05.webp)

Společnost Bacca vás poté bude informovat, zda je vaše účetní kniha pravá. Pokud není, znamená to, že zařízení bylo kompromitováno nebo že se jedná o padělek. V takovém případě jej okamžitě přestaňte používat.

![BACCA](assets/fr/06.webp)

V nabídce "*Apps*" si můžete prohlédnout seznam aplikací, které jsou již v zařízení Ledger nainstalovány.

![BACCA](assets/fr/07.webp)

Chcete-li nainstalovat aplikaci Bitcoin, klikněte na tlačítko "*Install*" a poté autorizujte instalaci v aplikaci Ledger.

![BACCA](assets/fr/08.webp)

Aplikace je dobře nainstalovaná.

![BACCA](assets/fr/09.webp)

Pokud nemáte nainstalovanou nejnovější verzi aplikace Bitcoin, zobrazí Bacca místo označení "*Latest*" tlačítko "*Update*". Kliknutím na toto tlačítko aplikaci jednoduše aktualizujte.

![BACCA](assets/fr/10.webp)

Nyní, když je váš Ledger správně nakonfigurován s nejnovější verzí aplikace Bitcoin, jste připraveni importovat a používat svou peněženku v softwaru pro správu, jako je Sparrow nebo Liana, aniž byste museli procházet službou Ledger Live!

Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Moc vám děkuji!

Doporučuji vám také podívat se na tento návod na GnuPG, který vysvětluje, jak zkontrolovat integritu a pravost softwaru před jeho instalací. To je důležitý postup, zejména při instalaci softwaru pro správu portfolia, jako je Liana nebo Sparrow :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

