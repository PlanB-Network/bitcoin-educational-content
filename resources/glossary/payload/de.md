---
term: PAYLOAD

---
Im allgemeinen Kontext der Datenverarbeitung bezieht sich eine Nutzlast auf die wesentlichen Daten innerhalb eines größeren Datenpakets. Bei einer SegWit-V0-Adresse auf Bitcoin entspricht die Nutzlast beispielsweise dem Hash des öffentlichen Schlüssels, ohne verschiedene Metadaten (den HRP, den Separator, die SegWit-Version und die Prüfsumme). Zum Beispiel haben wir in der Adresse "bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj":


- bc": der für den Menschen lesbare Teil (HRP);
- 1": das Trennzeichen;
- q": die SegWit-Version. Hier ist es die Version 0;
- c2eukw7reasfcmrafevp5dhv8635yuqa": die Nutzlast, hier der Hash des öffentlichen Schlüssels;
- ys50gj": die Prüfsumme.