---
term: SECP256R1
---

Tên được đặt cho một đường cong elliptic được định nghĩa bởi tiêu chuẩn NIST cho mã hóa khóa công khai. Nó sử dụng một trường số nguyên tố 256 bit và một phương trình đường cong elliptic $y^2 = x^3 + ax + b$ với các hằng số:

```text
a = -3
```

và

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Đường cong `secp256r1` được sử dụng rộng rãi trong nhiều giao thức, nhưng nó không được sử dụng trong Bitcoin. Thực tế, Satoshi Nakamoto đã chọn đường cong `secp256k1`, mà vào năm 2009 thì ít được biết đến. Lý do chính xác cho sự lựa chọn này không được biết, nhưng có thể là để giảm thiểu rủi ro của các cửa hậu. Các tham số của đường cong $k1$ thực sự đơn giản hơn nhiều so với đường cong $r1$, đặc biệt là hằng số $b$.

> ► *Đường cong này đôi khi cũng được gọi là "P-256".*