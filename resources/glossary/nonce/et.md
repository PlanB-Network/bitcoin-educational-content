---
term: NONCE
---

Arvutiteaduses viitab termin "nonce" numbrile, mida kasutatakse ainult üks kord ja seejärel asendatakse. See on sageli juhuslik või pseudojuhuslik. Nonce'e kasutatakse mitmesugustes krüptograafilistes protokollides, et tagada protsessi turvalisus. Näiteks Bitcoin'i protokollis kasutatavad ECDSA allkirjad hõlmavad nonce'i kasutamist. See tähendab, et iga allkirja jaoks peab see number olema uus. Kui see nii ei ole, on võimalik kahe sama nonce'i kasutava allkirja võrdlemisel arvutada kasutatud privaatvõti.

Nonce'e kasutatakse ka Bitcoin'i kaevandamisprotsessis. Kaevurid suurendavad neid muudetavaid väärtusi oma kandidaatblokkides. Nad muudavad nonce väärtust, et leida krüptograafiline räsi, mis on väiksem või võrdne raskustasemega. See protsess nõuab olulist arvutusvõimsust, kuna see hõlmab ammendavat otsingut suure hulga võimalike nonce'ide seas. Kui kaevur leiab nonce'i, mis nende blokki lisades toodab räsi, mis vastab raskuskriteeriumidele, edastatakse blokk võrku ja kaevur võidab preemia.

> ► *2010. aastal avastasid teadlased, et Sony PlayStation 3 kasutas erinevate koodipakettide allkirjastamisel sama nonce'i. Nonce'i taaskasutamine võimaldas ründajatel arvutada tarkvara allkirjastamiseks kasutatud privaatvõtit. Privaatvõtme olemasolul said ründajad luua kehtivaid allkirju mis tahes koodile, võimaldades neil käivitada volitamata tarkvara, sealhulgas piraattarkvara või kohandatud operatsioonisüsteeme, otse PS3 peal.*

> ► *Nonce'i termini päritolu kohta on levinud eksiarvamus. Mõned väidavad, et see tähistab lühendit "number only used once" (ainult üks kord kasutatav number). Tegelikkuses ulatub sõna päritolu 18. sajandisse ja pärineb vanainglise väljendi "then anes" semantilisest arengust, mis tähendas "selleks puhuks".*