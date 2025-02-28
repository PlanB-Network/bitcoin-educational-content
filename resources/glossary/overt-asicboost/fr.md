---
term: OVERT ASICBOOST
---

Version ouverte et transparente d'AsicBoost. AsicBoost est une technique d'optimisation algorithmique utilisée dans le minage de Bitcoin. Les mineurs utilisant la version Overt manipulent le champ `nVersion` du bloc candidat et utilisent cette modification comme un nonce supplémentaire. Cette méthode laisse le véritable champ `Nonce` du bloc inchangé lors de chaque tentative de hachage, ce qui réduit ainsi les calculs nécessaires pour chaque SHA256, en conservant certaines données identiques entre les tentatives. Cette version est détectable publiquement et ne dissimule pas ses modifications au reste du réseau, à l'inverse de la version Covert d'AsicBoost.

