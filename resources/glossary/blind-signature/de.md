---
term: BLINDSIGNATUR

---
Die Blindsignatur nach Chaum ist eine Form der digitalen Signatur, bei der der Aussteller der Signatur den Inhalt der Nachricht, die er signiert, nicht kennt. Die Signatur kann jedoch später mit der Originalnachricht überprüft werden. Diese Technik wurde 1983 von dem Kryptographen David Chaum entwickelt.

Nehmen wir das Beispiel eines Unternehmens, das ein vertrauliches Dokument, z. B. einen Vertrag, authentifizieren möchte, ohne dessen Inhalt preiszugeben. Das Unternehmen wendet einen Maskierungsprozess an, der das Originaldokument kryptografisch umwandelt und umkehrbar macht. Dieses veränderte Dokument wird an eine Zertifizierungsstelle geschickt, die eine Blindsignatur anbringt, ohne den zugrunde liegenden Inhalt zu kennen. Nach Erhalt des maskiert signierten Dokuments hebt das Unternehmen die Maskierung der Signatur auf. Das Ergebnis ist ein Originaldokument, das durch die Signatur der Behörde beglaubigt ist, ohne dass die Behörde jemals den ursprünglichen Inhalt gesehen hat.

Die Blindsignaturen von Chaum ermöglichen es also, die Authentizität eines Dokuments zu zertifizieren, ohne dessen Inhalt zu kennen, wodurch sowohl die Vertraulichkeit der Daten des Benutzers als auch die Integrität des signierten Dokuments gewährleistet wird.

In Bitcoin wird dieses Protokoll in Systemen chaotischer Banken als Overlay verwendet (Cashu, Fedimint, etc.), vor allem aber in chaotischen Coinjoin-Protokollen, um sicherzustellen, dass der Koordinator nicht in der Lage ist, eine Eingabe mit einer Ausgabe zu verbinden.