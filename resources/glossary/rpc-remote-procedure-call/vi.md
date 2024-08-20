---
term: RPC (REMOTE PROCEDURE CALL)
---

Một giao thức máy tính cho phép một chương trình thực thi một thủ tục trên một máy tính từ xa như thể nó được thực thi một cách địa phương. Cụ thể, trong bối cảnh của Bitcoin, nó được sử dụng để cho phép các ứng dụng tương tác với bitcoind. Nó có thể được sử dụng để thực thi các lệnh trên một nút Bitcoin, như gửi giao dịch, quản lý ví, hoặc truy cập thông tin trên blockchain. Sự an toàn của tương tác này được đảm bảo thông qua xác thực qua một tệp `.cookie` hoặc thông tin xác thực, sao cho chỉ có các khách hàng được ủy quyền mới có thể thực hiện RPCs trên nút.

> ► *Trong tiếng Anh, nó có thể được dịch là "Remote Procedure Call".*