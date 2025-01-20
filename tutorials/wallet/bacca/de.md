---
name: Bacca
description: Konfigurieren eines Ledgers ohne Ledger Live-Software
---
![cover](assets/cover.webp)

Wenn Sie einen Ledger verwenden, haben Sie wahrscheinlich festgestellt, dass Sie zumindest für die anfängliche Konfiguration des Geräts die Software Ledger Live verwenden müssen, um seine Authentizität zu überprüfen und die Bitcoin-Anwendung darauf zu installieren. Nach dieser Konfiguration ziehen es jedoch viele Bitcoiner vor, spezialisierte Bitcoin-Wallet-Verwaltungssoftware wie Sparrow oder Liana zu verwenden, anstatt Ledger Live. Obwohl Ledger hervorragende Hardware-Wallets herstellt, die schnell die neuesten Bitcoin-Funktionen enthalten, ist ihre Software nicht unbedingt an die spezifischen Bedürfnisse von Bitcoinern angepasst. Tatsächlich enthält Ledger Live viele Funktionen, die für Altcoins entwickelt wurden, während die Optionen für die Verwaltung von Bitcoin-Wallets begrenzt sind. Aber das Problem mit Sparrow und Liana ist (im Moment), dass sie Ihnen nicht erlauben, die Bitcoin-Anwendung auf dem Ledger zu installieren.

Um die Notwendigkeit zu umgehen, Ledger Live während der Erstkonfiguration Ihres Ledgers zu verwenden, können Sie das Bacca-Tool (oder "Ledger Installer") nutzen. Diese Software ermöglicht es Ihnen, die Bitcoin-Anwendung zu installieren und zu aktualisieren, die Echtheit Ihres Ledgers zu überprüfen und sogar später die Firmware des Geräts zu aktualisieren. Bacca wurde von Antoine Poinsot (Darosior), Bitcoin Core Entwickler bei Chaincode Labs, Mitbegründer [von Revault und Liana] (https://wizardsardine.com/) und Pythcoiner, entwickelt.

In diesem Tutorial zeige ich Ihnen, wie Sie dieses Tool verwenden können, damit Sie auf die Ledger Live-Software verzichten und trotzdem Ledger-Geräte nutzen können. Es funktioniert auf allen Geräten: Nano S Classic, Nano S Plus, Nano X, Flex und Stax.

---
*Bitte beachten Sie, dass dieses Tool recht neu ist und seine Entwickler angeben, dass es sich noch **in der Testphase** befindet. Sie empfehlen, es nur zu Testzwecken zu verwenden und nicht für ein Gerät, das eine echte Bitcoin-Wallet hosten soll, obwohl dies möglich ist. In dieser Hinsicht empfehle ich Ihnen, den Empfehlungen der Entwickler dieses Tools zu folgen, die [in der README ihres GitHub-Repositorys](https://github.com/darosior/ledger_installer) angegeben sind

---
## Voraussetzungen

Auf Ihrem Computer benötigen Sie zwei Tools, um Bacca zu verwenden:


- Git ;
- Rost.

Wenn Sie sie bereits installiert haben, können Sie diesen Schritt überspringen.

**Linux:**

Auf einer Linux-Distribution ist Git in der Regel vorinstalliert. Um zu überprüfen, ob Git auf Ihrem System installiert ist, können Sie den folgenden Befehl in das Terminal eingeben:

```bash
git --version
```

Wenn Sie Git nicht auf Ihrem System installiert haben, finden Sie hier den Befehl, um es auf einem Debian-System zu installieren:

```bash
sudo apt install git
```

Um Ihre Rust-Entwicklungsumgebung zu installieren, verwenden Sie den Befehl :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows:**

Um Git zu installieren, besuchen Sie [die offizielle Website des Projekts] (https://git-scm.com/). Laden Sie die Software herunter und folgen Sie den Installationsanweisungen.

![BACCA](assets/fr/01.webp)

Gehen Sie auf die gleiche Weise vor, um Rust von [der offiziellen Website] (https://www.rust-lang.org/tools/install) zu installieren.

![BACCA](assets/fr/02.webp)

**MacOS:**

Wenn Git noch nicht auf Ihrem System installiert ist, öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus, um es zu installieren:

```bash
git --version
```

Wenn Git nicht auf Ihrem System installiert ist, wird ein Fenster geöffnet, in dem Ihnen angeboten wird, Xcode zu installieren, das Git enthält. Folgen Sie einfach den Anweisungen auf dem Bildschirm, um mit der Installation fortzufahren.

Um Rust zu installieren, führen Sie den folgenden Befehl aus:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Bacca-Anlage

Öffnen Sie ein Terminal und gehen Sie zu dem Ordner, in dem Sie die Software speichern möchten. Führen Sie dann den folgenden Befehl aus:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Navigieren Sie zum Softwareverzeichnis:

```bash
cd ledger_installer
```

Verwenden Sie dann Cargo, um das Projekt zu kompilieren und die Bacca-GUI auszuführen:

```bash
cargo run -p ledger_manager_gui
```

Sie haben nun Zugriff auf die Softwareoberfläche.

![BACCA](assets/fr/03.webp)

## Konfigurieren des Ledgers

Wenn Ihr Ledger neu ist, müssen Sie zunächst den PIN-Code einrichten und die Wiederherstellungsphrase speichern. Für diese ersten Schritte benötigen Sie Ledger Live nicht. Schließen Sie Ihren Ledger einfach über das USB-Kabel an, um ihn mit Strom zu versorgen. Wenn Sie sich nicht sicher sind, wie Sie mit diesen beiden Schritten vorgehen sollen, können Sie am Anfang der Anleitung für Ihr Modell nachlesen:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Verwendung von Bacca

Schließen Sie Ihren Ledger an Ihren Computer an und entsperren Sie ihn mit dem von Ihnen eingestellten PIN-Code. Bacca sollte Ihren Ledger automatisch erkennen.

![BACCA](assets/fr/04.webp)

Um die Authentizität Ihres Ledger-Geräts zu bestätigen, klicken Sie auf die Schaltfläche "*Check*". Um fortzufahren, müssen Sie die Verbindung auf Ihrem Ledger-Gerät autorisieren.

![BACCA](assets/fr/05.webp)

Bacca wird Ihnen dann mitteilen, ob Ihr Ledger echt ist. Ist dies nicht der Fall, bedeutet dies entweder, dass das Gerät kompromittiert wurde oder dass es sich um eine Fälschung handelt. In diesem Fall sollten Sie es sofort nicht mehr benutzen.

![BACCA](assets/fr/06.webp)

Im Menü "*Apps*" können Sie die Liste der bereits auf Ihrem Ledger installierten Anwendungen einsehen.

![BACCA](assets/fr/07.webp)

Um die Bitcoin-Anwendung zu installieren, klicken Sie auf "*Installieren*" und autorisieren Sie dann die Installation auf Ihrem Ledger.

![BACCA](assets/fr/08.webp)

Die Anwendung ist gut installiert.

![BACCA](assets/fr/09.webp)

Wenn Sie nicht die neueste Version der Bitcoin-Anwendung installiert haben, zeigt Bacca eine Schaltfläche "*Update*" anstelle der Anzeige "*Latest*" an. Klicken Sie einfach auf diese Schaltfläche, um die Anwendung zu aktualisieren.

![BACCA](assets/fr/10.webp)

Nun, da Ihr Ledger korrekt mit der neuesten Version der Bitcoin-Anwendung konfiguriert ist, können Sie Ihr Wallet in eine Verwaltungssoftware wie Sparrow oder Liana importieren und verwenden, ohne Ledger Live zu verwenden!

Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen grünen Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Herzlichen Dank!

Ich empfehle Ihnen auch einen Blick auf dieses Tutorial über GnuPG, in dem erklärt wird, wie Sie die Integrität und Authentizität Ihrer Software vor der Installation überprüfen können. Dies ist eine wichtige Praxis, insbesondere bei der Installation von Portfolio-Management-Software wie Liana oder Sparrow :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

