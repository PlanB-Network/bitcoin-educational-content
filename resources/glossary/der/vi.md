---
term: ĐẠI HỌC
---

Từ viết tắt của *Distinguished Encoding Rules*. Đây là một tập hợp con nghiêm ngặt của các quy tắc mã hóa ASN.1 được định nghĩa trong đặc tả [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) và được sử dụng để mã hóa bất kỳ loại dữ liệu nào theo trình tự nhị phân. DER chủ yếu được sử dụng trong các lĩnh vực cụ thể, chẳng hạn như mật mã học, trong đó dữ liệu phải được mã hóa theo cách chuẩn, có thể dự đoán được.


Trên Bitcoin, chữ ký ECDSA được mã hóa theo định dạng DER. Chúng bao gồm hai số được mã hóa 32 byte (`r`,`s`). Định dạng chữ ký bao gồm Elements sau (71 byte):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Với :




- 0x30` (1 byte): định danh của cấu trúc hợp chất;
- length` (1 byte): độ dài của dữ liệu sau;
- 0x02` (1 byte): loại định danh dữ liệu `INTEGER` (số nguyên);
- `r-length` (1 byte): độ dài của giá trị `r` tiếp theo (32 byte);
- r` (32 byte): giá trị của `r` dưới dạng số nguyên big-endian;
- 0x02` (1 byte): loại định danh dữ liệu `INTEGER` (số nguyên);
- `s-length` (1 byte): độ dài của giá trị `s` tiếp theo (32 byte);
- `s` (32 byte): giá trị `s` dưới dạng số nguyên big-endian.


Trong giao dịch Bitcoin, một byte được thêm vào cuối chữ ký DER để chỉ ra loại SigHash được sử dụng.