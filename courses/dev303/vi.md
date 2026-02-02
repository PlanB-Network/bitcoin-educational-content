---
name: Học Rust với Bitcoin
goal: Nâng cao kỹ năng lập trình Rust của bạn thông qua lập trình Bitcoin.
objectives: 

  - Hãy làm quen với ngôn ngữ của Rust.
  - Hiểu lý do tại sao nên sử dụng Rust để phát triển Bitcoin.
  - Nắm vững kiến thức cơ bản về Lightning SDK

---

# Chuyến thám hiểm Rust dành cho những người chế tạo Bitcoin



Trong khóa học thực hành này, được quay phim trong một hội thảo do Fulgur' Ventures tổ chức vào tháng 10 năm 2023, bạn sẽ phát triển các kỹ năng Rust của mình bằng cách xây dựng các thành phần và dự án nhỏ thực tế tập trung vào Bitcoin. Chúng ta sẽ tìm hiểu về các nguyên tắc cơ bản của Rust, lý do tại sao Rust được sử dụng cho việc phát triển Bitcoin (an toàn bộ nhớ, hiệu suất và khả năng xử lý đồng thời an toàn), và cách bắt đầu với Lightning SDK để xây dựng các tính năng thanh toán.


Xuyên suốt các chương, bạn sẽ thực hành các mẫu cốt lõi của Rust (quyền sở hữu, vòng đời, đặc tính, bất đồng bộ), làm việc với các thành phần cơ bản của Bitcoin (khóa, giao dịch, kịch bản) và dần dần tích hợp các khái niệm Lightning (các nút, kênh, hóa đơn).


Không yêu cầu kinh nghiệm phát triển Rust hoặc Bitcoin trước đó, mặc dù quen thuộc với lập trình cơ bản sẽ hữu ích. Khóa học thân thiện với người mới bắt đầu nhưng vẫn đủ thực tế cho các kỹ sư chuyển sang sử dụng Bitcoin.


+++

# Giới thiệu

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Tổng quan khóa học

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Giới thiệu**


Chào mừng bạn đến với khóa học lập trình SDK dành cho người mới bắt đầu. Trong khóa đào tạo này, bạn sẽ học những kiến thức cơ bản về Rust, sau đó tập trung vào việc ứng dụng Rust vào lập trình Bitcoin, và kết thúc bằng một số trường hợp sử dụng SDK.


Các video về khóa đào tạo hiện chỉ có sẵn bằng tiếng Anh và là một phần của hội thảo trực tuyến được tổ chức vào tháng 10 năm ngoái tại Tuscany bởi Fulgure Venture. Khóa đào tạo này sẽ chỉ tập trung vào tuần đầu tiên. Phần thứ hai dành cho RGB và có thể được tìm thấy trong khóa học RGB.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Khóa đào tạo này mang đến cho bạn cơ hội phát triển kỹ năng lập trình trên Lightning Network bằng cách sử dụng Rust và nhiều SDK khác nhau. Khóa học được thiết kế dành cho các nhà phát triển có nền tảng lập trình vững chắc muốn tìm hiểu sâu hơn về lập trình dành riêng cho Lightning Network. Bạn sẽ học những kiến thức cơ bản về Rust, lý do tại sao nó phù hợp cho việc phát triển Bitcoin, và sau đó chuyển sang thực hành trực tiếp bằng cách sử dụng các SDK chuyên dụng.


**Phần 2: Học lập trình với Rust**

Trong phần này, bạn sẽ khám phá những kiến thức cơ bản về Rust thông qua một loạt các chương được trình bày theo trình tự tăng dần. Bạn sẽ học cách viết mã Rust, hiểu rõ các đặc điểm riêng của nó và nắm vững các tính năng thiết yếu qua bảy phần chi tiết. Mô-đun này rất cần thiết để hiểu tại sao Rust lại là ngôn ngữ được ưa chuộng trong phát triển Bitcoin.


**Phần 3: Rust & Bitcoin**

Tại đây, chúng ta sẽ tìm hiểu sâu sắc lý do tại sao Rust là một lựa chọn phù hợp cho việc phát triển Bitcoin. Bạn sẽ tìm hiểu về mô hình lỗi của nó, công cụ UniFFI và các đặc tính bất đồng bộ – tất cả đều là những yếu tố quan trọng trong việc xây dựng phần mềm mạnh mẽ và an toàn.


**Phần 4: Phát triển LNP/BP với SDK**

Bạn sẽ học cách phát triển các node LN bằng nhiều SDK khác nhau như Breez SDK và Greenlight cho Lipa. Bạn sẽ thấy cách triển khai các ứng dụng Lightning Network bằng cách sử dụng các thư viện được thiết kế để đơn giản hóa việc phát triển Bitcoin và Lightning.


Bạn đã sẵn sàng nâng cao kỹ năng Lightning Network của mình với Rust chưa? Cùng bắt đầu nào!

# Hãy học lập trình với cuốn sách Rust.

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Giới thiệu về Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Cài đặt và quản lý Rust bằng Rustup


Khi bắt đầu hành trình với Rust, bước đầu tiên là thiết lập một môi trường phát triển phù hợp. Phương pháp được khuyến nghị rộng rãi nhất để cài đặt Rust là thông qua Rustup, một hệ thống quản lý chuỗi công cụ xử lý việc cài đặt và cập nhật trên nhiều dự án và nền tảng khác nhau.


Rustup không chỉ đơn thuần là một trình cài đặt mà còn là một công cụ quản lý toàn diện cho môi trường phát triển Rust của bạn. Với Rustup, bạn có thể dễ dàng cài đặt thêm các mục tiêu biên dịch cho các nền tảng khác nhau, chẳng hạn như ARM64 cho phát triển Android hoặc các kiến trúc khác mà bạn cần hỗ trợ. Công cụ này cũng xử lý các bản cập nhật Rust một cách liền mạch, điều này đặc biệt có giá trị vì Rust phát hành một phiên bản ổn định mới khoảng sáu tuần một lần. Khi bạn cần cập nhật lên phiên bản mới nhất, chỉ cần lệnh `rustup update` đơn giản sẽ xử lý mọi thứ tự động.


Khi cài đặt Rustup, điều đáng lưu ý là mô hình bảo mật liên quan. Quá trình cài đặt tải xuống và thực thi một tập lệnh từ trang web chính thức của Rust qua HTTPS, cung cấp bảo mật mã hóa ở lớp vận chuyển. Các gói được tải xuống bởi Rustup và Cargo đến từ các nguồn đáng tin cậy (crates.io và cơ sở hạ tầng chính thức của Rust) và được hưởng lợi từ mã hóa HTTPS. Mặc dù phương pháp này an toàn cho hầu hết các trường hợp phát triển, một số tổ chức có chính sách bảo mật nghiêm ngặt có thể thích cài đặt Rust thông qua trình quản lý gói của bản phân phối Linux của họ, cung cấp thêm một lớp tin cậy thông qua cơ sở hạ tầng ký gói riêng của bản phân phối. Đối với mục đích học tập và phát triển nói chung, Rustup là một công cụ đã được khẳng định và được tin cậy rộng rãi trong hệ sinh thái Rust.


Đối với hầu hết các trường hợp phát triển, bạn có thể cài đặt Rustup bằng cách chạy tập lệnh cài đặt được cung cấp trên trang web chính thức của Rust. Trình cài đặt sẽ yêu cầu bạn chọn giữa các tùy chọn bộ công cụ khác nhau, trong đó bộ công cụ ổn định là lựa chọn được khuyến nghị cho hầu hết người dùng. Quá trình cài đặt diễn ra trong thư mục chính của bạn, không yêu cầu quyền quản trị viên và thiết lập tất cả các biến môi trường cần thiết để sử dụng ngay lập tức.


### Tìm hiểu về các chuỗi công cụ và thành phần của Rust


Hệ sinh thái phát triển của Rust bao gồm một số thành phần quan trọng hoạt động cùng nhau để cung cấp một môi trường lập trình hoàn chỉnh. Hiểu rõ các thành phần này giúp bạn điều hướng quy trình phát triển Rust hiệu quả hơn và khắc phục sự cố khi chúng phát sinh.


Trình biên dịch Rust, được gọi là `rustc`, tạo thành cốt lõi của bộ công cụ Rust. Mặc dù về mặt lý thuyết, bạn có thể sử dụng `rustc` trực tiếp để biên dịch các chương trình Rust, nhưng hầu hết công việc phát triển đều dựa vào Cargo, trình quản lý gói và hệ thống xây dựng của Rust. Cargo hoạt động tương tự như npm trong hệ sinh thái JavaScript, quản lý các phụ thuộc, điều phối quá trình xây dựng và cung cấp các lệnh tiện lợi cho các tác vụ phát triển thông thường. Khi bạn chạy các lệnh như `cargo build` hoặc `cargo run`, Cargo sẽ điều phối quá trình biên dịch, xử lý việc giải quyết các phụ thuộc và quản lý cấu trúc tổng thể của dự án.


Clippy là một công cụ kiểm tra cú pháp (linter) phân tích mã nguồn của bạn và đưa ra các đề xuất cải tiến. Không giống như các công cụ kiểm tra cú pháp cơ bản, Clippy hiểu các quy tắc Rust và có thể đề xuất các cách thức chuẩn mực hơn để thực hiện các tác vụ cụ thể. Công cụ này giúp bạn học hỏi các thực tiễn tốt nhất của Rust và viết mã dễ bảo trì hơn.


Bộ công cụ Rust cũng bao gồm các công cụ tài liệu toàn diện và tài liệu thư viện chuẩn, có thể truy cập thông qua trang web tài liệu chính thức của Rust. Tài liệu này đóng vai trò là tài liệu tham khảo không thể thiếu trong quá trình phát triển, cung cấp thông tin chi tiết về các hàm, kiểu và mô-đun của thư viện chuẩn. Tài liệu bao gồm nhiều ví dụ và giải thích giúp bạn hiểu không chỉ chức năng của các hàm mà còn cả cách sử dụng chúng hiệu quả trong chương trình của mình.


Rust hỗ trợ nhiều kênh phát hành: ổn định, beta và nightly. Kênh ổn định cung cấp các bản phát hành đã được kiểm thử kỹ lưỡng, phù hợp cho mục đích sử dụng trong môi trường sản xuất. Kênh beta cung cấp bản xem trước của bản phát hành ổn định tiếp theo, chủ yếu được sử dụng để kiểm tra cuối cùng trước khi phát hành chính thức. Kênh nightly bao gồm các tính năng thử nghiệm đang được phát triển tích cực, có thể hữu ích để thử nghiệm các khả năng mới của Rust, mặc dù các tính năng này có thể thay đổi hoặc bị loại bỏ trong các bản phát hành tương lai.


### Tạo và quản lý các dự án Rust với Cargo


Quá trình phát triển Rust hiện đại tập trung vào Cargo, giúp đơn giản hóa việc tạo dự án, quản lý phụ thuộc và quy trình xây dựng. Thay vì phải tạo thủ công các thư mục và tập tin, Cargo cung cấp cho generate một cấu trúc dự án hoàn chỉnh với các thiết lập mặc định hợp lý thông qua lệnh `cargo new`.


Khi bạn tạo một dự án mới bằng lệnh `cargo new project_name`, Cargo sẽ thiết lập cấu trúc thư mục chuẩn, tạo một tệp `main.rs` cơ bản với chương trình "Hello, world!", khởi tạo kho lưu trữ Git và tạo tệp `Cargo.toml` để cấu hình dự án. Tệp `Cargo.toml` đóng vai trò là điểm cấu hình trung tâm cho dự án của bạn, chứa siêu dữ liệu về dự án và liệt kê tất cả các phụ thuộc mà mã của bạn yêu cầu.


Cargo cung cấp một số lệnh thiết yếu cho công việc phát triển hàng ngày. Lệnh `cargo build` biên dịch dự án và các phụ thuộc của nó, tạo ra các tệp thực thi trong thư mục `target`. Để lặp lại nhanh chóng trong quá trình phát triển, lệnh `cargo run` kết hợp việc biên dịch và thực thi trong một bước duy nhất. Lệnh `cargo check` thực hiện tất cả các kiểm tra biên dịch mà không tạo ra tệp thực thi cuối cùng, giúp nó nhanh hơn đáng kể so với việc biên dịch toàn bộ khi bạn chỉ muốn xác minh rằng mã của mình được biên dịch chính xác.


Khi chuẩn bị mã để triển khai sản phẩm, cờ `--release` cho phép tối ưu hóa và loại bỏ các khẳng định gỡ lỗi. Bản dựng phát hành chạy nhanh hơn và tạo ra các tệp thực thi nhỏ hơn, nhưng mất nhiều thời gian hơn để biên dịch và loại bỏ thông tin gỡ lỗi hữu ích. Trình biên dịch áp dụng nhiều tối ưu hóa trong quá trình xây dựng bản phát hành và vô hiệu hóa các kiểm tra thời gian chạy như phát hiện tràn số nguyên, điều này cải thiện hiệu suất nhưng loại bỏ một số đảm bảo an toàn có trong bản dựng gỡ lỗi.


### Các biến số, tính khả biến và triết lý an toàn của Rust


Rust có cách tiếp cận khác biệt so với hầu hết các ngôn ngữ khác trong việc quản lý biến. Theo mặc định, tất cả các biến trong Rust đều bất biến, nghĩa là giá trị của chúng không thể thay đổi sau khi được gán giá trị ban đầu. Quyết định thiết kế này nhằm mục đích ngăn ngừa các lỗi lập trình phổ biến phát sinh từ những thay đổi trạng thái không mong muốn.


Khi bạn khai báo một biến bằng `let x = 5`, biến đó sẽ trở nên bất biến theo mặc định. Bất kỳ nỗ lực nào để sửa đổi giá trị của nó sau này sẽ dẫn đến lỗi biên dịch. Yêu cầu bất biến này buộc các nhà phát triển phải suy nghĩ cẩn thận về thời điểm thực sự cần thay đổi trạng thái và làm cho hành vi của mã dễ dự đoán hơn. Nhiều lỗi lập trình bắt nguồn từ việc các biến thay đổi một cách bất ngờ, và tính bất biến mặc định của Rust giúp ngăn ngừa những vấn đề này.


Khi thực sự cần sửa đổi giá trị của một biến, Rust yêu cầu khai báo rõ ràng khả năng thay đổi bằng từ khóa `mut`: `let mut x = 5`. Khai báo rõ ràng này đóng vai trò là tín hiệu rõ ràng cho cả trình biên dịch và các nhà phát triển khác rằng giá trị của biến này có thể thay đổi trong quá trình thực thi chương trình. Yêu cầu khai báo rõ ràng khả năng thay đổi khuyến khích việc cân nhắc kỹ lưỡng xem khả năng thay đổi có thực sự cần thiết cho từng biến hay không.


Rust cũng hỗ trợ kỹ thuật "shadowing" (che khuất biến), cho phép bạn khai báo một biến mới có cùng tên với biến trước đó. Không giống như thao tác thay đổi biến (mutation), "shadowing" tạo ra một biến hoàn toàn mới nhưng lại có cùng tên, giúp che giấu biến trước đó. Kỹ thuật này đặc biệt hữu ích khi chuyển đổi dữ liệu qua nhiều bước, chẳng hạn như phân tích chuỗi thành số và sau đó xử lý số đó thêm nữa. Với "shadowing", bạn có thể duy trì tên biến nhất quán trong suốt quá trình chuyển đổi trong khi thay đổi kiểu dữ liệu của biến ở mỗi bước.


Sự khác biệt giữa việc tạo biến mới (shadowing) và thay đổi kiểu dữ liệu (mutation) trở nên quan trọng khi xem xét các thay đổi về kiểu dữ liệu. Với việc tạo biến mới, bạn có thể thay đổi cả giá trị và kiểu dữ liệu của một biến vì bạn đang tạo một biến mới. Với việc thay đổi kiểu dữ liệu, bạn chỉ có thể thay đổi giá trị trong khi vẫn giữ nguyên kiểu dữ liệu, vì bạn đang sửa đổi một biến hiện có chứ không phải tạo một biến mới.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Các kiểu dữ liệu và nguyên tắc cơ bản của hệ thống kiểu dữ liệu


Rust triển khai một hệ thống kiểu dữ liệu tĩnh mạnh mẽ, trong đó mọi giá trị phải có một kiểu dữ liệu được xác định rõ ràng tại thời điểm biên dịch. Mặc dù điều này có vẻ hạn chế so với các ngôn ngữ kiểu động, nhưng khả năng suy luận kiểu dữ liệu của Rust có nghĩa là bạn hiếm khi cần phải chỉ định kiểu dữ liệu một cách rõ ràng. Trình biên dịch thường có thể xác định kiểu dữ liệu phù hợp dựa trên cách bạn sử dụng giá trị đó.


Tuy nhiên, một số trường hợp yêu cầu chú thích kiểu dữ liệu rõ ràng. Khi sử dụng các hàm chung như `parse()`, có thể chuyển đổi chuỗi thành nhiều kiểu số khác nhau, trình biên dịch cần biết bạn muốn kiểu dữ liệu cụ thể nào. Trong những trường hợp này, bạn cung cấp chú thích kiểu dữ liệu bằng cú pháp dấu hai chấm: `let guess: u32 = "42".parse().expect("Not a number!")`.


Các kiểu dữ liệu vô hướng của Rust bao gồm số nguyên, số thực, boolean và ký tự. Hệ thống kiểu số nguyên cung cấp khả năng kiểm soát chính xác việc sử dụng bộ nhớ và các đặc tính hiệu năng. Các kiểu số nguyên được đặt tên một cách có hệ thống: `i8`, `i16`, `i32`, `i64` và `i128` cho số nguyên có dấu, và `u8`, `u16`, `u32`, `u64` và `u128` cho số nguyên không dấu. Các con số biểu thị độ rộng bit, giúp việc sử dụng bộ nhớ và phạm vi giá trị trở nên rõ ràng ngay lập tức.


Các kiểu dữ liệu `isize` và `usize` cần được chú ý đặc biệt vì chúng thích ứng với kiến trúc mục tiêu của bạn. Trên hệ thống 64-bit, các kiểu dữ liệu này có độ rộng 64 bit, trong khi trên hệ thống 32-bit, chúng có độ rộng 32 bit. Các kiểu dữ liệu này thường được sử dụng cho việc lập chỉ mục mảng và bù trừ bộ nhớ vì chúng phù hợp với kích thước từ tự nhiên của kiến trúc mục tiêu, cho phép thực hiện các phép toán con trỏ và thao tác bộ nhớ hiệu quả.


Rust cung cấp nhiều cách để viết các hằng số nguyên, bao gồm định dạng thập phân, thập lục phân (`0x`), bát phân (`0o`) và nhị phân (`0b`). Bạn cũng có thể sử dụng dấu gạch dưới ở bất kỳ đâu trong các hằng số số để cải thiện khả năng đọc, chẳng hạn như viết `1_000_000` thay vì `1000000`. Dấu gạch dưới không ảnh hưởng đến giá trị nhưng có thể làm cho các số lớn dễ đọc hơn.


Các kiểu dữ liệu dấu phẩy động trong Rust khá đơn giản: `f32` cho số dấu phẩy động đơn chính xác và `f64` cho số dấu phẩy động kép chính xác. Kiểu `f64` thường được ưu tiên hơn do độ chính xác cao hơn và thực tế là các bộ xử lý hiện đại thường có thể xử lý các phép toán dấu phẩy động 64 bit hiệu quả như các phép toán 32 bit.


### Các kiểu dữ liệu phức hợp và tổ chức dữ liệu


Ngoài các kiểu dữ liệu vô hướng, Rust còn cung cấp các kiểu dữ liệu phức hợp nhóm nhiều giá trị lại với nhau. Bộ dữ liệu (tuple) cho phép bạn kết hợp các giá trị thuộc các kiểu khác nhau thành một giá trị phức hợp duy nhất. Bạn tạo bộ dữ liệu bằng cách sử dụng dấu ngoặc đơn và có thể chỉ định kiểu của từng phần tử: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


Bộ dữ liệu (tuple) hỗ trợ phân rã (destructuring), cho phép bạn trích xuất các giá trị riêng lẻ: `let (x, y, z) = tup`. Cú pháp này tạo ra ba biến riêng biệt từ các thành phần của bộ dữ liệu. Ngoài ra, bạn có thể truy cập trực tiếp các phần tử của bộ dữ liệu bằng cách sử dụng ký hiệu dấu chấm với chỉ số phần tử: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Mảng trong Rust khác biệt đáng kể so với mảng hoặc danh sách trong nhiều ngôn ngữ khác vì chúng có kích thước cố định, kích thước này trở thành một phần của kiểu dữ liệu. Một mảng gồm năm số nguyên có kiểu `[i32; 5]`, trong đó dấu chấm phẩy phân tách kiểu phần tử với độ dài của mảng. Thông tin về kích thước ở cấp độ kiểu dữ liệu này cho phép trình biên dịch thực hiện kiểm tra giới hạn và đảm bảo rằng các hàm nhận mảng biết chính xác số lượng phần tử cần nhận.


Bạn có thể khởi tạo mảng bằng cách liệt kê tất cả các phần tử một cách rõ ràng: `[1, 2, 3, 4, 5]`, hoặc bằng cách sử dụng cú pháp viết tắt cho mảng có các giá trị lặp lại: `[3; 5]` tạo ra một mảng gồm năm phần tử, tất cả đều có giá trị là 3. Cú pháp viết tắt này hữu ích để khởi tạo bộ đệm hoặc tạo mảng với các giá trị mặc định.


Việc truy cập mảng sử dụng cú pháp ngoặc vuông giống như hầu hết các ngôn ngữ khác, nhưng Rust cung cấp cả kiểm tra giới hạn tại thời điểm biên dịch và thời điểm chạy. Khi bạn truy cập một mảng với chỉ số cố định mà trình biên dịch có thể xác minh, nó sẽ phát hiện lỗi truy cập vượt quá giới hạn tại thời điểm biên dịch. Đối với các chỉ số động được xác định tại thời điểm chạy, Rust sẽ chèn các kiểm tra giới hạn khiến chương trình bị lỗi nếu bạn cố gắng truy cập một chỉ số không hợp lệ, ngăn ngừa các vi phạm an toàn bộ nhớ.



## Ownership và tính an toàn bộ nhớ trong Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Hiểu rõ cách tiếp cận độc đáo của Rust đối với quản lý bộ nhớ.


Chương này đề cập đến một trong những khái niệm quan trọng nhất của Rust. Mặc dù các khái niệm trước đó có thể quen thuộc với các lập trình viên đến từ các ngôn ngữ khác, nhưng quyền sở hữu là cách tiếp cận của Rust để giải quyết vấn đề an toàn bộ nhớ mà không cần đến cơ chế thu gom rác tự động.


Rust được thiết kế với mục tiêu cơ bản là ngăn ngừa các lỗi liên quan đến bộ nhớ thường gặp trong các ngôn ngữ cấp thấp như C và C++. Những vấn đề này bao gồm lỗi sử dụng sau khi giải phóng (use-after-free), trong đó bộ nhớ được truy cập sau khi đã được giải phóng, và lỗi tràn bộ đệm (buffer overflow), trong đó chương trình ghi dữ liệu ra ngoài phạm vi bộ nhớ đã được cấp phát. Các giải pháp truyền thống cho những vấn đề này thường liên quan đến những sự đánh đổi mà Rust hướng đến việc loại bỏ. Các ngôn ngữ cấp cao hơn như Java và Go giải quyết vấn đề an toàn bộ nhớ thông qua cơ chế thu gom rác (garbage collection), trong đó một quy trình tự động định kỳ xác định và giải phóng bộ nhớ không sử dụng. Tuy nhiên, cơ chế thu gom rác gây ra sự hao phí hiệu năng và có thể gây ra những gián đoạn không thể đoán trước trong quá trình thực thi chương trình, khiến chúng không phù hợp với lập trình hệ thống, nơi hiệu năng ổn định là rất quan trọng.


Rust đạt được tính an toàn bộ nhớ chủ yếu thông qua phân tích tĩnh được thực hiện tại thời điểm biên dịch. Trình biên dịch kiểm tra mã nguồn và có thể xác định xem hầu hết các thao tác bộ nhớ có an toàn hay không mà không cần đến quá trình thu gom rác. Đối với các trường hợp không thể xác minh tĩnh—chẳng hạn như truy cập mảng với các chỉ số được tính toán trong thời gian chạy—Rust chèn các kiểm tra giới hạn gây ra lỗi nghiêm trọng (panic) thay vì cho phép hành vi không xác định. Cách tiếp cận này khác biệt về cơ bản so với các trình phân tích tĩnh hiện có cho C và C++, vốn được tích hợp thêm vào các ngôn ngữ ban đầu không được thiết kế cho phân tích tĩnh toàn diện. Cú pháp và các quy tắc ngôn ngữ của Rust được xây dựng từ đầu để cho phép xác minh rộng rãi tại thời điểm biên dịch, đảm bảo rằng một khi chương trình được biên dịch thành công, nó sẽ chạy an toàn hoặc gây ra lỗi nghiêm trọng (panic) một cách có thể dự đoán được thay vì thể hiện hành vi không xác định.


### Hệ thống Ownership: Các quy tắc và nguyên tắc


Nền tảng của các đảm bảo an toàn bộ nhớ của Rust là hệ thống sở hữu, điều chỉnh cách quản lý bộ nhớ trong suốt quá trình thực thi chương trình. Ownership hoạt động dựa trên ba quy tắc cơ bản mà trình biên dịch luôn thực thi:


1. Mỗi giá trị trong Rust đều có một chủ sở hữu (một biến lưu trữ giá trị đó).

2. Chỉ có thể có một chủ sở hữu tại một thời điểm.

3. Khi chủ sở hữu không còn nằm trong phạm vi quản lý, giá trị sẽ bị mất.


Trong Rust, phạm vi thường được định nghĩa bằng dấu ngoặc nhọn, cho dù trong thân hàm, khối điều kiện hay khối phạm vi được tạo rõ ràng. Khi một biến được khai báo trong một phạm vi, phạm vi đó trở thành chủ sở hữu của giá trị biến. Biến vẫn có thể truy cập và hợp lệ trong suốt vòng đời của phạm vi, nhưng ngay khi quá trình thực thi rời khỏi phạm vi, tất cả các biến thuộc sở hữu sẽ tự động được dọn dẹp thông qua một quá trình gọi là "dropping".


Việc dọn dẹp tự động này được thực hiện thông qua cơ chế loại bỏ (drop) của Rust, trong đó ngôn ngữ tự động gọi một hàm loại bỏ trên các biến nằm ngoài phạm vi. Đối với các kiểu dữ liệu cơ bản, điều này đơn giản có nghĩa là vùng nhớ được đánh dấu là có thể tái sử dụng. Đối với các kiểu dữ liệu phức tạp hơn quản lý tài nguyên, các triển khai loại bỏ tùy chỉnh có thể thực hiện các thao tác dọn dẹp bổ sung, chẳng hạn như đóng các file handle hoặc giải phóng các kết nối mạng. Mô hình này, được mượn từ RAII (Resource Acquisition Is Initialization) của C++, đảm bảo rằng các tài nguyên luôn được giải phóng đúng cách mà không cần lập trình viên phải viết mã dọn dẹp rõ ràng.


### Di chuyển Ownership và bố trí bộ nhớ


Để hiểu cách chuyển giao quyền sở hữu giữa các biến, cần phải xem xét sự khác biệt giữa các kiểu dữ liệu đơn giản và phức tạp về bố cục bộ nhớ và hành vi sao chép. Các kiểu dữ liệu đơn giản như số nguyên, boolean và số thực có kích thước cố định, đã biết tại thời điểm biên dịch và có thể được sao chép hiệu quả. Khi bạn gán một biến số nguyên cho một biến số nguyên khác, Rust tạo ra một bản sao hoàn chỉnh, độc lập của giá trị, cho phép cả hai biến tồn tại đồng thời mà không cần lo lắng về quyền sở hữu.


Các kiểu dữ liệu phức tạp như chuỗi ký tự đặt ra một thách thức khác vì chúng quản lý bộ nhớ được cấp phát động. Một chuỗi ký tự trong Rust bao gồm ba thành phần được lưu trữ trên ngăn xếp: một con trỏ đến dữ liệu ký tự được cấp phát trên heap, độ dài hiện tại của chuỗi và tổng dung lượng của bộ đệm được cấp phát. Cấu trúc này cho phép các chuỗi ký tự tăng và giảm một cách hiệu quả trong khi vẫn duy trì thông tin về ranh giới của chúng. Khi bạn gán một biến chuỗi ký tự cho một biến chuỗi ký tự khác, Rust phải đối mặt với một lựa chọn: nó có thể chỉ sao chép cấu trúc dựa trên ngăn xếp (tạo ra hai con trỏ đến cùng một dữ liệu trên heap) hoặc thực hiện sao chép sâu toàn bộ dữ liệu trên heap.


Hành vi mặc định của Rust là di chuyển quyền sở hữu thay vì sao chép, chuyển dữ liệu vùng nhớ heap từ biến nguồn sang biến đích và vô hiệu hóa biến nguồn. Cách tiếp cận này ngăn chặn tình huống nguy hiểm khi nhiều biến có thể sửa đổi cùng một vùng nhớ heap hoặc khi cùng một vùng nhớ có thể được giải phóng nhiều lần khi các biến nằm ngoài phạm vi. Thao tác di chuyển hiệu quả vì nó chỉ sao chép cấu trúc nhỏ dựa trên ngăn xếp, chứ không phải dữ liệu heap có thể lớn, đồng thời duy trì tính an toàn bộ nhớ bằng cách đảm bảo quyền sở hữu duy nhất.


### Tài liệu tham khảo và mượn nguồn


Mặc dù việc chuyển quyền sở hữu mang lại sự an toàn, nhưng nó có thể gây hạn chế khi bạn cần sử dụng một giá trị ở nhiều nơi mà không cần chuyển quyền sở hữu. Rust giải quyết vấn đề này thông qua việc mượn, cho phép các hàm và biến tạm thời truy cập dữ liệu mà không cần nắm quyền sở hữu. Một tham chiếu, được tạo bằng toán tử dấu và (&), cung cấp quyền truy cập chỉ đọc vào một giá trị trong khi vẫn giữ quyền sở hữu cho biến gốc.


Tham chiếu cho phép các hàm hoạt động trên dữ liệu mà không cần tiêu thụ dữ liệu đó, giúp có thể sử dụng cùng một giá trị nhiều lần trong suốt chương trình. Khi bạn truyền một tham chiếu đến một hàm, bạn đang tạm thời cho mượn dữ liệu, và hàm phải trả lại tham chiếu trước khi chủ sở hữu ban đầu có thể lấy lại toàn quyền kiểm soát. Hình ảnh ẩn dụ về việc mượn này phản ánh bản chất tạm thời của quyền truy cập: giống như bạn có thể cho bạn bè mượn một cuốn sách trong khi vẫn giữ quyền sở hữu, tham chiếu cho phép truy cập tạm thời trong khi vẫn bảo toàn mối quan hệ sở hữu ban đầu.


Các tham chiếu có thể thay đổi mở rộng khái niệm này để cho phép sửa đổi dữ liệu được mượn, nhưng với những hạn chế nghiêm ngặt để duy trì tính an toàn. Rust chỉ cho phép một tham chiếu có thể thay đổi đến một phần dữ liệu tại bất kỳ thời điểm nào, ngăn chặn các cuộc tranh chấp dữ liệu, nơi nhiều phần của chương trình có thể đồng thời sửa đổi cùng một vùng nhớ. Ngoài ra, bạn không thể có cả tham chiếu có thể thay đổi và không thể thay đổi đến cùng một dữ liệu cùng một lúc, vì điều này có thể dẫn đến các tình huống mà mã giả định dữ liệu ổn định trong khi mã khác đang tích cực sửa đổi nó. Các quy tắc này được thực thi tại thời điểm biên dịch, loại bỏ toàn bộ các loại lỗi đồng thời gây ảnh hưởng đến các ngôn ngữ lập trình hệ thống khác.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Các kiểu chuỗi và lát cắt


Chuẩn Rust phân biệt giữa các chuỗi ký tự và kiểu dữ liệu String, phản ánh các chiến lược quản lý bộ nhớ và trường hợp sử dụng khác nhau. Các chuỗi ký tự được nhúng trực tiếp vào mã nhị phân đã biên dịch và có kiểu dữ liệu &str (string slice), đại diện cho một khung nhìn vào dữ liệu chuỗi bất biến. Các chuỗi ký tự này hiệu quả vì chúng không yêu cầu cấp phát bộ nhớ trong thời gian chạy, nhưng chúng không thể được sửa đổi vì chúng là một phần của mã chương trình.


Ngược lại, kiểu dữ liệu String quản lý bộ nhớ được cấp phát động và có thể tăng, giảm và được sửa đổi trong thời gian chạy. Bạn có thể tạo một chuỗi String từ một giá trị hằng bằng cách sử dụng String::from() hoặc các phương thức tương tự, phương thức này sẽ cấp phát bộ nhớ heap và sao chép nội dung của giá trị hằng đó. Sự khác biệt này cho phép Rust tối ưu hóa cả hiệu năng (sử dụng giá trị hằng khi có thể) và tính linh hoạt (sử dụng String khi cần sửa đổi).


Các lát cắt chuỗi (&str) cung cấp một phương thức trừu tượng mạnh mẽ để làm việc với các phần của chuỗi mà không cần sao chép dữ liệu. Một lát cắt chứa một con trỏ đến vị trí bắt đầu của dữ liệu chuỗi và độ dài, cho phép bạn tham chiếu các chuỗi con một cách hiệu quả. Cú pháp lát cắt sử dụng các phạm vi (ví dụ: &s[0..5]) để chỉ định phần nào của chuỗi cần tham chiếu. Vì các lát cắt là các tham chiếu, chúng phải tuân theo các quy tắc mượn, ngăn không cho chuỗi cơ bản bị sửa đổi trong khi các lát cắt tồn tại. Việc thực thi tại thời điểm biên dịch này ngăn ngừa các lỗi phổ biến như truy cập bộ nhớ không hợp lệ sau khi chuỗi gốc đã được giải phóng hoặc sửa đổi.


### Mảng, vectơ và các lát cắt chung


Khái niệm lát cắt mở rộng phạm vi từ chuỗi ký tự sang bất kỳ chuỗi phần tử nào, cung cấp một cách thống nhất để làm việc với cả mảng có kích thước cố định và vectơ động. Mảng trong Rust có độ dài được mã hóa trong kiểu dữ liệu của chúng (ví dụ: [i32; 5] cho một mảng gồm năm số nguyên 32 bit), làm cho chúng phù hợp với các trường hợp yêu cầu đảm bảo kích thước tại thời điểm biên dịch. Các hàm chấp nhận mảng có thể thực thi các yêu cầu về độ dài chính xác, hữu ích cho các hoạt động như các hàm mật mã cần đầu vào có kích thước chính xác.


Các lát cắt (&[T]) cung cấp một giải pháp thay thế linh hoạt hơn, thể hiện một cái nhìn vào bất kỳ chuỗi phần tử liền kề nào bất kể cơ chế lưu trữ cơ bản. Bạn có thể tạo các lát cắt từ mảng, vectơ hoặc các lát cắt khác, và cùng một lát cắt có thể tham chiếu đến các phần dữ liệu khác nhau trong suốt vòng đời của nó. Tính linh hoạt này làm cho các lát cắt trở nên lý tưởng cho các hàm cần xử lý các chuỗi mà không cần quan tâm đến cơ chế lưu trữ cụ thể hoặc kích thước chính xác.


Mối quan hệ giữa các kiểu dữ liệu sở hữu (String, Vec<T>) và các slice mượn tương ứng (&str, &[T]) tuân theo một mô hình nhất quán trong toàn bộ Rust. Các kiểu dữ liệu sở hữu quản lý bộ nhớ của chúng và có thể được sửa đổi, trong khi các slice cung cấp quyền truy cập hiệu quả, chỉ đọc vào các phần của dữ liệu đó. Thiết kế này cho phép các API vừa linh hoạt (chấp nhận nhiều loại đầu vào thông qua slice) vừa hiệu quả (tránh sao chép không cần thiết), đồng thời duy trì các đảm bảo an toàn của Rust thông qua hệ thống mượn.



## Cấu trúc, Xây dựng các kiểu dữ liệu phức tạp

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Cấu trúc trong Rust đóng vai trò là nền tảng để tạo ra các kiểu dữ liệu phức tạp, tương tự như các lớp trong các ngôn ngữ lập trình khác. Chúng cho phép bạn nhóm các dữ liệu liên quan lại với nhau thành một đơn vị duy nhất, thống nhất, có thể chứa nhiều trường thuộc các kiểu khác nhau. Cú pháp để định nghĩa một cấu trúc tuân theo một mẫu đơn giản: bạn sử dụng từ khóa `struct` theo sau là tên cấu trúc, sau đó định nghĩa các trường trong dấu ngoặc nhọn bằng cách sử dụng cú pháp dấu hai chấm để chỉ định kiểu dữ liệu của từng trường.


Rust tuân theo các quy ước đặt tên cụ thể cho các cấu trúc mà trình biên dịch sẽ thực thi thông qua các cảnh báo. Tên cấu trúc nên sử dụng kiểu CamelCase (còn được gọi là PascalCase), trong khi tên trường bên trong cấu trúc nên sử dụng kiểu snake_case với dấu gạch dưới. Quy ước này giúp duy trì tính nhất quán trong các cơ sở mã Rust và làm cho mã dễ đọc hơn đối với các nhà phát triển khác.


Việc tạo các thể hiện của cấu trúc yêu cầu bạn phải chỉ định giá trị cho tất cả các trường bằng cách sử dụng tên cấu trúc, theo sau là dấu ngoặc nhọn chứa các phép gán giá trị cho trường. Sau khi có một thể hiện cấu trúc, bạn có thể truy cập và sửa đổi các trường riêng lẻ bằng cú pháp dấu chấm, miễn là thể hiện đó được khai báo là có thể thay đổi. Cú pháp dấu chấm này hoạt động nhất quán trong Rust, không giống như các ngôn ngữ như C++ nơi bạn có thể sử dụng các toán tử khác nhau cho con trỏ so với đối tượng trực tiếp.


### Hàm khởi tạo và các phím tắt trường


Rust không có các hàm tạo tích hợp sẵn như một số ngôn ngữ lập trình hướng đối tượng khác, nhưng bạn có thể tạo các hàm trả về các thể hiện của cấu trúc để phục vụ cùng mục đích. Các hàm tạo này thường nhận tham số cho một số hoặc tất cả các trường và có thể thiết lập giá trị mặc định cho các trường khác. Khi viết các hàm như vậy, Rust cung cấp một cách viết tắt tiện lợi: nếu một tham số có cùng tên với một trường của cấu trúc, bạn chỉ cần viết tên trường đó một lần thay vì lặp lại nó theo định dạng `field: value`.


Bạn cũng có thể tạo các thể hiện của cấu trúc bằng cách sao chép giá trị từ các thể hiện hiện có bằng cú pháp cập nhật cấu trúc. Tính năng này cho phép bạn tạo một thể hiện mới trong khi chỉ định các trường bạn muốn thay đổi, với tất cả các trường khác được sao chép từ một thể hiện hiện có. Tuy nhiên, thao tác này tuân theo các quy tắc sở hữu của Rust, có nghĩa là các kiểu không phải Copy sẽ được di chuyển khỏi thể hiện nguồn, có khả năng khiến một số phần của thể hiện gốc không thể sử dụng được sau đó. Trình biên dịch theo dõi các di chuyển một phần này một cách thông minh, cho phép bạn tiếp tục sử dụng các trường không được di chuyển trong khi ngăn chặn truy cập vào các trường đã được di chuyển.


### Cấu trúc bộ dữ liệu và cấu trúc đơn vị


Rust hỗ trợ cấu trúc tuple, là các cấu trúc có các trường không tên được truy cập bằng chỉ mục thay vì bằng tên. Chúng hữu ích cho các kiểu bao bọc đơn giản hoặc khi bạn cần một cấu trúc nhưng không yêu cầu các trường được đặt tên. Bạn truy cập các trường của cấu trúc tuple bằng cách sử dụng ký hiệu dấu chấm theo sau là chỉ mục của trường, chẳng hạn như `.0` cho trường đầu tiên, `.1` cho trường thứ hai, v.v. Cách tiếp cận này hoạt động tốt cho các cấu trúc bao bọc một giá trị duy nhất hoặc chỉ chứa một vài giá trị có liên quan chặt chẽ mà tên có thể bị trùng lặp.


Cấu trúc đơn vị thể hiện dạng cấu trúc đơn giản nhất—chúng không chứa bất kỳ dữ liệu nào. Mặc dù thoạt nhìn có vẻ vô nghĩa, cấu trúc đơn vị trở nên có giá trị khi làm việc với hệ thống đặc tính của Rust, vì chúng có thể thực hiện các hành vi mà không cần lưu trữ bất kỳ dữ liệu nào. Các cấu trúc trống này đóng vai trò là các dấu hiệu hoặc vị trí giữ chỗ trong các mẫu Rust nâng cao hơn.


### Phương pháp và các chức năng liên quan


Các cấu trúc sẽ có thêm chức năng khi bạn thêm hành vi thông qua các khối triển khai. Sử dụng từ khóa `impl` theo sau là tên cấu trúc, bạn có thể định nghĩa các phương thức hoạt động trên các thể hiện của cấu trúc đó. Phương thức là các hàm nhận `self` làm tham số đầu tiên, có thể là một giá trị sở hữu (`self`), một tham chiếu bất biến (`&self`) hoặc một tham chiếu có thể thay đổi (`&mut self`), tùy thuộc vào những gì phương thức cần làm với thể hiện đó.


Việc lựa chọn kiểu tham số `self` quyết định hành vi của phương thức liên quan đến quyền sở hữu. Các phương thức nhận `&self` có thể đọc từ đối tượng mà không cần nắm giữ quyền sở hữu, do đó phù hợp với các thao tác không làm thay đổi cấu trúc. Các phương thức nhận `&mut self` có thể sửa đổi đối tượng trong khi vẫn cho phép người gọi giữ lại quyền sở hữu. Các phương thức nhận `self` theo giá trị sẽ tiêu thụ đối tượng, điều này phù hợp với các thao tác biến đổi cấu trúc thành một thứ khác hoặc khi phương thức đại diện cho thao tác cuối cùng trên đối tượng đó.


Các hàm liên kết là các hàm được định nghĩa trong một khối triển khai mà không nhận tham số `self`. Chúng tương tự như các phương thức tĩnh trong các ngôn ngữ khác và thường được sử dụng làm hàm tạo hoặc hàm tiện ích liên quan đến kiểu dữ liệu. Bạn gọi các hàm liên kết bằng cú pháp dấu hai chấm kép (`Type::function_name()`), điều này giúp phân biệt rõ ràng chúng với các phương thức được gọi trên các thể hiện.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Liệt kê: Mô hình hóa các lựa chọn và biến thể


Kiểu liệt kê trong Rust có nhiều khả năng hơn so với kiểu liệt kê trong nhiều ngôn ngữ khác. Mặc dù chúng có thể biểu diễn các tập hợp hằng số được đặt tên đơn giản, kiểu liệt kê Rust cũng có thể chứa dữ liệu bên trong mỗi biến thể, khiến chúng phù hợp để mô hình hóa các tình huống trong đó một giá trị có thể thuộc một trong nhiều kiểu hoặc trạng thái khác nhau. Mỗi biến thể của kiểu liệt kê có thể chứa các kiểu và lượng dữ liệu khác nhau, từ không có dữ liệu nào đến các cấu trúc phức tạp với các trường được đặt tên.


Khả năng gắn dữ liệu vào các biến thể enum giúp loại bỏ nhiều lỗi lập trình phổ biến trong các ngôn ngữ khác. Thay vì duy trì các biến riêng biệt cho chỉ báo kiểu và dữ liệu liên quan—điều này dễ dẫn đến sự không nhất quán—enum Rust gộp thông tin kiểu với chính dữ liệu. Thiết kế này đảm bảo dữ liệu luôn khớp với biến thể, ngăn ngừa sự không khớp có thể dẫn đến lỗi thời gian chạy.


Các biến thể của kiểu liệt kê (enum) có thể chứa dữ liệu dưới nhiều dạng: không có dữ liệu cho các cờ đơn giản, dữ liệu dạng tuple cho các trường không tên, hoặc dữ liệu dạng struct với các trường có tên. Bạn thậm chí có thể kết hợp các kiểu này trong cùng một kiểu liệt kê, chọn dạng phù hợp nhất cho mỗi biến thể. Tính linh hoạt này làm cho kiểu liệt kê phù hợp để mô hình hóa các khái niệm miền phức tạp, nơi các trường hợp khác nhau yêu cầu thông tin khác nhau.


#### Loại tùy chọn: Xử lý vắng mặt một cách an toàn


Một trong những kiểu liệt kê quan trọng nhất của Rust là `Option<T>`, dùng để biểu thị các giá trị có thể có hoặc không có mặt. Kiểu liệt kê này có hai biến thể: `Some(T)` chứa một giá trị thuộc kiểu T, và `None` biểu thị sự vắng mặt của một giá trị. Kiểu Option đóng vai trò là giải pháp của Rust cho các vấn đề con trỏ null thường gặp trong nhiều ngôn ngữ khác, buộc các nhà phát triển phải xử lý rõ ràng các trường hợp giá trị có thể bị thiếu.


Việc sử dụng kiểu dữ liệu Option giúp mã của bạn mạnh mẽ hơn vì trình biên dịch yêu cầu bạn phải xử lý cả trường hợp có và không có giá trị. Bạn không thể vô tình sử dụng một giá trị có thể bị thiếu mà không kiểm tra xem nó có tồn tại hay không. Việc xử lý rõ ràng này ngăn ngừa lỗi con trỏ null và các lỗi thời gian chạy tương tự, vốn là những nguồn gây lỗi phổ biến trong các ngôn ngữ lập trình khác.


Kiểu dữ liệu Option tích hợp với hệ thống khớp mẫu của Rust, cho phép bạn xử lý cả hai trường hợp. Các phương thức như `unwrap_or()` cung cấp các cách thuận tiện để trích xuất các giá trị với các giá trị mặc định dự phòng, trong khi các phương thức như `map()` và `and_then()` cho phép sử dụng các mẫu lập trình hàm để làm việc với các giá trị tùy chọn.


### Đối sánh mẫu bằng biểu thức đối sánh


Việc khớp mẫu thông qua biểu thức `match` cung cấp một cách để làm việc với các kiểu liệt kê (enum) và các kiểu dữ liệu khác. Một biểu thức `match` kiểm tra một giá trị và thực thi các đoạn mã khác nhau dựa trên mẫu mà giá trị đó khớp. Mỗi mẫu có thể phân tách giá trị khớp, liên kết các phần của nó với các biến có thể được sử dụng trong khối mã tương ứng.


Biểu thức so khớp phải bao quát toàn diện, nghĩa là chúng phải xử lý mọi trường hợp có thể xảy ra đối với kiểu dữ liệu đang được so khớp. Yêu cầu này giúp ngăn ngừa các lỗi có thể xảy ra nếu một số trường hợp vô tình bị bỏ sót. Khi bạn không muốn xử lý mọi trường hợp một cách rõ ràng, bạn có thể sử dụng mẫu ký tự đại diện (`_`) để bắt tất cả các trường hợp còn lại, hoặc gán các trường hợp chưa được xử lý cho một biến nếu bạn cần truy cập vào giá trị đó.


Cấu trúc `if let` cung cấp một giải pháp thay thế ngắn gọn hơn cho `match` khi bạn chỉ quan tâm đến một mẫu cụ thể. Cú pháp này đặc biệt hữu ích khi làm việc với các kiểu dữ liệu Option hoặc khi bạn muốn thực thi mã chỉ khi một giá trị khớp với một biến thể enum cụ thể. Cấu trúc `if let` có thể bao gồm một mệnh đề `else` cho các trường hợp mẫu không khớp, làm cho nó trở thành một cách đơn giản để xử lý các tình huống khớp mẫu đơn giản.


#### Bộ sưu tập: Quản lý các nhóm dữ liệu


Thư viện chuẩn của Rust cung cấp một số kiểu tập hợp để quản lý các nhóm dữ liệu có liên quan. Các tập hợp này có tính tổng quát, nghĩa là chúng có thể lưu trữ các phần tử thuộc bất kỳ kiểu nào và tự động xử lý việc quản lý bộ nhớ. Các tập hợp được sử dụng phổ biến nhất là vector cho danh sách có thứ tự, hash map cho các liên kết khóa-giá trị và chuỗi cho dữ liệu văn bản.


#### Vectơ: Mảng động


Vector đại diện cho các mảng có thể mở rộng, tức là kích thước có thể thay đổi trong quá trình thực thi chương trình. Không giống như các mảng có kích thước cố định, vector cấp phát bộ nhớ trên heap và có thể mở rộng hoặc thu hẹp khi cần thiết. Việc tạo một vector thường yêu cầu chú thích kiểu rõ ràng khi bắt đầu với một vector rỗng, vì trình biên dịch cần biết kiểu dữ liệu của các phần tử mà vector sẽ chứa.


Vector cung cấp nhiều cách để truy cập các phần tử, mỗi cách có đặc điểm an toàn khác nhau. Ký hiệu chỉ mục (`vec[0]`) cung cấp quyền truy cập trực tiếp nhưng sẽ gây lỗi nếu chỉ mục nằm ngoài phạm vi. Phương thức `get()` trả về một `Option`, cho phép bạn xử lý việc truy cập ngoài phạm vi một cách khéo léo. Việc lựa chọn giữa các phương pháp này phụ thuộc vào việc bạn có thể đảm bảo chỉ mục hợp lệ hay cần xử lý các lỗi tiềm ẩn hay không.


Các quy tắc mượn của Rust áp dụng cho các vector, ngăn ngừa các vấn đề an toàn bộ nhớ thường gặp. Nếu bạn giữ một tham chiếu đến một phần tử của vector, bạn không thể sửa đổi vector cho đến khi tham chiếu đó ra khỏi phạm vi. Điều này ngăn chặn các trường hợp tham chiếu có thể trỏ đến vùng nhớ đã được giải phóng sau các thao tác trên vector như thêm phần tử mới hoặc xóa vector.


#### Bản đồ Hash: Lưu trữ khóa-giá trị


Các bản đồ Hash cung cấp khả năng lưu trữ cặp khóa-giá trị hiệu quả, cho phép bạn nhanh chóng tra cứu các giá trị dựa trên khóa liên kết của chúng. Cả khóa và giá trị đều có thể thuộc bất kỳ kiểu dữ liệu nào, tuy nhiên khóa phải triển khai các thuộc tính cần thiết cho việc băm và so sánh bằng nhau. Các bản đồ Hash sẽ nắm quyền sở hữu các giá trị được chèn vào trừ khi các giá trị đó triển khai thuộc tính Copy.


Các bản đồ Hash cung cấp một số phương pháp để chèn và cập nhật giá trị. Phương pháp cơ bản `insert()` sẽ ghi đè lên các giá trị hiện có, trong khi `entry()` cung cấp logic chèn linh hoạt hơn. API cho phép bạn chèn giá trị chỉ khi chúng chưa tồn tại hoặc cập nhật các giá trị hiện có dựa trên trạng thái hiện tại của chúng. API này hữu ích cho các mẫu như đếm số lần xuất hiện hoặc duy trì tổng tích lũy.


Khi truy xuất giá trị từ bảng băm, phương thức `get()` trả về một `Option` vì khóa được yêu cầu có thể không tồn tại. Bạn có thể sử dụng các phương thức như `copied()` để chuyển đổi từ `Option<&T>` sang `Option<T>` cho các kiểu Copy, và `unwrap_or()` để cung cấp giá trị mặc định khi thiếu khóa.


### Xử lý chuỗi và Unicode


Chuỗi trong Rust được mã hóa UTF-8, cung cấp hỗ trợ Unicode đầy đủ nhưng làm tăng độ phức tạp so với các chuỗi ASCII đơn giản. Kiểu dữ liệu `String` đại diện cho dữ liệu văn bản có thể mở rộng và thuộc sở hữu, trong khi các lát cắt chuỗi (`&str`) cung cấp các chế độ xem mượn vào dữ liệu chuỗi. Bạn có thể chuyển đổi giữa các kiểu này khi cần, với các lát cắt chuỗi thường được sử dụng cho các tham số hàm để chấp nhận cả chuỗi thuộc sở hữu và chuỗi ký tự.


Thao tác chuỗi bao gồm các phương thức để nối thêm văn bản, định dạng nhiều giá trị cùng nhau và trích xuất chuỗi con. Phương thức `push_str()` nối các đoạn chuỗi mà không cần giành quyền sở hữu, trong khi macro `format!` cung cấp một cách linh hoạt để xây dựng chuỗi từ nhiều thành phần. Khi làm việc với chỉ số chuỗi, bạn phải cẩn thận để tuân thủ các ranh giới ký tự UTF-8 nhằm tránh lỗi nghiêm trọng khi chạy chương trình.


Để xử lý từng ký tự một cách an toàn, chuỗi cung cấp các phương thức lặp như `chars()` cho các giá trị vô hướng Unicode và `bytes()` để truy cập byte thô. Các trình lặp này xử lý mã hóa UTF-8 một cách chính xác, đảm bảo bạn không vô tình tách các ký tự nhiều byte. Cách tiếp cận này an toàn và đáng tin cậy hơn so với việc lập chỉ mục thủ công, đặc biệt khi làm việc với văn bản quốc tế có thể chứa các ký tự Unicode phức tạp.



## Hệ thống xử lý lỗi hai loại của Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust áp dụng một phương pháp xử lý lỗi hoàn toàn khác so với hầu hết các ngôn ngữ lập trình khác. Trong khi nhiều ngôn ngữ chủ yếu dựa vào ngoại lệ, Rust phân biệt giữa hai loại lỗi khác nhau và cung cấp các cơ chế cụ thể để xử lý từng loại. Chương này sẽ khám phá hệ thống xử lý lỗi toàn diện của Rust, bao gồm cả các lỗi không thể khắc phục làm chấm dứt chương trình và các lỗi có thể khắc phục cho phép chương trình tiếp tục chạy một cách trơn tru.


### Lỗi không thể khắc phục và tình trạng hoảng loạn


Lỗi không thể khắc phục là những tình huống mà chương trình rơi vào trạng thái không nhất quán hoặc không mong muốn, từ đó không thể khôi phục một cách an toàn. Những tình huống này bao gồm việc truy cập mảng vượt quá giới hạn, thực hiện các thao tác vi phạm an toàn bộ nhớ, hoặc gặp phải các điều kiện cho thấy lỗi logic cơ bản của chương trình. Khi xảy ra những lỗi như vậy, phản ứng thích hợp là chấm dứt chương trình ngay lập tức thay vì mạo hiểm gây ra thêm hư hỏng hoặc hành vi không xác định.


Trong Rust, các lỗi không thể khắc phục sẽ kích hoạt một sự cố nghiêm trọng (panic), khiến chương trình bị sập một cách có kiểm soát. Trước khi kết thúc, Rust thực hiện một quy trình gọi là unwinding, trong đó nó duyệt ngược lại ngăn xếp lệnh gọi để cung cấp dấu vết ngăn xếp chi tiết cho thấy chính xác nơi xảy ra sự cố. Quá trình unwinding này giúp các nhà phát triển xác định nguồn gốc của vấn đề trong quá trình gỡ lỗi. Đối với các ứng dụng quan trọng về hiệu năng hoặc hệ thống nhúng, bạn có thể tắt unwinding và cấu hình Rust để dừng ngay lập tức khi xảy ra sự cố nghiêm trọng, mặc dù điều này sẽ làm mất thông tin gỡ lỗi để có được tốc độ kết thúc nhanh hơn.


Bạn có thể kích hoạt lỗi panic một cách rõ ràng bằng cách sử dụng macro `panic!` với một thông báo tùy chỉnh. Khi lỗi panic xảy ra, bạn sẽ thấy đầu ra cho biết luồng nào đã gây ra lỗi và thông báo liên quan. Việc thiết lập biến môi trường `RUST_BACKTRACE` cung cấp thêm thông tin gỡ lỗi, hiển thị toàn bộ ngăn xếp cuộc gọi dẫn đến lỗi panic. Ví dụ, việc cố gắng truy cập phần tử 99 của một vectơ chỉ chứa ba phần tử sẽ gây ra lỗi panic với thông báo "chỉ mục nằm ngoài phạm vi" (index out of bounds), cùng với dấu vết ngược hiển thị trình tự chính xác của các cuộc gọi hàm dẫn đến lỗi.


### Các lỗi có thể khắc phục kèm kết quả


Các lỗi có thể khắc phục được thể hiện các điều kiện lỗi dự kiến mà chương trình có thể xử lý một cách khéo léo mà không cần chấm dứt. Ví dụ bao gồm việc cố gắng mở một tệp không tồn tại, lỗi kết nối mạng hoặc đầu vào không hợp lệ của người dùng. Đối với những tình huống này, Rust cung cấp kiểu liệt kê `Result`, kiểu này thể hiện rõ ràng các thao tác có thể thất bại và buộc các nhà phát triển phải xử lý cả trường hợp thành công và thất bại.


Kiểu liệt kê `Result` được định nghĩa với hai biến thể: `Ok(T)` cho các thao tác thành công chứa giá trị thuộc kiểu `T`, và `Err(E)` cho các lỗi chứa lỗi thuộc kiểu `E`. Thiết kế này sử dụng hệ thống kiểu của Rust để đảm bảo rằng các lỗi tiềm ẩn không thể bị bỏ qua. Các hàm có thể thất bại sẽ trả về một `Result`, và mã gọi phải xử lý rõ ràng cả trường hợp thành công và lỗi, thường sử dụng khớp mẫu với các biểu thức `match`.


Hãy xem xét hàm `File::open`, hàm này trả về một `Result<File, std::io::Error>`. Khi mở một tệp, bạn sẽ nhận được một đối tượng `File` nếu thành công hoặc một `std::io::Error` nếu thao tác thất bại. Bạn có thể sử dụng kết quả này để xử lý từng trường hợp một cách thích hợp. Trong trường hợp thành công, bạn có thể tiếp tục các thao tác với tệp, trong khi ở trường hợp lỗi, bạn có thể thử tạo tệp, thử một phương pháp khác hoặc truyền lỗi đến mã gọi. Việc xử lý rõ ràng này đảm bảo rằng chương trình của bạn đưa ra các quyết định có ý thức về việc phục hồi lỗi thay vì bị sập đột ngột.


### Các mẫu xử lý lỗi và các phương pháp rút gọn


Mặc dù việc khớp mẫu tường minh cung cấp khả năng kiểm soát hoàn toàn việc xử lý lỗi, Rust cung cấp một số phương thức tiện lợi cho các mẫu xử lý lỗi phổ biến. Phương thức `unwrap` trích xuất giá trị thành công từ một `Result` nhưng sẽ gây ra lỗi nghiêm trọng nếu xảy ra lỗi, điều này làm cho nó hữu ích cho việc tạo mẫu nhanh hoặc các tình huống mà bạn tự tin rằng một thao tác sẽ thành công. Phương thức `expect` hoạt động tương tự nhưng cho phép bạn cung cấp một thông báo lỗi nghiêm trọng tùy chỉnh, giúp việc gỡ lỗi dễ dàng hơn khi mọi thứ không suôn sẻ.


Để xử lý lỗi linh hoạt hơn, các phương thức như `unwrap_or_else` cho phép bạn cung cấp một closure được thực thi khi xảy ra lỗi, cho phép thực hiện logic phục hồi tùy chỉnh. Bạn có thể kết hợp các thao tác này với nhau để xử lý các tình huống phức tạp, chẳng hạn như cố gắng mở một tệp và tạo tệp đó nếu nó không tồn tại, với các chiến lược xử lý lỗi khác nhau cho mỗi bước.


Toán tử dấu hỏi (`?`) cung cấp cú pháp ngắn gọn để truyền lỗi, điều này rất phổ biến trong các chương trình Rust. Khi bạn thêm `?` vào một `Result`, nó sẽ tự động giải nén các giá trị thành công và trả về lỗi ngay lập tức từ hàm hiện tại. Toán tử này chỉ có thể được sử dụng trong các hàm trả về kiểu `Result`, đảm bảo rằng lỗi có thể được truyền đúng cách lên ngăn xếp cuộc gọi. Toán tử `?` làm cho mã xử lý lỗi dễ đọc hơn nhiều bằng cách loại bỏ các biểu thức khớp dài dòng trong khi vẫn duy trì ngữ nghĩa truyền lỗi rõ ràng.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Lan truyền lỗi và thiết kế hàm


Lan truyền lỗi là một khái niệm cơ bản trong xử lý lỗi Rust, cho phép các hàm truyền lỗi lên ngăn xếp cuộc gọi thay vì xử lý chúng cục bộ. Khi thiết kế các hàm có thể bị lỗi, bạn nên trả về kiểu `Result` để cung cấp cho người gọi sự linh hoạt trong việc quyết định cách xử lý lỗi. Cách tiếp cận này thúc đẩy việc xử lý lỗi có thể kết hợp, trong đó mỗi hàm trong chuỗi cuộc gọi có thể xử lý lỗi cục bộ hoặc truyền chúng lên mã cấp cao hơn có nhiều ngữ cảnh hơn để đưa ra quyết định phục hồi.


Toán tử dấu hỏi (?) giúp đơn giản hóa việc lan truyền lỗi. Thay vì viết các biểu thức khớp dài dòng cho mỗi thao tác có khả năng thất bại, bạn có thể kết hợp các thao tác với nhau bằng toán tử `?`, tạo ra mã dễ đọc, xử lý được trường hợp thành công đồng thời tự động lan truyền bất kỳ lỗi nào xảy ra. Mẫu này phổ biến đến mức nhiều hàm Rust được thiết kế đặc biệt để hoạt động tốt với toán tử `?`, cho phép xử lý lỗi trôi chảy trong toàn bộ mã nguồn của bạn.


Khi quyết định giữa việc gây ra lỗi nghiêm trọng (panic) và trả về lỗi, hãy xem xét liệu mã gọi có thể phục hồi một cách hợp lý sau sự cố hay không. Nếu sự cố đó là lỗi lập trình hoặc trạng thái hệ thống không thể phục hồi, thì việc gây ra lỗi nghiêm trọng là phù hợp. Tuy nhiên, nếu sự cố đó là một điều kiện được dự đoán trước mà mã gọi có thể xử lý khác nhau tùy thuộc vào ngữ cảnh, thì việc trả về một `Result` sẽ mang lại tính linh hoạt và khả năng kết hợp tốt hơn.


### Các nguyên tắc thực hành tốt nhất và những cân nhắc về thiết kế


Việc xử lý lỗi hiệu quả trong Rust đòi hỏi phải cân nhắc kỹ lưỡng khi nào nên sử dụng panic và khi nào nên trả về lỗi. Sử dụng panic cho các tình huống thể hiện lỗi lập trình hoặc các trạng thái không bao giờ được phép xảy ra trong các chương trình chính xác, chẳng hạn như truy cập dữ liệu được mã hóa cứng mà bạn biết là hợp lệ. Ví dụ, việc phân tích cú pháp một chuỗi địa chỉ IP được mã hóa cứng mà bạn đã xác minh là chính xác có thể sử dụng `expect` một cách an toàn với một thông báo mô tả lý do tại sao thao tác này không bao giờ được phép thất bại.


Đối với đầu vào do người dùng điều khiển hoặc tương tác với hệ thống bên ngoài, hãy luôn ưu tiên trả về kiểu dữ liệu `Result` thay vì gây ra lỗi nghiêm trọng. Người dùng mắc lỗi, tập tin bị xóa và kết nối mạng bị lỗi – đây là những điều kiện bình thường mà các chương trình được thiết kế tốt nên xử lý một cách khéo léo. Bằng cách trả về lỗi trong những tình huống này, bạn cho phép mã gọi thực hiện các chiến lược phục hồi thích hợp, cho dù đó là yêu cầu người dùng nhập dữ liệu khác, quay lại giá trị mặc định hoặc hiển thị các thông báo lỗi hữu ích.


Hãy cân nhắc việc tạo các kiểu dữ liệu tùy chỉnh thực thi việc kiểm tra tính hợp lệ tại thời điểm khởi tạo để ngăn chặn các trạng thái không hợp lệ lan truyền trong chương trình của bạn. Ví dụ, nếu chương trình của bạn yêu cầu các số nằm trong một phạm vi cụ thể, hãy tạo một kiểu bao bọc (wrapper type) để kiểm tra tính hợp lệ của dữ liệu đầu vào trong quá trình khởi tạo và không cho phép tạo ra các thể hiện không hợp lệ. Cách tiếp cận này sử dụng hệ thống kiểu dữ liệu của Rust để loại bỏ toàn bộ các lớp lỗi bằng cách làm cho các trạng thái không hợp lệ không thể biểu diễn được, giảm nhu cầu kiểm tra lỗi trong thời gian chạy trên toàn bộ mã nguồn của bạn.


## Các tính năng của lập trình hàm, bao đóng và con trỏ thông minh


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Mặc dù Rust không phải là một ngôn ngữ lập trình hàm thuần túy, nhưng nó tích hợp các tính năng lấy cảm hứng từ các mô hình lập trình hàm. Những tính năng này cho phép các nhà phát triển viết mã ngắn gọn bằng cách tận dụng các khái niệm như closure và iterator. Rust bao gồm các yếu tố hàm này để cung cấp các công cụ linh hoạt cho việc xử lý dữ liệu và cơ chế gọi lại.


Các tính năng lập trình hàm trong Rust duy trì các nguyên tắc cốt lõi của ngôn ngữ về an toàn bộ nhớ và trừu tượng hóa không tốn chi phí. Khi bạn sử dụng closure và iterator, bạn không phải hy sinh hiệu năng để đổi lấy khả năng diễn đạt – trình biên dịch Rust tối ưu hóa các cấu trúc này để tạo ra mã máy hiệu quả tương đương với các phương pháp dựa trên vòng lặp truyền thống.


### Hiểu về việc đóng cửa


Trong Rust, closure là các hàm ẩn danh có thể nắm bắt các biến từ môi trường xung quanh. Trong các ngôn ngữ lập trình khác, chúng thường được gọi là hàm lambda. Đặc điểm chính của closure là khả năng "bao trùm" môi trường của chúng, nghĩa là chúng có thể truy cập và sử dụng các biến tồn tại trong phạm vi mà closure được định nghĩa.


Cú pháp của closure sử dụng ký tự dấu gạch dọc (`|`) thay vì dấu ngoặc đơn để định nghĩa tham số. Đối với closure không có tham số, bạn viết `||`, và đối với closure có tham số, bạn liệt kê chúng giữa các dấu gạch dọc như `|x, y|`. Nếu phần thân của closure chỉ bao gồm một biểu thức duy nhất, bạn có thể bỏ qua dấu ngoặc nhọn, làm cho cú pháp rất ngắn gọn.


Hãy xem xét ví dụ thực tế này về một công ty áo thun tặng những chiếc áo độc quyền dựa trên sở thích của khách hàng. Nếu khách hàng đã chỉ định màu sắc yêu thích, họ sẽ nhận được màu đó; nếu không, họ sẽ nhận được màu có sẵn nhiều nhất làm mặc định. Sử dụng closure, logic này trở thành: `user_preference.unwrap_or_else(|| self.most_stocked())`. Closure `|| self.most_stocked()` chỉ cung cấp giá trị mặc định khi cần thiết và nó có thể truy cập `self` từ môi trường của nó.


### Suy luận kiểu đóng và tính linh hoạt


Một trong những tính năng tiện lợi nhất của Rust với closure là khả năng suy luận kiểu tự động. Không giống như các hàm thông thường, nơi bạn phải chỉ định rõ ràng kiểu tham số và kiểu trả về, closure thường có thể suy luận các kiểu này từ ngữ cảnh. Trình biên dịch phân tích cách closure được sử dụng và tự động xác định các kiểu phù hợp. Tuy nhiên, một khi closure được gọi với các kiểu cụ thể, các kiểu đó sẽ được cố định cho thể hiện closure đó.


Bạn có thể lưu trữ các closure trong biến giống như bất kỳ giá trị nào khác, biến chúng thành các đối tượng hạng nhất trong ngôn ngữ. Khi bạn gán một closure cho một biến, bạn có thể gọi nó sau đó bằng cách sử dụng dấu ngoặc đơn: `let my_closure = |x| x + 1; let result = my_closure(5);`. Tính linh hoạt này cho phép bạn truyền các closure làm đối số cho các hàm, trả về chúng từ các hàm và sử dụng chúng trong các cấu trúc dữ liệu.


Nếu trình biên dịch không thể suy luận kiểu dữ liệu hoặc nếu bạn muốn chỉ định rõ ràng, bạn có thể chú thích các tham số của closure và kiểu trả về bằng cú pháp tương tự như hàm: `|x: i32| -> i32 { x + 1 }`. Việc chỉ định kiểu rõ ràng này đôi khi cần thiết trong các trường hợp phức tạp, nơi trình biên dịch cần thêm thông tin để xác định kiểu dữ liệu một cách chính xác.


### Thu thập các biến môi trường


Các closure có thể nắm giữ các biến từ môi trường của chúng theo ba cách khác nhau: bằng tham chiếu bất biến, bằng tham chiếu có thể thay đổi hoặc bằng cách chiếm quyền sở hữu. Trình biên dịch Rust tự động xác định phương pháp nắm giữ hạn chế nhất đáp ứng nhu cầu của closure, tuân theo nguyên tắc quyền hạn tối thiểu.


Khi một closure chỉ cần đọc một giá trị, nó sẽ nắm giữ giá trị đó bằng tham chiếu bất biến. Điều này cho phép biến gốc vẫn có thể truy cập được sau khi closure được định nghĩa và gọi. Ví dụ, một closure in ra một danh sách sẽ mượn danh sách đó một cách bất biến, cho phép bạn tiếp tục sử dụng danh sách sau khi closure được thực thi.


Nếu một closure cần sửa đổi một biến được bắt giữ, nó phải bắt giữ bằng tham chiếu có thể thay đổi. Trong trường hợp này, cả biến được bắt giữ và chính closure đó đều phải được khai báo là có thể thay đổi. Khi đó, closure có thể sửa đổi biến được bắt giữ, nhưng các quy tắc mượn vẫn được áp dụng – bạn không thể có các tham chiếu khác đến biến đó trong khi closure có thể thay đổi vẫn tồn tại.


Phương pháp bắt giữ hạn chế nhất là giành quyền sở hữu, di chuyển các biến được bắt giữ vào trong closure. Điều này là cần thiết khi closure có thể tồn tại lâu hơn phạm vi mà các biến được định nghĩa ban đầu, chẳng hạn như khi tạo luồng. Bạn có thể buộc bắt giữ quyền sở hữu bằng cách sử dụng từ khóa `move` trước các tham số của closure: `move |x| { /* phần thân closure */ }`. Điều này rất cần thiết cho tính an toàn của luồng, vì các luồng không thể mượn biến một cách an toàn từ các luồng khác có thể kết thúc và giải phóng các biến của chúng.


### Đặc điểm đóng và các loại chức năng


Rust biểu diễn các closure thông qua một hệ thống đặc tính với ba đặc tính chính: `FnOnce`, `FnMut` và `Fn`. Các đặc tính này tạo thành một hệ thống phân cấp mô tả cách thức gọi các closure và những gì chúng có thể làm với các biến được nắm bắt.


`FnOnce` là đặc tính cơ bản nhất mà tất cả các closure đều triển khai. Nó đại diện cho các closure có thể được gọi ít nhất một lần. Một số closure, đặc biệt là những closure di chuyển các giá trị được nắm bắt hoặc sử dụng chúng theo một cách nào đó, chỉ có thể được gọi một lần vì chúng hủy hoặc di chuyển dữ liệu được nắm bắt trong quá trình thực thi.


`FnMut` đại diện cho các closure có thể được gọi nhiều lần và có thể thay đổi môi trường được nắm bắt. Các closure này nắm bắt các biến bằng tham chiếu có thể thay đổi và có thể sửa đổi chúng qua nhiều lần gọi. Các quy tắc mượn đảm bảo rằng khi một closure `FnMut` hoạt động, nó có quyền truy cập độc quyền và có thể thay đổi các biến được nắm bắt.


`Fn` là đặc tính hạn chế nhất, đại diện cho các closure có thể được gọi nhiều lần mà không làm thay đổi môi trường được nắm bắt. Các closure này chỉ nắm bắt bằng tham chiếu bất biến và có thể được gọi đồng thời mà không vi phạm các đảm bảo an toàn của Rust. Nếu một closure triển khai `Fn`, nó cũng tự động triển khai `FnMut` và `FnOnce`, vì việc có thể gọi nhiều lần mà không làm thay đổi môi trường ngụ ý rằng nó cũng có thể gọi được với sự thay đổi môi trường và có thể gọi một lần.


### Làm việc với các trình lặp


Các iterator trong Rust cung cấp một cách để xử lý các chuỗi dữ liệu. Chúng hoạt động theo kiểu "lười biếng", nghĩa là chúng không thực hiện bất kỳ công việc nào cho đến khi bạn sử dụng chúng bằng cách gọi các phương thức thực sự lặp qua dữ liệu. Việc đánh giá "lười biếng" này cho phép xâu chuỗi các thao tác một cách hiệu quả mà không cần tạo ra các tập hợp trung gian.


Đặc tính `Iterator` định nghĩa chức năng cốt lõi với một kiểu liên kết `Item` đại diện cho những gì trình lặp trả về, và một phương thức `next` trả về `Option<Self::Item>`. Khi `next` trả về `None`, trình lặp đã cạn kiệt. Thiết kế này cho phép các trình lặp biểu diễn cả các chuỗi hữu hạn và có khả năng vô hạn một cách an toàn.


Bạn có thể tạo các iterator từ các collection bằng cách sử dụng các phương thức như `iter()` để mượn và lặp, `iter_mut()` để mượn và lặp có thể thay đổi, và `into_iter()` để tiêu thụ và lặp. Việc lựa chọn giữa các phương thức này phụ thuộc vào việc bạn có cần sửa đổi các phần tử hay không và liệu bạn có muốn tiêu thụ collection gốc hay không.


### Bộ điều hợp và người tiêu dùng của trình lặp


Bộ chuyển đổi trình lặp là các phương thức biến đổi một trình lặp thành một trình lặp khác, cho phép bạn xích chuỗi các thao tác lại với nhau. Các bộ chuyển đổi phổ biến bao gồm `map` để biến đổi từng phần tử, `filter` để chọn các phần tử dựa trên một vị từ và `enumerate` để thêm chỉ mục. Các bộ chuyển đổi này hoạt động theo kiểu lười biếng – chúng không thực hiện bất kỳ công việc nào cho đến khi được sử dụng.


Phương thức `map` áp dụng một closure cho mỗi phần tử, biến đổi nó thành một thứ khác. Ví dụ: `numbers.iter().map(|x| x * 2)` tạo ra một iterator nhân đôi mỗi số. Phương thức `filter` chỉ giữ lại các phần tử mà closure của vị từ trả về true: `numbers.iter().filter(|&x| x > 10)` chỉ giữ lại các số lớn hơn mười.


Các phương thức tiêu thụ thực chất lặp qua dữ liệu và tạo ra kết quả cuối cùng. Phương thức `collect` tiêu thụ một iterator và tạo ra một collection từ đó. Bạn thường cần chỉ định kiểu dữ liệu của collection: `let vec: Vec<_> = iterator.collect()`. Các phương thức tiêu thụ khác bao gồm `sum` để cộng các phần tử số, `fold` để tích lũy các giá trị với một phép toán tùy chỉnh và `for_each` để thực hiện các tác động phụ trên từng phần tử.


### Các mẫu lặp nâng cao


Các thao tác lặp bổ sung bao gồm `zip` để kết hợp hai trình lặp theo từng phần tử, `chain` để nối các trình lặp và `filter_map` để kết hợp lọc và ánh xạ trong một thao tác. Phương thức `zip` tạo ra các cặp từ các phần tử tương ứng của hai trình lặp: `a.iter().zip(b.iter())` tạo ra các bộ `(a[0], b[0]), (a[1], b[1]), ...`.


Phương thức `fold` rất hữu ích để tích lũy các giá trị. Nó nhận một giá trị ban đầu và một closure kết hợp bộ tích lũy với từng phần tử: `numbers.iter().fold(0, |acc, x| acc + x)` cộng tất cả các số. Mẫu này có thể được sử dụng để thực hiện nhiều thao tác khác như tìm giá trị lớn nhất, xây dựng chuỗi hoặc tạo cấu trúc dữ liệu phức tạp.


Chuỗi lặp có thể thể hiện các phép biến đổi dữ liệu phức tạp một cách ngắn gọn. Ví dụ, xử lý dữ liệu âm thanh có thể bao gồm: `coefficients.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Điều này nhân các hệ số tương ứng và giá trị bộ đệm, cộng tổng các kết quả và dịch chuyển giá trị cuối cùng, tất cả trong một biểu thức dễ đọc duy nhất.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Giới thiệu về con trỏ thông minh


Con trỏ thông minh là các cấu trúc dữ liệu hoạt động giống như con trỏ truyền thống nhưng cung cấp thêm các khả năng và quản lý bộ nhớ tự động. Không giống như các tham chiếu đơn giản, con trỏ thông minh sở hữu dữ liệu mà chúng trỏ đến và có thể triển khai các hành vi tùy chỉnh cho việc cấp phát, giải phóng bộ nhớ và các mẫu truy cập. Chúng là công cụ thiết yếu để quản lý dữ liệu được cấp phát trên heap và triển khai các mẫu sở hữu phức tạp vượt ra ngoài hệ thống sở hữu cơ bản của Rust.


Tính "thông minh" của chúng đến từ khả năng tự động xử lý các tác vụ quản lý bộ nhớ mà nếu không sẽ cần sự can thiệp thủ công. Khi một con trỏ thông minh nằm ngoài phạm vi, nó có thể tự động giải phóng bộ nhớ liên kết, giảm số lượng tham chiếu hoặc thực hiện các thao tác dọn dẹp khác. Sự tự động hóa này giúp ngăn ngừa rò rỉ bộ nhớ và lỗi sử dụng sau khi giải phóng, đồng thời cung cấp tính linh hoạt hơn so với việc chỉ cấp phát bộ nhớ trên ngăn xếp.


Con trỏ thông minh thường triển khai hai đặc tính chính: `Deref` và `Drop`. Đặc tính `Deref` cho phép con trỏ thông minh được sử dụng như thể nó là một tham chiếu đến dữ liệu chứa bên trong. Đặc tính `Drop` cho phép thực hiện logic dọn dẹp tùy chỉnh khi con trỏ thông minh bị hủy. Cùng nhau, các đặc tính này cho phép con trỏ thông minh tự động quản lý bộ nhớ.


### Con trỏ thông minh Box


`Box<T>` là con trỏ thông minh đơn giản nhất, cung cấp cấp phát bộ nhớ trên heap cho bất kỳ kiểu dữ liệu `T` nào. Khi bạn tạo một `Box`, giá trị chứa bên trong được lưu trữ trên heap thay vì stack, và chính `Box` (chỉ là một con trỏ) được lưu trữ trên stack. Sự gián tiếp này hữu ích khi bạn cần lưu trữ một lượng lớn dữ liệu mà không cần di chuyển chúng, khi bạn cần một kiểu dữ liệu có kích thước không xác định tại thời điểm biên dịch, hoặc khi bạn muốn chuyển giao quyền sở hữu dữ liệu trên heap một cách hiệu quả.


Việc tạo một `Box` rất đơn giản: `let boxed_value = Box::new(42);` cấp phát một số nguyên trên heap. `Box` tự động quản lý bộ nhớ này – khi `Box` ra khỏi phạm vi, nó tự động giải phóng bộ nhớ heap. Việc dọn dẹp tự động này ngăn ngừa rò rỉ bộ nhớ mà không cần quản lý bộ nhớ thủ công.


Một trong những trường hợp sử dụng quan trọng nhất của `Box` là cho phép cấu trúc dữ liệu đệ quy. Hãy xem xét một danh sách liên kết trong đó mỗi nút chứa một giá trị và một con trỏ đến nút tiếp theo. Nếu không có `Box`, bạn không thể định nghĩa một cấu trúc như vậy vì trình biên dịch không thể xác định kích thước của một kiểu dữ liệu chứa chính nó. Bằng cách sử dụng `Box<Node>` cho con trỏ tiếp theo, bạn giải quyết được vấn đề về kích thước đệ quy vì `Box` có kích thước cố định, đã biết bất kể nó chứa gì.


### Triển khai Trait Deref


Trait `Deref` cho phép giải tham chiếu một kiểu dữ liệu bằng toán tử `*`, làm cho con trỏ thông minh hoạt động như các tham chiếu đến dữ liệu mà chúng chứa. Khi bạn triển khai `Deref` cho một con trỏ thông minh, bạn kích hoạt tính năng giải tham chiếu tự động, giúp con trỏ thông minh trở nên minh bạch khi sử dụng. Điều này có nghĩa là bạn có thể gọi các phương thức trên kiểu dữ liệu chứa trực tiếp thông qua con trỏ thông minh mà không cần giải tham chiếu tường minh.


Đặc tính `deref` định nghĩa một kiểu liên kết `Target` chỉ định kiểu tham chiếu mà thao tác giải tham chiếu sẽ tạo ra. Đặc tính này yêu cầu triển khai một phương thức `deref` trả về tham chiếu đến kiểu đích. Đối với `Box<T>`, việc triển khai trả về một tham chiếu đến giá trị `T` chứa bên trong.


Rust thực hiện ép kiểu tham chiếu tự động, có nghĩa là trình biên dịch có thể tự động chèn các lệnh gọi đến `deref` khi cần thiết để làm cho các kiểu dữ liệu tương thích. Đó là lý do tại sao bạn có thể truyền một `String` cho một hàm mong đợi một `&str` – trình biên dịch tự động giải tham chiếu `String` để nhận được một lát cắt chuỗi. Việc ép kiểu này có thể được xâu chuỗi nhiều cấp độ, vì vậy một `Box<String>` có thể được tự động chuyển đổi thành một `&str` thông qua nhiều thao tác giải tham chiếu.


### Triển khai thả tùy chỉnh


Đặc tính `Drop` cho phép bạn chỉ định mã dọn dẹp tùy chỉnh chạy khi một giá trị nằm ngoài phạm vi. Điều này đặc biệt quan trọng đối với các con trỏ thông minh quản lý các tài nguyên vượt ra ngoài bộ nhớ đơn thuần, chẳng hạn như xử lý tệp, kết nối mạng hoặc số lượng tham chiếu. Đặc tính `Drop` có một phương thức duy nhất, `drop`, nhận một tham chiếu có thể thay đổi đến `self` và thực hiện việc dọn dẹp.


Hầu hết các kiểu dữ liệu không cần triển khai phương thức `Drop` tùy chỉnh vì Rust tự động xử lý việc xóa các trường của chúng. Tuy nhiên, con trỏ thông minh thường cần logic tùy chỉnh để dọn dẹp tài nguyên mà chúng quản lý một cách đúng cách. Ví dụ, một con trỏ thông minh đếm tham chiếu cần giảm số lượng tham chiếu và có thể giải phóng dữ liệu dùng chung khi tham chiếu cuối cùng bị xóa.


Bạn cũng có thể chủ động loại bỏ một giá trị trước khi nó ra khỏi phạm vi bằng cách sử dụng `std::mem::drop()`. Hàm này sẽ nắm quyền sở hữu một giá trị và ngay lập tức loại bỏ nó, điều này có thể hữu ích để giải phóng tài nguyên sớm hoặc đảm bảo việc dọn dẹp diễn ra tại một điểm cụ thể trong chương trình của bạn. Hàm loại bỏ rõ ràng chỉ là một hàm nhận dạng nắm quyền sở hữu – công việc thực sự diễn ra khi giá trị được loại bỏ ở cuối hàm.


Nền tảng gồm các closure, iterator và con trỏ thông minh này cung cấp cho các nhà phát triển Rust những công cụ để viết mã dễ hiểu, an toàn và hiệu quả. Các tính năng này hoạt động cùng nhau để hỗ trợ các mẫu lập trình phổ biến trong khi vẫn duy trì các đảm bảo cốt lõi của Rust về an toàn bộ nhớ và hiệu suất.



## Đếm tham chiếu và khả năng thay đổi bên trong

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Đếm tham chiếu với RC


Đếm tham chiếu đại diện cho một loại con trỏ thông minh cơ bản khác trong Rust, được thiết kế đặc biệt để cho phép nhiều kịch bản sở hữu chung. Không giống như Box, tuân theo các quy tắc sở hữu đơn truyền thống trong đó một thực thể sở hữu dữ liệu, RC (Reference Counter) cho phép nhiều phần của mã của bạn chia sẻ quyền sở hữu cùng một dữ liệu đồng thời. Mô hình sở hữu chung này hoạt động thông qua một cơ chế đếm theo dõi số lượng tham chiếu tồn tại đến một phần dữ liệu cụ thể.


Hệ thống đếm tham chiếu hoạt động bằng cách duy trì một bộ đếm nội bộ, bộ đếm này tăng lên mỗi khi bạn sao chép một RC và giảm đi khi một RC bị hủy bỏ. Bộ nhớ chỉ được giải phóng khi bộ đếm này đạt đến 0, đảm bảo rằng dữ liệu vẫn hợp lệ miễn là còn bất kỳ tham chiếu nào tồn tại. Cách tiếp cận này ngăn chặn việc giải phóng bộ nhớ sớm đồng thời cho phép các mô hình chia sẻ dữ liệu linh hoạt mà không thể thực hiện được với quyền sở hữu Box đơn giản.


Một ví dụ thực tế cho thấy RC hữu ích là việc tạo ra các cấu trúc dữ liệu dùng chung như danh sách liên kết, trong đó nhiều danh sách có thể tham chiếu đến cùng một phần đuôi. Hãy xem xét việc cố gắng tạo hai danh sách riêng biệt cùng tham chiếu đến một chuỗi con chung. Với cơ chế sở hữu Box, điều này trở nên bất khả thi vì việc chuyển phần dùng chung vào danh sách đầu tiên sẽ chuyển quyền sở hữu, ngăn cản việc sử dụng nó trong danh sách thứ hai. RC giải quyết vấn đề này bằng cách cho phép bạn sao chép tham chiếu chứ không phải dữ liệu cơ bản, giúp tạo ra cấu trúc dùng chung trong khi vẫn đảm bảo an toàn bộ nhớ.


Khi bạn sao chép một RC, bạn không sao chép dữ liệu bên trong bất kể kích thước hay độ phức tạp của nó. Thay vào đó, bạn đang tạo một tham chiếu khác đến cùng một vị trí bộ nhớ và tăng bộ đếm tham chiếu. Điều này làm cho việc sao chép các thể hiện RC trở nên hiệu quả ngay cả đối với các cấu trúc dữ liệu lớn, vì chỉ có bản thân tham chiếu được sao chép trong khi dữ liệu cơ bản vẫn được giữ nguyên.


### Khả năng thay đổi bên trong với RefCell


RefCell giới thiệu khả năng thay đổi dữ liệu bên trong, cho phép bạn thay đổi dữ liệu ngay cả khi bạn chỉ có một tham chiếu bất biến đến nó. Khả năng này về cơ bản thay đổi cách thức thực thi các quy tắc mượn của Rust bằng cách chuyển các kiểm tra từ thời điểm biên dịch sang thời điểm chạy. Trong khi các tham chiếu thông thường dựa vào trình biên dịch để xác minh tính an toàn khi mượn, RefCell thực hiện các kiểm tra này trong quá trình thực thi chương trình, cung cấp tính linh hoạt cao hơn nhưng đổi lại là nguy cơ xảy ra lỗi nghiêm trọng khi chạy chương trình.


Nguyên tắc cốt lõi đằng sau RefCell là duy trì các quy tắc mượn tương tự như Rust thường thực thi tại thời điểm biên dịch, nhưng kiểm tra chúng một cách động. Tại bất kỳ thời điểm nào, bạn có thể có một tham chiếu có thể thay đổi hoặc bất kỳ số lượng tham chiếu bất biến nào đến dữ liệu bên trong RefCell. Nếu mã của bạn cố gắng vi phạm các quy tắc này bằng cách tạo ra các yêu cầu mượn xung đột đồng thời, chương trình sẽ báo lỗi nghiêm trọng (panic) thay vì tạo ra hành vi không xác định.


Việc kiểm tra trong quá trình thực thi này cho phép một số mẫu lập trình mà trình biên dịch có thể từ chối ngay cả khi chúng thực sự an toàn. Phân tích tĩnh của trình biên dịch không phải lúc nào cũng chứng minh được rằng các mẫu mượn phức tạp là chính xác, dẫn đến việc nó thiên về sự thận trọng. RefCell cho phép bạn ghi đè lên các hạn chế thận trọng này khi bạn tự tin vào tính đúng đắn của mã, nhưng sự tự tin này đi kèm với trách nhiệm đảm bảo sử dụng đúng cách để tránh lỗi trong quá trình thực thi.


Một trường hợp sử dụng phổ biến của RefCell liên quan đến các đối tượng giả lập trong các kịch bản kiểm thử. Khi triển khai một trait chỉ cung cấp quyền truy cập bất biến vào chính nó, nhưng triển khai giả lập của bạn cần theo dõi các thay đổi trạng thái bên trong, RefCell cho phép mô hình này. Bạn có thể gói trạng thái nội bộ trong một RefCell, cho phép đối tượng giả lập thay đổi dữ liệu theo dõi của nó ngay cả thông qua một giao diện bất biến.


### Kết hợp RC và RefCell để chia sẻ trạng thái có thể thay đổi


Sự kết hợp giữa RC và RefCell tạo ra một mô hình cho trạng thái có thể thay đổi được chia sẻ, trong đó nhiều người dùng có thể cùng sửa đổi dữ liệu. RC cung cấp khả năng sở hữu chung, trong khi RefCell cho phép thay đổi dữ liệu thông qua các tham chiếu bất biến. Sự kết hợp này hữu ích trong các trường hợp như cấu trúc đồ thị, bộ nhớ đệm, hoặc bất kỳ tình huống nào mà nhiều phần của chương trình cần cả quyền truy cập đọc và ghi vào dữ liệu được chia sẻ.


Khi bạn bao bọc một RefCell bên trong một RC, bạn tạo ra một cấu trúc có thể được sao chép và phân phối khắp chương trình, với mỗi bản sao cung cấp quyền truy cập vào cùng một dữ liệu có thể thay đổi bên trong. Tất cả các chủ sở hữu đều có thể sửa đổi dữ liệu bằng phương thức borrow_mut của RefCell, nhưng họ vẫn phải tuân thủ các quy tắc mượn tại thời điểm chạy. Mô hình này cho phép các kịch bản chia sẻ dữ liệu phức tạp trong khi vẫn duy trì các đảm bảo an toàn của Rust thông qua các kiểm tra tại thời điểm chạy.


Tuy nhiên, tính linh hoạt này đi kèm với những lưu ý quan trọng liên quan đến rò rỉ bộ nhớ và chu kỳ tham chiếu. Khi sử dụng RC với RefCell, có thể vô tình tạo ra các tham chiếu vòng tròn, trong đó các cấu trúc dữ liệu tự tham chiếu chính nó, trực tiếp hoặc thông qua một chuỗi các tham chiếu. Các chu kỳ này ngăn cản số lượng tham chiếu đạt đến 0, gây ra rò rỉ bộ nhớ vì dữ liệu dường như luôn có các tham chiếu hoạt động ngay cả khi nó không còn được truy cập từ phần còn lại của chương trình.


Giải pháp cho các chu kỳ tham chiếu liên quan đến việc sử dụng các tham chiếu yếu, không đóng góp vào số lượng tham chiếu được sử dụng cho các quyết định quản lý bộ nhớ. Tham chiếu yếu cho phép bạn duy trì kết nối giữa các cấu trúc dữ liệu mà không cần giữ chúng tồn tại, phá vỡ các chu kỳ tiềm ẩn trong khi vẫn bảo toàn khả năng truy cập dữ liệu liên quan khi dữ liệu đó vẫn còn tồn tại.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Nguyên tắc cơ bản về an toàn luồng và đồng thời


Cách tiếp cận của Rust đối với tính đồng thời tập trung vào việc ngăn chặn các lỗi tranh chấp dữ liệu và các vấn đề an toàn bộ nhớ ngay từ giai đoạn biên dịch. Hệ thống kiểu dữ liệu đảm bảo an toàn luồng thông qua các trait như `Send` và `Sync`, đánh dấu các kiểu dữ liệu là an toàn để truyền giữa các luồng hoặc an toàn để truy cập đồng thời tương ứng. Việc xác minh tại thời điểm biên dịch này giúp phát hiện nhiều lỗi đồng thời mà chỉ xuất hiện ở thời điểm chạy trong các ngôn ngữ lập trình hệ thống khác.


Việc tạo luồng trong Rust tuân theo một mô hình đơn giản bằng cách sử dụng `thread::spawn`, hàm này nhận một closure để thực thi trong luồng mới và trả về một handle để quản lý vòng đời của luồng. Luồng được tạo ra sẽ chạy đồng thời với luồng chính, và bạn có thể sử dụng phương thức `join` trên handle để chờ hoàn thành. Nếu không sử dụng `join` rõ ràng, các luồng được tạo ra có thể bị chấm dứt khi luồng chính kết thúc, có khả năng làm gián đoạn công việc chưa hoàn thành.


Từ khóa `move` trở nên rất quan trọng khi làm việc với các luồng vì các closure được truyền cho các luồng được tạo ra thường cần sở hữu dữ liệu của chúng thay vì mượn dữ liệu. Vì các luồng được tạo ra có thể tồn tại lâu hơn phạm vi đã tạo ra chúng, việc mượn dữ liệu từ phạm vi cha có thể tạo ra các vi phạm về vòng đời. Việc chuyển dữ liệu vào closure của luồng sẽ chuyển quyền sở hữu, đảm bảo dữ liệu vẫn hợp lệ trong suốt vòng đời của luồng đồng thời ngăn chặn việc truy cập từ phạm vi ban đầu.


Truyền thông điệp cung cấp một giải pháp thay thế cho việc đồng bộ hóa trạng thái chia sẻ thông qua các kênh cho phép các luồng giao tiếp bằng cách gửi dữ liệu thay vì chia sẻ bộ nhớ. Thư viện chuẩn của Rust cung cấp các kênh Đa nhà sản xuất Đơn người tiêu dùng (MPSC), trong đó nhiều luồng có thể gửi thông điệp đến một luồng nhận duy nhất. Mô hình này loại bỏ nhiều vấn đề đồng bộ hóa bằng cách tránh hoàn toàn trạng thái có thể thay đổi được chia sẻ, thay vào đó dựa vào việc trao đổi thông điệp để phối hợp.


### Đồng bộ hóa trạng thái chia sẻ với Mutex và Arc


Khi phương thức truyền thông điệp không phù hợp, Rust cung cấp khả năng xử lý đồng thời trạng thái chia sẻ truyền thống thông qua Mutex (loại trừ lẫn nhau) kết hợp với Arc (Bộ đếm tham chiếu nguyên tử). Mutex đảm bảo rằng chỉ một luồng có thể truy cập dữ liệu được bảo vệ tại một thời điểm bằng cách yêu cầu các luồng phải giành được khóa trước khi truy cập dữ liệu. Khóa sẽ tự động được giải phóng khi đối tượng bảo vệ được trả về bởi thao tác khóa nằm ngoài phạm vi, ngăn ngừa các tình huống bế tắc thường gặp do quên mở khóa.


Arc đóng vai trò là phiên bản tương đương an toàn cho đa luồng của RC, sử dụng các thao tác nguyên tử để quản lý số lượng tham chiếu một cách an toàn trên nhiều luồng. Trong khi RC hoạt động hoàn hảo cho các kịch bản đơn luồng, việc đếm tham chiếu không nguyên tử của nó tạo ra các điều kiện tranh chấp khi được truy cập từ nhiều luồng. Bộ đếm nguyên tử của Arc đảm bảo rằng các sửa đổi số lượng tham chiếu diễn ra an toàn ngay cả khi truy cập đồng thời, làm cho nó phù hợp để chia sẻ dữ liệu giữa các luồng.


Sự kết hợp giữa Arc và Mutex tạo ra một mô hình cho trạng thái có thể thay đổi được chia sẻ trong các chương trình đồng thời. Bằng cách bao bọc một Mutex trong một Arc, bạn có thể sao chép Arc để phân phối quyền truy cập vào cùng một mutex cho nhiều luồng, với mỗi luồng có thể giành được khóa và sửa đổi dữ liệu được bảo vệ một cách an toàn. Mô hình này cung cấp tính linh hoạt của trạng thái được chia sẻ trong khi vẫn duy trì các đảm bảo an toàn của Rust thông qua xác minh tại thời điểm biên dịch và khóa tại thời điểm chạy.


Các trait Send và Sync hoạt động ngầm để đảm bảo tính an toàn luồng tại thời điểm biên dịch. Send cho biết một kiểu dữ liệu có thể được chuyển giao an toàn cho một luồng khác, trong khi Sync cho biết các tham chiếu đến một kiểu dữ liệu có thể được chia sẻ an toàn giữa các luồng. Hầu hết các kiểu dữ liệu tự động triển khai các trait này khi các thành phần của chúng an toàn cho đa luồng, nhưng một số kiểu dữ liệu như RC và RefCell lại không triển khai chúng một cách rõ ràng vì chúng không được thiết kế cho truy cập đồng thời. Việc triển khai trait tự động này ngăn ngừa việc vô tình gây ra vi phạm an toàn luồng trong khi vẫn cho phép các kiểu dữ liệu an toàn hoạt động liền mạch trong các ngữ cảnh đồng thời.


## Tìm hiểu về Macro Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Giới thiệu về Macro trong Rust


Macro trong Rust là một tính năng lập trình siêu cấp cho phép các nhà phát triển viết mã tạo ra mã khác trong quá trình biên dịch. Không giống như các hàm được gọi trong thời gian chạy, macro được mở rộng sớm trong quá trình biên dịch, trước khi kiểm tra kiểu và các giai đoạn sau đó. Sự khác biệt cơ bản này làm cho macro đặc biệt hữu ích trong việc giảm sự lặp lại mã và tạo ra các ngôn ngữ chuyên biệt trong các chương trình Rust.


Dấu hiệu dễ nhận biết nhất của một lệnh gọi macro là dấu chấm than (!) theo sau tên macro. Ví dụ, khi sử dụng `println!("Hello, world!")`, bạn không gọi một hàm mà đang gọi một macro. Macro này sẽ mở rộng thành mã phức tạp hơn để xử lý các thao tác định dạng và xuất. Dấu chấm than đóng vai trò là tín hiệu trực quan cho các nhà phát triển biết rằng quá trình tạo mã đang diễn ra trong quá trình biên dịch chứ không phải là một lệnh gọi hàm thông thường.


Rust cung cấp ba loại macro khác nhau, mỗi loại phục vụ các mục đích khác nhau trong hệ sinh thái ngôn ngữ:



- Các macro giống hàm**: Có hình thức tương tự như lời gọi hàm nhưng hoạt động tại thời điểm biên dịch (ví dụ: `vec!`, `println!`)
- Macro kế thừa**: Tự động triển khai các đặc tính cho các kiểu (ví dụ: `#[derive(Debug, Clone)]`)
- Các macro giống thuộc tính**: Thay đổi hành vi của các phần tử mã mà chúng được áp dụng (ví dụ: `#[test]`, `#[tokio::main]`)


Hiểu rõ các loại macro khác nhau này là điều cần thiết để lập trình Rust hiệu quả, vì mỗi loại giải quyết các trường hợp sử dụng và mô hình lập trình cụ thể.


### Các loại macro và ứng dụng của chúng


Các macro giống hàm là loại macro thường gặp nhất trong lập trình Rust. Các macro này sử dụng cú pháp tương tự như các lời gọi hàm nhưng thực hiện việc khớp mẫu trên đầu vào của chúng để tạo ra mã phù hợp trong generate. Macro `vec!` là một ví dụ phổ biến thuộc loại này, cho phép các nhà phát triển tạo và khởi tạo các vectơ với cú pháp ngắn gọn. Khi bạn viết `vec![1, 2, 3, 4]`, macro sẽ mở rộng điều này thành mã tạo ra một vectơ mới, thêm từng phần tử riêng lẻ và trả về vectơ đã hoàn thành.


Macro `derive` cung cấp các triển khai trait tự động cho các kiểu tùy chỉnh, giúp giảm đáng kể mã lặp lại. Khi bạn thêm `#[derive(Debug)]` vào định nghĩa struct hoặc enum, bạn đang hướng dẫn trình biên dịch tạo ra một triển khai hoàn chỉnh của trait Debug cho kiểu đó. Triển khai được tạo ra này xử lý logic định dạng cần thiết để hiển thị nội dung của kiểu ở định dạng dễ đọc. Cơ chế `derive` hỗ trợ nhiều trait thư viện chuẩn, bao gồm `Clone`, `PartialEq`, khiến nó trở thành một công cụ thường được sử dụng để giảm mã lặp lại.


Các macro giống như thuộc tính sửa đổi hành vi của các phần tử mã mà chúng chú thích, cung cấp một cách để thêm siêu dữ liệu hoặc thay đổi hành vi biên dịch. Các macro này xuất hiện dưới dạng các thuộc tính được đặt phía trên các định nghĩa kiểu, hàm hoặc các cấu trúc mã khác. Ví dụ, thuộc tính `#[non_exhaustive]` trên một kiểu liệt kê cho biết rằng các biến thể bổ sung có thể được thêm vào trong các phiên bản tương lai, yêu cầu các biểu thức khớp phải bao gồm trường hợp mặc định. Cơ chế này đảm bảo khả năng tương thích ngược đồng thời cung cấp tài liệu rõ ràng về tiềm năng phát triển của kiểu.


### Tạo các macro tùy chỉnh giống như hàm


Việc viết các macro tùy chỉnh giống như hàm đòi hỏi phải hiểu cú pháp khớp mẫu của Rust dành cho định nghĩa macro. Định nghĩa macro sử dụng phương pháp khai báo, trong đó bạn chỉ định các mẫu khớp với các dạng đầu vào khác nhau và các mẫu tạo mã tương ứng. Mỗi macro có thể chứa nhiều nhánh, cho phép nó xử lý nhiều mẫu đầu vào khác nhau và tạo mã phù hợp cho từng trường hợp.


Hãy xem xét việc tạo một macro vectơ tùy chỉnh để minh họa các nguyên tắc cơ bản của việc xây dựng macro. Định nghĩa macro bắt đầu bằng `macro_rules!` theo sau là tên macro và một loạt các nhánh khớp mẫu. Mỗi nhánh bao gồm một mẫu khớp với cú pháp đầu vào cụ thể và một mẫu mã tạo ra mã Rust tương ứng. Ví dụ, một nhánh đơn giản có thể khớp với dấu ngoặc vuông rỗng `[]` và mã generate để tạo một vectơ rỗng, trong khi một nhánh khác khớp với một biểu thức đơn và tạo mã để tạo một vectơ có một phần tử.


Macro trở nên đặc biệt hữu ích khi triển khai các mẫu đối số biến đổi bằng cú pháp lặp. Mẫu `$($x:expr),*` khớp với không hoặc nhiều biểu thức được phân tách bằng dấu phẩy, cho phép macro xử lý một số lượng đối số tùy ý. Mẫu tạo mã tương ứng sử dụng `$(vec.push($x);)*` để lặp lại tất cả các biểu thức khớp và tạo các câu lệnh push riêng lẻ cho mỗi biểu thức. Cơ chế lặp này cho phép macro tạo mã mà việc viết thủ công sẽ không thể hoặc cực kỳ dài dòng.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Quá trình biên dịch chuyển đổi các lệnh gọi macro thành mã mở rộng trước khi kiểm tra kiểu và tối ưu hóa diễn ra. Khi trình biên dịch gặp một lệnh gọi macro, nó sẽ so khớp đầu vào với các mẫu đã định nghĩa và thay thế lệnh gọi macro bằng mã được tạo ra. Mã mở rộng này sau đó trải qua các quy trình biên dịch thông thường, bao gồm kiểm tra kiểu và tối ưu hóa. Các công cụ như `cargo expand` cho phép các nhà phát triển kiểm tra mã được tạo ra, cung cấp khả năng gỡ lỗi có giá trị khi phát triển các macro phức tạp.


### Khái niệm Macro nâng cao và gỡ lỗi


Việc phát triển macro đòi hỏi phải hiểu rõ sự khác biệt giữa thời điểm biên dịch và thời điểm thực thi. Macro được thực thi trong quá trình biên dịch, tạo ra mã sẽ chạy khi thực thi. Sự tách biệt về thời gian này có nghĩa là logic của macro không thể phụ thuộc vào các giá trị khi thực thi, nhưng nó cũng cho phép tối ưu hóa, trong đó các phép tính phức tạp có thể được thực hiện một lần trong quá trình biên dịch thay vì lặp đi lặp lại trong quá trình thực thi.


Hệ thống khớp mẫu trong macro hỗ trợ nhiều bộ chỉ định đoạn mã khác nhau, xác định loại phần tử mã nào có thể được khớp. Bộ chỉ định `expr` khớp với biểu thức, `ty` khớp với kiểu dữ liệu, `ident` khớp với định danh, và một số bộ chỉ định khác cung cấp khả năng kiểm soát chi tiết hơn đối với việc xác thực đầu vào. Các bộ chỉ định này đảm bảo rằng macro nhận được đầu vào hợp lệ về mặt cú pháp và cung cấp thông báo lỗi rõ ràng khi gặp cú pháp không hợp lệ.


Việc gỡ lỗi macro đặt ra những thách thức riêng do bản chất biên dịch của chúng. Lệnh `cargo expand` rất hữu ích cho việc phát triển macro, vì nó hiển thị mã được mở rộng hoàn toàn do các lệnh gọi macro tạo ra. Công cụ này cho phép các nhà phát triển xác minh rằng macro của họ có mã như dự định hay không và xác định các vấn đề trong logic mở rộng. Khi mã do macro tạo ra chứa lỗi, đầu ra được mở rộng sẽ giúp xác định chính xác xem vấn đề nằm ở định nghĩa macro hay cấu trúc mã được tạo ra.


Các macro phức tạp có thể triển khai các mẫu đệ quy, trong đó macro tự gọi chính nó với các đối số đã được sửa đổi để xử lý việc tạo mã lồng nhau hoặc lặp đi lặp lại. Tuy nhiên, các macro đệ quy đòi hỏi thiết kế cẩn thận để tránh mở rộng vô hạn và các vấn đề về hiệu suất biên dịch. Bản chất của việc mở rộng macro trong quá trình biên dịch có nghĩa là ngay cả các triển khai macro không hiệu quả cũng chỉ ảnh hưởng đến tốc độ biên dịch chứ không ảnh hưởng đến hiệu suất thời gian chạy, nhưng các macro quá phức tạp có thể làm chậm đáng kể quá trình xây dựng.



# Rust & Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Vì sao lại chọn Rust cho việc phát triển Bitcoin?

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Việc lựa chọn Rust cho việc phát triển Bitcoin và Lightning không phải là ngẫu nhiên. Phát triển Bitcoin mang những trách nhiệm đặc thù, khác biệt so với phát triển phần mềm thông thường. Khi làm việc với Bitcoin, các nhà phát triển thường xử lý tiền của người dùng trong một môi trường mà sai sót có thể không thể khắc phục được. Không giống như các hệ thống tài chính truyền thống với các biện pháp bảo vệ theo quy định và cơ chế hoàn trả, bản chất phi tập trung của Bitcoin có nghĩa là một khi giao dịch được phát đi, không có cơ quan nào để khiếu nại nhằm thu hồi tiền. Thực tế này đòi hỏi mức độ trách nhiệm và độ chính xác cao hơn trong phát triển phần mềm.


Triết lý "hành động nhanh và chấp nhận rủi ro" vốn hiệu quả trong nhiều lĩnh vực công nghệ lại không áp dụng được cho việc phát triển Bitcoin. Thay vào đó, hệ sinh thái này cần các ngôn ngữ và công cụ giúp các nhà phát triển tạo ra phần mềm mạnh mẽ, an toàn, nơi mà các lỗi được ngăn ngừa hoặc xử lý một cách khéo léo. Đó là lý do tại sao nhiều dự án Bitcoin nổi bật đã chuyển hướng sang Rust, bao gồm Bộ công cụ phát triển Bitcoin (BDK), Bộ công cụ phát triển Lightning (LDK) và BreezSDK.


Rust cung cấp ba đặc tính thiết yếu khiến nó đặc biệt phù hợp cho việc phát triển Bitcoin: hệ thống kiểu dữ liệu mạnh tĩnh, bộ công cụ hiện đại phong phú và khả năng tương thích đa nền tảng. Mỗi đặc điểm này đều góp phần vào khả năng của ngôn ngữ trong việc giúp các nhà phát triển viết mã an toàn hơn, đáng tin cậy hơn để xử lý các hoạt động tiền điện tử.


### Hệ thống tĩnh mạnh của Rust


Hệ thống kiểu dữ liệu của Rust cung cấp cả đặc điểm kiểu tĩnh và kiểu mạnh, hoạt động cùng nhau để phát hiện lỗi trước khi chúng ảnh hưởng đến người dùng. Bản chất tĩnh có nghĩa là việc kiểm tra kiểu dữ liệu diễn ra tại thời điểm biên dịch, yêu cầu các nhà phát triển phải giải quyết các lỗi không khớp kiểu dữ liệu trước khi chương trình có thể được xây dựng. Điều này trái ngược với các ngôn ngữ kiểu động, nơi các lỗi kiểu dữ liệu chỉ xuất hiện trong thời gian chạy, có thể sau khi phần mềm đã được triển khai và đang xử lý tiền của người dùng thực.


Điểm mạnh của hệ thống kiểu dữ liệu Rust nằm ở khả năng diễn đạt và tính chặt chẽ trong việc mô hình hóa các vấn đề. Không giống như các ngôn ngữ có hệ thống kiểu dữ liệu yếu hơn như C, nơi các nhà phát triển bị giới hạn ở các kiểu dữ liệu cơ bản như số và cấu trúc, Rust cho phép mô hình hóa kiểu dữ liệu phong phú, có thể biểu diễn chính xác các khái niệm phức tạp trong miền dữ liệu. Ví dụ, bạn có thể tạo các kiểu dữ liệu phân biệt giữa các loại danh sách khác nhau hoặc bắt buộc các thao tác nhất định chỉ được thực hiện trên các loại đối tượng cụ thể.


Điều làm cho hệ thống kiểu dữ liệu của Rust trở nên phù hợp với việc phát triển Bitcoin là cách tiếp cận của nó đối với tính an toàn bộ nhớ. Hệ thống kiểu dữ liệu dùng để mô hình hóa logic nghiệp vụ cũng đồng thời xử lý quyền sở hữu bộ nhớ và kiểm soát truy cập chia sẻ. Trách nhiệm kép này có nghĩa là các loại lỗ hổng phổ biến, chẳng hạn như rò rỉ bộ nhớ, lỗi giải phóng bộ nhớ hai lần và điều kiện tranh chấp, được trình biên dịch loại bỏ hoàn toàn. Hệ thống kiểu dữ liệu thực thi các đảm bảo an toàn này thông qua các khái niệm như quyền sở hữu, mượn và đếm tham chiếu, khiến việc đưa vào các lỗi liên quan đến bộ nhớ có thể làm tổn hại đến tính bảo mật hoặc ổn định trở nên cực kỳ khó khăn.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Công cụ hiện đại và hỗ trợ đa nền tảng


Hệ sinh thái công cụ của Rust cung cấp cho các nhà phát triển những công cụ giúp tăng năng suất và chất lượng mã. Trình biên dịch Rust được thiết kế không chỉ để dịch mã thành dạng nhị phân, mà còn đóng vai trò là công cụ giáo dục giúp các nhà phát triển học hỏi và cải thiện kỹ năng. Khi xảy ra lỗi biên dịch, trình biên dịch sẽ cung cấp giải thích chi tiết về lỗi và thường đề xuất các giải pháp cụ thể. Cách tiếp cận này đặc biệt có giá trị đối với các nhà phát triển mới làm quen với Rust, vì trình biên dịch giúp dạy các thực hành tốt và ngăn ngừa các lỗi thường gặp.


Ngôn ngữ này bao gồm Cargo, một trình quản lý gói thống nhất xử lý việc quản lý phụ thuộc, xây dựng, kiểm thử và tạo tài liệu. Sự tiêu chuẩn hóa này loại bỏ sự phân mảnh thường thấy trong các ngôn ngữ cũ hơn như C++, nơi nhiều công cụ cạnh tranh tạo ra sự không nhất quán giữa các dự án. Cargo cũng hỗ trợ các tiện ích mở rộng như rustfmt để định dạng mã và Clippy để phân tích tĩnh, đảm bảo mã tuân theo các hướng dẫn về kiểu dáng nhất quán và phát hiện các vấn đề tiềm ẩn trước khi chúng trở thành vấn đề thực sự.


Khả năng đa nền tảng của Rust mở rộng ra ngoài các hệ điều hành truyền thống để bao gồm các nền tảng di động như Android và iOS, cũng như WebAssembly cho các ứng dụng dựa trên trình duyệt. Khả năng hỗ trợ đa nền tảng này rất hữu ích cho các ứng dụng Bitcoin cần chạy trên nhiều môi trường khác nhau. Ví dụ, các dự án như Mutiny Wallet tận dụng khả năng biên dịch WebAssembly của Rust để tạo ra các ví Lightning chạy trực tiếp trên trình duyệt web, điều mà sẽ không khả thi nếu chỉ sử dụng các công nghệ web truyền thống.


### Hiểu về các loại lỗi và hậu quả của chúng


Việc xử lý lỗi hiệu quả bắt đầu từ việc hiểu rõ các loại lỗi khác nhau có thể xảy ra trong quá trình thực thi chương trình. Hãy xem xét một ứng dụng định tuyến đơn giản tính toán đường đi giữa các điểm địa lý. Ví dụ này minh họa ba loại lỗi cơ bản mà các nhà phát triển phải giải quyết: lỗi nhập liệu không hợp lệ, lỗi tài nguyên thời gian chạy và lỗi logic.


Lỗi nhập liệu không hợp lệ xảy ra khi một hàm nhận các tham số không đáp ứng yêu cầu của nó. Ví dụ, nếu một hệ tọa độ địa lý sử dụng số nguyên có dấu cho kinh độ nhưng lại nhận được giá trị âm trong khi chỉ có giá trị dương là hợp lệ, thì hàm không thể tiếp tục hoạt động một cách có ý nghĩa. Những lỗi này thể hiện sự vi phạm hợp đồng giữa người gọi và hàm, và phản hồi thích hợp thường là từ chối đầu vào và trả về chỉ báo lỗi.


Lỗi tài nguyên trong quá trình thực thi xảy ra khi các phụ thuộc bên ngoài không khả dụng hoặc không thể truy cập được. Việc đọc một tệp bản đồ có thể thất bại vì tệp không tồn tại, ứng dụng thiếu quyền truy cập phù hợp hoặc thiết bị lưu trữ không khả dụng. Những lỗi này nằm ngoài logic chương trình và thường yêu cầu khắc phục các vấn đề về môi trường hơn là thay đổi mã. Tuy nhiên, các ứng dụng mạnh mẽ phải dự đoán và xử lý các tình huống này một cách khéo léo.


Lỗi logic thể hiện các sai sót trong quá trình lập trình hoặc sự hiểu lầm về cách các thành phần tương tác với nhau. Nếu thuật toán định tuyến trả về một đường dẫn rỗng khi được cung cấp điểm bắt đầu và điểm kết thúc hợp lệ, điều này cho thấy một lỗi logic cần được sửa chữa trong chính mã nguồn. Không giống như các loại lỗi khác, lỗi logic thường yêu cầu gỡ lỗi và sửa đổi mã để giải quyết.


### Các chiến lược quản lý lỗi hiệu quả


Xây dựng phần mềm đáng tin cậy đòi hỏi các chiến lược chủ động nhằm giảm thiểu cơ hội xảy ra lỗi và xử lý các lỗi không thể tránh khỏi một cách khéo léo. Chiến lược đầu tiên liên quan đến việc hạn chế các lỗi có thể xảy ra thông qua thiết kế kiểu dữ liệu cẩn thận. Bằng cách chọn các kiểu dữ liệu chỉ có thể biểu diễn các giá trị hợp lệ, các nhà phát triển có thể loại bỏ toàn bộ các lớp lỗi nhập liệu không hợp lệ. Ví dụ, sử dụng số nguyên không dấu cho các giá trị không thể âm sẽ ngăn ngừa lỗi giá trị âm trong quá trình biên dịch.


Các câu lệnh khẳng định cung cấp thêm một lớp bảo vệ bằng cách kiểm tra rõ ràng xem các điều kiện mong đợi có đúng trong quá trình thực thi chương trình hay không. Những kiểm tra này phục vụ nhiều mục đích: chúng phát hiện lỗi trong quá trình thử nghiệm, khiến chương trình dừng hoạt động sớm khi xảy ra sự cố (giúp việc gỡ lỗi dễ dàng hơn) và đóng vai trò như tài liệu có thể thực thi mô tả các giả định của lập trình viên. Khi một câu lệnh khẳng định thất bại, điều đó cho thấy một giả định cơ bản về trạng thái của chương trình đã bị vi phạm, thường chỉ ra một lỗi logic cần được điều tra.


Nguyên tắc phân lớp trừu tượng giúp quản lý sự phức tạp bằng cách đảm bảo rằng các lỗi được xử lý ở các cấp độ phù hợp của hệ thống. Các chi tiết triển khai nội bộ, bao gồm các loại lỗi cụ thể từ các thư viện cấp thấp hơn, không nên lan truyền vượt quá ranh giới của hệ thống con. Thay vào đó, mỗi lớp nên dịch các lỗi thành các thuật ngữ có ý nghĩa ở cấp độ trừu tượng đó. Ví dụ, một ứng dụng wallet sử dụng thư viện Bitcoin nên dịch các lỗi phân tích mô tả cấp thấp thành các thông báo cấp cao hơn như "cấu hình wallet không hợp lệ" cung cấp thông tin hữu ích cho người dùng hoặc mã gọi.


Cách tiếp cận xử lý lỗi này, kết hợp với hệ thống kiểu dữ liệu và công cụ của Rust, giúp phát hiện các vấn đề tiềm ẩn ngay từ giai đoạn đầu của quá trình phát triển, trước khi chúng có thể ảnh hưởng đến người dùng hoặc làm tổn hại đến tính bảo mật của các ứng dụng Bitcoin.



## Mô hình lỗi

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust cung cấp một cách tiếp cận toàn diện để xử lý lỗi, cân bằng giữa tính an toàn và tính thực tiễn. Mặc dù các khái niệm về mô hình lỗi tổng quát áp dụng cho nhiều ngôn ngữ lập trình, Rust cung cấp các công cụ và mẫu cụ thể giúp việc xử lý lỗi trở nên rõ ràng và dễ quản lý. Hiểu rõ các cơ chế này là rất quan trọng để viết các ứng dụng Rust mạnh mẽ, có thể xử lý các tình huống bất ngờ một cách khéo léo trong khi vẫn duy trì hiệu suất và tính an toàn.


### Hoảng loạn và cách sử dụng thích hợp của nó


Cơ chế xử lý lỗi khẩn cấp (panic) của Rust là cách trực tiếp nhất để xử lý các lỗi không thể khắc phục. Khi bạn gọi macro `panic!`, chương trình sẽ ngay lập tức dừng thực thi, hoặc hủy bỏ (aborting) hoặc hoàn tác (unwinding) tùy thuộc vào cấu hình của bạn. Macro `panic!` chấp nhận một chuỗi thông báo mô tả lỗi, cung cấp ngữ cảnh để gỡ lỗi. Ngoài ra, các phương thức như `unwrap()` và `expect()` trên các kiểu Result và Option đóng vai trò là các phím tắt để gây ra lỗi khẩn cấp khi các kiểu này chứa giá trị lỗi hoặc None tương ứng. Phương thức `expect()` cho phép bạn cung cấp một thông báo tùy chỉnh, giúp nó cung cấp nhiều thông tin hơn một chút so với `unwrap()` khi gỡ lỗi các sự cố.


Mặc dù đơn giản, việc sử dụng panic cần được cân nhắc kỹ lưỡng trong mã nguồn sản xuất. Có một số trường hợp mà panic không chỉ được chấp nhận mà còn được khuyến khích. Khi viết ví dụ hoặc nguyên mẫu, panic cung cấp một cách rõ ràng để tập trung vào chức năng cốt lõi mà không làm rối mã bằng việc xử lý lỗi toàn diện. Trong môi trường thử nghiệm, panic thường là hành vi mong muốn khi các khẳng định thất bại, vì nó chỉ rõ rằng điều gì đó không mong đợi đã xảy ra. Cộng đồng Rust cũng thừa nhận các tình huống mà các nhà phát triển có nhiều kiến thức hơn trình biên dịch, chẳng hạn như khi phân tích cú pháp các địa chỉ IP được mã hóa cứng mà được biết là hợp lệ.


Tuy nhiên, sự an toàn tưởng chừng như tuyệt đối của các lỗi panic "được trình biên dịch xác minh" có thể gây hiểu lầm. Hãy xem xét một kịch bản mà bạn mã hóa cứng một địa chỉ IP và sử dụng `expect()` vì bạn biết nó hợp lệ. Theo thời gian, khi mã nguồn phát triển, giá trị được mã hóa cứng đó có thể được tái cấu trúc thành một hằng số, và sau đó hằng số đó có thể được thay đổi thành một thứ gì đó như "localhost" để mang lại trải nghiệm người dùng tốt hơn. Đột nhiên, lỗi panic "an toàn" của bạn trở thành một lỗi runtime. Sự phát triển này chứng minh tại sao nói chung tốt hơn là nên tránh các lỗi panic trong mã nguồn sản xuất và thay vào đó trả về các kiểu lỗi thích hợp có thể được xử lý một cách khéo léo.


Một ngoại lệ đáng chú ý đối với quy tắc "tránh gây lỗi panic" liên quan đến các thao tác mutex. Khi bạn gọi `lock()` trên một mutex, nó trả về một Result vì khóa có thể bị lỗi nếu một luồng khác gây lỗi panic trong khi đang giữ mutex. Điều này tạo ra một tình huống khó hiểu khi mã cục bộ của bạn nhận được lỗi cho một điều gì đó xảy ra trong một ngữ cảnh hoàn toàn khác. Vì bạn không thể xử lý một cách hợp lý lỗi bắt nguồn từ lỗi panic của một luồng khác, nhiều nhà phát triển coi việc giải nén khóa mutex là chấp nhận được, đặc biệt nếu bạn duy trì một codebase không gây lỗi panic ở những nơi khác.


### Làm việc với các loại kết quả và tùy chọn


Kiểu dữ liệu Result tạo nên xương sống của hệ thống xử lý lỗi của Rust. Là một kiểu liệt kê có thể chứa cả `Ok(value)` hoặc `Err(error)`, Result buộc bạn phải thừa nhận rõ ràng rằng các thao tác có thể thất bại. Kiểu dữ liệu Option phục vụ mục đích tương tự cho các trường hợp mà giá trị có thể đơn giản là không có, chứa `Some(value)` hoặc `None`. Mặc dù Option không cung cấp thông tin lỗi chi tiết, nhưng nó hoàn hảo cho các tình huống mà sự vắng mặt của một giá trị là có ý nghĩa và được dự đoán trước.


Cả Result và Option đều cung cấp một số phương thức tiện ích giúp việc xử lý lỗi trở nên dễ dàng hơn. Phương thức `unwrap_or()` trả về giá trị chứa bên trong nếu có, hoặc giá trị mặc định nếu có lỗi hoặc là None. Mẫu này đặc biệt hữu ích khi bạn có một phương án dự phòng hợp lý, chẳng hạn như phân tích cú pháp đầu vào của người dùng với một giá trị mặc định hợp lý khi quá trình phân tích cú pháp thất bại. Phương thức `unwrap_or_default()` hoạt động tương tự nhưng sử dụng giá trị mặc định của kiểu dữ liệu thay vì yêu cầu bạn chỉ định một giá trị. Mặc dù về mặt kỹ thuật, các phương thức này không xử lý lỗi theo nghĩa truyền thống, nhưng chúng cung cấp một cách để giảm thiểu chức năng một cách khéo léo khi xảy ra sự cố.


Toán tử dấu chấm hỏi (`?`) là một cú pháp ngắn gọn để truyền lỗi. Khi được áp dụng cho một Result hoặc Option, nó sẽ trích xuất giá trị thành công nếu có, hoặc ngay lập tức trả về lỗi từ hàm hiện tại nếu có vấn đề. Toán tử này loại bỏ các mẫu kiểm tra lỗi dài dòng thường thấy trong các ngôn ngữ như Go, nơi bạn phải tự kiểm tra và trả về lỗi ở mỗi bước. Về cơ bản, toán tử dấu chấm hỏi cung cấp cú pháp đơn giản hóa cho việc trả về sớm, cho phép bạn viết mã sạch, tuyến tính, tập trung vào trường hợp thành công trong khi tự động xử lý việc truyền lỗi.


### Các mẫu xử lý lỗi nâng cao


Phương thức `map()` trên các kiểu Result và Option cho phép xử lý lỗi theo kiểu hàm, giúp mã trở nên dễ hiểu và dễ kết hợp hơn. Khi bạn gọi `map()` trên một Result, hàm được cung cấp sẽ được áp dụng cho giá trị thành công nếu có, trong khi các lỗi sẽ tự động được truyền đi mà không bị thay đổi. Mẫu này hữu ích khi xâu chuỗi các thao tác, vì bạn có thể tập trung vào việc chuyển đổi giá trị mà không cần xử lý lại các trường hợp lỗi. Phương thức `map_err()` cung cấp chức năng ngược lại, cho phép bạn chuyển đổi các kiểu lỗi trong khi vẫn giữ nguyên các giá trị thành công.


Việc chuyển đổi lỗi trở nên rất quan trọng khi xây dựng các ứng dụng nhiều lớp, nơi các thành phần khác nhau cần các loại lỗi khác nhau. Hãy xem xét một hàm phân tích đầu vào của người dùng và cần chuyển đổi các lỗi phân tích cấp thấp thành các lỗi cụ thể theo miền. Sử dụng `map_err()`, bạn có thể dễ dàng chuyển đổi lỗi chung "định dạng số không hợp lệ" thành lỗi ngữ cảnh hơn "tuổi không hợp lệ" có ý nghĩa trong miền ứng dụng của bạn. Quá trình chuyển đổi này diễn ra ngay tại điểm xảy ra lỗi, giúp mã dễ đọc và dễ bảo trì hơn so với các khối try-catch truyền thống, nơi việc xử lý lỗi được tách biệt khỏi các thao tác có thể thất bại.


Sự kết hợp giữa toán tử dấu chấm hỏi và ánh xạ lỗi tạo ra các mẫu xử lý lỗi ngắn gọn. Bạn có thể xâu chuỗi các thao tác, chuyển đổi lỗi khi cần thiết và truyền chúng lên ngăn xếp cuộc gọi với mã lặp lại tối thiểu. Cách tiếp cận này giữ cho việc xử lý lỗi gần với các thao tác có thể thất bại trong khi vẫn duy trì sự tách biệt rõ ràng giữa các đường dẫn thành công và lỗi.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Thư viện bên ngoài và hệ sinh thái xử lý lỗi


Hệ sinh thái Rust bao gồm một số thư viện phổ biến mở rộng khả năng xử lý lỗi của thư viện chuẩn. Thư viện `anyhow` cung cấp một cách tiếp cận đơn giản hóa để xử lý lỗi bằng cách cung cấp một kiểu lỗi phổ quát có thể tự động chuyển đổi từ bất kỳ kiểu lỗi nào triển khai trait Error chuẩn. Việc chuyển đổi tự động này cho phép bạn sử dụng toán tử dấu hỏi với các kiểu lỗi khác nhau mà không cần chuyển đổi thủ công, điều này đặc biệt hữu ích cho các ứng dụng mà bạn không cần phân biệt giữa các kiểu lỗi khác nhau bằng lập trình.


Mặc dù `anyhow` rất hiệu quả trong việc đơn giản hóa việc xử lý lỗi cho các ứng dụng mà lỗi chủ yếu được hiển thị cho người dùng, nhưng nó lại có những hạn chế trong việc phát triển thư viện. Vì `anyhow` về cơ bản chuyển đổi tất cả các lỗi thành thông báo dạng chuỗi, nên người dùng thư viện của bạn không thể dễ dàng phản hồi bằng lập trình đối với các điều kiện lỗi khác nhau. Hạn chế này khiến `anyhow` phù hợp hơn với các ứng dụng dành cho người dùng cuối hơn là các thư viện cần cung cấp thông tin lỗi có cấu trúc cho người dùng của chúng.


Các phương pháp xử lý lỗi nâng cao hơn bao gồm việc tạo ra các kiểu lỗi tùy chỉnh mô phỏng các chế độ lỗi cụ thể của ứng dụng hoặc thư viện của bạn. Một mô hình lỗi được thiết kế tốt có thể phân biệt giữa đầu vào không hợp lệ (mà người gọi có thể sửa), lỗi thời gian chạy (có thể thử lại) và lỗi vĩnh viễn (cho thấy lỗi hoặc điều kiện không thể khắc phục). Cách tiếp cận có cấu trúc này cho phép người sử dụng mã của bạn đưa ra các quyết định thông minh về cách phản hồi các loại lỗi khác nhau, cho dù đó là thử lại các thao tác, nhắc người dùng nhập dữ liệu khác hoặc báo cáo lỗi cho nhà phát triển.


## UniFFI, cầu nối giữa thư viện Rust và nhiều ngôn ngữ lập trình khác nhau.


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Giới thiệu về UniFFI và Phát triển đa nền tảng


UniFFI là một công cụ giúp các thư viện Rust có thể truy cập được trên nhiều ngôn ngữ lập trình và nền tảng khác nhau. Được phát triển bởi Mozilla, công cụ này giải quyết một thách thức cơ bản trong phát triển phần mềm hiện đại: làm thế nào để tận dụng lợi ích về hiệu suất và an toàn của Rust trong khi vẫn duy trì khả năng tương thích với các hệ sinh thái phát triển đa dạng. Công cụ này tự động tạo ra các liên kết ngôn ngữ cho các thư viện Rust, loại bỏ nhu cầu các nhà phát triển phải tự tạo mã giao diện cho từng ngôn ngữ đích.


Vấn đề cốt lõi mà UniFFI giải quyết xuất phát từ bản chất của Rust như một ngôn ngữ biên dịch. Khi mã Rust được biên dịch, nó tạo ra đầu ra nhị phân với một hàm ngoại lai Interface (FFI) cung cấp giao diện cấp thấp, có thể khó sử dụng trực tiếp từ các ngôn ngữ cấp cao hơn như Python, Swift hoặc Kotlin. Theo truyền thống, mỗi nhà phát triển thư viện sẽ cần phải viết mã liên kết tùy chỉnh cho từng ngôn ngữ đích, tạo ra rào cản đáng kể cho việc áp dụng đa nền tảng. UniFFI loại bỏ sự dư thừa này bằng cách cung cấp một phương pháp chuẩn hóa để tự động tạo ra các liên kết này.


Triết lý thiết kế của công cụ này tập trung vào việc cho phép các nhà phát triển Rust tập trung vào logic nghiệp vụ cốt lõi của họ, đồng thời giúp các nhà phát triển làm việc bằng các ngôn ngữ khác có thể truy cập thư viện của họ. Ví dụ, một nhà phát triển iOS sử dụng Swift có thể sử dụng thư viện Rust thông qua các liên kết do UniFFI tạo ra, hiển thị giao diện Swift hoàn toàn gốc, mà không có dấu hiệu nào cho thấy rằng mã nguồn được viết bằng Rust. Sự tích hợp liền mạch này cho phép các nhóm tận dụng lợi ích về hiệu suất của Rust mà không yêu cầu tất cả các thành viên trong nhóm phải học Rust.


### Hiểu về Kiến trúc và Quy trình làm việc của UniFFI


UniFFI hoạt động thông qua một quy trình làm việc được xác định rõ ràng, chuyển đổi các thư viện Rust thành các gói tương thích đa ngôn ngữ. Quá trình này bắt đầu bằng việc tạo ra một tệp Ngôn ngữ Định nghĩa Thống nhất (UDL), đóng vai trò là đặc tả giao diện mô tả những phần nào của thư viện Rust của bạn nên được hiển thị cho các ngôn ngữ khác. Tệp UDL này hoạt động như một hợp đồng giữa việc triển khai Rust của bạn và các liên kết ngôn ngữ được tạo ra.


Kiến trúc này tuân theo nguyên tắc phân tách rõ ràng các mối quan tâm. Các nhà phát triển duy trì thư viện Rust của họ với các quy tắc và mẫu chuẩn của Rust, sau đó tạo một tệp UDL riêng biệt để ánh xạ giao diện công khai sang hệ thống kiểu của UniFFI. Trình tạo liên kết UniFFI xử lý cả thư viện Rust và đặc tả UDL để tạo ra các liên kết ngôn ngữ gốc cho các nền tảng mục tiêu được yêu cầu. Các liên kết được tạo ra này xử lý tất cả các thao tác đóng gói và giải mã dữ liệu phức tạp giữa môi trường thực thi ngôn ngữ nước ngoài và mã Rust.


Trong quá trình thực thi, kiến trúc này tạo ra một phương pháp phân lớp, trong đó mã ứng dụng được viết bằng ngôn ngữ đích (chẳng hạn như Kotlin cho Android) tương tác với mã liên kết được tạo ra, trông hoàn toàn giống với ngôn ngữ đó. Lớp liên kết này xử lý việc chuyển đổi giữa các kiểu dữ liệu dành riêng cho ngôn ngữ và các kiểu dữ liệu Rust, quản lý bộ nhớ một cách an toàn giữa các ngôn ngữ và cung cấp khả năng xử lý lỗi tuân theo các quy ước của ngôn ngữ đích. Logic nghiệp vụ Rust bên dưới vẫn không thay đổi và không biết đến nhiều giao diện ngôn ngữ được xây dựng trên đó.


### Làm việc với UDL: Định nghĩa Interface và Ánh xạ kiểu


Ngôn ngữ định nghĩa thống nhất (UDL) đóng vai trò là nền tảng chức năng của UniFFI, cung cấp một cách thức khai báo để chỉ định những phần nào của thư viện Rust cần được hiển thị và cách chúng được trình bày trong các ngôn ngữ đích. Các tệp UDL phải chứa ít nhất một không gian tên, hoạt động như một vùng chứa các hàm có thể được gọi trực tiếp mà không cần khởi tạo đối tượng. Các hàm trong không gian tên này thường xử lý các thao tác đơn giản nhận giá trị làm tham số và trả về kết quả.


UDL hỗ trợ một tập hợp toàn diện các kiểu dữ liệu tích hợp sẵn, ánh xạ tự nhiên đến các kiểu dữ liệu Rust tương ứng. Các kiểu dữ liệu cơ bản bao gồm các kiểu dữ liệu nguyên thủy chuẩn như boolean, các kích thước số nguyên khác nhau (u8, u32, v.v.), số thực và chuỗi ký tự. Các kiểu dữ liệu phức tạp hơn bao gồm vectơ, bảng băm và các khái niệm đặc thù của Rust như kiểu Tùy chọn (được biểu diễn bằng cú pháp dấu hỏi) và kiểu Kết quả để xử lý lỗi. Hệ thống kiểu dữ liệu cũng hỗ trợ các kiểu liệt kê, cả kiểu liệt kê đơn giản dựa trên giá trị và kiểu liệt kê phức tạp chứa dữ liệu liên kết, cho phép mô hình hóa dữ liệu có thể dịch được giữa các ngôn ngữ khác nhau.


Các cấu trúc trong Rust được chuyển đổi thành các từ điển trong UDL, duy trì sự tương ứng gần như một-một trong khi vẫn thích ứng với các quy ước cú pháp của UDL. Khi các cấu trúc Rust có các phương thức liên kết, chúng có thể được hiển thị dưới dạng giao diện trong UDL, tương tự như các lớp có phương thức trong các ngôn ngữ lập trình hướng đối tượng như Kotlin hoặc Swift. Ánh xạ này bảo toàn các mẫu thiết kế hướng đối tượng mà các nhà phát triển mong đợi trong các ngôn ngữ này, đồng thời duy trì cấu trúc và hành vi của triển khai Rust cơ bản.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


Việc triển khai Rust tương ứng sẽ định nghĩa các kiểu này và triển khai thuộc tính `uniffi::export` cho các liên kết generate dành cho Kotlin, Swift, Python và các ngôn ngữ được hỗ trợ khác.


### Xử lý lỗi và các tính năng nâng cao


UniFFI cung cấp khả năng xử lý lỗi bảo toàn mô hình lỗi dựa trên Kết quả của Rust trong khi dịch nó một cách phù hợp cho các ngôn ngữ đích. Các hàm trả về kiểu Kết quả trong Rust có thể được đánh dấu bằng từ khóa "throws" trong UDL, chỉ định các kiểu lỗi mà chúng có thể tạo ra. Những lỗi này phải được định nghĩa là các kiểu liệt kê lỗi trong tệp UDL và phải triển khai đặc tính Error chuẩn của Rust trong mã Rust cơ bản. Crate thiserror cung cấp một macro tiện lợi để triển khai đặc tính này, giảm đáng kể mã lặp lại.


Việc dịch xử lý lỗi thể hiện cách tiếp cận nhạy bén với ngôn ngữ của UniFFI. Trong Kotlin, các hàm được đánh dấu là throwing trong các phương thức UDL generate sẽ ném ngoại lệ theo quy ước của Java/Kotlin. Tương tự, các liên kết Python cũng sử dụng mô hình ngoại lệ của Python. Việc dịch này đảm bảo rằng việc xử lý lỗi cảm thấy tự nhiên và phù hợp với từng ngôn ngữ đích trong khi vẫn giữ nguyên ý nghĩa ngữ nghĩa của các kiểu lỗi Rust gốc.


Giao diện gọi lại (callback interfaces) đại diện cho một tính năng nâng cao khác cho phép giao tiếp hai chiều giữa các thư viện Rust và các ứng dụng sử dụng chúng. Khi một thư viện Rust cần gọi lại mã ứng dụng, các nhà phát triển có thể định nghĩa các đặc tính (traits) trong Rust và đánh dấu chúng là giao diện gọi lại trong UDL. Ứng dụng sử dụng sẽ triển khai các giao diện này bằng ngôn ngữ gốc của nó, và UniFFI sẽ xử lý việc chuyển đổi dữ liệu phức tạp cần thiết để gọi các hàm gọi lại này từ mã Rust. Mô hình này đòi hỏi phải xem xét cẩn thận tính an toàn của luồng, vì các hàm gọi lại có thể vượt qua ranh giới của các luồng, do đó cần có các giới hạn Gửi (Send) và Đồng bộ (Sync) ở phía Rust.


### Ứng dụng thực tiễn và những hạn chế hiện tại


UniFFI đã được cộng đồng phát triển tiền điện tử và blockchain chấp nhận rộng rãi, với các dự án lớn như BDK (Bộ công cụ phát triển Bitcoin), LDK (Bộ công cụ phát triển Lightning) và nhiều triển khai wallet khác sử dụng nó để cung cấp SDK cho thiết bị di động. Những dự án này chứng minh việc sử dụng UniFFI trong môi trường sản xuất.


Việc xem xét các tệp UDL thực tế từ các dự án này cho thấy các mẫu và phương pháp hay nhất đã được rút ra từ kinh nghiệm sử dụng thực tiễn. Ví dụ, tệp UDL của BDK cho thấy cách các mô hình miền phức tạp với nhiều kiểu liệt kê, cấu trúc và giao diện có thể được ánh xạ hiệu quả để tạo ra các SDK di động toàn diện. Tính nhất quán của cú pháp UDL trên các dự án khác nhau có nghĩa là các nhà phát triển quen thuộc với một thư viện hỗ trợ UniFFI có thể nhanh chóng hiểu và làm việc với các thư viện khác, tạo ra hiệu ứng mạng lưới có lợi cho toàn bộ hệ sinh thái.


Tuy nhiên, UniFFI cũng có những hạn chế đáng chú ý mà các nhà phát triển cần xem xét. Quan trọng nhất là việc thiếu hỗ trợ cho các giao diện bất đồng bộ. Tất cả các liên kết được tạo ra đều là đồng bộ, yêu cầu các nhà phát triển phải xử lý các thao tác bất đồng bộ trong mã Rust của họ và cung cấp các giao diện đồng bộ cho các ứng dụng sử dụng. Ngoài ra, việc đặt tài liệu cũng là một thách thức: tài liệu được viết bằng mã Rust không thể chuyển sang các liên kết được tạo ra, trong khi tài liệu trong các tệp UDL lại không có sẵn cho người dùng Rust trực tiếp sử dụng thư viện. Mặc dù đang có những nỗ lực để giải quyết những hạn chế này thông qua việc phân tích cú pháp và tạo tự động, nhưng chúng vẫn là những vấn đề cần xem xét đối với các triển khai hiện tại. Cuối cùng, UniFFI tạo ra các liên kết ngôn ngữ nhưng không xử lý việc đóng gói và phân phối dành riêng cho từng nền tảng, khiến các nhà phát triển phải tự quản lý các bước cuối cùng để tạo ra các gói phân phối cho mỗi nền tảng mục tiêu.


# Phát triển LNP/BP với SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## Nút LN trên SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Hiểu về kiến trúc mô-đun của LDK


Bộ công cụ phát triển Lightning (LDK) áp dụng một phương pháp khác để triển khai Lightning Network so với phần mềm nút truyền thống như CLightning hoặc LND. Trong khi các nút Lightning thông thường hoạt động như các ứng dụng daemon hoàn chỉnh chạy liên tục trên máy tính, LDK hoạt động như một thư viện Rust dạng mô-đun, cung cấp các thành phần cơ bản để xây dựng các giải pháp Lightning tùy chỉnh. Sự khác biệt về kiến trúc này làm cho LDK linh hoạt, cho phép các nhà phát triển lắp ráp chức năng Lightning theo cách phục vụ các yêu cầu cụ thể của dự án.


Triết lý cốt lõi của LDK xoay quanh tính mô-đun và khả năng thích ứng. Thay vì cung cấp một giải pháp nguyên khối, LDK cung cấp các thành phần riêng lẻ có thể được kết hợp, tùy chỉnh hoặc thay thế hoàn toàn. Mỗi thành phần đều đi kèm với các triển khai mặc định hoạt động ngay lập tức, nhưng các nhà phát triển vẫn giữ quyền tự do thay thế bằng các triển khai của riêng họ khi cần thiết. Ví dụ, LDK bao gồm các triển khai mặc định cho việc giám sát blockchain, ký giao dịch và truyền thông mạng, nhưng bất kỳ thành phần nào trong số này đều có thể được thay thế bằng các giải pháp tùy chỉnh phù hợp với các trường hợp sử dụng hoặc môi trường cụ thể.


Thiết kế dạng mô-đun này cho phép LDK hoạt động trên nhiều nền tảng và kịch bản khác nhau, điều mà các node Lightning truyền thống khó có thể làm được. Các ứng dụng di động, trình duyệt web, thiết bị nhúng và phần cứng chuyên dụng đều có thể tận dụng các thành phần của LDK theo cách phù hợp với các ràng buộc và yêu cầu riêng của chúng. Kiến trúc của thư viện đảm bảo rằng các nhà phát triển có thể tạo ra các ứng dụng hỗ trợ Lightning mà không bị ràng buộc bởi các mô hình hoạt động hoặc sự phụ thuộc hệ thống được xác định trước.


### Các trường hợp sử dụng LDK và tính linh hoạt của nền tảng


Tính linh hoạt về kiến trúc của LDK mở ra vô số trường hợp sử dụng vượt xa các triển khai nút Lightning truyền thống. Phát triển wallet trên thiết bị di động là một trong những ứng dụng hấp dẫn nhất, trong đó LDK cho phép tạo ra các ví Lightning không lưu ký tương tự như Phoenix và wallet. Các triển khai trên thiết bị di động này có thể duy trì quyền kiểm soát của người dùng đối với khóa riêng tư trong khi đồng bộ hóa với các nhà cung cấp dịch vụ Lightning (LSP) khi trực tuyến, cho phép nhận thanh toán và quản lý kênh liền mạch ngay cả khi kết nối không ổn định.


Việc tích hợp Mô-đun Bảo mật Phần cứng (HSM) thể hiện một trường hợp sử dụng mạnh mẽ khác của LDK. Bằng cách chỉ trích xuất các thành phần ký và xác minh giao dịch, các nhà phát triển có thể tạo ra các thiết bị ký giao dịch tương thích với Lightning, hiểu được ngữ cảnh và ý nghĩa của các giao dịch Lightning. Khả năng này vượt xa việc chỉ đơn giản là ký giao dịch, bao gồm cả việc phân tích thông minh về chuyển tiếp thanh toán, hoạt động kênh và các quyết định quan trọng về bảo mật. HSM có thể đánh giá xem một giao dịch có phải là một khoản thanh toán hợp pháp, một hoạt động định tuyến hay một nỗ lực có khả năng độc hại, cung cấp cho người dùng những thông tin chi tiết có ý nghĩa về bảo mật.


Các ứng dụng Lightning dựa trên web được hưởng lợi đáng kể từ triết lý thiết kế không sử dụng lệnh gọi hệ thống của LDK. Vì môi trường WebAssembly thiếu quyền truy cập trực tiếp vào các tài nguyên hệ thống như hệ thống tập tin, socket mạng hoặc nguồn entropy, cách tiếp cận thuần túy của LDK cho phép chức năng Lightning hoạt động liền mạch trong môi trường trình duyệt. Các nhà phát triển có thể triển khai các lớp mạng tùy chỉnh bằng cách sử dụng WebSockets và cung cấp các nguồn duy trì và ngẫu nhiên tương thích với trình duyệt trong khi vẫn đảm bảo tuân thủ đầy đủ giao thức Lightning.


### Các thành phần cốt lõi và kiến trúc hướng sự kiện


Kiến trúc nội bộ của LDK xoay quanh một số thành phần chính hoạt động cùng nhau thông qua một hệ thống hướng sự kiện. Hệ thống quản lý ngang hàng xử lý tất cả các giao tiếp với các nút Lightning khác, triển khai giao thức nhiễu để mã hóa và quản lý cấu trúc thông báo để tuân thủ giao thức Lightning. Thành phần này hoạt động độc lập với cơ chế truyền tải bên dưới, cho phép các nhà phát triển triển khai mạng thông qua socket TCP, WebSockets, kết nối nối tiếp USB hoặc bất kỳ kênh giao tiếp hai chiều nào khác.


Trình quản lý kênh đóng vai trò là điều phối viên trung tâm cho các hoạt động của kênh Lightning, phối hợp chặt chẽ với trình quản lý ngang hàng để thực hiện các hoạt động mở, đóng kênh và thanh toán. Khi nhà phát triển khởi tạo việc mở kênh, trình quản lý kênh sẽ tạo ra các thông điệp giao thức cần thiết và phối hợp với trình quản lý ngang hàng để xử lý quy trình đàm phán nhiều bước. Sự phân tách trách nhiệm này cho phép trừu tượng hóa rõ ràng giữa logic giao thức Lightning và các chi tiết giao tiếp mạng.


Hệ thống sự kiện của LDK cung cấp thông báo không đồng bộ cho tất cả các hoạt động quan trọng và thay đổi trạng thái. Các sự kiện bao trùm toàn bộ phạm vi hoạt động của Lightning, từ kết nối và ngắt kết nối giữa các thiết bị ngang hàng đến thanh toán thành công và thất bại, thay đổi trạng thái kênh và xác nhận blockchain. Cách tiếp cận hướng sự kiện này cho phép các ứng dụng phản hồi phù hợp với hoạt động của mạng Lightning trong khi vẫn duy trì sự tách biệt rõ ràng giữa chức năng cốt lõi của LDK và logic dành riêng cho ứng dụng. Các nhà phát triển có thể triển khai các trình xử lý sự kiện tùy chỉnh để cập nhật giao diện người dùng, kích hoạt thông báo hoặc bắt đầu các hành động tiếp theo dựa trên các sự kiện của mạng Lightning.


### Tích hợp và quản lý dữ liệu Blockchain


Việc tích hợp dữ liệu Blockchain đại diện cho một trong những lớp trừu tượng của LDK, được thiết kế để đáp ứng mọi thứ, từ các nút Bitcoin đầy đủ đến các ứng dụng di động nhẹ. LDK hỗ trợ hai chế độ tương tác blockchain chính, mỗi chế độ được tối ưu hóa cho các ràng buộc tài nguyên và yêu cầu hoạt động khác nhau. Chế độ khối đầy đủ cho phép các ứng dụng có quyền truy cập vào dữ liệu blockchain hoàn chỉnh chuyển toàn bộ khối cho LDK, cho phép giám sát giao dịch toàn diện và phản hồi ngay lập tức đối với các sự kiện blockchain có liên quan.


Đối với môi trường hạn chế tài nguyên, LDK cung cấp phương pháp dựa trên bộ lọc giúp giảm yêu cầu về băng thông và dung lượng lưu trữ. Ở chế độ này, LDK truyền đạt các yêu cầu giám sát của mình thông qua các giao diện trừu tượng, yêu cầu giám sát các ID giao dịch, UTXO hoặc mẫu kịch bản cụ thể. Lớp ứng dụng sau đó có thể thực hiện việc giám sát này bằng cách sử dụng máy chủ Electrum, trình khám phá khối hoặc các nguồn dữ liệu chuỗi khối nhẹ khác. Phương pháp này cho phép ví di động và ứng dụng web duy trì chức năng Lightning mà không cần đồng bộ hóa toàn bộ chuỗi khối.


Lớp lưu trữ dữ liệu trong LDK tuân theo các nguyên tắc trừu tượng tương tự, cung cấp cho các ứng dụng các khối dữ liệu nhị phân cần được lưu trữ và truy xuất một cách đáng tin cậy. LDK xử lý tất cả sự phức tạp của việc tuần tự hóa và giải tuần tự hóa trạng thái kênh Lightning, dữ liệu lan truyền mạng và các thông tin quan trọng khác. Các ứng dụng chỉ cần triển khai các cơ chế lưu trữ đáng tin cậy, cho dù sử dụng hệ thống tệp cục bộ, dịch vụ lưu trữ đám mây hay hệ thống cơ sở dữ liệu chuyên dụng. Thiết kế này đảm bảo việc quản lý trạng thái Lightning vẫn mạnh mẽ đồng thời cho phép các ứng dụng lựa chọn các giải pháp lưu trữ phù hợp với yêu cầu hoạt động và mô hình bảo mật của chúng.


### Các tính năng nâng cao và mô hình tích hợp


Khả năng của LDK mở rộng đến các tính năng của Lightning Network như thanh toán đa đường dẫn, tối ưu hóa tuyến đường và quản lý thông tin mạng. Hệ thống định tuyến duy trì cái nhìn toàn diện về cấu trúc liên kết Lightning Network thông qua việc tham gia giao thức gossip, cho phép tìm đường dẫn thông minh cho các khoản thanh toán. Các ứng dụng có thể ảnh hưởng đến các quyết định định tuyến thông qua các tham số cấu hình và thậm chí có thể triển khai logic định tuyến tùy chỉnh cho các trường hợp sử dụng chuyên biệt.


Hệ thống liên kết ngôn ngữ của thư viện cho phép tích hợp LDK trên nhiều môi trường lập trình, hỗ trợ Java, Kotlin, Swift, TypeScript, JavaScript và C++. Khả năng tương thích đa nền tảng này cho phép các ứng dụng di động được viết bằng ngôn ngữ gốc tích hợp chức năng Lightning trong khi vẫn duy trì hiệu suất tối ưu. Hệ thống liên kết bảo toàn kiến trúc hướng sự kiện và thiết kế mô-đun của LDK trên tất cả các ngôn ngữ được hỗ trợ, đảm bảo trải nghiệm nhất quán cho nhà phát triển bất kể nền tảng mục tiêu.


Ước tính phí và phát sóng giao dịch là những lĩnh vực bổ sung mà LDK cung cấp tính linh hoạt. Các ứng dụng có thể triển khai các chiến lược ước tính phí tùy chỉnh phù hợp với mô hình hoạt động cụ thể và yêu cầu của người dùng. Tương tự, việc phát sóng giao dịch có thể được tùy chỉnh để hoạt động với nhiều giao diện mạng Bitcoin khác nhau, từ kết nối trực tiếp với full node đến các dịch vụ phát sóng của bên thứ ba. Tính linh hoạt này đảm bảo rằng các ứng dụng dựa trên LDK có thể tối ưu hóa tương tác blockchain của chúng cho các trường hợp sử dụng cụ thể trong khi vẫn duy trì tuân thủ giao thức Lightning và các tiêu chuẩn bảo mật.


## SDK Breez

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Thách thức trong việc phát triển Lightning


Việc phát triển các ứng dụng tích hợp thanh toán Lightning đặt ra một rào cản đáng kể đối với hầu hết các nhà phát triển. Để tạo ra một ứng dụng có chức năng thanh toán Lightning, các nhà phát triển về cơ bản cần phải trở thành chuyên gia về Lightning, hiểu các khái niệm phức tạp như quản lý kênh, cân bằng thanh khoản và cấu trúc mạng. Yêu cầu về chuyên môn này tạo ra một vấn đề cơ bản cho việc áp dụng Lightning: mặc dù mạng Lightning hoạt động và các khoản thanh toán đáng tin cậy, nhưng sự phức tạp về kỹ thuật ngăn cản việc tích hợp rộng rãi vào các ứng dụng hàng ngày.


Thách thức cốt lõi nằm ở khoảng cách giữa những gì nhà phát triển cần và những gì họ muốn cung cấp. Nhà phát triển thường làm việc dưới áp lực thời hạn chặt chẽ và ưa thích các giải pháp đơn giản cho phép họ tập trung vào chức năng cốt lõi của ứng dụng thay vì trở thành chuyên gia về cơ sở hạ tầng thanh toán. Khi việc tích hợp Lightning gặp khó khăn, nhà phát triển thường hướng đến các giải pháp lưu ký vì chúng mang lại con đường dễ dàng nhất. Tuy nhiên, xu hướng hướng tới các dịch vụ lưu ký này làm suy yếu giá trị cốt lõi của Bitcoin về chủ quyền tài chính phi lưu ký.


### Tầm nhìn của Breez: Tia chớp khắp nơi


Breez ra đời từ một tầm nhìn đơn giản nhưng đầy tham vọng: kết nối mọi người với mạng Lightning thông qua các giao diện trực quan cho nền kinh tế Lightning. Cách tiếp cận của công ty nhận ra rằng, mặc dù mạng Lightning hoạt động tốt về mặt kỹ thuật, nhưng nó cần sự chấp nhận của người dùng để phát huy hết tiềm năng của mình. Thách thức về việc chấp nhận này không chỉ giới hạn ở người dùng cá nhân mà còn bao trùm toàn bộ hệ sinh thái các ứng dụng và dịch vụ có thể hưởng lợi từ việc tích hợp Lightning.


Ứng dụng Breez ban đầu đã thể hiện tầm nhìn này bằng cách cung cấp cho người dùng một nút Lightning không lưu giữ dữ liệu, chạy trực tiếp trên điện thoại di động của họ. Ứng dụng này đã giới thiệu các khả năng của Lightning như truyền phát các khoản thanh toán nhỏ cho người làm podcast và chức năng điểm bán hàng. Tuy nhiên, ứng dụng Breez cũng cho thấy một hạn chế kiến trúc quan trọng: hệ sinh thái ứng dụng di động không tạo điều kiện thuận lợi cho việc giao tiếp dễ dàng giữa các ứng dụng, buộc các nhà phát triển phải xây dựng tất cả các tính năng liên quan đến Lightning vào một ứng dụng duy nhất thay vì cho phép các ứng dụng chuyên biệt tận dụng cơ sở hạ tầng Lightning dùng chung.


Những bài học mà công ty rút ra từ ứng dụng Breez đã dẫn đến một nhận định quan trọng: tương lai của việc áp dụng Lightning phụ thuộc vào việc thuyết phục các nhà phát triển. Nếu tích hợp Lightning không lưu giữ dữ liệu trở thành lựa chọn dễ dàng nhất cho các nhà phát triển, nó sẽ trở thành lựa chọn mặc định. Cách tiếp cận này cũng mang lại lợi thế về mặt pháp lý, vì phần mềm không lưu giữ dữ liệu phải đối mặt với ít rào cản pháp lý hơn so với các dịch vụ lưu giữ dữ liệu, giúp các nhà phát triển dễ dàng triển khai ứng dụng của họ trên toàn cầu.


### Kiến trúc SDK Breez


Bộ SDK Breez cung cấp một phương pháp thay thế để tích hợp chức năng Lightning vào các ứng dụng. Thay vì yêu cầu mỗi ứng dụng phải chạy một node Lightning riêng, SDK cung cấp một kiến trúc duy trì các nguyên tắc không lưu giữ dữ liệu trong khi đơn giản hóa trải nghiệm của nhà phát triển. Về cơ bản, SDK cung cấp cho mỗi người dùng cuối một node Lightning cá nhân chạy trên cơ sở hạ tầng Greenlight, dịch vụ lưu trữ node Lightning dựa trên đám mây của Blockstream.


Kiến trúc này giải quyết đồng thời một số vấn đề quan trọng. Người dùng không cần lo lắng về quản lý cơ sở dữ liệu, thời gian hoạt động của máy chủ hay bảo trì cơ sở hạ tầng—những mối quan tâm quá lớn đối với người dùng thông thường. Tuy nhiên, không giống như các giải pháp lưu ký truyền thống, Greenlight không bao giờ có quyền truy cập vào khóa của người dùng. Nút Lightning trên đám mây không thể thực hiện bất kỳ thao tác nào nếu không có ứng dụng được kết nối đang hoạt động có thể ký các giao dịch và tin nhắn. Thiết kế này duy trì lợi ích bảo mật của việc tự lưu ký trong khi loại bỏ sự phức tạp trong vận hành.


Bộ SDK cũng hỗ trợ khả năng tương tác. Nhiều ứng dụng có thể kết nối với cùng một nút Lightning của người dùng bằng cùng một cụm từ seed, cho phép người dùng duy trì một số dư Lightning duy nhất trên các ứng dụng chuyên dụng khác nhau. Ví dụ, một người dùng có thể có cả ứng dụng Lightning wallet thông thường và ứng dụng podcast chuyên dụng, cả hai đều truy cập cùng một nguồn vốn và kênh Lightning. Kiến trúc này cho phép phát triển các ứng dụng chuyên biệt, tập trung trong khi vẫn duy trì cơ sở hạ tầng tài chính thống nhất.


### Các nhà cung cấp dịch vụ Lightning và thanh khoản tức thời


Một thành phần quan trọng của SDK Breez là khả năng tích hợp với các Nhà cung cấp Dịch vụ Lightning (LSP), hoạt động tương tự như các Nhà cung cấp Dịch vụ Internet nhưng dành cho mạng Lightning. LSP giải quyết một trong những thách thức phức tạp nhất của Lightning: quản lý thanh khoản. Trong các kênh Lightning, tiền chỉ có thể chảy theo hướng có thanh khoản, tương tự như các hạt trên bàn tính chỉ có thể di chuyển khi có khoảng trống.


Bộ SDK triển khai các kênh "đúng lúc" thông qua các nhà cung cấp dịch vụ Lightning (LSP), tự động quản lý thanh khoản mà không cần sự can thiệp của người dùng. Khi người dùng cần nhận thanh toán nhưng không có đủ thanh khoản đầu vào, LSP sẽ tự động mở một kênh Lightning mới ngay khi khoản thanh toán đến. Quá trình này diễn ra liền mạch trong nền, đảm bảo người dùng luôn có thể nhận thanh toán mà không cần hiểu cơ chế hoạt động của kênh.


Việc tích hợp LSP này không chỉ đơn thuần là quản lý thanh khoản. Bộ SDK bao gồm đầy đủ các chức năng Lightning ngay từ đầu: dịch vụ giám sát tích hợp để đảm bảo an ninh, khả năng tương tác on-chain thông qua các giao dịch hoán đổi ngầm, cổng nạp tiền pháp định thông qua các dịch vụ như MoonPay và hỗ trợ giao thức LNURL. Hệ thống cũng cung cấp khả năng sao lưu và phục hồi liền mạch, đảm bảo người dùng không bao giờ mất quyền truy cập vào tiền của họ ngay cả khi nhà cung cấp cơ sở hạ tầng thay đổi hoặc không khả dụng.


### Trải nghiệm triển khai và phát triển


Bộ SDK Breez ưu tiên trải nghiệm của nhà phát triển thông qua cách tiếp cận toàn diện, đầy đủ tính năng. SDK cung cấp các liên kết cho nhiều ngôn ngữ lập trình bao gồm Rust, Swift, Kotlin, Python, Go, React Native, Flutter và C#, cho phép các nhà phát triển tích hợp thanh toán Lightning bằng các công cụ phát triển ưa thích của họ. Kiến trúc này đơn giản hóa sự phức tạp của Lightning thông qua các API trong khi vẫn duy trì tính bảo mật của mạng Lightning.


Các thành phần chính hoạt động cùng nhau để mang lại trải nghiệm đơn giản hóa này. Trình phân tích cú pháp đầu vào tự động xử lý các định dạng thanh toán khác nhau, xác định xem một chuỗi có đại diện cho hóa đơn, LNURL hay phương thức thanh toán khác hay không và chuyển hướng nó đến chức năng xử lý thích hợp. Trình ký tích hợp quản lý tất cả các hoạt động mã hóa trong nền, trong khi trình hoán đổi xử lý các tương tác on-chain một cách minh bạch. Thiết kế này cho phép các nhà phát triển tập trung vào giá trị độc đáo của ứng dụng thay vì trở thành chuyên gia về cơ sở hạ tầng Lightning.


Kiến trúc phi tập trung của SDK đảm bảo rằng trong khi Greenlight có thể quan sát trạng thái kênh và thông tin định tuyến, họ không thể truy cập vào tiền của người dùng hoặc thực hiện các hoạt động trái phép. Người dùng duy trì quyền kiểm soát hoàn toàn đối với khóa riêng tư của họ, và các khóa này không bao giờ rời khỏi thiết bị của họ. Cách tiếp cận này thể hiện sự cân nhắc kỹ lưỡng giữa tính đơn giản trong vận hành và quyền riêng tư, cung cấp một lộ trình thiết thực cho việc áp dụng Lightning rộng rãi trong khi vẫn bảo toàn các nguyên tắc cốt lõi về chủ quyền tài chính của Bitcoin.


## So sánh LDK và Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Hiểu rõ những hạn chế của Bộ công cụ phát triển Lightning (LDK)


Bộ công cụ phát triển Lightning (LDK) là tập hợp các thư viện Rust được thiết kế để cung cấp cho các nhà phát triển sự linh hoạt khi xây dựng các ứng dụng Lightning Network. Tuy nhiên, sự linh hoạt này đi kèm với những thách thức đáng kể trong quá trình triển khai, điều đã trở nên rõ ràng trong quá trình phát triển thực tế tại Lipa. Bản chất cấp thấp của LDK có nghĩa là các nhà phát triển phải xử lý nhiều tác vụ phức tạp một cách độc lập, từ đồng bộ hóa đồ thị mạng đến tối ưu hóa định tuyến thanh toán. Mặc dù cách tiếp cận này cung cấp quyền kiểm soát hoàn toàn đối với việc triển khai Lightning, nhưng nó đòi hỏi nguồn lực phát triển đáng kể và chuyên môn kỹ thuật sâu rộng để đạt được độ tin cậy sẵn sàng cho môi trường sản xuất.


Một trong những tính năng quan trọng nhất còn thiếu trong LDK là hỗ trợ LNURL, một tiêu chuẩn được áp dụng rộng rãi giúp đơn giản hóa tương tác Lightning Network cho người dùng cuối. Ngoài ra, việc thiếu các đầu ra neo (anchor outputs) đã gây ra những thách thức nghiêm trọng về mặt vận hành, đặc biệt là trong môi trường có phí cao. Đầu ra Anchor giải quyết một vấn đề cơ bản với việc buộc đóng kênh Lightning: khi phí mạng tăng đột biến, các kênh có phí được xác định trước có thể không thể đóng đơn phương vì phí đặt trước không đủ để xác nhận giao dịch. Hạn chế này đặc biệt gây khó khăn cho các ứng dụng wallet trên thiết bị di động, nơi người dùng có thể bỏ wallet mà không phối hợp đóng kênh, khiến tiền có thể bị mắc kẹt trong thời điểm phí tăng đột biến.


Sự chưa hoàn thiện của LDK cũng thể hiện ở việc định tuyến thanh toán không đáng tin cậy, một vấn đề nghiêm trọng đối với bất kỳ ứng dụng Lightning nào. Mặc dù về mặt kỹ thuật là một giải pháp tốt, phạm vi rộng lớn của LDK với tư cách là một giải pháp chung đã gây khó khăn trong việc giải quyết nhanh chóng các vấn đề cụ thể. Nhóm phát triển nhận thấy mình phải dành nhiều thời gian để khắc phục sự cố định tuyến và triển khai các tính năng mà lý tưởng nhất là nên được xử lý ở cấp độ thư viện, cuối cùng ảnh hưởng đến tốc độ phát triển và chất lượng trải nghiệm người dùng.


### Khám phá những ưu điểm của Breez SDK và Greenlight


Việc chuyển đổi sang SDK Breez đánh dấu một sự thay đổi trong phương pháp kiến trúc, chuyển từ một node Lightning tự quản lý sang một giải pháp dựa trên đám mây được hỗ trợ bởi dịch vụ Greenlight của Blockstream. Sự thay đổi này đã ngay lập tức giải quyết một số vấn đề quan trọng gặp phải với việc triển khai LDK. Cải thiện đáng kể nhất đến từ độ tin cậy của thanh toán, chủ yếu là nhờ khả năng duy trì biểu đồ mạng luôn được cập nhật của Greenlight. Không giống như các triển khai Lightning di động truyền thống phải đồng bộ hóa thông tin mạng khi ứng dụng khởi chạy, các node Greenlight hoạt động liên tục trên đám mây, duy trì khả năng nhận biết mạng theo thời gian thực và cung cấp ngay lập tức dữ liệu biểu đồ đầy đủ khi người dùng kết nối.


Kiến trúc này tận dụng triển khai Core Lightning (CLN) đã được kiểm chứng qua thực tiễn, vốn đã định tuyến các khoản thanh toán thành công trong nhiều năm với tư cách là một trong những triển khai Lightning Network ban đầu. Kinh nghiệm tích lũy và độ tin cậy đã được chứng minh của CLN đã mang lại những cải tiến ổn định ngay lập tức so với dự án LDK mới hơn. Khi người dùng kích hoạt wallet được hỗ trợ bởi Greenlight, họ ngay lập tức thừa hưởng toàn bộ kiến thức mạng và khả năng định tuyến của một nút Lightning hoạt động liên tục, loại bỏ sự chậm trễ đồng bộ hóa và sự không chắc chắn trong định tuyến vốn gây khó khăn cho triển khai trước đó.


Triết lý thiết kế có định hướng của SDK Breez rất hữu ích cho việc phát triển wallet. Thay vì cung cấp một bộ công cụ Lightning chung chung, Breez tập trung cụ thể vào các ứng dụng wallet dành cho người dùng cuối, cho phép nhóm phát triển tập trung nỗ lực vào việc tạo ra các giải pháp toàn diện cho trường hợp sử dụng cụ thể này. Cách tiếp cận có mục tiêu này đã cho phép Breez tích hợp các dịch vụ thiết yếu trực tiếp vào SDK, bao gồm chức năng Nhà cung cấp dịch vụ Lightning (LSP) cho phép người dùng nhận thanh toán ngay lập tức sau khi cài đặt wallet, mà không cần thực hiện các thủ tục mở kênh thủ công.


### Các tính năng toàn diện và cải tiến trải nghiệm người dùng


Cách tiếp cận tích hợp của SDK Breez vượt xa chức năng Lightning cơ bản, kết hợp các tính năng nâng cao trải nghiệm người dùng. Việc tích hợp LSP sẵn có loại bỏ rào cản truyền thống là yêu cầu người dùng phải hiểu về quản lý kênh, cho phép nhận thanh toán ngay lập tức cho các cài đặt wallet mới. Quy trình thiết lập ban đầu này giúp thúc đẩy việc áp dụng rộng rãi, vì người dùng có thể bắt đầu nhận thanh toán Lightning mà không cần bất kỳ kiến thức kỹ thuật hoặc quy trình thiết lập nào.


Chức năng hoán đổi trên chuỗi cung ứng mang lại một lớp tối ưu hóa trải nghiệm người dùng khác bằng cách cho phép hiển thị số dư thống nhất cho người dùng. Thay vì buộc người dùng phải hiểu sự khác biệt giữa Lightning và on-chain/Bitcoin, dịch vụ hoán đổi cho phép chuyển đổi tự động giữa các lớp này khi cần thiết. Khi người dùng cần thực hiện thanh toán bằng on-chain, hệ thống có thể tự động hoán đổi tiền Lightning sang on-chain/Bitcoin một cách liền mạch, duy trì ảo tưởng về một số dư thanh khoản duy nhất trong khi xử lý sự phức tạp về mặt kỹ thuật bên trong.


Việc SDK hỗ trợ tính năng dự trữ kênh bằng không giải quyết một thách thức đáng kể về trải nghiệm người dùng trong các triển khai Lightning truyền thống. Thông thường, việc dự trữ kênh ngăn người dùng chi tiêu toàn bộ số dư hiển thị, gây nhầm lẫn khi thanh toán thất bại mặc dù dường như có đủ tiền. Bằng cách loại bỏ các khoản dự trữ này, Breez cho phép người dùng chi tiêu toàn bộ số dư hiển thị, mặc dù điều này đòi hỏi nhà cung cấp dịch vụ (LSP) phải chấp nhận rủi ro bổ sung. Sự đánh đổi này thể hiện cách tiếp cận lấy người dùng làm trung tâm của Breez, trong đó sự phức tạp về kỹ thuật và rủi ro được các nhà cung cấp dịch vụ gánh chịu để tạo ra trải nghiệm người dùng trực quan.


Các tính năng bổ sung như hỗ trợ LNURL, dịch vụ tỷ giá hối đoái và đồng bộ hóa đa thiết bị càng chứng minh cách tiếp cận toàn diện của SDK đối với việc phát triển wallet. Kiến trúc dựa trên đám mây cho phép người dùng truy cập nút Lightning của họ từ nhiều thiết bị hoặc ứng dụng, với Breez xử lý việc đồng bộ hóa trạng thái trên các điểm truy cập khác nhau này. Các mục trong lộ trình phát triển tương lai bao gồm chức năng chi tiêu toàn bộ để thoát hoàn toàn băng thông wallet, ghép nối để quản lý kênh động và một thị trường các nhà cung cấp dịch vụ Lightning (LSP) cạnh tranh để tạo ra sự cạnh tranh lành mạnh trong việc cung cấp dịch vụ.


### Đánh giá sự đánh đổi và các mối lo ngại về tập trung hóa


Việc chuyển đổi sang SDK Breez và Greenlight mang đến những đánh đổi quan trọng về tính tập trung cần được xem xét cẩn thận trong bối cảnh các nguyên tắc phi tập trung của Bitcoin. Kiến trúc dựa trên điện toán đám mây có nghĩa là các node Lightning của người dùng hoạt động trên cơ sở hạ tầng của Blockstream, tạo ra sự phụ thuộc vào cả hoạt động liên tục của Greenlight và sự phát triển không ngừng của Breez. Tính tập trung này không chỉ đơn thuần là sự tiện lợi, mà còn có khả năng ảnh hưởng đến khả năng thu hồi tiền của người dùng nếu dịch vụ không khả dụng hoặc nếu xảy ra kiểm duyệt.


Các kịch bản khôi phục đặt ra những thách thức đặc biệt trong kiến trúc này. Mặc dù người dùng vẫn giữ quyền kiểm soát khóa riêng của họ, nhưng việc truy cập vào quỹ mà không có cơ sở hạ tầng của Greenlight sẽ đòi hỏi chuyên môn kỹ thuật để khởi tạo các nút Core Lightning độc lập và khôi phục trạng thái kênh. Đối với người dùng cá nhân, quá trình khôi phục này có thể sẽ vô cùng phức tạp, và ngay cả các nhà cung cấp wallet cũng sẽ phải đối mặt với những thách thức đáng kể trong việc chuyển đổi toàn bộ cơ sở người dùng sang cơ sở hạ tầng thay thế nếu dịch vụ Greenlight bị ngừng hoạt động.


Các vấn đề về quyền riêng tư cũng thay đổi theo sự thay đổi kiến trúc này. Việc định tuyến dựa trên đám mây có nghĩa là Greenlight có khả năng nắm được thông tin về điểm đến của các khoản thanh toán, trong khi các kiến trúc chỉ dựa trên LSP trước đây chỉ giới hạn việc rò rỉ thông tin ở số tiền thanh toán và thời gian. Việc tạo Invoice trên đám mây càng mở rộng khả năng rò rỉ thông tin, vì các hóa đơn chưa sử dụng trước đây được giữ kín trên thiết bị của người dùng giờ đây sẽ đi qua cơ sở hạ tầng của Blockstream.


Mặc dù có những lo ngại về việc tập trung hóa, nhưng lợi ích thực tiễn thường vượt trội hơn so với rủi ro lý thuyết trong nhiều trường hợp sử dụng. Độ tin cậy được cải thiện, bộ tính năng toàn diện và trải nghiệm người dùng vượt trội cho phép các nhà phát triển wallet tập trung vào các cải tiến ở lớp ứng dụng thay vì quản lý cơ sở hạ tầng Lightning. Sự phân công lao động này phản ánh một hệ sinh thái đang trưởng thành, nơi các nhà cung cấp dịch vụ chuyên biệt xử lý các thách thức kỹ thuật phức tạp, cho phép các nhà phát triển ứng dụng tập trung vào trải nghiệm người dùng và logic kinh doanh. Chìa khóa nằm ở việc hiểu rõ những sự đánh đổi này và đưa ra các quyết định sáng suốt dựa trên các yêu cầu cụ thể của trường hợp sử dụng và mức độ chấp nhận rủi ro.




# Phần cuối

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Đánh giá & Xếp hạng

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Phần kết luận

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>