---
name: Payjoin
description: Payjoin trên Bitcoin là gì?
---
![Hình thu nhỏ Payjoin - steganography](assets/cover.webp)

***CHÚ Ý:** Sau khi các nhà sáng lập của Samourai Wallet bị bắt và máy chủ của họ bị tịch thu vào ngày 24 tháng 4, các Payjoins Stowaway trên Samourai Wallet chỉ hoạt động bằng cách trao đổi thủ công PSBT giữa các bên liên quan, với điều kiện cả hai người dùng đều kết nối với Dojo của riêng mình. Đối với Sparrow, các Payjoins qua BIP78 vẫn hoạt động. Tuy nhiên, có thể các công cụ này sẽ được khởi động lại trong những tuần tới. Trong khi chờ đợi, bạn có thể đọc bài viết này để hiểu cách hoạt động lý thuyết của payjoin.*

_Chúng tôi đang chú ý theo dõi sự phát triển của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này chỉ mang mục đích giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng những công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ luật pháp tại quốc gia của họ._

---
## Hiểu về Giao dịch Payjoin trên Bitcoin

Payjoin là một cấu trúc giao dịch Bitcoin đặc biệt giúp tăng cường quyền riêng tư cho người dùng trong quá trình thanh toán bằng cách hợp tác với người nhận thanh toán.

Vào năm 2015, [LaurentMT](https://twitter.com/LaurentMT) lần đầu tiên đề cập đến phương pháp này với tên gọi "giao dịch steganographic" trong một tài liệu có thể truy cập [tại đây](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Kỹ thuật này sau đó được Samourai Wallet áp dụng, trở thành ứng dụng đầu tiên triển khai nó với công cụ Stowaway vào năm 2018. Khái niệm về Payjoin cũng được tìm thấy trong [BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) và [BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki). Có một số thuật ngữ được sử dụng để chỉ Payjoin:
- Payjoin
- Stowaway
- P2EP (Pay-to-End-Point)
- Giao dịch Steganographic

Điểm độc đáo của Payjoin nằm ở khả năng tạo ra một giao dịch có vẻ bình thường ở cái nhìn đầu tiên nhưng thực chất là một mini Coinjoin giữa hai bên. Để thực hiện điều này, cấu trúc giao dịch bao gồm sự tham gia của người nhận thanh toán cùng với người gửi thực sự trong các input. Người nhận bao gồm một khoản thanh toán cho chính họ ở giữa giao dịch, điều này cho phép họ được thanh toán.

Hãy lấy một ví dụ cụ thể: nếu bạn mua một ổ bánh mì với giá `4000 sats` sử dụng một UTXO của `10,000 sats` và chọn Payjoin, người bán bánh mì của bạn sẽ thêm một UTXO của `15,000 sats` thuộc về họ như một input, mà họ sẽ nhận đầy đủ như một output, ngoài ra còn có `4000 sats` của bạn:
![Sơ đồ giao dịch Payjoin](assets/en/1.webp)

Trong ví dụ này, người bán bánh mì giới thiệu `15,000 sats` như một input và kết thúc với `19,000 sats`, với sự chênh lệch chính xác là `4000 sats`, đó là giá của ổ bánh mì. Về phía bạn, bạn bắt đầu với `10,000 sats` và kết thúc với `6,000 sats` như một output, đại diện cho sự chênh lệch `-4000 sats`, đó là giá của ổ bánh mì. Để đơn giản hóa ví dụ, tôi cố ý bỏ qua phí khai thác trong giao dịch này.
## Mục đích của giao dịch Payjoin là gì?
Giao dịch Payjoin phục vụ hai mục tiêu giúp người dùng tăng cường quyền riêng tư của họ khi thanh toán.
Trước hết, Payjoin nhằm mục đích gây nhầm lẫn cho người quan sát bên ngoài bằng cách tạo ra một bẫy trong phân tích chuỗi. Điều này được thực hiện thông qua Heuristic Sở Hữu Đầu Vào Chung (Common Input Ownership Heuristic - CIOH). Thông thường, khi một giao dịch trên blockchain có nhiều đầu vào, người ta giả định rằng tất cả các đầu vào này có khả năng thuộc về cùng một thực thể hoặc người dùng. Do đó, khi một nhà phân tích xem xét một giao dịch Payjoin, họ được dẫn dắt tin rằng tất cả các đầu vào đều đến từ cùng một người. Tuy nhiên, quan điểm này không chính xác bởi vì người nhận thanh toán cũng đóng góp đầu vào cùng với người thanh toán thực sự. Vì vậy, phân tích chuỗi được chuyển hướng sang một giải thích hóa ra là sai lầm.

Hơn nữa, Payjoin còn cho phép lừa dối người quan sát bên ngoài về số tiền thực sự đã được thanh toán. Bằng cách xem xét cấu trúc giao dịch, nhà phân tích có thể tin rằng số tiền thanh toán tương đương với số tiền của một trong các đầu ra. Tuy nhiên, trên thực tế, số tiền thanh toán không tương ứng với bất kỳ đầu ra nào. Thực tế, đó là sự chênh lệch giữa UTXO đầu ra của người nhận và UTXO đầu vào của người nhận. Trong trường hợp này, giao dịch Payjoin thuộc về lĩnh vực steganography. Nó cho phép ẩn số tiền thực sự của một giao dịch trong một giao dịch giả mạo hoạt động như một bẫy.

> Steganography là kỹ thuật ẩn thông tin trong dữ liệu hoặc đối tượng khác một cách không thể nhận biết được sự hiện diện của thông tin ẩn. Ví dụ, một thông điệp bí mật có thể được ẩn trong một chấm trong văn bản không liên quan gì đến nó, khiến nó không thể phát hiện bằng mắt thường (đây là kỹ thuật của micropoint). Khác với mã hóa, làm cho thông tin không thể hiểu được mà không có khóa giải mã, steganography không thay đổi thông tin. Nó vẫn được hiển thị ngay trước mắt. Mục tiêu của nó là ẩn sự tồn tại của thông điệp bí mật, trong khi mã hóa rõ ràng tiết lộ sự hiện diện của thông tin ẩn, mặc dù không thể truy cập mà không có khóa.

Hãy quay lại ví dụ của chúng ta về giao dịch Payjoin cho việc thanh toán một chiếc bánh mì baguette.
![Sơ đồ giao dịch Payjoin từ bên ngoài](assets/en/2.webp)
Khi thấy giao dịch này trên blockchain, một người quan sát bên ngoài theo dõi các heuristic thông thường của phân tích chuỗi sẽ giải thích như sau: "*Alice đã kết hợp 2 UTXOs làm đầu vào của giao dịch để thanh toán `19,000 sats` cho Bob*."
![Giải thích sai lầm về giao dịch Payjoin từ bên ngoài](assets/en/3.webp)
Giải thích này rõ ràng là không chính xác bởi vì, như bạn đã biết, hai UTXO đầu vào không thuộc về cùng một người. Hơn nữa, giá trị thực sự của khoản thanh toán không phải là `19,000 sats`, mà là `4,000 sats`. Phân tích của người quan sát bên ngoài do đó được hướng dẫn về một kết luận sai lầm, đảm bảo bảo vệ sự bảo mật của các bên liên quan.![sơ đồ giao dịch Payjoin](assets/en/1.webp)
Nếu bạn muốn phân tích một giao dịch Payjoin thực sự, đây là một giao dịch mà tôi đã thực hiện trên testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://mempool.space/fr/testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)
[**-> Khám phá hướng dẫn của chúng tôi về cách thực hiện Payjoin với Samourai Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)  
[**-> Khám phá hướng dẫn của chúng tôi về cách thực hiện Payjoin với Sparrow Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)

**Nguồn tài nguyên bên ngoài:**
- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki.