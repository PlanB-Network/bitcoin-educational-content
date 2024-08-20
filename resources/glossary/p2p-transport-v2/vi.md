---
term: P2P TRANSPORT V2
---

Phiên bản mới của giao thức truyền thông P2P của Bitcoin tích hợp mã hóa cơ hội để tăng cường quyền riêng tư và bảo mật trong giao tiếp giữa các nút. Cải tiến này nhằm giải quyết một số vấn đề với phiên bản cơ bản của giao thức P2P, đặc biệt là làm cho dữ liệu trao đổi không thể phân biệt được bởi một quan sát viên thụ động (như nhà cung cấp dịch vụ internet), từ đó giảm thiểu rủi ro của kiểm duyệt và các cuộc tấn công thông qua việc phát hiện các mẫu cụ thể trong các gói dữ liệu.

Mã hóa được thực hiện không bao gồm xác thực nhằm tránh thêm sự phức tạp không cần thiết và không làm ảnh hưởng đến bản chất không cần phép của kết nối mạng. Tuy nhiên, giao thức truyền thông P2P mới này cung cấp bảo mật tốt hơn chống lại các cuộc tấn công thụ động và làm cho các cuộc tấn công chủ động trở nên đắt đỏ và dễ phát hiện hơn (đặc biệt là các cuộc tấn công MITM). Sự giới thiệu của một dòng dữ liệu giả ngẫu nhiên làm phức tạp nhiệm vụ cho những kẻ tấn công muốn kiểm duyệt hoặc thao túng giao tiếp.

P2P Transport V2 đã được bao gồm như một tùy chọn (tắt theo mặc định) trong phiên bản 26.0 của Bitcoin Core, được triển khai vào tháng 12 năm 2023. Nó có thể được kích hoạt với tùy chọn `v2transport=1` trong tệp cấu hình.