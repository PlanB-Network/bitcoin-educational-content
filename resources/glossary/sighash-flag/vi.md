---
term: SIGHASH FLAG
---

Một tham số trong giao dịch Bitcoin quyết định những thành phần nào của giao dịch (đầu vào và đầu ra) được bảo vệ bởi chữ ký liên quan, từ đó trở nên không thể thay đổi. SigHash Flag là một byte được thêm vào chữ ký số của mỗi đầu vào. Do đó, sự lựa chọn của SigHash Flag trực tiếp ảnh hưởng đến những phần nào của giao dịch được đóng băng bởi chữ ký và những phần nào vẫn có thể được sửa đổi sau đó. Cơ chế này đảm bảo rằng chữ ký cam kết chính xác và an toàn dữ liệu giao dịch theo ý định của người ký. Có ba SigHash Flag chính:

- `SIGHASH_ALL` (`0x01`): Chữ ký áp dụng cho tất cả các đầu vào và đầu ra của giao dịch, do đó khóa chúng hoàn toàn;

- `SIGHASH_NONE` (`0x02`): Chữ ký áp dụng cho tất cả các đầu vào nhưng không áp dụng cho bất kỳ đầu ra nào, cho phép các đầu ra được sửa đổi sau chữ ký;

- `SIGHASH_SINGLE` (`0x03`): Chữ ký bao gồm tất cả các đầu vào và chỉ một đầu ra tương ứng với chỉ số của đầu vào đã ký.

Ngoài ba SigHash Flag này, bộ điều chỉnh `SIGHASH_ANYONECANPAY` (`0x80`) có thể được kết hợp với mỗi loại trước đó. Khi bộ điều chỉnh này được sử dụng, chỉ một phần của các đầu vào được ký, để lại những phần khác có thể được sửa đổi. Dưới đây là các kết hợp hiện có với bộ điều chỉnh:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Chữ ký áp dụng cho một đầu vào duy nhất trong khi bao gồm tất cả các đầu ra của giao dịch;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Chữ ký bao gồm một đầu vào duy nhất, không cam kết với bất kỳ đầu ra nào;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Chữ ký áp dụng cho một đầu vào và chỉ áp dụng cho đầu ra có cùng chỉ số với đầu vào này.

> ► *Một từ đồng nghĩa đôi khi được sử dụng cho "SigHash" là "Signature Hash Types".*