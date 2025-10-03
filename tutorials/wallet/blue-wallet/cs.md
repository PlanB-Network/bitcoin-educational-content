---
name: Blue Wallet

description: Radikálně jednoduché a výkonné portfolio Bitcoin
---
![cover](assets/cover.webp)



Začít používat Bitcoin se zdá být velkou výzvou pro lidi, kteří jsou skeptičtí k jednoduchosti jeho používání. Nalezení správných nástrojů, které tuto jednoduchost zajistí, se proto stává nesmírně důležitým pro lepší přijetí Bitcoin jako prostředku Exchange, a ne pouze jako úložiště hodnoty.



V tomto tutoriálu se podíváme na Blue Wallet, jednoduchý, ale velmi efektivní Bitcoin Wallet, který vám umožní spravovat bitcoiny osobně a také vytvářet správcovská družstva založená na [Multisig](https://planb.network/resources/glossary/multisig) (nebojte se, ještě se k němu vrátíme).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Začínáme s modrou Wallet



Blue Wallet je open source, samospasitelný Bitcoin Wallet, který vám umožní převzít kontrolu nad svými bitcoiny. Je k dispozici jako mobilní aplikace na platformách Android i iOS. V tomto návodu budeme vycházet z verze pro Android, nicméně všechny postupy, které budou rozvedeny, jsou stejně platné i pro iOS.



![download](assets/fr/01.webp)



⚠️ Nezapomeňte si stáhnout aplikaci Blue Wallet Bitcoin Wallet na oficiální platformě, abyste zaručili její pravost a ochránili své bitcoiny před možnými úniky a hackery.



Po instalaci můžete vytvořit nový soubor Wallet a uložit 12 slov pro obnovení nebo importovat stávající soubor Bitcoin Wallet. Zjistěte, jak vytvořit účinnou zálohu klíčových slov, abyste neztratili přístup ke svým bitcoinům.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pomocí modrého modulu Wallet můžete vytvořit samostatná specializovaná portfolia Bitcoin. Například můžete mít jedno Wallet pro úspory a druhé pro každodenní výdaje, a to vše ve stejné aplikaci.



![home](assets/fr/02.webp)



## Typy portfolia



V modré verzi Wallet najdete dva původní typy portfolia Bitcoin.



### Portfolio Bitcoin



Pokud jste zvyklí na jiná portfolia Bitcoin, jako je Phoenix nebo Aqua, nebudete s portfoliem Interface v modrém Wallet vůbec mimo.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Modrý Wallet Bitcoin Wallet představuje standardní Wallet v ekosystému Bitcoin. Bitcoiny můžete utrácet, pokud vlastníte slova pro obnovu, která v síti zajistí platný podpis pro ověření, že bitcoiny vlastníte.



Chcete-li vytvořit portfolio Bitcoin, klikněte na tlačítko **Přidat nyní**, vložte název portfolia a vyberte typ Bitcoin.



![bitcoin-wallet](assets/fr/03.webp)



Když kliknete na náhled Bitcoin Wallet, budete si moci prohlédnout historii transakcí a odesílat a přijímat bitcoiny.



⚠️ Všechny transakce v Bitcoin Wallet jsou v hlavním řetězci protokolu Bitcoin (Mainnet).





- Přijímání bitcoinů pomocí Bitcoin Blue Wallet Wallet je intuitivní. V dolní části obrazovky klikněte na tlačítko **Přijmout**. Sdílejte kód QR nebo svůj kód Bitcoin Address s odesílatelem, aby vám mohl bitcoiny poslat.



Můžete také nakonfigurovat předdefinovanou částku a určit tak částku Bitcoin, kterou chcete obdržet.



![receive-bitcoin](assets/fr/04.webp)





- Tlačítkem **Odeslat** odešlete bitcoiny na účet Bitcoin Address, nastavte požadovanou částku a ověřte transakci.



![send-bitcoin](assets/fr/05.webp)



Modrý Wallet umožňuje nastavit parametry zásilky Bitcoin podle vašich představ.



Pokud tedy chcete, aby byla vaše transakce rychle ověřena v Mempool a zahrnuta do bloku těžaři, můžete si zvolit poměr transakčních poplatků, který vám vyhovuje. V závislosti na zvoleném poměru budou těžaři vaši transakci upřednostňovat ve větší či menší míře. Více se dozvíte v našem návodu o prostoru Mempool.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Pomocí služby Blue Wallet můžete k jedné zásilce přidat více příjemců.



Když přidáte Bitcoin Address prvního příjemce, klikněte v možnostech na **Přidat příjemce**, přidejte Bitcoin Address a poté nastavte částku, která se má tomuto příjemci zaslat, a tak dále. Modrý Wallet odešle bitcoiny pro více zásilek na základě vaší jediné akce.



![add-recipients](assets/fr/07.webp)



Jednoho nebo všechny příjemce můžete odebrat kliknutím na **Odebrat příjemce**, resp. **Odebrat všechny příjemce**.



![remove-recipient](assets/fr/08.webp)





- **Nafoukněte poplatky**: Provedli jste transakci, jejíž potvrzení trvá dlouho? Povolením inflace poplatků můžete k čekající transakci přidat další poplatky a urychlit tak její potvrzení.



![bumping](assets/fr/09.webp)



### Portfolio Multisig



Multisig (multi-signature) Wallet představuje Wallet vytvořený seskupením určitého počtu (minimálně 2) peněženek Bitcoin. V tomto typu Wallet se v závislosti na zvolené konfiguraci a metodě utrácení bitcoinů stává kolektivní a kooperativní akcí.



V aplikaci Blue Wallet můžete vytvářet portfolia s více podpisy pro vaše sdružení, vaši rodinu nebo vaši společnost. V této části se budeme zabývat všemi aspekty tohoto speciálního typu portfolia.



Přidejte nové portfolio a vyberte typ **Multisig Vault** pro vytvoření portfolia s více podpisy.



![multisig-vault](assets/fr/10.webp)



Definujte konfiguraci m-de-n ve své organizaci s více podpisy kliknutím na **Nastavení trezoru**.



⚠️ V konfiguraci m-of-n představuje **m** minimální počet podpisů potřebných ke schválení transakce a **n** počet portfolií ve vaší organizaci.



Nezapomeňte definovat minimální počet podpisů (m) pro většinu vaší organizace. Například konfigurace s více podpisy 2 ze 3 vyžaduje, aby transakci před jejím provedením podepsaly dvě peněženky ve vaší organizaci.



❗Definice konfigurace m-of-n, kde n je rovno m, je velkým rizikem. Když člen ztratí přístup ke svému Wallet, ztratíte oprávnění utrácet bitcoiny v Wallet.



Zde je několik příkladů optimálních konfigurací pro zajištění bezpečnosti a dostupnosti bitcoinů:





- 2-de-3 multipodpis.





- multipodpis 5-de-7.



![vault-settings](assets/fr/11.webp)



Dodržujte osvědčené postupy výběrem formátu P2WSH.



❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh) neboli Pay to Witness Script Hash** je metoda uzamykání, která uzamkne odchozí bitcoiny (výstupy) vaší transakce na Hash vlastního skriptu, který nastaví Blue Wallet. Hlavní výhodou tohoto typu zamykání je, že snižuje velikost transakčních dat a implicitně umožňuje platit nižší transakční poplatky.



Vytvořte nebo importujte každé z **n** portfolií ve své konfiguraci. V našem výukovém programu budeme používat konfiguraci 2 ze 3 více podpisů. Nezapomeňte uložit slova obnovy pro každé portfolio zvlášť.



![vault-keys](assets/fr/12.webp)





- Přijímání bitcoinů



Na stránce Multisig Wallet najdete historii transakcí a tlačítka Přijmout a Odeslat.



Přijímání bitcoinů v Wallet s více podpisy probíhá stejně, jako když jste ve standardní Bitcoin Wallet.





- **Poslat bitcoiny** :



Díky správě Wallet s více podpisy se utrácení bitcoinů stává složenou akcí, ať už s jinými lidmi, nebo s druhým vlastním Wallet. Jediný podpis vašeho Wallet již nestačí. To přidává vašim bitcoinům Layer na bezpečnosti, protože zlomyslná osoba nebude moci tyto bitcoiny utratit, když se dostane do držení pouze jednoho z vašich soukromých klíčů.



Stejně jako u standardního portfolia Bitcoin modrého Wallet můžete v možnosti **Přidat příjemce** definovat více příjemců.



Při ověřování transakce budete potřebovat druhý podpis, který schválí utracení bitcoinů. Nezapomeňte, že jsme v konfiguraci s dvěma až třemi podpisy.



Druhý signatář Wallet, pokud je také uživatelem, může transakci podepsat, i když je mimo internet (bez Wi-Fi, bez mobilních dat), a to naskenováním QR kódu právě vytvořené [částečně podepsané transakce](https://planb.network/resources/glossary/psbt).



![mutisig-send](assets/fr/13.webp)





- S portfoliem **Multi signature** můžete jít ještě dál:



Na obrazovce Interface vícepodpisového modulu Wallet klikněte na tlačítko **Správa klíčů**.



Zapomenutím jednoho z obnovovacích slov jednoho ze signálních portfolií (**Zapomeňte na tento seed...**) oznámíte modrému Wallet, aby vymazal zálohu těchto slov ze své paměti. Vytvoříte tedy externí zálohu.



![revoke-key](assets/fr/14.webp)



Provedením této akce si ponecháte pouze veřejný klíč spojený s těmito slovy pro obnovení.



⚠️ Uchovávání pouze veřejných klíčů (XPUB) umožňuje přidat další úroveň zabezpečení ke konfiguraci 2 ze 3 více podpisů. Ve skutečnosti by mohlo být škodlivé uchovávat všechna slova pro obnovení na jednom místě, když je telefon napaden. Útočníci, kteří mají přístup pouze k jednomu **VYMAZÁVACÍMU** (klíčovému slovu), které používáte k podepisování transakcí, nebudou moci ukrást vaše bitcoiny (vyžadováno minimálně 02 podpisů), protože veřejné klíče nelze použít k podepisování transakcí.



## Další možnosti s modrým Wallet



### Zlepšení zabezpečení přístupu k portfoliu



V části Nastavení můžete pomocí možnosti **Zabezpečení** definovat použití otisku prstu k provedení transakce, exportu nebo odstranění zařízení Wallet. Tím se ověří pravost osoby, která používá váš smartphone.



![biometry](assets/fr/15.webp)



## Aktivace Lightning Network



Aplikace Lightning Network již není v aplikaci Blue Wallet nativně podporována.



V nabídce Nastavení > **Nastavení blesku** můžete při spuštění uzlu Lightning Network Daemon (LND) ručně přiřadit blesk Wallet. Nainstalujte rozbočovač LND a poté přidružte svůj blesk Wallet zadáním odkazu vygenerovaného rozbočovačem.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Nyní jste dokončili prohlídku modrého Wallet a jste připraveni používat Bitcoin v celé jeho jednoduchosti a síle. Doporučujeme vám udělat další krok a zjistit, jak můžete ve svých obchodech přijímat platby Bitcoin díky síle Lightning.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06