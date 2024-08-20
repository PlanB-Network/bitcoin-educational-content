---
term: ANONSETS (BỘ ẨN DANH)
---

Anonsets được sử dụng như các chỉ báo để đánh giá mức độ riêng tư của một UTXO cụ thể. Cụ thể hơn, chúng đo lường số lượng UTXO không thể phân biệt được trong bộ chứa đồng tiền đang được nghiên cứu. Vì cần một nhóm UTXO giống hệt nhau, anonsets thường được tính toán trong một chu kỳ của coinjoins. Chúng cho phép, khi thích hợp, đánh giá chất lượng của các coinjoins. Một anonset lớn có nghĩa là mức độ ẩn danh tăng lên, khiến việc phân biệt một UTXO cụ thể trong bộ trở nên khó khăn. Có hai loại anonsets:
* Bộ ẩn danh tiềm năng;
* Bộ ẩn danh hồi cứu.

Loại đầu tiên chỉ ra kích thước của nhóm mà UTXO đang được nghiên cứu được ẩn giấu, biết UTXO ở đầu vào. Chỉ số này cho phép đo lường khả năng chống lại việc phân tích quyền riêng tư của đồng tiền từ quá khứ đến hiện tại (đầu vào đến đầu ra). Trong tiếng Anh, tên của chỉ số này là “*forward anonset*,” hoặc “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.png)

Loại thứ hai chỉ ra số lượng nguồn có thể có cho một đồng tiền cụ thể, biết UTXO ở đầu ra. Chỉ số này cho phép đo lường khả năng chống lại việc phân tích quyền riêng tư của đồng tiền từ hiện tại đến quá khứ (đầu ra đến đầu vào). Trong tiếng Anh, tên của chỉ số này là “*backward anonset*,” hoặc “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.png)

> ► *Trong tiếng Pháp, người ta thường chấp nhận sử dụng thuật ngữ “anonset.” Tuy nhiên, nó có thể được dịch là “ensemble d'anonymat” hoặc “potentiel d'anonymat.” Trong cả tiếng Anh và tiếng Pháp, thuật ngữ “score” cũng đôi khi được sử dụng để chỉ anonsets (prospective score và retrospective score).*