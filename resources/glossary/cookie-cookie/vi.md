---
term: COOKIE (.COOKIE)
---

Tệp được sử dụng cho xác thực RPC (*Remote Procedure Call*) trong Bitcoin Core. Khi bitcoind khởi động, nó tạo ra một cookie xác thực duy nhất và lưu trữ nó trong tệp này. Các client hoặc script muốn tương tác với bitcoind qua giao diện RPC có thể sử dụng cookie này để xác thực một cách an toàn. Cơ chế này cho phép giao tiếp an toàn giữa bitcoind và các ứng dụng bên ngoài (như phần mềm ví, chẳng hạn), mà không cần quản lý thủ công tên người dùng và mật khẩu. Tệp `.cookie` được tạo lại mỗi khi khởi động lại bitcoind và được xóa khi tắt máy.