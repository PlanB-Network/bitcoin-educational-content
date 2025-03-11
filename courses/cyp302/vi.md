---
name: Giới thiệu về mật mã học chính thức
goal: Giới thiệu sâu sắc về khoa học và thực hành mật mã.
objectives: 

  - Khám phá mật mã Beale và các phương pháp mật mã hiện đại để hiểu các khái niệm cơ bản và lịch sử về mật mã.
  - Đi sâu vào lý thuyết số, nhóm và các lĩnh vực để nắm vững các khái niệm toán học quan trọng làm nền tảng cho mật mã học.
  - Nghiên cứu mã hóa luồng RC4 và AES với khóa 128 bit để tìm hiểu về các thuật toán mã hóa đối xứng.
  - Nghiên cứu hệ thống mật mã RSA, phân phối khóa và hàm băm để khám phá mật mã bất đối xứng.

---
# Đi sâu vào mật mã

Thật khó để tìm được nhiều tài liệu cung cấp giải pháp trung gian tốt cho giáo dục mật mã.

Một mặt, có những chuyên luận dài dòng, chính thức, thực sự chỉ có thể tiếp cận được với những người có nền tảng vững chắc về toán học, logic hoặc một số ngành học chính thức khác. Mặt khác, có những phần giới thiệu ở trình độ rất cao thực sự ẩn chứa quá nhiều chi tiết đối với bất kỳ ai ít nhất là tò mò một chút.

Phần giới thiệu về mật mã này tìm cách nắm bắt được điểm trung gian. Mặc dù nó có thể khá khó khăn và chi tiết đối với bất kỳ ai mới làm quen với mật mã, nhưng nó không phải là hang thỏ của một chuyên luận cơ bản thông thường.

+++
# Giới thiệu

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Mô tả ngắn gọn

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Cuốn sách này cung cấp phần giới thiệu sâu về khoa học và thực hành mật mã. Nếu có thể, cuốn sách tập trung vào khái niệm hơn là trình bày chính thức về tài liệu.

> Khóa học này dựa trên [kho lưu trữ của JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Được thôi. Nội dung vẫn chưa hoàn thiện và chỉ ở đây để giới thiệu cách chúng ta có thể tích hợp nó nếu JWburger đồng ý.
### Động lực và mục tiêu

Thật khó để tìm được nhiều tài liệu cung cấp giải pháp trung gian tốt cho giáo dục mật mã.

Một mặt, có những chuyên luận dài dòng, chính thức, thực sự chỉ có thể tiếp cận được với những người có nền tảng vững chắc về toán học, logic hoặc một số ngành học chính thức khác. Mặt khác, có những phần giới thiệu ở trình độ rất cao thực sự ẩn chứa quá nhiều chi tiết đối với bất kỳ ai ít nhất là tò mò một chút.

Phần giới thiệu về mật mã này tìm cách nắm bắt được điểm trung gian. Mặc dù nó có thể khá khó khăn và chi tiết đối với bất kỳ ai mới làm quen với mật mã, nhưng nó không phải là hang thỏ của một chuyên luận cơ bản thông thường.

### Đối tượng mục tiêu

Từ các nhà phát triển đến những người tò mò về trí tuệ, cuốn sách này hữu ích cho bất kỳ ai muốn hiểu biết sâu hơn về mật mã. Nếu mục tiêu của bạn là nắm vững lĩnh vực mật mã, thì cuốn sách này cũng là một điểm khởi đầu tốt.

### Hướng dẫn đọc

Cuốn sách hiện có bảy chương: "Mật mã là gì?" (Chương 1), "Nền tảng toán học của mật mã I" (Chương 2), "Nền tảng toán học của mật mã II" (Chương 3), "Mật mã đối xứng" (Chương 4), "RC4 và AES" (Chương 5), "Mật mã bất đối xứng" (Chương 6) và "Hệ thống mật mã RSA" (Chương 7). Một chương cuối cùng, "Mật mã trong thực hành", vẫn sẽ được thêm vào. Chương này tập trung vào các ứng dụng mật mã khác nhau, bao gồm bảo mật lớp vận chuyển, định tuyến onion và hệ thống trao đổi giá trị của Bitcoin.

Trừ khi bạn có nền tảng vững chắc về toán học, lý thuyết số có lẽ là chủ đề khó nhất trong cuốn sách này. Tôi cung cấp tổng quan về nó trong Chương 3 và nó cũng xuất hiện trong phần trình bày về AES trong Chương 5 và hệ thống mật mã RSA trong Chương 7.

Nếu bạn thực sự gặp khó khăn với các chi tiết chính thức trong những phần này của cuốn sách, tôi khuyên bạn nên đọc chúng ở cấp độ cao hơn ngay từ lần đầu tiên.

### Lời cảm ơn

Cuốn sách có ảnh hưởng nhất trong việc định hình lĩnh vực này là _Introduction to Modern Cryptography_ của Jonathan Katz và Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Một khóa học đi kèm có sẵn trên Coursera có tên là "Cryptography".

Các nguồn bổ sung chính hữu ích trong việc tạo ra bản tổng quan trong cuốn sách này là Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar và Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) và [một khóa học dựa trên cuốn sách của Paar có tên là “Introduction to Cryptography”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); và Bruce Schneier, Applied Cryptography, ấn bản lần 2, 2015 (Indianapolis, IN: John Wiley & Sons).

Tôi sẽ chỉ trích dẫn những thông tin và kết quả rất cụ thể mà tôi lấy từ những nguồn này, nhưng muốn bày tỏ lòng biết ơn chung của tôi đối với họ ở đây.

Đối với những độc giả muốn tìm hiểu thêm kiến thức nâng cao về mật mã sau phần giới thiệu này, tôi thực sự khuyên bạn nên đọc cuốn sách của Katz và Lindell. Khóa học của Katz trên Coursera dễ tiếp cận hơn so với cuốn sách.

### Đóng góp

Vui lòng xem [tệp đóng góp trong kho lưu trữ](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) để biết một số hướng dẫn về cách hỗ trợ dự án.

### Ký hiệu

**Các thuật ngữ chính:**

Các thuật ngữ chính trong các đoạn mã được giới thiệu bằng cách in đậm. Ví dụ, phần giới thiệu về mật mã Rijndael như một thuật ngữ chính sẽ như sau: **Mật mã Rijndael**.

Các thuật ngữ chính được định nghĩa rõ ràng, trừ khi chúng là tên riêng hoặc ý nghĩa của chúng quá rõ ràng trong cuộc thảo luận.

Bất kỳ định nghĩa nào thường được đưa ra khi giới thiệu một thuật ngữ chính, mặc dù đôi khi sẽ thuận tiện hơn nếu để lại định nghĩa cho đến thời điểm sau.

**Những từ và cụm từ được nhấn mạnh:**

Các từ và cụm từ được nhấn mạnh bằng chữ in nghiêng. Ví dụ, cụm từ "Nhớ mật khẩu của bạn" sẽ trông như sau: *Nhớ mật khẩu của bạn*.

**Ký hiệu chính thức:**

Ký hiệu chính thức chủ yếu liên quan đến các biến, biến ngẫu nhiên và tập hợp.


- Biến: Những biến này thường chỉ được biểu thị bằng chữ thường (ví dụ: "x" hoặc "y"). Đôi khi chúng được viết hoa để rõ ràng hơn (ví dụ: "M" hoặc "K").
- Biến ngẫu nhiên: Biến này luôn được biểu thị bằng chữ cái viết hoa (ví dụ: "X" hoặc "Y")
- Bộ: Những bộ này luôn được biểu thị bằng chữ in hoa đậm (ví dụ: **S**)

# Mật mã học là gì?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Mật mã Beale

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Chúng ta hãy bắt đầu cuộc điều tra của chúng ta về lĩnh vực mật mã với một trong những giai đoạn hấp dẫn và thú vị nhất trong lịch sử của nó: đó là về mật mã Beale. [1]

Theo tôi, câu chuyện về mật mã Beale có nhiều khả năng là hư cấu hơn là thực tế. Nhưng nó được cho là đã diễn ra như sau.

Vào cả mùa đông năm 1820 và 1822, một người đàn ông tên là Thomas J. Beale đã ở tại một nhà trọ do Robert Morriss làm chủ ở Lynchburg (Virginia). Vào cuối lần lưu trú thứ hai của Beale, ông đã đưa cho Morriss một chiếc hộp sắt đựng những giấy tờ có giá trị để cất giữ.

Vài tháng sau, Morriss nhận được một lá thư từ Beale có ngày 9 tháng 5 năm 1822. Lá thư nhấn mạnh giá trị to lớn của những thứ bên trong hộp sắt và liên quan đến một số chỉ dẫn cho Morriss: nếu Beale hoặc bất kỳ cộng sự nào của ông không bao giờ đến nhận hộp, ông phải mở nó đúng mười năm kể từ ngày của lá thư (tức là ngày 9 tháng 5 năm 1832). Một số giấy tờ bên trong sẽ được viết bằng văn bản thông thường. Tuy nhiên, một số giấy tờ khác sẽ "không thể hiểu được nếu không có sự trợ giúp của chìa khóa". Sau đó, "chìa khóa" này sẽ được một người bạn giấu tên của Beale chuyển đến Morriss vào tháng 6 năm 1832.

Mặc dù có hướng dẫn rõ ràng, Morriss đã không mở hộp vào tháng 5 năm 1832 và người bạn bí ẩn của Beale không bao giờ xuất hiện vào tháng 6 năm đó. Phải đến năm 1845, chủ quán trọ mới quyết định mở hộp. Trong đó, Morriss tìm thấy một ghi chú giải thích cách Beale và các cộng sự của ông phát hiện ra vàng và bạc ở miền Tây và chôn chúng cùng với một số đồ trang sức để giữ an toàn. Ngoài ra, hộp còn chứa ba **bản mã**: tức là các văn bản được viết bằng mã yêu cầu **khóa mật mã** hoặc bí mật và một thuật toán đi kèm để mở khóa. Quá trình mở khóa bản mã này được gọi là **giải mã**, trong khi quá trình khóa được gọi là **mã hóa**. (Như đã giải thích trong Chương 3, thuật ngữ cipher có thể mang nhiều ý nghĩa khác nhau. Trong tên "Beale ciphers", nó là viết tắt của ciphertexts.)

Ba bản mã mà Morriss tìm thấy trong hộp sắt đều bao gồm một chuỗi số được phân cách bằng dấu phẩy. Theo ghi chú của Beale, các bản mã này cung cấp riêng vị trí của kho báu, nội dung của kho báu và danh sách tên những người thừa kế hợp pháp của kho báu và cổ phần của họ (thông tin sau có liên quan trong trường hợp Beale và các cộng sự của ông không bao giờ đến nhận hộp).

Morris đã cố gắng giải mã ba bản mã trong hai mươi năm. Việc này sẽ dễ dàng với chìa khóa. Nhưng Morriss không có chìa khóa và không thành công trong nỗ lực khôi phục các văn bản gốc, hay **plaintext** như cách gọi thông thường trong mật mã học.

Gần cuối đời, Morriss đã trao lại chiếc hộp cho một người bạn vào năm 1862. Người bạn này sau đó đã xuất bản một tập sách nhỏ vào năm 1885, dưới bút danh J.B. Ward. Tập sách bao gồm mô tả về lịch sử (được cho là) của chiếc hộp, ba bản mã và giải pháp mà ông đã tìm ra cho bản mã thứ hai. (Rõ ràng là có một chìa khóa cho mỗi bản mã, và không có một chìa khóa nào có thể giải được cả ba bản mã như Beale ban đầu đã gợi ý trong lá thư gửi Morriss.)

Bạn có thể thấy bản mã hóa thứ hai trong *Hình 2* bên dưới. [2] Chìa khóa của bản mã hóa này là Tuyên ngôn Độc lập của Hoa Kỳ. Quy trình giải mã được thực hiện bằng cách áp dụng hai quy tắc sau:


- Đối với bất kỳ số n nào trong văn bản mã hóa, hãy xác định vị trí từ thứ n trong Tuyên ngôn Độc lập của Hoa Kỳ
- Thay thế số n bằng chữ cái đầu tiên của từ bạn tìm được

*Hình 1: Mã số Beale số 2*

![Figure 1: Beale cipher no 2.](assets/Figure1-1.webp "Figure 1: Beale cipher no. 2")

Ví dụ, số đầu tiên của bản mã hóa thứ hai là 115. Từ thứ 115 của Tuyên ngôn Độc lập là “institued”, do đó chữ cái đầu tiên của bản rõ là “i”. Bản mã hóa không trực tiếp chỉ ra khoảng cách giữa các từ và chữ hoa. Nhưng sau khi giải mã một vài từ đầu tiên, bạn có thể suy ra một cách hợp lý rằng từ đầu tiên của bản rõ chỉ đơn giản là “I”. (Bản rõ bắt đầu bằng cụm từ “Tôi đã gửi ở hạt Bedford.”)

Sau khi giải mã, thông điệp thứ hai cung cấp nội dung chi tiết của kho báu (vàng, bạc và đồ trang sức), và cho thấy rằng nó được chôn trong các bình sắt và được phủ bằng đá ở Quận Bedford (Virginia). Mọi người thích một bí ẩn hay, vì vậy đã nỗ lực rất nhiều để giải mã hai bản mật mã Beale khác, đặc biệt là bản mô tả vị trí của kho báu. Ngay cả nhiều nhà mật mã nổi tiếng cũng đã thử sức với chúng. Tuy nhiên, cho đến nay, vẫn chưa có ai có thể giải mã được hai bản mật mã khác.

**Lưu ý:**

[1] Để có bản tóm tắt hay về câu chuyện, hãy xem Simon Singh, *The Code Book*, Fourth Estate (London, 1999), trang 82-99. Một bộ phim ngắn về câu chuyện đã được Andrew Allen thực hiện vào năm 2010. Bạn có thể tìm thấy bộ phim, “The Thomas Beale Cipher,” [trên trang web của nó](http://www.thomasbealecipher.com/).

[2] Hình ảnh này có sẵn trên trang Wikipedia về mật mã Beale.

## Mật mã hiện đại

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Những câu chuyện đầy màu sắc như câu chuyện về mật mã Beale là những gì hầu hết chúng ta liên tưởng đến mật mã. Tuy nhiên, mật mã hiện đại khác biệt ít nhất ở bốn điểm quan trọng so với các ví dụ lịch sử này.

Đầu tiên, về mặt lịch sử, mật mã chỉ quan tâm đến **tính bí mật** (hoặc tính bảo mật). [3] Các bản mã sẽ được tạo ra để đảm bảo rằng chỉ một số bên nhất định mới có thể biết được thông tin trong các bản rõ, như trong trường hợp của các bản mã Beale. Để một lược đồ mã hóa phục vụ tốt cho mục đích này, việc giải mã bản mã chỉ khả thi nếu bạn có khóa.

Mật mã học hiện đại quan tâm đến nhiều chủ đề hơn là chỉ tính bí mật. Các chủ đề này chủ yếu bao gồm (1) **tính toàn vẹn của thông điệp**—tức là đảm bảo rằng thông điệp không bị thay đổi; (2) **tính xác thực của thông điệp**—tức là đảm bảo rằng thông điệp thực sự đến từ một người gửi cụ thể; và (3) **không thể chối cãi**—tức là đảm bảo rằng người gửi không thể phủ nhận sai sự thật sau này rằng cô ấy đã gửi thông điệp. [4]

Một sự phân biệt quan trọng cần ghi nhớ là giữa **sơ đồ mã hóa** và **sơ đồ mật mã**. Sơ đồ mã hóa chỉ liên quan đến tính bí mật. Trong khi sơ đồ mã hóa là sơ đồ mật mã, thì ngược lại thì không đúng. Sơ đồ mật mã cũng có thể phục vụ các chủ đề chính khác của mật mã, bao gồm tính toàn vẹn, tính xác thực và tính không thể chối cãi.

Các chủ đề về tính toàn vẹn và tính xác thực cũng quan trọng như tính bí mật. Các hệ thống truyền thông hiện đại của chúng ta sẽ không thể hoạt động nếu không có sự đảm bảo về tính toàn vẹn và tính xác thực của thông tin liên lạc. Tính không thể chối bỏ cũng là một mối quan tâm quan trọng, chẳng hạn như đối với các hợp đồng kỹ thuật số, nhưng ít cần thiết hơn trong các ứng dụng mật mã so với tính bí mật, tính toàn vẹn và tính xác thực.

Thứ hai, các chương trình mã hóa cổ điển như mật mã Beale luôn liên quan đến một khóa được chia sẻ giữa tất cả các bên liên quan. Tuy nhiên, nhiều chương trình mã hóa hiện đại không chỉ liên quan đến một mà là hai khóa: **khóa riêng tư** và **khóa công khai**. Trong khi khóa trước phải được giữ riêng tư trong bất kỳ ứng dụng nào, thì khóa sau thường là kiến thức công khai (do đó, chúng có tên gọi tương ứng). Trong phạm vi mã hóa, khóa công khai có thể được sử dụng để mã hóa thông điệp, trong khi khóa riêng có thể được sử dụng để giải mã.

Ngành mật mã học xử lý các lược đồ mà tất cả các bên chia sẻ một khóa được gọi là **mật mã đối xứng**. Khóa duy nhất trong lược đồ như vậy thường được gọi là **khóa riêng** (hoặc khóa bí mật). Ngành mật mã học xử lý các lược đồ yêu cầu cặp khóa riêng-công khai được gọi là **mật mã bất đối xứng**. Các nhánh này đôi khi cũng được gọi là **mật mã khóa riêng** và **mật mã khóa công khai** (mặc dù điều này có thể gây nhầm lẫn, vì các lược đồ mật mã khóa công khai cũng có khóa riêng).

Sự ra đời của mật mã bất đối xứng vào cuối những năm 1970 là một trong những sự kiện quan trọng nhất trong lịch sử mật mã. Nếu không có nó, hầu hết các hệ thống truyền thông hiện đại của chúng ta, bao gồm cả Bitcoin, sẽ không thể thực hiện được hoặc ít nhất là rất không thực tế.

Điều quan trọng là, mật mã học hiện đại không chỉ nghiên cứu các lược đồ mật mã khóa đối xứng và bất đối xứng (mặc dù điều đó bao gồm phần lớn lĩnh vực này). Ví dụ, mật mã học cũng liên quan đến các hàm băm và trình tạo số giả ngẫu nhiên, và bạn có thể xây dựng các ứng dụng trên các nguyên hàm này không liên quan đến mật mã khóa đối xứng hoặc bất đối xứng.

Thứ ba, các lược đồ mã hóa cổ điển, như những lược đồ được sử dụng trong mật mã Beale, mang tính nghệ thuật hơn là khoa học. Tính bảo mật được nhận thức của chúng phần lớn dựa trên trực giác về độ phức tạp của chúng. Chúng thường được vá khi phát hiện ra một cuộc tấn công mới vào chúng hoặc bị loại bỏ hoàn toàn nếu cuộc tấn công đặc biệt nghiêm trọng. Tuy nhiên, mật mã học hiện đại là một khoa học nghiêm ngặt với cách tiếp cận toán học chính thức để phát triển và phân tích các lược đồ mật mã. [5]

Cụ thể, mật mã học hiện đại tập trung vào **bằng chứng bảo mật** chính thức. Bất kỳ bằng chứng bảo mật nào cho một lược đồ mật mã đều diễn ra theo ba bước:

1. Tuyên bố về **định nghĩa mật mã về bảo mật**, nghĩa là một tập hợp các mục tiêu bảo mật và mối đe dọa do kẻ tấn công gây ra.

2. Tuyên bố về bất kỳ giả định toán học nào liên quan đến độ phức tạp tính toán của sơ đồ. Ví dụ, một sơ đồ mật mã có thể chứa một trình tạo số giả ngẫu nhiên. Mặc dù chúng ta không thể chứng minh những điều này tồn tại, chúng ta có thể cho rằng chúng tồn tại.

3. Trình bày **bằng chứng toán học về tính bảo mật** của lược đồ trên cơ sở khái niệm hình thức về tính bảo mật và bất kỳ giả định toán học nào.

Thứ tư, trong khi về mặt lịch sử, mật mã chủ yếu được sử dụng trong bối cảnh quân sự, thì nó đã thâm nhập vào các hoạt động hàng ngày của chúng ta trong thời đại kỹ thuật số. Cho dù bạn đang giao dịch ngân hàng trực tuyến, đăng bài trên phương tiện truyền thông xã hội, mua sản phẩm từ Amazon bằng thẻ tín dụng hay boa bitcoin cho bạn bè, thì mật mã là điều kiện tiên quyết của thời đại kỹ thuật số của chúng ta.

Với bốn khía cạnh này đối với mật mã học hiện đại, chúng ta có thể mô tả **mật mã học** hiện đại là khoa học liên quan đến sự phát triển và phân tích chính thức các lược đồ mật mã để bảo vệ thông tin kỹ thuật số chống lại các cuộc tấn công đối nghịch. [6] Bảo mật ở đây nên được hiểu rộng rãi là ngăn chặn các cuộc tấn công làm hỏng tính bí mật, tính toàn vẹn, tính xác thực và/hoặc tính không thể chối cãi trong truyền thông.

Mật mã học được coi là một phân ngành của **an ninh mạng**, liên quan đến việc ngăn chặn hành vi trộm cắp, phá hoại và sử dụng sai mục đích các hệ thống máy tính. Lưu ý rằng nhiều mối quan tâm về an ninh mạng có ít hoặc chỉ có một phần liên quan đến mật mã học.

Ví dụ, nếu một công ty đặt máy chủ đắt tiền tại địa phương, họ có thể lo ngại về việc bảo vệ phần cứng này khỏi bị trộm cắp và hư hỏng. Mặc dù đây là mối lo ngại về an ninh mạng, nhưng nó không liên quan nhiều đến mật mã.

Một ví dụ khác, **các cuộc tấn công lừa đảo** là một vấn đề phổ biến trong thời đại hiện đại của chúng ta. Các cuộc tấn công này cố gắng lừa mọi người thông qua email hoặc một số phương tiện truyền thông tin nhắn khác để từ bỏ thông tin nhạy cảm như mật khẩu hoặc số thẻ tín dụng. Mặc dù mật mã có thể giúp giải quyết các cuộc tấn công lừa đảo ở một mức độ nhất định, nhưng một cách tiếp cận toàn diện đòi hỏi nhiều hơn là chỉ sử dụng một số mật mã.

**Lưu ý:**

[3] Nói một cách chính xác, các ứng dụng quan trọng của các chương trình mật mã liên quan đến tính bí mật. Ví dụ, trẻ em thường sử dụng các chương trình mật mã đơn giản để "vui chơi". Tính bí mật không thực sự là mối quan tâm trong những trường hợp đó.

[4] Bruce Schneier, *Mật mã ứng dụng*, ấn bản lần 2, 2015 (Indianapolis, IN: John Wiley & Sons), trang 2.

[5] Xem Jonathan Katz và Yehuda Lindell, *Giới thiệu về mật mã học hiện đại*, CRC Press (Boca Raton, FL: 2015), đặc biệt là các trang 16–23, để có mô tả hay.

[6] So sánh Katz và Lindell, ibid., tr. 3. Tôi nghĩ rằng cách mô tả của họ có một số vấn đề, vì vậy hãy trình bày một phiên bản hơi khác về tuyên bố của họ ở đây.

## Giao tiếp mở

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Mật mã học hiện đại được thiết kế để cung cấp sự đảm bảo an ninh trong môi trường **giao tiếp mở**. Nếu kênh giao tiếp của chúng ta được bảo vệ tốt đến mức những kẻ nghe lén không có cơ hội thao túng hoặc thậm chí chỉ quan sát tin nhắn của chúng ta, thì mật mã học là thừa thãi. Tuy nhiên, hầu hết các kênh giao tiếp của chúng ta khó có thể được bảo vệ tốt như vậy.

Xương sống của truyền thông trong thế giới hiện đại là một mạng lưới cáp quang khổng lồ. Việc gọi điện thoại, xem tivi và duyệt web trong một hộ gia đình hiện đại thường dựa vào mạng lưới cáp quang này (một tỷ lệ nhỏ có thể chỉ dựa vào vệ tinh). Đúng là bạn có thể có các kết nối dữ liệu khác nhau trong nhà, chẳng hạn như cáp đồng trục, đường dây thuê bao kỹ thuật số (không đối xứng) và cáp quang. Nhưng, ít nhất là ở các nước phát triển, các phương tiện dữ liệu khác nhau này nhanh chóng kết nối bên ngoài ngôi nhà của bạn với một nút trong mạng lưới cáp quang khổng lồ kết nối toàn bộ địa cầu. Ngoại lệ là một số vùng xa xôi của thế giới phát triển, chẳng hạn như ở Hoa Kỳ và Úc, nơi lưu lượng dữ liệu vẫn có thể di chuyển khoảng cách đáng kể qua dây điện thoại bằng đồng truyền thống.

Sẽ không thể ngăn chặn những kẻ tấn công tiềm tàng truy cập vật lý vào mạng cáp này và cơ sở hạ tầng hỗ trợ của nó. Trên thực tế, chúng ta đã biết rằng hầu hết dữ liệu của chúng ta bị nhiều cơ quan tình báo quốc gia chặn lại tại các giao lộ quan trọng của Internet.[7] Điều này bao gồm mọi thứ từ tin nhắn Facebook đến địa chỉ trang web mà bạn truy cập.

Trong khi việc giám sát dữ liệu trên quy mô lớn đòi hỏi một đối thủ mạnh, chẳng hạn như một cơ quan tình báo quốc gia, những kẻ tấn công chỉ có ít nguồn lực có thể dễ dàng cố gắng do thám ở quy mô cục bộ hơn. Mặc dù điều này có thể xảy ra ở cấp độ nghe lén đường dây, nhưng việc chặn các liên lạc không dây dễ hơn nhiều.

Hầu hết dữ liệu mạng cục bộ của chúng ta—dù ở nhà, tại văn phòng hay trong quán cà phê—hiện nay đều truyền qua sóng vô tuyến đến các điểm truy cập không dây trên bộ định tuyến tất cả trong một, thay vì qua cáp vật lý. Vì vậy, kẻ tấn công cần ít tài nguyên để chặn bất kỳ lưu lượng cục bộ nào của bạn. Điều này đặc biệt đáng lo ngại vì hầu hết mọi người đều không làm gì nhiều để bảo vệ dữ liệu truyền qua mạng cục bộ của họ. Ngoài ra, những kẻ tấn công tiềm năng cũng có thể nhắm mục tiêu vào các kết nối băng thông rộng di động của chúng ta, chẳng hạn như 3G, 4G và 5G. Tất cả các phương thức liên lạc không dây này đều là mục tiêu dễ dàng cho kẻ tấn công.

Do đó, ý tưởng giữ bí mật thông tin liên lạc bằng cách bảo vệ kênh liên lạc là một khát vọng vô vọng đối với phần lớn thế giới hiện đại. Mọi thứ chúng ta biết đều gây ra chứng hoang tưởng nghiêm trọng: bạn nên luôn cho rằng có người đang nghe lén. Và mật mã là công cụ chính mà chúng ta có để có được bất kỳ loại bảo mật nào trong môi trường hiện đại này.

**Lưu ý:**

[7] Xem, ví dụ, Olga Khazan, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, ngày 16 tháng 7 năm 2013 (có tại [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Cơ sở toán học của mật mã 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Biến ngẫu nhiên

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Mật mã học dựa trên toán học. Và nếu bạn muốn xây dựng nhiều hơn sự hiểu biết hời hợt về mật mã học, bạn cần phải thoải mái với toán học đó.

Chương này giới thiệu hầu hết các kiến thức toán học cơ bản mà bạn sẽ gặp phải khi học mật mã. Các chủ đề bao gồm các biến ngẫu nhiên, phép toán modulo, phép toán XOR và tính ngẫu nhiên giả. Bạn nên nắm vững tài liệu trong các phần này để có thể hiểu sâu hơn về mật mã.

Phần tiếp theo sẽ đề cập đến lý thuyết số, một chủ đề khó hơn nhiều.

### Biến ngẫu nhiên

Một biến ngẫu nhiên thường được biểu thị bằng một chữ cái viết hoa không đậm. Vì vậy, ví dụ, chúng ta có thể nói về một biến ngẫu nhiên $X$, một biến ngẫu nhiên $Y$ hoặc một biến ngẫu nhiên $Z$. Đây là ký hiệu mà tôi cũng sẽ sử dụng từ đây trở đi.

**Biến ngẫu nhiên** có thể nhận hai hoặc nhiều giá trị khả thi, mỗi giá trị có một xác suất dương nhất định. Các giá trị khả thi được liệt kê trong **bộ kết quả**.

Mỗi lần bạn **lấy mẫu** một biến ngẫu nhiên, bạn sẽ rút ra một giá trị cụ thể từ tập kết quả của nó theo xác suất đã xác định.

Hãy chuyển sang một ví dụ đơn giản. Giả sử một biến X được định nghĩa như sau:


- X có tập kết quả $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

Dễ dàng thấy rằng $X$ là một biến ngẫu nhiên. Đầu tiên, có hai hoặc nhiều giá trị có thể mà $X$ có thể nhận, cụ thể là $1$ và $2$. Thứ hai, mỗi giá trị có thể có đều có xác suất dương xảy ra bất cứ khi nào bạn lấy mẫu $X$, cụ thể là $0,5$.

Tất cả những gì một biến ngẫu nhiên cần là một tập hợp kết quả với hai hoặc nhiều khả năng, trong đó mỗi khả năng có xác suất dương xảy ra khi lấy mẫu. Về nguyên tắc, sau đó, một biến ngẫu nhiên có thể được định nghĩa trừu tượng, không có bất kỳ ngữ cảnh nào. Trong trường hợp này, bạn có thể nghĩ về "lấy mẫu" như chạy một số thí nghiệm tự nhiên để xác định giá trị của biến ngẫu nhiên.

Biến $X$ ở trên được định nghĩa trừu tượng. Do đó, bạn có thể nghĩ về việc lấy mẫu biến $X$ ở trên như việc tung một đồng xu công bằng và gán “2” trong trường hợp mặt sấp và “1” trong trường hợp mặt ngửa. Đối với mỗi mẫu $X$, bạn tung lại đồng xu.

Ngoài ra, bạn cũng có thể nghĩ đến việc lấy mẫu $X$, như việc tung một con xúc xắc công bằng và gán “2” trong trường hợp con xúc xắc rơi vào $1$, $3$ hoặc $4$, và gán “1” trong trường hợp con xúc xắc rơi vào $2$, $5$ hoặc $6$. Mỗi lần bạn lấy mẫu $X$, bạn lại tung con xúc xắc.

Thực sự, bất kỳ thí nghiệm tự nhiên nào cho phép bạn xác định xác suất các giá trị có thể có của $X$ ở trên đều có thể được tưởng tượng theo bản vẽ.

Tuy nhiên, thông thường, các biến ngẫu nhiên không chỉ được giới thiệu một cách trừu tượng. Thay vào đó, tập hợp các giá trị kết quả có thể có ý nghĩa thực tế rõ ràng (thay vì chỉ là các con số). Ngoài ra, các giá trị kết quả này có thể được xác định theo một số loại thí nghiệm cụ thể (thay vì là bất kỳ thí nghiệm tự nhiên nào với các giá trị đó).

Bây giờ chúng ta hãy xem xét một ví dụ về biến $X$ không được định nghĩa trừu tượng. X được định nghĩa như sau để xác định đội nào trong hai đội bắt đầu một trận bóng đá:


- $X$ có kết quả được thiết lập {màu đỏ bắt đầu,màu xanh bắt đầu}
- Lật một đồng xu cụ thể $C$: mặt sấp = “đỏ đá ra”; mặt ngửa = “xanh đá ra”

$$
Pr [X = \text{red kicks off}] = 0.5
$$

$$
Pr [X = \text{blue kicks off}] = 0.5
$$

Trong trường hợp này, tập kết quả của X được cung cấp với một ý nghĩa cụ thể, cụ thể là đội nào sẽ bắt đầu trong một trận bóng đá. Ngoài ra, các kết quả có thể xảy ra và xác suất liên quan của chúng được xác định bằng một thí nghiệm cụ thể, cụ thể là tung một đồng xu $C$ cụ thể.

Trong các cuộc thảo luận về mật mã, các biến ngẫu nhiên thường được đưa ra so với một tập hợp kết quả có ý nghĩa thực tế. Nó có thể là tập hợp tất cả các thông điệp có thể được mã hóa, được gọi là không gian thông điệp, hoặc tập hợp tất cả các khóa mà các bên sử dụng mã hóa có thể chọn, được gọi là không gian khóa.

Tuy nhiên, các biến ngẫu nhiên trong các cuộc thảo luận về mật mã thường không được định nghĩa dựa trên một số thí nghiệm tự nhiên cụ thể, mà dựa trên bất kỳ thí nghiệm nào có thể tạo ra phân phối xác suất đúng.

Biến ngẫu nhiên có thể có phân phối xác suất rời rạc hoặc liên tục. Biến ngẫu nhiên có **phân phối xác suất rời rạc**—tức là biến ngẫu nhiên rời rạc—có số lượng kết quả có thể hữu hạn. Biến ngẫu nhiên $X$ trong cả hai ví dụ đã cho đến nay đều là rời rạc.

**Các biến ngẫu nhiên liên tục** có thể thay vào đó nhận các giá trị trong một hoặc nhiều khoảng. Ví dụ, bạn có thể nói rằng một biến ngẫu nhiên, khi lấy mẫu, sẽ nhận bất kỳ giá trị thực nào giữa 0 và 1, và mỗi số thực trong khoảng này đều có khả năng như nhau. Trong khoảng này, có vô số giá trị có thể xảy ra.

Đối với các cuộc thảo luận về mật mã, bạn chỉ cần hiểu các biến ngẫu nhiên rời rạc. Do đó, bất kỳ cuộc thảo luận nào về các biến ngẫu nhiên từ đây trở đi đều phải được hiểu là đề cập đến các biến ngẫu nhiên rời rạc, trừ khi có quy định cụ thể khác.

### Biểu đồ các biến ngẫu nhiên

Các giá trị có thể có và các xác suất liên quan cho một biến ngẫu nhiên có thể dễ dàng được hình dung thông qua một biểu đồ. Ví dụ, hãy xem xét biến ngẫu nhiên $X$ từ phần trước với một tập hợp kết quả là $\{1, 2\}$, và $Pr [X = 1] = 0,5$ và $Pr [X = 2] = 0,5$. Chúng ta thường sẽ hiển thị một biến ngẫu nhiên như vậy dưới dạng biểu đồ thanh như trong *Hình 1*.

*Hình 1: Biến ngẫu nhiên X*

![Figure 1: Random variable X.](assets/Figure2-1.webp)

Các thanh rộng trong *Hình 1* rõ ràng không có ý ám chỉ rằng biến ngẫu nhiên $X$ thực sự liên tục. Thay vào đó, các thanh được làm rộng để hấp dẫn hơn về mặt thị giác (chỉ một đường thẳng đứng cung cấp hình ảnh trực quan ít trực quan hơn).

### Biến đồng nhất

Trong cụm từ “biến ngẫu nhiên”, thuật ngữ “ngẫu nhiên” chỉ có nghĩa là “xác suất”. Nói cách khác, nó chỉ có nghĩa là hai hoặc nhiều kết quả có thể xảy ra của biến xảy ra với một số xác suất nhất định. Tuy nhiên, những kết quả này *không nhất thiết* phải có khả năng xảy ra như nhau (mặc dù thuật ngữ “ngẫu nhiên” thực sự có thể có nghĩa đó trong các ngữ cảnh khác).

**Biến đồng dạng** là trường hợp đặc biệt của biến ngẫu nhiên. Biến này có thể nhận hai hoặc nhiều giá trị với xác suất bằng nhau. Biến ngẫu nhiên $X$ được mô tả trong *Hình 1* rõ ràng là biến đồng dạng, vì cả hai kết quả có thể xảy ra đều có xác suất là $0,5$. Tuy nhiên, có nhiều biến ngẫu nhiên không phải là trường hợp của biến đồng dạng.

Ví dụ, hãy xem xét biến ngẫu nhiên $Y$. Nó có tập kết quả $\{1, 2, 3, 8, 10\}$ và phân phối xác suất sau:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Trong khi hai kết quả có thể thực sự có xác suất xảy ra bằng nhau, cụ thể là $1$ và $8$, $Y$ cũng có thể nhận một số giá trị nhất định với xác suất khác với $0,25$ khi lấy mẫu. Do đó, trong khi $Y$ thực sự là một biến ngẫu nhiên, nó không phải là một biến thống nhất.

Hình ảnh đồ họa của $Y$ được cung cấp trong *Hình 2*.

*Hình 2: Biến ngẫu nhiên Y*

![Figure 2: Random variable Y.](assets/Figure2-2.webp "Figure 2: Random variable Y")

Đối với ví dụ cuối cùng, hãy xem xét biến ngẫu nhiên Z. Nó có tập kết quả {1,3,7,11,12} và phân phối xác suất sau:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Bạn có thể thấy nó được mô tả trong *Hình 3*. Biến ngẫu nhiên Z, trái ngược với Y, là một biến đồng nhất, vì tất cả các xác suất cho các giá trị có thể có khi lấy mẫu đều bằng nhau.

*Hình 3: Biến ngẫu nhiên Z*

![Figure 3: Random variable Z.](assets/Figure2-3.webp "Figure 3: Random variable Z")

### Xác suất có điều kiện

Giả sử Bob có ý định chọn một ngày thống nhất từ năm dương lịch trước. Chúng ta nên kết luận gì về xác suất ngày được chọn là ngày mùa hè?

Miễn là chúng ta nghĩ rằng quá trình của Bob thực sự thống nhất, chúng ta nên kết luận rằng có 1/4 xác suất Bob chọn một ngày vào mùa hè. Đây là **xác suất không điều kiện** của ngày được chọn ngẫu nhiên là vào mùa hè.

Giả sử bây giờ thay vì vẽ một ngày theo lịch một cách thống nhất, Bob chỉ chọn một cách thống nhất từ những ngày mà nhiệt độ buổi trưa tại Crystal Lake (New Jersey) là 21 độ C hoặc cao hơn. Với thông tin bổ sung này, chúng ta có thể kết luận gì về xác suất Bob sẽ chọn một ngày vào mùa hè?

Chúng ta thực sự nên đưa ra một kết luận khác so với trước đây, ngay cả khi không có thêm bất kỳ thông tin cụ thể nào (ví dụ: nhiệt độ vào buổi trưa mỗi ngày trong năm ngoái).

Biết rằng Crystal Lake nằm ở New Jersey, chúng ta chắc chắn sẽ không mong đợi nhiệt độ vào buổi trưa là 21 độ C hoặc cao hơn vào mùa đông. Thay vào đó, nhiều khả năng đó là một ngày ấm áp vào mùa xuân hoặc mùa thu, hoặc một ngày nào đó vào mùa hè. Do đó, biết nhiệt độ vào buổi trưa tại Crystal Lake vào ngày đã chọn là 21 độ C hoặc cao hơn, thì khả năng ngày mà Bob chọn là vào mùa hè trở nên cao hơn nhiều. Đây là **xác suất có điều kiện** của ngày được chọn ngẫu nhiên là vào mùa hè, với điều kiện nhiệt độ vào buổi trưa tại Crystal Lake là 21 độ C hoặc cao hơn.

Không giống như trong ví dụ trước, xác suất của hai sự kiện cũng có thể hoàn toàn không liên quan. Trong trường hợp đó, chúng ta nói rằng chúng **độc lập**.

Ví dụ, giả sử một đồng xu công bằng nào đó đã rơi xuống mặt ngửa. Với thực tế này, vậy thì xác suất trời sẽ mưa vào ngày mai là bao nhiêu? Xác suất có điều kiện trong trường hợp này phải giống với xác suất không điều kiện rằng trời sẽ mưa vào ngày mai, vì việc tung đồng xu thường không có tác động gì đến thời tiết.

Chúng ta sử dụng ký hiệu "|" để viết ra các câu lệnh xác suất có điều kiện. Ví dụ, xác suất của sự kiện $A$ khi sự kiện $B$ đã xảy ra có thể được viết như sau:

$$
Pr[A|B]
$$

Vì vậy, khi hai biến cố $A$ và $B$ độc lập thì:

$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$

Điều kiện độc lập có thể được đơn giản hóa như sau:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Một kết quả quan trọng trong lý thuyết xác suất được gọi là **Định lý Bayes**. Về cơ bản, nó nêu rằng $Pr[A|B]$ có thể được viết lại như sau:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Thay vì sử dụng xác suất có điều kiện với các sự kiện cụ thể, chúng ta cũng có thể xem xét xác suất có điều kiện liên quan đến hai hoặc nhiều biến ngẫu nhiên trên một tập hợp các sự kiện có thể xảy ra. Giả sử hai biến ngẫu nhiên, $X$ và $Y$. Chúng ta có thể biểu thị bất kỳ giá trị có thể nào cho $X$ bằng $x$, và bất kỳ giá trị có thể nào cho $Y$ bằng $y$. Khi đó, chúng ta có thể nói rằng hai biến ngẫu nhiên là độc lập nếu tuyên bố sau đây đúng:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

với mọi $x$ và $y$.

Chúng ta hãy giải thích rõ hơn một chút về ý nghĩa của câu nói này.

Giả sử các tập kết quả cho $X$ và $Y$ được định nghĩa như sau: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ và **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Thông thường, người ta thường chỉ ra các tập giá trị bằng chữ in hoa, đậm.)

Bây giờ giả sử bạn lấy mẫu $Y$ và quan sát $y_1$. Câu lệnh trên cho chúng ta biết rằng xác suất để bây giờ thu được $x_1$ từ việc lấy mẫu $X$ chính xác giống như khi chúng ta chưa bao giờ quan sát $y_1$. Điều này đúng với bất kỳ $y_i$ nào mà chúng ta có thể rút ra từ mẫu ban đầu của $Y$. Cuối cùng, điều này không chỉ đúng với $x_1$. Đối với bất kỳ $x_i$ nào, xác suất xảy ra không bị ảnh hưởng bởi kết quả của việc lấy mẫu $Y$. Tất cả điều này cũng áp dụng cho trường hợp $X$ được lấy mẫu đầu tiên.

Chúng ta hãy kết thúc cuộc thảo luận của mình bằng một quan điểm triết học hơn một chút. Trong bất kỳ tình huống thực tế nào, xác suất của một số sự kiện luôn được đánh giá dựa trên một tập hợp thông tin cụ thể. Không có "xác suất vô điều kiện" theo bất kỳ nghĩa chặt chẽ nào của từ này.

Ví dụ, giả sử tôi hỏi bạn về khả năng lợn sẽ bay vào năm 2030. Mặc dù tôi không cung cấp thêm thông tin nào nữa, nhưng rõ ràng bạn biết rất nhiều về thế giới có thể ảnh hưởng đến phán đoán của bạn. Bạn chưa bao giờ thấy lợn bay. Bạn biết rằng hầu hết mọi người sẽ không mong đợi chúng bay. Bạn biết rằng chúng không thực sự được tạo ra để bay. Vân vân.

Do đó, khi chúng ta nói về “xác suất không điều kiện” của một số sự kiện trong bối cảnh thế giới thực, thuật ngữ đó thực sự chỉ có thể có ý nghĩa nếu chúng ta hiểu nó theo nghĩa giống như “xác suất mà không có bất kỳ thông tin rõ ràng nào khác”. Do đó, bất kỳ sự hiểu biết nào về “xác suất có điều kiện” đều phải luôn được hiểu theo một thông tin cụ thể nào đó.

Ví dụ, tôi có thể hỏi bạn về xác suất lợn sẽ bay vào năm 2030, sau khi đưa cho bạn bằng chứng rằng một số con dê ở New Zealand đã học cách bay sau vài năm huấn luyện. Trong trường hợp này, có lẽ bạn sẽ điều chỉnh phán đoán của mình về xác suất lợn sẽ bay vào năm 2030. Vì vậy, xác suất lợn sẽ bay vào năm 2030 phụ thuộc vào bằng chứng này về dê ở New Zealand.

## Phép toán modulo

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Mô-đun

Biểu thức cơ bản nhất với phép toán **modulo** có dạng sau: $x \mod y$.

Biến $x$ được gọi là số bị chia và biến $y$ là số chia. Để thực hiện phép toán modulo với số bị chia dương và số chia dương, bạn chỉ cần xác định phần dư của phép chia.

Ví dụ, hãy xem xét biểu thức $25 \mod 4$. Số 4 chia cho số 25 tổng cộng 6 lần. Phần dư của phép chia đó là 1. Do đó, $25 \mod 4$ bằng 1. Theo cách tương tự, chúng ta có thể đánh giá các biểu thức dưới đây:


- $29 \mod 30 = 29$ (vì 30 chia hết cho 29 nên tổng cộng là 0 lần và số dư là 29)
- $42 \mod 2 = 0$ (vì 2 chia hết cho 42 nên tổng cộng là 21 lần và số dư là 0)
- $12 \mod 5 = 2$ (vì 5 chia hết cho 12 nên tổng cộng là 2 lần và số dư là 2)
- $20 \mod 8 = 4$ (vì 8 chia hết cho 20 nên tổng cộng là 2 lần và số dư là 4)

Khi số bị chia hoặc số chia âm, các phép toán modulo có thể được xử lý theo nhiều cách khác nhau tùy theo ngôn ngữ lập trình.

Bạn chắc chắn sẽ gặp phải những trường hợp có cổ tức âm trong mật mã. Trong những trường hợp này, cách tiếp cận điển hình như sau:


- Đầu tiên hãy xác định giá trị gần nhất *thấp hơn hoặc bằng* số bị chia mà số chia chia với phần dư là 0. Gọi giá trị đó là $p$.
- Nếu số bị chia là x, thì kết quả của phép chia modulo là giá trị của x – p.

Ví dụ, giả sử số bị chia là $–20$ và số chia là 3. Giá trị gần nhất nhỏ hơn hoặc bằng $–20$ mà 3 chia đều là $–21$. Giá trị của $x – p$ trong trường hợp này là $–20 – (–21)$. Giá trị này bằng 1 và do đó, $–20 \mod 3$ bằng 1. Theo cách tương tự, chúng ta có thể đánh giá các biểu thức dưới đây:


- $–8 \mod 5 = 2$
- $–19 \mod 16 = 13$
- $–14 \mod 6 = 4$

Về ký hiệu, bạn thường sẽ thấy các loại biểu thức sau: $x = [y \mod z]$. Do có dấu ngoặc, phép toán modulo trong trường hợp này chỉ áp dụng cho vế phải của biểu thức. Ví dụ, nếu $y$ bằng 25 và $z$ bằng 4, thì $x$ được đánh giá là 1.

Nếu không có dấu ngoặc, phép toán modulo sẽ tác động lên *cả hai vế* của một biểu thức. Ví dụ, giả sử biểu thức sau: $x = y \mod z$. Nếu $y$ bằng 25 và $z$ bằng 4, thì tất cả những gì chúng ta biết là $x \mod 4$ được đánh giá là 1. Điều này phù hợp với bất kỳ giá trị nào của $x$ từ tập hợp $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.

Nhánh toán học liên quan đến các phép toán modulo trên các số và biểu thức được gọi là **số học modulo**. Bạn có thể coi nhánh này là số học trong các trường hợp mà trục số không dài vô hạn. Mặc dù chúng ta thường bắt gặp các phép toán modulo cho các số nguyên (dương) trong mật mã học, bạn cũng có thể thực hiện các phép toán modulo bằng bất kỳ số thực nào.

### Mật mã dịch chuyển

Phép toán modulo thường gặp trong mật mã học. Để minh họa, chúng ta hãy xem xét một trong những lược đồ mã hóa lịch sử nổi tiếng nhất: mật mã dịch chuyển.

Trước tiên, hãy định nghĩa nó. Giả sử một từ điển *D* coi tất cả các chữ cái của bảng chữ cái tiếng Anh theo thứ tự là tập hợp các số $\{0, 1, 2, \ldots, 25\}$. Giả sử một không gian tin nhắn **M**. Khi đó, **mã hóa dịch chuyển** là một lược đồ mã hóa được định nghĩa như sau:


- Chọn đồng đều một khóa $k$ từ không gian khóa **K**, trong đó **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Mã hóa tin nhắn $m \in \mathbf{M}$, như sau:
    - Phân tách $m$ thành các chữ cái riêng lẻ $m_0, m_1, \ldots, m_i, \ldots, m_l$
    - Chuyển đổi mỗi $m_i$ thành một số theo *D*
    - Với mỗi $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Chuyển đổi mỗi $c_i$ thành một chữ cái theo *D*
    - Sau đó kết hợp $c_0, c_1, \ldots, c_l$ để tạo ra bản mã $c$
- Giải mã một bản mã $c$ như sau:
    - Chuyển đổi mỗi $c_i$ thành một số theo *D*
    - Với mỗi $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Chuyển đổi mỗi $m_i$ thành một chữ cái theo *D*
    - Sau đó kết hợp $m_0, m_1, \ldots, m_l$ để tạo ra thông điệp gốc $m$

Toán tử modulo trong mã hóa dịch chuyển đảm bảo rằng các chữ cái bao quanh, do đó tất cả các chữ cái trong văn bản mã hóa đều được xác định. Để minh họa, hãy xem xét ứng dụng của mã hóa dịch chuyển trên từ “DOG”.

Giả sử bạn chọn một khóa có giá trị là 17. Chữ cái “O” tương đương với 15. Nếu không có phép toán modulo, việc cộng số văn bản thuần túy này với khóa sẽ tạo ra số văn bản mã hóa là 32. Tuy nhiên, số văn bản mã hóa đó không thể chuyển thành một chữ cái văn bản mã hóa, vì bảng chữ cái tiếng Anh chỉ có 26 chữ cái. Phép toán modulo đảm bảo rằng số văn bản mã hóa thực sự là 6 (kết quả của $32 \mod 26$), tương đương với chữ cái văn bản mã hóa “G”.

Toàn bộ mã hóa của từ “DOG” với giá trị khóa là 17 như sau:


- Tin nhắn = DOG = D,O,G = 3,15,6
- $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
- $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
- $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
- $c = UGX$

Mọi người đều có thể hiểu trực quan cách thức hoạt động của mã hóa dịch chuyển và có thể tự sử dụng. Tuy nhiên, để nâng cao kiến thức về mật mã, điều quan trọng là phải bắt đầu trở nên thoải mái hơn với việc chính thức hóa, vì các lược đồ sẽ trở nên khó khăn hơn nhiều. Do đó, tại sao các bước cho mã hóa dịch chuyển được chính thức hóa.

**Lưu ý:**

[1] Chúng ta có thể định nghĩa chính xác câu lệnh này, bằng cách sử dụng thuật ngữ từ phần trước. Giả sử một biến đồng nhất $K$ có $K$ là tập hợp các kết quả có thể xảy ra. Vì vậy:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...và cứ thế. Lấy mẫu biến thống nhất $K$ một lần để tạo ra một khóa cụ thể.

## Phép toán XOR

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Tất cả dữ liệu máy tính được xử lý, lưu trữ và gửi qua mạng ở cấp độ bit. Bất kỳ chương trình mã hóa nào được áp dụng cho dữ liệu máy tính cũng hoạt động ở cấp độ bit.

Ví dụ, giả sử bạn đã nhập một email vào ứng dụng email của mình. Bất kỳ mã hóa nào bạn áp dụng đều không xảy ra trực tiếp trên các ký tự ASCII của email của bạn. Thay vào đó, nó được áp dụng cho biểu diễn bit của các chữ cái và các ký hiệu khác trong email của bạn.

Một phép toán quan trọng cần hiểu đối với mật mã hiện đại, bên cạnh phép toán modulo, là phép toán **XOR**, hay phép toán “hoặc loại trừ”. Phép toán này lấy hai bit làm đầu vào và tạo ra một bit khác làm đầu ra. Phép toán XOR sẽ chỉ được ký hiệu là "XOR". Nó tạo ra 0 nếu hai bit giống nhau và 1 nếu hai bit khác nhau. Bạn có thể thấy bốn khả năng bên dưới. Ký hiệu $\oplus$ biểu diễn "XOR":


- $0 \oplus 0 = 0$
- $0 \oplus 1 = 1$
- $1 \oplus 0 = 1$
- $1 \oplus 1 = 0$

Để minh họa, giả sử bạn có một tin nhắn $m_1$ (01111001) và một tin nhắn $m_2$ (01011001). Hoạt động XOR của hai tin nhắn này có thể được xem bên dưới.


- $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Quá trình này rất đơn giản. Đầu tiên, bạn XOR các bit ngoài cùng bên trái của $m_1$ và $m_2$. Trong trường hợp này, đó là $0 \oplus 0 = 0$. Sau đó, bạn XOR cặp bit thứ hai từ bên trái. Trong trường hợp này, đó là $1 \oplus 1 = 0$. Bạn tiếp tục quá trình này cho đến khi bạn thực hiện xong thao tác XOR trên các bit ngoài cùng bên phải.

Dễ dàng thấy rằng phép toán XOR có tính giao hoán, cụ thể là $m_1 \oplus m_2 = m_2 \oplus m_1$. Ngoài ra, phép toán XOR cũng có tính kết hợp. Nghĩa là, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

Một phép toán XOR trên hai chuỗi có độ dài thay thế có thể có nhiều cách diễn giải khác nhau, tùy thuộc vào ngữ cảnh. Chúng tôi sẽ không quan tâm đến bất kỳ phép toán XOR nào trên các chuỗi có độ dài khác nhau ở đây.

Một phép toán XOR tương đương với trường hợp đặc biệt thực hiện phép toán modulo khi cộng các bit khi số chia là 2. Bạn có thể thấy sự tương đương trong các kết quả sau:


- $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
- $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
- $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
- $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Sự ngẫu nhiên giả

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Trong cuộc thảo luận của chúng tôi về các biến ngẫu nhiên và đồng nhất, chúng tôi đã đưa ra một sự phân biệt cụ thể giữa "ngẫu nhiên" và "đồng nhất". Sự phân biệt đó thường được duy trì trong thực tế khi mô tả các biến ngẫu nhiên. Tuy nhiên, trong bối cảnh hiện tại của chúng tôi, sự phân biệt này cần phải được loại bỏ và "ngẫu nhiên" và "đồng nhất" được sử dụng đồng nghĩa. Tôi sẽ giải thích lý do tại sao ở cuối phần này.

Để bắt đầu, chúng ta có thể gọi một chuỗi nhị phân có độ dài $n$ là **ngẫu nhiên** (hoặc **đồng đều**), nếu nó là kết quả của việc lấy mẫu một biến đồng nhất $S$ cung cấp cho mỗi chuỗi nhị phân có độ dài $n$ như vậy một xác suất lựa chọn như nhau.

Ví dụ, giả sử tập hợp tất cả các chuỗi nhị phân có độ dài 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Thông thường, viết một chuỗi 8 bit thành hai tứ phân, mỗi tứ phân được gọi là **nibble**.) Chúng ta hãy gọi tập hợp các chuỗi này là **$S_8$**.

Theo định nghĩa trên, khi đó, chúng ta có thể gọi một chuỗi nhị phân cụ thể có độ dài 8 là ngẫu nhiên (hoặc đồng đều), nếu đó là kết quả của việc lấy mẫu một biến đồng đều $S$ cung cấp cho mỗi chuỗi trong **$S_8$** một xác suất lựa chọn bằng nhau. Với điều kiện là tập hợp **$S_8$** bao gồm $2^8$ phần tử, xác suất lựa chọn khi lấy mẫu sẽ phải là $1/2^8$ cho mỗi chuỗi trong tập hợp.

Một khía cạnh quan trọng đối với tính ngẫu nhiên của chuỗi nhị phân là nó được xác định theo quá trình mà nó được chọn. Do đó, hình thức của bất kỳ chuỗi nhị phân cụ thể nào tự nó không tiết lộ gì về tính ngẫu nhiên của nó trong quá trình lựa chọn.

Ví dụ, nhiều người trực giác có ý tưởng rằng một chuỗi như $1111\ 1111$ không thể được chọn ngẫu nhiên. Nhưng điều này rõ ràng là sai.

Xác định một biến đồng nhất $S$ trên tất cả các chuỗi nhị phân có độ dài 8, khả năng chọn $1111\ 1111$ từ tập hợp **$S_8$** giống với khả năng chọn một chuỗi như $0111\ 0100$. Do đó, bạn không thể biết bất cứ điều gì về tính ngẫu nhiên của một chuỗi, chỉ bằng cách phân tích chính chuỗi đó.

Chúng ta cũng có thể nói về các chuỗi ngẫu nhiên mà không có nghĩa cụ thể là các chuỗi nhị phân. Ví dụ, chúng ta có thể nói về một chuỗi thập lục phân ngẫu nhiên $AF\ 02\ 82$. Trong trường hợp này, chuỗi sẽ được chọn ngẫu nhiên từ tập hợp tất cả các chuỗi thập lục phân có độ dài 6. Điều này tương đương với việc chọn ngẫu nhiên một chuỗi nhị phân có độ dài 24, vì mỗi chữ số thập lục phân biểu diễn 4 bit.

Thông thường, cụm từ “một chuỗi ngẫu nhiên”, không có điều kiện, ám chỉ một chuỗi được chọn ngẫu nhiên từ tập hợp tất cả các chuỗi có cùng độ dài. Đây là cách tôi đã mô tả ở trên. Tất nhiên, một chuỗi có độ dài $n$ cũng có thể được chọn ngẫu nhiên từ một tập hợp khác. Ví dụ, một chuỗi chỉ tạo nên một tập hợp con của tất cả các chuỗi có độ dài $n$, hoặc có lẽ là một tập hợp bao gồm các chuỗi có độ dài thay đổi. Tuy nhiên, trong những trường hợp đó, chúng ta sẽ không gọi nó là “chuỗi ngẫu nhiên”, mà là “một chuỗi được chọn ngẫu nhiên từ một tập hợp **S** nào đó”.

Một khái niệm chính trong mật mã học là tính giả ngẫu nhiên. Một **chuỗi giả ngẫu nhiên** có độ dài $n$ xuất hiện *như thể* nó là kết quả của việc lấy mẫu một biến đồng nhất $S$ cung cấp cho mỗi chuỗi trong **$S_n$** một xác suất lựa chọn bằng nhau. Tuy nhiên, trên thực tế, chuỗi là kết quả của việc lấy mẫu một biến đồng nhất $S'$ chỉ xác định một phân phối xác suất—không nhất thiết là một phân phối có xác suất bằng nhau cho tất cả các kết quả có thể—trên một tập hợp con của **$S_n$**. Điểm quan trọng ở đây là không ai có thể thực sự phân biệt được giữa các mẫu từ $S$ và $S'$, ngay cả khi bạn lấy nhiều mẫu trong số chúng.

Ví dụ, giả sử một biến ngẫu nhiên $S$. Tập kết quả của nó là **$S_{256}$**, đây là tập hợp tất cả các chuỗi nhị phân có độ dài 256. Tập hợp này có $2^{256}$ phần tử. Mỗi phần tử có xác suất chọn bằng nhau, $1/2^{256}$, khi lấy mẫu.

Ngoài ra, giả sử một biến ngẫu nhiên $S'$. Tập kết quả của nó chỉ bao gồm $2^{128}$ chuỗi nhị phân có độ dài 256. Nó có một số phân phối xác suất trên các chuỗi đó, nhưng phân phối này không nhất thiết phải đồng đều.

Giả sử bây giờ tôi lấy 1000 mẫu từ $S$ và 1000 mẫu từ $S'$ và đưa cho bạn hai tập kết quả. Tôi cho bạn biết tập kết quả nào liên quan đến biến ngẫu nhiên nào. Tiếp theo, tôi lấy một mẫu từ một trong hai biến ngẫu nhiên. Nhưng lần này tôi không cho bạn biết tôi lấy mẫu biến ngẫu nhiên nào. Nếu $S'$ là giả ngẫu nhiên, thì ý tưởng là xác suất bạn đoán đúng biến ngẫu nhiên nào tôi lấy mẫu thực tế không tốt hơn $1/2$.

Thông thường, một chuỗi giả ngẫu nhiên có độ dài $n$ được tạo ra bằng cách chọn ngẫu nhiên một chuỗi có kích thước $n – x$, trong đó $x$ là một số nguyên dương và sử dụng nó làm đầu vào cho một thuật toán mở rộng. Chuỗi ngẫu nhiên có kích thước $n – x$ này được gọi là **hạt giống**.

Chuỗi giả ngẫu nhiên là một khái niệm chính để làm cho mật mã trở nên thiết thực. Ví dụ, hãy xem xét mã hóa luồng. Với mã hóa luồng, một khóa được chọn ngẫu nhiên được đưa vào thuật toán mở rộng để tạo ra chuỗi giả ngẫu nhiên lớn hơn nhiều. Chuỗi giả ngẫu nhiên này sau đó được kết hợp với văn bản thuần túy thông qua thao tác XOR để tạo ra văn bản mã hóa.

Nếu chúng ta không thể tạo ra loại chuỗi giả ngẫu nhiên này cho mã hóa luồng, thì chúng ta sẽ cần một khóa dài bằng thông điệp để đảm bảo an toàn. Đây không phải là lựa chọn thực tế trong hầu hết các trường hợp.

Khái niệm về tính ngẫu nhiên giả được thảo luận trong phần này có thể được định nghĩa chính thức hơn. Nó cũng mở rộng sang các bối cảnh khác. Nhưng chúng ta không cần đi sâu vào cuộc thảo luận đó ở đây. Tất cả những gì bạn thực sự cần hiểu một cách trực quan đối với phần lớn mật mã là sự khác biệt giữa chuỗi ngẫu nhiên và chuỗi giả ngẫu nhiên. [2]

Lý do để loại bỏ sự phân biệt giữa “ngẫu nhiên” và “đồng nhất” trong cuộc thảo luận của chúng ta bây giờ cũng nên rõ ràng. Trong thực tế, mọi người sử dụng thuật ngữ giả ngẫu nhiên để chỉ một chuỗi xuất hiện **như thể** nó là kết quả của việc lấy mẫu một biến đồng nhất $S$. Nói một cách chính xác, chúng ta nên gọi một chuỗi như vậy là “giả đồng nhất”, sử dụng ngôn ngữ của chúng ta từ trước. Vì thuật ngữ “giả đồng nhất” vừa vụng về vừa không được ai sử dụng, chúng tôi sẽ không giới thiệu nó ở đây để làm rõ. Thay vào đó, chúng tôi chỉ loại bỏ sự phân biệt giữa “ngẫu nhiên” và “đồng nhất” trong bối cảnh hiện tại.

**Ghi chú**

[2] Nếu quan tâm đến phần trình bày chính thức hơn về những vấn đề này, bạn có thể tham khảo *Giới thiệu về mật mã học hiện đại* của Katz và Lindell, đặc biệt là chương 3.

# Cơ sở toán học của mật mã 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

## Lý thuyết số là gì?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Chương này đề cập đến một chủ đề nâng cao hơn về nền tảng toán học của mật mã: lý thuyết số. Mặc dù lý thuyết số rất quan trọng đối với mật mã đối xứng (như trong Rijndael Cipher), nhưng nó đặc biệt quan trọng trong bối cảnh mật mã khóa công khai.

Nếu bạn thấy các chi tiết về lý thuyết số phức tạp, tôi khuyên bạn nên đọc ở trình độ cao ngay từ đầu. Bạn luôn có thể quay lại sau.

___

Bạn có thể mô tả **lý thuyết số** là nghiên cứu về tính chất của số nguyên và các hàm toán học hoạt động với số nguyên.

Ví dụ, hãy xem xét rằng bất kỳ hai số $a$ và $N$ nào cũng là **số nguyên tố cùng nhau** (hoặc **số nguyên tố tương đối**) nếu ước chung lớn nhất của chúng bằng 1. Giả sử bây giờ là một số nguyên $N$ cụ thể. Có bao nhiêu số nguyên nhỏ hơn $N$ là số nguyên tố cùng nhau với $N$? Chúng ta có thể đưa ra các tuyên bố chung về câu trả lời cho câu hỏi này không? Đây là những loại câu hỏi điển hình mà lý thuyết số tìm cách trả lời.

Lý thuyết số hiện đại dựa trên các công cụ của đại số trừu tượng. Lĩnh vực **đại số trừu tượng** là một phân ngành của toán học, trong đó các đối tượng phân tích chính là các đối tượng trừu tượng được gọi là các cấu trúc đại số. **Cấu trúc đại số** là một tập hợp các phần tử được kết hợp với một hoặc nhiều phép toán, đáp ứng các tiên đề nhất định. Thông qua các cấu trúc đại số, các nhà toán học có thể hiểu sâu hơn về các vấn đề toán học cụ thể, bằng cách trừu tượng hóa các chi tiết của chúng.

Lĩnh vực đại số trừu tượng đôi khi cũng được gọi là đại số hiện đại. Bạn cũng có thể bắt gặp khái niệm **toán học trừu tượng** (hoặc **toán học thuần túy**). Thuật ngữ sau này không phải là tham chiếu đến đại số trừu tượng, mà đúng hơn là có nghĩa là nghiên cứu toán học vì lợi ích của chính nó, chứ không chỉ để mắt đến các ứng dụng tiềm năng.

Các tập hợp từ đại số trừu tượng có thể xử lý nhiều loại đối tượng, từ các phép biến đổi giữ nguyên hình dạng trên một tam giác đều đến các mẫu hình nền. Đối với lý thuyết số, chúng ta chỉ xem xét các tập hợp các phần tử chứa các số nguyên hoặc các hàm hoạt động với các số nguyên.

## Nhóm

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Một khái niệm cơ bản trong toán học là về một tập hợp các phần tử. Một tập hợp thường được biểu thị bằng các dấu phẩy với các phần tử được phân tách bằng dấu phẩy.

Ví dụ, tập hợp tất cả các số nguyên là $\{…, -2, -1, 0, 1, 2, …\}$. Các dấu ba chấm ở đây có nghĩa là một mẫu nhất định tiếp tục theo một hướng cụ thể. Vì vậy, tập hợp tất cả các số nguyên cũng bao gồm $3, 4, 5, 6$, v.v., cũng như $-3, -4, -5, -6$, v.v. Tập hợp tất cả các số nguyên này thường được ký hiệu là $\mathbb{Z}$.

Một ví dụ khác về tập hợp là $\mathbb{Z} \mod 11$, hay tập hợp tất cả các số nguyên modulo 11. Ngược lại với toàn bộ tập hợp $\mathbb{Z}$, tập hợp này chỉ chứa một số lượng hữu hạn các phần tử, cụ thể là $\{0, 1, \ldots, 9, 10\}$.

Một lỗi thường gặp là nghĩ rằng tập $\mathbb{Z} \mod 11$ thực sự là $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Nhưng điều này không đúng, xét theo cách chúng ta định nghĩa phép toán modulo trước đó. Bất kỳ số nguyên âm nào được rút gọn theo modulo 11 đều được bao quanh thành $\{0, 1, \ldots, 9, 10\}$. Ví dụ, biểu thức $-2 \mod 11$ bao quanh thành $9$, trong khi biểu thức $-27 \mod 11$ bao quanh thành $5$.

Một khái niệm cơ bản khác trong toán học là phép toán nhị phân. Đây là bất kỳ phép toán nào lấy hai phần tử để tạo ra phần tử thứ ba. Ví dụ, từ số học và đại số cơ bản, bạn sẽ quen thuộc với bốn phép toán nhị phân cơ bản: cộng, trừ, nhân và chia.

Hai khái niệm toán học cơ bản này, tập hợp và phép toán nhị phân, được sử dụng để định nghĩa khái niệm nhóm, cấu trúc thiết yếu nhất trong đại số trừu tượng.

Cụ thể, giả sử một số phép toán nhị phân $\circ$. Ngoài ra, giả sử một số tập hợp các phần tử **S** được trang bị phép toán đó. Tất cả “được trang bị” có nghĩa là phép toán $\circ$ có thể được thực hiện giữa bất kỳ hai phần tử nào trong tập hợp **S**.

Tổ hợp $\langle \mathbf{S}, \circ \rangle$ là một **nhóm** nếu nó đáp ứng bốn điều kiện cụ thể, được gọi là tiên đề nhóm.

1. Đối với bất kỳ $a$ và $b$ nào là phần tử của $\mathbf{S}$, $a \circ b$ cũng là phần tử của $\mathbf{S}$. Điều này được gọi là **điều kiện đóng**.

2. Đối với bất kỳ $a$, $b$ và $c$ nào là các phần tử của $\mathbf{S}$, thì trường hợp $(a \circ b) \circ c = a \circ (b \circ c)$. Điều này được gọi là **điều kiện kết hợp**.

3. Có một phần tử duy nhất $e$ trong $\mathbf{S}$, sao cho với mọi phần tử $a$ trong $\mathbf{S}$, phương trình sau đây đúng: $e \circ a = a \circ e = a$. Vì chỉ có một phần tử như vậy $e$, nên nó được gọi là **phần tử đồng nhất**. Điều kiện này được gọi là **điều kiện đồng nhất**.

4. Đối với mỗi phần tử $a$ trong $\mathbf{S}$, tồn tại một phần tử $b$ trong $\mathbf{S}$ sao cho phương trình sau đây đúng: $a \circ b = b \circ a = e$, trong đó $e$ là phần tử đồng nhất. Phần tử $b$ ở đây được gọi là **phần tử nghịch đảo**, và thường được ký hiệu là $a^{-1}$. Điều kiện này được gọi là **điều kiện nghịch đảo** hoặc **điều kiện khả nghịch**.

Hãy cùng khám phá nhóm xa hơn một chút. Ký hiệu tập hợp tất cả các số nguyên là $\mathbb{Z}$. Tập hợp này kết hợp với phép cộng chuẩn, hoặc $\langle \mathbb{Z}, + \rangle$, rõ ràng phù hợp với định nghĩa của một nhóm, vì nó đáp ứng bốn tiên đề trên.

1. Với mọi $x$ và $y$ là phần tử của $\mathbb{Z}$, $x + y$ cũng là phần tử của $\mathbb{Z}$. Do đó $\langle \mathbb{Z}, + \rangle$ thỏa mãn điều kiện đóng.

2. Với mọi $x$, $y$ và $z$ là các phần tử của $\mathbb{Z}$, $(x + y) + z = x + (y + z)$. Vậy $\langle \mathbb{Z}, + \rangle$ thỏa mãn điều kiện kết hợp.

3. Có một phần tử đồng nhất trong $\langle \mathbb{Z}, + \rangle$, cụ thể là 0. Với mọi $x$ trong $\mathbb{Z}$, cụ thể là: $0 + x = x + 0 = x$. Vậy $\langle \mathbb{Z}, + \rangle$ thỏa mãn điều kiện đồng nhất.

4. Cuối cùng, đối với mỗi phần tử $x$ trong $\mathbb{Z}$, tồn tại một $y$ sao cho $x + y = y + x = 0$. Ví dụ, nếu $x$ bằng 10, thì $y$ sẽ bằng $-10$ (trong trường hợp $x$ bằng 0, thì $y$ cũng bằng 0). Vì vậy, $\langle \mathbb{Z}, + \rangle$ thỏa mãn điều kiện nghịch đảo.

Điều quan trọng là tập hợp các số nguyên có phép cộng tạo thành một nhóm không có nghĩa là nó tạo thành một nhóm có phép nhân. Bạn có thể xác minh điều này bằng cách kiểm tra $\langle \mathbb{Z}, \cdot \rangle$ so với bốn tiên đề nhóm (trong đó $\cdot$ có nghĩa là phép nhân chuẩn).

Hai tiên đề đầu tiên rõ ràng là đúng. Ngoài ra, theo phép nhân, phần tử 1 có thể đóng vai trò là phần tử đồng nhất. Bất kỳ số nguyên $x$ nào nhân với 1, tức là tạo ra $x$. Tuy nhiên, $\langle \mathbb{Z}, \cdot \rangle$ không đáp ứng điều kiện nghịch đảo. Nghĩa là, không có phần tử duy nhất $y$ trong $\mathbb{Z}$ cho mọi $x$ trong $\mathbb{Z}$, do đó $x \cdot y = 1$.

Ví dụ, giả sử $x = 22$. Giá trị $y$ nào từ tập $\mathbb{Z}$ nhân với $x$ sẽ tạo ra phần tử đồng nhất 1? Giá trị $1/22$ sẽ hoạt động, nhưng giá trị này không nằm trong tập $\mathbb{Z}$. Trên thực tế, bạn gặp phải vấn đề này đối với bất kỳ số nguyên $x$ nào, ngoại trừ các giá trị 1 và -1 (trong đó $y$ phải lần lượt là 1 và -1).

Nếu chúng ta cho phép các số thực cho tập hợp của mình, thì các vấn đề của chúng ta phần lớn sẽ biến mất. Đối với bất kỳ phần tử $x$ nào trong tập hợp, phép nhân với $1/x$ sẽ cho kết quả là 1. Vì các phân số được bao gồm trong tập hợp các số thực, nên có thể tìm thấy một nghịch đảo cho mọi số thực. Ngoại lệ là số không, vì bất kỳ phép nhân nào với số không sẽ không bao giờ cho kết quả là phần tử đồng nhất 1. Do đó, tập hợp các số thực khác không được trang bị phép nhân thực sự là một nhóm.

Một số nhóm đáp ứng điều kiện chung thứ năm, được gọi là **điều kiện giao hoán**. Điều kiện này như sau:


- Giả sử một nhóm $G$ với một tập hợp **S** và một toán tử nhị phân $\circ$. Giả sử $a$ và $b$ là các phần tử của **S**. Nếu trường hợp $a \circ b = b \circ a$ đối với bất kỳ hai phần tử $a$ và $b$ nào trong **S**, thì $G$ thỏa mãn điều kiện giao hoán.

Bất kỳ nhóm nào đáp ứng điều kiện giao hoán được gọi là **nhóm giao hoán**, hoặc **nhóm Abelian** (theo tên Niels Henrik Abel). Có thể dễ dàng xác minh rằng cả tập hợp các số thực trên phép cộng và tập hợp các số nguyên trên phép cộng đều là nhóm Abelian. Tập hợp các số nguyên trên phép nhân không phải là một nhóm, do đó ipso facto không thể là một nhóm Abelian. Ngược lại, tập hợp các số thực khác không trên phép nhân cũng là một nhóm Abelian.

Bạn nên lưu ý hai quy ước quan trọng về ký hiệu. Đầu tiên, các dấu “+” hoặc “×” thường được sử dụng để biểu tượng hóa các phép toán nhóm, ngay cả khi các phần tử thực tế không phải là số. Trong những trường hợp này, bạn không nên hiểu các dấu này là phép cộng hoặc phép nhân số học chuẩn. Thay vào đó, chúng là các phép toán chỉ có sự tương đồng trừu tượng với các phép toán số học này.

Trừ khi bạn đang đề cập cụ thể đến phép cộng hoặc phép nhân số học, thì việc sử dụng các ký hiệu như $\circ$ và $\diamond$ cho các phép toán nhóm sẽ dễ dàng hơn vì chúng không có hàm ý ăn sâu vào văn hóa.

Thứ hai, vì lý do tương tự mà “+” và “×” thường được sử dụng để chỉ các phép toán không phải số học, các phần tử đồng nhất của nhóm thường được ký hiệu bằng “0” và “1”, ngay cả khi các phần tử trong các nhóm này không phải là số. Trừ khi bạn đang đề cập đến phần tử đồng nhất của một nhóm bằng số, thì sẽ dễ dàng hơn khi sử dụng một ký hiệu trung tính hơn như “$e$” để chỉ phần tử đồng nhất.

Nhiều tập hợp giá trị khác nhau và rất quan trọng trong toán học được trang bị một số phép toán nhị phân là nhóm. Tuy nhiên, các ứng dụng mật mã chỉ hoạt động với các tập hợp số nguyên hoặc ít nhất là các phần tử được mô tả bằng số nguyên, tức là trong phạm vi của lý thuyết số. Do đó, các tập hợp có số thực khác với số nguyên không được sử dụng trong các ứng dụng mật mã.

Chúng ta hãy kết thúc bằng cách cung cấp một ví dụ về các phần tử có thể được "mô tả bằng số nguyên", mặc dù chúng không phải là số nguyên. Một ví dụ hay là các điểm của đường cong elliptic. Mặc dù bất kỳ điểm nào trên đường cong elliptic rõ ràng không phải là số nguyên, nhưng một điểm như vậy thực sự được mô tả bằng hai số nguyên.

Ví dụ, đường cong elliptic rất quan trọng đối với Bitcoin. Bất kỳ cặp khóa công khai và riêng tư Bitcoin chuẩn nào cũng được chọn từ tập hợp các điểm được xác định bởi đường cong elliptic sau:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(số nguyên tố lớn nhất nhỏ hơn $2^{256}$). Tọa độ $x$ là khóa riêng tư và tọa độ $y$ là khóa công khai của bạn.

Giao dịch trong Bitcoin thường liên quan đến việc khóa đầu ra vào một hoặc nhiều khóa công khai theo một cách nào đó. Giá trị từ các giao dịch này sau đó có thể được mở khóa bằng cách tạo chữ ký số với các khóa riêng tương ứng.

## Nhóm tuần hoàn

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Một sự phân biệt chính mà chúng ta có thể rút ra là giữa **nhóm hữu hạn** và **nhóm vô hạn**. Nhóm trước có số lượng phần tử hữu hạn, trong khi nhóm sau có số lượng phần tử vô hạn. Số lượng phần tử trong bất kỳ nhóm hữu hạn nào được gọi là **cấp của nhóm**. Tất cả các mật mã thực tế liên quan đến việc sử dụng các nhóm đều dựa trên các nhóm hữu hạn (lý thuyết số).

Trong mật mã khóa công khai, một lớp nhất định của các nhóm Abel hữu hạn được gọi là nhóm tuần hoàn đặc biệt quan trọng. Để hiểu các nhóm tuần hoàn, trước tiên chúng ta cần hiểu khái niệm về lũy thừa phần tử nhóm.

Giả sử một nhóm $G$ với phép toán nhóm $\circ$, và $a$ là một phần tử của $G$. Khi đó, biểu thức $a^n$ sẽ được hiểu là phần tử $a$ kết hợp với chính nó tổng cộng $n – 1$ lần. Ví dụ, $a^2$ nghĩa là $a \circ a$, $a^3$ nghĩa là $a \circ a \circ a$, v.v. (Lưu ý rằng lũy thừa ở đây không nhất thiết là lũy thừa theo nghĩa số học chuẩn.)

Hãy chuyển sang một ví dụ. Giả sử $G = \langle \mathbb{Z} \mod 7, + \rangle$, và giá trị của chúng ta đối với $a$ bằng 4. Trong trường hợp này, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Hoặc, $a^4$ sẽ biểu diễn $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Một số nhóm Abelian có một hoặc nhiều phần tử, có thể tạo ra tất cả các phần tử nhóm khác thông qua phép lũy thừa liên tục. Các phần tử này được gọi là **phần tử sinh** hoặc **phần tử nguyên thủy**.

Một lớp quan trọng của các nhóm như vậy là $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, trong đó $N$ là một số nguyên tố. Ký hiệu $\mathbb{Z}^*$ ở đây có nghĩa là nhóm chứa tất cả các số nguyên dương khác không, nhỏ hơn $N$. Do đó, một nhóm như vậy luôn có $N – 1$ phần tử.

Ví dụ, hãy xem xét $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Nhóm này có các phần tử sau: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Cấp của nhóm này là 10 (thực tế bằng $11 – 1$).

Hãy cùng khám phá phép lũy thừa phần tử 2 từ nhóm này. Các phép tính cho đến $2^{12}$ được hiển thị bên dưới. Lưu ý rằng ở vế trái của phương trình, số mũ đề cập đến phép lũy thừa phần tử nhóm. Trong ví dụ cụ thể của chúng ta, điều này thực sự liên quan đến phép lũy thừa số học ở vế phải của phương trình (nhưng nó cũng có thể liên quan đến phép cộng chẳng hạn). Để làm rõ, tôi đã viết ra phép toán lặp lại, thay vì dạng số mũ ở vế phải.


- $2^1 = 2 \mod 11$
- $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
- $2^3 = 2 \cdot2 \cdot2 \mod 11 = 8 \mod 11$
- $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
- $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
- $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
- $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
- $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
- $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
- $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
- $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Nếu bạn nhìn kỹ, bạn có thể thấy rằng việc thực hiện phép lũy thừa trên phần tử 2 sẽ tuần hoàn qua tất cả các phần tử của $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ theo thứ tự sau: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Sau $2^{10}$, phép lũy thừa tiếp theo của phần tử 2 sẽ tuần hoàn qua tất cả các phần tử một lần nữa và theo cùng thứ tự. Do đó, phần tử 2 là một phần tử tạo trong $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Mặc dù $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ có nhiều máy phát điện, nhưng không phải tất cả các phần tử của nhóm này đều là máy phát điện. Ví dụ, hãy xem xét phần tử 3. Chạy qua 10 phép mũ đầu tiên, mà không hiển thị các phép tính cồng kềnh, sẽ cho kết quả sau:


- $3^1 = 3 \mod 11$
- $3^2 = 9 \mod 11$
- $3^3 = 5 \mod 11$
- $3^4 = 4 \mod 11$
- $3^5 = 1 \mod 11$
- $3^6 = 3 \mod 11$
- $3^7 = 9 \mod 11$
- $3^8 = 5 \mod 11$
- $3^9 = 4 \mod 11$
- $3^{10} = 1 \mod 11$

Thay vì tuần hoàn qua tất cả các giá trị trong $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, phép lũy thừa của phần tử 3 chỉ dẫn đến một tập hợp con của các giá trị đó: 3, 9, 5, 4 và 1. Sau phép lũy thừa thứ năm, các giá trị này bắt đầu lặp lại.

Bây giờ chúng ta có thể định nghĩa một **nhóm tuần hoàn** là bất kỳ nhóm nào có ít nhất một phần tử sinh. Nghĩa là, có ít nhất một phần tử nhóm mà từ đó bạn có thể tạo ra tất cả các phần tử nhóm khác thông qua phép mũ.

Bạn có thể đã nhận thấy trong ví dụ trên của chúng tôi rằng cả $2^{10}$ và $3^{10}$ đều bằng $1 \mod 11$. Trên thực tế, mặc dù chúng ta sẽ không thực hiện các phép tính, nhưng phép lũy thừa 10 của bất kỳ phần tử nào trong nhóm $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ sẽ cho kết quả là $1 \mod 11$. Tại sao lại như vậy?

Đây là một câu hỏi quan trọng nhưng cần phải bỏ nhiều công sức để trả lời.

Để bắt đầu, giả sử hai số nguyên dương $a$ và $N$. Một định lý quan trọng trong lý thuyết số phát biểu rằng $a$ có nghịch đảo phép nhân modulo $N$ (tức là, một số nguyên $b$ sao cho $a \cdot b = 1 \mod N$) nếu và chỉ nếu ước chung lớn nhất giữa $a$ và $N$ bằng 1. Nghĩa là, nếu $a$ và $N$ là các số nguyên tố cùng nhau.

Vì vậy, đối với bất kỳ nhóm số nguyên nào được trang bị phép nhân modulo $N$, chỉ các số nguyên tố cùng nhau nhỏ hơn với $N$ mới được bao gồm trong tập hợp. Chúng ta có thể biểu thị tập hợp này bằng $\mathbb{Z}^c \mod N$.

Ví dụ, giả sử $N$ là 10. Chỉ có các số nguyên 1, 3, 7 và 9 là nguyên tố cùng nhau với 10. Vì vậy, tập hợp $\mathbb{Z}^c \mod 10$ chỉ bao gồm $\{1, 3, 7, 9\}$. Bạn không thể tạo một nhóm với phép nhân số nguyên modulo 10 bằng bất kỳ số nguyên nào khác giữa 1 và 10. Đối với nhóm cụ thể này, các nghịch đảo là cặp 1 và 9, và 3 và 7.

Trong trường hợp $N$ tự nó là số nguyên tố, tất cả các số nguyên từ 1 đến $N – 1$ đều là số nguyên tố cùng nhau với $N$. Do đó, một nhóm như vậy có cấp là $N – 1$. Sử dụng ký hiệu trước đó của chúng tôi, $\mathbb{Z}^c \mod N$ bằng $\mathbb{Z}^* \mod N$ khi $N$ là số nguyên tố. Nhóm mà chúng tôi đã chọn cho ví dụ trước đó của mình, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, là một trường hợp cụ thể của lớp nhóm này.

Tiếp theo, hàm $\phi(N)$ tính toán số các số nguyên tố cùng nhau cho đến số $N$ và được gọi là **hàm Euler’s Phi**. [1] Theo **Định lý Euler**, bất cứ khi nào hai số nguyên $a$ và $N$ là các số nguyên tố cùng nhau, thì điều sau đây đúng:


- $a^{\phi(N)} \mod N = 1 \mod N$

Điều này có một hàm ý quan trọng đối với lớp nhóm $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ trong đó $N$ là số nguyên tố. Đối với các nhóm này, phép lũy thừa phần tử của nhóm biểu diễn phép lũy thừa số học. Nghĩa là, $a^{\phi(N)} \mod N$ biểu diễn phép toán số học $a^{\phi(N)} \mod N$. Vì bất kỳ phần tử $a$ nào trong các nhóm nhân này đều nguyên tố cùng nhau với $N$, điều đó có nghĩa là $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.

Định lý Euler là một kết quả thực sự quan trọng. Để bắt đầu, nó ngụ ý rằng tất cả các phần tử trong $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ chỉ có thể tuần hoàn qua một số giá trị theo phép lũy thừa chia hết cho $N – 1$. Trong trường hợp của $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, điều này có nghĩa là mỗi phần tử chỉ có thể tuần hoàn qua 2, 5 hoặc 10 phần tử. Các giá trị nhóm mà bất kỳ phần tử nào tuần hoàn qua khi lũy thừa được gọi là **cấp của phần tử**. Một phần tử có cấp tương đương với cấp của một nhóm là một phần tử tạo.

Hơn nữa, định lý Euler ngụ ý rằng chúng ta luôn có thể biết kết quả của $a^{N – 1} \mod N$ cho bất kỳ nhóm $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ trong đó $N$ là số nguyên tố. Điều này đúng bất kể các phép tính thực tế có phức tạp đến mức nào.

Ví dụ, giả sử nhóm của chúng ta là $\mathbb{Z}^* \mod 160,481,182$ (trong đó 160,481,182 thực sự là một số nguyên tố). Chúng ta biết rằng tất cả các số nguyên từ 1 đến 160,481,181 phải là các phần tử của nhóm này và $\phi(n) = 160,481,181$. Mặc dù chúng ta không thể thực hiện tất cả các bước trong phép tính, nhưng chúng ta biết rằng các biểu thức như $514^{160,481,181}$, $2,005^{160,481,181}$ và $256,212^{160,481,181}$ đều phải đánh giá là $1 \mod 160,481,182$.

**Lưu ý:**

[1] Hàm hoạt động như sau. Bất kỳ số nguyên $N$ nào cũng có thể được phân tích thành tích các số nguyên tố. Giả sử rằng một $N$ cụ thể được phân tích như sau: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ trong đó tất cả các $p$ là các số nguyên tố và tất cả các $e$ là các số nguyên lớn hơn hoặc bằng 1. Khi đó:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Công thức hàm Euler Phi để phân tích thừa số nguyên tố của $N$.

## Các cánh đồng

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Nhóm là cấu trúc đại số cơ bản trong đại số trừu tượng, nhưng còn nhiều cấu trúc khác nữa. Cấu trúc đại số duy nhất khác mà bạn cần phải quen thuộc là cấu trúc của **trường**, cụ thể là cấu trúc của **trường hữu hạn**. Kiểu cấu trúc đại số này thường được sử dụng trong mật mã học, chẳng hạn như trong Tiêu chuẩn mã hóa nâng cao. Sau này là lược đồ mã hóa đối xứng chính mà bạn sẽ gặp trong thực tế.

Một trường bắt nguồn từ khái niệm nhóm. Cụ thể, **trường** là một tập hợp các phần tử **S** được trang bị hai toán tử nhị phân $\circ$ và $\diamond$, đáp ứng các điều kiện sau:

1. Tập hợp **S** được trang bị $\circ$ là một nhóm Abel.

2. Tập hợp **S** được trang bị $\diamond$ là một nhóm Abel cho các phần tử “khác không”.

3. Tập hợp **S** được trang bị hai toán tử thỏa mãn điều kiện được gọi là điều kiện phân phối: Giả sử $a$, $b$ và $c$ là các phần tử của **S**. Khi đó **S** được trang bị hai toán tử thỏa mãn tính chất phân phối khi $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Lưu ý rằng, giống như với nhóm, định nghĩa về trường rất trừu tượng. Nó không đưa ra tuyên bố nào về các loại phần tử trong **S**, hoặc về các phép toán $\circ$ và $\diamond$. Nó chỉ nêu rằng trường là bất kỳ tập hợp phần tử nào có hai phép toán mà ba điều kiện trên được giữ nguyên. (Phần tử “không” trong nhóm Abelian thứ hai có thể được diễn giải trừu tượng.)

Vậy thì ví dụ về trường có thể là gì? Một ví dụ hay là tập hợp $\mathbb{Z} \mod 7$, hoặc $\{0, 1, \ldots, 7\}$ được xác định theo phép cộng chuẩn (thay cho $\circ$ ở trên) và phép nhân chuẩn (thay cho $\diamond$ ở trên).

Đầu tiên, $\mathbb{Z} \mod 7$ đáp ứng điều kiện để là nhóm Abel trên phép cộng, và nó đáp ứng điều kiện để là nhóm Abel trên phép nhân nếu bạn chỉ xét các phần tử khác không. Thứ hai, tổ hợp của tập hợp với hai toán tử đáp ứng điều kiện phân phối.

Về mặt giáo dục, việc khám phá những tuyên bố này bằng cách sử dụng một số giá trị cụ thể là rất đáng giá. Chúng ta hãy lấy các giá trị thử nghiệm 5, 2 và 3, một số phần tử được chọn ngẫu nhiên từ tập $\mathbb{Z} \mod 7$, để kiểm tra trường $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Chúng ta sẽ sử dụng ba giá trị này theo thứ tự, khi cần để khám phá các điều kiện cụ thể.

Trước tiên chúng ta hãy khám phá xem $\mathbb{Z} \mod 7$ được trang bị phép cộng có phải là một nhóm Abelian hay không.

1. **Điều kiện đóng**: Chúng ta lấy 5 và 2 làm giá trị của chúng ta. Trong trường hợp đó, $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Đây thực sự là một phần tử của $\mathbb{Z} \mod 7$, do đó kết quả phù hợp với điều kiện đóng.

2. **Điều kiện kết hợp**: Hãy lấy 5, 2 và 3 làm giá trị của chúng ta. Trong trường hợp đó, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Điều này phù hợp với điều kiện kết hợp.

3. **Điều kiện đồng nhất**: Lấy 5 làm giá trị của chúng ta. Trong trường hợp đó, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Vì vậy, 0 có vẻ là phần tử đồng nhất cho phép cộng.

4. **Điều kiện nghịch đảo**: Xét nghịch đảo của 5. Trường hợp cần phải là $[5 + d] \mod 7 = 0$, đối với một giá trị nào đó của $d$. Trong trường hợp này, giá trị duy nhất từ $\mathbb{Z} \mod 7$ đáp ứng điều kiện này là 2.

5. **Điều kiện giao hoán**: Hãy lấy 5 và 3 làm giá trị của chúng ta. Trong trường hợp đó, $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Điều này phù hợp với điều kiện giao hoán.

Tập $\mathbb{Z} \mod 7$ được trang bị phép cộng rõ ràng có vẻ là một nhóm Abelian. Bây giờ chúng ta hãy khám phá xem $\mathbb{Z} \mod 7$ được trang bị phép nhân có phải là một nhóm Abelian cho tất cả các phần tử khác không.

1. **Điều kiện đóng**: Lấy 5 và 2 làm giá trị của chúng ta. Trong trường hợp đó, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Đây cũng là một phần tử của $\mathbb{Z} \mod 7$, do đó kết quả phù hợp với điều kiện đóng.

2. **Điều kiện kết hợp**: Hãy lấy 5, 2 và 3 làm giá trị của chúng ta. Trong trường hợp đó, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Điều này phù hợp với điều kiện kết hợp.

3. **Điều kiện đồng nhất**: Lấy 5 làm giá trị của chúng ta. Trong trường hợp đó, $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Vì vậy, 1 có vẻ là phần tử đồng nhất cho phép nhân.

4. **Điều kiện nghịch đảo**: Xét nghịch đảo của 5. Trường hợp cần phải là $[5 \cdot d] \mod 7 = 1$, với một giá trị nào đó của $d$. Giá trị duy nhất từ $\mathbb{Z} \mod 7$ đáp ứng điều kiện này là 3. Điều này phù hợp với điều kiện nghịch đảo.

5. **Điều kiện giao hoán**: Lấy 5 và 3 làm giá trị của chúng ta. Trong trường hợp đó, $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Điều này phù hợp với điều kiện giao hoán.

Tập hợp $\mathbb{Z} \mod 7$ rõ ràng có vẻ đáp ứng các quy tắc để trở thành một nhóm Abel khi kết hợp với phép cộng hoặc phép nhân trên các phần tử khác không.

Cuối cùng, tập hợp này kết hợp với cả hai toán tử dường như đáp ứng điều kiện phân phối. Hãy lấy 5, 2 và 3 làm giá trị của chúng ta. Chúng ta có thể thấy rằng $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Bây giờ chúng ta đã thấy rằng $\mathbb{Z} \mod 7$ được trang bị phép cộng và phép nhân đáp ứng các tiên đề cho một trường hữu hạn khi thử nghiệm với các giá trị cụ thể. Tất nhiên, chúng ta cũng có thể chứng minh điều đó một cách tổng quát, nhưng sẽ không làm như vậy ở đây.

Một sự phân biệt quan trọng là giữa hai loại trường: trường hữu hạn và trường vô hạn.

**Trường vô hạn** bao gồm một trường trong đó tập hợp **S** là vô hạn lớn. Tập hợp các số thực $\mathbb{R}$ được trang bị phép cộng và phép nhân là một ví dụ về trường vô hạn. **Trường hữu hạn**, còn được gọi là **trường Galois**, là một trường trong đó tập hợp **S** là hữu hạn. Ví dụ trên của chúng ta về $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ là một trường hữu hạn.

Trong mật mã học, chúng ta chủ yếu quan tâm đến các trường hữu hạn. Nhìn chung, có thể chứng minh rằng một trường hữu hạn tồn tại đối với một tập hợp các phần tử **S** nếu và chỉ nếu nó có $p^m$ phần tử, trong đó $p$ là số nguyên tố và $m$ là số nguyên dương lớn hơn hoặc bằng một. Nói cách khác, nếu thứ tự của một tập hợp **S** là một số nguyên tố ($p^m$ trong đó $m = 1$) hoặc một số lũy thừa nguyên tố ($p^m$ trong đó $m > 1$), thì bạn có thể tìm thấy hai toán tử $\circ$ và $\diamond$ sao cho các điều kiện cho một trường được thỏa mãn.

Nếu một số trường hữu hạn có số phần tử là nguyên tố, thì nó được gọi là **trường nguyên tố**. Nếu số phần tử trong trường hữu hạn là lũy thừa nguyên tố, thì trường này được gọi là **trường mở rộng**. Trong mật mã học, chúng ta quan tâm đến cả trường nguyên tố và trường mở rộng. [2]

Các trường nguyên tố chính được quan tâm trong mật mã học là những trường mà tập hợp tất cả các số nguyên được điều chế bởi một số nguyên tố nào đó và các toán tử là phép cộng và phép nhân tiêu chuẩn. Lớp các trường hữu hạn này sẽ bao gồm $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, v.v. Đối với bất kỳ trường nguyên tố $\mathbb{Z} \mod p$ nào, tập hợp các số nguyên của trường đó như sau: $\{0, 1, \ldots, p – 2, p – 1\}$.

Trong mật mã học, chúng tôi cũng quan tâm đến các trường mở rộng, đặc biệt là bất kỳ trường nào có $2^m$ phần tử trong đó $m > 1$. Ví dụ, các trường hữu hạn như vậy được sử dụng trong Rijndael Cipher, tạo thành cơ sở của Advanced Encryption Standard. Trong khi các trường nguyên tố tương đối trực quan, các trường mở rộng cơ số 2 này có lẽ không dành cho bất kỳ ai không quen với đại số trừu tượng.

Để bắt đầu, thực sự đúng là bất kỳ tập hợp số nguyên nào có $2^m$ phần tử đều có thể được gán hai toán tử để biến tổ hợp của chúng thành một trường (miễn là $m$ là một số nguyên dương). Tuy nhiên, chỉ vì một trường tồn tại không nhất thiết có nghĩa là nó dễ khám phá hoặc đặc biệt thiết thực đối với một số ứng dụng nhất định.

Thực tế, các trường mở rộng đặc biệt có thể áp dụng của $2^m$ trong mật mã là những trường được xác định trên các tập hợp biểu thức đa thức cụ thể, chứ không phải một số tập hợp số nguyên.

Ví dụ, giả sử chúng ta muốn một trường mở rộng với $2^3$ (tức là 8) phần tử trong tập hợp. Mặc dù có thể có nhiều tập hợp khác nhau có thể được sử dụng cho các trường có kích thước đó, nhưng một tập hợp như vậy bao gồm tất cả các đa thức duy nhất có dạng $a_2x^2 + a_1x + a_0$, trong đó mỗi hệ số $a_i$ là 0 hoặc 1. Do đó, tập hợp **S** này bao gồm các phần tử sau:

1. $0$: Trường hợp $a_2 = 0$, $a_1 = 0$ và $a_0 = 0$.

2. $1$: Trường hợp $a_2 = 0$, $a_1 = 0$ và $a_0 = 1$.

3. $x$: Trường hợp $a_2 = 0$, $a_1 = 1$ và $a_0 = 0$.

4. $x + 1$: Trường hợp $a_2 = 0$, $a_1 = 1$ và $a_0 = 1$.

5. $x^2$: Trường hợp $a_2 = 1$, $a_1 = 0$ và $a_0 = 0$.

6. $x^2 + 1$: Trường hợp $a_2 = 1$, $a_1 = 0$ và $a_0 = 1$.

7. $x^2 + x$: Trường hợp $a_2 = 1$, $a_1 = 1$ và $a_0 = 0$.

8. $x^2 + x + 1$: Trường hợp $a_2 = 1$, $a_1 = 1$ và $a_0 = 1$.

Vì vậy, **S** sẽ là tập hợp $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Có thể định nghĩa hai phép toán nào trên tập hợp các phần tử này để đảm bảo tổ hợp của chúng là một trường?

Phép toán đầu tiên trên tập hợp **S** ($\circ$) có thể được định nghĩa là phép cộng đa thức chuẩn modulo 2. Tất cả những gì bạn phải làm là cộng các đa thức như bình thường, sau đó áp dụng modulo 2 cho mỗi hệ số của đa thức kết quả. Sau đây là một số ví dụ:


- $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
- $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
- $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

Phép toán thứ hai trên tập hợp **S** ($\diamond$) cần thiết để tạo trường phức tạp hơn. Đây là một dạng phép nhân, nhưng không phải là phép nhân chuẩn từ số học. Thay vào đó, bạn phải xem mỗi phần tử như một vectơ và hiểu phép toán như phép nhân hai vectơ đó theo modulo một đa thức bất khả quy.

Trước tiên, chúng ta hãy chuyển sang ý tưởng về đa thức bất khả quy. Một **đa thức bất khả quy** là đa thức không thể phân tích thành thừa số (giống như một số nguyên tố không thể phân tích thành các thành phần khác ngoài 1 và chính số nguyên tố đó). Đối với mục đích của chúng ta, chúng ta quan tâm đến các đa thức bất khả quy đối với tập hợp tất cả các số nguyên. (Lưu ý rằng bạn có thể phân tích thành thừa số một số đa thức nhất định theo, ví dụ, các số thực hoặc số phức, ngay cả khi bạn không thể phân tích chúng bằng số nguyên.)

Ví dụ, hãy xét đa thức $x^2 - 3x + 2$. Ta có thể viết lại thành $(x – 1)(x – 2)$. Do đó, đây không phải là đa thức bất khả quy. Bây giờ hãy xét đa thức $x^2 + 1$. Chỉ sử dụng số nguyên, không có cách nào để phân tích thêm biểu thức này. Do đó, đây là đa thức bất khả quy đối với số nguyên.

Tiếp theo, chúng ta hãy chuyển sang khái niệm phép nhân vectơ. Chúng ta sẽ không đi sâu vào chủ đề này, nhưng bạn chỉ cần hiểu một quy tắc cơ bản: Bất kỳ phép chia vectơ nào cũng có thể diễn ra miễn là số bị chia có bậc cao hơn hoặc bằng bậc của số chia. Nếu số bị chia có bậc thấp hơn số chia, thì số bị chia không còn có thể chia cho số chia nữa.

Ví dụ, hãy xem xét biểu thức $x^6 + x + 1 \mod x^5 + x^2$. Rõ ràng biểu thức này còn giảm nữa vì bậc của số bị chia, 6, cao hơn bậc của số chia, 5. Bây giờ hãy xem xét biểu thức $x^5 + x + 1 \mod x^5 + x^2$. Biểu thức này cũng giảm nữa vì bậc của số bị chia, 5, và số chia, 5, bằng nhau.

Tuy nhiên, bây giờ hãy xem xét biểu thức $x^4 + x + 1 \mod x^5 + x^2$. Biểu thức này không giảm thêm nữa, vì bậc của số bị chia, 4, thấp hơn bậc của số chia, 5.

Dựa trên thông tin này, bây giờ chúng ta đã sẵn sàng tìm phép toán thứ hai cho tập hợp $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Tôi đã nói rằng phép toán thứ hai nên được hiểu là phép nhân vectơ modulo một số đa thức bất khả quy. Đa thức bất khả quy này phải đảm bảo rằng phép toán thứ hai xác định một nhóm Abel trên **S** và phù hợp với điều kiện phân phối. Vậy thì đa thức bất khả quy đó phải là gì?

Vì tất cả các vectơ trong tập hợp đều có bậc 2 hoặc thấp hơn, nên đa thức bất khả quy phải có bậc 3. Nếu bất kỳ phép nhân nào của hai vectơ trong tập hợp tạo ra một đa thức bậc 3 hoặc cao hơn, chúng ta biết rằng modulo a đa thức bậc 3 luôn tạo ra một đa thức bậc 2 hoặc thấp hơn. Trường hợp này xảy ra vì bất kỳ đa thức bậc 3 hoặc cao hơn nào cũng luôn chia hết cho một đa thức bậc 3. Ngoài ra, đa thức đóng vai trò là ước số phải là bất khả quy.

Hóa ra có một số đa thức bất khả quy bậc 3 mà chúng ta có thể sử dụng làm ước số. Mỗi đa thức này định nghĩa một trường khác nhau kết hợp với tập hợp **S** và phép cộng modulo 2 của chúng ta. Điều này có nghĩa là bạn có nhiều tùy chọn khi sử dụng trường mở rộng $2^m$ trong mật mã.

Đối với ví dụ của chúng ta, giả sử chúng ta chọn đa thức $x^3 + x + 1$. Điều này thực sự không thể rút gọn được, vì bạn không thể phân tích nó bằng cách sử dụng các số nguyên. Ngoài ra, nó sẽ đảm bảo rằng bất kỳ phép nhân nào của hai phần tử sẽ tạo ra một đa thức bậc 2 hoặc nhỏ hơn.

Chúng ta hãy cùng xem xét ví dụ về phép toán thứ hai sử dụng đa thức $x^3 + x + 1$ làm ước số để minh họa cách thức hoạt động của phép toán. Giả sử bạn nhân các phần tử $x^2 + 1$ với $x^2 + x$ trong tập hợp **S** của chúng ta. Sau đó, chúng ta cần tính biểu thức $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Có thể đơn giản hóa như sau:


- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Ta biết rằng $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ có thể rút gọn vì số bị chia có bậc (4) cao hơn số chia (3).

Để bắt đầu, bạn có thể thấy rằng biểu thức $x^3 + x + 1$ chia thành $x^4 + x^3 + x^2 + x$ tổng cộng là $x$ lần. Bạn có thể xác minh điều này bằng cách nhân $x^3 + x + 1$ với $x$, tức là $x^4 + x^2 + x$. Vì số hạng sau có cùng bậc với số bị chia, tức là 4, nên chúng ta biết điều này đúng. Bạn có thể tính phần dư của phép chia này cho $x$ như sau:


- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
- $[x^3] \mod x^3 + x + 1 =$
- $x^3$

Vì vậy, sau khi chia $x^4 + x^3 + x^2 + x$ cho $x^3 + x + 1$ tổng cộng $x$ lần, chúng ta có phần dư là $x^3$. Có thể chia tiếp cho $x^3 + x + 1$ không?

Theo trực giác, có thể sẽ hấp dẫn khi nói rằng $x^3$ không còn có thể chia cho $x^3 + x + 1$ nữa, vì số hạng sau có vẻ lớn hơn. Tuy nhiên, hãy nhớ lại cuộc thảo luận của chúng ta về phép chia vectơ trước đó. Miễn là số bị chia có bậc lớn hơn hoặc bằng số chia, thì biểu thức có thể được rút gọn hơn nữa. Cụ thể, biểu thức $x^3 + x + 1$ có thể chia thành $x^3$ đúng 1 lần. Phần còn lại được tính như sau:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Bạn có thể thắc mắc tại sao $(x^3) - (x^3 + x + 1)$ lại được đánh giá là $x + 1$ chứ không phải $-x - 1$. Hãy nhớ rằng phép toán đầu tiên của trường của chúng ta được định nghĩa theo modulo 2. Do đó, phép trừ hai vectơ cho kết quả chính xác giống như phép cộng hai vectơ.

Tóm lại phép nhân $x^2 + 1$ và $x^2 + x$: Khi bạn nhân hai số hạng đó, bạn sẽ có được đa thức bậc 4, $x^4 + x^3 + x^2 + x$, cần phải rút gọn theo modulo $x^3 + x + 1$. Đa thức bậc 4 chia hết cho $x^3 + x + 1$ đúng $x + 1$ lần. Phần dư sau khi chia $x^4 + x^3 + x^2 + x$ cho $x^3 + x + 1$ đúng $x + 1$ lần là $x + 1$. Đây thực sự là một phần tử trong tập hợp $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$ của chúng ta.

Tại sao các trường mở rộng với cơ số 2 trên các tập hợp đa thức, như trong ví dụ trên, lại hữu ích cho mật mã học? Lý do là bạn có thể xem các hệ số trong các đa thức của các tập hợp như vậy, là 0 hoặc 1, như các phần tử của chuỗi nhị phân có độ dài cụ thể. Ví dụ, tập hợp **S** trong ví dụ trên của chúng tôi có thể được xem thay vào đó là một tập hợp **S** bao gồm tất cả các chuỗi nhị phân có độ dài 3 (từ 000 đến 111). Do đó, các phép toán trên **S** cũng có thể được sử dụng để thực hiện các phép toán trên các chuỗi nhị phân này và tạo ra một chuỗi nhị phân có cùng độ dài.

**Lưu ý:**

[2] Các trường mở rộng trở nên rất phản trực giác. Thay vì có các phần tử là số nguyên, chúng có các tập hợp đa thức. Ngoài ra, bất kỳ phép toán nào cũng được thực hiện theo modulo một số đa thức bất khả quy.

## Đại số trừu tượng trong thực tế

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Bất chấp ngôn ngữ chính thức và tính trừu tượng của cuộc thảo luận, khái niệm về nhóm không quá khó để nắm bắt. Nó chỉ là một tập hợp các phần tử cùng với một phép toán nhị phân, trong đó hiệu suất của phép toán nhị phân đó trên các phần tử đó đáp ứng bốn điều kiện chung. Một nhóm Abelian chỉ có một điều kiện bổ sung được gọi là tính giao hoán. Một nhóm cyclic, đến lượt nó, là một loại nhóm Abelian đặc biệt, cụ thể là nhóm có một bộ tạo. Một trường chỉ đơn thuần là một cấu trúc phức tạp hơn từ khái niệm nhóm cơ bản.

Nhưng nếu bạn là người có khuynh hướng thực tế, bạn có thể tự hỏi tại thời điểm này: Ai quan tâm? Việc biết một số tập hợp các phần tử có toán tử là một nhóm, hoặc thậm chí là một nhóm Abelian hoặc nhóm tuần hoàn, có liên quan gì đến thế giới thực không? Việc biết một cái gì đó là một trường?

Không đi sâu vào quá nhiều chi tiết, câu trả lời là "có". Các nhóm lần đầu tiên được tạo ra vào thế kỷ 19 bởi nhà toán học người Pháp Evariste Galois. Ông đã sử dụng chúng để đưa ra kết luận về việc giải các phương trình đa thức có bậc cao hơn năm.

Kể từ đó, khái niệm nhóm đã giúp làm sáng tỏ một số vấn đề trong toán học và những nơi khác. Ví dụ, trên cơ sở của chúng, nhà vật lý Murray-Gellman đã có thể dự đoán sự tồn tại của một hạt trước khi nó thực sự được quan sát trong các thí nghiệm. [3] Một ví dụ khác, các nhà hóa học sử dụng lý thuyết nhóm để phân loại hình dạng của các phân tử. Các nhà toán học thậm chí đã sử dụng khái niệm nhóm để rút ra kết luận về một thứ cụ thể như giấy dán tường!

Về cơ bản, việc chỉ ra rằng một tập hợp các phần tử có một số toán tử là một nhóm, có nghĩa là những gì bạn đang mô tả có một tính đối xứng cụ thể. Không phải tính đối xứng theo nghĩa thông thường của từ này, mà ở dạng trừu tượng hơn. Và điều này có thể cung cấp những hiểu biết sâu sắc đáng kể về các hệ thống và vấn đề cụ thể. Các khái niệm phức tạp hơn từ đại số trừu tượng chỉ cung cấp cho chúng ta thông tin bổ sung.

Quan trọng nhất, bạn sẽ thấy tầm quan trọng của các nhóm và trường lý thuyết số trong thực tế thông qua ứng dụng của chúng trong mật mã, đặc biệt là mật mã khóa công khai. Ví dụ, chúng ta đã thấy trong phần thảo luận về các trường, cách các trường mở rộng được sử dụng trong Mật mã Rijndael. Chúng ta sẽ giải quyết ví dụ đó trong *Chương 5*.

Để thảo luận thêm về đại số trừu tượng, tôi muốn giới thiệu loạt video tuyệt vời về đại số trừu tượng của Socratica. [4] Tôi đặc biệt muốn giới thiệu các video sau: “Đại số trừu tượng là gì?”, “Định nghĩa nhóm (mở rộng)”, “Định nghĩa vành (mở rộng)” và “Định nghĩa trường (mở rộng)”. Bốn video này sẽ cung cấp cho bạn một số hiểu biết bổ sung về nhiều nội dung thảo luận ở trên. (Chúng tôi không thảo luận về vành, nhưng trường chỉ là một loại vành đặc biệt.)

Để thảo luận thêm về lý thuyết số hiện đại, bạn có thể tham khảo nhiều cuộc thảo luận nâng cao về mật mã. Tôi xin đưa ra gợi ý về Introduction to Modern Cryptography của Jonathan Katz và Yehuda Lindell hoặc Understanding Cryptography của Christof Paar và Jan Pelzl để thảo luận thêm. [5]

**Lưu ý:**

[3] Xem [Video YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Đại số trừu tượng](https://www.socratica.com/subject/abstract-algebra)

[5] Katz và Lindell, *Giới thiệu về mật mã học hiện đại*, ấn bản lần thứ 2, 2015 (CRC Press: Boca Raton, FL). Paar và Pelzl, *Hiểu về mật mã học*, 2010 (Springer-Verlag: Berlin).

# Mật mã đối xứng

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice và Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Một trong hai nhánh chính của mật mã là mật mã đối xứng. Nó bao gồm các lược đồ mã hóa cũng như các lược đồ liên quan đến xác thực và toàn vẹn. Cho đến những năm 1970, tất cả mật mã đều bao gồm các lược đồ mã hóa đối xứng.

Cuộc thảo luận chính bắt đầu bằng việc xem xét các lược đồ mã hóa đối xứng và đưa ra sự phân biệt quan trọng giữa mã hóa luồng và mã hóa khối. Sau đó, chúng ta chuyển sang mã xác thực tin nhắn, là các lược đồ đảm bảo tính toàn vẹn và tính xác thực của tin nhắn. Cuối cùng, chúng ta khám phá cách các lược đồ mã hóa đối xứng và mã xác thực tin nhắn có thể được kết hợp để đảm bảo giao tiếp an toàn.

Chương này thảo luận về nhiều lược đồ mật mã đối xứng khác nhau từ thực hành. Chương tiếp theo cung cấp một bài trình bày chi tiết về mã hóa với mã hóa luồng và mã hóa khối từ thực hành, cụ thể là RC4 và AES.

Trước khi bắt đầu thảo luận về mật mã đối xứng, tôi muốn đưa ra một số nhận xét ngắn gọn về hình ảnh minh họa Alice và Bob trong chương này và các chương tiếp theo.

___

Khi minh họa các nguyên tắc của mật mã, mọi người thường dựa vào các ví dụ liên quan đến Alice và Bob. Tôi cũng sẽ làm như vậy.

Đặc biệt nếu bạn mới làm quen với mật mã, điều quan trọng là phải nhận ra rằng những ví dụ về Alice và Bob này chỉ nhằm mục đích minh họa cho các nguyên tắc và cấu trúc mật mã trong một môi trường đơn giản hóa. Tuy nhiên, các nguyên tắc và cấu trúc này có thể áp dụng cho nhiều bối cảnh thực tế hơn.

Sau đây là năm điểm chính cần ghi nhớ về các ví dụ liên quan đến Alice và Bob trong mật mã:

1. Chúng có thể dễ dàng được dịch thành các ví dụ với các loại tác nhân khác như công ty hoặc tổ chức chính phủ.

2. Có thể dễ dàng mở rộng để bao gồm ba diễn viên trở lên.

3. Trong các ví dụ, Bob và Alice thường là những người tham gia tích cực trong việc tạo ra từng thông điệp và trong việc áp dụng các lược đồ mật mã trên thông điệp đó. Nhưng trên thực tế, các thông tin liên lạc điện tử phần lớn là tự động. Ví dụ, khi bạn truy cập một trang web sử dụng bảo mật lớp truyền tải, thì thông thường, tất cả mật mã đều được xử lý bởi máy tính của bạn và máy chủ web.

4. Trong bối cảnh giao tiếp điện tử, “tin nhắn” được gửi qua kênh giao tiếp thường là các gói TCP/IP. Chúng có thể thuộc về một e-mail, tin nhắn Facebook, cuộc trò chuyện qua điện thoại, chuyển tập tin, trang web, tải phần mềm, v.v. Chúng không phải là tin nhắn theo nghĩa truyền thống. Tuy nhiên, các nhà mật mã học thường đơn giản hóa thực tế này bằng cách nêu rằng tin nhắn, ví dụ, là một e-mail.

5. Các ví dụ thường tập trung vào giao tiếp điện tử, nhưng cũng có thể mở rộng sang các hình thức giao tiếp truyền thống như thư từ.

## Các chương trình mã hóa đối xứng

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Chúng ta có thể định nghĩa một cách rộng rãi **sơ đồ mã hóa đối xứng** là bất kỳ sơ đồ mật mã nào có ba thuật toán:

1. **Thuật toán tạo khóa**, tạo ra khóa riêng tư.

2. **Thuật toán mã hóa**, sử dụng khóa riêng và văn bản thuần túy làm đầu vào và đưa ra văn bản mã hóa.

3. **Thuật toán giải mã**, lấy khóa riêng và văn bản mã hóa làm đầu vào và đưa ra văn bản thuần túy gốc.

Thông thường, một lược đồ mã hóa, dù là đối xứng hay không đối xứng, đều cung cấp một mẫu mã hóa dựa trên thuật toán cốt lõi, thay vì một thông số kỹ thuật chính xác.

Ví dụ, hãy xem xét Salsa20, một lược đồ mã hóa đối xứng. Nó có thể được sử dụng với cả độ dài khóa 128 và 256 bit. Lựa chọn về độ dài khóa ảnh hưởng đến một số chi tiết nhỏ của thuật toán (chính xác là số vòng trong thuật toán).

Nhưng người ta không thể nói rằng sử dụng Salsa20 với khóa 128 bit là một lược đồ mã hóa khác với Salsa20 với khóa 256 bit. Thuật toán cốt lõi vẫn giữ nguyên. Chỉ khi thuật toán cốt lõi thay đổi thì chúng ta mới thực sự nói đến hai lược đồ mã hóa khác nhau.

Các chương trình mã hóa đối xứng thường hữu ích trong hai trường hợp: (1) Các trường hợp mà hai hoặc nhiều tác nhân giao tiếp từ xa và muốn giữ bí mật nội dung giao tiếp của họ; và (2) các trường hợp mà một tác nhân muốn giữ bí mật nội dung của một tin nhắn theo thời gian.

Bạn có thể thấy mô tả về tình huống (1) trong *Hình 1* bên dưới. Bob muốn gửi một tin nhắn $M$ cho Alice qua một khoảng cách, nhưng không muốn những người khác có thể đọc được tin nhắn đó.

Đầu tiên, Bob mã hóa tin nhắn $M$ bằng khóa riêng $K$. Sau đó, anh ta gửi bản mã $C$ cho Alice. Sau khi Alice nhận được bản mã, cô ấy có thể giải mã bằng khóa $K$ và đọc bản rõ. Với một lược đồ mã hóa tốt, bất kỳ kẻ tấn công nào chặn được bản mã $C$ sẽ không thể biết được bất kỳ điều gì có ý nghĩa thực sự về tin nhắn $M$.

Bạn có thể thấy mô tả về tình huống (2) trong *Hình 2* bên dưới. Bob muốn ngăn người khác xem một số thông tin nhất định. Một tình huống điển hình có thể là Bob là một nhân viên lưu trữ dữ liệu nhạy cảm trên máy tính của mình, mà cả người ngoài và đồng nghiệp của anh ta đều không được phép đọc.

Bob mã hóa thông điệp $M$ tại thời điểm $T_0$ bằng khóa $K$ để tạo ra bản mã $C$. Tại thời điểm $T_1$, anh ta cần thông điệp một lần nữa và giải mã bản mã $C$ bằng khóa $K$. Bất kỳ kẻ tấn công nào có thể đã bắt gặp bản mã $C$ trong thời gian đó sẽ không thể suy ra bất kỳ điều gì quan trọng về $M$ từ nó.

*Hình 1: Bí mật trên không gian*

![Figure 1: Secrecy across space](assets/Figure4-1.webp "Figure 1: Secrecy across space")

*Hình 2: Sự bí mật theo thời gian*

![Figure 2: Secrecy across time](assets/Figure4-2.webp "Figure 2: Secrecy across time")

## Một ví dụ: Mã dịch chuyển

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Trong Chương 2, chúng ta đã gặp mã hóa dịch chuyển, đây là một ví dụ về một lược đồ mã hóa đối xứng rất đơn giản. Chúng ta hãy xem lại nó ở đây.

Giả sử một từ điển *D* coi tất cả các chữ cái của bảng chữ cái tiếng Anh, theo thứ tự, bằng tập hợp các số $\{0,1,2,\dots,25\}$. Giả sử một tập hợp các thông điệp có thể **M**. Khi đó, mã hóa dịch chuyển là một lược đồ mã hóa được định nghĩa như sau:


- Chọn ngẫu nhiên một khóa $k$ trong tập hợp các khóa có thể có **K**, trong đó **K** = $\{0,1,2,\dots,25\}$
- Mã hóa tin nhắn $m \in$ **M**, như sau:
    - Phân tách $m$ thành các chữ cái riêng lẻ $m_0, m_1,\dots, m_i, \dots, m_l$
    - Chuyển đổi mỗi $m_i$ thành một số theo *D*
    - Với mỗi $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Chuyển đổi mỗi $c_i$ thành một chữ cái theo *D*
    - Sau đó kết hợp $c_0, c_1,\dots, c_l$ để tạo ra bản mã $c$
- Giải mã một bản mã $c$ như sau:
    - Chuyển đổi mỗi $c_i$ thành một số theo *D*
    - Với mỗi $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Chuyển đổi mỗi $m_i$ thành một chữ cái theo *D*
    - Sau đó kết hợp $m_0, m_1,\dots, m_l$ để tạo ra thông điệp gốc $m$

Điều làm cho mã hóa dịch chuyển trở thành một lược đồ mã hóa đối xứng là cùng một khóa được sử dụng cho cả quá trình mã hóa và giải mã. Ví dụ, giả sử bạn muốn mã hóa tin nhắn “DOG” bằng mã hóa dịch chuyển và bạn chọn ngẫu nhiên "24" làm khóa. Mã hóa tin nhắn bằng khóa này sẽ tạo ra “BME”. Cách duy nhất để lấy lại tin nhắn gốc là sử dụng cùng một khóa, "24", cho quá trình giải mã.

Mã hóa Shift này là một ví dụ về **mã hóa thay thế đơn bảng chữ cái**: một lược đồ mã hóa trong đó bảng chữ cái của văn bản mã hóa là cố định (tức là chỉ sử dụng một bảng chữ cái). Giả sử rằng thuật toán giải mã là xác định, thì mỗi ký hiệu trong văn bản mã hóa thay thế có thể liên quan đến nhiều nhất một ký hiệu trong văn bản gốc.

Cho đến những năm 1700, nhiều ứng dụng mã hóa dựa nhiều vào mật mã thay thế đơn chữ cái, mặc dù chúng thường phức tạp hơn nhiều so với mật mã Shift. Ví dụ, bạn có thể chọn ngẫu nhiên một chữ cái từ bảng chữ cái cho mỗi chữ cái trong văn bản gốc theo ràng buộc là mỗi chữ cái chỉ xuất hiện một lần trong bảng chữ cái của văn bản mã hóa. Điều đó có nghĩa là bạn sẽ có 26 khóa riêng có thể có, một con số khổng lồ trong thời đại tiền máy tính.

Lưu ý rằng bạn sẽ gặp thuật ngữ **cipher** rất nhiều trong mật mã học. Lưu ý rằng thuật ngữ này có nhiều nghĩa khác nhau. Trên thực tế, tôi biết ít nhất năm nghĩa khác nhau của thuật ngữ này trong mật mã học.

Trong một số trường hợp, nó đề cập đến một lược đồ mã hóa, như trong mã hóa Shift và mã hóa thay thế đơn chữ cái. Tuy nhiên, thuật ngữ này cũng có thể đề cập cụ thể đến thuật toán mã hóa, khóa riêng hoặc chỉ là văn bản mã hóa của bất kỳ lược đồ mã hóa nào như vậy.

Cuối cùng, thuật ngữ cipher cũng có thể ám chỉ một thuật toán cốt lõi mà từ đó bạn có thể xây dựng các lược đồ mật mã. Chúng có thể bao gồm nhiều thuật toán mã hóa khác nhau, nhưng cũng có các loại lược đồ mật mã khác. Ý nghĩa của thuật ngữ này trở nên có liên quan trong bối cảnh của các thuật toán mã khối (xem phần “Block Ciphers” bên dưới).

Bạn cũng có thể bắt gặp các thuật ngữ **mã hóa** hoặc **giải mã**. Các thuật ngữ này chỉ đơn thuần là từ đồng nghĩa với mã hóa và giải mã.

## Tấn công bằng vũ lực và nguyên tắc của Kerckhoff

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Mã hóa dịch chuyển là một lược đồ mã hóa đối xứng rất không an toàn, ít nhất là trong thế giới hiện đại. [1] Kẻ tấn công có thể chỉ cần cố gắng giải mã bất kỳ văn bản mã hóa nào với tất cả 26 khóa có thể để xem kết quả nào có ý nghĩa. Kiểu tấn công này, trong đó kẻ tấn công chỉ cần lặp lại các khóa để xem khóa nào hiệu quả, được gọi là **tấn công vũ phu** hoặc **tìm kiếm khóa cạn kiệt**.

Đối với bất kỳ lược đồ mã hóa nào để đáp ứng được khái niệm tối thiểu về bảo mật, nó phải có một tập hợp các khóa khả thi hoặc **không gian khóa**, quá lớn đến mức các cuộc tấn công bằng vũ lực là không khả thi. Tất cả các lược đồ mã hóa hiện đại đều đáp ứng tiêu chuẩn này. Nó được gọi là **nguyên tắc không gian khóa đủ**. Một nguyên tắc tương tự thường áp dụng trong các loại lược đồ mật mã khác nhau.

Để cảm nhận được kích thước không gian khóa lớn trong các chương trình mã hóa hiện đại, hãy giả sử rằng một tệp đã được mã hóa bằng khóa 128 bit sử dụng tiêu chuẩn mã hóa nâng cao. Điều này có nghĩa là kẻ tấn công có một bộ $2^{128}$ khóa mà cô ta cần phải tuần hoàn để thực hiện một cuộc tấn công bằng vũ lực. Cơ hội thành công 0,78% với chiến lược này sẽ yêu cầu kẻ tấn công phải tuần hoàn khoảng $2,65 \times 10^{36}$ khóa.

Giả sử chúng ta lạc quan cho rằng kẻ tấn công có thể thử $10^{16}$ khóa mỗi giây (tức là 10 nghìn tỷ khóa mỗi giây). Để kiểm tra 0,78% trong tổng số tất cả các khóa trong không gian khóa, cuộc tấn công của cô ta sẽ phải kéo dài $2,65 \times 10^{20}$ giây. Khoảng 8,4 nghìn tỷ năm. Vì vậy, ngay cả một cuộc tấn công bằng vũ lực của một đối thủ mạnh đến mức phi lý cũng không thực tế với một lược đồ mã hóa 128 bit hiện đại. Đây là nguyên tắc không gian khóa đủ đang được áp dụng.

Liệu mã hóa dịch chuyển có an toàn hơn nếu kẻ tấn công không biết thuật toán mã hóa không? Có thể, nhưng không nhiều.

Trong mọi trường hợp, mật mã học hiện đại luôn cho rằng tính bảo mật của bất kỳ lược đồ mã hóa đối xứng nào chỉ dựa vào việc giữ bí mật khóa riêng. Kẻ tấn công luôn được cho là biết tất cả các chi tiết khác, bao gồm không gian tin nhắn, không gian khóa, không gian văn bản mã hóa, thuật toán lựa chọn khóa, thuật toán mã hóa và thuật toán giải mã.

Ý tưởng cho rằng tính bảo mật của một lược đồ mã hóa đối xứng chỉ có thể dựa vào tính bí mật của khóa riêng được gọi là **nguyên tắc Kerckhoff**.

Theo ý định ban đầu của Kerckhoffs, nguyên tắc này chỉ áp dụng cho các lược đồ mã hóa đối xứng. Tuy nhiên, một phiên bản tổng quát hơn của nguyên tắc này cũng áp dụng cho tất cả các loại lược đồ mật mã hiện đại khác: Thiết kế của bất kỳ lược đồ mật mã nào cũng không nhất thiết phải được giữ bí mật để được coi là an toàn; tính bảo mật chỉ có thể mở rộng đến một số chuỗi thông tin, thường là khóa riêng.

Nguyên lý của Kerckhoffs là trung tâm của mật mã hiện đại vì bốn lý do. [2] Đầu tiên, chỉ có một số lượng hạn chế các lược đồ mật mã cho các loại ứng dụng cụ thể. Ví dụ, hầu hết các ứng dụng mã hóa đối xứng hiện đại đều sử dụng mật mã Rijndael. Vì vậy, tính bảo mật của bạn liên quan đến thiết kế của lược đồ chỉ rất hạn chế. Tuy nhiên, có nhiều tính linh hoạt hơn trong việc giữ một số khóa riêng cho bí mật mật mã Rijndael.

Thứ hai, dễ thay thế một số chuỗi thông tin hơn là toàn bộ một chương trình mã hóa. Giả sử rằng tất cả nhân viên của một công ty đều có cùng một phần mềm mã hóa và cứ hai nhân viên thì có một khóa riêng để giao tiếp một cách bảo mật. Việc xâm phạm khóa là một rắc rối trong trường hợp này, nhưng ít nhất công ty có thể giữ nguyên phần mềm với các vi phạm bảo mật như vậy. Nếu công ty dựa vào tính bảo mật của chương trình, thì bất kỳ vi phạm nào đối với tính bảo mật đó sẽ yêu cầu thay thế toàn bộ phần mềm.

Thứ ba, nguyên tắc của Kerckhoffs cho phép chuẩn hóa và tương thích giữa những người dùng các chương trình mã hóa. Điều này mang lại lợi ích to lớn cho hiệu quả. Ví dụ, thật khó để tưởng tượng hàng triệu người có thể kết nối an toàn với máy chủ web của Google mỗi ngày, nếu bảo mật đó đòi hỏi phải giữ bí mật các chương trình mã hóa.

Thứ tư, nguyên tắc của Kerckhoff cho phép công chúng giám sát các chương trình mật mã. Kiểu giám sát này hoàn toàn cần thiết để đạt được các chương trình mật mã an toàn. Minh họa, thuật toán cốt lõi chính trong mật mã đối xứng, mật mã Rijndael, là kết quả của một cuộc thi do Viện Tiêu chuẩn và Công nghệ Quốc gia tổ chức từ năm 1997 đến năm 2000.

Bất kỳ hệ thống nào cố gắng đạt được **bảo mật bằng sự che giấu** đều dựa vào việc giữ bí mật các chi tiết về thiết kế và/hoặc triển khai. Trong mật mã học, đây sẽ là một hệ thống cụ thể dựa vào việc giữ bí mật các chi tiết thiết kế của lược đồ mật mã. Vì vậy, bảo mật bằng sự che giấu hoàn toàn trái ngược với nguyên tắc của Kerckhoffs.

Khả năng của tính cởi mở trong việc tăng cường chất lượng và bảo mật cũng mở rộng hơn đến thế giới kỹ thuật số chứ không chỉ là mật mã. Các bản phân phối Linux miễn phí và mã nguồn mở như Debian, chẳng hạn, thường có một số lợi thế hơn so với các bản phân phối Windows và MacOS về mặt quyền riêng tư, tính ổn định, bảo mật và tính linh hoạt. Mặc dù điều đó có thể có nhiều nguyên nhân, nhưng nguyên tắc quan trọng nhất có lẽ là, như Eric Raymond đã diễn đạt trong bài tiểu luận nổi tiếng của mình "The Cathedral and the Bazaar", rằng "nếu có đủ sự chú ý, mọi lỗi đều trở nên nông cạn". [3] Chính nguyên tắc kiểu trí tuệ của đám đông này đã mang lại cho Linux thành công đáng kể nhất.

Người ta không bao giờ có thể tuyên bố rõ ràng rằng một lược đồ mật mã là "an toàn" hay "không an toàn". Thay vào đó, có nhiều khái niệm khác nhau về bảo mật cho các lược đồ mật mã. Mỗi **định nghĩa về bảo mật mật mã** phải chỉ rõ (1) mục tiêu bảo mật, cũng như (2) khả năng của kẻ tấn công. Phân tích các lược đồ mật mã so với một hoặc nhiều khái niệm bảo mật cụ thể sẽ cung cấp thông tin chi tiết về ứng dụng và hạn chế của chúng.

Mặc dù chúng tôi sẽ không đi sâu vào tất cả các chi tiết của các khái niệm khác nhau về bảo mật mật mã, bạn nên biết rằng có hai giả định phổ biến trong tất cả các khái niệm mật mã hiện đại về bảo mật liên quan đến các lược đồ đối xứng và không đối xứng (và theo một số hình thức đối với các nguyên hàm mật mã khác):


- Kiến thức của kẻ tấn công về kế hoạch này tuân theo nguyên tắc của Kerckhoffs.
- Kẻ tấn công không thể thực hiện một cuộc tấn công vũ phu vào chương trình. Cụ thể, các mô hình đe dọa của các khái niệm mật mã về bảo mật thường thậm chí không cho phép các cuộc tấn công vũ phu, vì chúng cho rằng đây không phải là một cân nhắc có liên quan.

**Lưu ý:**

[1] Theo Seutonius, một mật mã dịch chuyển với giá trị khóa không đổi là 3 đã được Julius Caesar sử dụng trong các thông tin liên lạc quân sự của ông. Vì vậy, A sẽ luôn trở thành D, B luôn là E, C luôn là F, v.v. Do đó, phiên bản cụ thể này của mật mã dịch chuyển đã được gọi là **Mật mã Caesar** (mặc dù nó không thực sự là một mật mã theo nghĩa hiện đại của từ này, vì giá trị khóa là hằng số). Mật mã Caesar có thể đã an toàn vào thế kỷ thứ nhất trước Công nguyên, nếu kẻ thù của Rome không quen với mã hóa. Nhưng rõ ràng nó sẽ không phải là một kế hoạch an toàn trong thời hiện đại.

[2] Jonathan Katz và Yehuda Lindell, _Giới thiệu về mật mã học hiện đại_, CRC Press (Boca Raton, FL: 2015), trang 7f.

[3] Eric Raymond, “The Cathedral and the Bazaar,” bài báo được trình bày tại Linux Kongress, Würzburg, Đức (ngày 27 tháng 5 năm 1997). Có một số phiên bản tiếp theo cũng như một cuốn sách. Trích dẫn của tôi là từ trang 30 trong cuốn sách: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, ấn bản đã sửa đổi (2001), O’Reilly: Sebastopol, CA.

## Mã hóa luồng

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Các lược đồ mã hóa đối xứng thường được chia thành hai loại: **mã hóa luồng** và **mã hóa khối**. Tuy nhiên, sự phân biệt này có phần gây khó khăn vì mọi người sử dụng các thuật ngữ này theo cách không nhất quán. Trong một vài phần tiếp theo, tôi sẽ trình bày sự phân biệt theo cách mà tôi cho là tốt nhất. Tuy nhiên, bạn nên biết rằng nhiều người sẽ sử dụng các thuật ngữ này theo cách hơi khác so với cách tôi trình bày.

Trước tiên, chúng ta hãy chuyển sang mã hóa luồng. **Mã hóa luồng** là một lược đồ mã hóa đối xứng trong đó mã hóa bao gồm hai bước.

Đầu tiên, một chuỗi có độ dài bằng văn bản thuần túy được tạo ra thông qua khóa riêng. Chuỗi này được gọi là **keystream**.

Tiếp theo, luồng khóa được kết hợp toán học với văn bản thuần túy để tạo ra văn bản mã hóa. Sự kết hợp này thường là một phép toán XOR. Để giải mã, bạn chỉ có thể đảo ngược phép toán. (Lưu ý rằng $A \oplus B = B \oplus A$, trong trường hợp $A$ và $B$ là các chuỗi bit. Vì vậy, thứ tự của một phép toán XOR trong mã hóa luồng không quan trọng đối với kết quả. Thuộc tính này được gọi là **tính giao hoán**.)

Một mã hóa luồng XOR điển hình được mô tả trong *Hình 3*. Trước tiên, bạn lấy khóa riêng $K$ và sử dụng nó để tạo ra luồng khóa. Sau đó, luồng khóa được kết hợp với văn bản thuần túy thông qua thao tác XOR để tạo ra văn bản mã hóa. Bất kỳ tác nhân nào nhận được văn bản mã hóa đều có thể dễ dàng giải mã nó nếu họ có khóa $K$. Tất cả những gì cô ấy cần làm là tạo luồng khóa miễn là văn bản mã hóa theo quy trình được chỉ định của lược đồ và XOR nó với văn bản mã hóa.

*Hình 3: Mã hóa luồng XOR*

![Figure 3: An XOR stream cipher](assets/Figure4-3.webp "Figure 3: An XOR stream cipher")

Xin lưu ý rằng một lược đồ mã hóa thường là một khuôn mẫu để mã hóa với cùng một thuật toán cốt lõi, chứ không phải là một thông số kỹ thuật chính xác. Theo nghĩa mở rộng, một mã hóa luồng thường là một khuôn mẫu để mã hóa trong đó bạn có thể sử dụng các khóa có độ dài khác nhau. Mặc dù độ dài khóa có thể ảnh hưởng đến một số chi tiết nhỏ của lược đồ, nhưng nó sẽ không ảnh hưởng đến hình thức thiết yếu của nó.

Mã hóa dịch chuyển là một ví dụ về mã hóa luồng rất đơn giản và không an toàn. Sử dụng một chữ cái duy nhất (khóa riêng), bạn có thể tạo ra một chuỗi các chữ cái có độ dài bằng thông điệp (luồng khóa). Sau đó, luồng khóa này được kết hợp với văn bản thuần túy thông qua một phép toán modulo để tạo ra một văn bản mã hóa. (Phép toán modulo này có thể được đơn giản hóa thành phép toán XOR khi biểu diễn các chữ cái theo bit).

Một ví dụ nổi tiếng khác về mã hóa luồng là **mã hóa Vigenere**, theo tên Blaise de Vigenere, người đã phát triển đầy đủ vào cuối thế kỷ 16 (mặc dù những người khác đã thực hiện rất nhiều công trình trước đó). Đây là một ví dụ về **mã hóa thay thế đa bảng chữ cái**: một lược đồ mã hóa trong đó bảng chữ cái mã hóa cho một ký hiệu văn bản thuần túy thay đổi tùy thuộc vào vị trí của nó trong văn bản. Ngược lại với mã hóa thay thế đơn bảng chữ cái, các ký hiệu văn bản mã hóa có thể được liên kết với nhiều hơn một ký hiệu văn bản thuần túy.

Khi mã hóa trở nên phổ biến ở Châu Âu thời Phục hưng, thì **phân tích mật mã**—tức là việc phá mã—cũng vậy, đặc biệt là sử dụng **phân tích tần suất**. Phương pháp sau sử dụng các quy luật thống kê trong ngôn ngữ của chúng ta để phá mã, và đã được các học giả tiếng Ả Rập phát hiện ra vào thế kỷ thứ chín. Đây là một kỹ thuật hoạt động đặc biệt hiệu quả với các văn bản dài hơn. Và ngay cả các mật mã thay thế đơn chữ cái tinh vi nhất cũng không còn đủ để chống lại phân tích tần suất vào những năm 1700 ở Châu Âu, đặc biệt là trong các bối cảnh quân sự và an ninh. Vì mật mã Vigenere mang lại bước tiến đáng kể về mặt an ninh nên nó đã trở nên phổ biến trong giai đoạn này và được sử dụng rộng rãi vào cuối những năm 1700.

Nói một cách không chính thức, chương trình mã hóa hoạt động như sau:

1. Chọn một từ nhiều chữ cái làm khóa riêng.

2. Đối với bất kỳ tin nhắn nào, hãy áp dụng mã dịch chuyển cho từng chữ cái của tin nhắn bằng cách sử dụng chữ cái tương ứng trong từ khóa làm mã dịch chuyển.

3. Nếu bạn đã duyệt qua từ khóa nhưng vẫn chưa mã hóa hoàn toàn văn bản thuần túy, hãy áp dụng lại các chữ cái của từ khóa làm mã dịch chuyển cho các chữ cái tương ứng trong phần còn lại của văn bản.

4. Tiếp tục quá trình này cho đến khi toàn bộ tin nhắn được mã hóa.

Để minh họa, giả sử khóa riêng của bạn là "GOLD" và bạn muốn mã hóa tin nhắn "CRYPTOGRAPHY". Trong trường hợp đó, bạn sẽ tiến hành như sau theo mật mã Vigenère:


- $c_0 = [(2 + 6) \mod 26] = 8 = I$
- $c_1 = [(17 + 14) \mod 26] = 5 = F$
- $c_2 = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Do đó, văn bản mã hóa $c$ = "IFJSZCRUGDSB".

Một ví dụ nổi tiếng khác về mã hóa luồng là **one-time pad**. Với one-time pad, bạn chỉ cần tạo một chuỗi bit ngẫu nhiên dài bằng tin nhắn văn bản thuần túy và tạo ra văn bản mã hóa thông qua phép toán XOR. Do đó, khóa riêng và luồng khóa tương đương với one-time pad.

Trong khi mã Shift và mã Vigenere rất không an toàn trong thời đại hiện đại, thì sổ ghi chép một lần rất an toàn nếu sử dụng đúng cách. Có lẽ ứng dụng nổi tiếng nhất của sổ ghi chép một lần là, ít nhất là cho đến những năm 1980, cho **đường dây nóng Washington-Moscow**. [4]

Đường dây nóng là đường liên lạc trực tiếp giữa Washington và Moscow cho các vấn đề khẩn cấp được lắp đặt sau Khủng hoảng tên lửa Cuba. Công nghệ cho đường dây đã thay đổi qua nhiều năm. Hiện tại, nó bao gồm một cáp quang trực tiếp cũng như hai liên kết vệ tinh (để dự phòng), cho phép gửi email và nhắn tin văn bản. Đường liên kết kết thúc ở nhiều nơi khác nhau tại Hoa Kỳ. Lầu Năm Góc, Nhà Trắng và Raven Rock Mountain là những điểm cuối đã biết. Trái với quan điểm phổ biến, đường dây nóng chưa bao giờ liên quan đến điện thoại.

Về bản chất, chương trình one-time pad hoạt động như sau. Cả Washington và Moscow đều có hai bộ số ngẫu nhiên. Một bộ số ngẫu nhiên, do người Nga tạo ra, liên quan đến mã hóa và giải mã bất kỳ thông điệp nào bằng tiếng Nga. Một bộ số ngẫu nhiên, do người Mỹ tạo ra, liên quan đến mã hóa và giải mã bất kỳ thông điệp nào bằng tiếng Anh. Thỉnh thoảng, nhiều số ngẫu nhiên hơn sẽ được chuyển đến phía bên kia bởi những người đưa tin đáng tin cậy.

Washington và Moscow sau đó có thể giao tiếp bí mật bằng cách sử dụng những con số ngẫu nhiên này để tạo ra các miếng đệm dùng một lần. Mỗi lần bạn cần giao tiếp, bạn sẽ sử dụng phần tiếp theo của các con số ngẫu nhiên cho tin nhắn của mình.

Mặc dù có tính bảo mật cao, nhưng one-time pad phải đối mặt với những hạn chế thực tế đáng kể: khóa phải dài bằng tin nhắn và không có phần nào của one-time pad có thể được sử dụng lại. Điều này có nghĩa là bạn cần theo dõi vị trí của mình trong one-time pad, lưu trữ một số lượng lớn bit và trao đổi bit ngẫu nhiên với các đối tác của bạn theo thời gian. Do đó, one-time pad không thường xuyên được sử dụng trong thực tế.

Thay vào đó, các mã luồng chủ yếu được sử dụng trong thực tế là **mã luồng giả ngẫu nhiên**. Salsa20 và một biến thể có liên quan chặt chẽ được gọi là ChaCha là những ví dụ về các mã luồng giả ngẫu nhiên thường được sử dụng.

Với các mã hóa luồng giả ngẫu nhiên này, trước tiên bạn chọn ngẫu nhiên một khóa K ngắn hơn độ dài của văn bản thuần túy. Khóa ngẫu nhiên K như vậy thường được máy tính của chúng ta tạo ra dựa trên dữ liệu không thể đoán trước mà nó thu thập theo thời gian, chẳng hạn như thời gian giữa các tin nhắn mạng, chuyển động của chuột, v.v.

Khóa ngẫu nhiên $K$ này sau đó được chèn vào thuật toán mở rộng tạo ra luồng khóa giả ngẫu nhiên dài bằng thông điệp. Bạn có thể chỉ định chính xác luồng khóa cần dài bao nhiêu (ví dụ: 500 bit, 1000 bit, 1200 bit, 29.117 bit, v.v.).

Một luồng khóa giả ngẫu nhiên xuất hiện *như thể* nó được chọn hoàn toàn ngẫu nhiên từ tập hợp tất cả các chuỗi có cùng độ dài. Do đó, mã hóa bằng luồng khóa giả ngẫu nhiên xuất hiện như thể nó đã được thực hiện bằng một bảng một lần. Nhưng tất nhiên, không phải vậy.

Vì khóa riêng của chúng ta ngắn hơn luồng khóa và thuật toán mở rộng của chúng ta cần phải mang tính xác định để quá trình mã hóa/giải mã hoạt động, nên không phải mọi luồng khóa có độ dài cụ thể đó đều có thể là kết quả đầu ra từ hoạt động mở rộng của chúng ta.

Giả sử, ví dụ, khóa riêng của chúng ta có độ dài 128 bit và chúng ta có thể chèn nó vào một thuật toán mở rộng để tạo ra một luồng khóa dài hơn nhiều, chẳng hạn như 2.500 bit. Vì thuật toán mở rộng của chúng ta cần phải xác định, thuật toán của chúng ta có thể chọn tối đa $1/2^{128}$ chuỗi có độ dài 2.500 bit. Vì vậy, luồng khóa như vậy không bao giờ có thể được chọn hoàn toàn ngẫu nhiên từ tất cả các chuỗi có cùng độ dài.

Định nghĩa của chúng tôi về mã hóa luồng có hai khía cạnh: (1) luồng khóa miễn là văn bản thuần túy được tạo ra với sự trợ giúp của khóa riêng; và (2) luồng khóa này được kết hợp với văn bản thuần túy, thường thông qua thao tác XOR, để tạo ra văn bản mã hóa.

Đôi khi mọi người định nghĩa điều kiện (1) chặt chẽ hơn, bằng cách khẳng định rằng luồng khóa phải là ngẫu nhiên giả. Điều này có nghĩa là cả mã hóa dịch chuyển và bảng một lần đều không được coi là mã hóa luồng.

Theo quan điểm của tôi, việc xác định điều kiện (1) một cách rộng hơn cung cấp một cách dễ dàng hơn để tổ chức các lược đồ mã hóa. Ngoài ra, điều đó có nghĩa là chúng ta không phải ngừng gọi một lược đồ mã hóa cụ thể là mã hóa luồng chỉ vì chúng ta biết rằng nó thực sự không dựa vào các luồng khóa giả ngẫu nhiên.

**Lưu ý:**

[4] Bảo tàng Crypto, "Đường dây nóng Washington-Moscow", 2013, có tại [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Khối mã hóa

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Cách đầu tiên mà **mã hóa khối** thường được hiểu là một thứ gì đó nguyên thủy hơn mã hóa luồng: Một thuật toán cốt lõi thực hiện phép biến đổi bảo toàn độ dài trên một chuỗi có độ dài phù hợp với sự trợ giúp của khóa. Thuật toán này có thể được sử dụng để tạo ra các lược đồ mã hóa và có lẽ là các loại lược đồ mật mã khác.

Thông thường, một mã khối có thể lấy các chuỗi đầu vào có độ dài khác nhau như 64, 128 hoặc 256 bit, cũng như các khóa có độ dài khác nhau như 128, 192 hoặc 256 bit. Mặc dù một số chi tiết của thuật toán có thể thay đổi tùy thuộc vào các biến này, nhưng thuật toán cốt lõi không thay đổi. Nếu có, chúng ta sẽ nói về hai mã khối khác nhau. Lưu ý rằng việc sử dụng thuật ngữ thuật toán cốt lõi ở đây giống như đối với các lược đồ mã hóa.

Có thể thấy mô tả về cách thức hoạt động của mã khối trong *Hình 4* bên dưới. Một thông điệp $M$ có độ dài $L$ và một khóa $K$ đóng vai trò là đầu vào cho mã khối. Nó cho ra một thông điệp $M'$ có độ dài $L$. Khóa không nhất thiết phải có cùng độ dài với $M$ và $M'$ đối với hầu hết các mã khối.

*Hình 4: Một khối mã hóa*

![Figure 4: A block cipher](assets/Figure4-4.webp "Figure 4: A block cipher")

Bản thân mã khối không phải là một lược đồ mã hóa. Nhưng mã khối có thể được sử dụng với nhiều **chế độ hoạt động** khác nhau để tạo ra các lược đồ mã hóa khác nhau. Một chế độ hoạt động chỉ đơn giản là thêm một số thao tác bổ sung bên ngoài mã khối.

Để minh họa cách thức hoạt động này, hãy giả sử một mã khối (BC) yêu cầu chuỗi đầu vào 128 bit và khóa riêng 128 bit. Hình 5 bên dưới hiển thị cách mã khối đó có thể được sử dụng với **chế độ sổ mã điện tử** (**chế độ ECB**) để tạo ra một lược đồ mã hóa. (Các dấu ba chấm ở bên phải cho biết bạn có thể lặp lại mẫu này bao lâu tùy thích).

*Hình 5: Mã khối với chế độ ECB*

![Figure 5: A block cipher with ECB mode](assets/Figure4-5.webp "Figure 5: A block cipher with ECB mode")

Quy trình mã hóa sổ mã điện tử bằng mã khối như sau. Xem bạn có thể chia thông điệp văn bản thuần túy của mình thành các khối 128 bit không. Nếu không, hãy thêm **đệm** vào thông điệp để kết quả có thể được chia đều cho kích thước khối 128 bit. Đây là dữ liệu của bạn được sử dụng cho quy trình mã hóa.

Bây giờ hãy chia dữ liệu thành các phần chuỗi 128 bit ($M_1$, $M_2$, $M_3$, v.v.). Chạy từng chuỗi 128 bit qua mã khối với khóa 128 bit của bạn để tạo ra các phần văn bản mã hóa 128 bit ($C_1$, $C_2$, $C_3$, v.v.). Các phần này, khi được kết hợp lại, sẽ tạo thành văn bản mã hóa đầy đủ.

Giải mã chỉ là quá trình ngược lại, mặc dù người nhận cần một số cách dễ nhận biết để loại bỏ bất kỳ phần đệm nào khỏi dữ liệu đã giải mã để tạo ra thông điệp văn bản thuần túy ban đầu.

Mặc dù tương đối đơn giản, một khối mã hóa với chế độ sổ mã điện tử thiếu tính bảo mật. Điều này là do nó dẫn đến **mã hóa xác định**. Bất kỳ hai chuỗi dữ liệu 128 bit giống hệt nhau nào cũng được mã hóa theo cùng một cách. Thông tin đó có thể bị khai thác.

Thay vào đó, bất kỳ lược đồ mã hóa nào được xây dựng từ mã khối đều phải **có tính xác suất**: nghĩa là, việc mã hóa bất kỳ thông điệp $M$ nào hoặc bất kỳ phần cụ thể nào của $M$, nhìn chung sẽ tạo ra kết quả khác nhau mỗi lần. [5]

**Chế độ chuỗi khối mã hóa** (**chế độ CBC**) có lẽ là chế độ phổ biến nhất được sử dụng với mã hóa khối. Sự kết hợp, nếu được thực hiện đúng, sẽ tạo ra một sơ đồ mã hóa xác suất. Bạn có thể xem mô tả về chế độ hoạt động này trong *Hình 6* bên dưới.

*Hình 6: Mã khối với chế độ CBC*

![Figure 6: A block cipher with CBC mode](assets/Figure4-6.webp "Figure 6: A block cipher with CBC mode")

Giả sử kích thước khối lại là 128 bit. Vì vậy, để bắt đầu, bạn sẽ lại cần đảm bảo rằng tin nhắn văn bản gốc của bạn nhận được phần đệm cần thiết.

Sau đó, bạn XOR phần 128 bit đầu tiên của văn bản thuần túy của bạn với **vectơ khởi tạo** 128 bit. Kết quả được đưa vào mã hóa khối để tạo ra văn bản mã hóa cho khối đầu tiên. Đối với khối thứ hai gồm 128 bit, trước tiên bạn XOR văn bản thuần túy với văn bản mã hóa từ khối đầu tiên, trước khi chèn nó vào mã hóa khối. Bạn tiếp tục quá trình này cho đến khi bạn mã hóa toàn bộ tin nhắn văn bản thuần túy của mình.

Khi hoàn tất, bạn gửi tin nhắn được mã hóa cùng với vectơ khởi tạo chưa mã hóa cho người nhận. Người nhận cần biết vectơ khởi tạo, nếu không, cô ấy không thể giải mã được văn bản mã hóa.

Cấu trúc này an toàn hơn nhiều so với chế độ sổ mã điện tử khi sử dụng đúng cách. Trước tiên, bạn nên đảm bảo rằng vectơ khởi tạo là một chuỗi ngẫu nhiên hoặc giả ngẫu nhiên. Ngoài ra, bạn nên sử dụng một vectơ khởi tạo khác nhau mỗi lần sử dụng lược đồ mã hóa này.

Nói cách khác, vectơ khởi tạo của bạn phải là một nonce ngẫu nhiên hoặc giả ngẫu nhiên, trong đó **nonce** có nghĩa là "một số chỉ được sử dụng một lần". Nếu bạn duy trì thực hành này, thì chế độ CBC với mã hóa khối sẽ đảm bảo rằng bất kỳ hai khối văn bản thuần túy giống hệt nhau nào nhìn chung sẽ được mã hóa khác nhau mỗi lần.

Cuối cùng, chúng ta hãy chuyển sự chú ý sang **chế độ phản hồi đầu ra** (**chế độ OFB**). Bạn có thể xem mô tả về chế độ này trong *Hình 7*.

*Hình 7: Mã hóa khối với chế độ OFB*

![Figure 7: A block cipher with OFB mode](assets/Figure4-7.webp "Figure 7: A block cipher with OFB mode")

Với chế độ OFB, bạn cũng chọn một vectơ khởi tạo. Nhưng ở đây, đối với khối đầu tiên, vectơ khởi tạo được chèn trực tiếp vào mã khối bằng khóa của bạn. 128 bit kết quả sau đó được xử lý như một luồng khóa. Luồng khóa này được XOR với văn bản thuần túy để tạo ra văn bản mã hóa cho khối. Đối với các khối tiếp theo, bạn sử dụng luồng khóa từ khối trước đó làm đầu vào cho mã khối và lặp lại các bước.

Nếu bạn xem xét kỹ, những gì thực sự được tạo ra ở đây từ mã khối với chế độ OFB là mã luồng. Bạn tạo các phần luồng khóa 128 bit cho đến khi bạn có độ dài của văn bản thuần túy (loại bỏ các bit bạn không cần từ phần luồng khóa 128 bit cuối cùng). Sau đó, bạn XOR luồng khóa với thông điệp văn bản thuần túy của mình để có được văn bản mã hóa.

Trong phần trước về mã hóa luồng, tôi đã nêu rằng bạn tạo ra một luồng khóa với sự hỗ trợ của khóa riêng. Chính xác hơn, nó không chỉ phải được tạo bằng khóa riêng. Như bạn có thể thấy trong chế độ OFB, luồng khóa được tạo ra với sự hỗ trợ của cả khóa riêng và vectơ khởi tạo.

Lưu ý rằng giống như chế độ CBC, điều quan trọng là phải chọn một nonce giả ngẫu nhiên hoặc ngẫu nhiên cho vectơ khởi tạo mỗi khi bạn sử dụng mã hóa khối ở chế độ OFB. Nếu không, cùng một chuỗi tin nhắn 128 bit được gửi trong các giao tiếp khác nhau sẽ được mã hóa theo cùng một cách. Đây là một cách để tạo mã hóa xác suất bằng mã hóa luồng.

Một số mã hóa luồng chỉ sử dụng khóa riêng để tạo luồng khóa. Đối với các mã hóa luồng đó, điều quan trọng là bạn phải sử dụng một nonce ngẫu nhiên để chọn khóa riêng cho từng trường hợp giao tiếp. Nếu không, kết quả mã hóa với các mã hóa luồng đó cũng sẽ mang tính xác định, dẫn đến các vấn đề về bảo mật.

Mã khối hiện đại phổ biến nhất là **Mã Rijndael**. Đây là bài dự thi chiến thắng trong số mười lăm bài dự thi được Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) tổ chức từ năm 1997 đến năm 2000 nhằm thay thế một tiêu chuẩn mã hóa cũ hơn, **tiêu chuẩn mã hóa dữ liệu** (**DES**).

Mã Rijndael có thể được sử dụng với các thông số kỹ thuật khác nhau cho độ dài khóa và kích thước khối, cũng như trong các chế độ hoạt động khác nhau. Ủy ban cho cuộc thi NIST đã thông qua một phiên bản thu gọn của mã Rijndael—cụ thể là phiên bản yêu cầu kích thước khối 128 bit và độ dài khóa là 128 bit, 192 bit hoặc 256 bit—như một phần của **tiêu chuẩn mã hóa nâng cao** (**AES**). Đây thực sự là tiêu chuẩn chính cho các ứng dụng mã hóa đối xứng. Nó an toàn đến mức ngay cả NSA dường như cũng sẵn sàng sử dụng nó với khóa 256 bit cho các tài liệu tuyệt mật. [6]

Mã hóa khối AES sẽ được giải thích chi tiết trong *Chương 5*.

**Lưu ý:**

[5] Tầm quan trọng của mã hóa xác suất lần đầu tiên được nhấn mạnh bởi Shafi Goldwasser và Silvio Micali, “Mã hóa xác suất,” _Tạp chí Khoa học Máy tính và Hệ thống_, 28 (1984), 270–99.

[6] Xem NSA, "Bộ thuật toán an ninh quốc gia thương mại", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Làm rõ sự nhầm lẫn

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Sự nhầm lẫn về sự khác biệt giữa mã khối và mã luồng phát sinh vì đôi khi mọi người sẽ hiểu thuật ngữ mã khối là ám chỉ cụ thể đến *mã khối có chế độ mã hóa khối*.

Hãy xem xét các chế độ ECB và CBC trong phần trước. Các chế độ này yêu cầu cụ thể dữ liệu để mã hóa phải chia hết cho kích thước khối (có nghĩa là bạn có thể phải sử dụng phần đệm cho thông điệp gốc). Ngoài ra, dữ liệu trong các chế độ này cũng được mã hóa khối xử lý trực tiếp (và không chỉ kết hợp với kết quả của hoạt động mã hóa khối như trong chế độ OFB).

Do đó, thay vào đó, bạn có thể định nghĩa **mã hóa khối** là bất kỳ lược đồ mã hóa nào, hoạt động trên các khối có độ dài cố định của thông điệp tại một thời điểm (trong đó bất kỳ khối nào cũng phải dài hơn một byte, nếu không nó sẽ sụp đổ thành mã hóa luồng). Cả dữ liệu để mã hóa và văn bản mã hóa phải chia đều thành kích thước khối này. Thông thường, kích thước khối có độ dài là 64, 128, 192 hoặc 256 bit. Ngược lại, mã hóa luồng có thể mã hóa bất kỳ thông điệp nào thành các khối một bit hoặc byte tại một thời điểm.

Với sự hiểu biết cụ thể hơn về mã khối, bạn thực sự có thể khẳng định rằng các lược đồ mã hóa hiện đại là mã luồng hoặc mã khối. Từ đây trở đi, tôi sẽ hiểu thuật ngữ mã khối theo nghĩa chung hơn trừ khi được chỉ định khác.

Cuộc thảo luận về chế độ OFB trong phần trước cũng nêu ra một điểm thú vị khác. Một số mã luồng được xây dựng từ mã khối, như Rijndael với OFB. Một số như Salsa20 và ChaCha không được tạo ra từ mã khối. Bạn có thể gọi những mã sau là **mã luồng nguyên thủy**. (Thực sự không có thuật ngữ chuẩn nào để chỉ những mã luồng như vậy.)

Khi mọi người nói về ưu điểm và nhược điểm của mã luồng và mã khối, họ thường so sánh mã luồng nguyên thủy với các lược đồ mã hóa dựa trên mã khối.

Mặc dù bạn luôn có thể dễ dàng xây dựng một mã luồng từ một mã khối, nhưng thường rất khó để xây dựng một số loại cấu trúc với chế độ mã hóa khối (như chế độ CBC) từ một mã luồng nguyên thủy.

Từ thảo luận này, bây giờ bạn sẽ hiểu *Hình 8*. Nó cung cấp tổng quan về các lược đồ mã hóa đối xứng. Chúng tôi sử dụng ba loại lược đồ mã hóa: mã hóa luồng nguyên thủy, mã hóa luồng khối và mã hóa khối ở chế độ khối (còn được gọi là "mã hóa khối" trong sơ đồ).

*Hình 8: Tổng quan về các chương trình mã hóa đối xứng*

![Figure 8: Overview of symmetric encryption schemes](assets/Figure4-8.webp "Figure 8: Overview of symmetric encryption schemes")

## Mã xác thực tin nhắn

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Mã hóa liên quan đến tính bí mật. Nhưng mật mã cũng liên quan đến các chủ đề rộng hơn, chẳng hạn như tính toàn vẹn của thông điệp, tính xác thực và tính không thể chối cãi. Cái gọi là **mã xác thực thông điệp** (MAC) là các lược đồ mật mã khóa đối xứng hỗ trợ tính xác thực và tính toàn vẹn trong giao tiếp.

Tại sao lại cần bất cứ thứ gì ngoài tính bảo mật trong giao tiếp? Giả sử Bob gửi cho Alice một tin nhắn sử dụng mã hóa gần như không thể phá vỡ. Bất kỳ kẻ tấn công nào chặn được tin nhắn này sẽ không thể xác định được bất kỳ thông tin chi tiết quan trọng nào liên quan đến nội dung. Tuy nhiên, kẻ tấn công vẫn có ít nhất hai vectơ tấn công khác có sẵn cho cô ta:

1. Cô ấy có thể chặn được văn bản mã hóa, thay đổi nội dung của nó và gửi văn bản mã hóa đã thay đổi cho Alice.

2. Cô ấy có thể chặn hoàn toàn tin nhắn của Bob và gửi văn bản mã hóa do cô ấy tạo ra.

Trong cả hai trường hợp này, kẻ tấn công có thể không có bất kỳ hiểu biết nào về nội dung từ các bản mã (1) và (2). Nhưng cô ấy vẫn có thể gây ra thiệt hại đáng kể theo cách này. Đây là nơi mã xác thực tin nhắn trở nên quan trọng.

Mã xác thực tin nhắn được định nghĩa một cách lỏng lẻo là các lược đồ mật mã đối xứng với ba thuật toán: thuật toán tạo khóa, thuật toán tạo thẻ và thuật toán xác minh. Một MAC an toàn đảm bảo rằng các thẻ **không thể làm giả** đối với bất kỳ kẻ tấn công nào—tức là chúng không thể tạo thành công một thẻ trên tin nhắn để xác minh, trừ khi chúng có khóa riêng.

Bob và Alice có thể chống lại việc thao túng một thông điệp cụ thể bằng cách sử dụng MAC. Giả sử rằng họ không quan tâm đến tính bí mật. Họ chỉ muốn đảm bảo rằng thông điệp mà Alice nhận được thực sự là từ Bob và không bị thay đổi theo bất kỳ cách nào.

Quá trình này được mô tả trong *Hình 9*. Để sử dụng **MAC** (Mã xác thực tin nhắn), trước tiên họ sẽ tạo khóa riêng $K$ được chia sẻ giữa hai người. Bob tạo thẻ $T$ cho tin nhắn bằng khóa riêng $K$. Sau đó, anh ấy gửi tin nhắn cũng như thẻ tin nhắn cho Alice. Sau đó, cô ấy có thể xác minh rằng Bob thực sự đã tạo thẻ, bằng cách chạy khóa riêng, tin nhắn và thẻ thông qua thuật toán xác minh.

*Hình 9: Tổng quan về các chương trình mã hóa đối xứng*

![Figure 9: Overview of symmetric encryption schemes](assets/Figure4-9.webp "Figure 9: Overview of symmetric encryption schemes")

Do **tính không thể làm giả hiện hữu**, kẻ tấn công không thể thay đổi tin nhắn $M$ theo bất kỳ cách nào hoặc tạo tin nhắn của riêng mình với một thẻ hợp lệ. Điều này đúng ngay cả khi kẻ tấn công quan sát các thẻ của nhiều tin nhắn giữa Bob và Alice sử dụng cùng một khóa riêng. Nhiều nhất, kẻ tấn công có thể chặn Alice nhận tin nhắn $M$ (một vấn đề mà mật mã không thể giải quyết).

MAC đảm bảo rằng tin nhắn thực sự được Bob tạo ra. Tính xác thực này tự động ngụ ý tính toàn vẹn của tin nhắn—tức là, nếu Bob đã tạo ra một số tin nhắn, thì ipso facto, tin nhắn đó không bị kẻ tấn công thay đổi theo bất kỳ cách nào. Vì vậy, từ đây trở đi, bất kỳ mối quan tâm nào về xác thực đều được hiểu tự động là ngụ ý mối quan tâm về tính toàn vẹn.

Trong khi tôi đã phân biệt giữa tính xác thực và tính toàn vẹn của tin nhắn trong cuộc thảo luận của mình, thì việc sử dụng các thuật ngữ đó như từ đồng nghĩa cũng rất phổ biến. Khi đó, chúng ám chỉ ý tưởng về các tin nhắn được tạo ra bởi một người gửi cụ thể và không bị thay đổi theo bất kỳ cách nào. Theo tinh thần này, mã xác thực tin nhắn thường được gọi là **mã toàn vẹn tin nhắn**.

## Mã hóa được xác thực

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Thông thường, bạn sẽ muốn đảm bảo cả tính bảo mật và tính xác thực trong giao tiếp và do đó, các lược đồ mã hóa và lược đồ MAC thường được sử dụng cùng nhau.

**Sơ đồ mã hóa được xác thực** là sơ đồ kết hợp mã hóa với MAC theo cách cực kỳ an toàn. Cụ thể, nó phải đáp ứng các tiêu chuẩn về tính không thể làm giả hiện hữu cũng như khái niệm rất mạnh về tính bí mật, tức là khái niệm chống lại **các cuộc tấn công bằng văn bản mã hóa đã chọn**. [7]

Để một chương trình mã hóa có khả năng chống lại các cuộc tấn công vào văn bản mã hóa đã chọn, nó phải đáp ứng các tiêu chuẩn về **không thể thay đổi**: nghĩa là bất kỳ sửa đổi nào đối với văn bản mã hóa của kẻ tấn công đều phải tạo ra văn bản mã hóa không hợp lệ hoặc văn bản giải mã thành văn bản thuần túy không liên quan đến văn bản gốc. [8]

Vì một lược đồ mã hóa được xác thực đảm bảo rằng một bản mã do kẻ tấn công tạo ra luôn không hợp lệ (vì thẻ sẽ không được xác minh), nó đáp ứng các tiêu chuẩn về khả năng chống lại các cuộc tấn công bằng bản mã được chọn. Điều thú vị là bạn có thể chứng minh rằng một lược đồ mã hóa được xác thực luôn có thể được tạo ra từ sự kết hợp của một MAC không thể làm giả về mặt hiện sinh và một lược đồ mã hóa đáp ứng một khái niệm kém mạnh hơn về bảo mật, được gọi là **bảo mật tấn công bằng bản rõ được chọn**.

Chúng tôi sẽ không đi sâu vào tất cả các chi tiết về việc xây dựng các chương trình mã hóa được xác thực. Nhưng điều quan trọng là phải biết hai chi tiết về việc xây dựng chúng.

Đầu tiên, một lược đồ mã hóa được xác thực sẽ xử lý mã hóa trước rồi tạo thẻ tin nhắn trên văn bản mã hóa. Hóa ra các cách tiếp cận khác—chẳng hạn như kết hợp văn bản mã hóa với thẻ trên văn bản thuần túy hoặc trước tiên tạo thẻ rồi mã hóa cả văn bản thuần túy và thẻ—đều không an toàn. Ngoài ra, cả hai thao tác đều có khóa riêng được chọn ngẫu nhiên, nếu không thì tính bảo mật của bạn sẽ bị xâm phạm nghiêm trọng.

Nguyên tắc nói trên được áp dụng rộng rãi hơn: *bạn nên luôn sử dụng các khóa riêng biệt khi kết hợp các lược đồ mật mã cơ bản*.

Một lược đồ mã hóa được xác thực được mô tả trong *Hình 10*. Đầu tiên, Bob tạo một bản mã hóa $C$ từ tin nhắn $M$ bằng cách sử dụng một khóa được chọn ngẫu nhiên $K_C$. Sau đó, anh ta tạo một thẻ tin nhắn $T$ bằng cách chạy bản mã hóa và một khóa được chọn ngẫu nhiên khác $K_T$ thông qua thuật toán tạo thẻ. Cả bản mã hóa và thẻ tin nhắn đều được gửi đến Alice.

Alice bây giờ đầu tiên kiểm tra xem thẻ có hợp lệ hay không dựa trên văn bản mã hóa $C$ và khóa $K_T$. Nếu hợp lệ, cô ấy có thể giải mã tin nhắn bằng khóa $K_C$. Cô ấy không chỉ được đảm bảo về khái niệm bí mật rất mạnh mẽ trong giao tiếp của họ mà còn biết tin nhắn được tạo bởi Bob.

*Hình 10: Một chương trình mã hóa đã xác thực*

![Figure 10: An authenticated encryption scheme](assets/Figure4-10.webp "Figure 10: An authenticated encryption scheme")

MAC được tạo ra như thế nào? Mặc dù MAC có thể được tạo ra thông qua nhiều phương pháp, nhưng một cách phổ biến và hiệu quả để tạo ra chúng là thông qua **hàm băm mật mã**.

Chúng tôi sẽ giới thiệu chi tiết hơn về hàm băm mật mã trong *Chương 6*. Hiện tại, chỉ cần biết rằng **hàm băm** là một hàm có thể tính toán hiệu quả, lấy các đầu vào có kích thước tùy ý và tạo ra các đầu ra có độ dài cố định. Ví dụ, hàm băm phổ biến **SHA-256** (thuật toán băm an toàn 256) luôn tạo ra đầu ra 256 bit bất kể kích thước của đầu vào. Một số hàm băm, chẳng hạn như SHA-256, có các ứng dụng hữu ích trong mật mã học.

Loại thẻ phổ biến nhất được tạo ra bằng hàm băm mật mã là **mã xác thực tin nhắn dựa trên băm** (HMAC). Quá trình này được mô tả trong *Hình 11*. Một bên tạo ra hai khóa riêng biệt từ khóa riêng $K$, khóa bên trong $K_1$ và khóa bên ngoài $K_2$. Sau đó, văn bản thuần túy $M$ hoặc văn bản mã hóa $C$ được băm cùng với khóa bên trong. Sau đó, kết quả $T'$ được băm bằng khóa bên ngoài để tạo ra thẻ tin nhắn $T$.

Có một bảng các hàm băm có thể được sử dụng để tạo HMAC. Hàm băm được sử dụng phổ biến nhất là SHA-256.

*Hình 11: HMAC*

![Figure 11: HMAC](assets/Figure4-11.webp "Figure 11: HMAC")

**Lưu ý:**

[7] Các kết quả cụ thể được thảo luận trong phần này là từ Katz và Lindell, trang 131–47.

[8] Về mặt kỹ thuật, định nghĩa về các cuộc tấn công văn bản mã hóa được chọn khác với khái niệm không thể thay đổi. Nhưng bạn có thể chứng minh rằng hai khái niệm bảo mật đó là tương đương nhau.

## Phiên giao tiếp an toàn

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Giả sử hai bên đang trong một phiên giao tiếp và họ gửi nhiều tin nhắn qua lại.

Một lược đồ mã hóa được xác thực cho phép người nhận tin nhắn xác minh rằng tin nhắn đó được tạo bởi đối tác của mình trong phiên giao tiếp (miễn là khóa riêng chưa bị rò rỉ). Điều này đủ hiệu quả đối với một tin nhắn duy nhất. Tuy nhiên, thông thường, hai bên sẽ gửi tin nhắn qua lại trong một phiên giao tiếp. Và trong bối cảnh đó, một lược đồ mã hóa được xác thực đơn giản như đã mô tả trong phần trước không cung cấp được tính bảo mật.

Lý do chính là một chương trình mã hóa được xác thực không cung cấp bất kỳ đảm bảo nào rằng thông điệp thực sự cũng được gửi bởi tác nhân tạo ra nó trong một phiên giao tiếp. Hãy xem xét ba vectơ tấn công sau:

1. **Tấn công phát lại**: Kẻ tấn công gửi lại một bản mã và một thẻ mà kẻ đó đã chặn được giữa hai bên tại một thời điểm trước đó.

2. **Tấn công sắp xếp lại**: Kẻ tấn công chặn hai tin nhắn ở hai thời điểm khác nhau và gửi chúng đến người nhận theo thứ tự ngược lại.

3. **Tấn công phản xạ**: Kẻ tấn công theo dõi tin nhắn được gửi từ A đến B và cũng gửi tin nhắn đó đến A.

Mặc dù kẻ tấn công không biết về văn bản mã hóa và không thể tạo ra văn bản mã hóa giả mạo, các cuộc tấn công trên vẫn có thể gây ra thiệt hại đáng kể trong truyền thông.

Ví dụ, giả sử một thông điệp cụ thể giữa hai bên liên quan đến việc chuyển tiền tài chính. Một cuộc tấn công phát lại có thể chuyển tiền lần thứ hai. Một chương trình mã hóa xác thực vanilla không có khả năng phòng thủ chống lại các cuộc tấn công như vậy.

May mắn thay, những kiểu tấn công này có thể dễ dàng được giảm thiểu trong phiên giao tiếp bằng cách sử dụng **mã định danh** và **chỉ báo thời gian tương đối**.

Có thể thêm mã định danh vào tin nhắn văn bản thuần túy trước khi mã hóa. Điều này sẽ ngăn chặn mọi cuộc tấn công phản xạ. Ví dụ, một chỉ báo thời gian tương đối có thể là một số thứ tự trong một phiên giao tiếp cụ thể. Mỗi bên thêm một số thứ tự vào tin nhắn trước khi mã hóa, do đó người nhận biết được thứ tự các tin nhắn được gửi. Điều này loại bỏ khả năng sắp xếp lại các cuộc tấn công. Nó cũng loại bỏ các cuộc tấn công phát lại. Bất kỳ tin nhắn nào mà kẻ tấn công gửi xuống dòng sẽ có một số thứ tự cũ và người nhận sẽ biết không xử lý lại tin nhắn đó nữa.

Để minh họa cách các phiên giao tiếp an toàn hoạt động, hãy giả sử lại Alice và Bob. Họ gửi tổng cộng bốn tin nhắn qua lại. Bạn có thể thấy cách một lược đồ mã hóa được xác thực với các mã định danh và số thứ tự sẽ hoạt động như thế nào bên dưới trong *Hình 11*.

Phiên giao tiếp bắt đầu bằng việc Bob gửi một bản mã $C_{0,B}$ cho Alice với một thẻ tin nhắn $T_{0,B}$. Bản mã chứa tin nhắn, cũng như một mã định danh (BOB) và một số thứ tự (0). Thẻ $T_{0,B}$ được tạo trên toàn bộ bản mã. Trong các lần giao tiếp tiếp theo, Alice và Bob duy trì giao thức này, cập nhật các trường khi cần thiết.

*Hình 12: Phiên giao tiếp an toàn*

![Figure 12: A secure communication session](assets/Figure4-12.webp "Figure 12: A secure communication sessesion")

# RC4 và AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## Mã hóa luồng RC4

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

Trong Chương này, chúng ta sẽ thảo luận chi tiết về một lược đồ mã hóa với một mã hóa luồng nguyên thủy hiện đại, RC4 (hay "Mã hóa Rivest 4"), và một mã hóa khối hiện đại, AES. Trong khi mã hóa RC4 đã không còn được ưa chuộng như một phương pháp mã hóa, AES là tiêu chuẩn cho mã hóa đối xứng hiện đại. Hai ví dụ này sẽ cung cấp một ý tưởng tốt hơn về cách mã hóa đối xứng hoạt động bên trong.

___

Để hiểu được cách thức hoạt động của mã hóa luồng giả ngẫu nhiên hiện đại, tôi sẽ tập trung vào mã hóa luồng RC4. Đây là mã hóa luồng giả ngẫu nhiên được sử dụng trong các giao thức bảo mật điểm truy cập không dây WEP và WAP cũng như trong TLS. Vì RC4 có nhiều điểm yếu đã được chứng minh nên nó đã không còn được ưa chuộng. Trên thực tế, Lực lượng đặc nhiệm kỹ thuật Internet hiện cấm các ứng dụng máy khách và máy chủ sử dụng bộ RC4 trong mọi trường hợp của TLS. Tuy nhiên, nó hoạt động tốt như một ví dụ để minh họa cách thức hoạt động của mã hóa luồng nguyên thủy.

Để bắt đầu, trước tiên tôi sẽ chỉ cho bạn cách mã hóa tin nhắn văn bản thuần túy bằng mã hóa RC4 con. Giả sử tin nhắn văn bản thuần túy của chúng ta là “SOUP”. Mã hóa bằng mã hóa RC4 con của chúng ta, sau đó, tiến hành theo bốn bước.

### Bước 1

Đầu tiên, hãy định nghĩa một mảng **S** với $S[0] = 0$ đến $S[7] = 7$. Mảng ở đây chỉ đơn giản có nghĩa là một tập hợp các giá trị có thể thay đổi được được sắp xếp theo một chỉ mục, còn được gọi là danh sách trong một số ngôn ngữ lập trình (ví dụ: Python). Trong trường hợp này, chỉ mục chạy từ 0 đến 7 và các giá trị cũng chạy từ 0 đến 7. Vì vậy, **S** như sau:


- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Các giá trị ở đây không phải là số ASCII, mà là biểu diễn giá trị thập phân của chuỗi 1 byte. Vì vậy, giá trị 2 sẽ bằng $0000 \ 0011$. Do đó, độ dài của mảng **S** là 8 byte.

### Bước 2

Thứ hai, hãy định nghĩa một mảng khóa **K** có độ dài 8 byte bằng cách chọn một khóa từ 1 đến 8 byte (không cho phép phân số byte). Vì mỗi byte là 8 bit, bạn có thể chọn bất kỳ số nào từ 0 đến 255 cho mỗi byte của khóa.

Giả sử chúng ta chọn khóa **k** của mình là $[14, 48, 9]$, sao cho nó có độ dài là 3 byte. Sau đó, mỗi chỉ mục của mảng khóa của chúng ta được đặt theo giá trị thập phân cho phần tử cụ thể đó của khóa, theo thứ tự. Nếu bạn chạy qua toàn bộ khóa, hãy bắt đầu lại từ đầu, cho đến khi bạn đã điền đầy 8 ô của mảng khóa. Do đó, mảng khóa của chúng ta như sau:


- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Bước 3

Thứ ba, chúng ta sẽ chuyển đổi mảng **S** bằng mảng khóa **K**, trong một quy trình được gọi là **lập lịch khóa**. Quy trình này như sau trong mã giả:


- Tạo các biến **j** và **i**
- Đặt biến $j = 0$
- Với mỗi $i$ từ 0 đến 7:
    - Đặt $j = (j + S[i] + K[i]) \mod 8$
    - Hoán đổi $S[i]$ và $S[j]$

Sự biến đổi của mảng **S** được thể hiện trong *Bảng 1*.

Để bắt đầu, bạn có thể thấy trạng thái ban đầu của **S** là $[0, 1, 2, 3, 4, 5, 6, 7]$ với giá trị ban đầu là 0 cho **j**. Điều này sẽ được chuyển đổi bằng cách sử dụng mảng khóa $[14, 48, 9, 14, 48, 9, 14, 48]$.

Vòng lặp for bắt đầu với $i = 0$. Theo mã giả ở trên, giá trị mới của **j** trở thành 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Hoán đổi $S[0]$ và $S[6]$, trạng thái của **S** sau 1 vòng trở thành $[6, 1, 2, 3, 4, 5, 0, 7]$.

Ở hàng tiếp theo, $i = 1$. Đi qua vòng lặp for một lần nữa, **j** thu được giá trị là 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Hoán đổi $S[1]$ và $S[7]$ từ trạng thái hiện tại của **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, tạo ra $[6, 7, 2, 3, 4, 5, 0, 1]$ sau vòng 2.

Chúng ta tiếp tục quá trình này cho đến khi tạo ra hàng cuối cùng ở phía dưới cho mảng **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Bảng 1: Bảng lịch trình chính*

| Vòng | i | j | | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |

| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

|         |     |     |     |      |      |      |      |      |      |      |      |

| Ban đầu | | 0 | | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| 1 | 0 | 6 |     | 6 | 1 | 2 | 3 | 4 | 5 | 0 | 7 |

| 2 | 1 | 7 |     | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 3 | 2 | 2 |     | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 4 | 3 | 3 |     | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 5 | 4 | 3 |     | 6 | 7 | 2 | 0 | 3 | 5 | 4 | 1 |

| 6 | 5 | 6 |     | 6 | 4 | 2 | 0 | 3 | 7 | 5 | 1 |

| 7 | 6 | 1 |     | 6 | 4 | 2 | 0 | 3 | 7 | 5 | 2 |

| 8 | 7 | 2 |     | 6 | 4 | 1 | 0 | 3 | 7 | 5 | 2 |

### Bước 4

Bước thứ tư, chúng ta tạo ra **keystream**. Đây là chuỗi giả ngẫu nhiên có độ dài bằng với tin nhắn chúng ta muốn gửi. Chuỗi này sẽ được sử dụng để mã hóa tin nhắn gốc “SOUP”. Vì keystream cần phải dài bằng tin nhắn, chúng ta cần một keystream có 4 byte.

Luồng khóa được tạo ra bởi mã giả sau:


- Tạo các biến **j**, **i** và **t**.
- Đặt $j = 0$.
- Đối với mỗi $i$ của văn bản thuần túy, bắt đầu từ $i = 1$ và cho đến $i = 4$, mỗi byte của luồng khóa được tạo ra như sau:
    - $j = (j + S[i]) \mod 8$
    - Hoán đổi $S[i]$ và $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - Byte thứ $i^{th}$ của luồng khóa = $S[t]$

Bạn có thể theo dõi các tính toán trong *Bảng 2*.

Trạng thái ban đầu của **S** là $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Đặt $i = 1$, giá trị của **j** trở thành 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Sau đó, chúng ta hoán đổi $S[1]$ và $S[4]$ để tạo ra phép biến đổi của **S** ở hàng thứ hai, $[6, 3, 1, 0, 4, 7, 5, 2]$. Giá trị của **t** khi đó là 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Cuối cùng, byte cho luồng khóa là $S[7]$, hoặc 2.

Sau đó, chúng ta tiếp tục tạo ra các byte khác cho đến khi có được bốn byte sau: 2, 6, 3 và 7. Mỗi byte này sau đó có thể được sử dụng để mã hóa từng chữ cái của văn bản thuần túy, "SOUP".

Để bắt đầu, sử dụng bảng ASCII, chúng ta có thể thấy rằng “SOUP” được mã hóa theo giá trị thập phân của chuỗi byte cơ bản là “83 79 85 80”. Kết hợp với luồng khóa “2 6 3 7” tạo ra “85 85 88 87”, vẫn giữ nguyên sau phép toán modulo 256. Trong ASCII, văn bản mã hóa “85 85 88 87” bằng “UUXW”.

Điều gì xảy ra nếu từ cần mã hóa dài hơn mảng **S**? Trong trường hợp đó, mảng **S** chỉ tiếp tục biến đổi theo cách hiển thị ở trên cho mỗi byte **i** của văn bản thuần túy, cho đến khi chúng ta có số byte trong luồng khóa bằng với số chữ cái trong văn bản thuần túy.

*Bảng 2: Tạo luồng khóa*

| i | j | t | Dòng khóa | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |

| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

|     |     |     |           |      |      |      |      |      |      |      |      |

|     | 0 |     |           | 6 | 4 | 1 | 0 | 3 | 7 | 5 | 2 |

| 1 | 4 | 7 | 2 | 6 | 3 | 1 | 0 | 4 | 7 | 5 | 2 |

| 2 | 5 | 0 | 6 | 6 | 3 | 7 | 0 | 4 | 1 | 5 | 2 |

| 3 | 5 | 1 | 3 | 6 | 3 | 7 | 1 | 4 | 0 | 5 | 2 |

| 4 | 1 | 7 | 2 | 6 | 4 | 7 | 1 | 3 | 0 | 5 | 2 |

Ví dụ mà chúng ta vừa thảo luận chỉ là phiên bản giản lược của **mã hóa luồng RC4**. Mã hóa luồng RC4 thực tế có một mảng **S** dài 256 byte, không phải 8 byte, và một khóa có thể nằm trong khoảng từ 1 đến 256 byte, không phải trong khoảng từ 1 đến 8 byte. Mảng khóa và các luồng khóa sau đó đều được tạo ra khi xem xét độ dài 256 byte của mảng **S**. Các phép tính trở nên phức tạp hơn rất nhiều, nhưng các nguyên tắc vẫn giữ nguyên. Sử dụng cùng một khóa, [14,48,9], với mã hóa RC4 chuẩn, tin nhắn văn bản thuần túy "SOUP" được mã hóa thành 67 02 ed df ở định dạng thập lục phân.

Một mã hóa luồng trong đó luồng khóa cập nhật độc lập với thông điệp văn bản thuần túy hoặc văn bản mã hóa là **mã hóa luồng đồng bộ**. Luồng khóa chỉ phụ thuộc vào khóa. Rõ ràng, RC4 là một ví dụ về mã hóa luồng đồng bộ, vì luồng khóa không có mối quan hệ nào với văn bản thuần túy hoặc văn bản mã hóa. Tất cả các mã hóa luồng nguyên thủy của chúng tôi được đề cập trong chương trước, bao gồm mã hóa dịch chuyển, mã hóa Vigenère và bảng mã một lần, cũng thuộc loại đồng bộ.

Ngược lại, **mã hóa luồng không đồng bộ** có luồng khóa được tạo ra bởi cả khóa và các phần tử trước đó của văn bản mã hóa. Kiểu mã hóa này cũng được gọi là **mã hóa tự đồng bộ**.

Điều quan trọng là, keystream được tạo ra bằng RC4 phải được coi là một pad một lần và bạn không thể tạo keystream theo cùng một cách chính xác vào lần tiếp theo. Thay vì thay đổi key mỗi lần, giải pháp thực tế là kết hợp key với **nonce** để tạo ra bytestream.

## AES với khóa 128-bit

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Như đã đề cập trong chương trước, Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) đã tổ chức một cuộc thi từ năm 1997 đến năm 2000 để xác định một tiêu chuẩn mã hóa đối xứng mới. **Mật mã Rijndael** đã trở thành bài dự thi chiến thắng. Tên này là một cách chơi chữ dựa trên tên của những người sáng tạo ra nó là Vincent Rijmen và Joan Daemen người Bỉ.

Mã Rijndael là **mã khối**, nghĩa là có một thuật toán cốt lõi, có thể được sử dụng với các thông số kỹ thuật khác nhau cho độ dài khóa và kích thước khối. Sau đó, bạn có thể sử dụng nó với các chế độ hoạt động khác nhau để xây dựng các lược đồ mã hóa.

Ủy ban cho cuộc thi NIST đã thông qua một phiên bản thu hẹp của mật mã Rijndael—cụ thể là phiên bản yêu cầu kích thước khối 128 bit và độ dài khóa là 128 bit, 192 bit hoặc 256 bit—như một phần của **Tiêu chuẩn mã hóa nâng cao (AES)**. Phiên bản thu hẹp này của mật mã Rijndael cũng có thể được sử dụng trong nhiều chế độ hoạt động. Đặc điểm kỹ thuật cho tiêu chuẩn này được gọi là **Tiêu chuẩn mã hóa nâng cao (AES)**.

Để chỉ ra cách thức hoạt động của mã Rijndael, cốt lõi của AES, tôi sẽ minh họa quy trình mã hóa bằng khóa 128 bit. Kích thước khóa có tác động đến số vòng được giữ cho mỗi khối mã hóa. Đối với khóa 128 bit, cần 10 vòng. Với khóa 192 bit và 256 bit, sẽ lần lượt là 12 và 14 vòng.

Ngoài ra, tôi sẽ giả định rằng AES được sử dụng trong **ECB-mode**. Điều này làm cho việc trình bày dễ dàng hơn một chút và không quan trọng đối với thuật toán Rijndael. Chắc chắn, chế độ ECB không an toàn trong thực tế vì nó dẫn đến mã hóa xác định. Chế độ an toàn được sử dụng phổ biến nhất với AES là **CBC** (Cipher Block Chaining).

Hãy gọi khóa là $K_0$. Khi đó, cấu trúc với các tham số trên trông giống như trong *Hình 1*, trong đó $M_i$ biểu thị một phần của thông điệp văn bản thuần túy gồm 128 bit và $C_i$ biểu thị một phần của văn bản mã hóa gồm 128 bit. Phần đệm được thêm vào văn bản thuần túy cho khối cuối cùng, nếu văn bản thuần túy không thể chia đều cho kích thước khối.

*Hình 1: AES-ECB với khóa 128-bit*

![Figure 1: AES-ECB with a 128-bit key](assets/Figure5-1.webp "Figure 1: AES-ECB with a 128-bit key")

Mỗi khối văn bản 128 bit trải qua mười vòng trong sơ đồ mã hóa Rijndael. Điều này đòi hỏi một khóa vòng riêng cho mỗi vòng ($K_1$ đến $K_{10}$). Chúng được tạo ra cho mỗi vòng từ khóa 128 bit gốc $K_0$ bằng cách sử dụng **thuật toán mở rộng khóa**. Do đó, đối với mỗi khối văn bản được mã hóa, chúng ta sẽ sử dụng khóa gốc $K_0$ cũng như mười khóa vòng riêng. Lưu ý rằng 11 khóa giống nhau này được sử dụng cho mỗi khối văn bản thuần túy 128 bit cần mã hóa.

Thuật toán mở rộng khóa dài và phức tạp. Việc thực hiện thuật toán này không có nhiều lợi ích về mặt giáo dục. Bạn có thể tự mình xem xét thuật toán mở rộng khóa, nếu muốn. Sau khi tạo ra các khóa vòng, mã hóa Rijndael sẽ xử lý khối 128 bit đầu tiên của văn bản thuần túy, $M_1$, như được thấy trong *Hình 2*. Bây giờ chúng ta sẽ thực hiện các bước này.

*Hình 2: Thao tác $M_1$ bằng mã hóa Rijndael:*

**Vòng 0:**


- XOR $M_1$ và $K_0$ để tạo ra $S_0$

---
**Làm tròn n cho n = {1,...,9}:**


- XOR $S_{n-1}$ và $K_n$
- Thay thế byte
- Chuyển hàng
- Trộn các cột
- XOR $S$ và $K_n$ để tạo ra $S_n$

---
**Vòng 10:**


- XOR $S_9$ và $K_{10}$
- Thay thế byte
- Chuyển hàng
- XOR $S$ và $K_{10}$ để tạo ra $S_{10}$
- $S_{10}$ = $C_1$

### Vòng 0

Vòng 0 của mã Rijndael rất đơn giản. Một mảng $S_0$ được tạo ra bằng phép toán XOR giữa văn bản thuần túy 128 bit và khóa riêng. Nghĩa là,


- $S_0 = M_1 \oplus K_0$

### Vòng 1

Ở vòng 1, mảng $S_0$ đầu tiên được kết hợp với khóa vòng $K_1$ bằng cách sử dụng phép toán XOR. Điều này tạo ra trạng thái mới của $S$.

Thứ hai, hoạt động **thay thế byte** được thực hiện trên trạng thái hiện tại của $S$. Hoạt động này hoạt động bằng cách lấy từng byte của mảng $S$ 16 byte và thay thế bằng một byte từ một mảng có tên là **Rijndael’s S-box**. Mỗi byte có một phép biến đổi duy nhất và trạng thái mới của $S$ được tạo ra như một kết quả. Rijndael’s S-box được hiển thị trong *Hình 3*.

*Hình 3: Hộp S của Rijndael*

|     | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 0A | 0B | 0C | 0D | 0E | 0F |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 00 | 63 | 7C | 77 | 7B | F2 | 6B | 6F | C5 | 30 | 01 | 67 | 2B | FE | D7 | AB | 76 |

| 10 | CA | 82 | C9 | 7D | FA | 59 | 47 | F0 | QUẢNG CÁO | D4 | A2 | AF | 9C | A4 | 72 | C0 |

| 20 | B7 | FD | 93 | 26 | 36 | 3F | F7 | CC | 34 | A5 | E5 | F1 | 71 | D8 | 31 | 15 |

| 30 | 04 | C7 | 23 | C3 | 18 | 96 | 05 | 9A | 07 | 12 | 80 | E2 | EB | 27 | B2 | 75 |

| 40 | 09 | 83 | 2C | 1A | 1B | 6E | 5A | A0 | 52 | 3B | D6 | B3 | 29 | E3 | 2F | 84 |

| 50 | 53 | D1 | 00 | ED | 20 | FC | B1 | 5B | 6A | CB | BE | 39 | 4A | 4C | 58 | CF |

| 60 | D0 | EF | AA | FB | 43 | 4D | 33 | 85 | 45 | F9 | 02 | 7F | 50 | 3C | 9F | A8 |

| 70 | 51 | A3 | 40 | 8F | 92 | 9D | 38 | F5 | BC | B6 | DA | 21 | 10 | FF | F3 | D2 |

| 80 | CD | 0C | 13 | EC | 5F | 97 | 44 | 17 | C4 | A7 | 7E | 3D | 64 | 5D | 19 | 73 |

| 90 | 60 | 81 | 4F | DC | 22 | 2A | 90 | 88 | 46 | EE | B8 | 14 | DE | 5E | 0B | DB |

| A0 | E0 | 32 | 3A | 0A | 49 | 06 | 24 | 5C | C2 | D3 | AC | 62 | 91 | 95 | E4 | 79 |

| B0 | E7 | C8 | 37 | 6D | 8D | D5 | 4E | A9 | 6C | 56 | F4 | EA | 65 | 7A | AE | 08 |

| C0 | BA | 78 | 25 | 2E | 1C | A6 | B4 | C6 | E8 | ĐC | 74 | 1F | 4B | BD | 8B | 8A |

| D0 | 70 | 3E | B5 | 66 | 48 | 03 | F6 | 0E | 61 | 35 | 57 | B9 | 86 | C1 | 1D | 9E |

| E0 | E1 | F8 | 98 | 11 | 69 | D9 | 8E | 94 | 9B | 1E | 87 | E9 | CE | 55 | 28 | DF |

| F0 | 8C | A1 | 89 | 0D | bạn trai | E6 | 42 | 68 | 41 | 99 | 2D | 0F | B0 | 54 | BB | 16 |

Hộp S này là một nơi mà đại số trừu tượng phát huy tác dụng trong mật mã Rijndael, cụ thể là **trường Galois**.

Để bắt đầu, bạn định nghĩa mỗi phần tử byte có thể có từ 00 đến FF là một vectơ 8 bit. Mỗi vectơ như vậy là một phần tử của **Trường Galois GF(2^8)** trong đó đa thức bất khả quy cho phép toán modulo là $x^8 + x^4 + x^3 + x + 1$. Trường Galois với các thông số kỹ thuật này cũng được gọi là **Trường hữu hạn Rijndael**.

Tiếp theo, đối với mỗi phần tử có thể có trong trường, chúng ta tạo ra cái gọi là **Nyberg S-Box**. Trong hộp này, mỗi byte được ánh xạ vào **nghịch đảo nhân** của nó (tức là sao cho tích của chúng bằng 1). Sau đó, chúng ta ánh xạ các giá trị đó từ Nyberg S-box sang Rijndael S-Box bằng cách sử dụng **phép biến đổi affine**.

Hoạt động thứ ba trên mảng **S** là hoạt động **shift rows**. Nó lấy trạng thái của **S** và liệt kê tất cả mười sáu byte trong một ma trận. Việc điền vào ma trận bắt đầu từ trên cùng bên trái và thực hiện theo cách của nó bằng cách đi từ trên xuống dưới và sau đó, mỗi lần một cột được điền, dịch chuyển một cột sang phải và lên trên cùng.

Sau khi ma trận của **S** được xây dựng, bốn hàng được dịch chuyển. Hàng đầu tiên giữ nguyên. Hàng thứ hai di chuyển một sang bên trái. Hàng thứ ba di chuyển hai sang bên trái. Hàng thứ tư di chuyển ba sang bên trái. Một ví dụ về quy trình được cung cấp trong *Hình 4*. Trạng thái ban đầu của **S** được hiển thị ở trên cùng và trạng thái kết quả sau thao tác dịch chuyển hàng được hiển thị bên dưới.

*Hình 4: Thao tác chuyển hàng*

| F1 | A0 | B1 | 23 |

|------|------|------|------|

| 59 | 09 | 82 |

| 97 | 01 | B0 | CC |

| D4 | 72 | 04 | 21 |

| F1 | A0 | B1 | 23 |

|------|------|------|------|

| 09 | 82 | 59 |

| B0 | CC | 97 | 01 |

| 21 | Ngày 4 | 72 | 04 |

Ở bước thứ tư, **trường Galois** lại xuất hiện. Để bắt đầu, mỗi cột của ma trận **S** được nhân với cột của ma trận 4 x 4 được thấy trong *Hình 5*. Nhưng thay vì là phép nhân ma trận thông thường, thì đó là phép nhân vectơ **modulo một đa thức bất khả quy**, $x^8 + x^4 + x^3 + x + 1$. Các hệ số vectơ kết quả biểu diễn các bit riêng lẻ của một byte.

*Hình 5: Ma trận cột trộn*

| 02 | 03 | 01 | 01 |

|------|------|------|------|

| 01 | 02 | 03 | 01 |

| 01 | 01 | 02 | 03 |

| 03 | 01 | 01 | 02 |

Phép nhân cột đầu tiên của ma trận **S** với ma trận 4 x 4 ở trên cho kết quả như *Hình 6*.

*Hình 6: Phép nhân cột đầu tiên:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Bước tiếp theo, tất cả các số hạng trong ma trận sẽ phải được chuyển thành đa thức. Ví dụ, F1 biểu diễn 1 byte và sẽ trở thành $x^7 + x^6 + x^5 + x^4 + 1$, và 03 biểu diễn 1 byte và sẽ trở thành $x + 1$.

Tất cả các phép nhân sau đó được thực hiện **modulo** $x^8 + x^4 + x^3 + x + 1$. Điều này dẫn đến việc cộng bốn đa thức trong mỗi bốn ô của cột. Sau khi thực hiện các phép cộng đó **modulo 2**, bạn sẽ có được bốn đa thức. Mỗi đa thức này biểu diễn một chuỗi 8 bit hoặc 1 byte của **S**. Chúng ta sẽ không thực hiện tất cả các phép tính này ở đây trên ma trận trong *Hình 6* vì chúng rất rộng.

Sau khi cột đầu tiên được xử lý, ba cột còn lại của ma trận **S** được xử lý theo cùng cách. Cuối cùng, điều này sẽ tạo ra một ma trận có mười sáu byte có thể được chuyển đổi thành một mảng.

Bước cuối cùng, mảng **S** được kết hợp với khóa vòng một lần nữa trong phép toán **XOR**. Điều này tạo ra trạng thái $S_1$. Nghĩa là,


- $S_1 = S \oplus K_0$

### Vòng 2 đến vòng 10

Vòng 2 đến vòng 9 chỉ là sự lặp lại của vòng 1, *mutatis mutandis*. Vòng cuối cùng trông rất giống với các vòng trước, ngoại trừ bước **mix columns** bị loại bỏ. Nghĩa là, vòng 10 được thực hiện như sau:


- $S_9 \oplus K_{10}$
- Thay thế byte
- Chuyển hàng
- $S_{10} = S \oplus K_{10}$

Trạng thái $S_{10}$ hiện được đặt thành $C_1$, 128 bit đầu tiên của văn bản mã hóa. Tiến hành qua các khối văn bản thuần túy 128 bit còn lại sẽ tạo ra văn bản mã hóa đầy đủ **C**.

### Các hoạt động của mật mã Rijndael

Lý do đằng sau những phép toán khác nhau được thấy trong mật mã Rijndael là gì?

Không đi sâu vào chi tiết, các lược đồ mã hóa được đánh giá dựa trên mức độ chúng tạo ra sự nhầm lẫn và khuếch tán. Nếu lược đồ mã hóa có mức độ **nhầm lẫn** cao, điều đó có nghĩa là bản mã trông khác biệt đáng kể so với bản rõ. Nếu lược đồ mã hóa có mức độ **khuếch tán** cao, điều đó có nghĩa là bất kỳ thay đổi nhỏ nào đối với bản rõ đều tạo ra bản mã khác biệt đáng kể.

Lý do cho các hoạt động đằng sau mã Rijndael là chúng tạo ra cả mức độ nhầm lẫn và khuếch tán cao. Sự nhầm lẫn được tạo ra bởi hoạt động thay thế Byte, trong khi sự khuếch tán được tạo ra bởi các hoạt động dịch chuyển hàng và trộn cột.

# Mật mã bất đối xứng

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Vấn đề phân phối và quản lý chính

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Giống như mật mã đối xứng, các lược đồ bất đối xứng có thể được sử dụng để đảm bảo cả tính bí mật và xác thực. Tuy nhiên, ngược lại, các lược đồ này sử dụng hai khóa thay vì một: khóa riêng và khóa công khai.

Chúng tôi bắt đầu cuộc điều tra của mình bằng việc khám phá ra mật mã bất đối xứng, đặc biệt là các vấn đề thúc đẩy nó. Tiếp theo, chúng tôi thảo luận về cách các lược đồ bất đối xứng để mã hóa và xác thực hoạt động ở cấp độ cao. Sau đó, chúng tôi giới thiệu các hàm băm, là chìa khóa để hiểu các lược đồ xác thực bất đối xứng và cũng có liên quan trong các bối cảnh mật mã khác, chẳng hạn như đối với các mã xác thực tin nhắn dựa trên băm mà chúng tôi đã thảo luận trong Chương 4.

___

Giả sử Bob muốn mua một chiếc áo mưa mới từ Jim’s Sporting Goods, một nhà bán lẻ đồ thể thao trực tuyến với hàng triệu khách hàng ở Bắc Mỹ. Đây sẽ là lần đầu tiên anh ấy mua hàng từ họ và anh ấy muốn sử dụng thẻ tín dụng của mình. Vì vậy, trước tiên Bob sẽ cần tạo một tài khoản với Jim’s Sporting Goods, yêu cầu phải gửi thông tin cá nhân như địa chỉ và thông tin thẻ tín dụng của anh ấy. Sau đó, anh ấy có thể thực hiện các bước cần thiết để mua áo mưa.

Bob and Jim’s Sporting Goods sẽ muốn đảm bảo rằng thông tin liên lạc của họ được bảo mật trong suốt quá trình này, vì Internet là một hệ thống thông tin liên lạc mở. Ví dụ, họ sẽ muốn đảm bảo rằng không có kẻ tấn công tiềm năng nào có thể xác định được thông tin chi tiết về thẻ tín dụng và địa chỉ của Bob, và không có kẻ tấn công tiềm năng nào có thể lặp lại các giao dịch mua của anh ta hoặc tạo ra các giao dịch giả mạo thay mặt anh ta.

Một chương trình mã hóa xác thực nâng cao như đã thảo luận trong chương trước chắc chắn có thể bảo mật thông tin liên lạc giữa Bob và Jim’s Sporting Goods. Nhưng rõ ràng có những trở ngại thực tế khi triển khai một chương trình như vậy.

Để minh họa cho những trở ngại thực tế này, hãy giả sử chúng ta sống trong một thế giới mà chỉ có các công cụ mật mã đối xứng tồn tại. Vậy thì Jim’s Sporting Goods và Bob có thể làm gì để đảm bảo giao tiếp an toàn?

Trong những trường hợp đó, họ sẽ phải đối mặt với chi phí đáng kể để giao tiếp an toàn. Vì Internet là một hệ thống giao tiếp mở, họ không thể chỉ trao đổi một bộ chìa khóa qua đó. Do đó, Bob và một đại diện của Jim’s Sporting Goods sẽ cần phải trao đổi chìa khóa trực tiếp.

Một khả năng là Jim’s Sporting Goods tạo ra các địa điểm trao đổi chìa khóa đặc biệt, nơi Bob và những khách hàng mới khác có thể lấy một bộ chìa khóa để giao tiếp an toàn. Điều này rõ ràng sẽ tốn kém chi phí tổ chức đáng kể và làm giảm đáng kể hiệu quả mà khách hàng mới có thể mua hàng.

Ngoài ra, Jim’s Sporting Goods có thể gửi cho Bob một cặp chìa khóa thông qua một đơn vị chuyển phát nhanh đáng tin cậy. Điều này có lẽ hiệu quả hơn so với việc sắp xếp các địa điểm trao đổi chìa khóa. Nhưng điều này vẫn tốn kém đáng kể, đặc biệt là nếu nhiều khách hàng chỉ mua một hoặc một vài lần.

Tiếp theo, một lược đồ đối xứng cho mã hóa được xác thực cũng buộc Jim’s Sporting Goods phải lưu trữ các bộ khóa riêng biệt cho tất cả khách hàng của họ. Đây sẽ là một thách thức thực tế đáng kể đối với hàng nghìn khách hàng, chứ đừng nói đến hàng triệu khách hàng.

Để hiểu được điểm sau này, hãy giả sử Jim’s Sporting Goods cung cấp cho mỗi khách hàng cùng một cặp khóa. Điều này sẽ cho phép mỗi khách hàng—hoặc bất kỳ ai khác có thể có được cặp khóa này—đọc và thậm chí thao túng tất cả các thông tin liên lạc giữa Jim’s Sporting Goods và khách hàng của họ. Khi đó, bạn cũng có thể không sử dụng mật mã trong thông tin liên lạc của mình.

Ngay cả việc lặp lại một bộ khóa chỉ cho một số khách hàng cũng là một hành vi bảo mật tồi tệ. Bất kỳ kẻ tấn công tiềm năng nào cũng có thể cố gắng khai thác tính năng đó của chương trình (hãy nhớ rằng kẻ tấn công được cho là biết mọi thứ về một chương trình trừ khóa, theo nguyên tắc của Kerckhoffs.)

Vì vậy, Jim’s Sporting Goods sẽ phải lưu trữ một cặp chìa khóa cho mỗi khách hàng, bất kể những cặp chìa khóa này được phân phối như thế nào. Điều này rõ ràng đặt ra một số vấn đề thực tế.


- Cửa hàng đồ thể thao Jim sẽ phải lưu trữ hàng triệu cặp chìa khóa, mỗi khách hàng một bộ.
- Những chìa khóa này phải được bảo mật đúng cách vì chúng sẽ là mục tiêu chắc chắn của tin tặc. Bất kỳ vi phạm bảo mật nào cũng sẽ đòi hỏi phải trao đổi chìa khóa tốn kém nhiều lần, tại các địa điểm trao đổi chìa khóa đặc biệt hoặc qua dịch vụ chuyển phát nhanh.
- Bất kỳ khách hàng nào của Jim’s Sporting Goods cũng phải cất giữ an toàn một cặp chìa khóa tại nhà. Sẽ xảy ra tình trạng mất mát và trộm cắp, đòi hỏi phải trao đổi chìa khóa nhiều lần. Khách hàng cũng phải trải qua quy trình này đối với bất kỳ cửa hàng trực tuyến nào khác hoặc các loại thực thể khác mà họ muốn giao tiếp và giao dịch qua Internet.

Hai thách thức chính vừa được mô tả là những mối quan tâm rất cơ bản cho đến cuối những năm 1970. Chúng được gọi lần lượt là **vấn đề phân phối khóa** và **vấn đề quản lý khóa**.

Tất nhiên, những vấn đề này luôn tồn tại và thường gây đau đầu trong quá khứ. Ví dụ, lực lượng quân sự sẽ phải liên tục phân phối sách có chìa khóa để liên lạc an toàn cho nhân viên trên chiến trường với rủi ro và chi phí lớn. Nhưng những vấn đề này trở nên tồi tệ hơn khi thế giới ngày càng chuyển sang giao tiếp kỹ thuật số đường dài, đặc biệt là đối với các tổ chức phi chính phủ.

Nếu những vấn đề này không được giải quyết vào những năm 1970, thì việc mua sắm hiệu quả và an toàn tại Jim’s Sporting Goods có lẽ sẽ không tồn tại. Trên thực tế, hầu hết thế giới hiện đại của chúng ta với dịch vụ email, ngân hàng trực tuyến và mua sắm thực tế và an toàn có lẽ chỉ là một giấc mơ xa vời. Bất cứ thứ gì giống với Bitcoin đều không thể tồn tại.

Vậy, điều gì đã xảy ra vào những năm 1970? Làm sao chúng ta có thể mua hàng trực tuyến ngay lập tức và duyệt World Wide Web một cách an toàn? Làm sao chúng ta có thể gửi Bitcoin ngay lập tức trên toàn thế giới từ điện thoại thông minh của mình?

## Hướng đi mới trong mật mã học

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Đến những năm 1970, các vấn đề về phân phối khóa và quản lý khóa đã thu hút sự chú ý của một nhóm các nhà mật mã học thuật người Mỹ: Whitfield Diffie, Martin Hellman và Ralph Merkle. Trước sự hoài nghi nghiêm trọng từ phần lớn các đồng nghiệp, họ đã mạo hiểm đưa ra giải pháp cho vấn đề này.

Ít nhất một động lực chính cho dự án của họ là viễn kiến rằng truyền thông máy tính mở sẽ ảnh hưởng sâu sắc đến thế giới của chúng ta. Như Diffie và Helmann lưu ý vào năm 1976,

> Sự phát triển của các mạng lưới truyền thông điều khiển bằng máy tính hứa hẹn sự tiếp xúc dễ dàng và không tốn kém giữa những người hoặc máy tính ở hai đầu đối diện của thế giới, thay thế hầu hết thư từ và nhiều chuyến đi bằng viễn thông. Đối với nhiều ứng dụng, những liên lạc này phải được bảo mật chống lại cả việc nghe lén và việc đưa vào các thông điệp bất hợp pháp. Tuy nhiên, hiện tại, giải pháp cho các vấn đề bảo mật vẫn còn chậm so với các lĩnh vực khác của công nghệ truyền thông. *Mật mã học đương đại không thể đáp ứng được các yêu cầu, vì việc sử dụng nó sẽ gây ra những bất tiện nghiêm trọng cho người dùng hệ thống, đến mức loại bỏ nhiều lợi ích của xử lý từ xa.* [1]
Sự kiên trì của Diffie, Hellman và Merkle đã được đền đáp. Ấn phẩm đầu tiên về kết quả của họ là một bài báo của Diffie và Helmann năm 1976 có tựa đề “New Directions in Cryptography.” Trong đó, họ trình bày hai cách ban đầu để giải quyết vấn đề phân phối khóa và quản lý khóa.

Giải pháp đầu tiên mà họ đưa ra là một *giao thức trao đổi khóa* từ xa, tức là một tập hợp các quy tắc để trao đổi một hoặc nhiều khóa đối xứng qua một kênh truyền thông không an toàn. Giao thức này hiện được gọi là *trao đổi khóa Diffie-Helmann* hoặc *trao đổi khóa Diffie-Helmann-Merkle*. [2]

Với trao đổi khóa Diffie-Helmann, hai bên đầu tiên trao đổi một số thông tin công khai trên một kênh không an toàn như Internet. Trên cơ sở thông tin đó, sau đó, họ độc lập tạo một khóa đối xứng (hoặc một cặp khóa đối xứng) để giao tiếp an toàn. Trong khi cả hai bên tạo khóa của mình một cách độc lập, thông tin họ chia sẻ công khai đảm bảo rằng quá trình tạo khóa này mang lại cùng một kết quả cho cả hai bên.

Điều quan trọng là trong khi mọi người đều có thể theo dõi thông tin được các bên trao đổi công khai qua kênh không an toàn thì chỉ có hai bên tham gia trao đổi thông tin mới có thể tạo khóa đối xứng từ thông tin đó.

Tất nhiên, điều này nghe có vẻ hoàn toàn trái ngược với trực giác. Làm sao hai bên có thể trao đổi một số thông tin công khai mà chỉ cho phép họ tạo khóa đối xứng từ thông tin đó? Tại sao bất kỳ ai khác quan sát việc trao đổi thông tin lại không thể tạo cùng một khóa?

Tất nhiên là nó dựa trên một số phép toán đẹp. Trao đổi khóa Diffie-Helmann hoạt động thông qua một hàm một chiều với một cửa sập. Chúng ta hãy thảo luận về ý nghĩa của hai thuật ngữ này lần lượt.

Giả sử bạn được cung cấp một hàm số $f(x)$ và kết quả là $f(a) = y$, trong đó $a$ là một giá trị cụ thể cho $x$. Chúng ta nói rằng $f(x)$ là **hàm một chiều** nếu dễ dàng tính được giá trị $y$ khi cho $a$ và $f(x)$, nhưng không khả thi về mặt tính toán để tính được giá trị $a$ khi cho $y$ và $f(x)$. Tên gọi **hàm một chiều**, tất nhiên, bắt nguồn từ thực tế là một hàm như vậy chỉ thực tế để tính theo một hướng.

Một số hàm một chiều có cái được gọi là **cửa sập**. Mặc dù thực tế là không thể tính toán $a$ chỉ dựa trên $y$ và $f(x)$, nhưng có một thông tin nhất định $Z$ khiến việc tính toán $a$ từ $y$ trở nên khả thi về mặt tính toán. Thông tin $Z$ này được gọi là **cửa sập**. Các hàm một chiều có cửa sập được gọi là **hàm cửa sập**.

Chúng ta sẽ không đi sâu vào chi tiết về trao đổi khóa Diffie-Helmann ở đây. Nhưng về cơ bản, mỗi bên tham gia tạo ra một số thông tin, trong đó một phần được chia sẻ công khai và một phần vẫn giữ bí mật. Sau đó, mỗi bên lấy thông tin bí mật của mình và thông tin công khai được bên kia chia sẻ để tạo khóa riêng. Và thật kỳ diệu, cả hai bên sẽ có cùng một khóa riêng.

Bất kỳ bên nào chỉ quan sát thông tin được chia sẻ công khai giữa hai bên trong trao đổi khóa Diffie Helmann đều không thể sao chép các phép tính này. Họ sẽ cần thông tin riêng tư từ một trong hai bên để thực hiện việc đó.

Mặc dù phiên bản cơ bản của trao đổi khóa Diffie-Helmann được trình bày trong bài báo năm 1976 không thực sự an toàn, nhưng các phiên bản tinh vi của giao thức cơ bản chắc chắn vẫn đang được sử dụng cho đến ngày nay. Quan trọng nhất là mọi giao thức trao đổi khóa trong phiên bản mới nhất của giao thức bảo mật lớp truyền tải (phiên bản 1.3) về cơ bản là phiên bản được làm giàu của giao thức do Diffie và Hellman trình bày vào năm 1976. Giao thức bảo mật lớp truyền tải là giao thức chủ yếu để trao đổi thông tin được định dạng an toàn theo giao thức truyền siêu văn bản (http), tiêu chuẩn để trao đổi nội dung Web.

Điều quan trọng là trao đổi khóa Diffie-Helmann không phải là một lược đồ bất đối xứng. Nói một cách chính xác, nó có thể thuộc về lĩnh vực mật mã khóa đối xứng. Nhưng vì cả trao đổi khóa Diffie-Helmann và mật mã bất đối xứng đều dựa trên các hàm lý thuyết số một chiều với các cửa sập, nên chúng thường được thảo luận cùng nhau.

Cách thứ hai mà Diffie và Helmann đưa ra để giải quyết vấn đề phân phối và quản lý khóa trong bài báo năm 1976 của họ, tất nhiên là thông qua mật mã bất đối xứng.

Ngược lại với cách trình bày về trao đổi khóa Diffie-Hellman, họ chỉ cung cấp các đường nét chung về cách các lược đồ mật mã bất đối xứng có thể được xây dựng một cách hợp lý. Họ không cung cấp bất kỳ hàm một chiều nào có thể đáp ứng cụ thể các điều kiện cần thiết cho tính bảo mật hợp lý trong các lược đồ như vậy.

Tuy nhiên, một triển khai thực tế của một lược đồ bất đối xứng đã được tìm thấy một năm sau đó bởi ba nhà mật mã học và toán học hàn lâm khác nhau: Ronald Rivest, Adi Shamir và Leonard Adleman. [3] Hệ thống mật mã mà họ giới thiệu được gọi là **hệ thống mật mã RSA** (theo họ của họ).

Các hàm cửa bẫy được sử dụng trong mật mã bất đối xứng (và trao đổi khóa Diffie Helmann) đều liên quan đến hai **vấn đề khó tính toán** chính: phân tích thừa số nguyên tố và tính toán logarit rời rạc.

**Phân tích thừa số nguyên tố** yêu cầu, như tên gọi của nó, phân tích một số nguyên thành các thừa số nguyên tố của nó. Bài toán RSA cho đến nay là ví dụ nổi tiếng nhất về hệ thống mật mã liên quan đến phân tích thừa số nguyên tố.

**Bài toán logarit rời rạc** là bài toán xảy ra trong các nhóm tuần hoàn. Với một bộ tạo trong một nhóm tuần hoàn cụ thể, bài toán này yêu cầu tính toán số mũ duy nhất cần thiết để tạo ra một phần tử khác trong nhóm từ bộ tạo.

Các lược đồ dựa trên logarit rời rạc dựa trên hai loại chính của nhóm tuần hoàn: nhóm nhân số nguyên và nhóm bao gồm các điểm trên đường cong elliptic. Trao đổi khóa Diffie Helmann ban đầu như được trình bày trong “New Directions in Cryptography” hoạt động với nhóm nhân số nguyên tuần hoàn. Thuật toán chữ ký số của Bitcoin và lược đồ chữ ký Schnorr mới được giới thiệu (2021) đều dựa trên bài toán logarit rời rạc cho một nhóm tuần hoàn đường cong elliptic cụ thể.

Tiếp theo, chúng ta sẽ chuyển sang tổng quan cấp cao về tính bảo mật và xác thực trong bối cảnh bất đối xứng. Tuy nhiên, trước khi thực hiện, chúng ta cần ghi chú lịch sử ngắn gọn.

Bây giờ có vẻ hợp lý khi một nhóm các nhà mật mã và toán học người Anh làm việc cho Trụ sở Truyền thông Chính phủ (GCHQ) đã độc lập thực hiện các khám phá được đề cập ở trên một vài năm trước đó. Nhóm này bao gồm James Ellis, Clifford Cocks và Malcolm Williamson.

Theo lời kể của họ và GCHQ, James Ellis là người đầu tiên đưa ra khái niệm mật mã khóa công khai vào năm 1969. Người ta cho rằng Clifford Cocks sau đó đã phát hiện ra hệ thống mật mã RSA vào năm 1973, và Malcolm Williamson đã phát hiện ra khái niệm trao đổi khóa Diffie Helmann vào năm 1974. [4] Tuy nhiên, những khám phá của họ được cho là không được tiết lộ cho đến năm 1997, do tính chất bí mật của công việc được thực hiện tại GCHQ.

**Lưu ý:**

[1] Whitfield Diffie và Martin Hellman, “Những hướng đi mới trong mật mã học,” _IEEE Transactions on Information Theory_ IT-22 (1976), trang 644–654, tại trang 644.

[2] Ralph Merkle cũng thảo luận về một giao thức trao đổi khóa trong “Truyền thông an toàn qua các kênh không an toàn”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Mặc dù Merkle thực sự đã nộp bài báo này trước bài báo của Diffie và Hellman, nhưng nó đã được xuất bản sau. Giải pháp của Merkle không an toàn theo cấp số nhân, không giống như giải pháp của Diffie-Hellman.

[3] Ron Rivest, Adi Shamir và Leonard Adleman, “Một phương pháp để lấy chữ ký số và hệ thống mật mã khóa công khai”, _Communications of the Association for Computing Machinery_, 21 (1978), tr. 120–26.

[4] Một lịch sử tốt về những khám phá này được cung cấp bởi Simon Singh, _The Code Book_, Fourth Estate (London, 1999), Chương 6.

## Mã hóa và xác thực không đối xứng

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Tổng quan về **mã hóa bất đối xứng** với sự trợ giúp của Bob và Alice được cung cấp trong *Hình 1*.

Đầu tiên, Alice tạo một cặp khóa, bao gồm một khóa công khai ($K_P$) và một khóa riêng ($K_S$), trong đó “P” trong $K_P$ là viết tắt của “public” và “S” trong $K_S$ là viết tắt của “secret”. Sau đó, cô ấy phân phối khóa công khai này một cách tự do cho những người khác. Chúng ta sẽ quay lại chi tiết về quá trình phân phối này sau một chút. Nhưng bây giờ, hãy giả sử rằng bất kỳ ai, bao gồm cả Bob, đều có thể lấy được khóa công khai $K_P$ của Alice một cách an toàn.

Vào một thời điểm nào đó sau này, Bob muốn viết một thông điệp $M$ cho Alice. Vì nó bao gồm thông tin nhạy cảm, anh ấy muốn giữ bí mật nội dung cho mọi người trừ Alice. Vì vậy, trước tiên Bob mã hóa thông điệp $M$ của mình bằng $K_P$. Sau đó, anh ấy gửi bản mã kết quả $C$ cho Alice, người giải mã $C$ bằng $K_S$ để tạo ra thông điệp gốc $M$.

*Hình 1: Mã hóa không đối xứng*

![Figure 1: Asymmetric encryption](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")

Bất kỳ kẻ thù nào nghe lén cuộc giao tiếp của Bob và Alice đều có thể quan sát $C$. Cô ấy cũng biết $K_P$ và thuật toán mã hóa $E(\cdot)$. Tuy nhiên, điều quan trọng là thông tin này không cho phép kẻ tấn công giải mã khả thi văn bản mã hóa $C$. Giải mã cụ thể yêu cầu $K_S$, mà kẻ tấn công không sở hữu.

Các lược đồ mã hóa đối xứng thường cần phải an toàn trước kẻ tấn công có thể mã hóa hợp lệ các thông điệp văn bản thuần túy (được gọi là bảo mật tấn công văn bản mã hóa được chọn). Tuy nhiên, nó không được thiết kế với mục đích rõ ràng là cho phép kẻ tấn công hoặc bất kỳ ai khác tạo ra các văn bản mã hóa hợp lệ như vậy.

Điều này hoàn toàn trái ngược với một lược đồ mã hóa bất đối xứng, trong đó toàn bộ mục đích của nó là cho phép bất kỳ ai, kể cả kẻ tấn công, tạo ra các bản mã hợp lệ. Do đó, các lược đồ mã hóa bất đối xứng có thể được dán nhãn là **mã hóa truy cập nhiều**.

Để hiểu rõ hơn những gì đang xảy ra, hãy tưởng tượng rằng thay vì gửi tin nhắn điện tử, Bob muốn gửi một lá thư vật lý một cách bí mật. Một cách để đảm bảo tính bí mật là Alice gửi một ổ khóa an toàn cho Bob, nhưng giữ chìa khóa để mở khóa. Sau khi viết xong lá thư, Bob có thể đặt lá thư vào một hộp và đóng lại bằng ổ khóa của Alice. Sau đó, anh ta có thể gửi hộp khóa có tin nhắn cho Alice, người có chìa khóa để mở khóa.

Trong khi Bob có thể khóa ổ khóa, thì cả anh ta và bất kỳ người nào khác chặn hộp đều không thể mở ổ khóa nếu nó thực sự an toàn. Chỉ có Alice mới có thể mở khóa và xem nội dung lá thư của Bob vì cô ấy có chìa khóa.

Một chương trình mã hóa bất đối xứng, nói một cách đại khái, là phiên bản kỹ thuật số của quá trình này. Ổ khóa giống như khóa công khai và chìa khóa ổ khóa giống như khóa riêng tư. Tuy nhiên, vì ổ khóa là kỹ thuật số, nên Alice dễ dàng hơn nhiều và không tốn kém để phân phối nó cho bất kỳ ai muốn gửi tin nhắn bí mật cho cô ấy.

Để xác thực trong bối cảnh bất đối xứng, chúng tôi sử dụng **chữ ký số**. Do đó, chúng có cùng chức năng như mã xác thực tin nhắn trong bối cảnh đối xứng. Tổng quan về chữ ký số được cung cấp trong *Hình 2*.

Đầu tiên, Bob tạo một cặp khóa, bao gồm khóa công khai ($K_P$) và khóa riêng ($K_S$), và phân phối khóa công khai của mình. Khi anh ấy muốn gửi một tin nhắn đã xác thực đến Alice, trước tiên anh ấy lấy tin nhắn $M$ và khóa riêng của mình để tạo **chữ ký số** $D$. Sau đó, Bob gửi tin nhắn của mình cùng với chữ ký số cho Alice.

Alice chèn thông điệp, khóa công khai và chữ ký số vào **thuật toán xác minh**. Thuật toán này tạo ra **đúng** cho chữ ký hợp lệ hoặc **sai** cho chữ ký không hợp lệ.

Chữ ký số, như tên gọi của nó, là tương đương kỹ thuật số của chữ ký viết trên thư từ, hợp đồng, v.v. Trên thực tế, chữ ký số thường an toàn hơn nhiều. Với một chút nỗ lực, bạn có thể làm giả chữ ký viết; một quá trình dễ dàng hơn do chữ ký viết thường không được xác minh chặt chẽ. Tuy nhiên, chữ ký số an toàn, giống như mã xác thực tin nhắn an toàn, **không thể làm giả về mặt hiện hữu**: nghĩa là, với một lược đồ chữ ký số an toàn, không ai có thể tạo chữ ký cho tin nhắn vượt qua quy trình xác minh, trừ khi họ có khóa riêng.

*Hình 2: Xác thực không đối xứng*

![Figure 2: Asymmetric authentication](assets/Figure6-2.webp "Figure 2: Asymmetric authentication")

Giống như mã hóa bất đối xứng, chúng ta thấy sự tương phản thú vị giữa chữ ký số và mã xác thực tin nhắn. Đối với mã sau, thuật toán xác minh chỉ có thể được sử dụng bởi một trong các bên biết về giao tiếp an toàn. Điều này là do nó yêu cầu khóa riêng. Tuy nhiên, trong bối cảnh bất đối xứng, bất kỳ ai cũng có thể xác minh chữ ký số $S$ do Bob tạo.

Tất cả những điều này làm cho chữ ký số trở thành một công cụ cực kỳ mạnh mẽ. Ví dụ, nó tạo thành cơ sở để tạo chữ ký trên hợp đồng có thể được xác minh cho mục đích pháp lý. Nếu Bob đã ký trên hợp đồng trong cuộc trao đổi ở trên, Alice có thể trình bày thông điệp $M$, hợp đồng và chữ ký $S$ cho tòa án. Sau đó, tòa án có thể xác minh chữ ký bằng khóa công khai của Bob. [5]

Một ví dụ khác, chữ ký số là một khía cạnh quan trọng của phần mềm an toàn và phân phối bản cập nhật phần mềm. Loại xác minh công khai này không bao giờ có thể được tạo ra chỉ bằng mã xác thực tin nhắn.

Một ví dụ cuối cùng về sức mạnh của chữ ký số, hãy xem xét Bitcoin. Một trong những quan niệm sai lầm phổ biến nhất về Bitcoin, đặc biệt là trên phương tiện truyền thông, là các giao dịch được mã hóa: chúng không được mã hóa. Thay vào đó, các giao dịch Bitcoin hoạt động với chữ ký số để đảm bảo an ninh.

Bitcoin tồn tại theo từng đợt gọi là đầu ra giao dịch chưa sử dụng (hoặc **UTXO**). Giả sử bạn nhận được ba khoản thanh toán trên một địa chỉ Bitcoin cụ thể, mỗi khoản 2 bitcoin. Về mặt kỹ thuật, hiện tại bạn không có 6 bitcoin trên địa chỉ đó. Thay vào đó, bạn có ba đợt, mỗi đợt 2 bitcoin bị khóa bởi một vấn đề mật mã liên quan đến địa chỉ đó. Đối với bất kỳ khoản thanh toán nào bạn thực hiện, bạn có thể sử dụng một, hai hoặc cả ba đợt này, tùy thuộc vào số tiền bạn cần cho giao dịch.

Bằng chứng về quyền sở hữu đối với các đầu ra giao dịch chưa chi thường được thể hiện thông qua một hoặc nhiều chữ ký số. Bitcoin hoạt động chính xác vì các chữ ký số hợp lệ trên các đầu ra giao dịch chưa chi không khả thi về mặt tính toán để tạo ra, trừ khi bạn sở hữu thông tin bí mật cần thiết để tạo ra chúng.

Hiện tại, các giao dịch Bitcoin minh bạch bao gồm tất cả thông tin cần được xác minh bởi những người tham gia trong mạng, chẳng hạn như nguồn gốc của các đầu ra giao dịch chưa chi tiêu được sử dụng trong giao dịch. Mặc dù có thể ẩn một số thông tin đó và vẫn cho phép xác minh (như một số loại tiền điện tử thay thế như Monero), điều này cũng tạo ra những rủi ro bảo mật cụ thể.

Đôi khi có sự nhầm lẫn giữa chữ ký số và chữ ký viết tay được chụp bằng kỹ thuật số. Trong trường hợp sau, bạn chụp ảnh chữ ký viết tay của mình và dán vào một tài liệu điện tử như hợp đồng lao động. Tuy nhiên, đây không phải là chữ ký số theo nghĩa mật mã. Chữ ký sau chỉ là một con số dài chỉ có thể tạo ra khi sở hữu khóa riêng.

Cũng giống như trong cài đặt khóa đối xứng, bạn cũng có thể sử dụng mã hóa bất đối xứng và các lược đồ xác thực cùng nhau. Các nguyên tắc tương tự được áp dụng. Trước hết, bạn nên sử dụng các cặp khóa riêng-công khai khác nhau để mã hóa và tạo chữ ký số. Ngoài ra, trước tiên bạn nên mã hóa tin nhắn và sau đó xác thực tin nhắn đó.

Điều quan trọng là, trong nhiều ứng dụng, mật mã bất đối xứng không được sử dụng trong toàn bộ quá trình giao tiếp. Thay vào đó, nó thường chỉ được sử dụng để *trao đổi khóa đối xứng* giữa các bên mà họ thực sự sẽ giao tiếp.

Đây là trường hợp, ví dụ, khi bạn mua hàng trực tuyến. Biết được khóa công khai của người bán, họ có thể gửi cho bạn các tin nhắn được ký kỹ thuật số mà bạn có thể xác minh tính xác thực của chúng. Trên cơ sở này, bạn có thể làm theo một trong nhiều giao thức để trao đổi khóa đối xứng để giao tiếp an toàn.

Lý do chính cho tần suất của cách tiếp cận đã đề cập ở trên là mật mã bất đối xứng kém hiệu quả hơn nhiều so với mật mã đối xứng trong việc tạo ra một mức độ bảo mật cụ thể. Đây là một lý do tại sao chúng ta vẫn cần mật mã khóa đối xứng bên cạnh mật mã công khai. Ngoài ra, mật mã khóa đối xứng tự nhiên hơn nhiều trong các ứng dụng cụ thể như người dùng máy tính mã hóa dữ liệu của riêng họ.

Vậy thì chữ ký số và mã hóa khóa công khai giải quyết vấn đề phân phối khóa và quản lý khóa chính xác như thế nào?

Không có một câu trả lời nào ở đây. Mật mã bất đối xứng là một công cụ và không có một cách nào để sử dụng công cụ đó. Nhưng hãy lấy ví dụ trước đó của chúng tôi từ Jim’s Sporting Goods để chỉ ra cách các vấn đề thường được giải quyết trong ví dụ này.

Để bắt đầu, Jim’s Sporting Goods có thể sẽ tiếp cận một **cơ quan cấp chứng chỉ**, một tổ chức hỗ trợ phân phối khóa công khai. Cơ quan cấp chứng chỉ sẽ đăng ký một số thông tin chi tiết về Jim’s Sporting Goods và cấp cho họ một khóa công khai. Sau đó, họ sẽ gửi cho Jim’s Sporting Goods một chứng chỉ, được gọi là **chứng chỉ TLS/SSL**, với khóa công khai của Jim’s Sporting Goods được ký kỹ thuật số bằng khóa công khai của chính cơ quan cấp chứng chỉ đó. Theo cách này, cơ quan cấp chứng chỉ khẳng định rằng một khóa công khai cụ thể thực sự thuộc về Jim’s Sporting Goods.

Chìa khóa để hiểu quy trình này với chứng chỉ TLS/SSL là, mặc dù bạn thường không lưu trữ khóa công khai của Jim’s Sporting Goods ở bất kỳ đâu trên máy tính của mình, nhưng khóa công khai của các cơ quan cấp chứng chỉ được công nhận thực sự được lưu trữ trong trình duyệt hoặc trong hệ điều hành của bạn. Chúng được lưu trữ trong cái gọi là **chứng chỉ gốc**.

Do đó, khi Jim’s Sporting Goods cung cấp cho bạn chứng chỉ TLS/SSL, bạn có thể xác minh chữ ký số của cơ quan cấp chứng chỉ thông qua chứng chỉ gốc trong trình duyệt hoặc hệ điều hành của bạn. Nếu chữ ký hợp lệ, bạn có thể tương đối chắc chắn rằng khóa công khai trên chứng chỉ thực sự thuộc về Jim’s Sporting Goods. Trên cơ sở này, bạn có thể dễ dàng thiết lập giao thức để giao tiếp an toàn với Jim’s Sporting Goods.

Phân phối khóa hiện đã trở nên đơn giản hơn rất nhiều đối với Jim’s Sporting Goods. Không khó để thấy rằng quản lý khóa cũng đã trở nên đơn giản hơn rất nhiều. Thay vì phải lưu trữ hàng nghìn khóa, Jim’s Sporting Goods chỉ cần lưu trữ một khóa riêng cho phép tạo chữ ký cho khóa công khai trên chứng chỉ SSL của mình. Mỗi lần khách hàng truy cập vào trang web của Jim’s Sporting Goods, họ có thể thiết lập phiên giao tiếp an toàn từ khóa công khai này. Khách hàng cũng không cần lưu trữ bất kỳ thông tin nào (ngoại trừ khóa công khai của các cơ quan cấp chứng chỉ được công nhận trong hệ điều hành và trình duyệt của họ).

**Lưu ý:**

[5] Bất kỳ kế hoạch nào cố gắng đạt được sự không thể chối cãi, chủ đề khác mà chúng ta đã thảo luận trong Chương 1, về cơ bản sẽ cần liên quan đến chữ ký số.

## Hàm băm

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hàm băm có mặt ở khắp mọi nơi trong mật mã học. Chúng không phải là lược đồ đối xứng hay bất đối xứng, nhưng lại thuộc về một phạm trù mật mã riêng.

Chúng ta đã tìm hiểu về hàm băm trong Chương 4 khi tạo tin nhắn xác thực dựa trên hàm băm. Chúng cũng quan trọng trong bối cảnh chữ ký số, mặc dù có lý do hơi khác: Chữ ký số thường được tạo trên giá trị băm của một số tin nhắn (đã mã hóa), thay vì tin nhắn thực tế (đã mã hóa). Trong phần này, tôi sẽ giới thiệu chi tiết hơn về hàm băm.

Hãy bắt đầu bằng cách định nghĩa hàm băm. **Hàm băm** là bất kỳ hàm nào có thể tính toán hiệu quả, lấy đầu vào có kích thước tùy ý và tạo ra đầu ra có độ dài cố định.

**Hàm băm mật mã** chỉ là hàm băm hữu ích cho các ứng dụng trong mật mã. Đầu ra của hàm băm mật mã thường được gọi là **hash**, **hash-value** hoặc **message digest**.

Trong bối cảnh của mật mã học, "hàm băm" thường ám chỉ hàm băm mật mã. Tôi sẽ áp dụng phương pháp đó từ đây trở đi.

Một ví dụ về hàm băm phổ biến là **SHA-256** (thuật toán băm an toàn 256). Bất kể kích thước của đầu vào (ví dụ: 15 bit, 100 bit hoặc 10.000 bit), hàm này sẽ tạo ra giá trị băm 256 bit. Dưới đây, bạn có thể thấy một số ví dụ về đầu ra của hàm SHA-256.

“Xin chào”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

“Mật mã thật thú vị”: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Tất cả các đầu ra đều chính xác là 256 bit được viết ra theo định dạng thập lục phân (mỗi chữ số thập lục phân có thể được biểu diễn bằng bốn chữ số nhị phân). Vì vậy, ngay cả khi bạn đã chèn cuốn sách *Chúa tể những chiếc nhẫn* của Tolkien vào hàm SHA-256, đầu ra vẫn sẽ là 256 bit.

Các hàm băm như SHA-256 được sử dụng cho nhiều mục đích khác nhau trong mật mã học. Các thuộc tính nào được yêu cầu từ một hàm băm thực sự phụ thuộc vào ngữ cảnh của một ứng dụng cụ thể. Có hai thuộc tính chính thường được mong muốn của các hàm băm trong mật mã học: [6]

1. Chống va chạm

2. Ẩn

Hàm băm $H$ được gọi là **chống va chạm** nếu không thể tìm được hai giá trị $x$ và $y$ sao cho $x \neq y$, nhưng $H(x) = H(y)$.

Ví dụ, hàm băm chống va chạm rất quan trọng trong việc xác minh phần mềm. Giả sử bạn muốn tải xuống bản phát hành Windows của Bitcoin Core 0.21.0 (một ứng dụng máy chủ để xử lý lưu lượng mạng Bitcoin). Các bước chính bạn phải thực hiện để xác minh tính hợp pháp của phần mềm như sau:

1. Trước tiên, bạn cần tải xuống và nhập khóa công khai của một hoặc nhiều người đóng góp Bitcoin Core vào phần mềm có thể xác minh chữ ký số (ví dụ: Kleopetra). Bạn có thể tìm thấy các khóa công khai này [tại đây](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Bạn nên xác minh phần mềm Bitcoin Core bằng khóa công khai từ nhiều người đóng góp.

2. Tiếp theo, bạn cần xác minh khóa công khai mà bạn đã nhập. Ít nhất một bước bạn nên thực hiện là xác minh rằng khóa công khai bạn tìm thấy giống với khóa công khai đã công bố ở nhiều vị trí khác. Ví dụ, bạn có thể tham khảo các trang web cá nhân, trang Twitter hoặc trang Github của những người có khóa công khai mà bạn đã nhập. Thông thường, việc so sánh khóa công khai này được thực hiện bằng cách so sánh một hàm băm ngắn của khóa công khai được gọi là dấu vân tay.

3. Tiếp theo, bạn cần tải xuống tệp thực thi cho Bitcoin Core từ [trang web](www.bitcoincore.org). Sẽ có các gói có sẵn cho hệ điều hành Linux, Windows và MAC.

4. Tiếp theo, bạn phải tìm hai tệp phát hành. Tệp đầu tiên chứa hàm băm SHA-256 chính thức cho tệp thực thi bạn đã tải xuống cùng với các hàm băm trên tất cả các gói khác đã được phát hành. Tệp phát hành khác sẽ chứa các chữ ký từ nhiều người đóng góp khác nhau trên tệp phát hành với các hàm băm gói. Cả hai tệp phát hành này đều phải nằm trên trang web Bitcoin Core.

5. Tiếp theo, bạn sẽ cần tính toán hàm băm SHA-256 của tệp thực thi mà bạn đã tải xuống từ trang web Bitcoin Core trên máy tính của mình. Sau đó, bạn so sánh kết quả này với hàm băm gói chính thức cho tệp thực thi. Chúng phải giống nhau.

6. Cuối cùng, bạn sẽ phải xác minh rằng một hoặc nhiều chữ ký số trên tệp phát hành với các hàm băm gói chính thức thực sự tương ứng với một hoặc nhiều khóa công khai mà bạn đã nhập (các bản phát hành Bitcoin Core không phải lúc nào cũng được mọi người ký). Bạn có thể thực hiện việc này bằng một ứng dụng như Kleopetra.

Quá trình xác minh phần mềm này có hai lợi ích chính. Đầu tiên, nó đảm bảo rằng không có lỗi nào trong quá trình truyền tải khi tải xuống từ trang web Bitcoin Core. Thứ hai, nó đảm bảo rằng không có kẻ tấn công nào có thể khiến bạn tải xuống mã độc đã sửa đổi, bằng cách hack trang web Bitcoin Core hoặc bằng cách chặn lưu lượng truy cập.

Quy trình xác minh phần mềm nêu trên bảo vệ chống lại những vấn đề này chính xác như thế nào?

Nếu bạn đã cẩn thận xác minh các khóa công khai mà bạn đã nhập, thì bạn có thể khá chắc chắn rằng các khóa này thực sự là của họ và không bị xâm phạm. Vì chữ ký số có tính không thể làm giả hiện hữu, bạn biết rằng chỉ những người đóng góp này mới có thể tạo chữ ký số trên các hàm băm gói chính thức trên tệp phát hành.

Giả sử các chữ ký trên tệp phát hành bạn đã tải xuống được kiểm tra. Bây giờ bạn có thể so sánh giá trị băm bạn đã tính toán cục bộ cho tệp thực thi Windows bạn đã tải xuống với giá trị được bao gồm trong tệp phát hành đã ký đúng cách. Như bạn đã biết, hàm băm SHA-256 có khả năng chống va chạm, một sự trùng khớp có nghĩa là tệp thực thi của bạn giống hệt với tệp thực thi chính thức.

Bây giờ chúng ta hãy chuyển sang tính chất chung thứ hai của hàm băm: **ẩn**. Bất kỳ hàm băm $H$ nào cũng được cho là có tính chất ẩn nếu, đối với bất kỳ $x$ nào được chọn ngẫu nhiên từ một phạm vi rất lớn, không thể tìm thấy $x$ khi chỉ cho $H(x)$.

Dưới đây, bạn có thể thấy đầu ra SHA-256 của tin nhắn tôi đã viết. Để đảm bảo đủ tính ngẫu nhiên, tin nhắn bao gồm một chuỗi ký tự được tạo ngẫu nhiên ở cuối. Vì SHA-256 có thuộc tính ẩn, không ai có thể giải mã được tin nhắn này.


- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Nhưng tôi sẽ không để bạn phải hồi hộp cho đến khi SHA-256 trở nên yếu hơn. Tin nhắn gốc tôi viết như sau:


- “Đây là một thông điệp rất ngẫu nhiên, hoặc đúng hơn là khá ngẫu nhiên. Phần mở đầu này thì không, nhưng tôi sẽ kết thúc bằng một số ký tự tương đối ngẫu nhiên để đảm bảo một thông điệp rất khó đoán. XLWz4dVG3BxUWm7zQ9qS”.

Một cách phổ biến mà các hàm băm có thuộc tính ẩn được sử dụng là trong quản lý mật khẩu (khả năng chống va chạm cũng quan trọng đối với ứng dụng này). Bất kỳ dịch vụ dựa trên tài khoản trực tuyến nào như Facebook hoặc Google sẽ không lưu trữ trực tiếp mật khẩu của bạn để quản lý quyền truy cập vào tài khoản của bạn. Thay vào đó, họ sẽ chỉ lưu trữ một hàm băm của mật khẩu đó. Mỗi lần bạn nhập mật khẩu trên trình duyệt, một hàm băm sẽ được tính toán trước. Chỉ hàm băm đó được gửi đến máy chủ của nhà cung cấp dịch vụ và được so sánh với hàm băm được lưu trữ trong cơ sở dữ liệu phụ trợ. Thuộc tính ẩn có thể giúp đảm bảo rằng kẻ tấn công không thể khôi phục nó từ giá trị băm.

Tất nhiên, quản lý mật khẩu thông qua hàm băm chỉ hiệu quả nếu người dùng thực sự chọn mật khẩu khó. Thuộc tính ẩn giả định rằng x được chọn ngẫu nhiên từ một phạm vi rất lớn. Việc chọn mật khẩu như "1234", "mypassword" hoặc ngày sinh của bạn sẽ không mang lại bất kỳ bảo mật thực sự nào. Có danh sách dài các mật khẩu phổ biến và hàm băm của chúng mà kẻ tấn công có thể tận dụng nếu chúng có được hàm băm của mật khẩu của bạn. Các loại tấn công này được gọi là **tấn công từ điển**. Nếu kẻ tấn công biết một số thông tin cá nhân của bạn, chúng cũng có thể thử một số phỏng đoán có căn cứ. Do đó, bạn luôn cần mật khẩu dài, an toàn (tốt nhất là chuỗi dài, ngẫu nhiên từ trình quản lý mật khẩu).

Đôi khi một ứng dụng có thể cần một hàm băm có cả khả năng chống va chạm và ẩn. Nhưng chắc chắn không phải lúc nào cũng vậy. Ví dụ, quy trình xác minh phần mềm mà chúng ta đã thảo luận chỉ yêu cầu hàm băm hiển thị khả năng chống va chạm, việc ẩn không quan trọng.

Trong khi khả năng chống va chạm và ẩn là những tính chất chính được tìm kiếm ở hàm băm trong mật mã, thì trong một số ứng dụng nhất định, các loại tính chất khác cũng có thể được mong muốn.

**Lưu ý:**

[6] Thuật ngữ “ẩn” không phải là ngôn ngữ thông dụng, nhưng được lấy cụ thể từ Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller và Steven Goldfeder, *Công nghệ Bitcoin và tiền điện tử*, Nhà xuất bản Đại học Princeton (Princeton, 2016), Chương 1.

# Hệ thống mật mã RSA

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Vấn đề phân tích thành nhân tử

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Trong khi mật mã đối xứng thường khá trực quan đối với hầu hết mọi người, thì mật mã bất đối xứng thường không như vậy. Mặc dù bạn có thể thoải mái với mô tả cấp cao được cung cấp trong các phần trước, bạn có thể tự hỏi chính xác hàm một chiều là gì và chúng được sử dụng chính xác như thế nào để xây dựng các lược đồ bất đối xứng.

Trong chương này, tôi sẽ giải đáp một số bí ẩn xung quanh mật mã bất đối xứng, bằng cách xem xét sâu hơn một ví dụ cụ thể, cụ thể là hệ thống mật mã RSA. Trong phần đầu tiên, tôi sẽ giới thiệu bài toán phân tích thừa số mà bài toán RSA dựa trên. Sau đó, tôi sẽ đề cập đến một số kết quả chính từ lý thuyết số. Trong phần cuối, chúng ta sẽ tổng hợp thông tin này lại để giải thích bài toán RSA và cách sử dụng bài toán này để tạo ra các lược đồ mật mã bất đối xứng.

Việc bổ sung chiều sâu này vào cuộc thảo luận của chúng ta không phải là một nhiệm vụ dễ dàng. Nó đòi hỏi phải giới thiệu khá nhiều định lý và mệnh đề lý thuyết số. Nhưng đừng để toán học ngăn cản bạn. Làm việc thông qua cuộc thảo luận này sẽ cải thiện đáng kể sự hiểu biết của bạn về những gì nằm bên dưới mật mã bất đối xứng và là một khoản đầu tư xứng đáng.

Bây giờ chúng ta hãy chuyển sang bài toán phân tích thừa số.

___

Bất cứ khi nào bạn nhân hai số, chẳng hạn $a$ và $b$, chúng ta gọi các số $a$ và $b$ là **thừa số**, và kết quả là **tích**. Cố gắng viết một số $N$ vào phép nhân của hai hoặc nhiều thừa số được gọi là **phân tích** hoặc **phân tích thừa số**. [1] Bạn có thể gọi bất kỳ bài toán nào yêu cầu điều này là **bài toán phân tích thừa số**.

Khoảng 2.500 năm trước, nhà toán học người Hy Lạp Euclid xứ Alexandria đã khám phá ra một định lý quan trọng về phép phân tích số nguyên. Định lý này thường được gọi là **định lý phân tích duy nhất** và nêu như sau:

**Định lý 1**. Mọi số nguyên $N$ lớn hơn 1 đều là số nguyên tố hoặc có thể biểu diễn dưới dạng tích các ước nguyên tố.

Toàn bộ phần sau của tuyên bố này có nghĩa là bạn có thể lấy bất kỳ số nguyên không nguyên tố $N$ nào lớn hơn 1 và viết nó ra dưới dạng phép nhân các số nguyên tố. Dưới đây là một số ví dụ về các số nguyên không nguyên tố được viết dưới dạng tích của các thừa số nguyên tố.


- $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
- $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
- $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Đối với cả ba số nguyên trên, việc tính các thừa số nguyên tố của chúng tương đối dễ, ngay cả khi bạn chỉ được cung cấp $N$. Bạn bắt đầu với số nguyên tố nhỏ nhất, cụ thể là 2, và xem số nguyên $N$ chia hết cho số đó bao nhiêu lần. Sau đó, bạn chuyển sang kiểm tra khả năng chia hết của $N$ cho 3, 5, 7, v.v. Bạn tiếp tục quá trình này cho đến khi số nguyên $N$ của bạn được viết dưới dạng tích của chỉ các số nguyên tố.

Ví dụ, hãy lấy số nguyên 84. Dưới đây bạn có thể thấy quy trình xác định các thừa số nguyên tố của nó. Ở mỗi bước, chúng ta lấy ra thừa số nguyên tố nhỏ nhất còn lại (ở bên trái) và xác định số hạng còn lại cần phân tích. Chúng ta tiếp tục cho đến khi số hạng còn lại cũng là một số nguyên tố. Ở mỗi bước, phép phân tích hiện tại của 84 được hiển thị ở phía bên phải.


- Thừa số nguyên tố = 2: số dư = 42 ($84 = 2 \cdot 42$)
- Thừa số nguyên tố = 2: số dư = 21 ($84 = 2 \cdot 2 \cdot 21$)
- Thừa số nguyên tố = 3: số dư = 7 ($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
- Vì 7 là số nguyên tố nên kết quả là $2 \cdot 2 \cdot 3 \cdot 7$, hoặc $2^2 \cdot 3 \cdot 7$.

Giả sử bây giờ $N$ rất lớn. Sẽ khó khăn như thế nào để rút gọn $N$ thành các thừa số nguyên tố của nó?

Điều đó thực sự phụ thuộc vào $N$. Giả sử, ví dụ, $N$ là 50.450.400. Mặc dù con số này có vẻ đáng sợ, nhưng các phép tính không quá phức tạp và có thể dễ dàng thực hiện bằng tay. Như trên, bạn chỉ cần bắt đầu với 2 và làm việc theo cách của bạn. Bên dưới, bạn có thể thấy kết quả của quá trình này theo cách tương tự như trên.


- 2: 25.225.200 (50.450.400 đô la = 2 \cdot 25.225.200)
- 2: 12.612.600 (50.450.400 đô la = 2^2 \cdot 12.612.600)
- 2: 6.306.300 (50.450.400 đô la = 2^3 \cdot 6.306.300)
- 2: 3.153.150 (50.450.400 đô la = 2^4 \cdot 3.153.150)
- 2: 1.576.575 (50.450.400 đô la = 2^5 \cdot 1.576.575)
- 3: 525.525 (50.450.400 đô la = 2^5 \cdot 3 \cdot 525.525)
- 3: 175.175 (50.450.400 đô la = 2^5 \cdot 3^2 \cdot 175.175)
- 5: 35.035 (50.450.400 đô la = 2^5 \cdot 3^2 \cdot 5 \cdot 35.035 đô la)
- 5: 7.007 (50.450.400 đô la = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7.007 đô la)
- 7: 1.001 (50.450.400 đô la = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1.001 đô la)
- 7: 143 (50.450.400 đô la = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
- 11: 13 (50.450.400 đô la = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- Vì 13 là số nguyên tố nên kết quả là $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Giải quyết vấn đề này bằng tay mất một thời gian. Tất nhiên, máy tính có thể làm tất cả những điều này trong một phần nhỏ của một giây. Trên thực tế, máy tính thường có thể phân tích thừa số các số nguyên cực lớn trong một phần nhỏ của một giây.

Tuy nhiên, có một số ngoại lệ nhất định. Giả sử rằng trước tiên chúng ta chọn ngẫu nhiên hai số nguyên tố rất lớn. Người ta thường dán nhãn $p$ và $q$ cho chúng, và tôi sẽ áp dụng quy ước đó ở đây.

Để cụ thể hơn, hãy nói rằng $p$ và $q$ đều là số nguyên tố 1024 bit và chúng thực sự cần ít nhất 1024 bit để có thể biểu diễn (do đó bit đầu tiên phải là 1). Vì vậy, ví dụ, 37 không thể là một trong những số nguyên tố. Bạn chắc chắn có thể biểu diễn 37 bằng 1024 bit. Nhưng rõ ràng *bạn không cần* nhiều bit như vậy để biểu diễn nó. Bạn có thể biểu diễn 37 bằng bất kỳ chuỗi nào có 6 bit trở lên. (Trong 6 bit, 37 sẽ được biểu diễn là $100101$).

Điều quan trọng là phải đánh giá $p$ và $q$ lớn như thế nào nếu được chọn theo các điều kiện trên. Ví dụ, tôi đã chọn một số nguyên tố ngẫu nhiên cần ít nhất 1024 bit để biểu diễn bên dưới.


- 14.752.173.874.503.595.484.930.006.383.670.759.559.764.562.721.397.166.747.289.220.945.457.932.666.751 ,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,04 9,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484, 558.332.897.443.152.653.214.483.870.992.618.171.825.921.582.253.023.974.514.209.142.520.026.807.636.589

Giả sử bây giờ sau khi chọn ngẫu nhiên các số nguyên tố $p$ và $q$, chúng ta nhân chúng để thu được số nguyên $N$. Do đó, số nguyên sau này là số 2048 bit, cần ít nhất 2048 bit để biểu diễn. Nó lớn hơn rất nhiều so với $p$ hoặc $q$.

Giả sử bạn chỉ đưa cho máy tính $N$ và yêu cầu nó tìm hai ước nguyên tố 1024 bit của $N$. Xác suất máy tính phát hiện ra $p$ và $q$ là cực kỳ nhỏ. Bạn có thể nói rằng điều đó là không thể đối với mọi mục đích thực tế. Điều này đúng, ngay cả khi bạn sử dụng một siêu máy tính hoặc thậm chí là một mạng lưới các siêu máy tính.

Để bắt đầu, giả sử máy tính cố gắng giải quyết vấn đề bằng cách tuần hoàn qua các số 1024 bit, kiểm tra trong từng trường hợp xem chúng có phải là số nguyên tố không và có phải là ước số của $N$ không. Tập hợp các số nguyên tố cần kiểm tra khi đó xấp xỉ $1,265 \cdot 10^{305}$. [2]

Ngay cả khi bạn sử dụng tất cả máy tính trên hành tinh này và yêu cầu chúng cố gắng tìm và kiểm tra các số nguyên tố 1024 bit theo cách này, thì cơ hội tìm ra ước nguyên tố của $N$ là 1 trên một tỷ sẽ đòi hỏi thời gian tính toán dài hơn nhiều so với tuổi của Vũ trụ.

Trên thực tế, máy tính có thể làm tốt hơn quy trình thô sơ vừa mô tả. Có một số thuật toán mà máy tính có thể áp dụng để phân tích thừa số nhanh hơn. Tuy nhiên, vấn đề là ngay cả khi sử dụng các thuật toán hiệu quả hơn này, nhiệm vụ của máy tính vẫn không khả thi về mặt tính toán. [3]

Điều quan trọng là, khó khăn của việc phân tích thừa số trong các điều kiện vừa mô tả nằm ở giả định rằng không có thuật toán nào hiệu quả về mặt tính toán để tính các thừa số nguyên tố. Chúng ta thực sự không thể chứng minh rằng không tồn tại một thuật toán hiệu quả. Tuy nhiên, giả định này rất hợp lý: mặc dù đã có nhiều nỗ lực trong hàng trăm năm, chúng ta vẫn chưa tìm ra một thuật toán hiệu quả về mặt tính toán như vậy.

Do đó, bài toán phân tích thừa số, trong một số trường hợp nhất định, có thể được coi là một bài toán khó. Cụ thể, khi $p$ và $q$ là các số nguyên tố rất lớn, tích $N$ của chúng không khó để tính; nhưng phân tích thừa số chỉ với $N$ thì thực tế là không thể.

**Lưu ý:**

[1] Phân tích thừa số cũng có thể quan trọng khi làm việc với các loại đối tượng toán học khác ngoài số. Ví dụ, có thể hữu ích khi phân tích thừa số các biểu thức đa thức như $x^2 - 2x + 1$. Trong thảo luận của chúng tôi, chúng tôi sẽ chỉ tập trung vào phân tích thừa số của các số, cụ thể là số nguyên.

[2] Theo **định lý số nguyên tố**, số lượng các số nguyên tố nhỏ hơn hoặc bằng $N$ xấp xỉ là $N/\ln(N)$. Điều này có nghĩa là bạn có thể ước tính số lượng các số nguyên tố có độ dài 1024 bit bằng:

$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...tương đương khoảng $1,265 \times 10^{305}$.

[3] Điều tương tự cũng đúng đối với các bài toán logarit rời rạc. Do đó, tại sao các cấu trúc bất đối xứng lại hoạt động với các khóa lớn hơn nhiều so với các cấu trúc mật mã đối xứng.

## Kết quả lý thuyết số

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Thật không may, bài toán phân tích không thể được sử dụng trực tiếp cho các lược đồ mật mã bất đối xứng. Tuy nhiên, chúng ta có thể sử dụng một bài toán phức tạp hơn nhưng có liên quan đến vấn đề này: bài toán RSA.

Để hiểu được bài toán RSA, chúng ta sẽ cần hiểu một số định lý và mệnh đề từ lý thuyết số. Chúng được trình bày trong phần này thành ba tiểu mục: (1) cấp N, (2) khả nghịch modulo N và (3) định lý Euler.

Một số tài liệu trong ba tiểu mục đã được giới thiệu trong *Chương 3*. Nhưng tôi sẽ trình bày lại tài liệu đó để thuận tiện.

### Thứ tự của N

Số nguyên $a$ là **số nguyên tố cùng nhau** hoặc là **số nguyên tố tương đối** với số nguyên $N$, nếu ước chung lớn nhất giữa chúng là 1. Mặc dù theo quy ước, 1 không phải là số nguyên tố, nhưng nó là số nguyên tố cùng nhau của mọi số nguyên (tương tự như $-1$).

Ví dụ, hãy xem xét trường hợp khi $a = 18$ và $N = 37$. Đây rõ ràng là các số nguyên tố cùng nhau. Số nguyên lớn nhất chia hết cho cả 18 và 37 là 1. Ngược lại, hãy xem xét trường hợp khi $a = 42$ và $N = 16$. Đây rõ ràng không phải là các số nguyên tố cùng nhau. Cả hai số đều chia hết cho 2, lớn hơn 1.

Bây giờ chúng ta có thể định nghĩa thứ tự của $N$ như sau. Giả sử $N$ là một số nguyên lớn hơn 1. Khi đó, **thứ tự của N** là số tất cả các số nguyên tố cùng nhau với $N$ sao cho với mỗi số nguyên tố cùng nhau $a$, điều kiện sau đây được giữ nguyên: $1 \leq a < N$.

Ví dụ, nếu $N = 12$, thì 1, 5, 7 và 11 là các số nguyên tố cùng nhau duy nhất đáp ứng yêu cầu trên. Do đó, cấp số của 12 bằng 4.

Giả sử $N$ là số nguyên tố. Khi đó, bất kỳ số nguyên nào nhỏ hơn $N$ nhưng lớn hơn hoặc bằng 1 đều nguyên tố cùng nhau với nó. Điều này bao gồm tất cả các phần tử trong tập hợp sau: $\{1,2,3,….,N - 1\}$. Do đó, khi $N$ là số nguyên tố, thì cấp của $N$ là $N - 1$. Điều này được nêu trong mệnh đề 1, trong đó $\phi(N)$ biểu thị cấp của $N$.

**Đề xuất 1**. $\phi(N) = N - 1$ khi $N$ là số nguyên tố

Giả sử $N$ không phải là số nguyên tố. Khi đó, bạn có thể tính thứ tự của nó bằng cách sử dụng **hàm Euler’s Phi**. Trong khi việc tính thứ tự của một số nguyên nhỏ tương đối đơn giản, hàm Euler’s Phi trở nên đặc biệt quan trọng đối với các số nguyên lớn hơn. Đề xuất của hàm Euler’s Phi được nêu dưới đây.

**Định lý 2**. Cho $N$ bằng $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, trong đó tập hợp $\{p_i\}$ bao gồm tất cả các ước nguyên tố phân biệt của $N$ và mỗi $e_i$ biểu thị số lần ước nguyên tố $p_i$ xuất hiện đối với $N$. Sau đó,

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Định lý 2** cho thấy rằng khi bạn phân tích bất kỳ số $N$ không nguyên tố nào thành các thừa số nguyên tố riêng biệt, bạn có thể dễ dàng tính được cấp của $N$.

Ví dụ, giả sử $N = 270$. Đây rõ ràng không phải là số nguyên tố. Phân tích $N$ thành các thừa số nguyên tố của nó sẽ cho ra biểu thức: $2 \cdot 3^3 \cdot 5$. Theo hàm Euler’s Phi, thì thứ tự của $N$ như sau:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Tiếp theo giả sử $N$ là tích của hai số nguyên tố $p$ và $q$. **Định lý 2** ở trên phát biểu rằng thứ tự của $N$ như sau:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Đây là kết quả quan trọng đối với bài toán RSA nói riêng và được nêu trong **Đề xuất 2** bên dưới.

**Đề xuất 2**. Nếu $N$ là tích của hai số nguyên tố $p$ và $q$, thì cấp của $N$ là tích $(p - 1) \cdot (q - 1)$.

Để minh họa, giả sử $N = 119$. Số nguyên này có thể phân tích thành hai số nguyên tố, cụ thể là 7 và 17. Do đó, hàm Euler’s Phi cho thấy thứ tự của 119 như sau:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Nói cách khác, số nguyên 119 có 96 số nguyên tố cùng nhau trong phạm vi từ 1 đến 119. Trên thực tế, tập hợp này bao gồm tất cả các số nguyên từ 1 đến 119, không phải là bội số của 7 hoặc 17.

Từ đây trở đi, chúng ta hãy biểu thị tập hợp các số nguyên tố cùng nhau xác định thứ tự của $N$ là $C_N$. Đối với ví dụ của chúng ta, khi $N = 119$, tập hợp $C_{119}$ quá lớn để có thể liệt kê đầy đủ. Nhưng một số phần tử như sau:

$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Khả nghịch đảo modulo N

Ta có thể nói rằng một số nguyên $a$ là **khả nghịch đảo modulo N**, nếu tồn tại ít nhất một số nguyên $b$ sao cho $a \cdot b \mod N = 1 \mod N$. Bất kỳ số nguyên $b$ nào như vậy được gọi là **nghịch đảo** (hoặc **nghịch đảo nhân**) của $a$ khi giảm modulo $N$.

Giả sử, ví dụ, $a = 5$ và $N = 11$. Có nhiều số nguyên mà bạn có thể nhân 5, do đó $5 \cdot b \mod 11 = 1 \mod 11$. Ví dụ, hãy xem xét các số nguyên 20 và 31. Dễ dàng thấy rằng cả hai số nguyên này đều là nghịch đảo của 5 khi rút gọn theo modulo 11.


- $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
- $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Trong khi 5 có nhiều nghịch đảo quy giản theo modulo 11, bạn có thể chứng minh rằng chỉ tồn tại một nghịch đảo dương duy nhất của 5 nhỏ hơn 11. Trên thực tế, điều này không chỉ xảy ra riêng với ví dụ cụ thể của chúng ta mà còn là kết quả chung.

**Đề xuất 3**. Nếu số nguyên $a$ khả nghịch modulo $N$, thì phải có đúng một nghịch đảo dương của $a$ nhỏ hơn $N$. (Vì vậy, nghịch đảo duy nhất này của $a$ phải xuất phát từ tập hợp $\{1, \dots, N - 1\}$).

Hãy biểu thị nghịch đảo duy nhất của $a$ từ **Đề xuất 3** là $a^{-1}$. Đối với trường hợp khi $a = 5$ và $N = 11$, bạn có thể thấy rằng $a^{-1} = 9$, với điều kiện là $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Lưu ý rằng bạn cũng có thể thu được giá trị 9 cho $a^{-1}$ trong ví dụ của chúng tôi bằng cách chỉ cần giảm bất kỳ nghịch đảo nào khác của $a$ theo modulo 11. Ví dụ, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Vì vậy, bất cứ khi nào một số nguyên $a > N$ có thể đảo ngược modulo $N$, thì $a \mod N$ cũng phải có thể đảo ngược modulo $N$.

Không nhất thiết phải có nghịch đảo của $a$ theo phép trừ modulo $N$. Giả sử, ví dụ, $a = 2$ và $N = 8$. Không có $b$, hoặc bất kỳ $a^{-1}$ nào cụ thể, sao cho $2 \cdot b \mod 8 = 1 \mod 8$. Điều này là do bất kỳ giá trị nào của $b$ sẽ luôn tạo ra bội số của 2, do đó không có phép chia nào cho 8 có thể tạo ra số dư bằng 1.

Làm sao chúng ta biết chính xác được một số nguyên $a$ có nghịch đảo cho một $N$ nhất định? Như bạn có thể đã nhận thấy trong ví dụ trên, ước chung lớn nhất giữa 2 và 8 cao hơn 1, cụ thể là 2. Và điều này thực sự minh họa cho kết quả chung sau:

**Đề xuất 4**. Tồn tại một nghịch đảo của số nguyên $a$ cho phép rút gọn modulo $N$, và đặc biệt là một nghịch đảo dương duy nhất nhỏ hơn $N$, nếu và chỉ nếu ước chung lớn nhất giữa $a$ và $N$ là 1 (tức là nếu chúng là số nguyên tố cùng nhau).

Đối với trường hợp $a = 5$ và $N = 11$, chúng ta kết luận rằng $a^{-1} = 9$, với điều kiện là $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Điều quan trọng cần lưu ý là điều ngược lại cũng đúng. Nghĩa là, khi $a = 9$ và $N = 11$, thì $a^{-1} = 5$.

### Định lý Euler

Trước khi chuyển sang bài toán RSA, chúng ta cần hiểu thêm một định lý quan trọng nữa, đó là **Định lý Euler**. Định lý này nêu như sau:

**Định lý 3**. Giả sử hai số nguyên $a$ và $N$ là hai số nguyên tố cùng nhau. Khi đó, $a^{\phi(N)} \mod N = 1 \mod N$.

Đây là một kết quả đáng chú ý, nhưng hơi khó hiểu lúc đầu. Chúng ta hãy xem một ví dụ để hiểu rõ hơn.

Giả sử $a = 5$ và $N = 7$. Đây thực sự là các số nguyên tố cùng nhau như định lý Euler yêu cầu. Chúng ta biết rằng cấp số 7 bằng 6, vì 7 là số nguyên tố (xem **Đề xuất 1**).

Định lý Euler hiện nêu rằng $5^6 \mod 7$ phải bằng $1 \mod 7$. Dưới đây là các phép tính để chứng minh rằng điều này thực sự đúng.


- $5^6 \mod 7 = 15.625 \mod 7 = 1 \mod N$

Số nguyên 7 chia hết cho 15.624 tổng cộng 2.233 lần. Do đó, số dư của phép chia 16.625 cho 7 là 1.

Tiếp theo, sử dụng hàm Euler Phi, **Định lý 2**, bạn có thể suy ra **Đề xuất 5** bên dưới.

**Đề xuất 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ với mọi số nguyên dương $a$ và $b$.

Chúng tôi sẽ không trình bày lý do tại sao lại như vậy. Nhưng chỉ cần lưu ý rằng bạn đã thấy bằng chứng về đề xuất này thông qua thực tế là $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ khi $p$ và $q$ là số nguyên tố, như đã nêu trong **Đề xuất 2**.

Định lý Euler kết hợp với **Đề xuất 5** có ý nghĩa quan trọng. Hãy xem điều gì xảy ra, ví dụ, trong các biểu thức bên dưới, trong đó $a$ và $N$ là các số nguyên tố cùng nhau.


- $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
- $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
- $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Do đó, sự kết hợp của định lý Euler và **Đề xuất 5** cho phép chúng ta tính toán đơn giản một số biểu thức. Nhìn chung, chúng ta có thể tóm tắt hiểu biết như trong **Đề xuất 6**.

**Đề xuất 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Bây giờ chúng ta phải kết hợp mọi thứ lại với nhau trong bước cuối cùng đầy khó khăn.

Cũng giống như $N$ có thứ tự $\phi(N)$ bao gồm các phần tử của tập hợp $C_N$, chúng ta biết rằng số nguyên $\phi(N)$ cũng phải có thứ tự và tập hợp các số nguyên tố cùng nhau. Hãy đặt $\phi(N) = R$. Khi đó, chúng ta biết rằng cũng có một giá trị cho $\phi(R)$ và tập hợp các số nguyên tố cùng nhau $C_R$.

Giả sử bây giờ chúng ta chọn một số nguyên $e$ từ tập $C_R$. Chúng ta biết từ **Đề xuất 3** rằng số nguyên $e$ này chỉ có một nghịch đảo dương duy nhất nhỏ hơn $R$. Nghĩa là, $e$ có một nghịch đảo duy nhất từ tập $C_R$. Chúng ta hãy gọi nghịch đảo này là $d$. Với định nghĩa về nghịch đảo, điều này có nghĩa là $e \cdot d = 1 \mod R$.

Chúng ta có thể sử dụng kết quả này để đưa ra một tuyên bố về số nguyên $N$ ban đầu của chúng ta. Điều này được tóm tắt trong **Đề xuất 7**.

**Đề xuất 7**. Giả sử $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Khi đó, đối với bất kỳ phần tử $a$ nào của tập hợp $C_N$ thì phải xảy ra trường hợp $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Bây giờ chúng ta đã có tất cả các kết quả lý thuyết số cần thiết để nêu rõ bài toán RSA.

## Hệ thống mật mã RSA

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Bây giờ chúng ta đã sẵn sàng để nêu vấn đề RSA. Giả sử bạn tạo một tập hợp các biến bao gồm $p$, $q$, $N$, $\phi(N)$, $e$, $d$ và $y$. Gọi tập hợp này là $\Pi$. Nó được tạo như sau:

1. Tạo ngẫu nhiên hai số nguyên tố $p$ và $q$ có cùng số nguyên tố và tính tích $N$ của chúng.

2. Tính bậc của $N$, $\phi(N)$, theo tích sau: $(p - 1) \cdot (q - 1)$.

3. Chọn $e > 2$ sao cho nó nhỏ hơn và nguyên tố cùng nhau với $\phi(N)$.

4. Tính $d$ bằng cách đặt $e \cdot d \mod \phi(N) = 1$.

5. Chọn một giá trị ngẫu nhiên $y$ nhỏ hơn và nguyên tố cùng nhau với $N$.

Bài toán RSA bao gồm việc tìm $x$ sao cho $x^e = y$, trong khi chỉ được cung cấp một tập hợp con thông tin liên quan đến $\Pi$, cụ thể là các biến $N$, $e$ và $y$. Khi $p$ và $q$ rất lớn, thông thường người ta khuyên rằng chúng có kích thước 1024 bit, thì bài toán RSA được cho là khó. Bây giờ bạn có thể thấy tại sao lại như vậy khi xem xét các thảo luận trước đó.

Một cách dễ dàng để tính $x$ khi $x^e \mod N = y \mod N$ chỉ đơn giản là tính $y^d \mod N$. Chúng ta biết $y^d \mod N = x \mod N$ bằng các phép tính sau:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Vấn đề là chúng ta không biết giá trị $d$ vì nó không được đưa ra trong bài toán. Do đó, chúng ta không thể tính trực tiếp $y^d \mod N$ để tạo ra $x \mod N$.

Tuy nhiên, chúng ta có thể tính gián tiếp $d$ theo thứ tự của $N$, $\phi(N)$, vì chúng ta biết rằng $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Nhưng theo giả định, bài toán cũng không đưa ra giá trị cho $\phi(N)$.

Cuối cùng, thứ tự có thể được tính gián tiếp với các thừa số nguyên tố $p$ và $q$, do đó cuối cùng chúng ta có thể tính được $d$. Nhưng theo giả định, các giá trị $p$ và $q$ cũng không được cung cấp cho chúng ta.

Nói một cách nghiêm ngặt, ngay cả khi bài toán phân tích thừa số trong bài toán RSA là khó, chúng ta không thể chứng minh rằng bài toán RSA cũng khó. Cụ thể là có thể có những cách khác để giải bài toán RSA ngoài việc thông qua phân tích thừa số. Tuy nhiên, người ta thường chấp nhận và cho rằng nếu bài toán phân tích thừa số trong bài toán RSA là khó, thì bản thân bài toán RSA cũng khó.

Nếu bài toán RSA thực sự khó, thì nó tạo ra một hàm một chiều với một cửa sập. Hàm ở đây là $f(g) = g^e \mod N$. Với kiến thức về $f(g)$, bất kỳ ai cũng có thể dễ dàng tính toán một giá trị $y$ cho một $g = x$ cụ thể. Tuy nhiên, thực tế là không thể tính toán một giá trị cụ thể $x$ chỉ từ việc biết giá trị $y$ và hàm $f(g)$. Ngoại lệ là khi bạn được cung cấp một thông tin $d$, cửa sập. Trong trường hợp đó, bạn có thể chỉ cần tính $y^d$ để đưa ra $x$.

Chúng ta hãy xem xét một ví dụ cụ thể để minh họa cho bài toán RSA. Tôi không thể chọn một bài toán RSA được coi là khó theo các điều kiện trên vì các con số sẽ rất khó sử dụng. Thay vào đó, ví dụ này chỉ để minh họa cách thức hoạt động chung của bài toán RSA.

Để bắt đầu, giả sử bạn chọn hai số nguyên tố ngẫu nhiên là 13 và 31. Vậy $p = 13$ và $q = 31$. Tích $N$ của hai số nguyên tố này bằng 403. Ta có thể dễ dàng tính được bậc của 403. Nó tương đương với $(13 - 1) \cdot (31 - 1) = 360$.

Tiếp theo, theo bước 3 của bài toán RSA, chúng ta cần chọn một số nguyên tố chung cho 360 lớn hơn 2 và nhỏ hơn 360. Chúng ta không phải chọn giá trị này một cách ngẫu nhiên. Giả sử chúng ta chọn 103. Đây là số nguyên tố chung của 360 vì ước chung lớn nhất của nó với 103 là 1.

Bước 4 bây giờ yêu cầu chúng ta tính toán giá trị $d$ sao cho $103 \cdot d \mod 360 = 1$. Đây không phải là một nhiệm vụ dễ dàng bằng tay khi giá trị của $N$ lớn. Nó yêu cầu chúng ta sử dụng một thủ tục được gọi là **thuật toán Euclidean mở rộng**.

Mặc dù tôi không trình bày quy trình ở đây, nhưng nó cho ra giá trị 7 khi $e = 103$. Bạn có thể xác minh rằng cặp giá trị 103 và 7 thực sự đáp ứng điều kiện chung $e \cdot d \mod \phi(n) = 1$ thông qua các phép tính bên dưới.


- $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Điều quan trọng là, theo *Đề xuất 4*, chúng ta biết rằng không có số nguyên nào khác giữa 1 và 360 đối với $d$ sẽ tạo ra kết quả là $103 \cdot d = 1 \mod 360$. Ngoài ra, đề xuất ngụ ý rằng việc chọn một giá trị khác cho $e$ sẽ tạo ra một giá trị duy nhất khác cho $d$.

Ở bước 5 của bài toán RSA, chúng ta phải chọn một số nguyên dương $y$ là số nguyên tố chung nhỏ hơn 403. Giả sử chúng ta đặt $y = 2^{103}$. Lũy thừa 2 với 103 sẽ cho kết quả như bên dưới.


- $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$

Bài toán RSA trong ví dụ cụ thể này hiện như sau: Bạn được cung cấp $N = 403$, $e = 103$ và $y = 349 \mod 403$. Bây giờ bạn phải tính $x$ sao cho $x^{103} = 349 \mod 403$. Nghĩa là, bạn phải tìm ra giá trị ban đầu trước khi lũy thừa 103 là 2.

Sẽ dễ dàng (ít nhất là đối với máy tính) để tính $x$ nếu chúng ta biết rằng $d = 7$. Trong trường hợp đó, bạn chỉ có thể xác định $x$ như bên dưới.


- $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$

Vấn đề là bạn chưa được cung cấp thông tin rằng $d = 7$. Tất nhiên, bạn có thể tính $d$ từ thực tế là $103 \cdot d = 1 \mod 360$. Vấn đề là bạn cũng không được cung cấp thông tin rằng bậc của $N = 360$. Cuối cùng, bạn cũng có thể tính bậc của 403 bằng cách tính tích sau: $(p - 1) \cdot (q - 1)$. Nhưng bạn cũng không được thông báo rằng $p = 13$ và $q = 31$.

Tất nhiên, máy tính vẫn có thể giải quyết bài toán RSA cho ví dụ này tương đối dễ dàng, vì các số nguyên tố liên quan không lớn. Nhưng khi các số nguyên tố trở nên rất lớn, nó phải đối mặt với một nhiệm vụ thực tế là không thể.

Bây giờ chúng ta đã trình bày bài toán RSA, một tập hợp các điều kiện mà bài toán này khó, và toán học cơ bản. Làm thế nào để tất cả những điều này giúp ích cho mật mã bất đối xứng? Cụ thể, làm thế nào chúng ta có thể biến độ khó của bài toán RSA trong một số điều kiện nhất định thành một lược đồ mã hóa hoặc lược đồ chữ ký số?

Một cách tiếp cận là lấy bài toán RSA và xây dựng các lược đồ theo cách đơn giản. Ví dụ, giả sử bạn tạo ra một tập hợp các biến $\Pi$ như mô tả trong bài toán RSA và đảm bảo rằng $p$ và $q$ đủ lớn. Bạn đặt khóa công khai của mình bằng $(N, e)$ và chia sẻ thông tin này với thế giới. Như mô tả ở trên, bạn giữ bí mật các giá trị cho $p$, $q$, $\phi(n)$ và $d$. Trên thực tế, $d$ là khóa riêng của bạn.

Bất kỳ ai muốn gửi cho bạn một tin nhắn $m$ là một phần tử của $C_N$ có thể mã hóa nó như sau: $c = m^e \mod N$. (Bản mã $c$ ở đây tương đương với giá trị $y$ trong bài toán RSA.) Bạn có thể dễ dàng giải mã tin nhắn này chỉ bằng cách tính $c^d \mod N$.

Bạn có thể thử tạo một lược đồ chữ ký số theo cùng một cách. Giả sử bạn muốn gửi cho ai đó một tin nhắn $m$ với chữ ký số $S$. Bạn chỉ cần đặt $S = m^d \mod N$ và gửi cặp $(m,S)$ cho người nhận. Bất kỳ ai cũng có thể xác minh chữ ký số chỉ bằng cách kiểm tra xem $S^e \mod N = m \mod N$ hay không. Tuy nhiên, bất kỳ kẻ tấn công nào cũng sẽ gặp khó khăn thực sự khi tạo $S$ hợp lệ cho một tin nhắn, vì chúng không sở hữu $d$.

Thật không may, việc biến một vấn đề khó khăn, vấn đề RSA, thành một lược đồ mật mã không hề đơn giản như vậy. Đối với lược đồ mã hóa đơn giản, bạn chỉ có thể chọn các số nguyên tố chung của $N$ làm thông điệp của mình. Điều đó không để lại cho chúng ta nhiều thông điệp khả thi, chắc chắn là không đủ cho giao tiếp tiêu chuẩn. Ngoài ra, những thông điệp này phải được chọn ngẫu nhiên. Điều đó có vẻ hơi không thực tế. Cuối cùng, bất kỳ thông điệp nào được chọn hai lần sẽ tạo ra cùng một bản mã chính xác. Điều này cực kỳ không mong muốn trong bất kỳ lược đồ mã hóa nào và không đáp ứng bất kỳ khái niệm tiêu chuẩn hiện đại nghiêm ngặt nào về bảo mật trong mã hóa.

Các vấn đề trở nên tệ hơn đối với chương trình chữ ký số đơn giản của chúng tôi. Theo tình hình hiện tại, bất kỳ kẻ tấn công nào cũng có thể dễ dàng làm giả chữ ký số chỉ bằng cách đầu tiên chọn một số nguyên tố $N$ làm chữ ký và sau đó tính toán thông điệp gốc tương ứng. Điều này rõ ràng phá vỡ yêu cầu về tính không thể làm giả hiện hữu.

Tuy nhiên, với việc thêm một chút phức tạp thông minh, bài toán RSA có thể được sử dụng để tạo ra một lược đồ mã hóa khóa công khai an toàn cũng như một lược đồ chữ ký số an toàn. Chúng tôi sẽ không đi sâu vào chi tiết của các cấu trúc như vậy ở đây. [4] Tuy nhiên, điều quan trọng là sự phức tạp bổ sung này không làm thay đổi vấn đề RSA cơ bản cơ bản mà các lược đồ này dựa trên.

**Lưu ý:**

[4] Xem ví dụ, Jonathan Katz và Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), trang 410–32 về mã hóa RSA và trang 444–41 về chữ ký số RSA.

# Phần kết luận

<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>

## Đánh giá & Xếp hạng

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>

<isCourseReview>true</isCourseReview>
## Bài thi cuối kỳ

<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>

<isCourseExam>true</isCourseExam>
## Phần kết luận

<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>

<isCourseConclusion>true</isCourseConclusion>