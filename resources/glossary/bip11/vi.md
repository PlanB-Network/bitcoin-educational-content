---
term: BIP11
---

BIP được giới thiệu bởi Gavin Andresen vào tháng 3 năm 2012 đề xuất một phương pháp tiêu chuẩn để tạo giao dịch đa chữ ký trên Bitcoin. Đề xuất này nhằm tăng cường bảo mật cho bitcoin bằng cách yêu cầu nhiều chữ ký để xác thực một giao dịch. BIP11 giới thiệu một loại script mới, được gọi là "M-of-N multisig," nơi `M` đại diện cho số lượng chữ ký tối thiểu cần thiết từ số `N` khóa công khai tiềm năng. Tiêu chuẩn này sử dụng opcode `OP_CHECKMULTISIG`, đã tồn tại trong Bitcoin, nhưng trước đây không tuân thủ các quy tắc chuẩn hóa của các nút. Mặc dù loại script này không còn thường được sử dụng cho ví multisig thực tế, ưu tiên cho P2SH hoặc P2WSH, việc sử dụng nó vẫn là khả thi. Nó đặc biệt được sử dụng trong các meta-protocol như Stamps. Tuy nhiên, các nút có thể chọn không chuyển tiếp các giao dịch P2MS này với tham số `permitbaremultisig=0`.

> ► *Ngày nay, tiêu chuẩn này được biết đến với tên "bare-multisig" hoặc "P2MS".*