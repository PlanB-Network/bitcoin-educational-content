---
term: Açık ASICBoost
definition: Madenciliği optimize etmek için nVersion alanını manipüle eden şeffaf AsicBoost sürümü.
---

AsicBoost'un açık ve şeffaf sürümü. AsicBoost, Bitcoin Mining'de kullanılan algoritmik bir optimizasyon tekniğidir. Açık versiyonu kullanan madenciler aday bloğun `nVersion` alanını manipüle eder ve bu değişikliği ek bir Nonce olarak kullanır. Bu yöntem, her hashing denemesi sırasında bloğun gerçek `Nonce` alanını değiştirmeden bırakır, böylece denemeler arasında bazı verileri aynı tutarak her SHA256 için gereken hesaplamaları azaltır. Bu sürüm herkese açık olarak tespit edilebilir ve AsicBoost'un gizli sürümünün aksine değişikliklerini ağın geri kalanından gizlemez.