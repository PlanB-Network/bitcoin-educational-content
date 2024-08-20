---
term: SCRIPTWITNESS
---

Một phần tử trong các mục giao dịch SegWit chứa chữ ký và khóa công khai cần thiết để mở khóa bitcoin được gửi trong giao dịch. Tương tự như `scriptSig` của các giao dịch Legacy, `scriptWitness` tuy nhiên không được đặt ở cùng một vị trí. Thực sự, đây là phần, được gọi là "chứng thực" (`*witness*` trong tiếng Anh), được chuyển đến một cơ sở dữ liệu riêng biệt nhằm giải quyết vấn đề biến đổi giao dịch. Mỗi đầu vào SegWit có `scriptWitness` riêng của mình, và tất cả các phần tử `scriptWitness` cùng tạo thành trường `Witness` của giao dịch.

> ► *Hãy cẩn thận không nhầm lẫn `scriptWitness` với `witnessScript`. Trong khi `scriptWitness` chứa dữ liệu chứng thực cho bất kỳ đầu vào SegWit nào, `witnessScript` định nghĩa điều kiện chi tiêu của một UTXO P2WSH hoặc P2SH-P2WSH và tạo thành một script riêng biệt, tương tự như `redeemScript` cho một đầu ra P2SH.*