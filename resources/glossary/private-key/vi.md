---
term: KHÓA RIÊNG
---

Khóa riêng là một yếu tố cơ bản của mật mã bất đối xứng. Đây là một con số (256 bit trong bối cảnh của Bitcoin) đại diện cho một bí mật mật mã. Khóa này được sử dụng để ký số các giao dịch và chứng minh quyền sở hữu của một khóa công khai Bitcoin (và theo đó, một địa chỉ nhận) bằng cách thỏa mãn một `scriptPubKey`. Do đó, khóa riêng cho phép chi tiêu bitcoin bằng cách mở khóa các UTXO liên kết với khóa công khai tương ứng. Khóa riêng phải được giữ kín đáo một cách nghiêm ngặt, vì việc tiết lộ chúng có thể cho phép bên thứ ba xấu có khả năng kiểm soát các quỹ liên quan.

Trong hệ thống Bitcoin, khóa riêng được liên kết với một khóa công khai thông qua một thuật toán chữ ký số sử dụng đường cong elliptic (ECDSA hoặc Schnorr). Khóa công khai được tạo ra từ khóa riêng, nhưng việc thực hiện ngược lại gần như là không thể do độ khó tính toán tự nhiên trong việc giải quyết vấn đề toán học cơ bản (vấn đề logarit rời rạc). Khóa công khai thường được sử dụng để tạo ra một địa chỉ Bitcoin, được sử dụng để khóa bitcoin bằng một script. Trong mật mã, khóa riêng thường là các số ngẫu nhiên hoặc giả ngẫu nhiên. Trong bối cảnh cụ thể của ví Bitcoin xác định và phân cấp, khóa riêng được xác định một cách có hệ thống từ hạt giống. Khóa riêng thường bị nhầm lẫn với hạt giống hoặc với cụm từ khôi phục (mnemonic). Tuy nhiên, những yếu tố này là riêng biệt.

> ► *Trong tiếng Anh, khóa riêng được gọi là "private key." Thuật ngữ này đôi khi được viết tắt là "privkey," hoặc "PV."*