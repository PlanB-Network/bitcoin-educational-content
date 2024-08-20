---
term: SIGHASH_ANYPREVOUT
---

Đề xuất cho việc triển khai một bộ chỉnh sửa mới SigHash Flag trong Bitcoin, được giới thiệu với BIP118. `SIGHASH_ANYPREVOUT` cho phép linh hoạt hơn trong quản lý giao dịch, đặc biệt là cho các ứng dụng nâng cao như kênh thanh toán trên Lightning Network và bản cập nhật Eltoo. `SIGHASH_ANYPREVOUT` cho phép chữ ký không bị ràng buộc với bất kỳ UTXO trước đó cụ thể nào (*Bất kỳ Đầu ra Trước đó nào*). Khi sử dụng kết hợp với `SIGHASH_ALL`, nó sẽ cho phép ký tất cả các đầu ra của một giao dịch, nhưng không phải bất kỳ đầu vào nào. Điều này sẽ cho phép tái sử dụng chữ ký cho các giao dịch khác nhau, miễn là một số điều kiện cụ thể được đáp ứng.

> ► *Bộ chỉnh sửa SigHash này SIGHASH_ANYPREVOUT được phát triển từ ý tưởng SIGHASH_NOINPUT ban đầu được Joseph Poon đề xuất vào năm 2016 để nâng cao khái niệm của mình về Lightning Network.*