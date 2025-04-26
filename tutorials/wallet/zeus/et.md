---
name: Zeus

description: Mitme sõlmega isehoidev rahakott
---

![Zeus](assets/zeus_intro.webp)

ZEUS on mobiilne Bitcoin rahakott ja sõlme haldamise rakendus, mis pakub täielikke Bitcoin Lightning rahakoti funktsioone, muudab Bitcoinide maksmise lihtsaks, annab kasutajatele täieliku kontrolli oma finantside üle ning võimaldab edasijõudnud kasutajatel oma Lightning sõlmi mugavalt oma käe peal hallata.

## Kellele on ZEUS mõeldud?
Praegu on ZEUS mõeldud inimestele, kes jooksutavad omaenda [Lightning Network Daemon (LND)](https://lightning.engineering/) või [Core Lightning lightning (CLN)](https://blockstream.com/lightning/) kodu- või ärisõlmi ja haldavad neid Zeus kaudu kaugelt.

Kaupmehed, kes kasutavad [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) või [Alby](https://getalby.com/) (või mõnda muud LNDhub kontot), saavad samuti ühenduda, kasutada ja hallata oma sõlmi/kontosid ZEUS kaudu.

[Alates versioonist 0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/) hakkab ZEUS pakkuma tavalistele kasutajatele, kes soovivad lihtsalt kiiret ja odavat viisi Bitcoinide maksmiseks oma mobiilseadmest, kasutades [sisseehitatud mobiilset Lightning sõlme](https://docs.zeusln.app/category/embedded-node) integreeritud [Lightning Service Provider (LSP)](https://docs.zeusln.app/lsp/intro) abil.

## Olulised Zeus ressursid:
- Zeusi ametlik veebileht - [https://zeusln.app/](https://zeusln.app/)
- Zeusi dokumentatsioon - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeusi Githubi repositoorium](https://github.com/ZeusLN/zeus)
- [Zeusi Telegrami tugigrupp](https://t.me/ZeusLN)
- [Zeus NOSTRil](https://iris.to/zeus@zeusln.app)
- [Zeusi blogi teadaanded](https://blog.zeusln.com)

## Zeusi omadused
### Üldised omadused:
- Isehoidev, ainult Bitcoin ja Lightning rahakott
- Ei ole töötlemistasusid, ei ole KYC
- Täielikult avatud lähtekoodiga (APGLv3)
- Mitme sõlme/kontode tugi (võimalik hallata oma koduseid sõlmi, jooksutada sisseehitatud LND sõlme, ühenduda mitme LNDhub kontoga)
- Lihtne kasutada tegevusmenüü
- PIN-koodi või parooli krüpteering, privaatsusrežiim - peida oma tundlikud andmed
- Kontaktiraamat, mitu teemat, mitu keelt

### Tehnilised omadused
- Ühendus Tori kaudu
- Täielik LNURL tugi (makse, väljavõtmine, autentimine, kanal), saatmine Lightning aadressidele
- Detailne Lightning kanalite haldamine, MPP/AMP tugi, Keysend, marsruutimistasude haldamine
- Asendustasu (RBF) ja Lapse-maksab-vanema-eest (CPFP) tugi
- NFC maksed ja taotlused, sõnumite allkirjastamine ja kontrollimine
- Segwit ja Taproot tugi
- Lihtsad Taproot kanalid
- Isehoidev lightning aadressid (@zeuspay.com)
- Square'i müügikoht (varsti avatud PoS)

## Juhendid ja videoõpetused
Selleks, et osata kasutada Zeusi ja hallata Lightning kanaleid, likviidsust, tasusid jne, on parem esmalt lugeda mõningaid olulisi juhendeid Lightning võrgu kohta.

### Juhendid:
- [LND - Lightning Network Daemon Dokumentatsioon](https://docs.lightning.engineering/)
- [CLN - Core Lightning Dokumentatsioon](https://lightning.readthedocs.io/index.html)
- [Algajate Välkjuhend](https://bitcoiner.guide/lightning/) – autoriks Bitcoin Q&A
- [Välgu Sõlme Haldamine](https://www.lightningnode.info/) – autoriks openoms
- [Välguvõrk ja lennujaama analoogia](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Välgu Sõlme Likviidsuse Haldamine](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Välgu Sõlme Hooldus](https://darthcoin.substack.com/p/lightning-node-maintenance)

### Videoõpetus autorilt BTC Sessions

![Zeus Bitcoin Lightning Wallet - Mobiilse Sõlme Haldamine](https://youtu.be/hmmehTnV3ys)