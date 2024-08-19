---
term: BLIND SIGNATURE
---

Chaums Blind Signaturen sind eine Form der digitalen Signatur, bei der der Aussteller der Signatur den Inhalt der Nachricht, die er signiert, nicht kennt. Die Signatur kann jedoch später mit der ursprünglichen Nachricht verifiziert werden. Diese Technik wurde 1983 vom Kryptographen David Chaum entwickelt.

Betrachten wir das Beispiel eines Unternehmens, das ein vertrauliches Dokument, wie einen Vertrag, authentifizieren möchte, ohne dessen Inhalt preiszugeben. Das Unternehmen wendet einen Maskierungsprozess an, der das Originaldokument auf kryptographische Weise reversibel transformiert. Dieses modifizierte Dokument wird an eine Zertifizierungsstelle gesendet, die eine Blind Signatur anwendet, ohne den zugrundeliegenden Inhalt zu kennen. Nachdem das maskierte signierte Dokument empfangen wurde, demaskiert das Unternehmen die Signatur. Das Ergebnis ist ein Originaldokument, das durch die Signatur der Behörde authentifiziert ist, ohne dass die Behörde jemals den ursprünglichen Inhalt gesehen hat.

Somit ermöglichen Chaums Blind Signaturen die Zertifizierung der Authentizität eines Dokuments, ohne dessen Inhalt zu kennen, und gewährleisten sowohl die Vertraulichkeit der Daten des Benutzers als auch die Integrität des signierten Dokuments.

Im Bitcoin wird dieses Protokoll in Systemen von Chaumian-Banken als Overlay (Cashu, Fedimint usw.) verwendet, aber insbesondere in Chaumian-Coinjoin-Protokollen, um sicherzustellen, dass der Koordinator nicht in der Lage ist, einen Input mit einem Output zu verknüpfen.