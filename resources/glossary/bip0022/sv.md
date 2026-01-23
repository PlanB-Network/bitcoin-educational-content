---
term: BIP0022
definition: JSON-RPC-standarden getblocktemplate som gör det möjligt för mining-programvara att kommunicera med fullnoder för att konstruera block.
---

BIP som föreslogs 2012 av Luke Dashjr och som introducerar en standardiserad JSON-RPC-metod för externa Mining-gränssnitt, kallad "getblocktemplate". Med ökningen av Mining-svårigheter har användningen av specialiserad extern programvara för att producera Proof of Work utvecklats. Denna BIP föreslår en gemensam kommunikationsstandard för blockmallen mellan fullständiga noder och programvara som är specialiserad på Mining. Denna metod innebär att hela blockets struktur skickas, snarare än bara rubriken, så att Miner kan anpassa den.