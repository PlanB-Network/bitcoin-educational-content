---
name: Khai Thác Dưới Đại Dương

description: Giới thiệu về Khai Thác Dưới Đại Dương
---

![signup](assets/cover.webp)

**Tháng 5 năm 2024**

Khai Thác Dưới Đại Dương là một hồ bơi khai thác khá độc đáo. Tại đây, không yêu cầu tài khoản, địa chỉ email, mật khẩu. Giống như Bitcoin, mọi thứ đều minh bạch, ẩn danh và người đóng góp có thể chọn từ bốn mẫu khối khác nhau.

### Hệ Thống Bồi Thường

Hệ thống bồi thường của Ocean được gọi là TIDES, "Chỉ Số Minh Bạch của Cổ Phần Mở Rộng Độc Lập". Hệ thống này ghi lại công việc do các thợ mỏ cung cấp, được biết đến là "cổ phần". Hồ bơi tính toán phần trăm "cổ phần" cho mỗi người đóng góp, sau đó thêm địa chỉ Bitcoin của họ vào mẫu khối của hồ bơi là người hưởng lợi từ phần trăm này của phần thưởng khối.

Mẫu khối được cập nhật khoảng mỗi 10 giây để tính toán các giao dịch mới lợi nhuận nhất và để thay đổi phân phối của phần thưởng khối nếu cần thiết.

![signup](assets/rem.webp)

Việc máy của bạn có kết nối hay không vào thời điểm hồ bơi khai thác một khối mới không quan trọng. Công việc đã nộp trước đó được giữ lại cho tám khối tiếp theo được hồ bơi tìm thấy.

Giữ công việc cho tám khối thay vì đặt lại bộ đếm về không với mỗi khối mới được khai thác có nghĩa là bạn chỉ được bồi thường 100% một khi hồ bơi đã tìm thấy tám khối sau khi bạn bắt đầu đóng góp. Điều này cũng có nghĩa là bạn sẽ tiếp tục được bồi thường cho tám khối nếu bạn ngừng đóng góp vào hồ bơi.

Cơ chế này làm mịn sự bồi thường và ngăn chặn "nhảy hồ", tức là việc chuyển đổi hồ bơi thường xuyên tùy thuộc vào hồ bơi nào có khả năng tìm thấy khối tiếp theo nhất.

### Rút Tiền

Hoạt động của Khai Thác Dưới Đại Dương cho phép người đóng góp thu hồi "bitcoin sạch", tức là bitcoin được phát hành trực tiếp từ phần thưởng khối.

Khác với đa số các hồ bơi khác, Ocean không nhận bitcoin mới khai thác; địa chỉ của người đóng góp được tích hợp trực tiếp vào mẫu khối.

Hiện tại, số lượng tối thiểu để thực sự hưởng lợi từ bitcoin sạch là 1,048,576 sats. Với mỗi khối được hồ bơi khai thác, phần "cổ phần" của bạn phải đủ điều kiện bạn nhận được hơn 1,048,576 sats để chúng được trả trực tiếp cho bạn từ phần thưởng khối.
Nếu không, sats của bạn sẽ được Ocean giữ lại cho đến khi tổng phần thưởng của bạn vượt qua số lượng này.

Tất cả bitcoin tạm thời được giữ bởi Ocean đều ở địa chỉ này: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, mọi thứ đều có thể kiểm chứng trên TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
Cũng có thể rút sats của bạn qua Lightning sử dụng BOLT12. Chúng ta sẽ xem cách thiết lập điều này.

### Phí Hồ Bơi

Phí dao động từ 0% đến 2% tùy thuộc vào mẫu khối được chọn.

## Sự Minh Bạch của Ocean

### Dữ Liệu Người Đóng Góp

![signup](assets/1.webp)

Tất cả thông tin về hồ bơi đều minh bạch, bao gồm cả dữ liệu người dùng. Để hiểu điểm này, hãy xem một ví dụ:

[Trên bảng điều khiển Ocean](https://ocean.xyz/dashboard), bạn có nhiều thông tin như hashrate trong sáu tháng qua, số lượng người tham gia hồ bơi, tổng số bitcoin đã khai thác, v.v.

Chúng ta sẽ tập trung vào mục "Người Đóng Góp". Bạn có thể thấy danh sách tất cả người đóng góp với hashrate trung bình trong ba giờ qua cũng như phần trăm **"cổ phần"** và **"hash"** so với phần còn lại của hồ bơi.
**"Phần Trăm Cổ Phần"** là tỷ lệ công việc được cung cấp bởi người đóng góp trong cửa sổ của tám khối cuối cùng so với phần còn lại của nhóm.
**"Phần Trăm Hash"** là tỷ lệ hashrate trung bình được cung cấp bởi người đóng góp trong ba giờ cuối cùng so với phần còn lại của nhóm.

![signup](assets/2.webp)

Bạn sẽ nhận thấy rằng "Người Đóng Góp" được xác định bởi một địa chỉ Bitcoin. Bạn có thể nhấp vào bất kỳ địa chỉ nào trong số này để biết thêm chi tiết.

Nếu chúng ta lấy cái đầu tiên, cái có hashrate cao nhất [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), bạn có thể thấy tất cả các chi tiết về người dùng này: hashrate, số lượng bitcoin đã khai thác, với khối nào, và thậm chí là chi tiết của từng máy của họ (ASICs). Tuy nhiên, họ vẫn giữ ẩn danh, như trên Bitcoin.

### Mẫu Khối

Ở góc trên bên trái trên bảng điều khiển, bạn có "Khối Tiếp Theo". Trên trang này, có bốn mẫu khối khác nhau. Ocean cho phép mỗi người đóng góp chọn mẫu khối mà họ muốn hỗ trợ. Điều này không có ảnh hưởng trực tiếp đến tiền thưởng của bạn. Khi nhóm khai thác một khối, tất cả người đóng góp đều được thưởng bất kể họ đã chọn mẫu nào. Điều này chỉ đơn giản cho phép mọi người "bầu chọn" cho mẫu khối phù hợp với họ.

![signup](assets/3.webp)

**CORE:** Phí 2%, đây là mẫu Bitcoin Core cổ điển không có bộ lọc, như được viết trên trang của họ "Bao gồm giao dịch và phần lớn spam"

**CORE+ANTISPAM:** Phí 0%, Bitcoin Core với bộ lọc chống lại một số giao dịch như Ordinals "Bao gồm giao dịch và hạn chế spam"

**OCEAN:** Phí 0%, Bitcoin Knot "Chỉ bao gồm giao dịch và dữ liệu nhỏ hợp lý"

**DATA-FREE:** Phí 0%, Bitcoin Knot "Chỉ bao gồm giao dịch mà không có bất kỳ dữ liệu tùy ý nào"

### Sự Khác Biệt giữa Bitcoin Core và Bitcoin Knot
Bitcoin Core là phần mềm cho phép khoảng 99% các nút Bitcoin trên toàn thế giới hoạt động. Bitcoin là một giao thức, có nghĩa là, giống như Internet, nơi có nhiều trình duyệt khác nhau, có thể có nhiều chương trình phần mềm khác nhau cùng tồn tại trên cùng một TimeChain. Tuy nhiên, vì lo ngại về tính tương thích và để hạn chế rủi ro của lỗi sẽ để lại dấu vết không thể xóa nhòa trên TimeChain, hầu hết các nhà phát triển Bitcoin đều làm việc trên Bitcoin Core. Bitcoin Knots là một nhánh của Bitcoin Core, có nghĩa là nó chia sẻ phần lớn mã của họ, giảm thiểu rủi ro của lỗi. Nhánh này được tạo ra bởi Luke Dashjr, người muốn áp dụng các quy tắc hạn chế hơn so với Bitcoin Core mà không tạo ra một hard fork. Bây giờ, Bitcoin Core và Bitcoin Knots đồng tồn tại nhờ sự đồng thuận Nakamoto.

## Thêm Một Worker

Để thêm một worker, bắt đầu bằng cách chọn mẫu khối của bạn. Lựa chọn này sẽ xác định URL nhóm để nhập vào máy đào của bạn (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Tiếp theo, cho trường người dùng, nhập một địa chỉ Bitcoin bạn sở hữu. Dưới đây là danh sách các loại địa chỉ tương thích:
- **P2PKH** (Loại địa chỉ gốc. Bắt đầu bằng “1”)
- **P2SH** (Chữ ký đa dạng hoặc P2SH-Segwit. Bắt đầu bằng “3”)
- **Bech32** (Segwit. Bắt đầu bằng “bc”.)
- **Bech32m** (Taproot. Bắt đầu bằng “bc”. Dài hơn Bech32.)

Nếu bạn có nhiều máy đào, bạn có thể nhập cùng một địa chỉ cho tất cả chúng để tổng hợp tốc độ hash của chúng và hiển thị như một máy đào duy nhất. Bạn cũng có thể phân biệt chúng bằng cách thêm tên riêng biệt cho mỗi máy. Để làm điều này, chỉ cần thêm “.workername” sau địa chỉ Bitcoin.

Cuối cùng, cho trường mật khẩu, sử dụng `x`.

**Ví dụ:**
Nếu bạn chọn mẫu **OCEAN**, địa chỉ Bitcoin của bạn là `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` và bạn muốn đặt tên cho máy đào của mình là “Brrrr”, sau đó bạn sẽ cần nhập thông tin sau vào giao diện máy đào của mình:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **USER**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **PASSWORD**: `x`

Vài phút sau khi bắt đầu đào, bạn sẽ có thể xem dữ liệu của mình trên trang Ocean bằng cách tìm kiếm địa chỉ của mình.

### Tổng Quan Bảng Điều Khiển
- **Cổ Phần trong Cửa Sổ Phần Thưởng**: Dữ liệu này chỉ số lượng cổ phần, công việc bạn đã gửi cho bể trong cửa sổ của 8 khối cuối cùng được bể đào.
- **Ước Lượng Phần Thưởng trong Cửa Sổ**: Ước lượng số sats bạn sẽ kiếm được với công việc đã làm. Điều này không tính đến phí giao dịch, chỉ tính coinbase, những bitcoin mới được phát hành bởi mạng lưới.
- **Ước Lượng Thu Nhập Khối Tiếp Theo**: Ước lượng số sats kiếm được nếu một khối được đào ngay bây giờ. Lưu ý, nếu giá trị này ít hơn 1,048,576 sats, bạn sẽ không nhận được sats trực tiếp vào địa chỉ của mình. Chúng sẽ được gửi đến địa chỉ của Ocean cho đến khi thu nhập của bạn vượt qua ngưỡng này.

Dưới đây, bạn có một biểu đồ hiển thị lịch sử tốc độ hash của mình lên đến 6 tháng.

![signup](assets/4.webp)

Tại đây, bạn có tốc độ hash trung bình của mình qua các khoảng thời gian khác nhau, từ 60 giây đến 24 giờ, cũng như lịch sử các khối được bể đào mà bạn đã đóng góp và được thưởng.

![signup](assets/5.webp)

Bạn có tùy chọn xuất một tệp CSV của lịch sử này với nút **Download CSV**.

![signup](assets/6.webp)

Trong phần tiếp theo, bạn có danh sách tất cả các máy đào bạn đã kết nối với bể bằng địa chỉ này. Bạn có, tất nhiên, tốc độ hash cá nhân của họ, nhưng cũng số sats mà họ đã nhận được riêng lẻ cho công việc của họ.

![signup](assets/7.webp)

Bạn có thể nhấp vào **Nickname** của bất kỳ máy đào nào. Sau đó, bạn sẽ có tất cả thông tin chúng tôi vừa xem, nhưng cụ thể cho máy đào đó.

Và ở cuối trang, một số thông tin bổ sung nơi bạn có thể xem lịch sử thanh toán trên địa chỉ của mình, các sats bạn đã đào nhưng chưa được thanh toán, và tổng số sats bạn đã đào.

![signup](assets/8.webp)

Tại đây, bạn có thể thấy rằng trong hộp **Ước Lượng Thời Gian Đến Khoản Thanh Toán Tối Thiểu**, nó được viết là Lightning vì chúng tôi đã thiết lập một đề nghị BOLT12.

### Thiết Lập Rút Tiền Qua Lightning
Như bạn đã hiểu, Ocean hướng tới việc tối đa hóa sự minh bạch và giảm thiểu việc giữ hộ (giữ sats thay mặt bạn).
Chính vì vậy, đối với việc rút tiền qua Lightning, việc sử dụng **BOLT12 offers** là cần thiết. Đây là một cách mới để thực hiện thanh toán trên mạng lưới Lightning, bắt đầu xuất hiện vào năm 2024 và cho phép một số điều:
- Đây là một liên kết thanh toán có thể sử dụng lại, cho phép thanh toán tự động và, không giống như địa chỉ Lightning, BOLT12 không giữ hộ.
- Đây cũng là một phương thức thanh toán cung cấp bằng chứng rằng việc thanh toán đã được thực hiện, điều này không đúng với LNURLs.
- Rất quan trọng, nó có thể được sử dụng kết hợp với chữ ký Bitcoin để chứng minh rằng bạn vừa là người giữ địa chỉ BTC vừa là người đưa ra BOLT12 offer.
Tính đến ngày nay (Tháng 5 năm 2024), ít giải pháp tồn tại để sử dụng phương pháp này. Trong ví dụ này, chúng ta sẽ sử dụng máy chủ Start9 với Core Lightning. Khi các công cụ khác, chẳng hạn như Phoenix Wallet, đã tích hợp BOLT12 offers, hướng dẫn này vẫn áp dụng. Đảm bảo bạn có các kênh mở với dòng tiền vào, nếu không thanh toán sẽ không hoạt động.

Bắt đầu bằng cách truy cập bảng điều khiển của bạn trên trang Ocean bằng cách nhập địa chỉ BTC của bạn, sau đó nhấp vào tab **Configuration**.

![signup](assets/9.webp)

Chúng ta sẽ sao chép văn bản **Description**, ở đây:
`OCEAN Payouts for bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Bây giờ, hãy chuyển đến giao diện Core Lightning trên máy chủ Start9 của bạn (hoặc bất kỳ ví nào có khả năng cung cấp BOLT12 offer).

![signup](assets/10.webp)

Nhấp vào **Receive**.

Kiểm tra **Offer**, sau đó dán văn bản đã sao chép trước đó vào trường **Description** và để trống trường **Amount**.

![signup](assets/11.webp)

Nhấp vào **Generate Offer**.

![signup](assets/12.webp)

Bạn đã tạo ra một liên kết thanh toán có thể sử dụng lại và vĩnh viễn không yêu cầu máy chủ trung tâm như trường hợp với địa chỉ Lightning. Sao chép liên kết và sau đó quay trở lại trang Ocean.

Trong trường **Lightning BOLT12 Offer**, dán liên kết thanh toán và để trường **Block Height** ở giá trị mặc định. Nhấp vào **GENERATE**.

![signup](assets/13.webp)

Để Ocean đảm bảo rằng liên kết thanh toán này thực sự thuộc về bạn mà không sử dụng hệ thống tài khoản, bạn sẽ cần phải ký vào thông điệp vừa được tạo ra bằng khóa riêng tư tương ứng với địa chỉ Bitcoin bạn đang sử dụng. Nhiều giải pháp tồn tại để ký một thông điệp bằng khóa riêng tư của bạn. Trong hướng dẫn này, chúng ta sẽ lấy ví dụ của BlueWallet, nhưng phương pháp là giống nhau cho tất cả các ví.

![signup](assets/14.webp)

Giả sử khóa riêng tư của bạn nằm trong BlueWallet (bạn có thể làm tương tự với một ví cứng), nhấp vào ví liên quan.

![signup](assets/15.webp)

Sau đó vào **…** ở góc trên bên phải.

![signup](assets/15bis.webp)

Và **Sign/Verify Message**.

![signup](assets/16.webp)

Trong cửa sổ này, bạn có ba trường: **Address**, **Signature**, và **Message**.

Trong trường **Address**, nhập địa chỉ Bitcoin của bạn. Nếu quay lại ví dụ của chúng ta, đó là địa chỉ: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Để trống trường **Signature**.
Và dán thông điệp được tạo vào trường **Message** trên trang của Ocean: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Nhấn vào **Sign**.

Điều này sẽ tạo ra một chữ ký mã hóa chứng minh bạn là chủ sở hữu của địa chỉ `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, và chữ ký này là duy nhất nhờ vào thông điệp được cung cấp bởi Ocean, được tạo từ liên kết thanh toán BOLT12.

![signup](assets/17.webp)

Sao chép chữ ký và dán nó vào trang của Ocean, sau đó nhấn vào **CONFIRM**.

![signup](assets/18.webp)

Bạn sẽ thấy một thông điệp xác nhận.

![signup](assets/19.webp)

Bây giờ, đi đến tab **My Stats**. Thông tin bổ sung được hiển thị ở phía trên với liên kết thanh toán BOLT12 mà bạn đã tạo trước đó với Core Lightning trên Start9.

![signup](assets/20.webp)