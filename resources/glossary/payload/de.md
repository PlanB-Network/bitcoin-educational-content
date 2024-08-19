---
term: PAYLOAD
---

Im allgemeinen Kontext der Informatik bezieht sich ein Payload auf die wesentlichen Daten, die innerhalb eines größeren Datenpakets übertragen werden. Zum Beispiel entspricht bei einer SegWit V0-Adresse auf Bitcoin der Payload dem Hash des öffentlichen Schlüssels, unter Ausschluss verschiedener Metadaten (der HRP, der Separator, die SegWit-Version und die Prüfsumme). Zum Beispiel haben wir in der Adresse `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`:
* `bc` : der für Menschen lesbare Teil (HRP);
* `1` : der Separator;
* `q` : die SegWit-Version. Hier ist es Version 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : der Payload, hier der Hash des öffentlichen Schlüssels;
* `ys50gj` : die Prüfsumme.