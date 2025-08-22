---
term: OP_CHECKSIGADD (0XBA)
---

Yığından en üstteki üç değeri çıkarır: bir `public key`, bir `CScriptNum` `n` ve bir `signature`. İmza boş vektör değilse ve geçerli değilse, kod bir hatayla sonlanır. İmza geçerliyse veya boş vektörse (`OP_0`), iki senaryo sunulur:


- İmza boş vektör ise: `n` değerine sahip bir `CScriptNum` yığına itilir ve yürütme devam eder;
- İmza boş vektör değilse ve geçerli kalırsa: `n + 1` değerinde bir `CScriptNum` yığına itilir ve yürütme devam eder.

Basitleştirmek için, `OP_CHECKSIGADD`, `OP_CHECKSIG`e benzer bir işlem gerçekleştirir, ancak yığına doğru veya yanlış itmek yerine, imza geçerliyse yığının üstündeki ikinci değere `1` ekler veya imza boş vektörü temsil ediyorsa bu değeri değiştirmeden bırakır. oP_CHECKSIGADD`, Tapscript'te `OP_CHECKMULTISIG` ve `OP_CHECKMULTISIGVERIFY` ile aynı çoklu imza politikalarının oluşturulmasına izin verir, ancak toplu olarak doğrulanabilir bir şekilde, yani geleneksel bir Multisig'ın doğrulanmasındaki arama işlemini ortadan kaldırır ve böylece düğümlerin CPU'ları üzerindeki işlem yükünü azaltırken doğrulamayı hızlandırır. Bu işlem kodu Tapscript'e yalnızca Taproot'in ihtiyaçları için eklenmiştir.