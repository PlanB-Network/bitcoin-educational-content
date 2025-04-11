---
term: DNS SEEDS

---
Počáteční body připojení pro nové uzly Bitcoin, které se připojují k síti. Tato semena, což jsou vlastně specifické servery DNS, mají svou adresu trvale zabudovanou v kódu jádra bitcoinu. Když se nový uzel spustí, kontaktuje tyto servery, aby získal náhodný seznam IP adres pravděpodobně aktivních uzlů Bitcoinu. Nový uzel pak může navázat spojení s uzly na tomto seznamu a získat informace potřebné k provedení počátečního stažení bloku (IBD) a synchronizaci s řetězcem, který má nejvíce nahromaděné práce. Od roku 2024 je zde seznam DNS semen Bitcoin Core a osob odpovědných za jejich údržbu (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Todd;
- seed.bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.bitcoin.wiz.biz: Jason Maurice;
- seed.mainnet.achownodes.xyz: Ava Chow.

Semínka DNS jsou v pořadí druhou metodou navazování spojení mezi uzly Bitcoin. První metoda zahrnuje použití souboru peers.dat, který uzel sám vytvořil. Tento soubor je v případě nového uzlu přirozeně prázdný, pokud jej uživatel ručně neupravil.

> ► *Poznámka: Semínka DNS by se neměla zaměňovat se "semennými uzly", které jsou třetím způsobem navazování spojení.*