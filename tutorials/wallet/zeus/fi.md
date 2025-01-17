---
name: Zeus

description: Moninodinen itsehallinnollinen lompakko
---

![Zeus](assets/zeus_intro.webp)

ZEUS on mobiili Bitcoin-lompakko ja solmunhallintasovellus, joka tarjoaa täydet Bitcoin Lightning -lompakon toiminnot. Se tekee bitcoin-maksuista yksinkertaisia, antaa käyttäjille täyden hallinnan heidän varoistaan ja mahdollistaa edistyneemmille käyttäjille heidän Lightning-solmujensa hallinnan kämmenestään.

## Kenelle ZEUS on tarkoitettu?
Tällä hetkellä ZEUS on tarkoitettu ihmisille, jotka pyörittävät omaa [Lightning Network Daemon (LND)](https://lightning.engineering/) tai [Core Lightning lightning (CLN)](https://blockstream.com/lightning/) koti- / yrityssolmuaan ja hallitsevat niitä etänä Zeusin kautta.

Kauppiaat, jotka käyttävät [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) tai [Alby](https://getalby.com/) (tai mitä tahansa muuta LNDhub-tiliä), voivat myös yhdistää, käyttää ja hallita solmujaan / tilejään ZEUSin kautta.

[Alkaen versiosta v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS alkaa palvella keskivertokäyttäjiä, jotka haluavat vain yksinkertaisen tavan tehdä nopeita, edullisia bitcoin-maksuja mobiililaitteellaan tarjoamalla [sisäänrakennetun mobiili Lightning -solmun](https://docs.zeusln.app/category/embedded-node) integroidulla [Lightning Service Provider (LSP)](https://docs.zeusln.app/lsp/intro).

## Tärkeitä Zeus-resursseja:
- Zeusin virallinen verkkosivu - [https://zeusln.app/](https://zeusln.app/)
- Zeus Dokumentaatio - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github-repositorio](https://github.com/ZeusLN/zeus)
- [Zeus Telegram-tukiryhmä](https://t.me/ZeusLN)
- [Zeus NOSTR:ssä](https://iris.to/zeus@zeusln.app)
- [Zeus Blogi-ilmoitukset](https://blog.zeusln.com)

## Zeusin ominaisuudet
### Yleiset ominaisuudet:
- Itsehallinnollinen, vain Bitcoin ja Lightning -lompakko
- Ei käsittelymaksuja, Ei KYC
- Täysin avoimen lähdekoodin (APGLv3)
- Monen solmun / tilien tuki (voit hallita omaa kotisolmuasi, ajaa sisäänrakennettua LND-solmua, yhdistää useisiin LNDhub-tileihin)
- Helppokäyttöinen toimintovalikko
- PIN- tai salasanakryptaus, Yksityisyystila - piilota arkaluonteiset tietosi
- Yhteystietokirja, moniteemainen, monikielinen

### Tekniset ominaisuudet
- Yhteys Torin kautta
- Täysi LNURL-tuki (maksu, nosto, auth, kanava), Lähetys Lightning-osoitteisiin
- Yksityiskohtainen Lightning-kanavien hallinta, MPP/AMP-tuki, Keysend, reititysmaksujen hallinta
- Korvaa-maksulla (RBF) ja Lapsi-maksaa-vanhemmasta (CPFP) tuki
- NFC-maksut ja -pyynnöt, Viestien allekirjoitus & varmennus
- Segwit ja Taproot-tuki
- Yksinkertaiset Taproot-kanavat
- Itsehallinnolliset lightning-osoitteet (@zeuspay.com)
- Squaren Point of Sale (pian avoin PoS)

## Oppaat ja Videotutoriaalit
Jotta voisit käyttää Zeusta ja hallita Lightning-kanavia, likviditeettiä, maksuja jne., on parempi ensin lukea joitakin tärkeitä oppaita Lightning Networkista.

### Oppaat:
- [LND - Lightning Network Daemon Dokumentaatio](https://docs.lightning.engineering/)
- [CLN - Core Lightning Dokumentaatio](https://lightning.readthedocs.io/index.html)
- [Aloittelijan opas Lightning-verkkoon](https://bitcoiner.guide/lightning/) – Bitcoin Q&A:n toimesta
- [Lightning-solmun hallinta](https://www.lightningnode.info/) – openomsin toimesta
- [Lightning-verkko ja lentokenttävertaus](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Lightning-solmun likviditeetin hallinta](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Lightning-solmun ylläpito](https://darthcoin.substack.com/p/lightning-node-maintenance)

### Video-opas BTC Sessionsin toimesta

![Zeus Bitcoin Lightning Wallet - Mobiilisolmun hallinta](https://youtu.be/hmmehTnV3ys)