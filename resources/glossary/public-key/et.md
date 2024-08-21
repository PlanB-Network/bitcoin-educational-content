---
term: AVALIK VÕTI
---

Avalik võti on element, mida kasutatakse asümmeetrilises krüptograafias. See genereeritakse privaatvõtmest, kasutades pöördumatut matemaatilist funktsiooni. Bitcoinis tuletatakse avalikud võtmed nende vastavast privaatvõtmest, kasutades elliptilise kõvera ECDSA või Schnorri digitaalse allkirja algoritme. Erinevalt privaatvõtmest, võib avalikku võtit vabalt jagada, ilma et see ohustaks vahendite turvalisust. Bitcoin protokollis toimib avalik võti alusena Bitcoin aadressi loomiseks, mida seejärel kasutatakse UTXO kulutamistingimuste loomiseks kasutades `scriptPubKey`. Avalikke võtmeid aetakse sageli segamini peavõtme või laiendatud võtmetega (xpub...). Siiski on need elemendid üsna erinevad.

> ► *Inglise keeles nimetatakse avalikku võtit "public key". See termin on mõnikord lühendatult "pubkey" või "PK".*