---
name: Slipstream
description: Gửi giao dịch đã ký trực tiếp đến một thợ đào bằng Slipstream, không phát tán nó lên mạng Bitcoin
---

![bìa](assets/cover.webp)

Thông thường, khi bạn ký một giao dịch, nó sẽ tự động được phát tán đến mọi node Bitcoin trên mạng. Sau đó, nó chờ được đào.

Tuy nhiên, chừng nào giao dịch chưa nằm trong một khối, kẻ tấn công đã có được khóa riêng tư của bạn có thể thay thế nó và đánh cắp tiền. Đây thường là trường hợp nếu bạn sử dụng ví phần cứng ColdCard.

Công cụ Slipstream của công ty khai thác MARA cho phép bạn bỏ qua việc phát tán giao dịch lên mạng: giao dịch được gửi trực tiếp (và chỉ) đến một thợ đào, nhờ đó được giữ riêng tư và tránh bị lộ trên mạng. Giao dịch có thể sẽ mất nhiều thời gian hơn để được đào, nhưng nó sẽ được bảo vệ trước một cuộc tấn công thay thế.

Dưới đây, chúng tôi cung cấp một hướng dẫn cho phép người dùng [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), cũng như người dùng ví [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), sử dụng công cụ Slipstream của thợ đào MARA thông qua trang [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Cảnh báo**: công cụ này chỉ dành cho một số trường hợp sử dụng nhất định, chủ yếu là ví Liana, ví miniscript và một số loại multisig. Wizardsardine **khuyến cáo rõ ràng không nên** dùng công cụ này cho các ví có tiền đã ở mức rủi ro bị đánh cắp nghiêm trọng, chẳng hạn các ví có cụm từ khôi phục được tạo trên một thiết bị ColdCard bị ảnh hưởng bởi lỗ hổng trình sinh số ngẫu nhiên. Trong tình huống đó, cuộc chạy đua với kẻ tấn công được tính bằng giây, và một giao dịch gửi đến một thợ đào duy nhất sẽ mất lâu hơn nhiều để xác nhận so với một giao dịch được phát tán bình thường. Nếu điều này liên quan đến bạn, hãy đọc hướng dẫn chuyên biệt của chúng tôi trước:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Dành cho người dùng Liana

Liana được duy trì bởi Wizardsardine, đơn vị phát hành trang [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), vì vậy quy trình rất trực tiếp: bạn chỉ cần xuất tệp PSBT đã ký thay vì phát tán nó.

*Điều kiện tiên quyết: có tiền trong ví Liana của bạn.*

### Bước 1: Tạo giao dịch của bạn bằng Liana

Như thường lệ, hãy tạo giao dịch của bạn bằng cách thêm địa chỉ đích, mô tả và số tiền (ở đây là mức tối đa có sẵn trong ví).

Để thiết lập mức phí:

- chọn các coin bạn muốn chi tiêu bằng cách nhấp vào ô nhỏ ở phía dưới bên trái, dưới "Coins selection";
- sau đó nhập mức phí. Hãy nhớ đặt phí cao hơn nhiều so với mức đề xuất, như mô tả trên trang này: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Cuối cùng, nhấp vào "Next".

![Tạo giao dịch trong Liana](assets/fr/01.webp)

### Bước 2: Kiểm tra chi tiết giao dịch của bạn

Trước khi nhấp vào "Sign", hãy kiểm tra chi tiết giao dịch của bạn; cụ thể là:

- số tiền được gửi;
- số satoshi được dành cho phí giao dịch;
- nhưng trên hết, địa chỉ mà bạn đang gửi tiền đến (hãy nhớ kiểm tra 5/6 ký tự đầu, 5/6 ký tự cuối và 5/6 ký tự ở giữa địa chỉ để tránh các cuộc tấn công "address poisoning").

![Kiểm tra chi tiết giao dịch](assets/fr/02.webp)

### Bước 3: Chọn các ví ký

Tiếp theo, chọn các ví phần mềm và/hoặc ví phần cứng mà bạn cần dùng để ký giao dịch. Nhắc lại nhanh: trong trường hợp ví multisig 2-of-2, bạn cần 2 chữ ký trên 2.

### Bước 4: Xuất tệp PSBT của giao dịch

Giao dịch Bitcoin hiện đã được ký bằng các khóa phù hợp. Đừng nhấp vào "Broadcast", nếu không nó sẽ được chia sẻ với toàn bộ mạng và, nếu bạn sử dụng ví phần cứng ColdCard, giao dịch của bạn sẽ bị lộ công khai và tiền của bạn sẽ gặp rủi ro.

Bây giờ bạn có thể nhấp vào "Export", rồi lưu tệp PSBT cục bộ trên máy tính của mình.

![Xuất tệp PSBT từ Liana](assets/fr/03.webp)

### Bước 5: Gửi giao dịch đến thợ đào qua outofband.wizardsardine.com

Bây giờ đến các bước cuối cùng. Để gửi giao dịch đến thợ đào, tất cả những gì bạn cần làm là lấy tệp PSBT rồi kéo và thả nó vào khu vực được chỉ định.

![Thả tệp PSBT vào outofband.wizardsardine.com](assets/fr/04.webp)

Sau đó giao dịch được hiển thị như bên dưới.

![Giao dịch trong hàng đợi](assets/fr/05.webp)

### Bước 6: Gửi giao dịch qua Slipstream

Cuối cùng, tất cả những gì bạn cần làm là nhấp vào "Send" để giao dịch được gửi đến MARA qua Slipstream.

![Gửi giao dịch qua Slipstream](assets/fr/06.webp)

Trong vài giây, giao dịch sẽ chuyển từ "Sending" sang "Accepted":

![Giao dịch được Slipstream chấp nhận](assets/fr/07.webp)

Việc còn lại chỉ là sao chép mã định danh giao dịch (TXID), rồi dán nó vào [mempool.space](https://mempool.space/) để theo dõi nó được đào:

![Tra cứu TXID trên mempool.space](assets/fr/08.webp)

Xin lưu ý: giao dịch sẽ hiển thị là "Transaction not found" cho đến khi thợ đào MARA đào được một khối và đưa giao dịch của bạn vào đó. Việc này có thể mất vài chục phút, hoặc thậm chí vài giờ, vì MARA chỉ nắm khoảng 4.5% hash rate của mạng Bitcoin. Tính đến ngày 4 tháng 8 năm 2026, điều này tương ứng với khoảng một khối được đào mỗi 3 giờ 45 phút.

## Dành cho người dùng các ví khác

Nếu bạn không sử dụng [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) nhưng vẫn muốn dùng công cụ này, đây là hướng dẫn sử dụng ví multisig 2-of-2. Để làm điều này, chúng ta sẽ sử dụng phần mềm ví [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Điều kiện tiên quyết: có tiền trong ví Sparrow của bạn.*

### Bước 1: Tạo giao dịch của bạn

Với [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), hãy tạo giao dịch trên ví multisig của bạn. Hãy nhớ đặt phí cao hơn nhiều so với mức đề xuất, như mô tả trên trang này: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Sau khi tạo xong, nhấp vào "Create Transaction".

![Tạo giao dịch trong Sparrow](assets/fr/09.webp)

### Bước 2: Hoàn tất giao dịch của bạn

Để hoàn tất giao dịch, bây giờ bạn cần ký nó. Để làm điều này, nhấp vào "Finalize Transaction for Signing".

![Hoàn tất giao dịch để ký](assets/fr/10.webp)

### Bước 3: Ký giao dịch bằng các khóa khác nhau của bạn

Bây giờ là lúc ký giao dịch. Để làm điều này, chỉ cần ký nó bằng ví phần mềm hoặc ví phần cứng mà bạn sử dụng.

![Ký giao dịch bằng các khóa multisig](assets/fr/11.webp)

### Bước 4: Tải xuống giao dịch đã ký, và không phát tán nó lên mạng

Giao dịch Bitcoin hiện đã được ký bằng cả hai khóa của multisig 2-of-2 của chúng ta. Đừng nhấp vào "Broadcast Transaction", nếu không nó sẽ được chia sẻ với toàn bộ mạng và, nếu bạn sử dụng ví phần cứng ColdCard, giao dịch của bạn sẽ bị lộ công khai và tiền của bạn sẽ gặp rủi ro.

![Giao dịch đã ký, sẵn sàng nhưng chưa được phát tán](assets/fr/12.webp)

### Bước 5: Hiển thị script giao dịch đã ký, hoặc tải xuống tệp PSBT

Để hiển thị giao dịch Bitcoin đã ký, bây giờ nhấp vào "View Final Transaction". Sau đó bạn có thể sao chép script giao dịch Bitcoin đã ký:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Hiển thị script giao dịch đã ký](assets/fr/13.webp)

Nếu bạn muốn tải xuống tệp giao dịch, bạn có thể:

- nhấp vào "File", rồi "Save transaction…";
- hoặc nhấp vào nút kết nối mạng ở phía dưới bên phải (nút màu vàng), rồi nhấp vào "Save Final Transaction".

Sau đó giao dịch sẽ được lưu cục bộ trên máy tính của bạn.

![Lưu giao dịch cuối cùng cục bộ](assets/fr/14.webp)

### Bước 6: Gửi giao dịch đến thợ đào qua outofband.wizardsardine.com

Bây giờ đến các bước cuối cùng. Để gửi giao dịch đến thợ đào, tất cả những gì bạn cần làm là:

- truy cập [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- dán script giao dịch đã ký được sao chép ở bước trước, rồi nhấp vào "ADD TO QUEUE" bên dưới;

![Dán script giao dịch vào công cụ](assets/fr/15.webp)

- hoặc lấy tệp rồi kéo và thả nó vào khu vực được chỉ định.

![Thả tệp giao dịch vào công cụ](assets/fr/16.webp)

Sau đó giao dịch được hiển thị như bên dưới.

![Giao dịch trong hàng đợi](assets/fr/17.webp)

Nếu một thông báo cho bạn biết rằng tổng lượng satoshi đầu vào trong giao dịch của bạn là không xác định (và do đó, số satoshi dành cho phí không thể được tính), bạn chỉ cần nhập thủ công tổng lượng satoshi đầu vào. Để tìm nó, chỉ cần nhấp vào phần hiển thị giao dịch của bạn trong Sparrow, ở giữa sơ đồ:

![Tổng lượng đầu vào được hiển thị trong Sparrow](assets/fr/18.webp)

Sau đó nhập lượng đó (15,904 sats trong ví dụ của chúng tôi) vào công cụ [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Nhập thủ công tổng lượng đầu vào](assets/fr/19.webp)

Cuối cùng, hãy kiểm tra rằng mức phí là chính xác.

### Bước 7: Gửi giao dịch qua Slipstream

Cuối cùng, tất cả những gì bạn cần làm là nhấp vào "Send" để giao dịch được gửi đến MARA qua Slipstream.

![Gửi giao dịch qua Slipstream](assets/fr/20.webp)

Trong vài giây, giao dịch sẽ chuyển từ "Sending" sang "Accepted":

![Giao dịch được Slipstream chấp nhận](assets/fr/21.webp)

Việc còn lại chỉ là sao chép mã định danh giao dịch (TXID), rồi dán nó vào [mempool.space](https://mempool.space/) để theo dõi nó được đào:

![Tra cứu TXID trên mempool.space](assets/fr/22.webp)

Xin lưu ý: giao dịch sẽ hiển thị là "Transaction not found" cho đến khi thợ đào MARA đào được một khối và đưa giao dịch của bạn vào đó. Việc này có thể mất vài chục phút, hoặc thậm chí vài giờ, vì MARA chỉ nắm khoảng 4.5% hash rate của mạng Bitcoin. Tính đến ngày 4 tháng 8 năm 2026, điều này tương ứng với khoảng một khối được đào mỗi 3 giờ 45 phút.
