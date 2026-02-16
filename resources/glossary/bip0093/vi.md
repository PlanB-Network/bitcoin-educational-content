---
term: BIP0093
definition: Tiêu chuẩn Codex32 cho phép sao lưu hạt giống bằng cách chia nó thành nhiều phần thông qua việc chia sẻ bí mật của Shamir.
---

BIP thông tin gợi ý một tiêu chuẩn để lưu và khôi phục seed của danh mục đầu tư xác định phân cấp (theo BIP32) bằng cách sử dụng Chia sẻ khóa bí mật của Shamir. Giao thức này định nghĩa định dạng "codex32", lấy cảm hứng từ định dạng bech32, bằng cách giới thiệu một chuỗi có cấu trúc bao gồm tiền tố, tham số ngưỡng, mã định danh, chỉ mục chia sẻ, tải trọng và tổng kiểm tra (BCH). Phương pháp này cho phép chia seed thành tối đa 31 phần, trong đó ngưỡng được xác định (từ 1 đến 9) là bắt buộc để khôi phục seed hoàn toàn.