---
term: P2MS
---

P2MS viết tắt của *Pay to Multisig*, dịch là "thanh toán cho nhiều chữ ký". Đây là một mô hình script chuẩn được sử dụng để thiết lập các điều kiện chi tiêu cho một UTXO. Nó cho phép khóa bitcoin bằng nhiều khóa công khai. Để chi tiêu những bitcoin này, cần có chữ ký với một số lượng khóa riêng tư đã được định trước. Ví dụ, `P2MS 2/3` bao gồm `3` khóa công khai với `3` khóa riêng tư bí mật tương ứng. Để chi tiêu bitcoin được khóa bằng script P2MS này, cần có chữ ký với ít nhất `2` trong số `3` khóa riêng tư. Đây là một hệ thống bảo mật ngưỡng.

Script này được phát minh vào năm 2011 bởi Gavin Andresen khi ông tiếp quản việc bảo trì cho client Bitcoin chính. Ngày nay, P2MS chỉ được sử dụng một cách hạn chế bởi một số ứng dụng. Phần lớn các chữ ký đa phần hiện đại sử dụng các script khác như P2SH hoặc P2WSH. So với những cái này, P2MS cực kỳ đơn giản. Các khóa công khai mà nó bao gồm được tiết lộ khi nhận giao dịch. Sử dụng P2MS cũng tốn kém hơn so với các script chữ ký đa phần khác.

> ► *P2MS thường được gọi là "bare-multisig", có thể được dịch là "chữ ký đa phần trần trụi" hoặc "chữ ký đa phần thô". Đầu năm 2023, script P2MS trở thành tâm điểm của một cuộc tranh cãi do việc sử dụng sai trong giao thức Stamps. Ảnh hưởng của chúng đối với bộ UTXO được chỉ ra một cách rõ ràng.*