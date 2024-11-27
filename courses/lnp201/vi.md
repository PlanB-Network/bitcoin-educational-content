---
name: Giới thiệu lý thuyết về Lightning Network
goal: Khám phá Lightning Network từ góc độ kỹ thuật
objectives:
  - Hiểu về cách hoạt động của các kênh trong mạng.
  - Làm quen với các thuật ngữ HTLC, LNURL, và UTXO.
  - Tiếp thu cách quản lý tính thanh khoản và phí của LNN.
  - Nhận biết Lightning Network như một mạng lưới.
  - Hiểu về các ứng dụng lý thuyết của Lightning Network.
---

# Hành trình đến tầng thứ hai của Bitcoin

Hãy khám phá trái tim của Lightning Network, một hệ thống thiết yếu cho tương lai của các giao dịch Bitcoin. LNP201 là một khóa học lý thuyết về cách thức kỹ thuật của Lightning. Nó mở ra những nền tảng và cơ chế của mạng lớp thứ hai này, được thiết kế để làm cho các thanh toán Bitcoin nhanh chóng, tiết kiệm và có thể mở rộng.

Nhờ vào mạng lưới các kênh thanh toán của mình, Lightning cho phép thực hiện các giao dịch nhanh chóng và an toàn mà không cần ghi lại từng giao dịch trên blockchain Bitcoin. Qua các chương, bạn sẽ học cách mở, quản lý và đóng các kênh hoạt động như thế nào, cách thanh toán được chuyển tiếp qua các nút trung gian một cách an toàn trong khi giảm thiểu nhu cầu về sự tin cậy, và cách quản lý tính thanh khoản. Bạn sẽ khám phá những gì là giao dịch cam kết, HTLCs, khóa thu hồi, cơ chế trừng phạt, định tuyến hành tinh, và hóa đơn.

Cho dù bạn là người mới bắt đầu với Bitcoin hay người dùng có kinh nghiệm hơn, khóa học này sẽ cung cấp thông tin quý giá để hiểu và sử dụng Lightning Network. Mặc dù chúng tôi sẽ đề cập đến một số nguyên tắc cơ bản của hoạt động của Bitcoin trong các phần đầu, việc nắm vững cơ bản của phát minh của Satoshi trước khi lao vào LNP201 là rất quan trọng.

Chúc bạn khám phá thú vị!

+++

# Cơ bản

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Hiểu về Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Hiểu về Lightning Network](https://youtu.be/PszWk046x-I)

Chào mừng bạn đến với khóa học LNP201, mục tiêu là giải thích về cách thức kỹ thuật của Lightning Network.

Lightning Network là một mạng lưới các kênh thanh toán được xây dựng trên cơ sở giao thức Bitcoin, nhằm mục đích cho phép thực hiện các giao dịch nhanh chóng và với chi phí thấp. Nó cho phép tạo ra các kênh thanh toán giữa các bên tham gia, trong đó các giao dịch có thể được thực hiện gần như ngay lập tức và với phí rất thấp, mà không cần phải ghi lại từng giao dịch riêng lẻ trên blockchain. Như vậy, Lightning Network tìm cách cải thiện khả năng mở rộng của Bitcoin và làm cho nó có thể sử dụng cho các khoản thanh toán giá trị thấp.

Trước khi khám phá "mạng lưới", điều quan trọng là phải hiểu về khái niệm **kênh thanh toán** trên Lightning, cách nó hoạt động và các đặc điểm cụ thể của nó. Đây là chủ đề của chương đầu tiên này.

### Khái niệm về Kênh Thanh Toán

Một kênh thanh toán cho phép hai bên, ở đây là **Alice** và **Bob**, trao đổi tiền tệ qua Lightning Network. Mỗi người tham gia có một nút, được biểu diễn bằng một hình tròn, và kênh giữa họ được biểu diễn bằng một đoạn thẳng.

![LNP201](assets/en/01.webp)

Trong ví dụ của chúng tôi, Alice có 100,000 satoshis ở phía của mình trong kênh, và Bob có 30,000, với tổng cộng 130,000 satoshis, tạo thành **khả năng chứa của kênh**.

**Nhưng satoshi là gì?**

**Satoshi** (hay "sat") là một đơn vị tiền tệ trên Bitcoin. Tương tự như cent đối với euro, satoshi chỉ là một phần nhỏ của Bitcoin. Một satoshi bằng **0.00000001 Bitcoin**, hay một phần trăm triệu của một Bitcoin. Việc sử dụng satoshi trở nên ngày càng thực tiễn khi giá trị của Bitcoin tăng lên.

### Phân bổ Tiền trong Kênh

Hãy quay lại với kênh thanh toán. Khái niệm chính ở đây là "**phía của kênh**". Mỗi người tham gia có số tiền của họ trên phía kênh của mình: Alice 100,000 satoshis và Bob 30,000. Như chúng ta đã thấy, tổng số tiền này đại diện cho tổng công suất của kênh, một con số được thiết lập khi nó được mở.

![LNP201](assets/en/02.webp)

Hãy lấy một ví dụ về một giao dịch Lightning. Nếu Alice muốn gửi 40,000 satoshis cho Bob, điều này là khả thi bởi vì cô ấy có đủ tiền (100,000 satoshis). Sau giao dịch này, Alice sẽ có 60,000 satoshis ở phía của mình và Bob 70,000.

![LNP201](assets/en/03.webp)

**Công suất kênh**, ở mức 130,000 satoshis, vẫn giữ nguyên. Điều thay đổi là sự phân bổ tiền. Hệ thống này không cho phép gửi nhiều tiền hơn số tiền một người sở hữu. Ví dụ, nếu Bob muốn gửi lại 80,000 satoshis cho Alice, anh ta không thể, bởi vì anh ta chỉ có 70,000.

Một cách khác để hình dung sự phân bổ tiền là nghĩ về một **cái trượt** chỉ ra vị trí của tiền trong kênh. Ban đầu, với 100,000 satoshis cho Alice và 30,000 cho Bob, cái trượt một cách lô-gic ở phía Alice. Sau giao dịch 40,000 satoshis, cái trượt sẽ di chuyển nhẹ về phía Bob, người giờ đây có 70,000 satoshis.

![LNP201](assets/en/04.webp)

Biểu đồ này có thể hữu ích để tưởng tượng sự cân bằng tiền trong một kênh.

### Các Quy Tắc Cơ Bản của Một Kênh Thanh Toán

Điểm đầu tiên cần nhớ là **công suất kênh** là cố định. Nó hơi giống như đường kính của một ống: nó xác định số tiền tối đa có thể được gửi qua kênh một lần.
Hãy lấy một ví dụ: nếu Alice có 130,000 satoshis ở phía của mình, cô ấy chỉ có thể gửi tối đa 130,000 satoshis cho Bob trong một giao dịch duy nhất. Tuy nhiên, sau đó Bob có thể gửi lại số tiền này cho Alice, một phần hoặc toàn bộ.

Điều quan trọng cần hiểu là công suất cố định của kênh giới hạn số tiền tối đa của một giao dịch duy nhất, nhưng không giới hạn tổng số giao dịch có thể thực hiện, cũng như tổng khối lượng tiền được trao đổi trong kênh.

**Bạn nên rút ra điều gì từ chương này?**

- Công suất của một kênh là cố định và xác định số tiền tối đa có thể được gửi trong một giao dịch duy nhất.
- Tiền trong một kênh được phân bổ giữa hai bên tham gia, và mỗi bên chỉ có thể gửi cho bên kia số tiền họ sở hữu ở phía của mình.
- Mạng Lưới Lightning do đó cho phép trao đổi tiền một cách nhanh chóng và hiệu quả, trong khi tôn trọng các hạn chế do công suất của các kênh đặt ra.

Đây là kết thúc của chương đầu tiên, nơi chúng ta đã đặt nền móng cho Mạng Lưới Lightning. Trong các chương tiếp theo, chúng ta sẽ xem xét cách mở một kênh và đi sâu hơn vào các khái niệm đã được thảo luận ở đây.

## Bitcoin, Địa Chỉ, UTXO, và Giao Dịch

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, addresses, utxo, and transactions](https://youtu.be/cadCJ2V7zTg)
Chương này khá đặc biệt vì nó không trực tiếp nói về Lightning, mà về Bitcoin. Thực tế, Mạng Lưới Lightning là một lớp nằm trên Bitcoin. Do đó, việc hiểu một số khái niệm cơ bản của Bitcoin là cần thiết để nắm bắt được cách thức hoạt động của Lightning trong các chương tiếp theo. Trong chương này, chúng ta sẽ xem xét cơ bản về địa chỉ nhận Bitcoin, UTXOs, cũng như cách thức hoạt động của giao dịch Bitcoin.

### Địa Chỉ Bitcoin, Khóa Riêng và Khóa Công Khai

Một địa chỉ Bitcoin là một chuỗi ký tự được tạo ra từ một **khóa công khai**, được tính toán từ một **khóa riêng**. Như bạn chắc chắn biết, nó được sử dụng để khóa bitcoin, tương đương với việc nhận chúng vào ví của chúng ta.

Khóa riêng là một yếu tố bí mật mà **không bao giờ nên chia sẻ**, trong khi khóa công khai và địa chỉ có thể được chia sẻ mà không có rủi ro về an ninh (việc tiết lộ chúng chỉ đại diện cho rủi ro đối với quyền riêng tư của bạn). Dưới đây là một biểu diễn phổ biến mà chúng ta sẽ áp dụng trong suốt quá trình đào tạo này:

- Các **khóa riêng** sẽ được biểu diễn **theo chiều dọc**.
- Các **khóa công khai** sẽ được biểu diễn **theo chiều ngang**.
- Màu sắc của chúng chỉ ra người sở hữu chúng (Alice màu cam và Bob màu đen...).

### Giao Dịch Bitcoin: Gửi Tiền và Scripts

Trên Bitcoin, một giao dịch bao gồm việc gửi tiền từ một địa chỉ này sang địa chỉ khác. Hãy lấy ví dụ về Alice gửi 0.002 Bitcoin cho Bob. Alice sử dụng khóa riêng liên kết với địa chỉ của mình để **ký** giao dịch, qua đó chứng minh rằng cô ấy thực sự có khả năng chi tiêu số tiền này. Nhưng điều gì thực sự xảy ra đằng sau giao dịch này? Số tiền trên một địa chỉ Bitcoin được khóa bởi một **script**, một loại mini-program đặt ra một số điều kiện nhất định để chi tiêu số tiền.

Script phổ biến nhất yêu cầu một chữ ký với khóa riêng liên kết với địa chỉ. Khi Alice ký một giao dịch với khóa riêng của mình, cô ấy **mở khóa script** chặn số tiền, và chúng có thể sau đó được chuyển giao. Việc chuyển giao tiền bao gồm việc thêm một script mới vào số tiền này, quy định rằng để chi tiêu chúng lần này, chữ ký của khóa riêng của **Bob** sẽ được yêu cầu.

![LNP201](assets/en/05.webp)

### UTXOs: Unspent Transaction Outputs

Trên Bitcoin, thứ chúng ta thực sự trao đổi không phải là bitcoin trực tiếp, mà là **UTXOs** (_Unspent Transaction Outputs_), nghĩa là "đầu ra giao dịch chưa được chi tiêu".

Một UTXO là một phần của bitcoin có thể có bất kỳ giá trị nào, ví dụ, **2,000 bitcoins**, **8 bitcoins**, hoặc thậm chí **8,000 sats**. Mỗi UTXO được khóa bởi một script, và để chi tiêu nó, người ta phải thỏa mãn các điều kiện của script, thường là một chữ ký với khóa riêng tương ứng với một địa chỉ nhận cụ thể.

UTXOs không thể được chia nhỏ. Mỗi lần chúng được sử dụng để chi tiêu số lượng bitcoin mà chúng đại diện, việc này phải được thực hiện hoàn toàn. Điều này giống như một tờ tiền: nếu bạn có một tờ €10 và bạn nợ người bán bánh €5, bạn không thể chỉ cắt tờ tiền làm đôi. Bạn phải đưa cho anh ta tờ €10, và anh ta sẽ trả lại cho bạn €5 tiền thối. Đây chính xác là nguyên tắc tương tự đối với UTXOs trên Bitcoin! Ví dụ, khi Alice mở khóa một script với khóa riêng của mình, cô ấy mở khóa toàn bộ UTXO. Nếu cô ấy chỉ muốn gửi một phần của số tiền được đại diện bởi UTXO này cho Bob, cô ấy có thể "phân mảnh" nó thành nhiều phần nhỏ hơn. Sau đó, cô ấy sẽ gửi 0.0015 BTC cho Bob và gửi phần còn lại, 0.0005 BTC, đến một **địa chỉ thay đổi**.

Dưới đây là một ví dụ về một giao dịch với 2 đầu ra:

- Một UTXO trị giá 0.0015 BTC dành cho Bob, được khóa bởi một script yêu cầu chữ ký khóa riêng của Bob.
- Một UTXO trị giá 0.0005 BTC dành cho Alice, được khóa bởi một script yêu cầu chữ ký của chính cô ấy.

![LNP201](assets/en/06.webp)

### Địa Chỉ Đa Chữ Ký

Ngoài việc tạo ra địa chỉ đơn giản từ một khóa công khai duy nhất, cũng có thể tạo ra **địa chỉ đa chữ ký** từ nhiều khóa công khai. Một trường hợp đặc biệt thú vị cho Mạng Lưới Lightning là **địa chỉ đa chữ ký 2/2**, được tạo ra từ hai khóa công khai:

![LNP201](assets/en/07.webp)

Để chi tiêu số tiền được khóa với địa chỉ đa chữ ký 2/2 này, cần phải ký bằng cả hai khóa riêng liên kết với các khóa công khai.

![LNP201](assets/en/08.webp)

Loại địa chỉ này chính xác là biểu diễn trên blockchain Bitcoin của các kênh thanh toán trên Mạng Lưới Lightning.

**Bạn nên nhớ gì từ chương này?**

- Một **địa chỉ Bitcoin** được tạo ra từ một khóa công khai, mà chính nó được tạo ra từ một khóa riêng.
- Số tiền trên Bitcoin được khóa bởi **scripts**, và để chi tiêu số tiền này, người ta phải thỏa mãn script, thường liên quan đến việc cung cấp một chữ ký với khóa riêng tương ứng.
- **UTXOs** là các phần của bitcoin được khóa bởi scripts, và mỗi giao dịch trên Bitcoin bao gồm việc mở khóa một UTXO và sau đó tạo ra một hoặc nhiều UTXO mới để trả lại.
- **Địa chỉ đa chữ ký 2/2** yêu cầu chữ ký của hai khóa riêng để chi tiêu số tiền. Các địa chỉ cụ thể này được sử dụng trong bối cảnh của Lightning để tạo ra các kênh thanh toán.

Chương này về Bitcoin đã cho chúng ta xem xét lại một số khái niệm cơ bản cho những gì tiếp theo. Trong chương tiếp theo, chúng ta sẽ cụ thể khám phá cách mở kênh trên Mạng Lưới Lightning hoạt động như thế nào.

# Mở và Đóng Kênh

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Mở Kênh

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![mở một kênh](https://youtu.be/B2caBC0Rxko)

Trong chương này, chúng ta sẽ xem xét cụ thể hơn cách mở một kênh thanh toán trên Mạng Lưới Lightning và hiểu mối liên kết giữa hoạt động này và hệ thống Bitcoin cơ bản.

### Kênh Thanh Toán Lightning

Như chúng ta đã thấy trong chương đầu tiên, một **kênh thanh toán** trên Lightning có thể được so sánh với một "ống" để trao đổi tiền tệ giữa hai bên tham gia (**Alice** và **Bob** trong ví dụ của chúng ta). Sức chứa của kênh này tương ứng với tổng số tiền có sẵn ở mỗi bên. Trong ví dụ của chúng ta, Alice có **100,000 satoshis** và Bob có **30,000 satoshis**, tạo thành **tổng sức chứa** là **130,000 satoshis**.

![LNP201](assets/en/09.webp)

### Các Cấp Độ Trao Đổi Thông Tin

Rất quan trọng khi phân biệt rõ ràng các cấp độ trao đổi trên Mạng Lưới Lightning:

- **Giao tiếp ngang hàng (giao thức Lightning)**: Đây là các tin nhắn mà các nút Lightning gửi cho nhau để giao tiếp. Chúng tôi sẽ biểu diễn những tin nhắn này bằng các đường nét đứt màu đen trong các sơ đồ của chúng tôi.
- **Kênh thanh toán (giao thức Lightning)**: Đây là các con đường để trao đổi tiền tệ trên Lightning, mà chúng tôi sẽ biểu diễn bằng các đường liền màu đen.
- **Giao dịch Bitcoin (giao thức Bitcoin)**: Đây là các giao dịch được thực hiện trên chuỗi, mà chúng tôi sẽ biểu diễn bằng các đường màu cam.

![LNP201](assets/en/10.webp)
Đáng chú ý là một nút Lightning có thể giao tiếp qua giao thức P2P mà không cần mở kênh, nhưng để trao đổi tiền, việc mở một kênh là cần thiết.

### Các Bước Để Mở Một Kênh Lightning

1. **Trao đổi tin nhắn**: Alice muốn mở một kênh với Bob. Cô ấy gửi cho anh ấy một tin nhắn chứa số tiền cô ấy muốn gửi vào kênh (130,000 sats) và khóa công khai của mình. Bob phản hồi bằng cách chia sẻ khóa công khai của mình.

![LNP201](assets/en/11.webp)

2. **Tạo địa chỉ đa chữ ký**: Với hai khóa công khai này, Alice tạo một **địa chỉ đa chữ ký 2/2**, nghĩa là số tiền sau này được gửi vào địa chỉ này sẽ yêu cầu cả hai chữ ký (Alice và Bob) để chi tiêu.

![LNP201](assets/en/12.webp)

3. **Giao dịch gửi tiền**: Alice chuẩn bị một giao dịch Bitcoin để gửi tiền vào địa chỉ đa chữ ký này. Ví dụ, cô ấy có thể quyết định gửi **130,000 satoshis** vào địa chỉ đa chữ ký này. Giao dịch này được **xây dựng nhưng chưa được công bố** trên blockchain.

![LNP201](assets/en/13.webp)

4. **Giao dịch rút tiền**: Trước khi công bố giao dịch gửi tiền, Alice xây dựng một giao dịch rút tiền để cô có thể lấy lại tiền của mình trong trường hợp có vấn đề với Bob. Thực sự, một khi Alice công bố giao dịch gửi tiền, số sats của cô ấy sẽ bị khóa trên một địa chỉ đa chữ ký 2/2, yêu cầu cả hai chữ ký của cô ấy và Bob để mở khóa. Alice bảo vệ khỏi rủi ro mất mát này bằng cách xây dựng giao dịch rút tiền cho phép cô lấy lại tiền của mình.

![LNP201](assets/en/14.webp)

5. **Chữ ký của Bob**: Alice gửi giao dịch gửi tiền cho Bob như một bằng chứng và yêu cầu anh ấy ký vào giao dịch rút tiền. Một khi chữ ký của Bob được thu thập trên giao dịch rút tiền, Alice được đảm bảo có thể lấy lại tiền của mình bất cứ lúc nào, vì chỉ cần chữ ký của mình là có thể mở khóa đa chữ ký.

![LNP201](assets/en/15.webp)

6. **Công bố giao dịch gửi tiền**: Một khi chữ ký của Bob được thu thập, Alice có thể công bố giao dịch gửi tiền trên blockchain Bitcoin, qua đó chính thức mở kênh Lightning giữa hai người dùng.

![LNP201](assets/en/16.webp)

### Kênh được mở khi nào?

Kênh được coi là đã mở một khi giao dịch gửi tiền được bao gồm trong một khối Bitcoin và nó đạt được một độ sâu nhất định của các xác nhận (số lượng khối tiếp theo).

**Bạn nên nhớ gì từ chương này?**

- Việc mở kênh bắt đầu với việc trao đổi **tin nhắn** giữa hai bên (trao đổi số tiền và khóa công khai).
- Một kênh được hình thành bằng cách tạo một **địa chỉ đa chữ ký 2/2** và gửi tiền vào đó qua một giao dịch Bitcoin.
- Người mở kênh đảm bảo họ có thể **lấy lại tiền của mình** thông qua một giao dịch rút tiền được ký bởi bên kia trước khi công bố giao dịch gửi tiền.

Trong chương tiếp theo, chúng ta sẽ khám phá cách thức kỹ thuật của một giao dịch Lightning trong một kênh.

## Giao Dịch Cam Kết

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![Giao dịch Lightning & giao dịch cam kết](https://youtu.be/aPqI34tpypM)

Trong chương này, chúng ta sẽ khám phá cách thức kỹ thuật của một giao dịch trong một kênh trên Mạng Lưới Lightning, tức là khi tiền được chuyển từ một phía của kênh sang phía kia.

### Nhắc nhở về vòng đời của kênh

Như đã thấy trước đây, một kênh Lightning bắt đầu với việc **mở** thông qua một giao dịch Bitcoin. Kênh có thể được **đóng** bất cứ lúc nào, cũng thông qua một giao dịch Bitcoin. Giữa hai thời điểm này, có thể thực hiện một số lượng gần như vô hạn các giao dịch trong kênh, mà không cần qua blockchain Bitcoin. Hãy xem xét điều gì xảy ra trong một giao dịch trong kênh.

![LNP201](assets/en/17.webp)

### Trạng thái ban đầu của kênh

Tại thời điểm mở kênh, Alice đã gửi **130,000 satoshis** vào địa chỉ đa chữ ký của kênh. Do đó, trong trạng thái ban đầu, tất cả các quỹ đều ở phía Alice. Trước khi mở kênh, Alice cũng đã yêu cầu Bob ký một **giao dịch rút tiền**, điều này sẽ cho phép cô ấy lấy lại quỹ của mình nếu cô ấy muốn đóng kênh.

![LNP201](assets/en/18.webp)

### Giao dịch Chưa Công Bố: Các Giao dịch Cam Kết

Khi Alice thực hiện một giao dịch trong kênh để gửi quỹ cho Bob, một giao dịch Bitcoin mới được tạo ra để phản ánh sự thay đổi này trong phân phối quỹ. Giao dịch này, được gọi là **giao dịch cam kết**, không được công bố trên blockchain nhưng đại diện cho trạng thái mới của kênh sau giao dịch Lightning.

Hãy lấy một ví dụ với Alice gửi 30,000 satoshis cho Bob:

- **Ban đầu**: Alice có 130,000 satoshis.
- **Sau giao dịch**: Alice có 100,000 satoshis, và Bob 30,000 satoshis.
  Để xác nhận việc chuyển giao này, Alice và Bob tạo ra một **giao dịch Bitcoin mới chưa công bố** sẽ gửi **100,000 satoshis cho Alice** và **30,000 satoshis cho Bob** từ địa chỉ đa chữ ký. Cả hai bên đều xây dựng giao dịch này một cách độc lập, nhưng với cùng một dữ liệu (số lượng và địa chỉ). Một khi đã xây dựng, mỗi bên ký vào giao dịch và trao đổi chữ ký của họ với người kia. Điều này cho phép bất kỳ bên nào công bố giao dịch bất cứ lúc nào nếu cần thiết để lấy lại phần của họ trong kênh trên blockchain Bitcoin chính.
  ![LNP201](assets/en/19.webp)

### Quy Trình Chuyển Giao: Hóa Đơn

Khi Bob muốn nhận quỹ, anh ấy gửi Alice một **_hóa đơn_** cho 30,000 satoshis. Alice sau đó tiến hành thanh toán hóa đơn này bằng cách bắt đầu chuyển giao trong kênh. Như chúng ta đã thấy, quy trình này dựa vào việc tạo và ký một **giao dịch cam kết** mới.

Mỗi giao dịch cam kết đại diện cho phân phối quỹ mới trong kênh sau khi chuyển giao. Trong ví dụ này, sau giao dịch, Bob có 30,000 satoshis và Alice có 100,000 satoshis. Nếu một trong hai bên quyết định công bố giao dịch cam kết này trên blockchain, điều đó sẽ dẫn đến việc đóng kênh và quỹ sẽ được phân phối theo phân phối cuối cùng này.

![LNP201](assets/en/20.webp)

### Trạng Thái Mới Sau Một Giao Dịch Thứ Hai

Hãy lấy một ví dụ khác: sau giao dịch đầu tiên khi Alice gửi 30,000 satoshis cho Bob, Bob quyết định gửi **10,000 satoshis trở lại cho Alice**. Điều này tạo ra một trạng thái mới của kênh. **Giao dịch cam kết** mới sẽ đại diện cho phân phối cập nhật này:

- **Alice** giờ đây có **110,000 satoshis**.
- **Bob** có **20,000 satoshis**.

![LNP201](assets/en/21.webp)

Một lần nữa, giao dịch này không được công bố trên blockchain nhưng có thể được công bố bất cứ lúc nào trong trường hợp kênh được đóng.

Tóm lại, khi quỹ được chuyển giao trong một kênh Lightning:

- Alice và Bob tạo ra một **giao dịch cam kết** mới, phản ánh sự phân bổ mới của quỹ.
- Giao dịch Bitcoin này được **ký** bởi cả hai bên nhưng **không được công bố** trên blockchain Bitcoin miễn là kênh vẫn mở.
- Các giao dịch cam kết đảm bảo rằng mỗi bên tham gia có thể thu hồi quỹ của mình bất cứ lúc nào trên blockchain Bitcoin bằng cách công bố giao dịch đã ký cuối cùng.

Tuy nhiên, hệ thống này có một khuyết điểm tiềm ẩn, chúng ta sẽ giải quyết trong chương tiếp theo. Chúng ta sẽ xem xét cách mỗi bên có thể bảo vệ mình khỏi nỗ lực gian lận của bên kia.

## Khóa Huỷ Bỏ

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
![transactions part 2](https://youtu.be/RRvoVTLRJ84)
Trong chương này, chúng ta sẽ đi sâu hơn vào cách giao dịch hoạt động trên Mạng Lưới Sét bằng cách thảo luận về các cơ chế được đặt ra để bảo vệ chống lại gian lận, đảm bảo rằng mỗi bên tuân thủ các quy tắc trong kênh.

### Nhắc lại: Giao Dịch Cam Kết

Như đã thấy trước đây, giao dịch trên Mạng Lưới Sét dựa vào **giao dịch cam kết** chưa được công bố. Những giao dịch này phản ánh sự phân bổ hiện tại của quỹ trong kênh. Khi một giao dịch Mạng Lưới Sét mới được thực hiện, một giao dịch cam kết mới được tạo ra và ký bởi cả hai bên để phản ánh trạng thái mới của kênh.

Hãy lấy một ví dụ đơn giản:

- **Trạng thái ban đầu**: Alice có **100,000 satoshis**, Bob có **30,000 satoshis**.
- Sau một giao dịch nơi Alice gửi **40,000 satoshis** cho Bob, giao dịch cam kết mới phân bổ quỹ như sau:
  - Alice: **60,000 satoshis**
  - Bob: **70,000 satoshis**

![LNP201](assets/en/22.webp)

Bất cứ lúc nào, cả hai bên đều có thể công bố **giao dịch cam kết mới nhất** đã ký để đóng kênh và thu hồi quỹ của mình.

### Lỗi: Gian Lận bằng cách Công bố một Giao Dịch Cũ

Một vấn đề tiềm ẩn phát sinh nếu một trong hai bên quyết định **gian lận** bằng cách công bố một giao dịch cam kết cũ. Ví dụ, Alice có thể công bố một giao dịch cam kết cũ nơi cô ấy có **100,000 satoshis**, mặc dù thực tế bây giờ cô chỉ còn **60,000**. Điều này sẽ cho phép cô ấy ăn cắp **40,000 satoshis** từ Bob.

![LNP201](assets/en/23.webp)

Còn tồi tệ hơn, Alice có thể công bố giao dịch rút tiền đầu tiên, giao dịch trước khi kênh được mở, nơi cô ấy có **130,000 satoshis**, và do đó ăn cắp toàn bộ quỹ của kênh.

![LNP201](assets/en/24.webp)

### Giải Pháp: Khóa Huỷ Bỏ và Thời Gian Khóa

Để ngăn chặn loại gian lận này của Alice, trên Mạng Lưới Sét, **cơ chế bảo mật** được thêm vào các giao dịch cam kết:

1. **Thời gian khóa**: Mỗi giao dịch cam kết bao gồm một thời gian khóa cho quỹ của Alice. Thời gian khóa là một nguyên tắc hợp đồng thông minh đặt ra một điều kiện thời gian phải được đáp ứng để một giao dịch được thêm vào một khối. Điều này có nghĩa là Alice không thể thu hồi quỹ của mình cho đến khi một số khối nhất định đã trôi qua nếu cô ấy công bố một trong các giao dịch cam kết. Thời gian khóa này bắt đầu áp dụng từ sự xác nhận của giao dịch cam kết. Thời gian của nó thường tỷ lệ với kích thước của kênh, nhưng cũng có thể được cấu hình một cách thủ công.
2. **Khóa Huỷ Bỏ**: Quỹ của Alice cũng có thể được chi tiêu ngay lập tức bởi Bob nếu anh ta sở hữu **khóa huỷ bỏ**. Khóa này bao gồm một bí mật do Alice giữ và một bí mật do Bob giữ. Lưu ý rằng bí mật này khác nhau cho mỗi giao dịch cam kết.
   Nhờ vào sự kết hợp của 2 cơ chế này, Bob có thời gian để phát hiện nỗ lực gian lận của Alice và trừng phạt cô ấy bằng cách thu hồi đầu ra của mình với khóa thu hồi, điều này đối với Bob có nghĩa là thu hồi lại tất cả các quỹ của kênh. Giao dịch cam kết mới của chúng ta giờ đây sẽ trông như thế này:
   ![LNP201](assets/en/25.webp)

Hãy cùng nhau chi tiết về cách thức hoạt động của cơ chế này.

### Quy Trình Cập Nhật Giao Dịch

Khi Alice và Bob cập nhật trạng thái của kênh với một giao dịch Lightning mới, họ trao đổi trước **bí mật** tương ứng của họ cho giao dịch cam kết trước đó (cái sẽ trở nên lỗi thời và có thể cho phép một trong họ gian lận). Điều này có nghĩa là, trong trạng thái mới của kênh:

- Alice và Bob có một giao dịch cam kết mới đại diện cho sự phân phối hiện tại của quỹ sau giao dịch Lightning.
- Mỗi người có bí mật của người kia cho giao dịch trước đó, điều này cho phép họ sử dụng khóa thu hồi chỉ khi một trong họ cố gắng gian lận bằng cách công bố một giao dịch với trạng thái cũ trong mempools của các nút Bitcoin. Thực sự, để trừng phạt bên kia, cần phải giữ cả hai bí mật và giao dịch cam kết của bên kia, bao gồm cả đầu vào đã ký. Không có giao dịch này, khóa thu hồi một mình là vô dụng. Cách duy nhất để lấy được giao dịch này là thu hồi nó từ mempools (trong các giao dịch đang chờ xác nhận) hoặc trong các giao dịch đã được xác nhận trên blockchain trong thời gian khóa thời gian, điều này chứng minh rằng bên kia đang cố gắng gian lận, dù có chủ ý hay không.

Hãy lấy một ví dụ để hiểu rõ quy trình này:

1. **Trạng Thái Ban Đầu**: Alice có **100,000 satoshis**, Bob **30,000 satoshis**.

![LNP201](assets/en/26.webp)

2. Bob muốn nhận 40,000 satoshis từ Alice qua kênh Lightning của họ. Để làm điều này:
   - Anh ấy gửi cho cô ấy một hóa đơn cùng với bí mật của mình cho khóa thu hồi của giao dịch cam kết trước đó.
   - Đáp lại, Alice cung cấp chữ ký của mình cho giao dịch cam kết mới của Bob, cũng như bí mật của cô ấy cho khóa thu hồi của giao dịch trước đó.
   - Cuối cùng, Bob gửi chữ ký của mình cho giao dịch cam kết mới của Alice.
   - Những trao đổi này cho phép Alice gửi **40,000 satoshis** cho Bob trên Lightning qua kênh của họ, và các giao dịch cam kết mới giờ đây phản ánh sự phân phối quỹ mới này.

![LNP201](assets/en/27.webp)

3. Nếu Alice cố gắng công bố giao dịch cam kết cũ nơi cô ấy vẫn sở hữu **100,000 satoshis**, Bob, sau khi đã lấy được khóa thu hồi, có thể ngay lập tức thu hồi quỹ sử dụng khóa này, trong khi Alice bị chặn bởi khóa thời gian.

![LNP201](assets/en/28.webp)

Ngay cả trong trường hợp này, Bob không có lợi ích kinh tế nào trong việc cố gắng gian lận, nếu anh ta vẫn làm vậy, Alice cũng được hưởng sự bảo vệ đối xứng, mang lại cho cô ấy những bảo đảm tương tự.

**Bạn nên rút ra điều gì từ chương này?**

Các **giao dịch cam kết** trên Mạng Lưới Lightning bao gồm các cơ chế bảo mật giảm cả rủi ro gian lận và động cơ thực hiện gian lận. Trước khi ký một giao dịch cam kết mới, Alice và Bob trao đổi **bí mật** tương ứng của họ cho các giao dịch cam kết trước đó. Nếu Alice cố gắng công bố một giao dịch cam kết cũ, Bob có thể sử dụng **khóa thu hồi** để thu hồi tất cả quỹ trước khi Alice có thể làm vậy (vì cô ấy bị chặn bởi khóa thời gian), điều này trừng phạt cô ấy vì đã cố gắng gian lận.

Hệ thống bảo mật này đảm bảo rằng các bên tham gia tuân thủ các quy tắc của Mạng Lưới Lightning, và họ không thể lợi dụng từ việc công bố các giao dịch cam kết cũ.
Tại thời điểm này trong quá trình đào tạo, bạn đã biết cách các kênh Lightning được mở và các giao dịch trong những kênh này hoạt động như thế nào. Trong chương tiếp theo, chúng ta sẽ khám phá các cách khác nhau để đóng một kênh và thu hồi bitcoin của bạn trên blockchain chính.

## Đóng Kênh

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![đóng một kênh](https://youtu.be/FVmQvNpVW8Y)

Trong chương này, chúng ta sẽ thảo luận về **việc đóng một kênh** trên Mạng Lưới Lightning, được thực hiện thông qua một giao dịch Bitcoin, giống như khi mở một kênh. Sau khi thấy cách các giao dịch trong một kênh hoạt động, bây giờ là lúc để xem cách đóng một kênh và thu hồi quỹ trên blockchain Bitcoin.

### Nhắc nhở về vòng đời của kênh

**Vòng đời của một kênh** bắt đầu với việc **mở kênh**, thông qua một giao dịch Bitcoin, sau đó các giao dịch Lightning được thực hiện bên trong nó, và cuối cùng, khi các bên muốn thu hồi quỹ của mình, kênh được **đóng** thông qua một giao dịch Bitcoin thứ hai. Các giao dịch trung gian được thực hiện trên Lightning được biểu diễn bởi các **giao dịch cam kết** không được công bố.

![LNP201](assets/en/29.webp)

### Ba loại đóng kênh

Có ba cách chính để đóng kênh này, có thể được gọi là **người tốt, kẻ xấu, và kẻ trốn tránh** (lấy cảm hứng từ Andreas Antonopoulos trong _Mastering the Lightning Network_):

1. **Người Tốt**: **đóng kênh hợp tác**, nơi Alice và Bob đồng ý đóng kênh.
2. **Kẻ Xấu**: **đóng kênh ép buộc**, nơi một trong các bên quyết định đóng kênh một cách trung thực, nhưng không có sự đồng ý của bên kia.
3. **Kẻ Xấu Xí**: **đóng kênh với gian lận**, nơi một trong các bên cố gắng ăn cắp quỹ bằng cách công bố một giao dịch cam kết cũ (bất kỳ cái nào trừ cái cuối cùng, phản ánh sự phân phối công bằng và chính xác của quỹ).

Hãy lấy một ví dụ:

- Alice sở hữu **100,000 satoshis** và Bob **30,000 satoshis**.
- Sự phân phối này được phản ánh trong **2 giao dịch cam kết** (một cho mỗi người dùng) không được công bố, nhưng có thể được công bố trong trường hợp đóng kênh.

![LNP201](assets/en/30.webp)

### Người Tốt: đóng kênh hợp tác

Trong một **đóng kênh hợp tác**, Alice và Bob đồng ý đóng kênh. Dưới đây là cách thức hoạt động:

1. Alice gửi một tin nhắn cho Bob qua giao thức giao tiếp Lightning để đề xuất đóng kênh.
2. Bob đồng ý, và hai bên không thực hiện thêm giao dịch nào trong kênh.

![LNP201](assets/en/31.webp)

3. Alice và Bob cùng nhau thương lượng về phí của **giao dịch đóng kênh**. Phí này thường được tính dựa trên thị trường phí Bitcoin tại thời điểm đóng kênh. Quan trọng là phải lưu ý rằng **luôn luôn là người mở kênh** (Alice trong ví dụ của chúng ta) phải trả phí đóng kênh.
4. Họ xây dựng một **giao dịch đóng kênh mới**. Giao dịch này giống như một giao dịch cam kết, nhưng không có thời gian chờ hoặc cơ chế thu hồi, vì cả hai bên đang hợp tác và không có rủi ro gian lận. Giao dịch đóng kênh hợp tác này do đó khác với các giao dịch cam kết.
   Ví dụ, nếu Alice sở hữu **100,000 satoshis** và Bob **30,000 satoshis**, giao dịch kết thúc sẽ chuyển **100,000 satoshis** vào địa chỉ của Alice và **30,000 satoshis** vào địa chỉ của Bob, không có ràng buộc thời gian. Khi giao dịch này được cả hai bên ký, Alice sẽ công bố nó. Khi giao dịch được xác nhận trên blockchain Bitcoin, kênh Lightning sẽ chính thức được đóng.

![LNP201](assets/en/32.webp)

**Đóng cửa hợp tác** là phương pháp ưu tiên để đóng cửa vì nó nhanh chóng (không có thời gian chờ) và phí giao dịch được điều chỉnh theo điều kiện thị trường Bitcoin hiện tại. Điều này tránh trả quá ít, có thể gây nguy cơ chặn giao dịch trong mempools, hoặc trả quá nhiều không cần thiết, dẫn đến tổn thất tài chính không cần thiết cho các bên tham gia.

### Điều Xấu: đóng cửa bắt buộc

Khi nút của Alice gửi tin nhắn cho nút của Bob yêu cầu đóng cửa hợp tác, nếu anh ta không phản hồi (ví dụ, do mất kết nối internet hoặc vấn đề kỹ thuật), Alice có thể tiến hành với **đóng cửa bắt buộc** bằng cách công bố **giao dịch cam kết cuối cùng đã ký**.
Trong trường hợp này, Alice chỉ đơn giản công bố giao dịch cam kết cuối cùng, phản ánh trạng thái của kênh vào thời điểm giao dịch Lightning cuối cùng diễn ra với sự phân phối tiền tệ chính xác.

![LNP201](assets/en/33.webp)

Giao dịch này bao gồm một **thời gian chờ** cho tiền của Alice, làm cho việc đóng cửa trở nên chậm hơn.

![LNP201](assets/en/34.webp)

Ngoài ra, phí của giao dịch cam kết có thể không phù hợp vào thời điểm đóng cửa, vì chúng được thiết lập khi giao dịch được tạo, đôi khi là vài tháng trước. Nói chung, các khách hàng Lightning ước lượng phí cao để tránh vấn đề trong tương lai, nhưng điều này có thể dẫn đến phí quá cao, hoặc ngược lại quá thấp.

Tóm lại, **đóng cửa bắt buộc** là lựa chọn cuối cùng khi đối tác không còn phản hồi. Nó chậm hơn và kém kinh tế hơn so với đóng cửa hợp tác. Do đó, nó nên được tránh càng nhiều càng tốt.

### Gian lận: lừa đảo

Cuối cùng, một việc đóng cửa với **gian lận** xảy ra khi một trong các bên cố gắng công bố một giao dịch cam kết cũ, thường là nơi họ giữ nhiều tiền hơn họ nên có. Ví dụ, Alice có thể công bố một giao dịch cũ nơi cô ấy sở hữu **120,000 satoshis**, trong khi thực tế cô ấy chỉ sở hữu **100,000** bây giờ.

![LNP201](assets/en/35.webp)

Bob, để ngăn chặn sự gian lận này, giám sát blockchain Bitcoin và mempool của mình để đảm bảo Alice không công bố một giao dịch cũ. Nếu Bob phát hiện ra một nỗ lực gian lận, anh ta có thể sử dụng **khóa thu hồi** để thu hồi tiền của Alice và trừng phạt cô ấy bằng cách lấy toàn bộ tiền trong kênh. Vì Alice bị chặn bởi thời gian chờ trên đầu ra của mình, Bob có thời gian để tiêu nó mà không cần thời gian chờ ở phía mình để thu hồi toàn bộ số tiền vào một địa chỉ mà anh ta sở hữu.

![LNP201](assets/en/36.webp)

Rõ ràng, gian lận có thể thành công nếu Bob không hành động trong thời gian do thời gian chờ trên đầu ra của Alice quy định. Trong trường hợp này, đầu ra của Alice được mở khóa, cho phép cô ấy sử dụng nó để tạo một đầu ra mới đến một địa chỉ cô ấy kiểm soát.

**Bạn nên rút ra điều gì từ chương này?**

Có ba cách để đóng một kênh:

1. **Đóng cửa hợp tác**: Nhanh chóng và ít tốn kém, nơi cả hai bên đồng ý đóng kênh và công bố một giao dịch kết thúc được điều chỉnh.
2. **Đóng cửa bắt buộc**: Ít mong muốn hơn, vì nó dựa vào việc công bố một giao dịch cam kết, với phí có thể không phù hợp và một thời gian chờ, làm chậm quá trình đóng cửa.
3. **Gian lận**: Nếu một trong hai bên cố gắng ăn cắp tiền bằng cách công bố một giao dịch cũ, bên kia có thể sử dụng khóa hủy bỏ để trừng phạt hành vi gian lận này.
   Trong các chương tiếp theo, chúng ta sẽ khám phá Mạng Lưới Lightning từ một góc độ rộng lớn hơn, tập trung vào cách thức hoạt động của mạng lưới này.

# Một Mạng Lưới Thanh Khoản

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Mạng Lưới Lightning

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![mạng lưới lightning](https://youtu.be/RAZAa3v41DM)

Trong chương này, chúng ta sẽ khám phá cách thức các khoản thanh toán trên Mạng Lưới Lightning có thể đến được với người nhận ngay cả khi họ không được kết nối trực tiếp qua một kênh thanh toán. Lightning thực sự là một **mạng lưới các kênh thanh toán**, cho phép gửi tiền đến một nút xa thông qua các kênh của các bên tham gia khác. Chúng ta sẽ khám phá cách thức các khoản thanh toán được định tuyến qua mạng lưới, cách thanh khoản di chuyển giữa các kênh, và cách tính phí giao dịch.

### Mạng Lưới Các Kênh Thanh Toán

Trên Mạng Lưới Lightning, một giao dịch tương ứng với việc chuyển tiền giữa hai nút. Như đã thấy trong các chương trước, để thực hiện giao dịch Lightning, cần phải mở một kênh với ai đó. Kênh này cho phép thực hiện gần như vô hạn số lượng giao dịch ngoại tuyến trước khi đóng nó lại để lấy lại số dư trên chuỗi. Tuy nhiên, phương pháp này có nhược điểm là yêu cầu một kênh trực tiếp với người khác để nhận hoặc gửi tiền, điều này ngụ ý một giao dịch mở và một giao dịch đóng cho mỗi kênh. Nếu tôi dự định thực hiện một số lượng lớn các khoản thanh toán với người này, việc mở và đóng kênh trở nên có lợi về chi phí. Ngược lại, nếu tôi chỉ cần thực hiện một vài giao dịch Lightning, việc mở một kênh trực tiếp không có lợi, vì nó sẽ tốn cho tôi 2 giao dịch trên chuỗi cho một số lượng hạn chế các giao dịch ngoại tuyến. Trường hợp này có thể xảy ra, ví dụ, khi muốn thanh toán bằng Lightning tại một cửa hàng mà không có kế hoạch quay lại.

Để giải quyết vấn đề này, Mạng Lưới Lightning cho phép định tuyến một khoản thanh toán qua nhiều kênh và nút trung gian, do đó cho phép thực hiện giao dịch mà không cần một kênh trực tiếp với người khác.

Ví dụ, hãy tưởng tượng rằng:

- **Alice** (màu cam) có một kênh với **Suzie** (màu xám) với **100,000 satoshis** ở phía mình và **30,000 satoshis** ở phía Suzie.
- **Suzie** có một kênh với **Bob** trong đó cô ấy sở hữu **250,000 satoshis** và Bob không có satoshis nào.

![LNP201](assets/en/37.webp)

Nếu Alice muốn gửi tiền cho Bob mà không mở một kênh trực tiếp với anh ấy, cô ấy sẽ phải qua Suzie, và mỗi kênh sẽ cần điều chỉnh thanh khoản ở mỗi phía. **Các satoshis được gửi vẫn nằm trong các kênh tương ứng của họ**; chúng thực sự không "vượt qua" các kênh, nhưng việc chuyển giao được thực hiện thông qua việc điều chỉnh thanh khoản nội bộ trong mỗi kênh.

Giả sử Alice muốn gửi **50,000 satoshis** cho Bob:

1. **Alice** gửi 50,000 satoshis cho **Suzie** trong kênh chung của họ.
2. **Suzie** sao chép việc chuyển giao này bằng cách gửi 50,000 satoshis cho **Bob** trong kênh của họ.

![LNP201](assets/en/38.webp)
Vì vậy, khoản thanh toán được chuyển đến Bob thông qua việc di chuyển tính thanh khoản trong từng kênh. Cuối cùng, Alice còn lại với 50,000 sats. Cô ấy thực sự đã chuyển 50,000 sats vì ban đầu, cô ấy có 100,000. Bob, về phía mình, kết thúc với thêm 50,000 sats. Đối với Suzie (nút trung gian), hoạt động này là trung lập: ban đầu, cô ấy có 30,000 sats trong kênh với Alice và 250,000 sats trong kênh với Bob, tổng cộng 280,000 sats. Sau hoạt động, cô ấy giữ 80,000 sats trong kênh với Alice và 200,000 sats trong kênh với Bob, đó là cùng một tổng số như ở khởi điểm.
Do đó, việc chuyển giao này bị giới hạn bởi **tính thanh khoản có sẵn** theo hướng của việc chuyển giao.

### Tính toán Lộ trình và Giới hạn Tính thanh khoản

Hãy lấy một ví dụ lý thuyết về một mạng lưới khác với:

- **130,000 satoshis** ở phía Alice (màu cam) trong kênh của cô ấy với **Suzie** (màu xám).
- **90,000 satoshis** ở phía **Suzie** và **200,000 satoshis** ở phía **Carol** (màu hồng).
- **150,000 satoshis** ở phía **Carol** và **100,000 satoshis** ở phía **Bob**.

![LNP201](assets/en/39.webp)

Số lượng tối đa Alice có thể gửi đến Bob trong cấu hình này là **90,000 satoshis**, vì cô ấy bị giới hạn bởi lượng tính thanh khoản nhỏ nhất có sẵn trong kênh từ **Suzie đến Carol**. Trong hướng ngược lại (từ Bob đến Alice), không có khoản thanh toán nào có thể thực hiện được vì phía **Suzie** trong kênh với **Alice** không chứa satoshis nào. Do đó, không có **lộ trình** nào có thể sử dụng cho việc chuyển giao theo hướng này.
Alice gửi **40,000 satoshis** đến Bob qua các kênh:

1. Alice chuyển 40,000 satoshis đến kênh của cô ấy với Suzie.
2. Suzie chuyển 40,000 satoshis đến Carol trong kênh chung của họ.
3. Cuối cùng, Carol chuyển 40,000 satoshis đến Bob.

![LNP201](assets/en/40.webp)

**Satoshis được gửi** trong mỗi kênh **vẫn ở trong kênh**, vì vậy satoshis được Carol gửi đến Bob không giống như những satoshis được Alice gửi đến Suzie. Việc chuyển giao chỉ được thực hiện bằng cách điều chỉnh tính thanh khoản bên trong mỗi kênh. Hơn nữa, tổng khả năng của các kênh vẫn không thay đổi.

![LNP201](assets/en/41.webp)

Như trong ví dụ trước, sau giao dịch, nút nguồn (Alice) mất đi 40,000 satoshis. Các nút trung gian (Suzie và Carol) giữ lại tổng số tiền như cũ, làm cho hoạt động này trung lập đối với họ. Cuối cùng, nút đích (Bob) nhận thêm 40,000 satoshis.

Vai trò của các nút trung gian do đó rất quan trọng trong việc hoạt động của Lightning Network. Họ tạo điều kiện cho việc chuyển giao bằng cách cung cấp nhiều lộ trình cho các khoản thanh toán. Để khuyến khích các nút này cung cấp tính thanh khoản của họ và tham gia vào việc định tuyến thanh toán, **phí định tuyến** được trả cho họ.

### Phí Định Tuyến

Các nút trung gian áp dụng phí để cho phép thanh toán đi qua các kênh của họ. Phí này được thiết lập bởi **mỗi nút cho mỗi kênh**. Phí bao gồm 2 yếu tố:

1. "**Phí cơ bản**": một số tiền cố định cho mỗi kênh, thường là **1 sat** theo mặc định, nhưng có thể tùy chỉnh.
2. "**Phí biến đổi**": một phần trăm của số tiền chuyển nhượng, được tính bằng **phần triệu (ppm)**. Theo mặc định, nó là **1 ppm** (1 sat cho mỗi triệu satoshis được chuyển), nhưng cũng có thể được điều chỉnh.
   Phí cũng khác nhau tùy thuộc vào hướng của việc chuyển nhượng. Ví dụ, cho một lần chuyển từ Alice sang Suzie, phí của Alice được áp dụng. Ngược lại, từ Suzie sang Alice, phí của Suzie được sử dụng.

Ví dụ, cho một kênh giữa Alice và Suzie, chúng ta có thể có:

- **Alice**: phí cơ bản là 1 sat và 1 ppm cho phí biến đổi.
- **Suzie**: phí cơ bản là 0.5 sat và 10 ppm cho phí biến đổi.

![LNP201](assets/en/42.webp)

Để hiểu rõ hơn cách phí hoạt động, hãy nghiên cứu cùng một Mạng Lưới Lightning như trước, nhưng bây giờ với các phí định tuyến sau:

- Kênh **Alice - Suzie**: phí cơ bản là 1 satoshi và 1 ppm cho Alice.
- Kênh **Suzie - Carol**: phí cơ bản là 0 satoshi và 200 ppm cho Suzie.
- Kênh **Carol - Bob**: phí cơ bản là 1 satoshi và 1 ppm cho Suzie 2.
  ![LNP201](assets/en/43.webp)

Đối với cùng một khoản thanh toán **40,000 satoshis** cho Bob, Alice sẽ phải gửi một chút nhiều hơn, vì mỗi nút trung gian sẽ trừ phí của mình:

- **Carol** trừ 1.04 satoshis trên kênh với Bob:
  $$ f*{\text{Carol-Bob}} = \text{phí cơ bản} + \left(\frac{\text{ppm} \times \text{số lượng}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ sats} $$

- **Suzie** trừ 8 satoshis phí trên kênh với Carol:
  $$ f*{\text{Suzie-Carol}} = \text{phí cơ bản} + \left(\frac{\text{ppm} \times \text{số lượng}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ sats} $$

Tổng số phí cho khoản thanh toán này trên con đường này do đó là **9.04 satoshis**. Do đó, Alice phải gửi **40,009.04 satoshis** để Bob nhận chính xác **40,000 satoshis**.

![LNP201](assets/en/44.webp)

Dung lượng thanh khoản do đó được cập nhật:

![LNP201](assets/en/45.webp)

### Định Tuyến Hành Tinh

Để định tuyến một khoản thanh toán từ người gửi đến người nhận, Mạng Lưới Lightning sử dụng một phương pháp gọi là "**định tuyến hành tinh**". Khác với định tuyến dữ liệu cổ điển, nơi mỗi bộ định tuyến quyết định hướng của dữ liệu dựa trên điểm đến của chúng, định tuyến hành tinh hoạt động khác biệt:

- **Nút gửi tính toán toàn bộ tuyến đường**: Alice, ví dụ, xác định rằng khoản thanh toán của cô ấy phải đi qua Suzie và Carol trước khi đến được Bob.
- **Mỗi nút trung gian chỉ biết về hàng xóm trực tiếp của mình**: Suzie chỉ biết rằng cô ấy nhận được tiền từ Alice và cô ấy phải chuyển chúng cho Carol. Tuy nhiên, Suzie không biết liệu Alice có phải là nút nguồn hay một nút trung gian, và cô ấy cũng không biết liệu Carol có phải là nút nhận cuối cùng hay chỉ là một nút trung gian khác. Nguyên tắc này cũng áp dụng cho Carol và tất cả các nút khác trên đường đi. Do đó, Onion routing bảo vệ sự bảo mật của giao dịch bằng cách che giấu danh tính của người gửi và người nhận cuối cùng. Để đảm bảo nút truyền tải có thể tính toán một lộ trình hoàn chỉnh đến người nhận trong Onion routing, nó phải duy trì một **đồ thị mạng** để biết topologi của mình và xác định các lộ trình có thể.
  **Bạn nên rút ra điều gì từ chương này?**

1. Trên Lightning, thanh toán có thể được định tuyến giữa các nút không trực tiếp kết nối thông qua các kênh trung gian. Mỗi nút trung gian này hỗ trợ việc chuyển tiếp thanh khoản.
2. Các nút trung gian nhận được hoa hồng cho dịch vụ của mình, bao gồm phí cố định và phí biến đổi.
3. Onion routing cho phép nút truyền tải tính toán lộ trình hoàn chỉnh mà không cần các nút trung gian biết nguồn hoặc điểm đến cuối cùng.

Trong chương này, chúng ta đã khám phá việc định tuyến thanh toán trên Mạng Lưới Lightning. Nhưng một câu hỏi được đặt ra: điều gì ngăn cản các nút trung gian chấp nhận một khoản thanh toán đến mà không chuyển tiếp nó đến điểm đến tiếp theo, với mục đích chặn giao dịch? Đây chính xác là vai trò của HTLCs mà chúng ta sẽ nghiên cứu trong chương tiếp theo.

## HTLC – Hợp Đồng Thời Gian Khóa Băm

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

Trong chương này, chúng ta sẽ khám phá cách Lightning cho phép thanh toán di chuyển qua các nút trung gian mà không cần phải tin tưởng họ, nhờ vào **HTLC** (_Hợp Đồng Thời Gian Khóa Băm_). Những hợp đồng thông minh này đảm bảo rằng mỗi nút trung gian chỉ nhận được tiền từ kênh của mình nếu nó chuyển tiếp thanh toán cho người nhận cuối cùng, nếu không, thanh toán sẽ không được xác nhận.

Vấn đề đặt ra cho việc định tuyến thanh toán do đó là sự tin tưởng cần thiết ở các nút trung gian, và giữa chính các nút trung gian. Để minh họa điều này, hãy xem lại ví dụ mạng Lightning đơn giản của chúng ta với 3 nút và 2 kênh:

- Alice có một kênh với Suzie.
- Suzie có một kênh với Bob.

Alice muốn gửi 40,000 sats cho Bob nhưng cô ấy không có một kênh trực tiếp với anh ấy và không muốn mở một kênh. Cô ấy tìm kiếm một lộ trình và quyết định đi qua nút của Suzie.

![LNP201](assets/en/46.webp)

Nếu Alice một cách ngây thơ gửi 40,000 satoshis cho Suzie hy vọng rằng Suzie sẽ chuyển số tiền này cho Bob, Suzie có thể giữ số tiền cho mình và không chuyển gì cho Bob.

![LNP201](assets/en/47.webp)
Để tránh tình huống này, trên Lightning, chúng ta sử dụng HTLCs (Hợp Đồng Thời Gian Khóa Băm), làm cho việc thanh toán cho nút trung gian có điều kiện, nghĩa là Suzie phải đáp ứng một số điều kiện nhất định để truy cập vào tiền của Alice và chuyển chúng cho Bob.

### Cách HTLCs Hoạt Động

HTLC là một hợp đồng đặc biệt dựa trên hai nguyên tắc:

- **Điều kiện truy cập**: Người nhận phải tiết lộ một bí mật để mở khóa thanh toán dành cho họ.
- **Hết hạn**: Nếu thanh toán không được hoàn thành hoàn toàn trong một khoảng thời gian đã định, nó sẽ bị hủy và tiền sẽ trở về với người gửi.

Dưới đây là cách quy trình này hoạt động trong ví dụ của chúng ta với Alice, Suzie, và Bob:

![LNP201](assets/en/48.webp)
**Tạo bí mật**: Bob tạo một bí mật ngẫu nhiên được ký hiệu là _s_ (hình ảnh trước), và tính toán băm của nó được ký hiệu là _r_ với hàm băm được ký hiệu là _h_. Chúng ta có:

$$
r = h(s)
$$

Sử dụng hàm băm làm cho việc tìm _s_ chỉ với _h(s)_ trở nên không thể, nhưng nếu _s_ được cung cấp, việc xác minh nó tương ứng với _h(s)_ trở nên dễ dàng.

![LNP201](assets/en/49.webp)

**Gửi yêu cầu thanh toán**: Bob gửi một **hóa đơn** cho Alice yêu cầu một khoản thanh toán. Hóa đơn này đặc biệt bao gồm băm _r_.

![LNP201](assets/en/50.webp)

**Gửi thanh toán có điều kiện**: Alice gửi một HTLC của 40,000 satoshis cho Suzie. Điều kiện để Suzie nhận được số tiền này là cô ấy cung cấp cho Alice một bí mật _s'_ thỏa mãn phương trình sau:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**Chuyển HTLC cho người nhận cuối cùng**: Suzie, để nhận được 40,000 satoshis từ Alice, phải chuyển một HTLC tương tự của 40,000 satoshis cho Bob, người có điều kiện tương tự, tức là anh ta phải cung cấp cho Suzie một bí mật _s'_ thỏa mãn phương trình:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Xác nhận bằng bí mật _s_**: Bob cung cấp _s_ cho Suzie để nhận được 40,000 satoshis hứa hẹn trong HTLC. Với bí mật này, Suzie có thể mở khóa HTLC của Alice và nhận được 40,000 satoshis từ Alice. Khoản thanh toán sau đó được chuyển đúng cho Bob.

![LNP201](assets/en/53.webp)
Quy trình này ngăn Suzie giữ tiền của Alice mà không hoàn thành việc chuyển tiền cho Bob, vì cô ấy phải gửi thanh toán cho Bob để nhận được bí mật _s_ và do đó mở khóa HTLC của Alice. Hoạt động vẫn giữ nguyên ngay cả khi tuyến đường bao gồm nhiều nút trung gian: chỉ là việc lặp lại các bước của Suzie cho mỗi nút trung gian. Mỗi nút được bảo vệ bởi điều kiện của các HTLC, vì việc mở khóa HTLC cuối cùng bởi người nhận tự động kích hoạt việc mở khóa tất cả các HTLC khác theo cách thác nước.

### Hết hạn và quản lý HTLC trong trường hợp có vấn đề

Nếu trong quá trình thanh toán, một trong các nút trung gian, hoặc nút nhận, ngừng phản hồi, đặc biệt trong trường hợp mất internet hoặc mất điện, thì việc thanh toán không thể hoàn thành, bởi vì bí mật cần thiết để mở khóa các HTLC không được truyền đi. Lấy ví dụ của chúng ta với Alice, Suzie, và Bob, vấn đề này xảy ra, ví dụ, nếu Bob không truyền bí mật _s_ cho Suzie. Trong trường hợp này, tất cả các HTLC trên dòng đường bị chặn, và số tiền họ bảo đảm cũng vậy.

![LNP201](assets/en/54.webp)

Để tránh điều này, HTLC trên Lightning có một thời hạn hết hạn cho phép loại bỏ HTLC nếu nó không được hoàn thành sau một thời gian nhất định. Thời hạn hết hạn tuân theo một trật tự cụ thể vì nó bắt đầu trước tiên với HTLC gần nhất với người nhận, và sau đó dần dần di chuyển lên đến người phát hành giao dịch. Trong ví dụ của chúng ta, nếu Bob không bao giờ cung cấp bí mật _s_ cho Suzie, điều này sẽ đầu tiên khiến HTLC của Suzie về phía Bob hết hạn.

![LNP201](assets/en/55.webp)

Sau đó là HTLC từ Alice đến Suzie.
Nếu thứ tự hết hạn của HTLC được đảo ngược, Alice có thể thu hồi thanh toán của mình trước khi Suzie có thể bảo vệ mình khỏi khả năng bị lừa. Thực sự, nếu Bob quay lại để yêu cầu HTLC của mình trong khi Alice đã loại bỏ HTLC của mình, Suzie sẽ ở vào thế bất lợi. Do đó, thứ tự hết hạn của HTLC theo cấp độ này đảm bảo rằng không có nút trung gian nào phải chịu tổn thất không công bằng.

### Biểu diễn của HTLCs trong các giao dịch cam kết

Các giao dịch cam kết biểu diễn HTLCs theo cách mà các điều kiện họ áp đặt lên Lightning có thể được chuyển sang Bitcoin trong trường hợp đóng kênh ép buộc trong thời gian sống của một HTLC. Như một lời nhắc nhở, các giao dịch cam kết đại diện cho trạng thái hiện tại của kênh giữa hai người dùng và cho phép đóng kênh một cách ép buộc trong trường hợp có vấn đề. Với mỗi trạng thái mới của kênh, 2 giao dịch cam kết được tạo ra: một cho mỗi bên. Hãy xem xét lại ví dụ của chúng tôi với Alice, Suzie và Bob, nhưng nhìn kỹ hơn vào những gì xảy ra ở cấp độ kênh giữa Alice và Suzie khi HTLC được tạo.

Trước khi bắt đầu thanh toán 40,000 sats giữa Alice và Bob, Alice có 100,000 sats trong kênh của mình với Suzie, trong khi Suzie giữ 30,000. Các giao dịch cam kết của họ như sau:

Alice vừa nhận được hóa đơn của Bob, đáng chú ý chứa _r_, băm của bí mật. Do đó, cô ấy có thể tạo một HTLC 40,000 satoshis với Suzie. HTLC này được biểu diễn trong các giao dịch cam kết mới nhất như một đầu ra được gọi là "**_HTLC Out_**" ở phía Alice, vì các quỹ đang đi ra, và "**_HTLC In_**" ở phía Suzie, vì các quỹ đang đi vào.

Các đầu ra liên quan đến HTLC chia sẻ chính xác cùng một điều kiện, cụ thể là:

- Nếu Suzie có thể cung cấp bí mật _s_, cô ấy có thể mở khóa đầu ra này ngay lập tức và chuyển nó đến một địa chỉ cô ấy kiểm soát.
- Nếu Suzie không sở hữu bí mật _s_, cô ấy không thể mở khóa đầu ra này, và Alice sẽ có thể mở khóa nó sau một khoảng thời gian để gửi nó đến một địa chỉ cô ấy kiểm soát. Khoảng thời gian này do đó cấp cho Suzie một khoảng thời gian để phản ứng nếu cô ấy có được _s_.

Những điều kiện này chỉ áp dụng nếu kênh được đóng (tức là, một giao dịch cam kết được công bố trên chuỗi) trong khi HTLC vẫn còn hoạt động trên Lightning, nghĩa là thanh toán giữa Alice và Bob chưa được hoàn tất, và các HTLC chưa hết hạn. Nhờ những điều kiện này, Suzie có thể thu hồi 40,000 satoshis của HTLC nợ cô ấy bằng cách cung cấp _s_. Nếu không, Alice thu hồi các quỹ sau khi hết hạn của khoảng thời gian, bởi vì nếu Suzie không biết _s_, điều đó có nghĩa là cô ấy đã không chuyển 40,000 satoshis cho Bob, và do đó, các quỹ của Alice không nợ cô ấy.

Hơn nữa, nếu kênh được đóng trong khi nhiều HTLCs đang chờ xử lý, sẽ có nhiều đầu ra bổ sung tương ứng với số lượng HTLCs đang diễn ra.
Nếu kênh không được đóng, sau khi thanh toán Lightning hết hạn hoặc thành công, các giao dịch cam kết mới được tạo ra để phản ánh trạng thái mới, ổn định của kênh, tức là không có HTLCs nào đang chờ xử lý. Các đầu ra liên quan đến HTLCs do đó có thể được loại bỏ khỏi các giao dịch cam kết.
Cuối cùng, trong trường hợp đóng kênh hợp tác khi một HTLC đang hoạt động, Alice và Suzie ngừng chấp nhận thanh toán mới và chờ đợi sự giải quyết hoặc hết hạn của các HTLC đang diễn ra. Điều này cho phép họ công bố một giao dịch đóng kênh nhẹ nhàng hơn, không bao gồm các đầu ra liên quan đến HTLCs, từ đó giảm phí và tránh việc chờ đợi một khóa thời gian có thể xảy ra.

**Bạn nên rút ra điều gì từ chương này?**

HTLCs cho phép việc chuyển hướng thanh toán Lightning qua nhiều nút mà không cần phải tin tưởng chúng. Dưới đây là các điểm chính cần nhớ:

1. HTLCs đảm bảo an toàn cho các khoản thanh toán thông qua một bí mật (preimage) và thời gian hết hạn.
2. Việc giải quyết hoặc hết hạn của HTLCs tuân theo một trật tự cụ thể: sau đó từ điểm đến về phía nguồn, nhằm bảo vệ mỗi nút.
3. Miễn là một HTLC chưa được giải quyết hoặc hết hạn, nó được duy trì như một đầu ra trong các giao dịch cam kết mới nhất.

Trong chương tiếp theo, chúng ta sẽ khám phá cách một nút phát hành một giao dịch Lightning tìm và chọn lựa các tuyến đường cho khoản thanh toán của mình để đạt được nút nhận.

## Tìm Đường Đi

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![tìm đường đi](https://youtu.be/wnUGJjOxd9Q)

Trong các chương trước, chúng ta đã thấy cách sử dụng các kênh của nút khác để chuyển hướng thanh toán và đạt được một nút mà không cần kết nối trực tiếp với nó qua một kênh. Chúng ta cũng đã thảo luận cách đảm bảo an toàn cho việc chuyển giao mà không cần tin tưởng các nút trung gian. Trong chương này, chúng ta sẽ tập trung vào việc tìm tuyến đường tốt nhất có thể để đạt được nút mục tiêu.

### Vấn Đề Định Tuyến trong Lightning

Như chúng ta đã thấy, trong Lightning, đó là nút gửi thanh toán phải tính toán toàn bộ tuyến đường đến người nhận, bởi vì chúng ta sử dụng một hệ thống định tuyến kiểu hành tây. Các nút trung gian không biết điểm xuất phát hoặc điểm đến cuối cùng. Họ chỉ biết nơi thanh toán đến từ đâu và nút nào họ phải chuyển tiếp tiếp theo. Điều này có nghĩa là nút gửi phải duy trì một cấu trúc mạng lưới địa phương động, với các nút Lightning hiện có và các kênh giữa chúng, tính đến việc mở, đóng và cập nhật trạng thái.

![LNP201](assets/en/61.webp)
Ngay cả với cấu trúc mạng Lightning này, có thông tin thiết yếu cho việc định tuyến vẫn không thể truy cập được bởi nút gửi, đó là phân phối chính xác của thanh khoản trong các kênh tại bất kỳ thời điểm nào. Thực tế, mỗi kênh chỉ hiển thị **tổng công suất** của nó, nhưng phân phối nội bộ của quỹ chỉ được biết đến bởi hai nút tham gia. Điều này đặt ra thách thức cho việc định tuyến hiệu quả, vì sự thành công của khoản thanh toán phụ thuộc đáng kể vào việc số tiền của nó ít hơn thanh khoản thấp nhất trên tuyến đường được chọn. Tuy nhiên, các thanh khoản không phải tất cả đều hiển thị cho nút gửi.
![LNP201](assets/en/62.webp)

### Cập Nhật Bản Đồ Mạng

Để giữ bản đồ mạng của họ được cập nhật, các nút thường xuyên trao đổi thông điệp thông qua một thuật toán gọi là "**_gossip_**". Đây là một thuật toán phân tán được sử dụng để lan truyền thông tin theo cách dịch bệnh đến tất cả các nút trong mạng, cho phép trao đổi và đồng bộ hóa trạng thái toàn cầu của các kênh trong vài chu kỳ giao tiếp. Mỗi nút lan truyền thông tin đến một hoặc nhiều hàng xóm được chọn một cách ngẫu nhiên hoặc không, những nút này, lần lượt, lan truyền thông tin đến các hàng xóm khác và cứ thế cho đến khi đạt được trạng thái đồng bộ hóa toàn cầu.

2 thông điệp chính được trao đổi giữa các nút Lightning như sau:

- "**Thông Báo Kênh**": các thông điệp báo hiệu việc mở một kênh mới.
- "**Cập Nhật Kênh**": cập nhật thông điệp về trạng thái của một kênh, đặc biệt là về sự phát triển của phí (nhưng không phải về phân phối thanh khoản).
  Các nút Lightning cũng theo dõi blockchain Bitcoin để phát hiện các giao dịch đóng kênh. Kênh đã đóng sau đó sẽ được loại bỏ khỏi bản đồ vì nó không thể được sử dụng để định tuyến các khoản thanh toán của chúng ta nữa.

### Định Tuyến Một Khoản Thanh Toán

Hãy lấy ví dụ về một mạng Lightning nhỏ với 7 nút: Alice, Bob, 1, 2, 3, 4, và 5. Hãy tưởng tượng rằng Alice muốn gửi một khoản thanh toán cho Bob nhưng phải thông qua các nút trung gian.

![LNP201](assets/en/63.webp)

Dưới đây là phân phối thực tế của quỹ trong các kênh này:

- **Kênh giữa Alice và 1**: 250,000 sats ở phía Alice, 80,000 ở phía 1 (tổng dung lượng là 330,000 sats).
- **Kênh giữa 1 và 2**: 300,000 sats ở phía 1, 200,000 ở phía 2 (tổng dung lượng là 500,000 sats).
- **Kênh giữa 2 và 3**: 50,000 sats ở phía 2, 60,000 ở phía 3 (tổng dung lượng là 110,000 sats).
- **Kênh giữa 2 và 5**: 90,000 sats ở phía 2, 160,000 ở phía 5 (tổng dung lượng là 250,000 sats).
- **Kênh giữa 2 và 4**: 180,000 sats ở phía 2, 110,000 ở phía 4 (tổng dung lượng là 290,000 sats).
- **Kênh giữa 4 và 5**: 200,000 sats ở phía 4, 10,000 ở phía 5 (tổng dung lượng là 210,000 sats).
- **Kênh giữa 3 và Bob**: 50,000 sats ở phía 3, 250,000 ở phía Bob (tổng dung lượng là 300,000 sats).
- **Kênh giữa 5 và Bob**: 260,000 sats ở phía 5, 100,000 ở phía Bob (tổng dung lượng là 360,000 sats).

![LNP201](assets/en/64.webp)

Để thực hiện một khoản thanh toán 100,000 sats từ Alice đến Bob, các lựa chọn định tuyến bị giới hạn bởi thanh khoản có sẵn trong mỗi kênh. Lộ trình tối ưu cho Alice, dựa trên phân phối thanh khoản đã biết, có thể là chuỗi `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Nhưng vì Alice không biết chính xác phân phối quỹ trong mỗi kênh, cô ấy phải ước lượng lộ trình tối ưu một cách có xác suất, lưu ý đến các tiêu chí sau:

- **Xác suất thành công**: một kênh có tổng dung lượng lớn hơn có khả năng chứa đủ thanh khoản hơn. Ví dụ, kênh giữa nút 2 và nút 3 có tổng dung lượng là 110,000 sats, vì vậy nó khó có thể tìm thấy 100,000 sats hoặc nhiều hơn ở phía nút 2, mặc dù điều này vẫn có thể xảy ra.
- **Phí giao dịch**: khi chọn lộ trình tốt nhất, nút gửi cũng xem xét các phí do mỗi nút trung gian áp dụng và tìm cách giảm thiểu tổng chi phí định tuyến.
- **Hết hạn của HTLCs**: để tránh việc thanh toán bị chặn, thời gian hết hạn của HTLCs cũng là một tham số cần xem xét.
- **Số lượng nút trung gian**: cuối cùng, một cách rộng rãi hơn, nút gửi sẽ tìm cách tìm một tuyến đường với ít nút trung gian nhất có thể để giảm thiểu rủi ro thất bại và hạn chế phí giao dịch Lightning.
  Bằng cách phân tích những tiêu chí này, nút gửi có thể thử nghiệm các tuyến đường có khả năng nhất và cố gắng tối ưu hóa chúng. Trong ví dụ của chúng ta, Alice có thể xếp hạng các tuyến đường tốt nhất như sau:

1. `Alice → 1 → 2 → 5 → Bob`, vì đây là tuyến đường ngắn nhất với dung lượng cao nhất.
2. `Alice → 1 → 2 → 4 → 5 → Bob`, vì tuyến đường này cung cấp dung lượng tốt, mặc dù dài hơn tuyến đầu tiên.
3. `Alice → 1 → 2 → 3 → Bob`, vì tuyến đường này bao gồm kênh `2 → 3`, có dung lượng rất hạn chế, nhưng vẫn có khả năng sử dụng.

### Thực Hiện Thanh Toán

Alice quyết định thử tuyến đường đầu tiên của mình (`Alice → 1 → 2 → 5 → Bob`). Do đó, cô ấy gửi một HTLC 100,000 sats đến nút 1. Nút này kiểm tra xem nó có đủ thanh khoản với nút 2 không, và tiếp tục truyền dẫn. Nút 2 sau đó nhận HTLC từ nút 1, nhưng nhận ra rằng nó không có đủ thanh khoản trong kênh của mình với nút 5 để chuyển một khoản thanh toán 100,000 sats. Nó sau đó gửi một thông điệp lỗi trở lại cho nút 1, người truyền nó cho Alice. Tuyến đường này đã thất bại.

![LNP201](assets/en/66.webp)

Sau đó, Alice cố gắng chuyển khoản thanh toán của mình sử dụng tuyến đường thứ hai của mình (`Alice → 1 → 2 → 4 → 5 → Bob`). Cô ấy gửi một HTLC 100,000 sats đến nút 1, người truyền nó đến nút 2, sau đó đến nút 4, đến nút 5, và cuối cùng đến Bob. Lần này, thanh khoản đủ, và tuyến đường hoạt động. Mỗi nút mở khóa HTLC của mình theo cách xếp tầng sử dụng preimage được Bob cung cấp (bí mật _s_), điều này cho phép thanh toán của Alice cho Bob được hoàn thành thành công.

![LNP201](assets/en/67.webp)

Việc tìm kiếm một tuyến đường được thực hiện như sau: nút gửi bắt đầu bằng cách xác định các tuyến đường tốt nhất có thể, sau đó thử thanh toán lần lượt cho đến khi tìm được một tuyến đường hoạt động.

Đáng chú ý là Bob có thể cung cấp thông tin cho Alice trong **hóa đơn** để tạo điều kiện thuận lợi cho việc định tuyến. Ví dụ, anh ấy có thể chỉ ra các kênh gần đó với thanh khoản đủ hoặc tiết lộ sự tồn tại của các kênh riêng tư. Những chỉ dẫn này cho phép Alice tránh các tuyến đường ít có khả năng thành công và trước tiên thử các con đường được Bob khuyến nghị.

**Bạn nên rút ra điều gì từ chương này?**

1. Các nút duy trì một bản đồ về cấu trúc mạng thông qua các thông báo và bằng cách theo dõi việc đóng kênh trên blockchain Bitcoin.
2. Việc tìm kiếm một tuyến đường tối ưu cho một khoản thanh toán vẫn mang tính chất xác suất và phụ thuộc vào nhiều tiêu chí.
3. Bob có thể cung cấp chỉ dẫn trong **hóa đơn** để hướng dẫn việc định tuyến của Alice và giúp cô ấy tránh thử nghiệm các tuyến đường không có khả năng thành công.

Trong chương tiếp theo, chúng ta sẽ cụ thể nghiên cứu về cách hoạt động của hóa đơn, cùng với một số công cụ khác được sử dụng trên Mạng Lưới Lightning.

# Công Cụ của Mạng Lưới Lightning

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Hóa Đơn, LNURL, và Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
![hóa đơn, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)
Trong chương này, chúng ta sẽ xem xét kỹ lưỡng hơn về cách thức hoạt động của **hóa đơn** Lightning, tức là yêu cầu thanh toán được gửi bởi nút nhận đến nút gửi. Mục tiêu là hiểu cách thức thanh toán và nhận thanh toán trên Lightning. Chúng ta cũng sẽ thảo luận về 2 phương án thay thế cho hóa đơn truyền thống: LNURL và Keysend.
![LNP201](assets/en/68.webp)

### Cấu Trúc của Hóa Đơn Lightning

Như đã giải thích trong chương về HTLCs, mỗi giao dịch thanh toán bắt đầu với việc tạo ra một **hóa đơn** bởi người nhận. Hóa đơn này sau đó được truyền đến người thanh toán (qua mã QR hoặc bằng cách sao chép và dán) để khởi đầu giao dịch thanh toán. Một hóa đơn bao gồm hai phần chính:

1. **Phần Dễ Đọc**: phần này chứa metadata rõ ràng nhìn thấy được để nâng cao trải nghiệm người dùng.
2. **Phần Payload**: phần này bao gồm thông tin dành cho máy móc để xử lý giao dịch thanh toán.

Cấu trúc điển hình của một hóa đơn bắt đầu với một định danh `ln` cho "Lightning", tiếp theo là `bc` cho Bitcoin, sau đó là số lượng của hóa đơn. Một dấu phân cách `1` phân biệt phần dễ đọc với phần dữ liệu (payload).

Hãy xem xét hóa đơn sau đây là một ví dụ:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Chúng ta có thể chia nó thành 2 phần. Đầu tiên, đó là Phần Dễ Đọc:

```invoice
lnbc100u
```

Sau đó là phần dành cho payload:

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Hai phần được tách biệt bởi một `1`. Dấu phân cách này được chọn thay vì một ký tự đặc biệt để cho phép sao chép dễ dàng toàn bộ hóa đơn bằng cách nhấp đúp.

Trong phần đầu tiên, chúng ta có thể thấy:

- `ln` chỉ ra rằng đây là một giao dịch Lightning.
- `bc` chỉ ra rằng mạng Lightning hoạt động trên blockchain Bitcoin (không phải trên testnet hoặc trên Litecoin).
- `100u` chỉ ra số lượng của hóa đơn, được biểu thị bằng **microsatoshis** (`u` có nghĩa là "micro"), tương đương ở đây là 10,000 sats.

Để chỉ định số lượng thanh toán, nó được biểu thị bằng các đơn vị phụ của bitcoin. Dưới đây là các đơn vị được sử dụng:

- **Millibitcoin (ký hiệu `m`):** Đại diện cho một phần nghìn của một bitcoin.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
  $$

- **Microbitcoin (ký hiệu `u`):** Còn được gọi là "bit", đại diện cho một phần triệu của một bitcoin.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
  $$

- **Nanobitcoin (ký hiệu `n`):** Đại diện cho một phần tỷ của một bitcoin.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
  $$

- **Picobitcoin (ký hiệu `p`):** Đại diện cho một phần nghìn tỷ của một bitcoin.
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
  $$

### Nội Dung của một Hóa Đơn

Nội dung của một hóa đơn bao gồm một số thông tin cần thiết để xử lý thanh toán:

- **Dấu thời gian:** Thời điểm tạo hóa đơn, được biểu thị bằng Unix Timestamp (số giây đã trôi qua kể từ ngày 1 tháng 1 năm 1970).
- **Băm Bí Mật**: Như chúng ta đã thấy trong phần về HTLCs, nút nhận phải cung cấp cho nút gửi băm của preimage. Điều này được sử dụng trong HTLCs để bảo đảm giao dịch. Chúng tôi gọi nó là "_r_".
- **Bí Mật Thanh Toán**: Một bí mật khác được tạo ra bởi người nhận, nhưng lần này nó được truyền đến nút gửi. Nó được sử dụng trong onion routing để ngăn các nút trung gian đoán liệu nút tiếp theo có phải là người nhận cuối cùng hay không. Điều này duy trì một hình thức bảo mật cho người nhận đối với nút trung gian cuối cùng trên tuyến đường.
- **Khóa Công Khai của Người Nhận**: Chỉ ra cho người thanh toán biết định danh của người được thanh toán.
- **Thời Gian Hết Hạn**: Thời gian tối đa để thanh toán hóa đơn (mặc định là 1 giờ).
- **Gợi Ý Định Tuyến**: Thông tin bổ sung do người nhận cung cấp để giúp người gửi tối ưu hóa tuyến đường thanh toán.
- **Chữ Ký**: Đảm bảo tính toàn vẹn của hóa đơn bằng cách xác thực tất cả thông tin.

Các hóa đơn sau đó được mã hóa trong **bech32**, cùng một định dạng như địa chỉ Bitcoin SegWit (định dạng bắt đầu với `bc1`).

### LNURL Rút Tiền

Trong một giao dịch truyền thống, như mua hàng tại cửa hàng, hóa đơn được tạo ra cho tổng số tiền cần thanh toán. Khi hóa đơn được trình bày (dưới dạng mã QR hoặc chuỗi ký tự), khách hàng có thể quét nó và hoàn tất giao dịch. Sau đó, việc thanh toán tuân theo quy trình truyền thống mà chúng ta đã nghiên cứu trong phần trước. Tuy nhiên, quy trình này đôi khi có thể rất phức tạp đối với trải nghiệm người dùng, vì nó yêu cầu người nhận gửi thông tin cho người gửi qua hóa đơn.
Đối với một số tình huống, như rút bitcoin từ một dịch vụ trực tuyến, quy trình truyền thống quá phức tạp. Trong những trường hợp như vậy, giải pháp rút tiền **LNURL** đơn giản hóa quy trình này bằng cách hiển thị mã QR mà ví của người nhận quét để tự động tạo hóa đơn. Sau đó, dịch vụ thanh toán hóa đơn, và người dùng chỉ thấy một giao dịch rút tiền tức thì.

![LNP201](assets/en/69.webp)

LNURL là một giao thức truyền thông quy định một tập hợp các chức năng được thiết kế để đơn giản hóa các tương tác giữa các nút Lightning và khách hàng, cũng như các ứng dụng bên thứ ba. Việc rút tiền LNURL, như chúng ta vừa thấy, chỉ là một ví dụ trong số các chức năng khác.
Giao thức này dựa trên HTTP và cho phép tạo liên kết cho các hoạt động khác nhau, như yêu cầu thanh toán, yêu cầu rút tiền, hoặc các chức năng khác nhằm nâng cao trải nghiệm người dùng. Mỗi LNURL là một URL được mã hóa bech32 với tiền tố lnurl, khi được quét, kích hoạt một loạt các hành động tự động trên ví Lightning.
Ví dụ, tính năng LNURL-withdraw (LUD-03) cho phép rút tiền từ một dịch vụ bằng cách quét mã QR, mà không cần phải tạo hóa đơn một cách thủ công. Tương tự, LNURL-auth (LUD-04) cho phép đăng nhập vào các dịch vụ trực tuyến bằng cách sử dụng khóa riêng trên ví Lightning của mình thay vì mật khẩu.

### Gửi một Khoản Thanh Toán Lightning Không Cần Hóa Đơn: Keysend

Một trường hợp thú vị khác là chuyển tiền mà không cần nhận hóa đơn trước, được biết đến là "**Keysend**". Giao thức này cho phép gửi tiền bằng cách thêm một preimage vào dữ liệu thanh toán được mã hóa, chỉ có thể truy cập bởi người nhận. Preimage này cho phép người nhận mở khóa HTLC, do đó thu hồi tiền mà không cần tạo hóa đơn trước.

Để đơn giản hóa, trong giao thức này, chính người gửi tạo ra bí mật được sử dụng trong các HTLCs, thay vì người nhận. Thực tế, điều này cho phép người gửi thực hiện một khoản thanh toán mà không cần phải tương tác với người nhận trước đó.

![LNP201](assets/en/70.webp)

**Những điều bạn nên rút ra từ chương này?**

1. Một **Hóa Đơn Lightning** là một yêu cầu thanh toán bao gồm một phần dễ đọc và một phần dữ liệu máy.
2. Hóa đơn được mã hóa trong **bech32**, với một dấu phân cách `1` để dễ dàng sao chép và một phần dữ liệu chứa tất cả thông tin cần thiết để xử lý thanh toán.
3. Các quy trình thanh toán khác tồn tại trên Lightning, đáng chú ý là **LNURL-Withdraw** để đơn giản hóa việc rút tiền, và **Keysend** cho các chuyển tiền trực tiếp không cần hóa đơn.

Trong chương tiếp theo, chúng ta sẽ xem xét cách một người vận hành nút có thể quản lý tính thanh khoản trong các kênh của mình, để không bao giờ bị chặn và luôn có thể gửi và nhận thanh toán trên Mạng Lưới Lightning.

## Quản Lý Tính Thanh Khoản của Bạn

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![quản lý tính thanh khoản của bạn](https://youtu.be/YuPrbhEJXbg)

Trong chương này, chúng ta sẽ khám phá các chiến lược để quản lý tính thanh khoản một cách hiệu quả trên Mạng Lưới Lightning. Việc quản lý tính thanh khoản thay đổi tùy thuộc vào loại người dùng và bối cảnh. Chúng ta sẽ xem xét các nguyên tắc chính và các kỹ thuật hiện có để hiểu rõ hơn cách tối ưu hóa việc quản lý này.

### Nhu Cầu về Tính Thanh Khoản

Có ba hồ sơ người dùng chính trên Lightning, mỗi người có nhu cầu thanh khoản cụ thể:

1. **Người thanh toán (The Payer)**: Đây là người thực hiện thanh toán. Họ cần thanh khoản ra để có thể chuyển tiền cho người dùng khác. Ví dụ, đây có thể là một người tiêu dùng.
2. **Người bán (hoặc Người nhận thanh toán - The Seller or Payee)**: Đây là người nhận thanh toán. Họ cần thanh khoản vào để có thể chấp nhận thanh toán vào nút của mình. Ví dụ, đây có thể là một doanh nghiệp hoặc một cửa hàng trực tuyến.
3. **Người điều hướng (The Router)**: Một nút trung gian, thường chuyên về điều hướng thanh toán, cần phải tối ưu hóa thanh khoản của mình trong mỗi kênh để điều hướng càng nhiều thanh toán càng tốt và kiếm được phí.

Rõ ràng, những hồ sơ này không cố định; một người dùng có thể chuyển đổi giữa người thanh toán và người nhận thanh toán tùy thuộc vào các giao dịch. Ví dụ, Bob có thể nhận lương trên Lightning từ nhà tuyển dụng của mình, đặt anh ta vào vị trí của một "người bán" cần thanh khoản vào. Sau đó, nếu anh ta muốn sử dụng lương của mình để mua thức ăn, anh ta trở thành một "người thanh toán" và sau đó phải có thanh khoản ra.

Để hiểu rõ hơn, hãy lấy ví dụ về một mạng lưới đơn giản gồm ba nút: người mua (Alice), người điều hướng (Suzie), và người bán (Bob).

![LNP201](assets/en/71.webp)

Hãy tưởng tượng rằng người mua muốn gửi 30,000 sats cho người bán và thanh toán được thực hiện qua nút của người điều hướng. Mỗi bên sau đó phải có một lượng thanh khoản tối thiểu theo hướng của thanh toán:

- Người thanh toán phải có ít nhất 30,000 satoshi ở phía của họ trong kênh với người điều hướng.
- Người bán phải có một kênh nơi 30,000 satoshi ở phía đối diện để có thể nhận chúng.
- Người điều hướng phải có 30,000 satoshi ở phía người thanh toán trong kênh của họ, và cũng 30,000 satoshi ở phía của họ trong kênh với người bán, để có thể điều hướng thanh toán.

![LNP201](assets/en/72.webp)

### Chiến lược Quản lý Thanh khoản

Người thanh toán phải đảm bảo duy trì đủ thanh khoản ở phía của họ trong các kênh để đảm bảo thanh khoản ra. Điều này được chứng minh là tương đối đơn giản, vì chỉ cần mở các kênh Lightning mới để có thanh khoản này. Thực tế, các quỹ khóa ban đầu trong multisig on-chain hoàn toàn ở phía người thanh toán trong kênh Lightning ngay từ đầu. Khả năng thanh toán do đó được đảm bảo miễn là các kênh được mở với đủ quỹ. Khi thanh khoản ra cạn kiệt, chỉ cần mở các kênh mới.
Ngược lại, đối với người bán, nhiệm vụ này phức tạp hơn. Để có thể nhận thanh toán, họ phải có thanh khoản ở phía đối diện của các kênh của họ. Do đó, việc mở một kênh không đủ: họ cũng phải thực hiện một thanh toán trong kênh này để di chuyển thanh khoản sang phía bên kia trước khi họ có thể tự nhận thanh toán. Đối với một số hồ sơ người dùng Lightning cụ thể, như các nhà bán lẻ, có sự chênh lệch rõ ràng giữa những gì nút của họ gửi và nhận, vì mục tiêu chính của một doanh nghiệp là thu nhiều hơn chi để tạo ra lợi nhuận. May mắn thay, đối với những người dùng này với nhu cầu thanh khoản vào cụ thể, một số giải pháp tồn tại:

- **Thu hút các kênh**: Người bán có lợi thế do khối lượng thanh toán vào dự kiến trên nút của họ. Lấy điều này vào tài khoản, họ có thể cố gắng thu hút các nút điều hướng đang tìm kiếm thu nhập từ phí giao dịch và có thể mở các kênh về phía họ, hy vọng sẽ điều hướng các thanh toán của họ và thu thập các phí liên quan.
- **Di chuyển thanh khoản**: Người bán cũng có thể mở một kênh và chuyển một số tiền về phía đối diện bằng cách thực hiện các khoản thanh toán giả mạo cho một nút khác, nút này sau đó sẽ trả lại tiền theo một cách khác. Chúng ta sẽ xem trong phần tiếp theo cách thực hiện thao tác này.
- **Mở kênh tam giác**: Các nền tảng tồn tại cho các nút muốn mở kênh một cách cộng tác, cho phép mỗi người hưởng lợi từ thanh khoản đến và đi ngay lập tức. Ví dụ, [LightningNetwork+](https://lightningnetwork.plus/) cung cấp dịch vụ này. Nếu Alice, Bob và Suzie muốn mở một kênh với 100,000 sats, họ có thể thỏa thuận trên nền tảng này để Alice mở một kênh về phía Bob, Bob về phía Suzie, và Suzie về phía Alice. Theo cách này, mỗi người có 100,000 sats của thanh khoản đi và 100,000 sats của thanh khoản đến, trong khi chỉ phong tỏa 100,000 sats.

![LNP201](assets/en/73.webp)

- **Mua kênh**: Dịch vụ cho thuê kênh Lightning cũng tồn tại để có được thanh khoản đến, như [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) hoặc [Lightning Labs Pool](https://lightning.engineering/pool/). Ví dụ, Alice có thể mua một kênh một triệu satoshis về phía nút của mình để có thể nhận thanh toán.

![LNP201](assets/en/74.webp)

Cuối cùng, đối với các bộ định tuyến, mục tiêu là tối đa hóa số lượng thanh toán được xử lý và phí thu được, họ phải:

- Mở các kênh có nguồn vốn dồi dào với các nút chiến lược.
- Điều chỉnh định kỳ sự phân bổ của quỹ trong các kênh theo nhu cầu của mạng.

### Dịch vụ Loop Out

Dịch vụ [Loop Out](https://lightning.engineering/loop/), được cung cấp bởi Lightning Labs, cho phép di chuyển thanh khoản sang phía đối diện của kênh trong khi thu hồi quỹ trên blockchain Bitcoin. Ví dụ, Alice gửi 1 triệu satoshis qua Lightning đến một nút loop, sau đó nút này trả lại số tiền đó cho cô ấy bằng bitcoin trên chuỗi. Điều này cân bằng kênh của cô ấy với 1 triệu satoshis ở mỗi bên, tối ưu hóa khả năng nhận thanh toán của cô ấy.

![LNP201](assets/en/75.webp)

Do đó, dịch vụ này cho phép tăng thanh khoản đến trong khi thu hồi bitcoin của mình trên chuỗi, giúp giới hạn việc giam cầm tiền mặt cần thiết để chấp nhận thanh toán bằng Lightning.

**Bạn nên rút ra điều gì từ chương này?**

- Để gửi thanh toán trên Lightning, bạn phải có đủ thanh khoản ở phía của bạn trong các kênh của mình. Để tăng khả năng gửi này, chỉ cần mở kênh mới.
- Để nhận thanh toán, bạn cần có thanh khoản ở phía đối diện trong các kênh của mình. Tăng khả năng nhận này phức tạp hơn, vì nó đòi hỏi người khác mở kênh về phía bạn, hoặc thực hiện các khoản thanh toán (giả mạo hoặc thực sự) để di chuyển thanh khoản sang phía bên kia.
- Duy trì thanh khoản ở nơi mong muốn có thể còn khó khăn hơn tùy thuộc vào việc sử dụng các kênh. Đó là lý do tại sao các công cụ và dịch vụ tồn tại để giúp cân bằng các kênh theo ý muốn.

Trong chương tiếp theo, tôi đề xuất xem lại các khái niệm quan trọng nhất của khóa đào tạo này.

# Đi Sâu Hơn

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Kết Luận Đào Tạo

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![kết luận](https://youtu.be/MaWpD0rbkVo)
Trong chương cuối cùng này, đánh dấu sự kết thúc của khóa học LNP201, tôi đề xuất ôn lại những khái niệm quan trọng mà chúng ta đã cùng nhau tìm hiểu.
Mục tiêu của khóa học này là cung cấp cho bạn một hiểu biết toàn diện và kỹ thuật về Lightning Network. Chúng ta đã khám phá cách mà Lightning Network dựa vào blockchain Bitcoin để thực hiện các giao dịch ngoại tuyến, trong khi vẫn giữ được những đặc điểm cơ bản của Bitcoin, đặc biệt là không cần phải tin tưởng các nút khác.

### Các Kênh Thanh Toán

Trong các chương đầu, chúng ta đã khám phá cách hai bên, bằng cách mở một kênh thanh toán, có thể thực hiện giao dịch ngoài blockchain Bitcoin. Dưới đây là các bước đã được trình bày:

1. **Mở Kênh**: Việc tạo kênh được thực hiện thông qua một giao dịch Bitcoin khóa số tiền trong một địa chỉ chữ ký đa 2/2. Khoản tiền gửi này đại diện cho kênh Lightning trên blockchain.

![LNP201](assets/en/76.webp) 2. **Giao Dịch Trong Kênh**: Trong kênh này, sau đó có thể thực hiện nhiều giao dịch mà không cần phải công bố chúng trên blockchain. Mỗi giao dịch Lightning tạo ra một trạng thái mới của kênh được phản ánh trong một giao dịch cam kết.
![LNP201](assets/en/77.webp)

3. **Bảo Đảm và Đóng Kênh**: Các bên tham gia cam kết với trạng thái mới của kênh bằng cách trao đổi khóa thu hồi để bảo vệ số tiền và ngăn chặn gian lận. Cả hai bên có thể đóng kênh một cách hợp tác bằng cách thực hiện một giao dịch mới trên blockchain Bitcoin, hoặc như một biện pháp cuối cùng thông qua một việc đóng ép buộc. Phương án này, mặc dù kém hiệu quả hơn vì mất nhiều thời gian hơn và đôi khi được đánh giá thấp về phí, vẫn cho phép khôi phục lại số tiền. Trong trường hợp gian lận, nạn nhân có thể trừng phạt kẻ gian lận bằng cách thu hồi tất cả số tiền từ kênh trên blockchain.

![LNP201](assets/en/78.webp)

### Mạng Lưới Các Kênh

Sau khi nghiên cứu về các kênh độc lập, chúng ta đã mở rộng phân tích của mình ra mạng lưới các kênh:

- **Định Tuyến**: Khi hai bên không được kết nối trực tiếp bởi một kênh, mạng lưới cho phép định tuyến qua các nút trung gian. Các khoản thanh toán sau đó chuyển từ một nút này sang nút khác.

![LNP201](assets/en/79.webp)

- **HTLCs**: Các khoản thanh toán chuyển qua các nút trung gian được bảo đảm bởi "_Hợp Đồng Khóa Thời Gian Băm_" (HTLC), cho phép khóa số tiền cho đến khi thanh toán được hoàn thành từ đầu đến cuối.

![LNP201](assets/en/80.webp)

- **Định Tuyến Hành Tinh**: Để đảm bảo tính bảo mật của khoản thanh toán, định tuyến hành tinh che giấu điểm đến cuối cùng khỏi các nút trung gian. Nút gửi do đó phải tính toán toàn bộ lộ trình, nhưng do thiếu thông tin hoàn chỉnh về tính thanh khoản của các kênh, nó tiến hành thông qua các lần thử liên tiếp để định tuyến khoản thanh toán.

![LNP201](assets/en/81.webp)

### Quản Lý Tính Thanh Khoản

Chúng ta đã thấy rằng quản lý tính thanh khoản là một thách thức trên Lightning để đảm bảo dòng chảy mượt mà của các khoản thanh toán. Gửi thanh toán tương đối đơn giản: chỉ cần mở một kênh. Tuy nhiên, việc nhận thanh toán đòi hỏi phải có tính thanh khoản ở phía đối diện của các kênh của mình. Dưới đây là một số chiến lược đã được thảo luận:

- **Thu Hút Các Kênh**: Bằng cách khuyến khích các nút khác mở kênh về phía mình, người dùng nhận được tính thanh khoản đến.

- **Di Chuyển Tính Thanh Khoản**: Bằng cách gửi thanh toán đến các kênh khác, tính thanh khoản di chuyển sang phía đối diện.

![LNP201](assets/en/82.webp)

- **Sử Dụng Các Dịch Vụ như Loop và Pool**: Những dịch vụ này cho phép cân bằng lại hoặc mua các kênh với tính thanh khoản ở phía đối diện.
  ![LNP201](assets/en/83.webp)
- **Mở Kênh Hợp Tác**: Cũng có các nền tảng có sẵn để kết nối thực hiện các mở kênh tam giác và có tính thanh khoản đến.

![LNP201](assets/en/84.webp)

# Kết luận

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Đánh giá khóa học này

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Bài kiểm tra cuối cùng

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Kết luận

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
Chúc mừng! 🎉

Bạn đã hoàn thành khóa đào tạo LNP 201 - Giới thiệu về Lightning Network!

Bạn có thể tự hào về bản thân, vì đây không phải là một chủ đề dễ dàng.

Rất ít người đi sâu vào hang thỏ Bitcoin đến như vậy.

Xin cảm ơn **Fanis Michalakis** rất nhiều vì đã cung cấp khóa học miễn phí tuyệt vời này về cách hoạt động kỹ thuật của Lightning Network.

Hãy theo dõi anh ấy trên [Twitter](https://x.com/FanisMichalakis), trên [blog của anh ấy](https://fanismichalakis.fr/) hoặc thông qua công việc của anh ấy tại [LN Markets](https://lnmarkets.com/).

Giờ đây, khi bạn đã thành thạo Lightning Network, tôi mời bạn khám phá các khóa học miễn phí khác của chúng tôi trên Plan ₿ Network để đào sâu hiểu biết về các khía cạnh khác của phát minh của Satoshi Nakamoto:

#### Hiểu cách hoạt động của ví Bitcoin với

https://planb.network/courses/cyp201

#### Khám phá lịch sử nguồn gốc của Bitcoin với

https://planb.network/courses/his201

#### Cấu hình máy chủ thanh toán BTC với

https://planb.network/courses/btc305

#### Nắm vững các nguyên tắc quyền riêng tư trong Bitcoin

https://planb.network/courses/btc204

#### Khám phá những điều cơ bản về khai thác với

https://planb.network/courses/min201

#### Học cách tạo cộng đồng Bitcoin của bạn với

https://planb.network/courses/btc302

