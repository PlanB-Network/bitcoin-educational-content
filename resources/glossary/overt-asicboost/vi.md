---
term: OVERT ASICBOOST
---

Phiên bản mở và minh bạch của AsicBoost. AsicBoost là một kỹ thuật tối ưu hóa thuật toán được sử dụng trong việc đào Bitcoin. Các thợ mỏ sử dụng phiên bản Overt thao tác trường `nVersion` của khối ứng viên và sử dụng sự thay đổi này như một nonce bổ sung. Phương pháp này giữ nguyên trường `Nonce` thực sự của khối trong mỗi lần thử băm, do đó giảm bớt các phép tính cần thiết cho mỗi SHA256, bằng cách giữ một số dữ liệu giống nhau giữa các lần thử. Phiên bản này có thể được phát hiện công khai và không giấu các sửa đổi của mình khỏi phần còn lại của mạng, không giống như phiên bản Covert của AsicBoost.