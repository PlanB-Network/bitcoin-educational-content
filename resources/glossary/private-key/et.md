---
term: PRIVAATNE KEY

---
Privaatne võti on asümmeetrilise krüptograafia põhielement. See on arv (Bitcoini kontekstis 256 bitti), mis kujutab endast krüptograafilist saladust. Seda võtit kasutatakse tehingute digitaalseks allkirjastamiseks ja Bitcoini avaliku võtme (ja seega ka vastuvõtva aadressi) omandiõiguse tõendamiseks, rahuldades "scriptPubKey". Seega võimaldavad privaatvõtmed bitcoinide kulutamist, vabastades vastava avaliku võtmega seotud UTXOd. Privaatvõtmeid tuleb hoida rangelt konfidentsiaalsena, sest nende avalikustamine võib võimaldada pahatahtlikel kolmandatel isikutel võtta kontrolli seotud vahendite üle.

Bitcoini süsteemis on privaatne võti seotud avaliku võtmega digitaalallkirja algoritmi abil, mis kasutab elliptilisi kõveraid (ECDSA või Schnorr). Avalik võti on tuletatud eravõti, kuid vastupidist on praktiliselt võimatu saavutada, kuna selle aluseks oleva matemaatilise probleemi (diskreetse logaritmi probleem) lahendamine on arvutuslikult keeruline. Avalikku võtit kasutatakse tavaliselt Bitcoini aadressi genereerimiseks, mida kasutatakse bitcoinide lukustamiseks skripti abil. Krüptograafias on privaatvõtmed sageli juhuslikud või pseudosrandomarvud. Bitcoini deterministlike ja hierarhiliste rahakottide spetsiifilises kontekstis on privaatvõtmed deterministlikult tuletatud seemnest. Privaatvõtmeid aetakse sageli segamini seemne või taastamislausega (mnemoonikaga). Need elemendid on siiski erinevad.

> ► *Inglise keeles nimetatakse privaatvõtit "private key" Seda terminit lühendatakse mõnikord "privkey" või "PV" *