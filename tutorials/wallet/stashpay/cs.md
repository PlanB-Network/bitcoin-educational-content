---
name: StashPay
description: Minimalistický model Bitcoin Wallet pro každého
---

![cover](assets/cover.webp)



Uživatelské zkušenosti jsou klíčovým faktorem při zavádění řešení Bitcoin po celém světě. Poskytování hladkého, jednoduchého a technicky nezatíženého prostředí je pro mnoho peněženek a platforem Exchange prioritou. V tomto ohledu StashPay vyniká svým minimalistickým přístupem a zároveň demonstruje sílu Lightning Network.



V tomto tutoriálu se podíváme na toto portfolio a zjistíme, jak funguje a jak je ideální pro malé firmy nebo soloprůmyslníky.



## Začínáme se StashPay



StashPay je blesková samoobsluha Wallet uznávaná především pro své minimalistické uživatelské prostředí.  S tímto Wallet nepotřebujete žádné technické znalosti, abyste mohli přijímat a odesílat své první satoši.



StashPay je open-source projekt vyvinutý v React Native a jeho cílem je vyřešit problém vysokých transakčních poplatků i u transakcí v hlavním řetězci protokolu Bitcoin. Je k dispozici jako mobilní aplikace na platformách Android a iOS prostřednictvím odkazů ke stažení, které jsou k dispozici na [webových stránkách](https://stashpay.me/).



![introduce](assets/fr/01.webp)



Je důležité stáhnout aplikaci pro Android z webových stránek, protože není k dispozici v obchodě Google Play.


Po dokončení stahování udělte potřebná oprávnění, abyste mohli aplikaci nainstalovat do telefonu se systémem Android.



Po instalaci aplikace vám StashPay při prvním otevření vytvoří počáteční účet Bitcoin Wallet. Před každou transakcí doporučujeme vytvořit zálohu tohoto Wallet. Níže naleznete všechny naše pokyny, jak zajistit, aby vaše obnovovací fráze byly řádně zálohovány.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Do nastavení StashPay se dostanete kliknutím na ikonu "Nastavení" a poté klikněte na možnost **Vytvořit zálohu**. Poté autorizujte zobrazení frází pro obnovení. Nekopírujte fráze pro obnovení do schránky telefonu, protože mohou být přístupné jiným podvodným aplikacím nainstalovaným v mobilním telefonu.



![backup](assets/fr/02.webp)



Můžete také obnovit již používaný kód Bitcoin Wallet kliknutím na možnost **Obnovit kód Wallet** a vložením 12 nebo 24 slov obnovení.



### Obdržte své první satoši na StashPay



Na domovské obrazovce klikněte na tlačítko **Přijmout** a nastavte částku vyšší, než je částka uvedená červeně. V našem případě nemůžeme pomocí StashPay Wallet přijmout méně než 0,11 USD.



![receive](assets/fr/03.webp)



Po zadání částky můžete kliknout na tlačítko **Vytvořit Invoice** a poté naskenovat nebo zkopírovat Invoice a odeslat jej odesílateli satoshis.



![receive_sats](assets/fr/04.webp)



Historii transakcí si můžete prohlédnout kliknutím na ikonu "hodin" na domovské stránce.



![network_fee](assets/fr/05.webp)



Jistě jste si všimli, že za příjem satoši musíte zaplatit síťový poplatek. Tyto poplatky budou odečteny od satoshis, které se chystáte obdržet. Je to proto, že StashPay je Wallet založený na vývojové sadě Breez. Chcete-li přijímat satoshis s implementací sady bez uzlu Lightning, bude Breez zákazníkovi (v našem případě StashPay) účtovat `0,25 % + 40 satoshis`. Více se dozvíte v našem výukovém programu Misty Breez.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Posílejte bitcoiny pomocí StashPay



Posílání bitcoinů pomocí StashPay je díky minimalistickému systému Interface poměrně intuitivní. Na domovské obrazovce klikněte na tlačítko **Odeslat**. Naskenujte QR kód nebo vložte číslo Address, na které chcete poslat satoši. StashPay automaticky zjistí řetězec protokolu Bitcoin, na který chcete bitcoiny poslat.



![send](assets/fr/06.webp)



Protože StashPay je Wallet založený na vývojové sadě Breez, těží ze zajímavé výhody: posílání bitcoinů v hlavním řetězci za nízké náklady. Breez využívá službu Boltz k provádění transakcí mezi různými řetězci protokolu Bitcoin, což umožňuje zákazníkům, kteří implementují vývojovou sadu, využívat tuto službu přímo ve své aplikaci.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Breez SDK však stanovuje minimální částku, za kterou můžete posílat bitcoiny na Address v hlavním řetězci.



![onchain](assets/fr/07.webp)



Bitcoiny můžete posílat také pomocí Lightning Address příjemce. Prohlédněte si údaje o transakci a potvrďte ji kliknutím na tlačítko **Odeslat**.



![confirm](assets/fr/08.webp)



## Více konfigurací



V nastavení StashPay můžete upravit konfigurace a přizpůsobit si tak používání Wallet.



StashPay vám umožňuje Exchange satoši v místní měně podle vašeho výběru. Klikněte na možnost **Měny** a poté vyhledejte svou měnu v seznamu +113 měn, které StashPay nabízí.



![currencies](assets/fr/09.webp)



V nabídce **Možnosti příjmu** najdete všechna nastavení pro příjem bitcoinů pomocí StashPay. Například výběrem možnosti **Vybrat Lightning nebo Onchain** povolíte svému Wallet přijímat bitcoiny z hlavního řetězce.



![receive-onchain](assets/fr/10.webp)



Možnost **Scan OnChain addresses** vám umožní obnovit zůstatek na Wallet kontrolou všech UTXO (bitcoinů, které jste ještě neutratili) spojených s různými adresami.



![rescan](assets/fr/11.webp)



V nabídce **Export log** jsou uvedeny všechny akce infrastruktury Breez a Boltz týkající se vašich transakcí a atomických výměn mezi různými řetězci protokolu Bitcoin.



![export](assets/fr/12.webp)



Právě jste si poradili s minimalistickou platební kartou Bitcoin Wallet od společnosti StashPay. Pokud vám tento návod přišel užitečný, doporučujeme náš návod, jak začít s Bitcoin a vydělat si první bitcoiny.



https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f