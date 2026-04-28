---
term: Anonsets (anonymity sets)

definition: Các chỉ số đo mức độ quyền riêng tư của UTXO bằng cách đếm số lượng UTXO không phân biệt được trong một tập hợp, thường sau khi coinjoin.
---
Anonset được sử dụng như các chỉ báo để đánh giá mức độ riêng tư của một UTXO cụ thể. Cụ thể hơn, chúng đo lường số lượng UTXO không thể phân biệt trong tập hợp bao gồm đồng tiền đang được nghiên cứu. Do cần có một nhóm UTXO giống hệt nhau, anonset thường được tính toán trong một chu kỳ coinjoin. Chúng cho phép, khi cần thiết, đánh giá chất lượng của các coinjoin. Một anonset có kích thước lớn biểu thị mức độ ẩn danh cao hơn, vì việc phân biệt một UTXO cụ thể trong tập hợp trở nên khó khăn.

Có hai loại anonset: forward anonset (forward-looking metrics); và backward anonset (backward-looking metrics). Thuật ngữ "*score*" đôi khi cũng được dùng để chỉ anonset.

Chỉ số thứ nhất cho biết kích thước của nhóm mà UTXO đầu ra đang được nghiên cứu ẩn mình trong đó, khi biết UTXO đầu vào. Chỉ số này cho phép đo lường mức độ bền vững của quyền riêng tư của đồng tiền trước một phân tích từ quá khứ đến hiện tại (từ đầu vào đến đầu ra). Chỉ số thứ hai cho biết số lượng nguồn có thể có đối với một đồng tiền nhất định, khi biết UTXO đầu ra. Chỉ số này cho phép đo lường mức độ bền vững của quyền riêng tư của đồng tiền trước một phân tích từ hiện tại đến quá khứ (từ đầu ra đến đầu vào).










