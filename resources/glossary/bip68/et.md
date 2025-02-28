---
term: BIP68

---
Kehtestatud võimalus kasutada suhtelisi lukustusajaid välja `nSequence` kaudu. See võimaldab tehingul määrata suhtelise viivituse enne blokki lisamist. Seda viivitust saab määratleda plokkide arvuna või 512 sekundi (st reaalajas) korrutisena. Pange tähele, et see uus tõlgendus väljale `nSequence` kehtib ainult siis, kui väli `nVersion` on suurem või võrdne `2`ga. See `nSequence`-välja tõlgendus toimub Bitcoini konsensusreeglite tasandil. Suhteline timelock määrab viivituse, mis algab eelmise tehingu aktsepteerimisest, samas kui absoluutne timelock määrab täpse hetke, enne mida tehingut ei saa blokki lisada. BIP68 võeti kasutusele 4. juulil 2016 soft forki kaudu koos BIP112 ja BIP113-ga, mis aktiveeriti esmakordselt BIP9 meetodi abil.