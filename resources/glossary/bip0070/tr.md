---
term: BIP0070
definition: SSL sertifikası ile imzalanmış ödeme taleplerini kullanan etkileşimli ödeme protokolü. Hiçbir zaman yaygın olarak benimsenmedi.
---

Bitcoin için interaktif ödeme protokolü. Ödeme taleplerinin gönderilmesini ve ödemelerin güvenli ve standartlaştırılmış bir şekilde alınmasını sağlar. Bu protokolde, istemci ek bir parametre (BIP72'de açıklanmıştır) ile genişletilmiş bir Bitcoin URI'sine (BIP21) tıklar. Ödeme talebi satıcının SSL sertifikası ile imzalanır. Bu talebin alınması ve doğrulanması üzerine, ödeme ayrıntıları müşterinin Wallet işlem Interface'ına otomatik olarak doldurulur. Bu protokol, ödemenin onaylanmasını sağlar ve ödemenin yararlanıcı kuruluşunu netleştirerek güvenliği ve kullanıcı deneyimini geliştirir. BIP70'de önerilen bu yöntem tüccarlar tarafından hiçbir zaman yaygın olarak benimsenmemiştir.