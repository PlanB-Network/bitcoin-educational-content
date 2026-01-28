---
term: CPFP (Child Pays For Parent)
definition: Metod som gör det möjligt för mottagaren att påskynda en fastnad transaktion genom att skapa en barn-transaktion med höga avgifter.
---

En transaktionsmekanism som syftar till att påskynda bekräftelsen av en Bitcoin-transaktion, liknande det som Replace-by-fee (RBF) gör, men från mottagarens sida. När en transaktion med avgifter som är för låga jämfört med marknaden fastnar i nodernas mempooler och inte bekräftas tillräckligt snabbt kan mottagaren göra en ny transaktion och spendera de bitcoins som mottagits i den blockerade transaktionen, även om den ännu inte är bekräftad. Denna andra transaktion kräver nödvändigtvis att den första minas för att kunna bekräftas. Miners tvingas därför att inkludera båda transaktionerna tillsammans. Den andra transaktionen kommer att fördela mycket mer i transaktionsavgifter än den första, på ett sådant sätt att den genomsnittliga avgiften uppmuntrar miners att inkludera båda transaktionerna. Den underordnade transaktionen (den andra) betalar för den överordnade transaktionen som har fastnat (den första). Det är därför det kallas för en "CPFP"


CPFP gör det alltså möjligt för mottagaren att få sina pengar snabbare trots de låga initiala avgifterna för avsändaren, till skillnad från RBF (*Replace-by-fee*), som gör det möjligt för avsändaren att ta initiativ till att påskynda sin egen transaktion genom att höja avgifterna.