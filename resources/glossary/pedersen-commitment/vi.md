---
term: Pedersen commitment
---

Pedersen commitment là một loại Commitment mật mã có đặc tính đồng hình với phép toán cộng. Điều này có nghĩa là có thể xác thực tổng của hai cam kết mà không tiết lộ các giá trị riêng lẻ.


Về mặt hình thức, nếu:


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


sau đó :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Ví dụ, tính chất này hữu ích trong việc che giấu số lượng mã thông báo được trao đổi trong các hệ thống tiền điện tử, chẳng hạn như RGB, trong khi vẫn có thể xác minh tổng số.