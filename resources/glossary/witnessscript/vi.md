---
term: WITNESSSCRIPT
---

Một script xác định các điều kiện mà theo đó bitcoin có thể được chi tiêu từ P2WSH hoặc P2SH-P2WSH UTXOs. Thông thường, `witnessScript` xác định các điều kiện của một ví đa chữ ký dưới chuẩn SegWit. Trong các chuẩn script này, `scriptPubKey` của UTXO (đầu ra) chứa một hash của `witnessScript`. Để sử dụng UTXO này như một đầu vào trong một giao dịch mới, người giữ phải tiết lộ `witnessScript` gốc, để chứng minh sự phù hợp của nó với dấu vân tay trong `scriptPubKey`. `witnessScript` sau đó phải được bao gồm trong `scriptWitness` của giao dịch, nơi cũng chứa các yếu tố cần thiết để xác thực script, như chữ ký. Do đó, `witnessScript` tương đương với `redeemScript` trong một giao dịch P2SH, với sự khác biệt là nó được đặt trong phần chứng của giao dịch, và không phải trong `scriptSig`.

> ► *Cảnh báo, `witnessScript` không nên bị nhầm lẫn với `scriptWitness`. Trong khi `witnessScript` xác định các điều kiện chi tiêu của một P2WSH hoặc P2SH-P2WSH UTXO và tạo thành một script riêng biệt, `scriptWitness` chứa dữ liệu chứng của bất kỳ đầu vào SegWit nào.*