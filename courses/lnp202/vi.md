---
name: Thiết lập nút Lightning đầu tiên của bạn
goal: Hiểu, cài đặt, cấu hình và sử dụng nút Lightning
objectives: 


  - Hiểu rõ vai trò và mục đích của một nút Lightning.
  - Xác định các giải pháp phần mềm khác nhau hiện có.
  - Cài đặt và cấu hình một nút Lightning (LND).
  - Kết nối tài khoản chi phí.
  - Hãy hiểu rõ các rủi ro khi sử dụng nút Lightning.


---

# Bước đầu tiên của bạn hướng tới quyền tự chủ trên Lightning



Bạn đã sở hữu sats đầu tiên, bảo đảm an toàn cho quỹ tự quản lý và triển khai một node Bitcoin để tự chủ trong việc sử dụng on-chain. Bước tiếp theo là đạt được quyền tự chủ tương tự trên Lightning: đó chính là mục tiêu của khóa học này.



LNP202 hướng đến người dùng trung cấp và hướng dẫn bạn từng bước triển khai nút Lightning đầu tiên mà không cần kỹ năng kỹ thuật nâng cao.



Bạn sẽ học cách cài đặt LND trên Umbrel, mở và quản lý các kênh của mình, giám sát nút mạng và kết nối wallet di động, để bạn có thể tận hưởng trải nghiệm tương tự như wallet lưu ký, đồng thời vẫn giữ quyền kiểm soát hoàn toàn đối với tiền của mình.



+++


# Giới thiệu


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Tổng quan khóa học


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 là khóa học thực hành được thiết kế để giúp bạn tự vận hành mạng Lightning bằng cách vận hành node của riêng mình. Mục tiêu rất đơn giản: bắt đầu với một node Bitcoin đã được thiết lập sẵn, triển khai LND trên Umbrel, bảo mật đúng cách, mở và quản lý các kênh đầu tiên, sau đó sử dụng node của bạn hàng ngày từ một thiết bị wallet di động. Khóa học này giả định rằng bạn đã tham gia khóa BTC 202, vì tôi cho rằng node Bitcoin trên Umbrel của bạn đã được thiết lập và đồng bộ hóa. Chúng ta sẽ không quay lại cách thiết lập node Bitcoin ở đây.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Để hiểu rõ hơn về cơ chế hoạt động bên trong của Lightning, khóa học LNP 201 cũng rất được khuyến khích, mặc dù nó không phải là điều kiện tiên quyết cho khóa học này:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Trong phần đầu tiên của khóa học LNP202 này, chúng ta sẽ xem xét Lightning node thực sự là gì, nó khác với wallet đơn giản như thế nào, và tại sao vận hành một node cá nhân là cách duy nhất để sử dụng Lightning mà không cần ủy quyền sats của bạn cho bên thứ ba đáng tin cậy. Phần này kết thúc bằng một lựa chọn chiến lược: giải pháp nào phù hợp với bạn, từ những cách tiếp cận đơn giản nhất đến Lightning node cổ điển, loại node mà chúng ta sẽ triển khai trong khóa học này.



Trong Phần 2 của khóa học, bạn sẽ cài đặt LND trên Umbrel, sau đó thiết lập các yếu tố ngăn ngừa những sai lầm tốn kém nhất: một chiến lược sao lưu thực tế và bảo vệ chống gian lận thông qua một trạm giám sát. Khi những điều cơ bản này đã được thiết lập, bạn sẽ mở kênh đầu tiên của mình để bắt đầu thanh toán trên Lightning bằng cơ sở hạ tầng của riêng bạn.



Như vậy, trong khóa học LNP202 này, chúng ta sẽ thiết lập một node Lightning ở chế độ cắm và chạy thông qua Umbrel, thay vì phương pháp dòng lệnh truyền thống, để phù hợp với người dùng trình độ trung cấp. Nếu bạn thích cài đặt bằng dòng lệnh, tôi khuyên bạn nên làm theo hướng dẫn bên dưới. Các khóa học Lightning nâng cao hơn, hướng dẫn bằng dòng lệnh cũng đang được chuẩn bị.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Phần 3 sẽ hướng dẫn bạn từ một nút hoạt động đến một nút mà bạn biết cách kiểm soát. Bạn sẽ bắt đầu bằng cách xác định hồ sơ người vận hành nút Lightning của mình (người tiêu dùng, người bán hoặc bộ định tuyến), sau đó làm quen với một gói phần mềm quản lý hoàn chỉnh để theo dõi các kênh và hoạt động một cách hiệu quả trên cấu trúc mạng của bạn. Cuối cùng, bạn sẽ giải quyết một điểm rất quan trọng của Lightning: làm thế nào để có được thanh khoản đầu vào, cho dù thông qua các giải pháp trả phí hay hợp tác.



Phần 4 sẽ tập trung vào việc sử dụng hàng ngày. Bạn sẽ thiết lập kết nối giữa nút mạng của mình và khách hàng di động, để bạn có thể thanh toán và thu tiền một cách đơn giản từ điện thoại thông minh của mình, mà không cần từ bỏ quyền tự quản lý. Trước tiên, chúng ta sẽ xem xét phương pháp mạng thông qua *Tailscale*, sau đó là phương pháp giao thức thông qua *Nostr Wallet Connect*, với những ưu điểm và nhược điểm tương ứng. Khóa học sẽ kết thúc với chương cuối cùng cung cấp cho bạn những thói quen đúng đắn để duy trì quyền tự quản lý của mình, cả về mặt vận hành và sư phạm.



Nếu bạn hoàn thành khóa học LNP202 này theo đúng trình tự, đến cuối khóa học bạn sẽ có một cấu hình hoàn chỉnh cho thiết bị Lightning node của mình, hoạt động tốt cho việc sử dụng hàng ngày và trên hết là nằm trong tầm kiểm soát.




## Hiểu về các điểm sét


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Trước khi khởi chạy node của riêng bạn, chương này sẽ tóm tắt ngắn gọn lý thuyết cơ bản đằng sau [Lightning Network](https://planb.academy/resources/glossary/lightning-network). Việc hiểu rõ các cơ chế liên quan thực sự rất quan trọng, vì điều này sẽ giúp bạn xác định rủi ro và áp dụng các biện pháp tốt để hạn chế chúng. Tuy nhiên, tôi sẽ không đi sâu vào chi tiết ở đây, vì đây không phải là mục tiêu chính của khóa học này. Nếu bạn muốn tìm hiểu sâu hơn về chủ đề này, tôi đặc biệt khuyên bạn nên tham khảo khóa học LNP 201 của Fanis Michalakis, đây là tài liệu tham khảo hàng đầu trong lĩnh vực này



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Nút Lightning là gì?



Hãy quay lại những điều cơ bản: trước khi định nghĩa node là gì, chúng ta cần hiểu Lightning Network là gì. Đó là một giao thức lớp trên cùng, được xây dựng trên nền tảng Bitcoin, được thiết kế để cho phép các giao dịch BTC [ngoài chuỗi](https://planb.academy/resources/glossary/offchain) (offchain) diễn ra nhanh chóng (với độ hoàn tất gần như tức thì) và nhìn chung là không tốn kém. "Ngoài chuỗi" (offchain) có nghĩa là các giao dịch được thực hiện trên Lightning không nhằm mục đích xuất hiện trên [chuỗi khối](https://planb.academy/resources/glossary/blockchain) Bitcoin chính. Lightning cũng là một phần phản ứng trước việc sử dụng Bitcoin ngày càng tăng và tình trạng tắc nghẽn [trên chuỗi](https://planb.academy/resources/glossary/onchain) (onchain), điều này đang làm dấy lên lo ngại về [khả năng mở rộng](https://planb.academy/resources/glossary/scalability) của hệ thống.



Để hoạt động, Lightning dựa vào việc mở các [kênh thanh toán](https://planb.academy/resources/glossary/payment-channel) giữa các bên tham gia, trong đó các giao dịch có thể được thực hiện gần như tức thời, thường với phí tối thiểu, mà không cần phải đăng ký từng giao dịch một trên chuỗi khối Bitcoin. Các kênh này có thể được mở trong thời gian rất dài, chỉ yêu cầu các giao dịch trên chuỗi khi chúng được mở và đóng.



Một [nút Lightning](https://planb.academy/resources/glossary/lightning-node) là một thành phần tham gia vào mạng Lightning, mở các kênh và thực hiện thanh toán với các nút khác. Nói một cách cụ thể, một nút Lightning là một phần mềm chạy trên máy tính và thực thi giao thức Lightning Network. Ví dụ bao gồm LND, Core Lightning hoặc Eclair. Vai trò chính của phần mềm này là:




- Kết nối với [nút Bitcoin](https://planb.academy/resources/glossary/full-node) để lấy thông tin từ chuỗi khối chính;
- Tạo và quản lý các kênh thanh toán hai chiều với các nút khác;
- Trao đổi tin nhắn với toàn bộ mạng Lightning.



![Image](assets/fr/001.webp)



### So sánh Node và Lightning Wallet: một sự khác biệt quan trọng



Trên Bitcoin (trên chuỗi), "*[wallet](https://planb.academy/resources/glossary/wallet)*" đề cập đến phần mềm quản lý [khóa riêng tư](https://planb.academy/resources/glossary/private-key) của bạn, tính toán số dư từ [UTXO](https://planb.academy/resources/glossary/utxo) và xây dựng các giao dịch của bạn. wallet này có thể dựa trên nút Bitcoin của riêng bạn hoặc của người khác, nhưng hiện nay, vai trò của nút và wallet trên chuỗi là hoàn toàn khác biệt.



Trên Lightning, việc tái sử dụng loại từ vựng này khó hơn mà không gây nhầm lẫn. Thuật ngữ "*Lightning wallet*" khá mơ hồ, bởi vì trên thực tế không tồn tại một Lightning wallet thực sự tự quản lý, trừ khi nó dựa trên một nút mạng. Do đó, chỉ có hai trường hợp có thể xảy ra:



- Để có một node Lightning thực sự (tức là không lưu giữ khóa): phần mềm bạn đang sử dụng (ví dụ: một ứng dụng di động như Phoenix hoặc một phiên bản LND trên Umbrel) thực sự đang chạy một node, và bạn thực sự nắm giữ các khóa để lấy Bitcoin của mình. Trong trường hợp này, "*Lightning wallet*" của bạn thực chất chỉ là một giao diện người dùng trên đỉnh của một node Lightning, dù là được nhúng hay từ xa.



- Để sử dụng dịch vụ lưu ký: bạn sử dụng một ứng dụng hiển thị số dư trong [sats](https://planb.academy/resources/glossary/satoshi-sat) trên Lightning, nhưng trên thực tế, số tiền đó nằm trên một node của nhà cung cấp (ví dụ: Wallet of Satoshi). Bạn không có khóa cũng như quyền kiểm soát các kênh. Số dư của bạn chỉ đơn thuần là một mục nhập kế toán trong cơ sở dữ liệu của công ty. Điều này tương tự như việc để bitcoin của bạn trên một sàn giao dịch, với tất cả các rủi ro liên quan. Trong trường hợp này, "*Lightning wallet*" của bạn chỉ đơn thuần là quyền truy cập vào một tài khoản được quản lý bởi một nhà điều hành, người này lại vận hành một node Lightning thực sự.



Vì vậy, không có trường hợp trung gian nào trên Lightning: hoặc bạn có một node (thậm chí là node nhúng) để tự quản lý, hoặc bạn không có, và một công ty sở hữu sats của bạn. Nhưng như chúng ta sẽ thấy trong các chương tiếp theo, hai cách sử dụng này đôi khi khó phân biệt. Ví dụ, Phoenix là một ứng dụng di động nhúng một node Lightning thực sự, nhưng người dùng không nhất thiết phải biết điều đó, vì toàn bộ sự phức tạp trong hoạt động của nó gần như được che giấu hoàn toàn.



### Đây là lời nhắc về cách thức hoạt động của Lightning Network



Trong phần này, tôi sẽ nhắc lại nhanh cách thức hoạt động của Lightning. Một lần nữa, nếu bạn muốn tìm hiểu sâu hơn về các khái niệm lý thuyết, tôi mời bạn tham khảo khóa học LNP 201 chuyên dụng.



#### Kênh thanh toán: mở, cập nhật và đóng



Cốt lõi của mạng Lightning dựa trên các kênh thanh toán hai chiều. Một kênh có thể được mở (tức là tạo), cập nhật khi các giao dịch Lightning diễn ra, và cuối cùng là đóng lại. Từ góc nhìn trên chuỗi, một kênh không gì khác hơn là một [đầu ra](https://planb.academy/resources/glossary/output) [đa chữ ký](https://planb.academy/resources/glossary/multisig) 2/2.



![Image](assets/fr/002.webp)



Từ góc nhìn của Lightning, đây là một kênh thanh toán với [tính thanh khoản](https://planb.academy/resources/glossary/liquidity-lightning) được phân chia giữa hai bên tham gia.



![Image](assets/fr/003.webp)





- Mở kênh:**



Hai nút quyết định mở một kênh. Một trong số chúng cam kết bitcoin trong một giao dịch trên chuỗi gọi là *giao dịch cấp vốn*. Giao dịch này tạo ra một đầu ra dựa trên [kịch bản](https://planb.academy/resources/glossary/script) đa chữ ký 2 trên 2, có nghĩa là việc chi tiêu số tiền này trên Bitcoin yêu cầu [chữ ký](https://planb.academy/resources/glossary/digital-signature) của cả hai nút trong kênh. Trước khi thực hiện giao dịch này, bên cung cấp tiền yêu cầu bên kia ký một *giao dịch rút tiền*, giao dịch này không được thực hiện trên chuỗi, nhưng cho phép bên đó thu hồi tiền của mình trong trường hợp xảy ra sự cố.



![Image](assets/fr/004.webp)





- Giao dịch Commitment:**



Trạng thái của kênh (tức là sự phân phối sats giữa A và B) được biểu thị bằng một *[commitment transaction](https://planb.academy/resources/glossary/commitment-transaction)*, được cả hai nút biết đến nhưng không được phát sóng ngay lập tức trên blockchain. Giao dịch này mô tả cách phân phối lại tiền của kênh trên chuỗi theo các khoản thanh toán được thực hiện trên Lightning.



Với mỗi giao dịch thanh toán Lightning, hai nút mạng sẽ ký một trạng thái mới thay thế trạng thái trước đó. Trạng thái cũ bị thu hồi nhờ cơ chế khóa thu hồi: nếu một trong hai bên cố gắng phát tán trạng thái cũ, bên kia có thể thu hồi toàn bộ số tiền như một khoản phạt.



Ý tưởng quan trọng ở đây là luôn có một giao dịch Bitcoin đã được ký, không được phát sóng trên chuỗi, được lưu giữ bởi các nút và cho phép phân phối lại sats của nhau theo các khoản thanh toán được thực hiện trên Lightning Network.



![Image](assets/fr/005.webp)





- Đóng kênh:**



Một kênh có thể được đóng một cách gọn gàng thông qua hình thức đóng hợp tác, khi cả hai bên đồng ý về trạng thái cuối cùng của kênh, hoặc đơn phương (đóng cưỡng chế) nếu một trong các bên tham gia ngừng hợp tác hoặc không thể liên lạc được. Trong mọi trường hợp, việc đóng kênh diễn ra dưới hình thức một giao dịch trên chuỗi, sử dụng đầu ra 2/2 và phân phối tiền cho các bên tham gia theo trạng thái hợp lệ cuối cùng của kênh.



![Image](assets/fr/006.webp)



Như vậy, Lightning hoạt động như một lớp thứ cấp được neo trên Bitcoin: chỉ một số sự kiện nhất định (việc mở và đóng các kênh) mới xuất hiện trên chuỗi khối chính. Các khoản thanh toán trung gian vẫn nằm ngoài chuỗi khối.



Trước khi đi sâu hơn, đây là hai khái niệm thiết yếu để hiểu cách quản lý kênh Lightning:




- Liquidity*: lượng sats có sẵn ở một bên kênh;
- *[Dung lượng](https://planb.academy/resources/glossary/lightning-channel-capacity)*: đó là tổng số tiền bị khóa trong đầu ra đa chữ ký 2/2, tức là tổng lượng thanh khoản ở cả hai phía của kênh.



#### Một mạng lưới các kênh và tính thanh khoản



Kênh không chỉ dùng để thanh toán giữa hai nút: nó là một phần của mạng lưới toàn cầu gồm các kênh liên kết với nhau. Nút của bạn có thể định tuyến thanh toán cho người dùng khác thông qua các kênh của chính nó, và bạn có thể gửi sats đến một nút Lightning mà bạn không có kênh trực tiếp, miễn là tìm thấy được đường dẫn hợp lệ giữa hai nút của bạn.



Mỗi nút đều biết, thông qua giao thức [lan truyền thông tin](https://planb.academy/resources/glossary/gossip), một bản đồ của mạng này: các kênh nào tồn tại, các nút nào được kết nối bằng kênh hai chiều và dung lượng nào được công bố. Để gửi một khoản thanh toán cho người nhận không có kênh trực tiếp, nút của bạn sẽ tính toán một lộ trình gồm nhiều bước nhảy: nút của bạn → nút X → nút Y → nút người nhận. Tại mỗi bước nhảy, khoản thanh toán sẽ đi qua một kênh phải có đủ tính thanh khoản theo hướng thanh toán.



![Image](assets/fr/007.webp)



Do đó, tính thanh khoản của một kênh không đối xứng: một bên có thể bị quá tải, trong khi bên kia gần như trống rỗng. Quản lý tính thanh khoản này, tức là biết sats đang ở đâu và chúng có thể di chuyển theo hướng nào, là một trong những khía cạnh quan trọng nhất của việc vận hành một nút Lightning. Chúng ta sẽ xem xét chi tiết hơn về điều này trong các chương thực hành tiếp theo.



#### HTLC: Vận chuyển tiền thanh toán mà không bị cướp



Để cho phép thanh toán được thực hiện thông qua các nút trung gian mà không cần sự tin tưởng, Lightning sử dụng các [hợp đồng thông minh](https://planb.academy/resources/glossary/smart-contract) có tên là *[HTLC](https://planb.academy/resources/glossary/htlc)* (*Hashed Time-Locked Contracts*). Nói một cách đơn giản, HTLC quy định việc chuyển tiền phụ thuộc vào việc tiết lộ một bí mật, và tích hợp một ràng buộc về thời gian để bảo vệ người gửi trong trường hợp giao dịch thất bại. Do đó, mỗi khoản thanh toán đều phải tuân theo việc trình bày một tiền ảnh (một bí mật có [hàm băm](https://planb.academy/resources/glossary/hash-function) tương ứng với một giá trị đã được thỏa thuận). Nếu người nhận cuối cùng cung cấp tiền ảnh này, họ có thể nhận được tiền, điều này cho phép mỗi nút trung gian thu hồi lại tiền của chính mình.



![Image](assets/fr/008.webp)



Tôi sẽ không đi sâu vào các chi tiết kỹ thuật về cách hoạt động của HTLC, vì chúng không cần thiết cho mục đích của khóa học này. Bạn sẽ tìm thấy lời giải thích chuyên sâu trong khóa học lý thuyết LNP 201. Chỉ cần nhớ rằng HTLC cho phép trao đổi nguyên tử: hoặc giao dịch được hoàn tất và không ai bị thiệt hại trong quá trình định tuyến, hoặc giao dịch thất bại và mỗi người tham gia thu hồi lại số tiền ban đầu của mình. Không có trường hợp nào ở giữa.



### Các triển khai nút Lightning chính



Cũng giống như Bitcoin, có nhiều phiên bản triển khai giao thức Lightning. Một số nhóm độc lập đang phát triển các phiên bản riêng của họ, tất cả đều tương thích với nhau vì chúng tuân thủ cùng một tiêu chuẩn ([BOLT](https://planb.academy/resources/glossary/bolt)). Dưới đây là các phiên bản triển khai chính đang được sử dụng hiện nay.



#### LND (*Lightning Network Daemon*)



LND là một bản triển khai hoàn chỉnh của giao thức Lightning, được viết bằng ngôn ngữ Go và phát triển bởi Lightning Labs.



![Image](assets/fr/009.webp)



#### Tia sét lõi (*CLN*)



Core Lightning (trước đây là *C-Lightning*) là phiên bản được phát triển bởi Blockstream. Nó được viết bằng ngôn ngữ C, với một số thành phần được viết bằng Rust.



![Image](assets/fr/010.webp)



#### Bánh Eclair



Eclair là một hệ thống được viết bằng ngôn ngữ Scala và được phát triển bởi công ty ACINQ của Pháp. ACINQ vận hành một trong những nút định tuyến quan trọng nhất trong mạng Lightning bằng Eclair, và sử dụng hệ thống này làm nền tảng phần mềm cho các sản phẩm của riêng mình, chẳng hạn như ứng dụng Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Bộ công cụ phát triển Lightning*)



LDK (*Lightning Development Kit*) là một bộ công cụ phát triển Rust, được duy trì bởi Spiral (Block, trước đây là Square). Nó không phải là một bộ daemon sẵn sàng sử dụng như LND hoặc CLN, mà là một thư viện dành cho các nhà phát triển muốn tích hợp Lightning trực tiếp vào ứng dụng của họ.



![Image](assets/fr/012.webp)



Trong khóa học LNP202 này, chúng ta sẽ tập trung chủ yếu vào LND: phương thức triển khai được sử dụng phổ biến nhất trong các giải pháp trọn gói dành cho khách hàng tư nhân, chẳng hạn như Umbrel.



Như vậy là phần nhắc lại ngắn gọn về cách thức hoạt động của Lightning đến đây là kết thúc. Một lần nữa, nếu có bất kỳ khái niệm nào bạn chưa hiểu hoặc muốn tìm hiểu sâu hơn trước khi áp dụng chúng vào thực tế, khóa học của Fanis Michalakis là tài liệu tham khảo thiết yếu về chủ đề này:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Tại sao bạn nên tự vận hành node Lightning của riêng mình?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Trả lời câu hỏi này khá đơn giản, vì nó mang tính chất tu từ: nếu không có node riêng, bạn không thực sự sử dụng Lightning nữa, mà chỉ là ảo ảnh về Lightning trên toàn bộ cơ sở hạ tầng của công ty.



Việc sử dụng wallet lưu ký Lightning có nghĩa là về mặt kỹ thuật, bitcoin thuộc về công ty vận hành node. Bạn không nắm giữ khóa riêng tư và không kiểm soát các kênh. Số dư wallet của bạn chỉ là một dòng trong cơ sở dữ liệu của nhà cung cấp dịch vụ. Tình huống này chắc chắn rất thuận tiện cho người mới bắt đầu, và trải nghiệm người dùng thường mượt mà, nhưng câu hỏi cơ bản là: lợi thế của việc sử dụng Bitcoin và Lightning là gì nếu cuối cùng bạn lại từ bỏ chính những khía cạnh làm nên sự khác biệt giữa chúng với các loại tiền tệ và ngân hàng truyền thống?



Hai giá trị cốt lõi của Bitcoin là chủ quyền tiền tệ (không còn phụ thuộc vào cơ quan trung ương để phát hành và nắm giữ) và khả năng chống kiểm duyệt (không thể để bên thứ ba ngăn chặn hoặc lọc các khoản thanh toán). Một hệ thống lưu ký trên Lightning đi ngược lại cả hai mục tiêu này: bạn không thể kiểm tra nguồn cung tiền nội bộ của nền tảng, và theo định nghĩa, một nhà điều hành nắm giữ tất cả các quỹ và tất cả các kênh có thể kiểm duyệt, trì hoãn, ưu tiên hoặc chặn các khoản thanh toán của bạn. Trong những điều kiện này, chúng ta có thể tự hỏi một cách chính đáng, **việc sử dụng bitcoin thông qua Lightning có ý nghĩa gì nếu nó lại tái tạo những mô hình tin tưởng và phụ thuộc tương tự như với các hệ thống tiền tệ nhà nước truyền thống**.



> Điều cần thiết là một hệ thống thanh toán điện tử dựa trên bằng chứng mật mã thay vì sự tin tưởng, cho phép bất kỳ hai bên nào sẵn sàng giao dịch trực tiếp với nhau mà không cần đến bên thứ ba đáng tin cậy.
*Báo cáo trắng Satoshi Nakamoto, Bitcoin


Bỏ qua khía cạnh triết học, những bất lợi cụ thể hơn đối với bạn như sau. Thứ nhất, bạn không có cách nào để xác minh rằng công ty đó thực sự nắm giữ số bitcoin tương ứng với số dư được hiển thị. Công ty đó có thể hoạt động theo hình thức dự trữ một phần, bị tấn công mạng, phá sản hoặc đơn giản là biến mất. Trong trường hợp này, bạn chỉ là một chủ nợ khác, không có gì đảm bảo chắc chắn rằng bạn sẽ lấy lại được tiền của mình.



Thứ hai, công ty phải đối mặt với các rủi ro pháp lý: lệnh cấm, đóng băng quỹ, yêu cầu chặn người dùng hoặc giao dịch, tăng cường giám sát, hoặc thậm chí là cấm hoàn toàn hoạt động tại một số khu vực pháp lý nhất định. Mọi ràng buộc tác động lên nhà cung cấp dịch vụ đều ảnh hưởng đến bạn.



Về mặt bảo mật thông tin, tình hình cũng không khá hơn. Người điều hành hệ thống có thể xem tất cả các giao dịch của bạn: số tiền, tần suất, người nhận, số dư, thói quen chi tiêu. Kết hợp với thông tin do ứng dụng cung cấp và có thể cả phân tích chuỗi dữ liệu cơ bản trên Bitcoin, thông tin này có thể tạo ra một hồ sơ rất chính xác về hoạt động tài chính của bạn. Một lần nữa, điều này hoàn toàn trái ngược với mục tiêu của Bitcoin là giảm thiểu việc giám sát tài chính.



Tin vui là ngày nay, việc vận hành một node Lightning riêng không còn là đặc quyền của các chuyên gia kỹ thuật như hồi cuối những năm 2010 nữa. Các giải pháp tương đối đơn giản đã có sẵn cho người dùng cá nhân, và chúng tôi sẽ giải thích chi tiết hơn ở chương tiếp theo.




## Lựa chọn giải pháp phù hợp cho công việc


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Ngày nay, bạn hoàn toàn có thể có được trải nghiệm người dùng rất gần với wallet quản trị Lightning, trong khi vẫn duy trì quyền tự quản lý. Mục tiêu của chương này là giúp bạn lựa chọn con đường phù hợp nhất với hồ sơ của mình.



### Phương án 1: Không sử dụng Lightning trực tiếp



Giải pháp đầu tiên đơn giản là không sử dụng Lightning trực tiếp, mà sử dụng Bitcoin, [Liquid](https://planb.academy/resources/glossary/liquid-network) hoặc wallet tích hợp tính năng [hoán đổi nguyên tử](https://planb.academy/resources/glossary/atomic-swap). Ví dụ, các ứng dụng Aqua hoặc Bull Bitcoin Wallet sử dụng phương pháp này, cho phép bạn thanh toán [hóa đơn Lightning](https://planb.academy/resources/glossary/invoice-lightning) mà không cần tự vận hành nút Lightning, đồng thời vẫn duy trì quyền tự quản lý.



Nguyên tắc rất đơn giản: tiền của bạn được lưu trữ trong Bitcoin, hoặc on-chain, hoặc trên Liquid, và bạn truy cập chúng thông qua wallet, nơi bạn giữ các khóa theo cách truyền thống. Khi bạn quét hóa đơn Lightning, wallet của bạn sẽ khởi tạo một giao dịch (on-chain hoặc Liquid) đến một dịch vụ hoán đổi nguyên tử. Dịch vụ này sau đó sẽ quản lý khoản thanh toán Lightning thông qua nút mạng của riêng nó, sử dụng bitcoin mà bạn đã cung cấp cho on-chain hoặc thông qua Liquid. Kết quả là, bạn không cần phải tự mình xử lý bất kỳ kênh Lightning nào, nhưng vẫn có thể thanh toán hóa đơn Lightning một cách liền mạch.



![Image](assets/fr/013.webp)



Ưu điểm chính của phương pháp này, so với wallet lưu ký Lightning thông thường, là bạn luôn giữ quyền kiểm soát 100% số tiền của mình. Bitcoin được lưu trữ trên onchain hoặc Liquid wallet của bạn, với [cụm từ ghi nhớ](https://planb.academy/resources/glossary/seed) riêng của bạn. Ngay cả trong quá trình hoán đổi, bạn vẫn giữ được quyền kiểm soát tiền của mình, vì giao dịch hoán đổi là nguyên tử. Nó dựa trên một cơ chế mã hóa đảm bảo chỉ có hai kết quả có thể xảy ra: hoặc giao dịch hoán đổi thành công hoàn toàn, hoặc thất bại và dịch vụ không thể chiếm đoạt tiền của bạn.



Hầu hết các danh mục đầu tư cung cấp loại chức năng này đều dựa vào [Boltz](https://boltz.exchange/) cho phần kỹ thuật của giao dịch hoán đổi.



Giải pháp này cũng mang lại những lợi thế thú vị về mặt bảo mật, đặc biệt khi kết hợp với Liquid. Đối với người mới bắt đầu, việc thiết lập và lưu trữ cũng rất dễ dàng: một cụm từ ghi nhớ kinh điển, không cần kênh, không cần cân bằng thanh khoản...



Mặt khác, phương pháp này cũng có những hạn chế. Thứ nhất, nó không phải là không thể tranh cãi: bạn phụ thuộc vào sự sẵn có và thiện chí của dịch vụ hoán đổi. Nếu dịch vụ đó không còn muốn xử lý tài khoản của bạn, hoặc ngừng hoạt động, bạn sẽ không thể thanh toán hóa đơn Lightning thông qua đó nữa. Sau đó là các khoản phí không nhỏ: bạn phải trả cả [phí giao dịch](https://planb.academy/resources/glossary/transaction-fees) trên chuỗi hoặc Liquid, và phí hoa hồng của dịch vụ hoán đổi. Ngoài ra, nếu phí trên chuỗi tăng mạnh, việc sử dụng Lightning có thể trở nên rất tốn kém.



Vì vậy, đối với việc sử dụng không thường xuyên, nó vẫn có thể chấp nhận được, nhưng đối với người dùng Lightning thường xuyên, tốt hơn hết là nên sử dụng một node Lightning chuyên dụng.



### Phương án 2: Các nút Lightning tích hợp trên tàu



Loại giải pháp thứ hai dựa trên các node Lightning được nhúng trực tiếp vào ứng dụng di động. Phoenix và Wallet đã tiên phong trong mô hình này và vẫn là chuẩn mực. Ngày nay, các dự án khác cũng cung cấp các phương pháp tương tự, chẳng hạn như Zeus (ở chế độ nhúng) hoặc BitKit.



Ý tưởng rất đơn giản: ứng dụng thực sự chạy một node Lightning, nhưng tất cả các thao tác phức tạp đều được xử lý tự động ở chế độ nền. Bạn có giao diện "*Lightning wallet*" với cụm từ ghi nhớ để sao lưu, bạn có thể xem số dư và thanh toán hóa đơn, nhưng bạn không quản lý kênh, tính thanh khoản hoặc hầu hết các tham số.



![Image](assets/fr/014.webp)



Các giải pháp này luôn đảm bảo tính tự quản lý. Khóa kiểm soát tiền là generated và được lưu trữ trên điện thoại của bạn, còn bản sao lưu được thực hiện thông qua seed hoặc cơ chế tương đương. Bạn không chỉ đơn thuần sở hữu một tài khoản với nhà cung cấp dịch vụ, mà thực sự sở hữu bitcoin được khóa trong các kênh thuộc về bạn và không thể bị đánh cắp.



Những ưu điểm của các nút trên tàu LN là rất nhiều:




- Cực kỳ dễ cài đặt và sử dụng;
- Trải nghiệm người dùng gần giống với Lightning wallet được quản lý bởi bên thứ ba, nhưng với khả năng tự quản lý;
- Không cần quản lý thủ công các kênh hoặc tính thanh khoản;
- Sao lưu tương đối đơn giản.



Tuy nhiên, các wallet nhúng này cũng có những hạn chế đáng kể. Thứ nhất, về mặt bảo mật, nhà điều hành dịch vụ (ví dụ: ACINQ trong trường hợp Phoenix) có cái nhìn khá chi tiết về các luồng dữ liệu đi qua nút của bạn: số lượng, tần suất, người nhận, ngay cả khi điều này chắc chắn sẽ được cải thiện, đặc biệt là với việc dần dần áp dụng *Các nút Trampoline*. Thứ hai, bạn phụ thuộc rất nhiều vào nhà điều hành này với tư cách là đối tác Lightning chính của mình. Nếu nút ACINQ không khả dụng (trong trường hợp Phoenix), nếu công ty chịu áp lực pháp lý hoặc thay đổi mô hình kinh doanh, trải nghiệm người dùng của bạn có thể bị suy giảm nghiêm trọng, hoặc thậm chí bị ảnh hưởng.



Cuối cùng, sự đơn giản này cũng có cái giá của nó. Các dịch vụ nút LN nhúng thường tính phí cụ thể cho các khoản tiền gửi, rút tiền hoặc một số hoạt động quản lý kênh nhất định. Theo tôi, mô hình này hợp lý xét về dịch vụ được cung cấp, nhưng đối với việc sử dụng chuyên sâu, nó có thể đắt hơn nhiều so với một nút Lightning thông thường được quản lý tốt.



### Phương án 3: nút Lightning cổ điển



Giải pháp thứ ba, giải pháp mà chúng ta sẽ xem xét kỹ hơn trong khóa học LNP202 này, là vận hành một nút Lightning thông thường trên một máy chủ hoặc thiết bị chuyên dụng.



"Cổ điển" ở đây có nghĩa là bạn tự cài đặt và cấu hình một hệ thống Lightning (ví dụ: LND) trên node Bitcoin của riêng mình. Bạn chọn các peer, mở kênh, quản lý [thanh khoản vào và ra](https://planb.academy/resources/glossary/inbound-capacity), và thiết lập chính sách phí định tuyến.



Xét về tính chủ quyền, đây là giải pháp tốt nhất. Bạn không còn phụ thuộc vào một công ty cụ thể nào cho các kênh hoặc thanh toán của mình: nếu một bên kiểm duyệt bạn hoặc đóng một kênh, bạn có thể mở một kênh khác với một node khác. Nếu một dịch vụ biến mất, sats của bạn vẫn nằm trong các kênh bạn kiểm soát và bạn có thể chuyển chúng về lại trên chuỗi. Bạn cũng có thể tối ưu hóa chi phí dài hạn: một khi các kênh của bạn được định cỡ và quản lý đúng cách, tổng chi phí thanh toán có thể trở nên rất thấp.



Về vấn đề bảo mật thông tin, rõ ràng bạn phải tuân thủ các giới hạn của mô hình hoạt động của Lightning, nhưng bạn không giao toàn bộ hoạt động kinh doanh của mình cho một nhà điều hành duy nhất.



Ngược lại, việc thiết lập một node Lightning truyền thống rõ ràng phức tạp hơn: bạn phải cài đặt, cấu hình, bảo trì, theo dõi cập nhật, hiểu logic của các kênh và chính sách tính phí, quản lý kênh và dòng tiền, v.v. Cấu hình sai, sao lưu cẩu thả hoặc quản lý bất cẩn có thể dễ dàng dẫn đến mất sats. Node này cũng phải hoạt động liên tục.



Đây chính xác là con đường tôi đề xuất bạn nên theo trong khóa học này, đồng hành cùng bạn từng bước để hạn chế rủi ro và xây dựng phương pháp tiếp cận của bạn.



### Giải pháp nào phù hợp với hồ sơ người dùng nào?



Để chọn giải pháp phù hợp với hồ sơ người dùng Lightning của bạn, bạn cần xem xét hai yếu tố: tần suất sử dụng Lightning và mức độ sẵn sàng quản lý kỹ thuật của bạn.



Nếu bạn không thực hiện nhiều giao dịch Lightning một cách thường xuyên, nhưng vẫn muốn có thể thanh toán hóa đơn LN từ điện thoại của mình thỉnh thoảng, mà không cần từ bỏ quyền tự quản lý tiền: thì Bitcoin, Liquid hoặc wallet có chức năng hoán đổi có lẽ là lựa chọn tốt nhất. Bạn vẫn giữ quyền sở hữu tiền của mình, không cần quản lý bất kỳ node nào và chấp nhận mức phí cao hơn một chút để đổi lấy sự đơn giản.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Nếu bạn sử dụng Lightning thường xuyên và muốn hưởng lợi từ một node thực sự, nhưng không muốn mất thời gian quản lý kênh, phí hoặc cơ sở hạ tầng, thì một node Lightning nhúng trên thiết bị di động là một giải pháp tốt. Bạn vẫn giữ quyền kiểm soát tiền của mình, giao diện người dùng vẫn rất dễ sử dụng và tất cả sự phức tạp đều được ẩn đi, đổi lại là sự phụ thuộc đáng kể vào nhà mạng.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Nếu bạn là người dùng trung cấp hoặc cao cấp, sẵn sàng đầu tư thời gian để hiểu và quản lý cơ sở hạ tầng của mình, và muốn kiểm soát tối đa các kênh, tính thanh khoản và chi phí: thì một node Lightning dựa trên máy chủ truyền thống là lựa chọn phù hợp. Đây là giải pháp đòi hỏi khắt khe nhất, nhưng cũng phù hợp nhất với ý tưởng về chủ quyền của Bitcoin.




# Tạo nút Lightning đầu tiên của bạn


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Lắp đặt LND với Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Giờ chúng ta đã xem xét những kiến thức cơ bản về Lightning và các giải pháp hiện có, đã đến lúc đi vào vấn đề chính. Để tham gia khóa học này, bạn cần một nút Bitcoin được đồng bộ hóa với Umbrel. Khóa đào tạo LNP202 này là phần tiếp theo của BTC 202; nếu bạn chưa có nút Bitcoin, tôi khuyến khích bạn tham gia khóa đào tạo khác trước khi quay lại đây sau khi nút của bạn đã được đồng bộ hóa. Tôi đặc biệt khuyên bạn nên tham khảo khóa học đó, vì tôi sẽ không đi sâu vào chi tiết về hoạt động, cấu hình và các biện pháp bảo mật của nó.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Trong chương đầu tiên này, chúng ta sẽ xem xét cách cài đặt LND trên Umbrel của bạn. Cách thức hoạt động của Umbrel khiến bước này rất đơn giản, vì tất cả những gì bạn cần làm là cài đặt một ứng dụng.



Từ trang chủ, hãy mở "App Store" ở cuối giao diện.



![Image](assets/fr/015.webp)



Trong thanh tìm kiếm, nhập `Lightning Node`, sau đó nhấp vào ứng dụng.



![Image](assets/fr/016.webp)



Sau đó nhấp vào nút "Cài đặt" để bắt đầu quá trình cài đặt.



![Image](assets/fr/017.webp)



Từ trang chủ, hãy nhấp vào ứng dụng để mở, sau đó chọn `Thiết lập một nút mới`.



![Image](assets/fr/018.webp)



Bạn được cung cấp một cụm từ ghi nhớ gồm 24 từ. Hãy giữ nó ở một nơi an toàn. Chúng ta sẽ xem xét chi tiết hơn trong chương tiếp theo về cách khôi phục quyền truy cập vào nút Lightning của bạn (đây là một quy trình phức tạp hơn nhiều so với Bitcoin hoặc wallet đơn giản), nhưng hiện tại hãy nhớ rằng cụm từ này đóng vai trò rất quan trọng và phải được lưu giữ hết sức cẩn thận.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Hãy lưu cụm từ này theo cách tương tự như một cụm từ ghi nhớ thông thường: trên một phương tiện vật lý (giấy hoặc kim loại) được cất giữ ở một vị trí an toàn, sau đó nhấp vào nút `TIẾP THEO`.



![Image](assets/fr/019.webp)



Sau đó, nhập các từ trong câu của bạn để kiểm tra xem bạn đã viết đúng chưa.



![Image](assets/fr/020.webp)



Một thông báo cảnh báo sẽ nhắc nhở bạn rằng ứng dụng đang ở phiên bản beta và Lightning Network vẫn là một công nghệ thử nghiệm. Rõ ràng, đừng bao giờ đầu tư số tiền vào node Lightning của bạn mà bạn không sẵn sàng mất.



Sau đó, bạn sẽ đến giao diện chính của nút Lightning. Ở bên trái, bạn sẽ thấy Bitcoin onchain wallet được lưu trữ trên nút của bạn. Đây chính là generated từ cụm từ 24 từ mà bạn vừa lưu.



Ở trung tâm, bạn sẽ thấy Lightning wallet. Nó thực sự đại diện cho [dòng tiền bạn chi ra](https://planb.academy/resources/glossary/outbound-capacity), tức là số bitcoin bạn sở hữu trong các kênh Lightning của mình.



Ở bên phải, bạn sẽ thấy một số thông tin quan trọng về nút của mình:




- Số lượng kết nối và kênh đang mở;
- Tổng dòng tiền chi ra của bạn, tức là số tiền bạn có thể chi tiêu trên lý thuyết cho Lightning;
- Tổng lượng tiền mặt bạn có thể nhận được, tức là số tiền bạn có thể nhận được về mặt lý thuyết trên Lightning.



![Image](assets/fr/021.webp)



Chúng ta hãy bắt đầu bằng cách tùy chỉnh nút của mình. Nhấp vào ba dấu chấm nhỏ ở góc trên bên phải giao diện, sau đó nhấp vào `Cài đặt nâng cao`. Trong menu con `Cá nhân hóa`, bạn có thể đặt tên công khai cho nút của mình (tránh sử dụng tên thật) và chọn màu sắc.



![Image](assets/fr/046.webp)



Sau đó nhấp vào nút màu xanh lá cây "LƯU VÀ KHỞI ĐỘNG LẠI" để khởi động lại node và áp dụng các thay đổi này.



Nút Lightning của bạn hiện đã sẵn sàng mở các kênh đầu tiên để thực hiện thanh toán. Nhưng trước tiên, hãy cùng xem cách bảo vệ sats của bạn!



## Lưu nút Lightning của bạn


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Trước khi gửi sats đầu tiên đến node của bạn, điều quan trọng là phải hiểu cách thức sao lưu hoạt động và những rủi ro liên quan. Không giống như danh mục đầu tư onchain Bitcoin đơn giản, việc sao lưu node Lightning khá phức tạp: chiến lược sai lầm có thể dẫn đến mất vĩnh viễn tiền của bạn. Trong chương này, chúng ta sẽ xem xét những gì thực sự cần được sao lưu và cách Umbrel xử lý quy trình này với LND.



Trong khóa học này, chúng ta sẽ sử dụng phiên bản LND (*Lightning Network Daemon*). Mặc dù các nguyên tắc tương tự nhau ở các phiên bản khác, nhưng các tệp và quy trình khôi phục mà tôi sẽ trình bày là dành riêng cho LND.



### Tôi nên lưu trữ những gì trên một node Lightning?



Trên một nút Lightning, chỉ cứu seed và hy vọng mọi thứ sẽ trở lại bình thường là chưa đủ. Nhiều yếu tố đóng vai trò khác nhau, vì vậy điều quan trọng là phải phân biệt được chúng.



#### seed (*aezeed*)



Khi bạn khởi tạo LND, bạn sẽ nhận được một chuỗi seed gồm 24 từ. Đây là định dạng dành riêng cho LND được gọi là "*aezeed*". Nó không phải là seed BIP39 cổ điển, mặc dù trông rất giống. Từ seed này, LND sẽ suy ra các khóa riêng tư của wallet trên chuỗi của bạn được liên kết với nút Lightning, tức là các địa chỉ mà bạn có thể nhận hoặc chuyển lại bitcoin sau khi kênh bị đóng.



![Image](assets/fr/019.webp)



Do đó, seed này có thể được sử dụng để tạo lại wallet trên chuỗi liên kết với node của bạn và để lấy lại số tiền đã được chuyển về chuỗi (ví dụ: sau khi kênh bị đóng). Mặt khác, chỉ riêng seed không đủ để khôi phục các kênh Lightning của bạn vẫn đang mở, vì nó không chứa thông tin cần thiết về trạng thái của các kênh đó.



#### Cơ sở dữ liệu kênh (`channel.db`)



LND lưu trữ trạng thái chi tiết của các kênh của bạn trong một cơ sở dữ liệu có tên là `channel.db`. Cơ sở dữ liệu này chứa:




- danh sách các kênh đang mở của bạn;
- Những người cùng cấp bậc với bạn và thông tin nhận dạng của họ;
- các commitment transaction cuối cùng cho mỗi kênh (các trạng thái kế tiếp xác định ai sở hữu cái gì trong kênh và cho phép thu hồi tiền trên chuỗi trong trường hợp xảy ra sự cố);
- Thông tin cần thiết để trừng phạt một người đồng nghiệp cố gắng phát tán một báo cáo cũ.



Vấn đề với cơ sở dữ liệu này là nó liên tục thay đổi: mỗi khoản thanh toán, mỗi lần định tuyến, mỗi lần mở hoặc đóng kênh đều làm thay đổi nội dung của nó. Đó là lý do tại sao việc sao lưu thông thường (ví dụ: sao chép định kỳ tệp `channel.db` của bạn) lại nguy hiểm. Nếu bạn khôi phục một phiên bản `channel.db` quá cũ và lắp ráp lại nút với trạng thái lỗi thời này, các đối tác của bạn có thể coi rằng bạn đang phát sóng trạng thái kênh cũ. Trong trường hợp này, giao thức sẽ đưa ra hình phạt: đối tác của bạn có thể thu hồi toàn bộ số tiền trong kênh, như thể bạn đã cố tình gian lận.



Trên thực tế, `channel.db` không phải là một phương tiện sao lưu đúng nghĩa. Nó là trạng thái hoạt động hiện tại của node của bạn. Tình huống duy nhất mà việc sử dụng nó để khôi phục node có ý nghĩa là khi bạn khôi phục cơ sở dữ liệu này trực tiếp từ một máy vừa bị lỗi (ví dụ: một ổ đĩa vẫn có thể đọc được). Trong trường hợp này, bạn khôi phục trạng thái gần nhất và có thể khởi động lại LND trên một máy khác dựa trên cơ sở dữ liệu này, an tâm rằng trạng thái này là cập nhật nhất có thể, vì máy cũ không còn hoạt động nữa. Một tình huống khác mà phương pháp này có thể đóng vai trò là bản sao lưu hữu ích là trong cấu hình hai ổ đĩa, với bản sao động, vĩnh viễn từ ổ này sang ổ kia. Tuy nhiên, loại thiết lập này phức tạp hơn để thực hiện.



Nhưng việc sao chép định kỳ tệp `channel.db` và lưu trữ chúng dưới dạng bản sao lưu để khôi phục sau này là một ý tưởng rất tồi: vào ngày bạn sử dụng chúng, bạn có nguy cơ tự gây thiệt hại cho mình và mất toàn bộ dữ liệu sats.



#### Sao lưu kênh tĩnh (SCB)



Để giúp khôi phục sau sự cố, LND đã giới thiệu cơ chế *Sao lưu kênh tĩnh* (SCB). Đây là một tệp đặc biệt, thường được gọi là `channel.backup`, chứa thông tin tĩnh về các kênh của bạn: các đối tác của bạn là ai, cách liên hệ với họ và kênh của bạn là gì.



Tệp này không chứa trạng thái kênh chi tiết hoặc lịch sử cập nhật. Nó không cho phép bạn mở lại các kênh ở trạng thái chính xác như trước đó, cũng như không cho phép tiếp tục vận hành nút Lightning này. Thay vào đó, vai trò của nó là hoạt động như một điểm neo để yêu cầu các bên tham gia khác giúp bạn đóng tất cả các kênh một cách gọn gàng, và do đó nhận được sats trên chuỗi, với các khóa mà bạn có thể lấy lại nhờ seed. Vì vậy, không giống như tệp `channel.db`, được sửa đổi với mỗi khoản thanh toán hoặc định tuyến, tệp SCB chỉ được cập nhật khi một kênh được mở hoặc đóng.



Khi khôi phục thông qua SCB, quy trình như sau:




- Bạn khôi phục seed của mình (*aezeed*), thao tác này sẽ tạo lại wallet trên chuỗi liên kết với nút Lightning;
- Bạn cung cấp cho LND SCB mới nhất của bạn;
- LND sử dụng SCB để tìm danh sách các thiết bị ngang hàng và các kênh bạn đang sử dụng với họ;
- Nó liên hệ với từng nút mạng, thông báo cho họ rằng bạn đã bị mất dữ liệu và yêu cầu họ "buộc đóng" kênh kết nối với họ để bạn có thể khôi phục phần dữ liệu trên chuỗi của mình.



Ý tưởng là các đồng nghiệp của bạn, khi nhận thấy bạn báo cáo mất dữ liệu, sẽ phát sóng commitment transaction cuối cùng của họ và đóng kênh bắt buộc. Sau khi các giao dịch này được xác nhận, tiền của bạn sẽ xuất hiện trở lại trong danh mục đầu tư trên chuỗi (được liên kết với seed).



Tuy nhiên, cơ chế phục hồi này không hoàn hảo. Thứ nhất, nó không thực sự khôi phục nút Lightning của bạn, vì tất cả các kênh sẽ bị đóng. Khi đó, bạn sẽ phải xây dựng một nút Lightning mới từ đầu. Thứ hai, nó không đảm bảo phục hồi 100%, mặc dù nó làm tăng đáng kể khả năng khôi phục số dư trên chuỗi của bạn trong trường hợp xảy ra sự cố. Thực tế, giao thức phục hồi này phụ thuộc vào sự hợp tác và khả năng hoạt động của các máy chủ ngang hàng: nếu một trong số chúng ngoại tuyến, bị mất dữ liệu hoặc từ chối hợp tác, tiền của bạn có thể bị chặn hoặc thậm chí bị mất vĩnh viễn. Đó là lý do tại sao điều quan trọng là không nên giữ các kênh mở trên nút Lightning của bạn với các máy chủ ngang hàng không thể truy cập được trong thời gian dài. Nếu bạn bị mất dữ liệu vào thời điểm đó và máy chủ ngang hàng vẫn không thể truy cập được, việc phục hồi thông qua SCB sẽ không thể thực hiện được và tiền của bạn sẽ bị mất cho đến khi máy chủ ngang hàng đó hoạt động trở lại (có thể là vĩnh viễn).



Tóm lại, một chiến lược sao lưu Lightning hiệu quả trên LND dựa trên ba trụ cột:




- seed của bạn (*aezeed*), dành cho lớp onchain;
- Hệ thống dự phòng SCB tự động đáng tin cậy;
- Quản lý kênh tốt bằng cách lựa chọn các đối tác đáng tin cậy và chủ động đóng các kênh thường xuyên không thể liên lạc được.



### Umbrel quản lý việc sao lưu dữ liệu từ node LND của bạn như thế nào?



Umbrel cung cấp cơ chế sao lưu đơn giản hóa cho nút LND, dựa chính xác trên SCB. Ý tưởng là giúp bạn tiết kiệm thời gian thao tác với tệp này, tạo bản sao lưu và tự động hóa quy trình ở mức tối đa.



Khi bạn tạo nút của mình trên Umbrel, bạn sẽ nhận được seed, thiết bị này đóng vai trò kép:




- Nó lấy Bitcoin và wallet trên chuỗi liên kết với nút Lightning của bạn;
- Nó được sử dụng để tạo ra mã định danh sao lưu và khóa mã hóa dùng cho việc sao lưu SCB từ xa.



Nhờ cơ chế này, Umbrel tự động tạo bản sao lưu mã hóa của SCB của bạn và lưu trữ trên máy chủ của nó thông qua Tor. SCB được lưu trữ ở dạng mã hóa, nhờ vào khóa được tạo ra từ seed của bạn. Vì vậy, trong trường hợp mất dữ liệu, tất cả những gì bạn cần làm là tạo lại Bitcoin và nút Lightning trên Umbrel, trên cùng một máy hoặc máy khác, sau đó nhập seed của bạn. Sau đó, bạn sẽ có thể truy xuất trạng thái SCB mới nhất từ máy chủ Umbrel, giải mã nó và bắt đầu quá trình khôi phục tiền của mình.



Các bản sao lưu này được mã hóa cục bộ bởi node của bạn trước khi gửi đi, đảm bảo tính bảo mật dữ liệu của bạn: Umbrel không thể đọc nội dung của SCB. Quá trình truyền tải diễn ra thông qua Tor, ngăn chặn việc rò rỉ địa chỉ IP của bạn. Hơn nữa, Umbrel của bạn thêm nhiễu vào lưu lượng truy cập (đệm ngẫu nhiên và các bản sao lưu giả được gửi không đều đặn) để ngăn máy chủ suy luận chính xác thời điểm bạn mở hoặc đóng kênh.



Ưu điểm chính của phương pháp này là nó đơn giản hóa đáng kể việc sao lưu nút Lightning của bạn: bạn chỉ cần sao lưu seed một lần trong quá trình khởi tạo nút. Điều này tiềm ẩn một số rủi ro, vì đây chỉ là bản sao lưu của SCB, nhưng đối với số tiền hợp lý thì đây là một sự thỏa hiệp chấp nhận được.



### Các biện pháp tốt nhất để hạn chế rủi ro mất mát



Ngay cả khi có bản sao lưu Umbrel, một vài thao tác tốt đơn giản cũng có thể giảm đáng kể nguy cơ mất sats:





- Theo dõi tình trạng sẵn sàng của các đồng nghiệp:



Nếu một kênh quan trọng thường xuyên được liên kết với một máy chủ ngang hàng không thể truy cập hoặc không ổn định, việc đóng kênh đó một cách an toàn trong khi nút của bạn vẫn đang hoạt động sẽ an toàn hơn. Việc đóng kênh chủ động, dù là hợp tác hay bắt buộc, sẽ loại bỏ một nguồn gây rắc rối tiềm tàng trong trường hợp khôi phục SCB.





- Tránh tập trung quá nhiều thanh khoản vào các đối thủ không rõ danh tính:



Kênh liên lạc giữa bạn và máy chủ càng rộng, thì độ tin cậy càng quan trọng. Hãy chọn những máy chủ uy tín, có kết nối tốt và hoạt động tích cực để quá trình khôi phục dữ liệu thông qua SCB trong tương lai diễn ra suôn sẻ.





- Bổ sung Umbrel bằng các bản sao lưu cục bộ:



Ngoài tính năng sao lưu tự động của Umbrel, bạn cũng có thể lưu trữ một bản sao mã hóa của tệp SCB (`channel.backup`) trên phương tiện lưu trữ ngoài và cập nhật định kỳ. Tốt nhất, bạn nên cập nhật mỗi khi mở hoặc đóng một kênh. Điều này cung cấp cho bạn giải pháp sao lưu dự phòng nếu vì bất kỳ lý do nào mà dịch vụ sao lưu tự động của Umbrel không khả dụng.





- Quản lý seed của bạn đúng cách



seed và Umbrel của bạn không chỉ khôi phục wallet trên chuỗi khối mà còn tạo ra khóa mã hóa cho các bản sao lưu. Do đó, kẻ tấn công có quyền truy cập vào chúng có thể tiến hành khôi phục và chuyển tiền của bạn sang wallet của hắn, mà không cần phải tiếp cận vật lý với node của bạn.



Vì vậy, nếu bạn cần khôi phục node của mình nhưng không còn seed nữa, bạn sẽ không thể khôi phục được bất cứ thứ gì: tất cả dữ liệu sats của bạn sẽ bị mất. Do đó, điều rất quan trọng là phải sao lưu seed của bạn một cách cẩn thận nhất, chỉ trên phương tiện vật lý (giấy hoặc kim loại), và giữ nó ở một nơi an toàn. Để biết thêm thông tin về cách quản lý seed, vui lòng tham khảo hướng dẫn này:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Làm thế nào để lưu lại nút Lightning của tôi trên Umbrel?



Giờ bạn đã hiểu cách hoạt động của lý thuyết, hãy cùng đi vào chi tiết cụ thể. Từ ứng dụng Lightning Node của bạn (thực chất là LND), hãy nhấp vào ba dấu chấm nhỏ ở góc trên bên phải.



![Image](assets/fr/022.webp)



Có ba yếu tố đáng quan tâm ở đây đối với bản sao lưu:




- Hãy kiểm tra xem tùy chọn "Sao lưu tự động" đã được bật chưa. Thao tác này sẽ tự động gửi tệp SCB đã mã hóa của bạn đến máy chủ của Umbrel.
- Sau đó, bạn có thể chọn gửi qua Tor hoặc mạng thông thường bằng tùy chọn "Sao lưu qua Tor". Như đã giải thích ở các phần trước, tôi đặc biệt khuyên bạn nên sử dụng Tor để bảo vệ tính bảo mật của dữ liệu.
- Cuối cùng, có một nút "Tải xuống tệp sao lưu kênh", cho phép bạn tải xuống tệp "channel.backup", tức là bản sao lưu được mã hóa của SCB, về máy tính của bạn. Điều này cho phép bạn thực hiện thêm các bản sao lưu cục bộ định kỳ, ngoài những bản sao lưu được tự động gửi đến máy chủ Umbrel.



Giờ bạn đã biết cách bảo vệ sats của node Lightning khỏi mất dữ liệu. Trong chương tiếp theo, chúng ta sẽ xem xét cách bảo mật node của bạn trước các nỗ lực gian lận.




## Watchtower: vai trò và thiết lập


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



Trong Lightning, mỗi kênh dựa trên một chuỗi các trạng thái kế tiếp nhau, được biểu thị bằng các commitment transaction chưa được công bố. Với mỗi giao dịch thanh toán hoặc định tuyến Lightning, hai bên tham gia kênh sẽ tạo ra một cặp commitment transaction mới, phản ánh sự phân bổ tiền hiện tại trong kênh. Các commitment transaction cũ sẽ trở nên lỗi thời.



Nếu một trong các bên công bố trạng thái lỗi thời, bên kia có quyền xử phạt và thu hồi toàn bộ số tiền của kênh. Trong chương này, chúng ta sẽ xem xét ngắn gọn cách thức hoạt động của cơ chế này, và sau đó giải thích cách thiết lập ***tháp canh***: một hệ thống để bảo vệ nút Lightning của bạn khỏi các nỗ lực gian lận có thể xảy ra.



### Hiểu cách thức hoạt động của tháp canh


Tại bất kỳ thời điểm nào, mỗi bên tham gia kênh đều có một commitment transaction, nếu được công bố, họ có thể đóng kênh và thu hồi phần tiền của mình. Quá trình này được gọi là *đóng kênh bắt buộc*. Nhưng nếu họ cố gắng công bố một commitment transaction cũ hơn, tương ứng với trạng thái trước đó của kênh khi nó nắm giữ nhiều sats hơn, thì giao dịch này sẽ bị coi là hành vi gian lận. Trong trường hợp này, bên đối tác có thể sử dụng khóa thu hồi được liên kết với trạng thái cũ hơn này để thu hồi toàn bộ số tiền trong kênh, trong khi kẻ gian lận sẽ bị khóa tạm thời bởi cơ chế khóa thời gian.


Hệ thống này có nghĩa là việc công bố trạng thái cũ, tức là cố gắng gian lận, là rất rủi ro: nếu bên kia nhìn thấy giao dịch này trên mempool hoặc trên blockchain trước khi thời gian khóa hết hạn, họ có thể sử dụng khóa thu hồi và lấy lại toàn bộ số tiền. **Do đó, tính bảo mật của kênh Lightning của bạn phụ thuộc vào khả năng phát hiện hành vi gian lận trong khoảng thời gian được quy định bởi thời gian khóa.**



#### Tại sao tháp canh lại cần thiết?



Cơ chế xử phạt chỉ có hiệu lực nếu bên bị thiệt hại có khả năng:




- Theo dõi từng khối Bitcoin mới để xem kênh commitment transaction đã được công bố hay chưa;
- Xác định xem giao dịch này tương ứng với trạng thái hợp lệ cuối cùng hay trạng thái đã bị hủy bỏ;
- Trong trường hợp trạng thái bị thu hồi, cần phát tán giao dịch hợp pháp kịp thời, sử dụng khóa thu hồi để thu hồi toàn bộ số tiền trước khi thời hạn khóa hết hiệu lực.



![Image](assets/fr/023.webp)



Trong trường hợp lý tưởng, nút Lightning của bạn hoạt động trực tuyến 24/7, được đồng bộ hóa và liên tục giám sát chuỗi khối. Vì lý do này, nó có thể tự mình phát hiện hành vi gian lận và phản ứng. Tuy nhiên, trên thực tế, một nút Lightning cá nhân có thể bị tắt, đặc biệt là trong trường hợp mất điện kéo dài hoặc mất kết nối Internet.



Chính trong những khoảng thời gian ngừng hoạt động này, rủi ro trở nên hiện hữu: nếu một người dùng không trung thực đăng tải trạng thái cũ trong khi node của bạn đang ngoại tuyến, và thời gian khóa (timelock) hết hạn mà bạn không có bất kỳ phản hồi nào, thì hành vi gian lận sẽ có hiệu lực. Bạn sẽ mất một phần hoặc toàn bộ số tiền của mình trong kênh.



Watchtower được giới thiệu để giảm thiểu rủi ro này. Watchtower là một dịch vụ bên ngoài, giám sát blockchain thay mặt bạn, quét tìm khả năng công bố trạng thái cũ trên một trong các kênh của bạn và, nếu cần, tự động phát sóng giao dịch phạt thay mặt bạn. Vì vậy, ngay cả khi nút Lightning của bạn ngoại tuyến trong một thời gian dài, miễn là watchtower bạn đang sử dụng hoạt động, nó sẽ có thể bảo vệ tiền của bạn bằng cách giám sát mọi nỗ lực gian lận và áp dụng hình phạt tương ứng ngay khi phát hiện ra.



#### Cách thức hoạt động của một tháp canh



Tháp canh được thiết kế để giảm thiểu thông tin thu thập được về các kênh liên lạc của bạn, đồng thời cung cấp cho nó phương tiện để hành động trong trường hợp xảy ra sự cố:




- Với mỗi trạng thái kênh mới với một nút ngang hàng, nút của bạn sẽ chuẩn bị trước một giao dịch phạt tiềm năng. Trong trường hợp nút ngang hàng này gian lận, giao dịch này sẽ cho phép bạn thu hồi toàn bộ số tiền trong kênh;
- Sau đó, nút của bạn mã hóa giao dịch phạt này bằng cách sử dụng TXID của commitment transaction tương ứng (TXID sẽ được sử dụng nếu kẻ gian lận cố gắng thực hiện hành vi gian lận). Chừng nào chưa có sự đóng lại nào diễn ra, trạm giám sát không thể giải mã giao dịch này, vì nó không biết đầy đủ TXID của giao dịch gian lận;
- Nút của bạn gửi cho tháp giám sát một gói tin chứa giao dịch phạt được mã hóa và một nửa TXID của giao dịch gian lận tiềm năng.



Do TXID được truyền đến trạm giám sát không đầy đủ, nó không thể giải mã giao dịch công lý. Tuy nhiên, nó có thể theo dõi chuỗi khối để tìm TXID khớp với phần nó sở hữu. Nếu phát hiện giao dịch như vậy, nó sẽ cố gắng sử dụng TXID đầy đủ của giao dịch đó để giải mã giao dịch phạt của bạn. Nếu việc giải mã thành công, nó biết đó là hành vi gian lận và ngay lập tức công bố giao dịch phạt cho bạn.



![Image](assets/fr/024.webp)



Do đó, trạm giám sát không thể nhìn thấy chi tiết các kênh của bạn: cả danh tính của những người dùng khác, số dư, hay cấu trúc giao dịch. Nó chỉ thấy các gói dữ liệu được mã hóa. Thông tin duy nhất nó có thể suy ra là tốc độ cập nhật kênh của bạn, vì nó nhận được một gói dữ liệu cho mỗi trạng thái mới, nhưng không thể biết nội dung của nó. Trong trường hợp gian lận, nó chắc chắn sẽ phát hiện ra thông tin kênh bằng cách giải mã giao dịch phạt, nhưng ít nhất thiết bị sats của bạn sẽ được bảo vệ.



Cơ chế này dựa trên một sự thỏa hiệp: bạn ủy quyền cho tháp canh khả năng công bố giao dịch phạt đã được ký trước, nhưng giao dịch này vẫn hoàn toàn không minh bạch đối với tháp canh cho đến khi có hành vi gian lận xảy ra. Tháp canh không thể sửa đổi người nhận hoặc chuyển hướng tiền, vì nó chỉ có một giao dịch đã được ký, với các đầu ra bị đóng băng có lợi cho bạn. Nó cũng không thể biết chi tiết của một kênh trong trường hợp đóng cửa bắt buộc hoặc hợp tác hợp pháp, vì TXID không khớp. Mặt khác, tháp canh vẫn là một bên thứ ba đáng tin cậy tối thiểu: bạn cần dựa vào nó để hoạt động trực tuyến và phát sóng giao dịch công lý của bạn một cách chính xác khi bạn cần.



#### Trở thành một tháp canh



Về lý thuyết, bất kỳ nút Lightning nào cũng có thể hoạt động như một tháp canh cho các nút khác (nếu chúng sử dụng cùng một phương thức triển khai, ví dụ: LND), đồng thời bản thân nó cũng được bảo vệ bởi các nút khác đóng vai trò tương tự. Trong các phần thực hành tiếp theo, tôi sẽ hướng dẫn bạn cách thiết lập cơ chế đơn giản này trên LND của bạn dưới sự điều khiển của Umbrel.


Do đó, một chiến lược thú vị có thể là thỏa thuận với những người bạn tin cậy trong cộng đồng Bitcoin để họ đóng vai trò như "tháp canh" cho nhau. Bạn theo dõi kênh của họ, và họ theo dõi kênh của bạn.



### Hãy tìm một tháp canh vị tha



Nếu bạn không quen biết ai có thể cung cấp dịch vụ tháp canh, có một số tháp canh công cộng vị tha mà bạn có thể kết nối. Ví dụ, trong khóa học LNP202 này, tôi đề nghị bạn kết nối với dịch vụ tháp canh do LN+ và Voltage cùng cung cấp, đây là tháp canh dành cho LND.


Đây là thông tin đăng nhập:



- Thông qua Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Qua mạng thông thường:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Để cảm ơn họ vì đã cung cấp dịch vụ tháp canh miễn phí này, [bạn có thể quyên góp qua Lightning](https://lightningnetwork.plus/donation).


Giờ chúng ta đang sử dụng dịch vụ tháp canh vị tha, hãy xem cách cấu hình nó trên nút LND của chúng ta dưới Umbrel.


### Dựng tháp canh


Từ ứng dụng `Lightning Node`, hãy nhấp vào ba dấu chấm ở góc trên bên phải giao diện, sau đó chọn `Cài đặt nâng cao`.


![Image](assets/fr/025.webp)


Sau đó, vào menu `Watchtower`.


![Image](assets/fr/026.webp)



Kích hoạt tùy chọn `Watchtower Client`, sau đó nhấp vào nút `SAVE AND RESTART NODE`. Chờ LND khởi động lại.


![Image](assets/fr/027.webp)


Sau khi khởi động lại hoàn tất, hãy quay lại menu tương tự và nhập ID của tháp canh vị tha mà bạn chọn vào trường được cung cấp. Sau đó nhấp vào nút `THÊM` để xác nhận. Bạn cũng có thể điều chỉnh tham số `Tỷ lệ phí quét khách hàng Watchtower`: đây là tỷ lệ phí bạn sẵn sàng trả cho một giao dịch công lý có thể được phát sóng bởi tháp canh. Không cần thiết phải chọn tỷ lệ quá cao, nhưng bạn cũng nên tránh tỷ lệ quá thấp, nếu không giao dịch hợp pháp sẽ không được xác nhận kịp thời.


Khởi động lại node của bạn bằng cách sử dụng nút `LƯU VÀ KHỞI ĐỘNG LẠI NODE` để áp dụng các thay đổi này.


![Image](assets/fr/028.webp)



Nếu bạn quay lại menu này, bạn sẽ thấy rằng nút Lightning của bạn hiện đã được bảo vệ bởi tháp canh mà bạn vừa thêm vào.



![Image](assets/fr/029.webp)



Một trạm giám sát tự nguyện thường là đủ, đặc biệt nếu bạn không đầu tư số tiền lớn vào node Lightning của mình và nếu bạn quản lý node tốt (đừng để nó tắt quá lâu). Để tăng cường bảo mật hơn nữa, bạn cũng có thể thêm một vài trạm bằng cách lặp lại quy trình tương tự.



## Mở kênh Lightning đầu tiên của bạn


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Nếu bạn đã đọc đến đây, bạn hẳn đã biết rằng một node Lightning không có kênh kết nối thì giống như một thiết bị wallet trống rỗng: nó tồn tại, nhưng vô dụng. Để có thể gửi hoặc nhận thanh toán, node của bạn phải được kết nối với ít nhất một node khác trong mạng Lightning thông qua một kênh. Trong tương lai, chúng tôi đặc biệt khuyến nghị mở nhiều kênh, vì lý do khả năng phục hồi và hiệu quả định tuyến. Trong các chương tiếp theo, chúng ta cũng sẽ xem xét cách quản lý tài sản thanh khoản, tối ưu hóa cấu trúc kênh và sử dụng các công cụ nâng cao hơn giao diện LND cơ bản trên Umbrel.



Nhưng trong chương giới thiệu này, mục tiêu đơn giản là hiểu cách chọn một thiết bị Lightning peer tốt, tìm thông tin cần thiết để chọn peer của bạn ở đâu, và cuối cùng là cách mở kênh đầu tiên của bạn thông qua giao diện LND cơ bản.



### Làm thế nào để chọn một máy chủ Lightning phù hợp?



Khi mở một kênh, bạn cần chọn một nút ngang hàng: một nút Lightning khác mà nút của bạn sẽ được kết nối trực tiếp thông qua kênh. Việc lựa chọn nút ngang hàng này rất quan trọng, vì nó sẽ ảnh hưởng trực tiếp đến:




- giúp cho các khoản thanh toán của bạn được chuyển đến đúng nơi một cách dễ dàng;
- Độ tin cậy của các kênh của bạn theo thời gian;
- chi phí định tuyến của bạn.



Không có gì là hoàn toàn phù hợp với tất cả mọi người, nhưng có một số tiêu chí đáng tin cậy để xác định các ứng viên phù hợp.



#### 1. Kết nối nút



Một nút ngang hàng tốt là một nút được kết nối tốt với mạng Lightning. Điều này có nghĩa là không chỉ có số lượng kênh lớn (mặc dù đây có thể là một chỉ báo), mà trên hết là được kết nối với các nút đáng tin cậy khác và chiếm vị trí đủ trung tâm trong biểu đồ mạng.



Một nút mạng được kết nối tốt sẽ làm tăng khả năng tìm được tuyến đường hiệu quả đến hầu hết các điểm đến thanh toán. Điều này cũng làm giảm số lượng các nút trung gian cần thiết, giúp giảm chi phí.



Ngược lại, việc mở kênh đầu tiên của bạn đến một nút bị cô lập hoặc kết nối yếu có thể hạn chế các khả năng của bạn: bạn có thể thanh toán cho nút này, nhưng sẽ khó khăn hơn nhiều để thanh toán cho phần còn lại của mạng.



#### 2. Vốn hóa và năng lực kênh phân phối



Một nút ngang hàng tốt cũng là một nút có đủ vốn. Điều này được thể hiện bằng tổng dung lượng kênh của nó (tổng sats được phân bổ cho tất cả các kênh) và dung lượng kênh trung bình của nó (thường thì việc có một vài kênh có vốn tốt sẽ hiệu quả hơn là nhiều kênh nhỏ).



Một nút mạng có dung lượng quá lớn, hoặc có tất cả các kênh đều nhỏ, sẽ không thể định tuyến các khoản thanh toán có giá trị lớn, dẫn đến lỗi định tuyến đối với bạn.



#### 3. Chính sách chi phí



Mỗi nút mạng tự đặt phí định tuyến riêng (`phí cơ bản` và `tỷ lệ phí`). Một nút mạng tốt sẽ không tính phí quá cao cho các kênh chiến lược. Đối với kênh đầu tiên, tốt nhất nên chọn một nút mạng có phí tương đối vừa phải để không gây khó khăn cho việc thanh toán của chính bạn.



Hãy nhớ rằng phí định tuyến của chính bạn cũng ảnh hưởng đến cách người khác nhìn nhận bạn: một nút mạng liên tục thay đổi phí hoặc áp đặt các khoản phí vô lý hiếm khi được đánh giá cao.



#### 4. Sự ổn định và thâm niên



Tính ổn định của máy chủ ngang hàng là một tiêu chí rất quan trọng. Một máy chủ tốt có thời gian hoạt động cao (rất hiếm khi ngoại tuyến), giữ cho các kênh của nó mở trong thời gian dài và không liên tục mở/đóng các kênh một cách vô lý.



Các kênh cũ và vẫn đang hoạt động là một tín hiệu tốt: chúng cho thấy mối quan hệ này có lợi cho bên kia, rằng nút mạng biết cách quản lý vốn của mình và không bị đóng bất cứ lúc nào, vì vậy bạn không phải liên tục trả phí trên chuỗi cho việc đóng và mở lại.



Ngược lại, một người dùng thường xuyên ngoại tuyến hoặc nhanh chóng đóng kênh liên lạc có thể gây ra rắc rối cho bạn và phát sinh thêm chi phí khi mở các kênh mới.



Ngay cả với những tiêu chí này, bạn cũng sẽ không thể đưa ra lựa chọn hoàn hảo ngay lần đầu tiên. Điều đó là bình thường: chất lượng thực sự của một người dùng được thể hiện qua cách họ sử dụng sản phẩm. Vì vậy, điều quan trọng là:




- Theo dõi hoạt động kênh (khối lượng định tuyến, tính khả dụng, v.v.);
- Đóng các kênh không có mục đích sử dụng hoặc các kênh có người dùng thường xuyên ngoại tuyến;
- Hãy phân bổ lại vốn của bạn vào những đối tác tốt hơn theo thời gian.



Ý tưởng không phải là mở và đóng các kênh mỗi ngày (điều này sẽ tốn kém về chi phí trên chuỗi), mà là dần dần phát triển cấu trúc mạng của bạn để hội tụ vào một tập hợp các nút mạng đáng tin cậy, được kết nối tốt và tương thích với nhu cầu của bạn.



### Tôi có thể tìm người cùng trình độ như thế nào?



Để áp dụng các tiêu chí này, bạn cần các công cụ cung cấp khả năng hiển thị mạng Lightning. Có một số trình khám phá và dịch vụ có sẵn để thực hiện việc này. Trong số các trình khám phá Lightning nổi tiếng nhất là [1ML](https://1ml.com/) và [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Tuy nhiên, ở đây tôi đề nghị bạn sử dụng [công cụ Lightning Terminal từ Lightning Labs](https://terminal.lightning.engineering/), công cụ này cung cấp bảng xếp hạng (mặc dù dựa trên một số tiêu chí chủ quan) các nút Lightning được coi là phù hợp nhất để mở kênh.



![Image](assets/fr/030.webp)



Vấn đề với các node Lightning lớn nhất ở đầu bảng xếp hạng này là hầu hết chúng không chấp nhận mở kênh với số tiền dưới mức rất cao. Nhiều node cũng áp dụng các chính sách quản lý ngang hàng nghiêm ngặt, điều này có thể dẫn đến việc kênh của bạn bị đóng. Mặt khác, các node này thường không cần thanh khoản đến, do số lượng kết nối khổng lồ của chúng.



Do đó, tôi khuyên bạn nên xem xét các nút mạng theo thứ hạng giảm dần để tìm một nút có kết nối tốt, đáng tin cậy và đủ trung tâm trong biểu đồ mạng, mà không quá lớn. Ví dụ, ở đây tôi đã xác định được nút Lightning trên stacker.news, nút này có kết nối rất tốt, dung lượng cao và chiếm vị trí trung tâm trong biểu đồ mạng.



![Image](assets/fr/031.webp)



Một cách tiếp cận thú vị khác là mở kênh liên lạc với một bên cần nguồn vốn đầu vào, chẳng hạn như một thương nhân mà bạn quen biết, một hiệp hội hoặc một cộng đồng. Chiến lược này có ba ưu điểm:




- Vì thực thể được chọn cần nguồn vốn đầu vào, nên về mặt logic, họ sẽ ít có động lực để đóng kênh của bạn mà không có lý do chính đáng;
- Hoạt động kinh tế của nó làm tăng khả năng định tuyến trên kênh này, và do đó thu được một số khoản phí;
- Bạn đang giúp ích cho hệ sinh thái và đóng góp giá trị cho những người dùng Bitcoin khác.



Sau khi xác định được một node phù hợp, bạn có thể lấy ID Node của nó. ID này đơn giản là sự kết hợp của khóa công khai của node, dấu phân cách `@`, địa chỉ IP hoặc địa chỉ Tor của node và cổng được sử dụng. Bạn có thể dễ dàng truy cập ID này từ hồ sơ của node trên bất kỳ trình khám phá Lightning nào.



### Mở kênh đầu tiên của bạn thông qua LND



Giờ chúng ta đã xác định được nút cần thiết để mở kênh đầu tiên, chúng ta cần sats khóa vào đó. Để làm được điều này, bạn cần cung cấp cho Bitcoin wallet trên chuỗi được liên kết với LND của bạn.



Từ giao diện chính LND, hãy tìm `Bitcoin Wallet` của bạn, sau đó nhấp vào nút `Nạp tiền`. Địa chỉ nhận trên chuỗi sẽ là generated: hãy gửi sats đến địa chỉ này. Số tiền bạn cần chuyển phụ thuộc vào dung lượng bạn muốn phân bổ cho kênh đầu tiên của mình, nhưng hãy nhớ rằng bạn cần gửi nhiều hơn một chút so với dung lượng mục tiêu. Ví dụ, nếu bạn muốn mở kênh 500.000 sats, đừng gửi chính xác 500.000 sats, mà hãy gửi một số tiền cao hơn.



![Image](assets/fr/032.webp)



Sau khi giao dịch được phát sóng, nó sẽ hiển thị trên giao diện. Hãy đợi xác nhận trước khi mở kênh. Bạn sẽ thấy một mũi tên màu xanh lá cây bên cạnh khi giao dịch được xác nhận.



![Image](assets/fr/033.webp)



Cuộn xuống giao diện chính, sau đó nhấp vào `+ MỞ KÊNH`.



![Image](assets/fr/034.webp)



Nhập `Node ID` của node bạn muốn mở kênh, chỉ định số tiền bạn muốn khóa, sau đó điều chỉnh phí giao dịch mở kênh theo trạng thái của thị trường phí onchain. Tất nhiên, hãy đảm bảo bạn có đủ tiền trong danh mục đầu tư onchain LND của mình trước đó.



Sau khi đã thiết lập tất cả các thông số, hãy nhấp vào nút `MỞ KÊNH`.



![Image](assets/fr/035.webp)



Hãy đợi giao dịch mở tài khoản được xác nhận trên chuỗi. Kênh đầu tiên của bạn hiện đã chính thức hoạt động: chúc mừng!



Như bạn thấy, hiện tại, 100% thanh khoản của kênh đang nằm về phía tôi: điều này là bình thường, vì tôi là người đã mở kênh. Khi các phương thức thanh toán và định tuyến phát triển, sự phân bổ này sẽ thay đổi, nhưng tổng dung lượng của kênh sẽ luôn giữ nguyên.



![Image](assets/fr/036.webp)



Giờ bạn đã có kênh, bạn có thể thực hiện các khoản thanh toán Lightning đầu tiên, miễn là nút bạn chọn được kết nối đúng cách với mạng. Tất nhiên, trong các chương sau, chúng ta sẽ xem xét cách thiết lập phương thức thanh toán hóa đơn Lightning thuận tiện hơn từ điện thoại di động của bạn. Nhưng bây giờ, hãy thử thực hiện khoản thanh toán đầu tiên trực tiếp từ LND đến Umbrel.



Để thực hiện việc này, trong phần `Lightning Wallet`, hãy nhấp vào nút `GỬI`, sau đó dán hóa đơn cần thiết lập.



![Image](assets/fr/037.webp)



Tổng số tiền trên hóa đơn đã được hiển thị. Vui lòng xác nhận thanh toán bằng cách nhấp vào nút "GỬI".



![Image](assets/fr/038.webp)



Nếu tìm thấy tuyến đường hợp lệ, giao dịch thanh toán Lightning đầu tiên của bạn sẽ thành công.



![Image](assets/fr/039.webp)



Nếu chúng ta xem xét sự phân bổ thanh khoản trong kênh, ta thấy rằng bên kia hiện có 5.002 sats ở phía mình. Con số này tương ứng với 5.000 sats của khoản thanh toán mà tôi vừa thực hiện, và anh ấy đã chuyển tiếp đến nút của người nhận. 2 sats còn lại đại diện cho phí định tuyến mà tôi đã trả, vì người nhận đã nhận được chính xác 5.000 sats.



![Image](assets/fr/040.webp)



Để nâng cao độ tin cậy của các khoản thanh toán, rõ ràng là cần phải mở thêm các kênh khác. Tùy thuộc vào mục tiêu của chúng ta, chúng ta cũng cần tìm cách để có thể cung cấp nguồn vốn đầu vào để nhận thanh toán trên Lightning. Đây sẽ là chủ đề của phần tiếp theo.



# Quản lý nút Lightning của bạn


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Xác định cấu hình người vận hành nút của bạn


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Giờ đây, khi nút Lightning của bạn đã được thiết lập và hoạt động, bước tiếp theo là xác định hồ sơ nhà giao dịch của bạn. Đây là một lựa chọn quan trọng, vì nó quyết định chiến lược mở kênh, loại đối tác bạn ưu tiên và cách bạn quản lý thanh khoản.



Trên Lightning, để điều này hoạt động, bạn cần thanh khoản theo đúng hướng. Thanh khoản đi ra tương ứng với khả năng thanh toán của bạn (sats có sẵn ở phía bạn của kênh). Thanh khoản đi vào tương ứng với khả năng nhận của bạn (sats có sẵn ở phía các nút khác). Nói cách khác, hồ sơ của bạn tóm gọn lại thành một câu hỏi đơn giản: phần lớn thời gian, sats của bạn đang rời khỏi nút của bạn hay đang đi vào nút của bạn?



### Người tiêu dùng



Đây là hồ sơ của phần lớn người dùng. Bạn sử dụng node của mình để thực hiện thanh toán Lightning: mua hàng hóa và dịch vụ, thanh toán hóa đơn, gửi tiền boa - tóm lại, sử dụng Lightning như một phương tiện thanh toán nhanh chóng. Mặt khác, bạn nhận được rất ít hoặc chỉ rất ít từ Lightning, ví dụ như một vài khoản quyên góp, hoàn tiền giữa bạn bè hoặc một vài khoản thanh toán nhỏ.



Hồ sơ này dễ quản lý nhất vì nhu cầu chính của bạn là khả năng thanh toán. Về mặt thực tế, điều này có nghĩa là bạn cần thanh khoản đầu ra. Sau khi bạn đã mở một hoặc nhiều kênh có quy mô phù hợp đến các nút ổn định, được kết nối tốt, các khoản thanh toán đầu ra của bạn sẽ tự động chuyển thanh khoản sang phía bên kia của các kênh. Chính sự chuyển động này tạo ra một lượng thanh khoản đầu vào hợp lý một cách tự nhiên. Kết quả là, ngay cả khi bạn không tìm cách nhận tiền thường xuyên, bạn vẫn có thể nhận tiền định kỳ mà không cần thực hiện một chiến lược phức tạp. Vì vậy, bạn không cần phải lo lắng về thanh khoản đầu vào của mình.



Trong khóa học LNP202 này, chúng ta sẽ tập trung vào cấu hình người vận hành nút "người tiêu dùng", vì đây là cấu hình tương ứng với hầu hết người dùng Bitcoin trên mạng Lightning.



### Nhà bán lẻ



Về cơ bản, người bán hàng là đối lập với người tiêu dùng. Mục tiêu chính ở đây không phải là thanh toán mà là thu tiền. Một doanh nghiệp, nhà cung cấp dịch vụ, cửa hàng trực tuyến hoặc điểm bán hàng chấp nhận Lightning sẽ nhận được nhiều khoản thanh toán đến và thực hiện tương đối ít khoản thanh toán đi từ nút này.



Hồ sơ này đòi hỏi khắt khe hơn, vì một khoản thanh toán bị từ chối trên Lightning có thể đồng nghĩa với việc mất đi một giao dịch. Do đó, ưu tiên hàng đầu là thanh khoản đến. Nếu node của bạn không có đủ thanh khoản đến, khách hàng của bạn sẽ thấy các khoản thanh toán của họ thất bại, ngay cả khi họ có đủ tiền, đơn giản vì không có cách nào để chuyển thanh khoản đến bạn đúng hướng.



Thách thức lớn đối với người bán cũng đến từ sự phát triển tự nhiên của các kênh. Nếu bạn chỉ tập trung nhận hàng, các kênh của bạn sẽ dần bị quá tải. Vì vậy, bạn cần các cơ chế để duy trì và làm mới nguồn thanh khoản đến.



Tuy nhiên, có một trường hợp đơn giản hơn: hồ sơ người tiêu dùng/người bán hỗn hợp. Nếu bạn thu tiền trên Lightning, nhưng cũng chi tiêu trên Lightning (chi phí kinh doanh, thanh toán cho nhà cung cấp, hoặc thậm chí chi phí cá nhân), thì các khoản thanh toán đi của bạn sẽ tự động tạo ra dòng tiền vào. Việc quản lý trở nên suôn sẻ hơn, vì các dòng tiền bù trừ cho nhau, và bạn ít cần phải sử dụng các cơ chế nhân tạo được thiết kế chỉ để lấy lại tính thanh khoản dòng tiền vào.



### Bộ định tuyến



Bộ định tuyến này là một cấu hình cụ thể. Nó không sử dụng nút Lightning của mình để thanh toán hoặc thu tiền, mà để định tuyến các khoản thanh toán của người khác và thu phí. Mục tiêu là trở thành một tuyến đường hữu ích, đáng tin cậy và cạnh tranh về mặt kinh tế trong biểu đồ Lightning.



Thành thật mà nói, việc làm router trên Lightning phức tạp hơn vẻ ngoài của nó, và việc đạt được lợi nhuận rất khó. Trước hết, việc mở và đóng kênh rất tốn kém về chi phí trên chuỗi. Để định tuyến hiệu quả, bạn thường phải điều chỉnh cấu trúc mạng, thử nghiệm, đóng các kênh hoạt động kém hiệu quả, mở các kênh mới và thường xuyên cân bằng lại thanh khoản. Thứ hai, cạnh tranh rất khốc liệt: các node lớn, đã được thiết lập sẵn thường chiếm một phần lớn lưu lượng truy cập, và rất khó để giành được chỗ đứng nếu không đầu tư một lượng vốn đáng kể vào các kênh có quy mô lớn.



Ngoài ra còn có yêu cầu vận hành cao. Một nút định tuyến phải cực kỳ ổn định, được giám sát, sao lưu đúng cách và quản lý chặt chẽ. Bạn phải giám sát hiệu suất kênh, điều chỉnh chính sách phí, duy trì thanh khoản cân bằng, quản lý các đối tác và nhanh chóng giải quyết các vấn đề kỹ thuật. Mức độ tham gia này có thể thú vị như một sở thích kỹ thuật hoặc như một đóng góp cho cơ sở hạ tầng, nhưng nếu mục tiêu của bạn chỉ đơn giản là sử dụng Lightning một cách độc lập, thì việc tham gia định tuyến để kiếm tiền hiếm khi có liên quan. Đó là lý do tại sao khóa học LNP202 này không đi sâu vào khía cạnh này.



### Hãy xác định rõ vị trí của bạn trước khi tiếp tục



Nếu bạn thuộc nhóm người tiêu dùng, ưu tiên của bạn sẽ là khả năng thanh toán đáng tin cậy với quy trình quản lý đơn giản. Nếu bạn là người bán hàng, ưu tiên của bạn sẽ là thu tiền mặt không gặp sự cố, điều này ngụ ý một chiến lược thu hút thanh khoản đầu vào. Nếu bạn đang cân nhắc định tuyến thanh toán, bạn cần xem xét nó như một hoạt động đòi hỏi nhiều nỗ lực, tiềm ẩn rủi ro kinh tế và tốn nhiều thời gian.



Việc xác định hồ sơ này ngay bây giờ sẽ giúp bạn tránh được một lỗi thường gặp: áp dụng chiến lược kênh được thiết kế cho người bán hoặc nhà mạng, trong khi bạn chỉ là một người dùng muốn thanh toán.



## Sử dụng trình quản lý nút Lightning


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



Trong phần trước của khóa đào tạo LNP202 này, chúng ta đã sử dụng giao diện cơ bản của ứng dụng `Lightning Node` trên Umbrel. Giao diện này đủ dùng cho các thao tác thiết yếu (kiểm tra số dư, xem phân phối tiền mặt, mở và đóng kênh), nhưng nó được đơn giản hóa một cách có chủ ý. Sự đơn giản này hạn chế các tùy chọn có sẵn và không cho phép truy cập vào nhiều tính năng nâng cao của nút LND của bạn. Vì lý do đó, bây giờ chúng ta sẽ sử dụng một phần mềm quản lý nút Lightning toàn diện hơn.



Phần mềm bổ sung này chỉ đơn giản là một giao diện quản lý hỗ trợ cho node của bạn. Điều này có nghĩa là bạn có thể tiếp tục sử dụng giao diện `Lightning Node` song song, và thậm chí sử dụng nhiều giao diện khác nhau nếu muốn. Đây chỉ đơn giản là những cách khác nhau để tương tác với cùng một Lightning node.



Trong số những chương trình phần mềm nổi tiếng nhất có thể kể đến:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Cả ba đều là những giải pháp tốt. Nếu muốn, bạn có thể thử cả ba với node của mình trước khi chọn giải pháp phù hợp nhất. Cá nhân tôi sử dụng ThunderHub vì thói quen và vì nó có vẻ hoàn thiện hơn các giải pháp khác. Đây là công cụ tôi sẽ giới thiệu trong khóa đào tạo này, nhưng bạn cũng có thể chọn một trong hai lựa chọn thay thế còn lại. Chúng tôi có hướng dẫn riêng cho từng chương trình này trên Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Cài đặt ThunderHub



Tất cả các chương trình này đều có thể được cài đặt rất dễ dàng từ App Store của Umbrel. Như tôi đã nói, chúng ta sẽ sử dụng ThunderHub ở đây, nhưng nếu bạn muốn thử nghiệm một thiết bị khác sau này, quy trình sẽ tương tự.



![Image](assets/fr/041.webp)



Umbrel cung cấp cho bạn mật khẩu mặc định để truy cập ThunderHub. Hãy sao chép mật khẩu đó: bạn sẽ cần nó ngay lập tức. Nhớ lưu mật khẩu này vào trình quản lý mật khẩu của bạn, vì bạn sẽ được yêu cầu nhập mật khẩu mỗi khi mở phần mềm.



![Image](assets/fr/042.webp)



Nhấp vào `Đăng nhập`, sau đó dán mật khẩu do Umbrel cung cấp để đăng nhập.



![Image](assets/fr/043.webp)



Sau đó, bạn sẽ được chuyển đến trang chủ ThunderHub, nơi hiển thị các thông tin chính về nút Lightning của bạn.



![Image](assets/fr/044.webp)



Trước tiên, tôi khuyên bạn nên kích hoạt xác thực hai yếu tố (2FA). Trong phần cài đặt, chỉ cần nhấp vào `Bật` bên cạnh `Bật 2FA`, sau đó làm theo các bước thông thường.



![Image](assets/fr/045.webp)



### Sử dụng ThunderHub



ThunderHub tương đối dễ học. Tất cả các menu đều có thể truy cập từ cột bên trái của giao diện. Tóm lại, đây là chức năng của từng menu:




- Trang chủ: Tổng quan về nút, số dư và các thao tác nhanh;
- Bảng điều khiển: bảng điều khiển có thể tùy chỉnh với các tiện ích và số liệu;
- Các nút ngang hàng: xem và quản lý các kết nối đến các nút Lightning khác;
- kênh: quản lý kênh hoàn chỉnh (thanh khoản, phí, đóng kênh, v.v.);
- "Tái cân bằng": một công cụ để tái cân bằng các kênh thông qua thanh toán tuần hoàn;
- Giao dịch: lịch sử các khoản thanh toán Lightning đã gửi và nhận;
- `forwards`: thống kê định tuyến và chi phí generated bởi nút của bạn;
- `Chain`: Danh mục đầu tư onchain Bitcoin (UTXO và các giao dịch);
- Tích hợp gW-201 cho mục đích giám sát và sao lưu;
- `Công cụ`: các công cụ nâng cao (sao lưu, báo cáo, bánh macaron, chữ ký, v.v.);
- Trao đổi: Trao đổi Lightning/trên chuỗi thông qua Boltz;
- `Thống kê`: Thống kê tổng thể và hiệu suất của node Lightning của bạn.



Với bộ chức năng này, bạn có đầy đủ công cụ cần thiết để quản lý nút Lightning của mình một cách hiệu quả. Không nhất thiết phải nắm vững mọi tùy chọn ngay lập tức: chúng ta sẽ cùng khám phá chúng dần dần trong suốt khóa học này. Tuy nhiên, nếu bạn muốn hiểu sâu hơn về phần mềm, hãy xem hướng dẫn ThunderHub của chúng tôi:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Mục mà chúng ta quan tâm nhất ở đây là `Kênh`. Mục này cung cấp cái nhìn chi tiết về tất cả các kênh trong node của bạn, cùng với sự phân bổ thanh khoản của chúng. Cụ thể, bạn có thể thấy kênh nào đang mở trong mục `Mở`, kênh nào đang chờ được mở hoặc đóng trong mục `Đang chờ`, và kênh nào đã đóng trong mục `Đã đóng`.



![Image](assets/fr/047.webp)



Đối với một kênh cụ thể, bạn có thể nhấp vào tên hoặc ID kênh của người dùng để mở trang Amboss của người dùng đó và xem thêm thông tin. Bạn cũng có thể nhấp vào biểu tượng bút chì để sửa đổi các tham số của kênh, bao gồm cả chính sách phí áp dụng cho kênh đó nếu nút của bạn định tuyến các khoản thanh toán đến nút của người dùng kia.



![Image](assets/fr/048.webp)



Nếu bạn chủ yếu sử dụng nút Lightning của mình như một "người tiêu dùng", bạn không cần thay đổi các khoản phí này: bạn có thể giữ nguyên các giá trị mặc định. Mặt khác, nếu bạn muốn hiểu rõ hơn về cách thức hoạt động của phí định tuyến trên Lightning, tôi khuyên bạn nên tham gia khóa đào tạo LNP 201, và đặc biệt là chương 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bằng cách nhấp vào dấu X nhỏ bên cạnh một người dùng khác, bạn có thể bắt đầu đóng kênh giao dịch. Ví dụ, nếu bạn nhận thấy một người dùng nào đó thường xuyên không hoạt động, bạn nên đóng kênh này để phân bổ lại vốn của mình cho một người dùng đáng tin cậy hơn.



Khi đó bạn có hai lựa chọn. Lựa chọn đầu tiên, và luôn được ưu tiên hơn, là đóng kênh hợp tác. Bằng cách xác nhận hành động này, nút của bạn yêu cầu nút kia cùng đóng kênh. Nếu họ chấp nhận, bạn có thể phát sóng giao dịch đóng kênh trên chuỗi và thu hồi phần tiền của mình. Ưu điểm của phương pháp này là bạn chọn phí giao dịch trên chuỗi, do đó tránh được các chi phí không cần thiết, và tiền được thu hồi nhanh hơn, không bị khóa thời gian.



![Image](assets/fr/049.webp)



Phương án thứ hai là đóng cửa bắt buộc. Trong trường hợp này, bạn không cần xin phép đối tác và trực tiếp phát sóng commitment transaction cuối cùng mà bạn đang sở hữu. Tôi không khuyến khích phương pháp này trừ khi đó là biện pháp cuối cùng, ví dụ như nếu đối tác liên tục từ chối đóng cửa hợp tác hoặc không còn phản hồi. Đóng cửa bắt buộc có hai nhược điểm chính: phí thường rất cao, vì chúng đã được thiết lập trước để dự đoán sự tăng phí trên chuỗi, và có sự chậm trễ trong việc thu hồi tiền, vì chúng bị khóa bởi khóa thời gian. Khóa thời gian này cho phép đối tác của bạn có thời gian phản ứng trong trường hợp có hành vi gian lận (điều này rõ ràng không xảy ra ở đây, nhưng bạn vẫn phải chờ).



![Image](assets/fr/050.webp)



Cuối cùng, để mở một kênh mới, hãy vào menu `Trang chủ` và nhấp vào `Mở kênh` trong phần `Liquidity`. Sau đó, bạn có thể nhập ID của nút đã chọn, dung lượng kênh, phí định tuyến Lightning mong muốn và phí onchain cho giao dịch mở kênh.



![Image](assets/fr/051.webp)



Đây là những thao tác chính bạn cần thực hiện trên ThunderHub. Chúng ta sẽ khám phá thêm các tính năng khác trong suốt khóa học LNP202 này.



## Thu được nguồn vốn đầu vào


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Như bạn thấy, việc có thanh khoản đầu ra để thực hiện thanh toán trên Lightning không quá phức tạp. Chỉ cần tự mở kênh đến các node khác và bắt đầu gửi sats. Mặt khác, việc có thanh khoản đầu vào để nhận thanh toán trên Lightning phức tạp hơn, vì bạn cần các node khác mở kênh đến bạn hoặc bạn cần tự chuyển thanh khoản bằng cách thực hiện thanh toán.



Nếu bạn chọn hồ sơ "người tiêu dùng", nhìn chung bạn không cần phải lo lắng về dòng tiền vào. Việc sử dụng nút Lightning của bạn chủ yếu hướng đến thanh toán, chứ không phải rút tiền mặt. Chỉ cần thực hiện một vài giao dịch thanh toán Lightning, bạn sẽ tự nhiên tạo ra dòng tiền vào theo thời gian.



Mặt khác, nếu bạn có hồ sơ "thương nhân", tình hình sẽ ngược lại: bạn chủ yếu sẽ thu tiền thanh toán và thực hiện rất ít giao dịch. Vì vậy, bạn không thể chỉ dựa vào các khoản thanh toán của chính mình để có được thanh khoản. Do đó, việc các node Lightning khác mở kênh kết nối với node của bạn trở nên cần thiết. Nhưng làm thế nào để đạt được điều này? Làm thế nào để bạn thuyết phục các nhà điều hành khác giữ vốn cho bạn? Đó chính xác là những gì chúng ta sẽ tìm hiểu trong chương này.



### Mua thanh khoản đầu vào



Như bạn đã biết, cách hiệu quả nhất để khiến ai đó hành động là trả tiền cho họ. Đối với dòng tiền vào node Lightning của bạn, nguyên tắc cũng hoàn toàn tương tự. Cách đơn giản nhất để có được các kênh kết nối đến node của bạn là trả tiền cho dịch vụ và khoản vốn đầu tư cần thiết.



Nếu bạn là doanh nghiệp hoặc nhà bán lẻ, cách tiếp cận này cho phép bạn nhanh chóng có được các kênh đáng tin cậy để thu tiền từ khách hàng mà không gặp trở ngại.



Có nhiều cách để mua thanh khoản vào. Cách mà cá nhân tôi sử dụng và khuyên dùng là nền tảng [Magma](https://magma.amboss.tech/) của Amboss. Nó rất dễ sử dụng, việc mở kênh nhanh chóng và tỷ lệ phí nhìn chung hợp lý. Magma hoạt động như một thị trường với người tạo lệnh và người nhận lệnh, nhưng phiên bản 2 đã đơn giản hóa trải nghiệm rất nhiều: chỉ cần tạo yêu cầu, thanh toán giá qua Lightning, và Magma sẽ tự động khớp với mức giá chào bán tốt nhất hiện có. Sau sáu lần xác nhận trên chuỗi, kênh của bạn với thanh khoản đến sẽ được thiết lập và hoạt động. Đây là cách nó hoạt động:



Hãy truy cập [trang web Magma](https://magma.amboss.tech/buy), vào mục `Mua kênh`.



![Image](assets/fr/052.webp)



Nếu muốn, bạn có thể tạo tài khoản để theo dõi các giao dịch mua hàng của mình, nhưng điều này không bắt buộc. Nếu bạn không tạo tài khoản, Magma sẽ chỉ cung cấp cho bạn một ID phiên, cho phép bạn truy xuất các giao dịch mua hàng của mình sau này.



Sau khi truy cập trang web, hãy điền thông tin cần thiết để mua thanh khoản. Chọn "Một lần" để mua một lần duy nhất, sau đó nhập số tiền bạn sẵn sàng trả cho thanh khoản sắp tới. Số tiền trả càng cao, dung lượng kênh được mở cho node của bạn càng lớn. Ước tính dung lượng kênh được hiển thị bên dưới: đây chỉ là ước tính, vì số tiền cuối cùng sẽ phụ thuộc vào mức giá chào mua tốt nhất mà Magma tìm được, đôi khi cao hơn, đôi khi thấp hơn.



![Image](assets/fr/053.webp)



Sau đó, nhập ID nút của bạn. Bạn có thể tìm thấy ID này, ví dụ, trong menu `ID nút` của ứng dụng `Lightning Node` trên Umbrel.



![Image](assets/fr/054.webp)



Sau khi điền đầy đủ thông tin, hãy nhấp vào nút "Xem lại & mở đơn hàng".



![Image](assets/fr/055.webp)



Nếu bạn chưa tạo tài khoản, Magma sẽ cung cấp cho bạn khóa phiên và tệp sao lưu. Hãy giữ hai mục này ở nơi an toàn, vì chúng sẽ cho phép bạn khôi phục đơn hàng sau này hoặc theo dõi trạng thái đơn hàng trong trường hợp có sự cố. Sau khi đã lưu tệp, hãy nhấp vào nút "Thanh toán bằng Lightning".



![Image](assets/fr/056.webp)



Sau đó, Magma sẽ gửi hóa đơn Lightning qua generate với số tiền bạn đã chọn. Bạn phải thanh toán. Nếu bạn đã có kênh trên nút Lightning của mình, bạn có thể thanh toán trực tiếp từ đó hoặc sử dụng một thiết bị Lightning wallet bên ngoài khác.



![Image](assets/fr/057.webp)



Sau khi thanh toán hoàn tất, giao dịch sẽ hiển thị trạng thái đang xử lý trên giao diện Magma.



![Image](assets/fr/058.webp)



Sau vài phút, yêu cầu được xử lý: một kênh với sats được mở đến nút Lightning của bạn. Sau khi giao dịch mở được xác nhận trên chuỗi, bạn sẽ có quyền truy cập vào lượng thanh khoản đến tương ứng.



![Image](assets/fr/059.webp)



Magma cũng được tích hợp trực tiếp vào ThunderHub. Trong tab `Trang chủ`, cuộn xuống phần `Liquidity` và nhấp vào `Mua Liquidity đến`. Tất cả những gì bạn cần làm là nhập số lượng mong muốn và xác nhận. Bạn không cần phải thanh toán bất kỳ hóa đơn nào theo cách thủ công, vì ThunderHub sẽ tự động xử lý việc thanh toán từ node của bạn.



![Image](assets/fr/060.webp)



Nếu bạn là một thương nhân, loại dịch vụ này đặc biệt phù hợp, vì nó cho phép bạn nhanh chóng nhận được một lượng lớn thanh khoản từ các node đáng tin cậy, đảm bảo rằng khách hàng của bạn sẽ có thể thanh toán cho bạn mà không gặp khó khăn. Mặt khác, nếu bạn là cá nhân hoặc nếu bạn không muốn trả tiền cho thanh khoản, cũng có những giải pháp miễn phí. Hãy cùng xem xét.



### Thanh khoản đầu tư hợp tác



Nếu bạn không phải là nhà giao dịch nhưng vẫn cần một lượng thanh khoản nhất định (ví dụ: để chuẩn bị node khi khởi động, trong khi chờ thanh toán), bạn không nhất thiết phải trả phí. Một trong những giải pháp tôi ưa thích là hợp tác với các nhà điều hành node khác cũng cần thanh khoản đầu vào để mở các kênh Lightning cho nhau. Bằng cách này, việc mở kênh sẽ mang lại cho bạn thanh khoản đầu ra, đồng thời cung cấp cho bạn thanh khoản đầu vào miễn phí (trừ phí onchain khi mở kênh).



Tất nhiên, bạn có thể tự mình sắp xếp việc này trực tiếp với những người cùng sử dụng Bitcoin. Tuy nhiên, có một nền tảng chuyên dụng cho loại mở vòng tròn này: [Lightning Network +](https://lightningnetwork.plus/). Nguyên tắc là không mở hai kênh giữa cùng một người, mà thiết lập các vòng tròn mở với sự tham gia của tối thiểu ba người, hoặc thậm chí nhiều hơn.



Hãy xem một ví dụ để hiểu cách Lightning Network+ hoạt động:




- Một người điều hành nút mạng, có tên là `A`, đăng tải một thông báo cho biết anh ta muốn mở một kênh 1 triệu sats với hai người khác;
- Quảng cáo vẫn hiển thị cho đến khi có thêm người tham gia;
- Sau đó, hai người vận hành, `B` và `C`, cùng tham gia thông báo nút `A`. Tam giác lúc này đã hoàn chỉnh, và giai đoạn khai mạc có thể bắt đầu.
- Nút `A` mở một kênh liên lạc với nút `B`;
- Nút `B` mở một kênh liên lạc với nút `C`;
- Nút `C` mở một kênh liên lạc với nút `A`.



Khi kết thúc hoạt động, mỗi nút có 1 triệu sats thanh khoản đầu ra và 1 triệu sats thanh khoản đầu vào. Mô hình này có thể được mở rộng cho bốn hoặc năm người tham gia.



Tất nhiên, không có cơ chế kỹ thuật nào đảm bảo rằng người tham gia sẽ thực sự mở kênh mà họ đã cam kết tạo ra. Đó là lý do tại sao nền tảng đã thiết lập một hệ thống đánh giá uy tín, dựa trên những đánh giá tích cực khi người điều hành thực hiện đúng cam kết của họ. Và trong trường hợp xấu nhất, nếu bạn gặp phải người không hợp tác, bạn sẽ không mất tiền: bạn chỉ đơn giản là bỏ lỡ một cơ hội thu hút vốn đầu tư.



Giải pháp này đặc biệt phù hợp với hồ sơ "người tiêu dùng", vì nó cho phép bạn nhận được thanh khoản đầu vào miễn phí, đồng thời kết nối nút của bạn với các nhà điều hành nhỏ khác. Mặt khác, nếu bạn là nhà giao dịch, cách tiếp cận này thường không phù hợp: mỗi sat thanh khoản đầu vào yêu cầu chặn một sat thanh khoản đầu ra, và nhu cầu thanh khoản đầu vào lớn của bạn khi đó sẽ dẫn đến việc ràng buộc quá nhiều vốn.



Để sử dụng Lightning Network+, bạn có hai lựa chọn: hoặc sử dụng ứng dụng tích hợp trong Umbrel, hoặc sử dụng trang web truyền thống và tạo tài khoản bằng cách đăng nhập từ thiết bị của bạn. Tôi khuyên bạn nên chọn cách thứ hai, vì ứng dụng tích hợp không cung cấp đầy đủ các chức năng có sẵn.



Truy cập trang web [Lightning Network +](https://lightningnetwork.plus/) và nhấp vào nút `Đăng nhập` ở góc trên bên phải giao diện.



![Image](assets/fr/061.webp)



Để xác thực bản thân, bạn cần ký vào thông điệp được cung cấp bằng khóa riêng của nút Lightning của mình. Với ThunderHub, thao tác này rất đơn giản. Hãy bắt đầu bằng cách sao chép thông điệp được hiển thị bởi LN+.



![Image](assets/fr/062.webp)



Trong ThunderHub, hãy vào tab `Công cụ`, sau đó nhấp vào nút `Ký tên` trong phần `Tin nhắn`.



![Image](assets/fr/063.webp)



Dán thông báo xác thực do LN+ cung cấp, sau đó nhấp vào `Ký`.



![Image](assets/fr/064.webp)



ThunderHub sau đó ký tin nhắn này bằng khóa riêng của nút của bạn. Sao chép chữ ký generated.



![Image](assets/fr/065.webp)



Dán chữ ký này vào ô tương ứng trên trang web LN+, sau đó nhấp vào `Đăng nhập`.



![Image](assets/fr/066.webp)



Bạn hiện đã được kết nối với LN+ bằng node Lightning của mình. Quá trình này cho phép LN+ xác minh rằng bạn là chủ sở hữu hợp pháp của node mà bạn đang yêu cầu trên nền tảng của họ.



![Image](assets/fr/067.webp)



Nếu muốn, bạn có thể cá nhân hóa hồ sơ LN+ của mình, ví dụ như thêm một đoạn tiểu sử ngắn.



Để tham gia vào lần mở kênh vòng tròn đầu tiên, hãy vào menu `Swaps` ở đầu giao diện. Tại đây, bạn sẽ tìm thấy tất cả các giao dịch hoán đổi hiện có, tùy thuộc vào đặc điểm của nút của bạn.



![Image](assets/fr/068.webp)



Để tham gia một đợt trao đổi hiện có, chỉ cần nhấp vào đó và đăng ký. Tuy nhiên, trên LN+, người tạo ra một đợt trao đổi có thể đặt ra một số điều kiện cho người tham gia, chẳng hạn như số lượng kênh tối thiểu hoặc tổng dung lượng node tối thiểu. Do đó, đặc biệt là trong giai đoạn đầu, có thể sẽ có rất ít đợt trao đổi dành cho node của bạn. Trong trường hợp của tôi, mặc dù đã có một vài kênh mở, nhưng không có đợt trao đổi nào dành cho node của tôi. Vì vậy, tôi đã tạo ra đợt trao đổi của riêng mình, và bạn cũng có thể làm như vậy nếu bạn đang ở trong tình huống tương tự.



Nhấp vào `Bắt đầu trao đổi Liquidity`, sau đó nhập các thông số chào giá của bạn:




- Chọn tổng số người tham gia (3, 4 hoặc 5);
- Hãy chỉ định số lượng kênh cần mở (đảm bảo bạn có ít nhất số lượng này trong wallet trên chuỗi của mình);
- Xác định thời gian mở kênh. Đây là khoảng thời gian mà các bên tham gia đồng ý không đóng kênh;
- Ở bên phải, bạn có thể thiết lập các hạn chế cho người tham gia: số lượng kênh tối thiểu, tổng dung lượng tối thiểu và loại kết nối được chấp nhận.



Sau khi đã thiết lập tất cả các thông số, hãy nhấp vào nút `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



Đề nghị hoán đổi của bạn đã được tạo. Bây giờ tất cả những gì bạn cần làm là chờ các nhà điều hành nút khác đăng ký. Nếu các điều kiện của bạn không quá khắt khe, việc này sẽ không mất quá nhiều thời gian. Hãy nhớ theo dõi trạng thái hoán đổi của bạn trong những giờ hoặc ngày tiếp theo.



![Image](assets/fr/070.webp)



Tất cả các vị trí hoán đổi đã được chọn: giờ chúng ta chuyển sang giai đoạn mở kênh. Mỗi người tham gia có thể xem, từ giao diện LN+ của mình, nút nào mà họ cần mở kênh Lightning.



![Image](assets/fr/084.webp)



Về phía bạn, hãy mở kênh bằng cách sử dụng ID nút do LN+ cung cấp và tuân thủ số lượng được chỉ định. Như chúng ta đã thấy trong các chương trước, bạn có thể thực hiện việc này thông qua ThunderHub, với một trình quản lý nút Lightning khác hoặc trực tiếp từ giao diện ứng dụng nút Lightning cơ bản.



![Image](assets/fr/085.webp)



Sau khi quá trình mở kênh được bắt đầu, bạn có thể thấy nó xuất hiện trong phần các kênh đang chờ. Trong trường hợp của tôi, đó là kênh có nút `Plebian_fr`.



![Image](assets/fr/086.webp)



Sau đó, bạn có thể quay lại LN+ để xác nhận rằng bạn đã bắt đầu mở kênh. Chỉ cần nhấp vào nút `Channel Opening Started`.



![Image](assets/fr/087.webp)



Khi tất cả những người tham gia khác cũng đã mở kênh mà họ đã cam kết, hãy nhớ để lại đánh giá tích cực cho họ.



![Image](assets/fr/088.webp)



Trong trường hợp gặp khó khăn hoặc chậm trễ, bạn có thể liên hệ trực tiếp với các bạn cùng lớp thông qua phần bình luận ở cuối trang.



![Image](assets/fr/089.webp)



Một số người tham gia có thể muốn cân bằng lại các kênh luân chuyển ngay từ đầu bằng cách tự thanh toán cho chính mình. Điều này đảm bảo sự phân phối tiền mặt cân bằng trong mỗi kênh. Nếu bạn ở vị trí "người tiêu dùng", điều này không bắt buộc, nhưng bạn có thể tự thực hiện việc cân bằng lại này nếu muốn, hoặc tạm thời đặt phí kênh của mình về 0 để tạo điều kiện thuận lợi hơn cho người khác muốn thực hiện việc đó. Đôi khi không ai muốn làm điều này cả.



![Image](assets/fr/090.webp)




# Khai thác tối đa tiềm năng của nút Lightning của bạn


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Kết nối thiết bị di động wallet thông qua Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Vậy là xong, giờ bạn đã có một node Lightning được kết nối tốt, với cả thanh khoản đến và đi. Vì vậy, bạn đã sẵn sàng sử dụng node Lightning của mình trong thực tế. Cho đến nay, chúng ta luôn sử dụng các giao diện trực tiếp trên Umbrel, hoặc ứng dụng `Lightning Node` hoặc giao diện `ThunderHub`. Các công cụ này hoạt động tốt cho việc gửi và nhận thanh toán, nhưng rõ ràng là không được tối ưu hóa cho các giao dịch thanh toán Lightning hàng ngày. Giao diện được thiết kế để sử dụng trên máy tính, không thực tế trên điện thoại thông minh, và cũng yêu cầu kết nối với cùng một mạng để hoạt động đúng cách (mặc dù về mặt kỹ thuật, có thể kết nối từ xa qua Tor).



Trên thực tế, điều mà chúng ta, những người sử dụng Bitcoin, đang tìm kiếm là một giao diện Lightning wallet cổ điển trên điện thoại thông minh: khả năng quét hóa đơn bằng mã QR và một giao diện đơn giản để thanh toán và rút tiền sats. Đây chính xác là những gì chúng ta sẽ triển khai trong chương này và chương tiếp theo. Ý tưởng chung là có một ứng dụng Lightning wallet di động trên điện thoại thông minh của bạn, có thể được sử dụng ở bất cứ đâu (không chỉ mạng cục bộ của bạn) nhưng, ở chế độ nền, dựa vào nút Lightning của riêng bạn để gửi và nhận thanh toán.



### Các giải pháp để kết nối khách hàng di động là gì?



Hiện nay, có nhiều cách để thực hiện việc này, cả về ứng dụng di động lẫn loại kết nối giữa thiết bị của bạn và ứng dụng đó. Ba chế độ kết nối chính là:




- thông qua ***Tor***;
- thông qua VPN ***Tailscale***;
- thông qua ***NostrWalletKết nối***.



Vài năm trước, tôi từng kết nối qua ***Tor***, nhưng tôi nhanh chóng ngừng lại: số lần lỗi và độ trễ kết nối quá lớn. Về lý thuyết, nó hoạt động, nhưng trên thực tế, trải nghiệm người dùng rất tệ. Vì vậy, tôi khuyên bạn không nên sử dụng phương pháp này.



Giải pháp thay thế mà tôi áp dụng sau đó là sử dụng VPN ***Tailscale*** để đảm bảo liên lạc giữa ứng dụng di động và thiết bị đầu cuối. Giải pháp này hoạt động rất tốt: ngay cả trên mạng di động có băng thông thấp, các khoản thanh toán của tôi vẫn luôn được thực hiện mà không gặp khó khăn. Đây là phương pháp tôi sẽ giới thiệu đầu tiên trong chương này, với ứng dụng Zeus.



Trong chương tiếp theo, chúng ta sẽ xem xét một giải pháp khác, mới hơn, cũng hoạt động rất tốt: ***Nostr Wallet Connect***. Lần này, chúng ta sẽ sử dụng ứng dụng Alby Go để giới thiệu cho bạn một giải pháp thay thế, mặc dù Zeus cũng tương thích với NWC nếu bạn muốn.



### Cài đặt và cấu hình Tailscale



Đối với phương pháp đầu tiên này, chúng ta cần Tailscale. Đây là giải pháp VPN dựa trên WireGuard, cho phép bạn kết nối an toàn các thiết bị trải rộng trên Internet, đồng thời tự động quản lý mã hóa, xác thực và vượt NAT. Nói một cách đơn giản, nó giống như tất cả các thiết bị của bạn được kết nối với cùng một mạng LAN với bộ định tuyến của bạn, ngay cả khi chúng có thể ở bất kỳ đâu trên Internet.



Để sử dụng, trước tiên hãy tạo tài khoản. Truy cập trang web Tailscale, sau đó nhấp vào nút "Bắt đầu".



![Image](assets/fr/071.webp)



Tiếp theo, hãy chọn một nhà cung cấp danh tính cho tài khoản Tailscale của bạn. Cá nhân tôi đã sử dụng một trong các tài khoản GitHub của mình để đăng nhập.



![Image](assets/fr/072.webp)



Sau khi đăng nhập, bạn sẽ được hỏi một vài câu hỏi về cách sử dụng dịch vụ của mình. Hãy trả lời ngắn gọn để tiếp tục.



![Image](assets/fr/073.webp)



Tailscale sau đó đề nghị cài đặt phần mềm khách hàng vào máy tính của bạn. Hiện tại, đó không phải là điều chúng ta quan tâm: hãy truy cập trực tiếp vào Umbrel và cài đặt ứng dụng Tailscale từ App Store.



![Image](assets/fr/074.webp)



Khi ứng dụng mở ra, hãy nhấp vào `Đăng nhập`, sau đó làm theo quy trình xác thực, sử dụng phương pháp tương tự như khi bạn tạo tài khoản.



![Image](assets/fr/075.webp)



Nhấp vào `Kết nối` để xác nhận. Thiết bị Umbrel của bạn hiện đã được kết nối với mạng VPN.



![Image](assets/fr/076.webp)



Sau đó, tải ứng dụng Tailscale về điện thoại thông minh của bạn và đăng nhập bằng cùng một tài khoản. Xin lưu ý: trên Android, không thể sử dụng hai VPN cùng lúc. Để Tailscale hoạt động, bạn cần tắt bất kỳ VPN nào khác đang hoạt động. Hơn nữa, mỗi khi bạn muốn sử dụng nút Lightning của mình thông qua Zeus, bạn cần kích hoạt VPN Tailscale, nếu không kết nối sẽ không được thiết lập.



![Image](assets/fr/077.webp)



Trên thiết bị Tailscale, khi đã có ít nhất hai máy khách được kết nối, bạn có thể truy cập vào bảng điều khiển quản trị với danh sách tất cả các thiết bị được kết nối với mạng và địa chỉ IP Tailscale của chúng.



![Image](assets/fr/078.webp)



### Kết nối Zeus



Cài đặt ứng dụng Zeus trên điện thoại của bạn. Khi ứng dụng mở ra, chọn `Thiết lập nâng cao`, sau đó chọn `Tạo hoặc kết nối wallet`.



![Image](assets/fr/079.webp)



Trong phần `Giao diện Wallet`, hãy chọn `LND (REST)`. Sau đó, nhập địa chỉ Tailscale của Umbrel, bạn có thể tìm thấy địa chỉ này từ bảng điều khiển Tailscale hoặc trực tiếp trong ứng dụng Tailscale trên Umbrel. Đối với cổng, hãy nhập `8080`.



![Image](assets/fr/080.webp)



Zeus sau đó yêu cầu bạn cung cấp một "Macaroon". Đây là một ủy quyền token cho phép bạn xác định chính xác các quyền được cấp cho một ứng dụng (trong trường hợp này là Zeus) để tương tác với nút Lightning của bạn. Có thể lấy một macaroon bằng generate từ ThunderHub, trong menu "Công cụ", menu con "Tiệm bánh", nhưng để làm điều này, cách dễ nhất là lấy trực tiếp từ ứng dụng "Nút Lightning".



Nhấp vào ba dấu chấm nhỏ ở góc trên bên phải giao diện, sau đó nhấp vào `Kết nối Wallet`. Chọn `REST (Mạng cục bộ)`. Sau đó, bạn sẽ có thể sao chép một chiếc bánh macaroon với quyền phù hợp.



![Image](assets/fr/081.webp)



Dán nó vào ô tương ứng trong Zeus, sau đó nhấp vào nút `LƯU CẤU HÌNH VÍ`.



![Image](assets/fr/082.webp)



Giờ đây, bạn có thể truy cập vào node Lightning của mình từ ứng dụng Zeus. Điều này có nghĩa là bạn có thể sử dụng hóa đơn generate để nhận thanh toán trực tiếp trên node Lightning từ điện thoại thông minh của mình, và cũng có thể thanh toán hóa đơn Lightning ở bất cứ đâu.



![Image](assets/fr/083.webp)



Mẹo: Tailscale không chỉ giới hạn ở việc sử dụng nút Lightning của bạn từ xa. Nó cho phép bạn truy cập tất cả các công cụ của Umbrel từ phần mềm khác, thậm chí từ xa. Ví dụ: bạn có thể sử dụng địa chỉ IP Tailscale của Umbrel để kết nối nút Bitcoin (thông qua Electrs hoặc Fulcrum) với Sparrow Wallet mà không cần thông qua Tor. Một lần nữa, điều này tránh được sự chậm chạp vốn có của Tor. Chỉ cần cài đặt ứng dụng khách Tailscale trên máy tính của bạn và kết nối nó với mạng.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

Trong chương tiếp theo, chúng ta sẽ xem xét một cách khác, cũng hiệu quả không kém, để kết nối máy khách di động với nút Lightning của bạn: Nostr Wallet Connect. Chúng ta sẽ sử dụng một ứng dụng khác từ Zeus (mặc dù Zeus cũng tương thích với NWC), cụ thể là Alby Go.



## Kết nối thiết bị di động wallet qua NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Nếu bạn chưa tin tưởng vào kết nối Tailscale, hoặc nếu việc quản lý VPN kép có vẻ quá phức tạp, chương này đề xuất một cách khác để sử dụng ứng dụng khách di động từ xa để thanh toán và nhận sats thông qua nút Lightning của bạn: ***Kết nối Nostr Wallet***.



Trong ví dụ này, chúng ta sẽ sử dụng ứng dụng di động Alby Go, được thiết kế rất tốt và đặc biệt dễ học. Tuy nhiên, bạn cũng có thể sử dụng Zeus hoặc bất kỳ ứng dụng di động nào khác tương thích với NWC. Bạn có thể tìm thấy danh sách các ứng dụng tương thích trên kho lưu trữ GitHub [`awesome-nwc`](https://github.com/getAlby/awesome-nwc).



### Chức năng kết nối Nostr Wallet hoạt động như thế nào?



Nostr Wallet Connect là một giao thức tiêu chuẩn cho phép ứng dụng hoặc trang web kích hoạt các hành động trên một nút Lightning từ xa mà không cần thiết lập kết nối mạng trực tiếp với nút đó (không có API LND được phơi bày, không có VPN, không có dịch vụ `.onion`...). NWC định nghĩa cách một ứng dụng tạo ra một ý định (ví dụ: `pay_intece`) và nhận kết quả.



Nó hoạt động khá đơn giản. Bạn khởi tạo một phiên bằng cách quét mã QR hoặc thông qua liên kết sâu `nostr+walletconnect:`. Chuỗi này chứa các tham số phiên và một mã bí mật ủy quyền. Sau đó, khi ứng dụng muốn thanh toán, nó sẽ tuần tự hóa yêu cầu, mã hóa nó và xuất bản nó dưới dạng một sự kiện trên máy chủ chuyển tiếp Nostr. Nút đọc sự kiện trên máy chủ chuyển tiếp, giải mã nó, kiểm tra xem tác giả có được ủy quyền cho phiên này hay không, thực hiện thanh toán, sau đó trả về phản hồi được mã hóa (thành công với tiền ảnh hoặc lỗi). Máy chủ chuyển tiếp chỉ đóng vai trò là trung gian vận chuyển: nó không thể đọc nội dung, nhưng nó có thể quan sát thời gian và tần suất của các yêu cầu.



So với kết nối qua Tailscale hoặc Tor, ưu điểm chính của NWC là nút mạng của bạn không thể truy cập trực tiếp từ bên ngoài. Điều này giúp đơn giản hóa đáng kể việc sử dụng trên thiết bị di động: nút mạng của bạn không cần phải chấp nhận các kết nối đến, nó chỉ cần có khả năng giao tiếp với một máy chủ chuyển tiếp. Mặt khác, bạn sẽ tạo ra sự phụ thuộc chức năng vào các máy chủ chuyển tiếp Nostr: nếu chúng không khả dụng, trải nghiệm sẽ bị suy giảm. Ngoài ra, ngay cả khi các tin nhắn được mã hóa, máy chủ chuyển tiếp vẫn có thể quan sát được một số siêu dữ liệu hoạt động nhất định.



Sự khác biệt về mô hình bảo mật cũng rất quan trọng. Với Tailscale hoặc Tor, bạn cho phép truy cập trực tiếp vào node của mình (thông qua API hoặc LND) được bảo vệ bởi các bí mật cực kỳ nhạy cảm. Điều này rất mạnh mẽ, vì bạn có thể quản lý mọi thứ, nhưng nó cũng tạo ra bề mặt tấn công ở lớp thấp hơn. Với NWC, quyền truy cập mang tính ứng dụng hơn: bạn ủy quyền một phiên token chỉ cho phép thực hiện một số hành động nhất định.



### Cài đặt Alby Hub trên nút Lightning của bạn



Trước đây, có một ứng dụng dành riêng cho kết nối NWC trong App Store của Umbrel, nhưng tiếc là ứng dụng này hiện không còn nữa. Giờ đây, bạn cần sử dụng Alby Hub để thiết lập loại kết nối này. Để làm điều đó, hãy bắt đầu bằng cách cài đặt ứng dụng Alby Hub trực tiếp từ cửa hàng ứng dụng.



![Image](assets/fr/091.webp)



Khi mở chương trình, hãy bỏ qua các màn hình giới thiệu, sau đó nhấp vào nút `Bắt đầu (LND)`. Điều quan trọng là phải kiểm tra xem nó hiển thị `LND`, chứ không phải `LDK`, trong ngoặc. Nếu `LND` xuất hiện, điều này có nghĩa là Alby Hub đã phát hiện chính xác nút Lightning hiện có của bạn và sẽ tự cấu hình làm giao diện cho nó. Mặt khác, nếu `LDK` được hiển thị, điều này cho thấy Alby Hub chưa phát hiện nút của bạn và sắp tạo một nút mới, điều này không phải là mục đích ở đây.



![Image](assets/fr/092.webp)



Sau đó, bạn sẽ được yêu cầu thiết lập tài khoản Alby. Đối với việc sử dụng giới hạn trong NWC, điều này không bắt buộc, nhưng bạn có thể muốn làm như vậy nếu muốn tận dụng các dịch vụ cụ thể của Alby. Nếu không, hãy nhấp vào "Có thể sau" để tiếp tục.



![Image](assets/fr/093.webp)



Tiếp theo, hãy chọn một mật khẩu mạnh và độc đáo. Mật khẩu này sẽ bảo vệ quyền truy cập vào Alby Hub trên máy chủ của bạn. Nhớ lưu mật khẩu này vào trình quản lý mật khẩu của bạn.



![Image](assets/fr/094.webp)



Thao tác này sẽ đưa bạn đến giao diện Alby Hub. Bạn không cần phải thực hiện toàn bộ quá trình cấu hình, trừ khi bạn muốn sử dụng nó làm trình quản lý chính cho node Lightning của mình. Như chúng ta đã thấy trước đó, Alby Hub thực tế có thể thay thế việc sử dụng ThunderHub để quản trị node của bạn. Nếu bạn muốn tìm hiểu thêm về các tùy chọn của Alby Hub, hãy xem hướng dẫn chuyên dụng của chúng tôi:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Vào menu `Kết nối`.



![Image](assets/fr/095.webp)



Tại đây, bạn có thể thấy tất cả các ứng dụng có thể kết nối với nút Lightning của bạn thông qua NWC. Chúng bao gồm Zeus, đã được đề cập trong chương trước. Ở đây, chúng ta sẽ sử dụng Alby Go. Nhấp vào Alby Go, sau đó nhấp vào nút `Kết nối với Alby Go` để bắt đầu quá trình kết nối.



![Image](assets/fr/096.webp)



### Lắp đặt và kết nối Alby Go



Trên điện thoại thông minh của bạn, hãy cài đặt ứng dụng Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



Trong Alby Hub, hãy cấu hình các quyền bạn muốn cấp cho ứng dụng Alby Go trên nút Lightning của bạn. Ví dụ, bạn có thể đặt giới hạn chi tiêu mỗi kỳ, ngày hết hạn cho liên kết NWC hoặc để lại toàn quyền kiểm soát. Sau khi đã thiết lập các tham số, hãy nhấp vào nút `Tiếp theo`.



![Image](assets/fr/097.webp)



Alby Hub sau đó là generate quét mã QR để thiết lập kết nối NWC giữa nút Lightning của bạn và Alby Go.



![Image](assets/fr/098.webp)



Trên ứng dụng Alby Go, khi mở lần đầu, hãy nhấp vào `Kết nối Wallet`, sau đó quét mã QR do Alby Hub cung cấp.



![Image](assets/fr/099.webp)



Hãy chọn một tên để nhận dạng wallet này. Giờ đây bạn đã có quyền truy cập từ xa vào nút Lightning của mình thông qua Alby Go. Bạn có thể sử dụng generate để tạo hóa đơn và nhận sats trên nút của mình, hoặc thiết lập hóa đơn Lightning trực tiếp bằng sats.



![Image](assets/fr/100.webp)



Ví dụ, tôi đã gửi 1543 sats từ giao diện Alby Go.



![Image](assets/fr/101.webp)



Nếu tôi truy cập giao diện cơ bản của node Lightning trên Umbrel, tôi có thể thấy rằng khoản thanh toán này thực sự đã được node của tôi thực hiện.



![Image](assets/fr/102.webp)



Giờ bạn đã biết cách dễ dàng sử dụng nút Lightning của mình từ bất cứ đâu.



## Khả năng tự chủ lâu dài trên Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Chúng ta đã kết thúc khóa học thực hành LNP202 này. Giờ đây, bạn đã nắm được những kiến thức cơ bản cần thiết để sử dụng Lightning Network một cách độc lập: bạn hiểu vai trò thực sự của một node, những ưu nhược điểm của các phương pháp khác nhau, và bạn đã thiết lập một instance LND trên Umbrel với chiến lược sao lưu và bảo vệ nhất quán. Bạn cũng đã mở các kênh giao dịch đầu tiên, học cách quản lý thanh khoản để đảm bảo các khoản thanh toán của bạn được thực hiện đáng tin cậy hàng ngày.



Từ góc độ vận hành, nút mạng của bạn giờ đây cần được bảo trì định kỳ. Điều quan trọng nhất là giám sát nó (thời gian hoạt động, đồng bộ hóa, trạng thái kênh, lỗi thanh toán, v.v.), áp dụng các bản cập nhật do Umbrel cung cấp khi có phiên bản ổn định và kiểm tra định kỳ xem các bản sao lưu và cấu hình tháp giám sát của bạn vẫn đang hoạt động.



Khi nói đến các kênh, hãy có cách tiếp cận thực tế: giữ lại những kênh hữu ích, đóng những kênh không hoạt động vĩnh viễn hoặc liên kết với các đối tác không ổn định, và dần dần phân bổ lại vốn của bạn vào một cấu trúc mạng mạnh mẽ hơn.



**Một trong những sai lầm phổ biến nhất ở giai đoạn này là phân bổ quá nhiều vốn cho node Lightning của bạn. Hãy nhớ rằng node Lightning của bạn kém an toàn hơn nhiều so với wallet phần cứng, và tính khả dụng của số tiền được cam kết cho các kênh của bạn phụ thuộc vào các cơ chế sao lưu vẫn chưa hoàn hảo. Do đó, điều rất quan trọng là chỉ nên giữ ở mức hợp lý, số tiền mà bạn có thể chấp nhận mất trong trường hợp xảy ra sự cố, và luôn giữ phần lớn sats của bạn trên wallet phần cứng trên chuỗi.**



Về các công cụ, tôi khuyên bạn nên luôn tò mò và chú ý đến những phát triển mới. Trong buổi đào tạo này, chúng ta đã khám phá một số công cụ, từ việc quản lý node, kết nối cho đến sử dụng từ xa để thực hiện thanh toán. Tuy nhiên, Lightning là một lĩnh vực đặc biệt năng động. Mỗi năm, các công cụ mới và hữu ích lại xuất hiện, và nhiều ứng dụng mới cũng được áp dụng trên Umbrel. Việc cập nhật những phát triển mới này có thể giúp bạn khám phá ra những giải pháp mạnh mẽ hơn hoặc thiết thực hơn so với những giải pháp được trình bày trong khóa học này.



Về mặt đào tạo, nếu bạn chưa làm, tôi đặc biệt khuyên bạn nên tham gia khóa học lý thuyết LNP 201 của Fanis Michalakis, chuyên về vận hành Lightning Network. Khóa học này sẽ giúp bạn hiểu rõ hơn các thao tác được thực hiện trong khóa học LNP202 này, và mang lại cho bạn sự tự tin hơn trong việc quản lý hàng ngày nút mạng của mình.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Tuy nhiên, cũng không kém phần quan trọng đối với hành trình khám phá Bitcoin của bạn, tôi cũng khuyên bạn nên tham khảo khóa học xuất sắc của Ludovic Lars về lịch sử hình thành Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Nhưng trước khi tiếp tục, bạn có thể viết đánh giá về khóa học LNP202 này và, tất nhiên, tham gia kỳ thi lấy chứng chỉ để xác nhận rằng bạn đã hiểu hết nội dung của khóa học.



# Phần cuối


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Đánh giá & Xếp hạng


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Bài kiểm tra cuối kỳ


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Phần kết luận


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>