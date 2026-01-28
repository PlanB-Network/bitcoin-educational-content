---
term: Djup
definition: Nivån för en nyckel i härledningsstrukturen för en HD-plånbok från masternyckeln.
---

I samband med HD-plånböcker (Hierarchical Deterministic) avser djup den specifika nivån för en nyckel (offentlig eller privat), en chain code, en utökad nyckel eller en Address inom Wallet:s härledningsstruktur från huvudnyckeln. Varje nivå i denna struktur kan ses som en våning i ett nyckelträd, där huvudnyckeln är roten (djup 0) och de efterföljande nivåerna definierar olika attribut som t.ex:

syfte (djup 1), typ av valuta (djup 2), konto (djup 3), typ av kedja (djup 4) och index för den specifika Address (djup 5).





För att gå från ett djup till nästa används en härledningsprocess från ett par överordnade nycklar till ett par underordnade nycklar.


> ► * Termen "avledningsgolv" används ibland också i stället för djup.*