---
term: SIGOPS (CÁC THAO TÁC CHỮ KÝ)
---

Ám chỉ các thao tác chữ ký số cần thiết để xác thực các giao dịch. Mỗi giao dịch Bitcoin có thể chứa nhiều đầu vào, mỗi đầu vào có thể yêu cầu một hoặc nhiều chữ ký để được coi là hợp lệ. Việc xác minh các chữ ký này được thực hiện thông qua việc sử dụng các opcode cụ thể được gọi là "sigops". Cụ thể, điều này bao gồm `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG`, và `OP_CHECKMULTISIGVERIFY`. Các thao tác này đặt ra một số công việc nhất định cho các nút mạng phải xác minh chúng. Để ngăn chặn các cuộc tấn công DoS thông qua việc tăng số lượng sigops một cách nhân tạo, giao thức do đó áp đặt một giới hạn về số lượng sigops được phép mỗi khối, để đảm bảo rằng tải xác thực vẫn có thể quản lý được cho các nút. Giới hạn này hiện được đặt ở mức tối đa 80,000 sigops mỗi khối. Để đếm, các nút tuân theo các quy tắc sau:

Trong `scriptPubKey`, `OP_CHECKSIG` và `OP_CHECKSIGVERIFY` được tính là 4 sigops. Các opcode `OP_CHECKMULTISIG` và `OP_CHECKMULTISIGVERIFY` được tính là 80 sigops. Thực tế, trong quá trình đếm, các thao tác này được nhân với 4 khi chúng không phải là một phần của đầu vào SegWit (đối với một P2WPKH, số lượng sigops sẽ là 1);

Trong `redeemScript`, các opcode `OP_CHECKSIG` và `OP_CHECKSIGVERIFY` cũng được tính là 4 sigops, `OP_CHECKMULTISIG` và `OP_CHECKMULTISIGVERIFY` được tính là `4n` nếu chúng đứng trước `OP_n`, hoặc 80 sigops nếu không;

Đối với `witnessScript`, `OP_CHECKSIG` và `OP_CHECKSIGVERIFY` được tính là 1 sigop, `OP_CHECKMULTISIG` và `OP_CHECKMULTISIGVERIFY` được tính là `n` nếu chúng được giới thiệu bởi `OP_n`, hoặc 20 sigops nếu không;

Trong các kịch bản Taproot, sigops được xử lý khác so với các kịch bản truyền thống. Thay vì đếm trực tiếp mỗi thao tác chữ ký, Taproot giới thiệu một ngân sách sigops cho mỗi đầu vào giao dịch, tương ứng với kích thước của đầu vào đó. Ngân sách này là 50 sigops cộng với kích thước byte của chứng từ đầu vào. Mỗi thao tác chữ ký giảm ngân sách này đi 50. Nếu việc thực hiện một thao tác chữ ký làm cho ngân sách giảm xuống dưới không, kịch bản sẽ không hợp lệ. Phương pháp này cho phép nhiều linh hoạt hơn trong các kịch bản Taproot, đồng thời duy trì bảo vệ chống lại các lạm dụng tiềm năng liên quan đến sigops, bằng cách liên kết trực tiếp chúng với trọng lượng của đầu vào. Do đó, các kịch bản Taproot không được bao gồm trong giới hạn 80,000 sigops mỗi khối.