---
term: THỜI GIAN TRUNG BÌNH MỖI VÒNG
---

Thời gian trung bình mỗi vòng là một chỉ số được sử dụng để ước lượng thời gian mà một nhóm đào cần để tìm ra một khối, dựa trên độ khó của mạng và hashrate của nhóm. Chỉ số này được tính bằng cách lấy số lượng shares cần thiết để tìm ra một khối và chia cho hashrate của nhóm. Ví dụ, nếu một nhóm đào có 200 thợ mỏ, và mỗi người tạo ra trung bình 4 shares mỗi giây, tổng sức mạnh tính toán của nhóm là 800 shares mỗi giây:

```text
200 * 4 = 800
```

Giả sử rằng, trung bình, cần 1 triệu shares để tìm ra một khối hợp lệ, thời gian trung bình mỗi vòng của nhóm sẽ là 1,250 giây, hay khoảng 21 phút:

```text
1,000,000 / 800 = 1,250
```

Trong thực tế, điều này có nghĩa là, trung bình, nhóm đào sẽ tìm thấy một khối mỗi khoảng 21 phút. Chỉ số này biến động theo sự thay đổi trong hashrate của nhóm: sự tăng lên trong hashrate sẽ giảm *Thời Gian Trung Bình Mỗi Vòng*, trong khi sự giảm xuống sẽ kéo dài nó. Chỉ số này cũng biến động theo mỗi lần điều chỉnh định kỳ của mục tiêu độ khó Bitcoin (mỗi 2016 khối). Phép đo này không tính đến các khối được tìm thấy bởi các nhóm khác và chỉ tập trung vào hiệu suất nội bộ của nhóm đang được nghiên cứu.