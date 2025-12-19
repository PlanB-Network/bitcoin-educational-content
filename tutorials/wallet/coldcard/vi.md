---
name: COLDCARD Mk

description: Tạo, sao lưu và sử dụng khóa riêng Bitcoin với thiết bị Coldcard và Bitcoin Core
---

![cover](assets/cover.webp)

Tạo, sao lưu và sử dụng khóa riêng Bitcoin với thiết bị Coldcard và Bitcoin Core

## Hướng dẫn đầy đủ về cách tạo khóa riêng bằng Coldcard và sử dụng nó qua giao diện của node Bitcoin Core của bạn!

Tại cốt lõi của việc sử dụng mạng Bitcoin nằm ở khái niệm về mật mã bất đối xứng: một cặp khóa - một khóa riêng và một khóa công khai - mã hóa và giải mã dữ liệu, một khái niệm đảm bảo tính bảo mật của giao tiếp.

Trong trường hợp của Bitcoin, bằng cách tạo ra một cặp khóa riêng và công khai như vậy, chúng ta có thể lưu trữ bitcoin (UTXO hoặc Unspent Transaction Output) và ký các giao dịch để chi tiêu chúng.

Ngày nay, có nhiều công cụ có sẵn để hỗ trợ việc tạo ngẫu nhiên khóa riêng và sao lưu nó dưới dạng văn bản sử dụng BIP 39 - một tiêu chuẩn xác định cách ví liên kết cụm từ ghi nhớ (cụm từ hạt giống) với khóa mã hóa. Thông thường, cụm từ ghi nhớ bao gồm 12 hoặc 24 từ, cần phải được sao lưu một cách an toàn để có thể khôi phục ví và bitcoin của bạn sau này.

Trong bài viết này, chúng ta sẽ học cách tạo khóa riêng bằng cách sử dụng Coldcard Mk4, một trong những thiết bị được sử dụng rộng rãi và an toàn nhất trong thế giới Bitcoin, sử dụng phương pháp lắc xúc xắc để đảm bảo entropy tối đa, và cách sử dụng nó với Bitcoin Core theo cách không kết nối mạng!

> 🧰| Hãy chuẩn bị những công cụ sau để theo dõi hướng dẫn:
>
> - Thiết bị Coldcard (Mk3 hoặc Mk4)
> - Thẻ MicroSD (4GB là đủ)
> - Cáp USB chỉ dùng để cấp nguồn (mini-usb cho Mk3, usb-c cho Mk4)
> - Một hoặc nhiều xúc xắc chất lượng

## Tạo một cụm từ ghi nhớ mới với Coldcard

Chúng ta sẽ bắt đầu quá trình tạo khóa riêng từ đầu, giả sử là một Coldcard mới được mở khỏi hộp mà đã được thiết lập PIN (theo các bước trên Coldcard khi khởi tạo thiết bị).

> 🚨 | Để đặt lại khóa riêng của một Coldcard đã được cấu hình, hãy thực hiện các bước sau:
> Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed> ✓
> _Chú ý_: Coldcard của bạn sẽ quên khóa riêng sau các bước này. Hãy chắc chắn bạn đã sao lưu cụm từ ghi nhớ của mình một cách đúng đắn nếu bạn muốn có thể khôi phục nó sau này.

## Các bước cần thực hiện:

Kết nối với Coldcard bằng PIN > New Seed Words > 24 Word Dice Roll

Thực hiện 100 lần lắc xúc xắc, ghi lại kết quả thu được từ 1 đến 6 trên Coldcard sau mỗi lần lắc. Bằng cách thực hành phương pháp này, bạn tạo ra 256 byte entropy, do đó ưu tiên tạo ra một khóa riêng hoàn toàn ngẫu nhiên. Coinkite cũng cung cấp tài liệu cần thiết cho việc xác minh độc lập hệ thống tạo entropy của họ.

![Visual Cold Card Screenshot](assets/guide-agora/1.webp)

Một khi hoàn thành 100 lần lắc xúc xắc, nhấn ✓ và sau đó ghi lại 24 từ thu được theo thứ tự. Kiểm tra hai lần và nhấn ✓. Cuối cùng, tất cả những gì còn lại là hoàn thành bài kiểm tra xác minh của 24 từ trên Coldcard, và voila, khóa riêng mới của bạn đã được tạo!

Tiếp theo, chọn có kích hoạt chức năng NFC (Mk4) và USB hay không bằng cách theo dõi các bước hiển thị. Một khi ở trong menu chính, đã đến lúc cập nhật firmware của thiết bị. Đi đến Advanced/Tools > Upgrade Firmware > Show Version, và kiểm tra trang web chính thức để xác nhận và tải xuống phiên bản mới nhất có sẵn. Nên cập nhật Coldcard để được hưởng mức độ bảo mật tối đa.
Trước khi tiếp tục, bạn nên ghi lại Dấu Vân Tay Khóa Chính (XFP) liên kết với khóa riêng. Dữ liệu này cho phép xác minh nhanh chóng nếu bạn đang trong ví đúng trong trường hợp khôi phục, chẳng hạn. Đi tới Advanced/Tools > View Identity > Master Key Fingerprint (XFP) và ghi lại chuỗi tám ký tự chữ và số nhận được. XFP có thể được ghi chú tại cùng một nơi với cụm từ ghi nhớ, nó không phải là dữ liệu nhạy cảm.
> 💡 Đề xuất rằng bạn nên thử nghiệm sao lưu cụm từ ghi nhớ của mình trên một phần mềm khác. Để làm điều này một cách an toàn, hãy tham khảo bài viết của chúng tôi Kiểm tra sao lưu ví Bitcoin với Tails trong ít hơn 5 phút.

## Phần thưởng Bảo Mật: "Cụm Từ Bí Mật" (tùy chọn)

Một cụm từ bí mật (passphrase) là một yếu tố tuyệt vời để thêm vào cấu hình ví nhằm tăng cường lớp bảo vệ cho bitcoin của bạn. Cụm từ bí mật hoạt động như một loại từ thứ 25 đối với cụm từ ghi nhớ. Một khi đã thêm, một ví hoàn toàn mới được tạo ra cùng với khóa riêng và cụm từ ghi nhớ liên quan. Không cần thiết phải ghi lại cụm từ ghi nhớ mới, vì ví này có thể được truy cập bằng cách kết hợp cụm từ ghi nhớ ban đầu với cụm từ bí mật đã chọn.

Mục tiêu là ghi chú cụm từ bí mật riêng biệt khỏi cụm từ ghi nhớ vì kẻ tấn công có quyền truy cập vào cả hai mục sẽ có quyền truy cập vào quỹ. Ngược lại, kẻ tấn công chỉ có quyền truy cập vào một trong những mục này sẽ không có quyền truy cập vào quỹ, và đây chính là lợi thế cụ thể tối ưu hóa mức độ bảo mật của cấu hình ví.

![Thêm một cụm từ bí mật dẫn đến một ví hoàn toàn khác](assets/guide-agora/2.webp)

## Các bước để thêm cụm từ bí mật với Coldcard:

Passphrase > Add Words (được đề xuất) > Apply. Thiết bị sẽ hiển thị XFP của ví mới được tạo với cụm từ bí mật, điều này nên được ghi chú lại cùng với cụm từ bí mật vì những lý do đã đề cập trước đó.

> 💡 Tài nguyên bổ sung liên quan đến cụm từ bí mật:

    https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af
    https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/
    https://armantheparman.com/passphrase/

## Xuất ví sang Bitcoin Core

Ví giờ đây đã sẵn sàng để được xuất sang phần mềm để tương tác với mạng Bitcoin. Trong hướng dẫn này, chúng tôi sẽ sử dụng Bitcoin Core (v24.1).

Tham khảo hướng dẫn cài đặt và cấu hình của chúng tôi cho Bitcoin Core:

> Chạy node của riêng bạn với Bitcoin Core - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Cấu hình Tor cho một node Bitcoin Core - https://agora256.com/configuration-tor-bitcoin-core/

Đầu tiên, chèn một thẻ micro SD vào Coldcard, sau đó xuất ví cho Bitcoin Core bằng cách thực hiện các bước sau: Advanced/Tools > Export Wallet > Bitcoin Core. Hai tệp sẽ được ghi vào thẻ micro SD: bitcoin-core.sig & bitcoin-core.txt. Chèn thẻ micro SD vào máy tính nơi Bitcoin Core được cài đặt, và mở tệp .txt. Bạn sẽ thấy dòng "For wallet with master key fingerprint." Xác minh rằng XFP tám ký tự khớp với cái bạn đã ghi khi tạo khóa riêng của mình.
Trước khi thực hiện theo hướng dẫn trong tệp, hãy bắt đầu bằng cách chuẩn bị ví trong giao diện Bitcoin Core bằng cách thực hiện các bước sau: đi tới tab File > Tạo ví. Chọn một tên cho ví của bạn (có thể thay thế thuật ngữ "porte-monnaie" trong Core) và kiểm tra các tùy chọn Disable private keys, Create an empty wallet, và Wallet descriptors như hình dưới đây. Sau đó, nhấn nút Create.
![tạo ví](assets/guide-agora/3.webp)

Một khi ví đã được tạo trong Bitcoin Core, đi tới tab Window > Console và đảm bảo rằng ví được chọn ở đầu trang hiển thị tên của ví bạn đã tạo.

Bây giờ, trong tệp .txt được tạo bởi Coldcard trước đó, sao chép dòng bắt đầu với importdescriptors, sau đó dán nó vào console của Bitcoin Core. Một phản hồi bao gồm dòng "success": true nên được trả về.

![cửa sổ nút](assets/guide-agora/4.webp)

Nếu phản hồi chứa "message": "Ranged descriptors should not have a label", xóa mục nhập "label": "Coldcard xxxx0000" trong dòng được sao chép từ tệp .txt, sau đó dán lại dòng đầy đủ vào console của Bitcoin Core.

Trợ giúp: [https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md)

## Xác nhận việc nhập ví vào Bitcoin Core

Để đảm bảo rằng thao tác đã thành công, cần phải xác nhận rằng ví mong muốn đã được nhập vào Bitcoin Core. Một phương pháp đơn giản để xác nhận điều này là kiểm tra xem các địa chỉ được tạo trong Coldcard có khớp với các địa chỉ được tạo trong Bitcoin Core hay không.

Bitcoin Core: Receive > Tạo một địa chỉ nhận mới
Coldcard: Address Explorer > Chọn địa chỉ bắt đầu với bc1q. Địa chỉ 'bc1q' của Coldcard nên khớp với địa chỉ hiển thị trong Bitcoin Core.
Nhận và gửi giao dịch trong chế độ 'air-gapped'

Việc nhận một giao dịch cực kỳ đơn giản; chỉ cần nhấn Receive, gắn nhãn cho giao dịch (tùy chọn nhưng được khuyến nghị), và Tạo một địa chỉ nhận mới. Sau đó, tất cả những gì còn lại là chia sẻ địa chỉ với người gửi.

Bây giờ, yếu tố then chốt của cài đặt Coldcard + Bitcoin Core này là gửi giao dịch mà không cần Coldcard và khóa riêng của nó được kết nối với internet, một phương pháp được gọi là air-gapped sử dụng chức năng TBSP (PSBT - Partially Signed Bitcoin Transactions) của Bitcoin.
Cơ bản, chúng ta sử dụng giao diện Bitcoin Core để xây dựng một giao dịch, mà sau đó chúng ta sẽ xuất qua thẻ micro SD đến Coldcard để ký, và sau đó trả lại tệp giao dịch đã ký cho Bitcoin Core và phát sóng giao dịch lên mạng. Chúng ta phải làm theo cách này vì ví được nhập vào Bitcoin Core không có khóa riêng, chỉ có khóa công khai (cho phép chúng ta tạo địa chỉ nhận của mình), vì vậy chúng ta không thể ký một giao dịch trực tiếp trong phần mềm để chi tiêu bitcoin của mình.

Trước khi tiếp tục, hãy đảm bảo các tùy chọn sau được kích hoạt trong Settings > Wallet:

> - Enable coin control features
> - Spend unconfirmed coins (Tùy chọn)
> - Enable TBPS checks

![tùy chọn](assets/guide-agora/5.webp)

### Các bước để gửi trong chế độ air-gapped:
Gửi > Đầu vào > chọn utxo mong muốn, sau đó nhập địa chỉ của người nhận vào mục Thanh toán cho. Phí giao dịch: Chọn... > Tùy chỉnh > Nhập phí giao dịch (Bitcoin Core tính bằng sats/kilobyte thay vì sat/byte như hầu hết các giải pháp ví thay thế. Vậy 4000 sats/kilobyte = 4 sats/byte). Tạo một giao dịch chưa ký > lưu tệp vào thẻ micro SD và chèn nó vào Coldcard.
Trong Coldcard, nhấn Sẵn sàng để ký, xác minh chi tiết giao dịch, sau đó nhấn ✓ và chèn thẻ micro SD trở lại máy tính sau khi các tệp đã ký được tạo.

Quay lại Bitcoin Core, đi tới tab Tệp > Tải TBSP từ tệp, và nhập tệp giao dịch đã ký .psbt. Hộp Thao tác PSBT sẽ xuất hiện trên màn hình, xác nhận rằng giao dịch đã được ký hoàn toàn và sẵn sàng được phát sóng. Tất cả những gì còn lại là nhấn Phát sóng giao dịch.

![Thao tác PSBT](assets/guide-agora/6.webp)

### Kết luận

Sự kết hợp của thiết bị Coldcard với Bitcoin Core, nơi bạn chạy node của riêng mình, là mạnh mẽ. Thêm vào đó là một khóa riêng được tạo ra với 100 lần lắc xúc xắc và một cụm từ bí mật, và cấu hình ví của bạn trở thành một pháo đài tinh vi và vững chắc.

Hãy liên hệ với chúng tôi để chia sẻ ý kiến và câu hỏi của bạn! Mục tiêu của chúng tôi là chia sẻ kiến thức và tăng cường hiểu biết hàng ngày.