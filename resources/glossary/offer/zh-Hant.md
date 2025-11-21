---
term: 供應
---

在 BOLT12 中，*offers* 是靜態 QR 代碼，可在 Lightning Network 上進行多次付款。與傳統發票不同，*offers* 可以重複使用。它們可用於 generate 多個 Invoice 請求。當用戶掃描包含 *offer* 的 QR 碼時，它會向相關的 Lightning 節點發送請求新 Invoice 的消息。節點會回應一個付款人可以使用的Invoice。因此，*offer*為在Lightning上接收來自不同用戶的多筆付款提供了唯一的識別碼。