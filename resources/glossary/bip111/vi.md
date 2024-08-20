---
term: BIP111
---

Đề xuất việc thêm một bit dịch vụ có tên `NODE_BLOOM` để cho phép các nút tín hiệu một cách rõ ràng sự hỗ trợ của họ đối với Bộ lọc Bloom như được mô tả trong BIP37. Việc giới thiệu `NODE_BLOOM` cho phép các nhà điều hành nút có thể vô hiệu hóa dịch vụ này nhằm giảm thiểu rủi ro của DoS. Tùy chọn BIP37 được vô hiệu hóa theo mặc định trong Bitcoin Core. Để kích hoạt nó, tham số `peerbloomfilters=1` phải được nhập vào trong tệp cấu hình.