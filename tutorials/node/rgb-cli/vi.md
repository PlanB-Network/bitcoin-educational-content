---
name: RGB CLI
description: Tôi có thể tạo và trao đổi hợp đồng thông minh trên RGB như thế nào?
---
![cover](assets/cover.webp)


Trong hướng dẫn này, chúng ta sẽ cùng tìm hiểu quy trình từng bước viết hợp đồng, sử dụng công cụ dòng lệnh `rgb` do hiệp hội LNP/BP tạo ra. Mục tiêu là để hướng dẫn cách cài đặt và thao tác với CLI, biên dịch Schema, nhập Interface và Interface Implementation, và sau đó phát hành tài sản RGB. Chúng ta cũng sẽ xem xét logic cơ bản, bao gồm biên dịch và xác thực trạng thái. Sau khi hoàn thành hướng dẫn này, bạn sẽ có thể tái tạo quy trình và tạo hợp đồng RGB của riêng mình.


## Lời nhắc về giao thức RGB


RGB là một giao thức chạy trên nền tảng Bitcoin và mô phỏng chức năng hợp đồng thông minh cũng như quản lý tài sản kỹ thuật số, mà không làm quá tải hệ thống blockchain mà nó dựa trên. Không giống như các hợp đồng thông minh on-chain thông thường (như trên Ethereum chẳng hạn), RGB dựa vào hệ thống "*xác thực phía máy khách*": phần lớn dữ liệu và lịch sử trạng thái được trao đổi và lưu trữ độc quyền bởi các bên tham gia, trong khi Bitcoin blockchain chỉ lưu trữ các cam kết mã hóa nhỏ (thông qua các cơ chế như *Tapret* hoặc *Opret*). Do đó, trong giao thức RGB, Bitcoin blockchain chỉ đóng vai trò là máy chủ đóng dấu thời gian và hệ thống bảo vệ double-spending.


Hợp đồng RGB được cấu trúc giống như một cỗ máy trạng thái tiến hóa. Nó bắt đầu với một Genesis xác định trạng thái ban đầu (ví dụ: mô tả nguồn cung, mã giao dịch hoặc siêu dữ liệu khác) theo một Schema được định kiểu và biên dịch nghiêm ngặt. Sau đó, các State Transition và, nếu cần, State Extension được áp dụng để sửa đổi hoặc mở rộng trạng thái này. Mỗi thao tác, dù là chuyển giao tài sản có thể hoán đổi (RGB20) hay tạo ra tài sản độc nhất (RGB21), đều liên quan đến *Seal sử dụng một lần*. Chúng liên kết các Bitcoin và UTXO với các trạng thái off-chain và ngăn chặn việc chi tiêu kép, đồng thời đảm bảo tính bảo mật và khả năng mở rộng.


Để tìm hiểu thêm về cách thức hoạt động của giao thức RGB, tôi khuyên bạn nên tham gia khóa đào tạo toàn diện này:


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Logic nội bộ của RGB dựa trên các thư viện Rust mà bạn, với tư cách là nhà phát triển, có thể nhập vào dự án của mình để quản lý phần *Client-side Validation*. Ngoài ra, nhóm LNP/BP đang làm việc trên các liên kết cho các ngôn ngữ khác, nhưng điều này vẫn chưa được hoàn thiện. Thêm vào đó, các thực thể khác như Bitfinex đang phát triển các ngăn xếp tích hợp riêng của họ, nhưng chúng ta sẽ thảo luận về những điều này trong một hướng dẫn khác. Hiện tại, CLI `rgb` là tài liệu tham khảo chính thức, mặc dù nó vẫn còn tương đối chưa được hoàn thiện.


## Lắp đặt và giới thiệu công cụ RGB CLI


Lệnh chính được gọi đơn giản là `rgb`. Nó được thiết kế để gợi nhớ đến `git`, với một tập hợp các lệnh phụ để thao tác với hợp đồng, thực thi chúng, phát hành tài sản, v.v. Bitcoin và Wallet hiện chưa được tích hợp, nhưng sẽ được tích hợp trong phiên bản sắp tới (0.11). Phiên bản tiếp theo này sẽ cho phép người dùng tạo và quản lý wallet của họ (thông qua các mô tả) trực tiếp từ `rgb`, bao gồm cả việc tạo PSBT, khả năng tương thích với phần cứng bên ngoài (ví dụ: wallet phần cứng) để ký và khả năng tương tác với phần mềm như Sparrow. Điều này sẽ đơn giản hóa toàn bộ quy trình phát hành và chuyển giao tài sản.


### Lắp đặt qua Cargo


Chúng tôi cài đặt công cụ vào Rust bằng lệnh:


```bash
cargo install rgb-contracts --all-features
```


(Lưu ý: thư viện này có tên là `rgb-contracts`, và lệnh được cài đặt sẽ có tên là `rgb`. Nếu đã tồn tại một thư viện có tên `rgb`, có thể xảy ra xung đột, do đó mới có tên gọi như vậy.)


Quá trình cài đặt biên dịch một lượng lớn các thư viện phụ thuộc (ví dụ: phân tích cú pháp lệnh, tích hợp Electrum, quản lý bằng chứng không tiết lộ thông tin, v.v.).


Sau khi quá trình cài đặt hoàn tất, thì:


```bash
rgb
```


Chạy lệnh `rgb` (không có đối số) sẽ hiển thị danh sách các lệnh con có sẵn, chẳng hạn như `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, v.v. Bạn có thể thay đổi thư mục lưu trữ cục bộ (một thư mục chứa tất cả nhật ký, sơ đồ và triển khai), chọn mạng (testnet, mainnet) hoặc cấu hình máy chủ Electrum của bạn.


![RGB-CLI](assets/fr/01.webp)


### Tổng quan ban đầu về các chức năng điều khiển


Khi bạn chạy lệnh sau, bạn sẽ thấy rằng giao diện `RGB20` đã được tích hợp sẵn theo mặc định:


```bash
rgb interfaces
```


Nếu giao diện này chưa được tích hợp, hãy sao chép tệp:


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Biên dịch nó:


```bash
cargo run
```


Sau đó, nhập giao diện mà bạn lựa chọn:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Tuy nhiên, chúng tôi được thông báo rằng chưa có lược đồ nào được nhập vào phần mềm. Cũng không có hợp đồng nào trong kho lưu trữ. Để xem, hãy chạy lệnh:


```bash
rgb schemata
```


Sau đó, bạn có thể sao chép kho lưu trữ để lấy các sơ đồ mạch cụ thể:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


Kho lưu trữ này chứa, trong thư mục `src/`, một số tệp Rust (ví dụ: `nia.rs`) định nghĩa các lược đồ (NIA cho "*Tài sản không thể mở rộng*", UDA cho "*Tài sản kỹ thuật số duy nhất*", v.v.). Để biên dịch, bạn có thể chạy lệnh sau:


```bash
cd rgb-schemata
cargo run
```


Thao tác này tạo ra một số tệp `.rgb` và `.rgba` tương ứng với sơ đồ đã biên dịch. Ví dụ, bạn sẽ tìm thấy tệp `NonInflatableAsset.rgb`.


### Nhập khẩu Schema và Interface Implementation


Giờ bạn có thể nhập sơ đồ vào `rgb`:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


Thao tác này sẽ thêm nó vào kho lưu trữ cục bộ. Nếu chúng ta chạy lệnh sau, ta sẽ thấy lược đồ hiện đã xuất hiện:


```bash
rgb schemata
```


## Tạo (phát hành) Contract


Có hai cách tiếp cận để tạo ra một tài sản mới:




- Chúng ta có thể sử dụng script hoặc viết mã trong Rust để tạo ra Contract bằng cách điền các trường lược đồ (trạng thái toàn cục, Owned State, v.v.) và tạo ra tệp `.rgb` hoặc `.rgba`;
- Hoặc sử dụng trực tiếp lệnh phụ `issue`, với tệp YAML (hoặc TOML) mô tả các thuộc tính của token.


Bạn có thể tìm thấy các ví dụ trong Rust trong thư mục `examples`, minh họa cách bạn xây dựng một `ContractBuilder`, điền vào `trạng thái toàn cục` (tên tài sản, mã chứng khoán, nguồn cung, ngày tháng, v.v.), xác định Owned State (UTXO nào được gán cho nó), sau đó biên soạn tất cả những điều này thành một *lô hàng hợp đồng* mà bạn có thể xuất, xác thực và nhập vào kho.


Cách khác là chỉnh sửa thủ công tệp YAML để tùy chỉnh `ticker`, `name`, `supply`, v.v. Giả sử tệp có tên là `RGB20-demo.yaml`. Bạn có thể chỉ định:




- `spec`: mã chứng khoán, tên, độ chính xác;
- `terms`: một trường dành cho các thông báo pháp lý;
- `issuedSupply`: số lượng token đã được phát hành;
- `assignments`: chỉ ra Seal dùng một lần (*định nghĩa niêm phong*) và số lượng đã được mở khóa.


Dưới đây là một ví dụ về tệp YAML cần tạo:


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: Plan ₿ Academy
name: Plan ₿ Academy
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-CLI](assets/fr/05.webp)


Sau đó chỉ cần chạy lệnh:


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


Trong trường hợp của tôi, mã định danh lược đồ duy nhất (phải được đặt trong dấu ngoặc đơn) là `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` và tôi chưa nhập bất kỳ tổ chức phát hành nào. Vì vậy, lệnh của tôi là:


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Nếu bạn không biết ID lược đồ, hãy chạy lệnh sau:


```bash
rgb schemata
```


CLI trả lời rằng một hợp đồng mới đã được phát hành và thêm vào kho. Nếu chúng ta nhập lệnh sau, ta sẽ thấy hiện có thêm một hợp đồng nữa, tương ứng với hợp đồng vừa được phát hành:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


Tiếp theo, lệnh tiếp theo hiển thị trạng thái toàn cầu (tên, mã chứng khoán, nguồn cung...) và danh sách Owned State, tức là các phân bổ (ví dụ: 1 triệu Plan ₿ Academy token được định nghĩa trong UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## Xuất, nhập và xác thực


Để chia sẻ hợp đồng này với người dùng khác, bạn có thể xuất hợp đồng từ kho lưu trữ sang tệp:


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


Tệp `myContractPBN.rgb` có thể được chuyển cho người dùng khác, người đó có thể thêm nó vào kho lưu trữ của mình bằng lệnh:


```bash
rgb import myContractPBN.rgb
```


Khi nhập khẩu, nếu đó là một lô hàng hợp đồng đơn giản, chúng ta sẽ nhận được thông báo "`Đang nhập lô hàng rgb`". Nếu đó là một lô hàng chuyển đổi trạng thái lớn hơn, lệnh sẽ khác (`rgb accept`).


Để đảm bảo tính hợp lệ, bạn cũng có thể sử dụng chức năng xác thực cục bộ. Ví dụ, bạn có thể chạy lệnh sau:


```bash
rgb validate myContract.rgb
```


### Hướng dẫn sử dụng, xác minh và hiển thị Stash


Xin nhắc lại, stash là kho lưu trữ cục bộ các lược đồ, giao diện, triển khai và hợp đồng (Genesis + chuyển đổi). Mỗi lần bạn chạy lệnh "import", bạn sẽ thêm một phần tử vào stash. Bạn có thể xem chi tiết stash này bằng lệnh :


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


Thao tác này sẽ tạo một thư mục chứa thông tin chi tiết về toàn bộ kho đồ.


## Chuyển giao và PSBT


Để thực hiện chuyển khoản, bạn cần thao tác với thiết bị Bitcoin hoặc wallet cục bộ để quản lý các cam kết `Tapret` hoặc `Opret`.


### Tạo hóa đơn


Trong hầu hết các trường hợp, sự tương tác giữa các bên tham gia hợp đồng (ví dụ: Alice và Bob) diễn ra thông qua việc tạo hóa đơn. Nếu Alice muốn Bob thực hiện một việc gì đó (chuyển khoản token, phát hành lại, hành động trong DAO, v.v.), Alice sẽ tạo một hóa đơn nêu chi tiết hướng dẫn của mình cho Bob. Vì vậy, ta có:




- Alice** (người phát hành hóa đơn);
- Bob** (người nhận và thực hiện hóa đơn).


Không giống như các hệ sinh thái khác, hóa đơn RGB không chỉ giới hạn ở khái niệm thanh toán. Nó có thể bao gồm bất kỳ yêu cầu nào liên kết với hợp đồng: thu hồi khóa, bỏ phiếu, tạo hình khắc trên NFT, v.v. Thao tác tương ứng có thể được mô tả trong giao diện hợp đồng.


Lệnh sau tạo ra hóa đơn RGB:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Với :




- `$CONTRACT`: Mã định danh Contract (*ContractId*) ;
- `$INTERFACE`: giao diện cần sử dụng (ví dụ: `RGB20`);
- `$ACTION`: tên của thao tác được chỉ định trong giao diện (đối với thao tác chuyển giao token đơn giản, tên này có thể là "Transfer"). Nếu giao diện đã cung cấp một thao tác mặc định, bạn không cần nhập lại ở đây;
- `$STATE`: dữ liệu trạng thái cần chuyển (ví dụ: số lượng token nếu chuyển một token có thể thay thế được);
- `$SEAL`: Seal dùng một lần của người thụ hưởng (Alice), tức là một tham chiếu rõ ràng đến UTXO. Bob sẽ sử dụng thông tin này để xây dựng giao dịch chứng thực, và đầu ra tương ứng sau đó sẽ thuộc về Alice (ở dạng *blinded UTXO* hoặc không được mã hóa).


Ví dụ, với các lệnh sau:


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI sẽ tạo ra hóa đơn như sau:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Thông tin này có thể được truyền đến Bob thông qua bất kỳ kênh nào (văn bản, mã QR, v.v.).


### Thực hiện chuyển khoản


Để chuyển tiền từ hóa đơn này:




- Bob (người đang giữ token trong kho của mình) có Bitcoin và wallet. Anh ta cần chuẩn bị một giao dịch Bitcoin (dưới dạng PSBT, ví dụ: `tx.psbt`) để chi tiêu các UTXO vào nơi có các RGB và token cần thiết, cộng thêm một UTXO để đổi tiền;
- Bob thực thi lệnh sau:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Thao tác này tạo ra một tệp `consignment.rgb` chứa nội dung sau:
 - Lịch sử chuyển đổi chứng minh cho Alice thấy rằng token là hàng thật;
 - Quá trình chuyển đổi mới này chuyển đổi token sang Alice dùng một lần (Seal);
 - Giao dịch chứng kiến ​​(không có chữ ký).
- Bob gửi tệp `consignment.rgb` này đến Alice (qua email, máy chủ chia sẻ hoặc giao thức RGB-RPC, Storm, v.v.);
- Alice nhận được `consignment.rgb` và chấp nhận nó vào kho lưu trữ của mình:


```bash
alice$ rgb accept consignment.rgb
```




- CLI kiểm tra tính hợp lệ của quá trình chuyển đổi và thêm nó vào kho lưu trữ của Alice. Nếu không hợp lệ, lệnh sẽ thất bại với các thông báo lỗi chi tiết. Ngược lại, lệnh sẽ thành công và báo cáo rằng giao dịch mẫu vẫn chưa được phát sóng trên mạng Bitcoin (Bob đang chờ tín hiệu xanh từ Alice);
- Để xác nhận, lệnh `accept` trả về một chữ ký (*phiếu lương*) mà Alice có thể gửi cho Bob để chứng minh rằng cô ấy đã xác nhận *lô hàng*;
- Bob sau đó có thể ký và công bố (`--publish`) giao dịch Bitcoin của mình:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Ngay sau khi giao dịch này được on-chain xác nhận, quyền sở hữu tài sản được coi là đã chuyển giao cho Alice. wallet của Alice, đang theo dõi giao dịch mining, thấy Owned State mới xuất hiện trong kho của mình.


Giờ bạn đã biết cách phát hành và chuyển nhượng hợp đồng RGB. Nếu thấy hướng dẫn này hữu ích, tôi rất biết ơn nếu bạn nhấn nút thích bên dưới. Vui lòng chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn rất nhiều!


Tôi cũng khuyên bạn nên xem hướng dẫn khác này, trong đó tôi giải thích cách khởi chạy một node Lightning tương thích với RGB để trao đổi token gần như tức thì:


https://planb.academy/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea