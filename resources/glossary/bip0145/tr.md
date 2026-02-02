---
term: BIP0145
definition: SegWit desteğini ve işlem ağırlığı hesaplamasını entegre etmek için JSON-RPC getblocktemplate çağrısının güncellenmesi.
---

JSON-RPC çağrısı `getblocktemplate`, BIP141'e uygun olarak SegWit desteğini içerecek şekilde güncellenir. Bu güncelleme, madencilerin SegWit tarafından getirilen işlemlerin ve blokların yeni "ağırlık" ölçümünü ve sigops limitinin hesaplanması gibi diğer parametreleri dikkate alarak bloklar oluşturmasına olanak tanır.