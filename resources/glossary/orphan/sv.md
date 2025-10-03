---
term: ORPHAN
---

Teoretiskt sett avser en Orphan block ett giltigt block som tas emot av en nod som ännu inte har förvärvat det överordnade blocket, det vill säga det föregående i kedjan. Även om detta block är giltigt förblir det isolerat lokalt som ett föräldralöst block.


I dagligt tal används dock termen "Orphan block" ofta för ett block utan barn: ett giltigt block som inte finns kvar i den huvudsakliga Bitcoin-kedjan. Detta inträffar när två miners hittar ett giltigt block på samma kedjehöjd inom en kort period och sänder det över nätverket. Noderna väljer så småningom bara ett block att inkludera i kedjan, baserat på principen om den kedja som har mest arbete ackumulerat, vilket gör det andra "föräldralöst"


![](../../dictionnaire/assets/9.webp)


> personligen föredrar jag att använda termen "Orphan block" för att tala om ett block utan en förälder och termen "stale block" för att hänvisa till ett block som inte har ett barn. Jag tycker att detta är mer logiskt och förståeligt, även om en majoritet av bitcoiners inte följer denna användning.