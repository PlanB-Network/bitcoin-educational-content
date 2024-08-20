---
term: DEPTH
---

Trong bối cảnh của ví HD (Hierarchical Deterministic), depth (độ sâu) chỉ đến cấp độ cụ thể của một khóa (công khai hoặc riêng tư), một mã chuỗi, một khóa mở rộng, hoặc một địa chỉ trong cấu trúc phái sinh của ví từ khóa chính. Mỗi cấp độ của cấu trúc này có thể được xem như một tầng trong cây khóa, nơi khóa chính ở gốc (độ sâu 0) và các cấp độ tiếp theo xác định các thuộc tính khác nhau như:
mục đích (độ sâu 1), loại tiền tệ (độ sâu 2), tài khoản (độ sâu 3), loại chuỗi (độ sâu 4), và chỉ số của địa chỉ cụ thể (độ sâu 5).

![](../../dictionnaire/assets/18.png)

Để di chuyển từ một độ sâu này sang độ sâu tiếp theo, một quá trình phái sinh được sử dụng từ một cặp khóa cha mẹ sang một cặp khóa con.

> ► *Thuật ngữ "tầng phái sinh" đôi khi cũng được sử dụng thay cho độ sâu.*