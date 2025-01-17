---
term: EMPREINTE DE PORTEFEUILLE
---

Ensemble de caractéristiques distinctives observables dans les transactions effectuées par un même portefeuille Bitcoin. Ces caractéristiques peuvent inclure des similitudes dans l'utilisation des types de scripts, la réutilisation d'adresses, l'ordre des UTXOs, la place des outputs de change, la signalisation de RBF (*Replace-by-Fee*), le numéro de version, le champ `nSequence` et le champ `nLockTime`. 

Les empreintes de portefeuille sont utilisées par les analystes pour tracer les activités d'une entité particulière sur la blockchain en identifiant des patterns récurrents dans ses transactions. Par exemple, un utilisateur qui envoie systématiquement son change vers des adresses P2TR (`bc1p…`) crée une empreinte caractéristique qui peut être utilisée pour suivre ses transactions futures. 

Comme le précise LaurentMT dans le Space Kek #19 (un podcast francophone), l'utilité des empreintes de portefeuille dans l'analyse de chaîne s'accroît de manière significative avec le temps. En effet, le nombre croissant de types de scripts et le déploiement de plus en plus progressif de ces nouvelles fonctionnalités par les logiciels de portefeuille accentuent les différences. Il arrive même que l'on puisse identifier avec exactitude le logiciel employé par l'entité tracée. Il faut donc comprendre que l’étude de l’empreinte d'un portefeuille s'avère particulièrement pertinente pour les transactions récentes, davantage que pour celles initiées au début des années 2010.

