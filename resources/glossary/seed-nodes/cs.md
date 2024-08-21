---
term: SEED NODES
---

Statický seznam veřejných Bitcoin uzlů, integrovaný přímo do zdrojového kódu Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Tento seznam slouží jako spojovací body pro nové Bitcoin uzly připojující se k síti, ale je využit pouze v případě, že DNS semena neposkytnou odpověď během 60 sekund od jejich požadavku. V takovém případě se nový Bitcoin uzel připojí k těmto seed uzlům, aby navázal první spojení se sítí a požádal o IP adresy dalších uzlů. Konečným cílem je získat nezbytné informace pro provedení počátečního stahování bloků (IBD) a synchronizaci s řetězcem, který má nejvíce nahromaděné práce. Seznam seed uzlů zahrnuje téměř 1000 uzlů, identifikovaných v souladu s normou stanovenou BIP155. Seed uzly tak představují třetí metodu připojení k síti pro Bitcoin uzel, po možném využití souboru `peers.dat`, vytvořeného samotným uzlem, a požádání o DNS semena.

> ► *Poznámka, seed uzly by neměly být zaměňovány s "DNS semeny", která jsou druhou metodou navazování spojení.*