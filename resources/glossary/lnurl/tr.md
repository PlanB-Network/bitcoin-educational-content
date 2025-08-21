---
term: LNURL
---

Lightning düğümleri ve istemcilerin yanı sıra üçüncü taraf uygulamaları arasındaki etkileşimleri basitleştirmek için tasarlanmış bir dizi özelliği belirten iletişim protokolü. Bu protokol HTTP'yi temel alır ve ödeme talebi, para çekme talebi veya kullanıcı deneyimini geliştiren diğer işlevler gibi çeşitli işlemler için bağlantılar oluşturulmasını sağlar. Her LNURL, tarandığında Lightning Wallet üzerinde bir dizi otomatik eylemi tetikleyen `lnurl` önekiyle bech32'de kodlanmış bir URL'dir.


Örneğin, LNURL-Withdraw (LUD-03), manuel olarak generate a Invoice yapmak zorunda kalmadan bir QR kodunu tarayarak bir hizmetten para çekmenizi sağlar. Veya LNURL-auth (LUD-04), çevrimiçi hizmetlere parola yerine Lightning Wallet'ünüzdeki özel anahtarı kullanarak bağlanmanızı sağlar.