---
name: Đi sâu vào Simplicity
goal: Nắm vững triết lý thiết kế, hệ thống kiểu và toàn bộ vòng đời của Simplicity
objectives:
  - Hiểu ba phương pháp hợp thành nền tảng và chín combinator tạo nên một ngôn ngữ hoàn chỉnh
  - Xây dựng logic Boolean, số học và SHA-256 từ hệ thống kiểu tối giản của Simplicity
  - Nắm được cách các hiệu ứng phụ Failure và Reader cho phép tương tác thực sự với blockchain
  - Học cách các chương trình Simplicity trở thành địa chỉ Taproot và được chi tiêu bằng dữ liệu witness
---

# Đi sâu vào Simplicity

Một khảo sát chuyên sâu về lý thuyết và các quyết định thiết kế đằng sau ngôn ngữ Simplicity, dựa trên loạt bài hoàn chỉnh gồm năm phần ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) của [Dr. Russell O'Connor](https://r6.ca/), người tạo ra Simplicity tại Blockstream Research. Khóa học này giải thích *vì sao* Simplicity được thiết kế như vậy, chứ không phải cách viết nó.

Khóa học đi theo các bài viết của Dr. O'Connor qua ba cách nền tảng để kết hợp các phép tính, hệ thống kiểu tối giản và định lý đầy đủ của nó, việc xây dựng các kiểu dữ liệu và số học thực tiễn từ các nguyên lý đầu tiên, việc đưa hiệu ứng phụ vào một cách cẩn trọng để tương tác với blockchain, và cuối cùng là cách các chương trình được cam kết vào địa chỉ và được chi tiêu on-chain.

+++

# Giới thiệu

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Tổng quan khóa học

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Chào mừng đến với SCR403 — Đi sâu vào Simplicity!

Khóa học này dựa trên loạt bài **"Delving Simplicity"** do [Dr. Russell O'Connor](https://r6.ca/) viết, một Infrastructure Tech Developer tại [Blockstream](https://blockstream.com/) và là người tạo ra Simplicity. Các bài viết gốc được xuất bản trên diễn đàn [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) và là tư liệu nguồn chính cho khóa học này. Chúng tôi biết ơn công trình tiên phong của ông, nhờ đó nội dung giáo dục này mới có thể ra đời.

### Bạn sẽ học gì

Khóa học này khám phá triết lý thiết kế và nền tảng toán học đằng sau Simplicity, ngôn ngữ script thế hệ mới được kích hoạt trên [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) vào tháng 7 năm 2025. Khóa học đi theo trọn bộ loạt bài năm phần và được cấu trúc thành hai phần nội dung chính:

1. **Nền tảng của Simplicity** — Vì sao tính toán trên blockchain đòi hỏi một ngôn ngữ khác về căn bản, ba cách kết hợp thao tác (tuần tự, song song, điều kiện), và chín combinator lõi tạo thành một ngôn ngữ đầy đủ về mặt toán học
2. **Từ kiểu dữ liệu đến chương trình** — Xây dựng logic Boolean, số học và SHA-256 từ các nguyên lý đầu tiên; hiểu các hiệu ứng phụ Failure và Reader cho phép tương tác với blockchain; và học cách các chương trình được cam kết vào địa chỉ Taproot thông qua Commitment Merkle Root rồi được chi tiêu bằng dữ liệu witness

### Điều kiện tiên quyết

Đây là một khóa học **trình độ chuyên gia** (khoảng 10 giờ). Bạn nên nắm vững:
- Các khái niệm cơ bản về Bitcoin scripting (việc xác thực giao dịch làm gì)
- Các khái niệm lập trình nền tảng (kiểu, hàm, hợp thành)
- Một chút quen thuộc với ký hiệu toán học sẽ hữu ích nhưng không bắt buộc. Chúng tôi sẽ giới thiệu mọi thứ khi cần

### Tài nguyên chính

- **Bài viết gốc**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) của Dr. Russell O'Connor trên Delving Bitcoin
- **Kho mã Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — mã nguồn và các chứng minh hình thức Rocq
- **Trang web chính thức**: [simplicity-lang.org](https://simplicity-lang.org/) — tài liệu và tham chiếu SimplicityHL
- **Blog Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — tổng quan kỹ thuật

Sẵn sàng đi sâu vào một trong những công trình kỹ thuật Bitcoin thanh lịch nhất chưa? Bắt đầu nào!

## Simplicity là gì?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Nếu bạn đến với khóa học này mà chưa có nền tảng về Simplicity, chương này sẽ giúp bạn định hướng trước khi chúng ta đi vào phần sâu.

### Simplicity trong vài nét

Simplicity là một **ngôn ngữ hợp đồng thông minh gốc Bitcoin**, hiện đang chạy trên Liquid Network. Được Dr. Russell O'Connor hình dung lần đầu khoảng năm 2012 và trình bày chi tiết trong bài báo năm 2017 của ông *Simplicity: A New Language for Blockchains*, nó được kích hoạt trên Liquid Network vào tháng 7 năm 2025 sau nhiều năm xác minh hình thức và phát triển.

Khác với Solidity của Ethereum, một ngôn ngữ hợp đồng cấp cao và Turing-complete, Simplicity được thiết kế tối giản một cách có chủ ý. Nó có:
- **Ba bộ tạo kiểu** (đơn vị, tổng, tích)
- **Chín combinator** (các thao tác cơ bản và quy tắc hợp thành)
- **Không vòng lặp, không đệ quy, không bộ nhớ động**

Chỉ từ các primitive này, bạn có thể xây dựng mọi phép tính cần thiết cho xác thực giao dịch, từ logic Boolean đến băm SHA-256 đầy đủ.

### Hôm nay bạn có thể làm gì với Simplicity?

Simplicity đã đang vận hành các ứng dụng thực tế trên Liquid Network. Đáng chú ý nhất là [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), một thị trường quyền chọn không cần oracle, nơi người dùng giao dịch quyền chọn mua trên L-BTC với USDt làm tài sản thế chấp (hợp đồng cơ sở cũng hỗ trợ quyền chọn bán). Các dự án Simplicity đang hoạt động khác gồm [Swaption](https://swaption.io/) của SideSwap (quyền chọn) và dự án mã nguồn mở [Deadcat](https://github.com/Resolvr-io/deadcat) của Resolvr (thị trường dự đoán). Ngoài DeFi, Simplicity cho phép các điều kiện chi tiêu nâng cao như vault, covenant và các sơ đồ multisig phức tạp vốn bất khả thi hoặc không an toàn trong Bitcoin Script.

### Khóa học này là gì — và không phải là gì

Đây **không** phải là hướng dẫn lập trình thực hành. Bạn sẽ không viết chương trình Simplicity ở đây. Nếu đó là điều bạn đang tìm, hãy xem:
- [simplicity-lang.org](https://simplicity-lang.org/) — tài liệu chính thức và ngôn ngữ cấp cao SimplicityHL
- [Kho GitHub Simplicity](https://github.com/BlockstreamResearch/simplicity) — triển khai tham chiếu, ví dụ và chứng minh Rocq
- [Bài viết blog Blockstream](https://blog.blockstream.com/en-simplicity-github/) về cách bắt đầu

Điều khóa học này **thực sự** bàn đến: các **lựa chọn triết lý và kỹ thuật** đằng sau thiết kế của Simplicity. Vì sao ngôn ngữ này được tạo ra theo cách này? Vì sao chỉ có chín combinator? Vì sao không có đệ quy? Vì sao việc hệ thống kiểu kết nối với phép tính sequent của Gentzen lại quan trọng?

Hãy xem nó như việc hiểu **vì sao động cơ được xây theo cách này** thay vì học lái chiếc xe.

### Khóa học này dành cho ai?

Khóa học này lý tưởng cho:
- **Nhà phát triển giao thức** muốn hiểu nền tảng của Simplicity trước khi viết mã
- **Nhà nghiên cứu Bitcoin** quan tâm đến xác minh hình thức và cách tiếp cận dựa trên lý thuyết kiểu
- **Nhà khoa học máy tính** tò mò về mối liên hệ giữa phép tính sequent và tính toán trên blockchain
- **Bitcoiner nâng cao** muốn vượt ra ngoài hiểu biết bề mặt về khả năng scripting của Liquid

Nếu các thuật ngữ như "kiểu tổng", "combinator" hoặc "phép tính sequent" hoàn toàn mới với bạn, đừng lo; chúng tôi giải thích mọi thứ từ đầu. Nhưng hãy chuẩn bị cho một hành trình dày đặc và mang tính toán học.

### Từ bài viết thành khóa học

Loạt bài "Delving Simplicity" gốc của Dr. O'Connor được cấu trúc thành năm bài kỹ thuật. Khóa học này tổ chức lại và chú giải tư liệu đó thành một lộ trình học tập tuần tự với các bài quiz để kiểm tra hiểu biết của bạn trên đường đi. Các ý tưởng, định nghĩa và chứng minh là của ông, còn chúng tôi đã điều chỉnh định dạng cho giáo dục có cấu trúc.

# Nền tảng của Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Các cách nền tảng để kết hợp phép tính

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Giờ đây Simplicity đã được kích hoạt trên Liquid Network, tôi muốn đi sâu vào triết lý và thiết kế của ngôn ngữ Simplicity.

Xác thực giao dịch của Bitcoin là một ứng dụng khác biệt đáng kể so với thiết kế ngôn ngữ lập trình thông thường. Chi phí block space rất đắt đỏ nên chương trình cần phải gọn. Các chương trình trong giao dịch Bitcoin chỉ từng được thực thi trên một đầu vào duy nhất và mọi người đều thực thi chương trình trên cùng đầu vào đó. Ngoài ra, tác nhân ủy quyền giao dịch đã biết trước kết quả của phép tính: giao dịch hợp lệ.

Thông thường, tác nhân ủy quyền sẽ chạy các phép tính tốn kém hơn nhiều để suy ra dữ liệu witness chứng thực tính hợp lệ của giao dịch, trong khi các chương trình chạy trên blockchain cần kiểm tra tính hợp lệ của dữ liệu witness. Kiểm tra tính hợp lệ thường rẻ hơn nhiều so với chứng minh tính hợp lệ.

Chúng tôi đã thiết kế Simplicity với các thách thức thiết kế ngôn ngữ độc đáo như vậy trong đầu. Ví dụ, Simplicity yêu cầu các nhánh không được thực thi phải bị cắt tỉa để chúng không xuất hiện trên blockchain. Các bước tiền xử lý được thiết kế cẩn thận để thể hiện độ phức tạp thời gian (gần) tuyến tính theo kích thước chương trình Simplicity. Phân tích tĩnh được dùng thay cho "gas", vốn không thể được tính nếu không thực thi mã theo một cách được quy định, nhờ đó các chi tiết của mô hình thực thi không trở thành yếu tố then chốt của đồng thuận. Không cấp phát bộ nhớ động trong quá trình thực thi. Và còn nhiều nữa.

Trước khi đi sâu vào các chi tiết thiết kế của Simplicity, tôi muốn bắt đầu loạt bài này bằng một số triết lý lập trình về các cách tổng quát để kết hợp những khối xây dựng cơ bản nhằm tạo ra chức năng mới.

### Hợp thành

Giả sử một người đang thiết kế một ngôn ngữ cho các giao dịch có thể lập trình trên một blockchain như Bitcoin. Cụ thể, chương trình chỉ có quyền truy cập vào dữ liệu giao dịch và dữ liệu UTXO của các input, và việc thực thi chỉ xác định tính hợp lệ của giao dịch (điều này cho phép kết quả thực thi được cache). Giả sử người đó bắt đầu với một tập các thao tác cơ bản có thể thực hiện nhiều nhiệm vụ khác nhau như tính toán cơ bản, đọc và/hoặc xử lý dữ liệu từ giao dịch, và xác minh chữ ký. Mỗi thao tác tiêu thụ một kiểu đầu vào nào đó (có thể rỗng) và trả về một kiểu đầu ra nào đó. Chúng ta có những cách nào để kết hợp các thao tác cơ bản này thành các thao tác phức tạp hơn?

### Hợp thành tuần tự

![Hợp thành tuần tự](assets/en/001.webp)

Phương pháp hợp thành nền tảng nhất là hợp thành tuần tự. Nếu chúng ta có hai thao tác cơ bản, trong đó kiểu dữ liệu đầu ra của thao tác này khớp với kiểu dữ liệu đầu vào của thao tác kia, thì chúng ta có thể kết hợp hai thao tác này thành một thao tác hợp thành mới. Thao tác mới này chạy hai thao tác cơ bản đó theo thứ tự, lấy đầu vào là đầu vào của thao tác thứ nhất, truyền đầu ra của thao tác thứ nhất đó vào đầu vào của thao tác thứ hai, và cuối cùng trả về đầu ra của thao tác thứ hai đó.

Tất nhiên, chúng ta không cần tự giới hạn ở việc chỉ kết hợp các thao tác cơ bản. Giờ chúng ta đã có một số thao tác hợp thành, ta cũng có thể kết hợp chúng bằng hợp thành hàm.

Trong toán học, hợp thành tuần tự này thường chỉ được gọi là "hợp thành", và người ta có thể nghĩ rằng đây là cách duy nhất để hợp thành mọi thứ. Tuy nhiên, chúng ta còn có những cách khác để hợp thành các thao tác.

### Hợp thành song song

![Hợp thành song song](assets/en/002.webp)

Giả sử chúng ta có hai thao tác, chúng có thể là thao tác cơ bản hoặc phức tạp, và cả hai đều nhận cùng một kiểu đầu vào. Một cách nền tảng thứ hai để hợp thành hai thao tác này là thực thi cả hai trên cùng một đầu vào. Đây được gọi là hợp thành song song, và kiểu đầu ra là "tích" của các kiểu đầu ra của các thao tác gốc, chứa cặp gồm hai đầu ra.

Dù được gọi là hợp thành "song song", và về nguyên tắc hai thao tác có thể được thực thi song song, thực thi song song không phải là yêu cầu vận hành. Chúng ta có thể triển khai hợp thành song song "tuần tự" bằng cách thực thi một thao tác trước rồi đến thao tác thứ hai. Chúng ta không quan tâm đến chi tiết cách hợp thành song song được triển khai miễn là đầu ra giống nhau.

### Hợp thành điều kiện

![Hợp thành điều kiện](assets/en/003.webp)

Hợp thành điều kiện là đối ngẫu của hợp thành song song. Trong trường hợp này, chúng ta có hai thao tác tạo ra cùng đầu ra, và chúng ta hợp thành chúng bằng cách chọn một trong hai để thực thi. Đầu vào của thao tác hợp thành này là "tổng" hoặc "tagged union" của các kiểu đầu vào của thao tác gốc. Trong trường hợp này, tag, "Left" hoặc "Right", là một bit duy nhất trong dữ liệu của đầu vào, xác định kiểu dữ liệu nào đang được mang theo, và do đó thao tác nào trong hai thao tác có thể được thực thi.

Hợp thành điều kiện hoạt động theo cùng một cách ngay cả khi đầu vào là tổng của hai kiểu giống hệt nhau. Kiểu tổng vẫn chứa một tag, và giá trị của tag đó xác định thao tác nào trong hai thao tác sẽ được thực thi.

### Hợp thành trong Bitcoin Script

Có nhiều cách hiện thực hóa ba loại hợp thành này trong các ngôn ngữ lập trình khác nhau. Trong Bitcoin Script, hợp thành tuần tự được hiện thực hóa (xấp xỉ) bằng việc nối hai routine (đây là lý do Bitcoin Script được gọi là một ngôn ngữ lập trình concatenative), vì đầu ra của một routine được để lại trên stack để routine kế tiếp tiêu thụ. Hợp thành song song đạt được bằng cách dùng các thao tác duplicate và swap để thao tác stack sao cho hai routine có thể chạy trên cùng một đầu vào. Mọi thứ không hoàn toàn đơn giản, vì cái chúng ta gọi là "tích" của các kiểu thường được hiện thực bằng cách sử dụng nhiều stack item. Hy vọng bạn thấy được ý tưởng tổng quát.

Tất nhiên, hợp thành điều kiện được hiện thực hóa bằng `OP_IF`, nhánh theo giá trị trên stack. Trong trường hợp này, item trên đỉnh stack đóng vai trò của tag, và thường item hoặc các item tiếp theo trên stack thuộc các "kiểu" khác nhau tùy thuộc vào giá trị của tag. Với mỗi trường hợp, kiểu của stack item có thể chỉ phù hợp để xử lý bởi một trong các nhánh trong `OP_IF`. Tuy nhiên, sau khi chúng ta đến `OP_ENDIF`, các stack item phải có "kiểu" nhất quán sao cho phần script còn lại có thể tiếp tục độc lập với nhánh đã được chọn trước đó.

### Hợp thành trong Simplicity

Chúng tôi thiết kế Simplicity với các combinator triển khai trực tiếp ba dạng hợp thành này. Cùng với một vài combinator nữa để hỗ trợ các thao tác cơ bản khác liên quan đến kiểu tích và kiểu tổng, ngôn ngữ Simplicity lõi cuối cùng gồm chín combinator đủ để biểu diễn mọi phép tính hữu hạn. Chúng ta sẽ thảo luận chi tiết hơn trong chương tiếp theo.

### Loại hợp thành thứ tư

Trước khi kết thúc, ta nên nhắc rằng còn ít nhất một loại hợp thành nữa trong Khoa học Máy tính, đó là "hợp thành đệ quy". Trong hợp thành đệ quy, một thao tác được lặp lại nhiều lần.

Lưu ý rằng Bitcoin Script không hỗ trợ hợp thành đệ quy, và tương tự, chúng tôi đã loại trừ rõ ràng đệ quy không bị chặn khỏi thiết kế của Simplicity. Luận điểm của chúng tôi là tính toán lặp không bị chặn được triển khai tốt hơn bằng các covenant đệ quy, tính toán qua nhiều giao dịch. Điều này cho phép người dùng tránh các ràng buộc về block space và standardness, đồng thời dự đoán chi phí giao dịch tốt hơn.

Dù vậy, có những cách lạm dụng tính năng delegation của Simplicity để cung cấp thứ gì đó giống hợp thành đệ quy không bị chặn, điều mà chúng ta có thể thảo luận sau trong loạt bài này.

### Kết luận

Chúng ta đã xem xét ba dạng hợp thành chính để biến các thao tác cơ bản thành các thao tác phức tạp:

- hợp thành tuần tự
- hợp thành song song
- hợp thành điều kiện

Chúng ta đã thảo luận cách các dạng hợp thành này được hiện thực hóa trong Bitcoin Script, và gợi ý cách chúng đã ảnh hưởng đến thiết kế của ngôn ngữ Simplicity. Chúng ta lưu ý rằng loại hợp thành thứ tư, hợp thành đệ quy, bị loại trừ rõ ràng khỏi cả Simplicity lẫn Bitcoin Script.

Trong chương tiếp theo, chúng ta sẽ mô tả chín combinator tạo nên lõi của ngôn ngữ Simplicity, cách chúng trực tiếp hiện thực hóa ba dạng hợp thành này, và cách điều đó tạo thành một ngôn ngữ hoàn chỉnh để mô tả mọi phép tính hữu hạn.

## Tính đầy đủ combinator của Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

Trong chương này, chúng ta giới thiệu ngôn ngữ Simplicity lõi và chỉ ra rằng ngôn ngữ này là đầy đủ, nghĩa là mọi phép tính hữu hạn đều có thể được biểu diễn trong nó.

### Các kiểu Simplicity

Simplicity hỗ trợ ba constructor kiểu nền tảng. Kiểu tích `A × B` biểu diễn đầu ra của hợp thành song song, trong khi kiểu tổng `A + B` (tagged union) xử lý đầu vào của hợp thành điều kiện. Kiểu thứ ba là kiểu đơn vị.

### Kiểu đơn vị

Kiểu đơn vị, ký hiệu là `𝟙` hoặc `ONE`, chứa đúng một giá trị: tuple rỗng `⟨⟩` hoặc `()`. Kiểu dữ liệu không bit này không mang thông tin nào.

### Kiểu tổng

Kiểu tổng `A + B` kết hợp hai kiểu với các tag cho biết "left" hoặc "right." Các giá trị được viết là `σᴸ(a)` hoặc `inl(a)` cho giá trị gắn tag trái và `σᴿ(b)` hoặc `inr(b)` cho giá trị gắn tag phải. Các tag vẫn phân biệt ngay cả khi kết hợp các kiểu giống hệt nhau.

#### Kiểu Boolean

Kiểu `𝟙 + 𝟙`, ký hiệu là `𝟚` hoặc `TWO`, biểu diễn kiểu một bit với hai giá trị. Theo quy ước, `σᴸ⟨⟩` biểu diễn false/zero, còn `σᴿ⟨⟩` biểu diễn true/one.

### Kiểu tích

Kiểu tích `A × B` chứa các cặp giá trị viết là `⟨a, b⟩` hoặc `(a, b)`. Kiểu `𝟚 × 𝟚` có bốn giá trị, khác với bốn giá trị trong `𝟚 + 𝟚`.

### Biểu thức Simplicity lõi

Các thao tác được ký hiệu là `f : A ⊢ B`, nghĩa là kiểu đầu vào `A` và kiểu đầu ra `B`. Simplicity là "first-order" — nó không có kiểu hàm.

### Hai thao tác cơ bản

Ngôn ngữ lõi cung cấp hai thao tác cơ bản:

**Identity (`iden`).** Thao tác identity truyền nguyên đầu vào qua không thay đổi:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Thao tác unit bỏ đầu vào và trả về tuple rỗng:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Chúng tạo thành các họ với một thao tác cho mỗi kiểu.

### Ba combinator hợp thành

Hợp thành tuần tự dùng `comp f g` (viết là `f ⨾ g` hoặc `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Hợp thành song song dùng `pair f g` (viết là `f ▵ g` hoặc `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Hợp thành điều kiện dùng `case f g : (A + B) × C ⊢ D`, cho phép các nhánh truy cập môi trường dùng chung `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Vì sao hợp thành điều kiện lại có dạng này — một tổng được ghép cặp với môi trường dùng chung `C` — thay vì một `copair f g : A + B ⊢ C` đơn giản hơn chỉ chọn một nhánh? Vì một `copair` trần không thể biểu diễn **phân phối**: hàm `dist : (A + B) × C ⊢ A × C + B × C` đẩy một đầu vào dùng chung vào bất cứ nhánh nào được chọn. Bằng cách đưa môi trường `C` trực tiếp vào `case`, Simplicity có được hợp thành điều kiện *và* phân phối từ một combinator duy nhất — một trong những quyết định thiết kế then chốt giữ ngôn ngữ lõi ở mức chín combinator.

### Bốn combinator nữa

Tiêu thụ kiểu tích dùng `take` và `drop`:

**take** trích xuất phần tử bên trái:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** trích xuất phần tử bên phải:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Tạo kiểu tổng dùng `injl` và `injr`:

**injl** bọc bằng tag trái:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** bọc bằng tag phải:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Chín combinator lõi

Tổng cộng, Simplicity có đúng chín combinator lõi:

| Combinator | Mục đích |
|---|---|
| `iden` | Truyền đầu vào qua |
| `unit` | Bỏ đầu vào |
| `comp` | Hợp thành tuần tự |
| `pair` | Hợp thành song song |
| `case` | Hợp thành điều kiện |
| `take` | Trích trái từ tích |
| `drop` | Trích phải từ tích |
| `injl` | Chèn vào bên trái của tổng |
| `injr` | Chèn vào bên phải của tổng |

### Simplicity và phép tính sequent

Thiết kế của Simplicity bắt nguồn từ mảnh hội-tuyển của phép tính sequent Gentzen. Chính xác hơn, nó là một biến thể của *diễn giải hàm* của phép tính sequent, bản thân điều này tương tự với tương ứng Curry-Howard giữa suy diễn tự nhiên và lambda calculus. Các quy tắc combinator thể hiện "các kiểu nhỏ hơn trong tiền đề so với kết luận", cho phép Bit Machine — trình thông dịch máy stack trừu tượng của Simplicity — giảm thiểu sao chép dữ liệu trong quá trình thực thi.

### Giá trị không phải là biểu thức

Biểu thức Simplicity biểu thị thao tác, không phải giá trị. Ký hiệu `scribe b : A ⊢ B` biểu diễn một biểu thức duy nhất luôn trả về giá trị `b`, đóng vai trò tiện lợi ký hiệu chứ không phải một combinator. Điều này phản chiếu Bitcoin Script, nơi các thao tác như `OP_1` đẩy giá trị thay vì biểu diễn chúng trực tiếp.

### Định lý đầy đủ của Simplicity

Khi đã có đủ chín combinator, làm sao chúng ta biết mình không thiếu thứ gì — rằng chín combinator này thực sự đủ? Định lý đầy đủ của Simplicity trả lời điều này: với bất kỳ hàm nào giữa các kiểu Simplicity (hữu hạn), sẽ có một biểu thức Simplicity biểu thị nó. Chứng minh mang tính xây dựng — nó chỉ ra cách xây biểu thức:

1. **Phân rã đầu vào**: Dùng các biểu thức `case` lồng nhau để phân rã hoàn toàn bất kỳ đầu vào nào thuộc bất kỳ kiểu nào thành các bit cấu thành của nó
2. **Xây bảng tra cứu**: Với mỗi đầu vào khả dĩ, dùng `scribe` để tạo đầu ra tương ứng
3. **Lắp ráp**: Các case lồng nhau và scribe cùng tạo thành một bảng tra cứu khổng lồ triển khai hàm

Định lý này được xác minh hình thức trong proof assistant Rocq (trước đây là Coq). Chứng minh là một phần của kho mã Simplicity chính thức và đã được máy kiểm tra về tính đúng đắn.

Dù định lý đầy đủ đảm bảo rằng chín combinator của Simplicity có thể biểu diễn mọi hàm giữa các kiểu Simplicity (hữu hạn), các biểu thức thu được từ phép xây dựng bảng tra cứu lớn đến mức không thực tế. Một hàm trên đầu vào 256 bit sẽ cần một bảng tra cứu với 2²⁵⁶ mục. Đây là lý do các chương tiếp theo tập trung vào việc xây dựng các biểu thức hiệu quả khai thác cấu trúc của phép tính, thay vì brute-force mọi thứ qua bảng tra cứu.

### Kết luận

Ngôn ngữ lõi của Simplicity bao gồm một hệ thống kiểu và các combinator cho phép mọi phép tính hữu hạn. Dù định lý Đầy đủ đảm bảo tính biểu đạt, các biểu thức sinh ra từ phép xây dựng tổng quát lớn đến mức không thực tế. Phát triển Simplicity thực tiễn liên quan đến việc khai thác cấu trúc tính toán để có các biểu thức ngắn gọn. Các chương tiếp theo khám phá cấu trúc dữ liệu, tương tác giao dịch và các combinator bổ sung.

# Từ kiểu dữ liệu đến chương trình

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Xây dựng kiểu dữ liệu

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Trong các chương trước, chúng ta đã chỉ ra cách tập combinator lõi của Simplicity đủ để triển khai mọi phép tính thuần hữu hạn. Chương này cho thấy cách xây dựng các cấu trúc dữ liệu và phép tính thực tiễn từ những primitive này — giống như cách máy tính được xây từ các cổng logic.

### Logic Boolean

Kiểu Boolean, ký hiệu `𝟚`, bằng `𝟙 + 𝟙` và có hai giá trị: `σᴸ⟨⟩` (false) và `σᴿ⟨⟩` (true). Dùng các combinator lõi, các toán tử logic Boolean có thể được xây dựng.

#### Thao tác And

Thao tác logic `and : 𝟚 × 𝟚 ⊢ 𝟚` nhận hai bit và trả về một bit. Triển khai này rẽ nhánh theo bit đầu tiên: nếu false, trả về false; nếu không, trả về bit thứ hai.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Kiểm thử với `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Kiểm thử với `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Các thao tác logic khác

Thao tác `not` cần một combinator trợ giúp:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

`iden ▵ unit : A ⊢ A × 𝟙` ban đầu thêm một "môi trường" rỗng vào đầu vào, cho phép combinator `case` áp dụng. Việc dùng `take` trong hai nhánh loại bỏ môi trường rỗng này để thực thi `f` hoặc `g`.

Các thao tác logic Boolean khác:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bộ cộng bit

Một "half-adder" nhận hai bit và cộng chúng, tạo ra đầu ra hai bit: bit nhớ và bit tổng.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Một "full-adder" cộng ba bit, tạo đầu ra hai bit. Đầu vào dùng tuple lồng nhau `(𝟚 × 𝟚) × 𝟚`.

Với tuple lồng nhau, ký hiệu ngắn gọn được dùng:

- `O f` biểu thị `take f`
- `I f` biểu thị `drop f`
- `H` biểu thị `iden`

Ví dụ, `I O H` nghĩa là `drop (take iden) : A × (B × C) ⊢ B`, trích xuất giá trị ở giữa. Ký hiệu này gợi đến chữ số nhị phân: khi nghĩ về tuple lồng nhau như cây nhị phân, ký hiệu biểu diễn các chữ số nhị phân đảo ngược của vị trí trên cây. Các biểu thức này tạo thành chỉ số De Bruijn cho Simplicity.

**Lưu ý:** Ký hiệu `I`, `O` và `H` chỉ áp dụng cho các biểu thức con chỉ gồm `take`, `drop` và `iden`.

Full-adder hợp thành hai half-adder, lấy logic `or` của các bit nhớ:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Ở dòng đầu tiên, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` chạy half-adder trên hai bit đầu, lưu lại bit cuối.

Ở dòng thứ hai, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` lưu bit đầu tiên (carry-out của half-adder thứ nhất) và chạy half-adder trên hai bit cuối.

Ở dòng cuối, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` lấy OR logic của hai bit đầu (carry-out của cả hai half-adder) và trả về bit sum-out của half-adder thứ hai.

Điều này minh họa lập trình Simplicity: dùng ký hiệu `I`, `O` và `H` để tham chiếu các bit dữ liệu, tạo các "môi trường" phù hợp để gọi các hàm khác thông qua hợp thành tuần tự.

Người dùng không định nghĩa trực tiếp các thao tác cấp thấp. Phần sau của loạt bài này thảo luận các jet thư viện chuẩn triển khai những hàm phổ biến. Người dùng cuối không được kỳ vọng lập trình trực tiếp bằng Simplicity, tương tự như Bitcoin Script. Thay vào đó, các ngôn ngữ cấp cao như SimplicityHL sinh mã Simplicity, quản lý các "môi trường" biểu thức con và dịch các biến có tên thành các chuỗi `take` và `drop` thích hợp.

### Vector

Vector độ dài cố định được định nghĩa bằng cách tạo các tích lặp của kiểu `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Chúng có thể được viết là `A^2`, `A^4`, `A^8`, v.v.

Vector chỉ được định nghĩa cho các độ dài là lũy thừa của hai. Các lũy thừa khác đòi hỏi chọn quy ước đặt ngoặc.

Cho biểu thức `f : A ⊢ B`, việc ghép cặp lặp lại "map" nó trên các vector độ dài cố định:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Cho hàm `f : A × B ⊢ B`, việc lặp hoặc "folding" trên các vector độ dài cố định:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Có nhiều biến thể. Cho `f : A × B ⊢ C`, "zip" trên các vector được ghép cặp với `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Cho `f : (A × B) × C ⊢ C`, fold trên các vector được ghép cặp với `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Kết hợp `map` và `fold-right` tạo các combinator tích lũy: `f : A × C ⊢ C × B` cho `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Còn nhiều biến thể khác có thể tồn tại.

#### Từ nhiều bit

Một vector bit tạo ra số nguyên nhiều bit. Ví dụ, `𝟚³²` là kiểu từ 32 bit. `𝟚²⁵⁶` là kiểu từ 256 bit, phù hợp cho hash và các thao tác mật mã.

Dùng full-adder, một biến thể của các thao tác vector định nghĩa một "ripple carry adder" trên các từ nhiều bit:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` nhận hai số nhị phân n bit và một carry-input một bit, trả về một cờ carry-out một bit và một tổng n bit.

#### SHA-256

Bằng cách định nghĩa đệ quy các thao tác số học trên từ nhiều bit — trừ, nhân, chia — và các thao tác logic theo bit như AND, OR, XOR logic, rồi kết hợp chúng nhiều lần, ngay cả hàm nén khối của SHA-256 cũng có thể được xây dựng:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Phép nén SHA-256 được định nghĩa hình thức bằng Simplicity trong proof assistant Rocq (trước đây là Coq), với một chứng minh hình thức rằng triển khai `sha256-hash-block` là đúng.

Phép nén chạy quá chậm dưới dạng Simplicity thô. Jet thực thi các hàm phổ biến như nén SHA-256 một cách native. Các triển khai Simplicity thuần đóng vai trò đặc tả hình thức cho jet.

### Kiểu Option

Kiểu Option sinh ra từ việc lấy tổng với kiểu đơn vị:

```
Option A ≔ 𝟙 + A
```

Kiểu `Option A` có thể được viết là `A?` hoặc `𝕊 A` (trong đó `𝕊` nghĩa là "successor"). Các hàm map trên kiểu option:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Các combinator monadic như bind có thể được định nghĩa:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffer độ dài biến đổi

"Buffer" là các kiểu cho vector được lấp đầy một phần:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Kiểu `Xᑉ⁸` mở rộng thành `(1 + X⁴) × ((1 + X²) × (1 + X))`. Xem nó như một đa thức và khai triển sẽ cho `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Diễn giải như một kiểu, nó biểu diễn tổng của mọi tuple khả dĩ của X có độ dài đến 7, bao gồm cả tuple rỗng. Đây chính xác là kiểu của list có độ dài nhỏ hơn nghiêm ngặt 8.

Giống vector, các thao tác mapping và folding có thể được định nghĩa trên buffer. Các thao tác stack gồm `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` và `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` nối một item vào buffer, trả về một vector đầy nếu xảy ra tràn. `pop-<n` loại bỏ một item, trả về buffer nhỏ hơn và item bị loại bỏ, tùy chọn trả về nothing nếu buffer ban đầu rỗng.

Định nghĩa `push-<n`, theo đệ quy:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Simplicity thô trở nên khó theo dõi khi vượt quá một mức độ phức tạp nhất định. Người dùng cuối sử dụng các ngôn ngữ cấp cao như SimplicityHL để sinh ra những biểu thức thành ngữ này.

### Kết luận

Chương này đã chỉ ra cách xây dựng các thao tác logic từ bit. Từ đó, số học cấp bit xuất hiện, cho phép lý luận về thực thi. Các kiểu vector được phát triển, minh họa việc lặp trên các từ nhiều bit để định nghĩa số học. Tiếp tục như vậy, các thao tác mật mã như SHA-256 và xác thực chữ ký Schnorr có thể được định nghĩa chỉ bằng các combinator Simplicity — tất cả thực sự đã được định nghĩa bằng Simplicity.

Chương này không phải là hướng dẫn toàn diện về mọi kiểu dữ liệu và thao tác khả dĩ có thể xây dựng trong Simplicity, mà minh họa cách đạt được chức năng thực tiễn trong các ràng buộc của Simplicity. Dù các kiểu bị chặn hữu hạn, vẫn có thể định nghĩa các vector, kiểu buffer và thao tác hữu ích lặp trên những cấu trúc này.

Các đặc tả thao tác của thư viện chuẩn thực tế hơi khác so với các định nghĩa ở đây. Ví dụ, full-adder dùng một hàm XOR 3 ngả và hàm logic "majority" thay vì hai half-adder.

Trong thực tế, các chương trình Simplicity dùng jet cho các thao tác số học và mật mã. Tuy nhiên, jet chỉ thay thế biểu thức. Các combinator lặp trên buffer và vector không thể được thay bằng jet, nên xuất hiện trong các chương trình Simplicity thực tế. Dù thay vì trực tiếp dùng chúng, người dùng cuối sử dụng các ngôn ngữ cấp cao như SimplicityHL để sinh các biểu thức như vậy.

Các combinator được định nghĩa đệ quy dường như tăng theo cấp số nhân về kích thước biểu thức. Điều này không thành vấn đề. Trong quá trình serialization, biểu thức được mã hóa dưới dạng DAG (đồ thị có hướng không chu trình) thay vì cây. Biểu diễn thực tế chỉ tăng tuyến tính.

Cho đến nay, chỉ các phép tính thuần được xem xét. Tương tác với dữ liệu giao dịch cho các nhiệm vụ như ký giao dịch đòi hỏi một cách nào đó để chương trình fail nếu chữ ký không hợp lệ. Chương tiếp theo thảo luận về hiệu ứng phụ trong Simplicity.

## Hai hiệu ứng phụ

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Trong các chương trước, chúng ta đã chỉ ra cách xây dựng một số cấu trúc dữ liệu và phép tính bằng tập combinator lõi của Simplicity. Như đã lưu ý, các combinator lõi đủ để triển khai mọi phép tính thuần hữu hạn. Điều này đặt ra câu hỏi: còn có thể đạt được điều gì nữa? Chúng ta có thể thêm các hiệu ứng phụ bổ sung vào biểu thức.

Có nhiều loại hiệu ứng phụ khả dĩ cho biểu thức: cập nhật trạng thái, ghi vào log, ném ngoại lệ, đọc từ môi trường, gọi continuation, v.v. Các hiệu ứng phụ có trong Simplicity sẽ phụ thuộc vào ứng dụng.

Với các ứng dụng Bitcoin và Liquid, hiện chúng ta có hai hiệu ứng phụ: hiệu ứng Failure, là hiệu ứng ngoại lệ trong đó ngoại lệ có kiểu `𝟙`, và hiệu ứng Reader, cho phép truy cập dữ liệu từ môi trường giao dịch. Các combinator lõi của chúng ta là "thuần"; chúng không có hiệu ứng phụ. Tuy nhiên, jet có thể đưa vào các primitive mới có hiệu ứng phụ.

### Jet có hiệu ứng

Chúng ta sẽ nói thêm về jet ở phần sau của khóa học này, nhưng ở đây chúng ta giới thiệu vài jet ví dụ để minh họa hiệu ứng phụ của chúng.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` là một jet cho một biểu thức nhận pubkey x-only, một thông điệp 256 bit và một chữ ký Schnorr, rồi không trả về gì! Theo kiểu của nó, nó đáng ra phải hành xử giống như `unit`. Khác biệt nằm ở hiệu ứng phụ của jet: nếu xác thực chữ ký thất bại, toàn bộ phép tính bị hủy bằng cách ném một ngoại lệ (kiểu đơn vị). Đây là hiệu ứng Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` là một jet tối giản để biểu diễn hiệu ứng Failure. Nếu đầu vào của `verify` là `false`, toàn bộ phép tính bị hủy bằng cách ném một ngoại lệ. Nếu đầu vào là `true`, không có gì được trả về, nhưng phép tính có thể tiếp tục.

#### Hash giao dịch

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` có vẻ là một hàm hằng, vì chỉ có một giá trị đầu vào khả dĩ: tuple rỗng. Tuy nhiên, jet này đọc từ môi trường giao dịch và tạo ra một hash của dữ liệu giao dịch tương tự như message digest `SIGHASH_ALL` dùng trong xác minh chữ ký của Bitcoin Script. Đây là một ví dụ về hiệu ứng Reader: giá trị trả về phụ thuộc vào môi trường giao dịch mà jet được thực thi trong đó. Có nhiều jet băm khác băm các tập con khác nhau của dữ liệu môi trường giao dịch để giúp xây dựng message digest tùy chỉnh cho chữ ký.

#### Jet introspection

`input-sequence : 𝟚³² ⊢ 𝟚³²?` là một hàm nhận chỉ số input và trả về sequence number của giao dịch cho input đó, tùy chọn trả về nothing nếu chỉ số vượt phạm vi. Một lần nữa, giá trị đầu ra không phải là hàm thuần của chỉ số input, mà thao tác dùng hiệu ứng Reader để truy cập môi trường giao dịch nhằm xác định giá trị đầu ra. Có nhiều jet introspection khác trả về các mảnh khác nhau của dữ liệu môi trường giao dịch.

### Phân loại hiệu ứng

Không phải mọi hiệu ứng phụ đều như nhau. Một số hiệu ứng phụ hành xử tốt hơn các hiệu ứng khác. Chúng ta có thể phân loại hiệu ứng theo mức độ chúng phù hợp với các phép biến đổi chương trình.

#### Hiệu ứng giao hoán

Một hiệu ứng giao hoán là hiệu ứng mà, nếu bạn hoán đổi đầu ra của hai biểu thức, bạn có thể hoán đổi an toàn chính các biểu thức đó mà không làm thay đổi hiệu ứng của biểu thức. Xét `swap = I H ▵ O H : A × B ⊢ B × A`. Nếu `f ▵ g ⨾ swap = g ▵ f` với mọi biểu thức `f` và `g` có hiệu ứng phụ, thì các hiệu ứng là giao hoán.

Đọc dữ liệu giao dịch từ môi trường là một hiệu ứng giao hoán vì kết quả đọc từ môi trường là như nhau, bất kể chúng ta thực hiện việc đọc theo thứ tự nào.

Nói chung, ném ngoại lệ không phải là hiệu ứng giao hoán. Nếu `f` ném một ngoại lệ nào đó `e₁` và `g` ném một ngoại lệ khác `e₂`, thì ngoại lệ nào được ném từ cặp `f` và `g` phụ thuộc vào thứ tự chúng được thực thi.

Tuy nhiên, trong trường hợp đặc biệt của hiệu ứng Failure, trong đó chỉ có thể ném ngoại lệ kiểu đơn vị, hiệu ứng là giao hoán. Bất kể `f` hay `g` ném ngoại lệ, ngoại lệ kết quả sẽ giống nhau, vì chỉ có một giá trị ngoại lệ khả dĩ.

#### Hiệu ứng lũy đẳng

Một hiệu ứng lũy đẳng là hiệu ứng mà, nếu bạn nhân đôi đầu ra của một biểu thức, bạn có thể nhân đôi an toàn chính biểu thức đó mà không làm thay đổi hiệu ứng của biểu thức. Xét `dup = iden ▵ iden : A ⊢ A × A`. Nếu `f ⨾ dup = dup ⨾ f ▵ f` với mọi `f` có hiệu ứng phụ, thì các hiệu ứng là lũy đẳng.

Đọc dữ liệu giao dịch từ môi trường là một hiệu ứng lũy đẳng. Ném ngoại lệ cũng là một hiệu ứng lũy đẳng. Dù chỉ một trong hai biểu thức được nhân đôi sẽ được thực thi, bất kỳ ngoại lệ nào được ném bởi `dup ⨾ f ▵ f` cũng sẽ giống như ngoại lệ được ném bởi `f ⨾ dup`.

Tuy nhiên, ghi vào log có thể không lũy đẳng, vì nhân đôi hiệu ứng sẽ khiến thông điệp log xuất hiện hai lần. Tuy nhiên, nếu log gồm một _tập_ thông điệp thay vì một _danh sách_ thông điệp, thì hiệu ứng sẽ lũy đẳng (và giao hoán) vì việc chèn vào tập tự nó là một thao tác lũy đẳng.

#### Hiệu ứng đơn vị

Một hiệu ứng đơn vị là hiệu ứng mà, nếu bạn bỏ đầu ra của một biểu thức, bạn có thể bỏ an toàn chính biểu thức đó mà không làm thay đổi hiệu ứng của biểu thức. Nếu luôn đúng rằng `f ⨾ unit = unit` với mọi `f` có hiệu ứng phụ, thì các hiệu ứng của bạn là đơn vị.

Đọc dữ liệu từ môi trường là một trong số ít loại hiệu ứng đơn vị. Nếu kết quả đọc dữ liệu giao dịch từ môi trường bị bỏ đi, toàn bộ biểu thức thực hiện việc đọc có thể bị bỏ.

Hiệu ứng failure không đơn vị. Nếu `f` ném một ngoại lệ thì `f ⨾ unit` cũng vậy; việc thực thi thậm chí sẽ không đến được combinator `unit` trước khi phép tính bị hủy. Mặt khác, `unit` rõ ràng sẽ không ném ngoại lệ nào, nên hiệu ứng của `f ⨾ unit` và `unit` sẽ khác nhau.

Tóm lại, đây là cách các hiệu ứng đã thảo luận ở trên đáp ứng ba thuộc tính này:

| Hiệu ứng | Giao hoán | Lũy đẳng | Đơn vị |
| --- | :---: | :---: | :---: |
| Reader (môi trường giao dịch) | ✓ | ✓ | ✓ |
| Failure (ngoại lệ kiểu đơn vị) | ✓ | ✓ | ✗ |
| Writer (log như một tập) | ✓ | ✓ | ✗ |
| Ngoại lệ tổng quát (kiểu tùy ý) | ✗ | ✓ | ✗ |

### Các hiệu ứng được phép trong Simplicity

Một loại hiệu ứng càng có nhiều thuộc tính hành xử tốt, bộ tối ưu hóa Simplicity càng có nhiều không gian để biến đổi các chương trình dùng những hiệu ứng đó. Lý tưởng nhất, chúng ta chỉ cho phép các hiệu ứng có cả ba thuộc tính: giao hoán, lũy đẳng và đơn vị. Điều này sẽ cho phép bộ tối ưu hóa thực hiện bất kỳ loại biến đổi chương trình nào nó muốn. Tuy nhiên, đọc từ môi trường là hiệu ứng duy nhất thỏa mãn cả ba thuộc tính.

Thay vào đó, chúng ta yêu cầu các hiệu ứng Simplicity phải giao hoán và lũy đẳng. Cả hai hiệu ứng chúng ta dùng trong Simplicity, hiệu ứng Failure và hiệu ứng Reader, đều giao hoán và lũy đẳng. Điều này cho phép thực hiện một lớp lớn các tối ưu hóa trên mã Simplicity.

Tuy nhiên, phép biến đổi "discard" mô tả ở trên, cố thay `f ⨾ unit` bằng `unit`, hoặc bất kỳ phép biến đổi tương tự nào, không được phép nếu `f` có thể tạo ra hiệu ứng Failure. Thật vậy, hãy tưởng tượng `f` chứa một assertion `bip0340-verify`. Sẽ là thảm họa nếu cố tối ưu hóa bỏ mất kiểm tra đó.

### Vì sao lại cho phép hiệu ứng phụ?

Vì sao Simplicity lại cho phép hiệu ứng phụ? Chẳng phải sẽ tốt hơn nếu mọi chương trình nhận toàn bộ giao dịch làm đầu vào và trả về một đầu ra Boolean quyết định giao dịch có hợp lệ hay không sao?

#### Xác minh theo batch

Một lý do chúng ta có hiệu ứng Failure là để hỗ trợ [xác minh theo batch](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) cho chữ ký Schnorr. Trong xác minh theo batch, nhiều kiểm tra chữ ký Schnorr riêng lẻ được gom lại với nhau theo cách mà nếu bất kỳ kiểm tra chữ ký đơn lẻ nào thất bại, thì toàn bộ batch thất bại.

Quy trình batching này cải thiện hiệu quả so với việc xác minh từng chữ ký riêng lẻ. Nhược điểm là nếu xác minh batch thất bại, chúng ta không biết kiểm tra chữ ký cụ thể nào đã thất bại.

Bằng cách dùng hiệu ứng phụ failure, `bip0340-verify` đảm bảo rằng nếu kiểm tra chữ ký thất bại, toàn bộ giao dịch thất bại. Nếu `bip0340-verify` thay vào đó trả về `𝟚`, một kiểu Boolean, cho thành công hoặc thất bại, thì một kiểm tra chữ ký thất bại vẫn có thể dẫn đến một nhánh nơi script thành công. Trong trường hợp đó, chúng ta cần biết chữ ký cụ thể có hợp lệ hay không, và vì vậy không thể tận dụng xác minh theo batch.

#### Dữ liệu giao dịch tính trước

Một vấn đề trong Bitcoin Script thời kỳ đầu là hàm băm dùng để tạo message digest cho chữ ký tuyến tính theo kích thước giao dịch. Thông thường mỗi input tạo ít nhất một message digest cho xác minh chữ ký, nên tổng lượng băm là bậc hai theo kích thước giao dịch.

Vấn đề này đã được sửa trong Segwit và các lần lặp sau của Bitcoin Script bằng cách định nghĩa lại các message digest sao cho chúng có thể được tính trong thời gian hằng số cho mỗi kiểm tra chữ ký. Điều này dựa vào việc có `PrecomputedTransactionData`, thứ tính trước các hash của dữ liệu giao dịch một lần rồi được chia sẻ bởi các phép tính sighash của từng input. Các jet băm giao dịch của Simplicity dựa vào cùng loại dữ liệu giao dịch tính trước để đảm bảo jet chạy trong thời gian hằng số.

Giả sử `sig-all-hash` không dùng hiệu ứng Reader. Giả sử bằng cách nào đó chúng ta xây được một kiểu Simplicity cho môi trường giao dịch. Hãy gọi nó là `TxEnv`, sao cho `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` là kiểu của jet. Một định nghĩa như vậy sẽ yêu cầu jet `sig-all-hash` có khả năng tính hash của bất kỳ giao dịch nào, không chỉ giao dịch mà nó tham gia. Các chương trình Simplicity có thể sao chép `TxEnv` đã cho và truyền một bản sao đã sửa đổi của nó vào `sig-all-hash`. Trong trường hợp đó, `sig-all-hash` không thể dựa vào `PrecomputedTransactionData`, và chúng ta sẽ quay lại việc cần thời gian tuyến tính theo bất kỳ dữ liệu giao dịch nào được truyền vào phiên bản này của `sig-all-hash`.

Vì `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` dùng hiệu ứng Reader để truy cập dữ liệu giao dịch, nó _chỉ_ có quyền truy cập vào một môi trường giao dịch cố định. Vì lý do đó, triển khai của jet có thể an toàn dùng `PrecomputedTransactionData` và hoạt động trong thời gian hằng số.

### Cross-Input Signature Aggregation

Dù hiện tại cả Liquid lẫn Bitcoin đều chưa hỗ trợ [cross-input signature aggregation](https://hrf.org/latest/cisa-research-paper/), chúng tôi muốn kiểm tra rằng Simplicity có thể tương thích với nó khi thời điểm đến.

Dù chi tiết chưa được hoàn thiện, chúng tôi hình dung half-aggregation được triển khai bằng một hiệu ứng Writer. Nghĩa là, một jet mới với kiểu như `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` sẽ nhận một public key, message digest và thành phần `r` của chữ ký Schnorr (một chữ ký Schnorr gồm một thành phần `r` và một thành phần `s`) rồi ghi nó vào log giao dịch trước khi tiếp tục thực thi. Sau đó, ở nơi khác trong giao dịch hoặc cùng với giao dịch, một thành phần `s` tổng hợp cho tất cả các chữ ký Schnorr half-aggregated sẽ được cung cấp. Giao dịch chỉ hợp lệ khi một thành phần `s` tổng hợp như vậy được cung cấp cho tất cả các key, message và thành phần `r` đã được ghi log.

Để đáp ứng các yêu cầu của Simplicity, hiệu ứng Writer này cần lũy đẳng và giao hoán. Có thể đảm bảo điều này bằng cách xem log writer như một tập các tuple gồm key, message và thành phần `r`. Điều này hiệu quả vì các thao tác tập là lũy đẳng và giao hoán. Xem log như một tập giá trị sẽ tương thích với thuật toán xác minh half-aggregation.

### Kết luận

Trong chương này, chúng ta đã xem xét việc thêm hiệu ứng phụ vào các phép tính mà Simplicity có thể thực hiện. Chúng ta đã phân loại nhiều loại hiệu ứng theo mức độ hành xử tốt của chúng đối với các loại biến đổi chương trình khác nhau. Chúng ta đã quyết định giới hạn các hiệu ứng của Simplicity ở những hiệu ứng giao hoán và lũy đẳng.

Hai hiệu ứng chúng ta dùng cho các ứng dụng Bitcoin và Liquid là hiệu ứng Reader, để truy cập môi trường giao dịch, và hiệu ứng Failure, để hủy bỏ và làm chương trình thất bại. Một số jet sử dụng các thao tác primitive nơi các loại hiệu ứng phụ này có thể xảy ra.

Hiệu ứng Failure xác định đầu ra của một chương trình Simplicity: chương trình hoặc thất bại, khiến giao dịch không hợp lệ, hoặc chương trình thành công. Hiệu ứng Reader cung cấp một loại đầu vào cho chương trình Simplicity: môi trường chứa dữ liệu giao dịch. Nhưng chúng ta cũng cần cung cấp các đầu vào khác, chẳng hạn chữ ký số, cho chương trình Simplicity.

Trong chương tiếp theo, chúng ta sẽ xem chương trình Simplicity là gì, cách chúng được chuyển thành địa chỉ, và cách chúng ta thêm các đầu vào khác, chẳng hạn chữ ký, vào chương trình Simplicity.

## Chương trình và địa chỉ

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Trong chương trước, chúng ta đã mô tả hai hiệu ứng phụ được dùng trong Simplicity: hiệu ứng Failure, xác định chương trình thành công hay thất bại, và hiệu ứng Reader, cung cấp quyền truy cập vào môi trường giao dịch. Giờ chúng ta chuyển sang câu hỏi thực tế: chính xác thì chương trình Simplicity là gì, và nó trở thành địa chỉ trên blockchain như thế nào?

### Chương trình Simplicity

Một chương trình Simplicity được định nghĩa là một biểu thức Simplicity có kiểu `𝟙 ⊢ 𝟙`. Chữ ký kiểu này nghĩa là chương trình không nhận đầu vào có ý nghĩa (chỉ giá trị đơn vị) và không tạo đầu ra có ý nghĩa (chỉ giá trị đơn vị). Hiệu ứng Reader nắm bắt đầu vào môi trường giao dịch, còn hiệu ứng Failure cho biết thành công hay thất bại. Các hiệu ứng này xử lý I/O thay vì chính các kiểu Simplicity.

### Commitment Merkle Root

Thay vì lưu trữ chương trình hoàn chỉnh on-chain, Bitcoin dùng cam kết — một thực hành mở rộng từ Pay-to-Script-Hash (P2SH). Simplicity dùng Commitment Merkle Root (CMR).

Mỗi combinator nhận một tag SHA-256 suy ra từ mẫu: `Simplicity␟Commitment␟[identifier]`, trong đó `␟` biểu diễn mã ASCII 31 (unit separator).

Mỗi tag là hash SHA-256 của chuỗi pre-image tương ứng liệt kê dưới đây:

| Combinator | Tag pre-image (chuỗi ASCII) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Một biểu thức Simplicity sau đó được băm đệ quy thành một CMR 256 bit bằng cách tính midstate SHA-256 được gắn tag cho mỗi combinator cùng với CMR của các đối số của nó (viết `#ᶜ(e)` cho CMR của biểu thức `e`, và `∥` cho phép nối byte):

| Combinator | Quy tắc CMR |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Các combinator nhị phân (`comp`, `pair`, `case`) nối CMR của cả hai con; các combinator đơn ngôi (`take`, `drop`, `injl`, `injr`) nối CMR của một con duy nhất sau 32 byte padding `0x00`; và các lá không ngôi (`iden`, `unit`) băm riêng tag của chúng. Hai quy ước giữ việc này rẻ để tính toán: các midstate SHA-256 được dùng để **mỗi biểu thức cần nhiều nhất một lần gọi hàm nén SHA-256** (giả sử midstate đến các tag hằng đã được tính trước), và các constructor một đối số thêm tiền tố cho đối số bằng 32 byte padding `0x00`, cho phép thêm một chút tiền tính toán cho các triển khai muốn dùng.

Đối với combinator `unit` — một constructor không ngôi không có biểu thức con làm đối số — quy tắc này chuyên biệt thành `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, trong đó `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tag được đưa vào hai lần). CMR kết quả cho chương trình `unit` tầm thường là:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Điều quan trọng là CMR không cam kết với các kiểu của biểu thức Simplicity, mà thay vào đó dựa vào suy luận kiểu trong quá trình chi tiêu.

### Địa chỉ

Địa chỉ sử dụng cơ chế Taproot của BIP-0341 với các CMR được cam kết dưới TapLeaf version `0xbe`. Quy trình gồm:

1. Tính một TapLeaf tagged hash kết hợp byte version, độ dài CMR và chính CMR
2. Tweak một public key nội bộ (dùng điểm NUMS khi không muốn có đường key-spend)
3. Chuyển đổi sang định dạng bech32m
4. Thêm các checksum thích hợp

Khi không muốn có đường key-spend, public key nội bộ được đặt thành một điểm **NUMS** ("Nothing-Up-My-Sleeve"): một điểm trên đường cong được chọn có chủ ý sao cho không ai biết logarithm rời rạc của nó — nói cách khác, một điểm không có private key tương ứng. Vì không ai có thể tạo chữ ký cho nó, đường key-spend được chứng minh là không thể sử dụng, và output chỉ có thể được chi tiêu *thông qua* đường script Simplicity đã cam kết. Trong ứng dụng thực tế, điểm NUMS này nên được ngẫu nhiên hóa như BIP-0341 khuyến nghị, để các output không có đường key-spend không thể phân biệt với các output Taproot thông thường (một lợi ích về quyền riêng tư).

#### Từ Simplicity đến địa chỉ

Hãy đi qua toàn bộ phép suy dẫn cho chương trình đơn giản nhất có thể: `unit : 𝟙 ⊢ 𝟙`, một no-op luôn thành công.

**1. Tag combinator.** Trước hết tính tag `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Đưa tag vào hai lần để thu được CMR của chương trình:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf hash.** Thêm tiền tố cho CMR bằng TapLeaf version `0xbe` của Simplicity và độ dài CMR `0x20` (32 byte), rồi lấy Elements TapLeaf tagged hash (tagged hash là `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Chỉ có một leaf này nên không có TapBranch, vì vậy hash này đã là gốc TapTree.

**4. TapTweak.** Vì chúng ta không muốn đường key-spend, ta dùng điểm NUMS BIP-0341 làm key nội bộ và tweak nó bằng gốc TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Output key.** Tweak key nội bộ trên đường cong, `output_pk = lift_x(internal_pk) ⊕ t·G` (số học đường cong elliptic được tóm tắt ở đây), cho ra output key x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Địa chỉ Bech32m.** Mã hóa output key x-only, thêm tiền tố `p` (ký tự witness-version SegWit v1), thêm tiền tố human-readable của Liquid-testnet `tex1`, và nối checksum Bech32m. Địa chỉ cuối cùng là:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Đó là rất nhiều việc — nhưng phần lớn là do chính Taproot bắt buộc, không phải do Simplicity.

### Biểu thức witness

Một loại combinator mới xử lý việc chương trình Simplicity không có đầu vào: biểu thức witness. Combinator `witness` cho phép dữ liệu chữ ký và các vật liệu witness khác được tích hợp vào chương trình.

```
      w : B
-----------------
witness w : A ⊢ B
```

Ngữ nghĩa của biểu thức witness rất đơn giản: nó bỏ qua đầu vào và chỉ trả về giá trị `w` (có thể thuộc bất kỳ kiểu Simplicity nào), tức là `⟦witness w⟧(a) = w`. Điều này **không thêm năng lực biểu đạt mới** — theo định lý đầy đủ, Simplicity đã có thể xây mọi hàm hằng như vậy (nhớ lại macro `scribe` từ các chương trước). Điểm mấu chốt của combinator `witness` nằm hoàn toàn ở **CMR** của nó: giá trị `w` được **loại trừ** khỏi CMR của biểu thức, nên địa chỉ có thể được tính trước khi biết `w`, và `w` được cung cấp tại thời điểm chi tiêu.

Lựa chọn thiết kế này hỗ trợ pruning — các nhánh điều kiện không được thực thi không cần được tiết lộ on-chain, bao gồm cả các biểu thức witness liên quan của chúng. Khi một nhánh bị prune, verifier chỉ cần CMR của subtree bị prune, không cần nội dung thực tế của nó.

### Giá trị witness

Có thể có vẻ như là một hạn chế khi biểu thức witness chỉ có thể giữ một *giá trị*, chứ không phải một biểu thức Simplicity tổng quát hơn. Nhưng chương trình cho blockchain dựa trên UTXO chỉ được thực thi một lần. Không cần truyền cả một biểu thức con vào một node witness: người dùng có thể đơn giản tự chạy biểu thức con đó off-chain, và chép đầu ra của nó vào giá trị witness để thu được cùng một kết quả.

(Sau này trong khóa học này, chúng ta sẽ gặp combinator `disconnect`, hoạt động khá giống một biểu thức witness mà *có* nhận toàn bộ một biểu thức Simplicity làm đối số.)

Một thiết kế thay thế sẽ đưa toàn bộ dữ liệu witness vào như một đối số cho chương trình Simplicity cấp cao nhất. Biểu thức witness được ưu tiên vì hai lý do. Thứ nhất, **pruning**: các nhánh không được thực thi của biểu thức `case` không bao giờ được tiết lộ on-chain, và mọi biểu thức witness bên trong các nhánh đó bị prune cùng với chúng. Thứ hai, **tính cục bộ**: biểu thức witness cho phép chúng ta đặt từng giá trị witness đúng nơi nó được dùng, thay vì luồn nó xuống từ đầu vào cấp cao nhất của chương trình.

### Suy luận kiểu

Vì CMR không cam kết với kiểu, hệ thống kiểu được tái dựng trong quá trình chi tiêu. Thuật toán suy luận kiểu của Simplicity xác định các kiểu tối thiểu cho từng biểu thức con dựa trên cấu trúc combinator. Chính xác hơn, suy luận tính kiểu *principal* (tổng quát nhất) của mọi biểu thức con; mọi biến kiểu còn tự do sau đó được khởi tạo thành kiểu đơn vị `𝟙`, tạo ra một kiểu duy nhất, tối thiểu cho chương trình.

### Kết luận

Trong chương này, chúng ta đã xác lập rằng chương trình Simplicity là các biểu thức có kiểu `𝟙 ⊢ 𝟙`, giải thích cách Commitment Merkle Root được xây dựng từ các hash SHA-256 được gắn tag của từng combinator, và chỉ ra cách CMR được chuyển thành địa chỉ on-chain thông qua Taproot BIP-0341. Chúng ta đã giới thiệu biểu thức witness như cơ chế để cung cấp dữ liệu chữ ký và các đầu vào khác tại thời điểm chi tiêu mà không cam kết với giá trị của chúng tại thời điểm tạo địa chỉ.

# Phần cuối

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Đánh giá & Xếp hạng

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Bài thi cuối khóa

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Kết luận

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
