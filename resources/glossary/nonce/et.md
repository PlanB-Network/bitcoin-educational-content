---
term: NONCE

---
Arvutite kontekstis viitab termin "nonce" numbrile, mida kasutatakse ainult üks kord ja mis seejärel asendatakse. See on sageli juhuslik või pseudosjuhuslik. Nonce'i kasutatakse erinevates krüptograafilistes protokollides, et tagada protsessi turvalisus. Näiteks Bitcoini protokollis kasutatavad ECDSA allkirjad sisaldavad nonce'i kasutamist. See tähendab, et see number peab olema iga allkirja puhul uus. Kui see ei ole nii, siis on võimalik kasutada eravõti välja arvutada, võrreldes kahte sama nonce'i kasutavat allkirja.

Bitcoini kaevandamise protsessis kasutatakse ka nonces'e. Kaevandajad suurendavad neid muudetavaid väärtusi oma kandidaatblokkides. Nad muudavad nonce'i väärtust, et leida krüptograafiline hash, mis on madalam või võrdne raskusastme eesmärgiga. See protsess nõuab märkimisväärset arvutusvõimsust, kuna see hõlmab ammendavat otsingut suure hulga võimalike nonce'ide hulgast. Kui kaevandaja leiab nonce'i, mis tema plokki lisades annab raskuskriteeriumidele vastava digesti, edastatakse plokk võrku ja kaevandaja võidab tasu.

> ► *2010. aastal avastasid teadlased, et Sony PlayStation 3 kasutas erinevate koodipakettide allkirjastamisel sama nonce'i. Selline nonce'i korduvkasutamine võimaldas ründajatel arvutada tarkvara allkirjastamiseks kasutatava privaatvõtme. Ründaja võis isikliku võtme abil luua kehtivaid allkirju mis tahes koodile, mis võimaldas neil käivitada PS3-l otse volitamata tarkvara, sealhulgas piraatmänge või kohandatud operatsioonisüsteeme
> ► *Üldlevinud on väärarusaam mõiste "nonce" päritolu kohta Mõned väidavad, et see kujutab endast lühendit "number only used once" Tegelikkuses pärineb sõna päritolu 18. sajandist ja pärineb vanainglise väljendi "then anes" semantilisest arengust, mis tähendas "juhuks" *