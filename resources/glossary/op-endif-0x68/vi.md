---
term: OP_ENDIF (0X68)
---

Đánh dấu kết thúc của một cấu trúc điều khiển có điều kiện được bắt đầu bởi một `OP_IF` hoặc `OP_NOTIF`, thường được theo sau bởi một hoặc nhiều `OP_ELSE`. Nó chỉ ra rằng việc thực thi của script nên tiếp tục vượt qua cấu trúc có điều kiện, bất kể nhánh nào được thực thi. Nói cách khác, `OP_ENDIF` phục vụ để phân định kết thúc của các khối có điều kiện trong script.