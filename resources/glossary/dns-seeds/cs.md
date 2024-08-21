---
term: DNS SEEDS
---

Počáteční spojovací body pro nové uzly Bitcoinu připojující se k síti. Tyto "seedy", které jsou ve skutečnosti specifickými DNS servery, mají svou adresu trvale zabudovanou v kódu Bitcoin Core. Když se nový uzel spustí, kontaktuje tyto servery, aby získal náhodný seznam IP adres předpokládaně aktivních uzlů Bitcoinu. Nový uzel pak může navázat spojení s uzly na tomto seznamu, aby získal informace potřebné k provedení svého počátečního stahování bloků (Initial Block Download - IBD) a synchronizaci s řetězcem, který má nejvíce nahromaděné práce. K roku 2024 zde je seznam DNS seedů Bitcoin Core a jednotlivci odpovědní za jejich údržbu (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNS seedy jsou druhou metodou, podle priority, pro uzel Bitcoinu k navázání spojení. První metodou je použití souboru peers.dat, který uzel sám vytvořil. Tento soubor je přirozeně prázdný v případě nového uzlu, pokud uživatel neudělal manuální úpravy.

> ► *Poznámka, DNS seedy by neměly být zaměňovány se "seed uzly", které jsou třetím způsobem, jak navázat spojení.*