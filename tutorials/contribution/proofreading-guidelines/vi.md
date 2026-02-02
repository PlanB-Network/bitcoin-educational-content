---
name: Hướng dẫn hiệu đính
description: Những điều quan trọng cần lưu ý khi hiệu đính trên Plan ₿ Academy là gì?
---

![github](assets/cover.webp)

Chào mừng bạn đến với bài hướng dẫn này, ở đây chúng ta sẽ nói **các nguyên tắc cần tuân theo khi hiệu đính nội dung trên Plan ₿ Academy**. Chúng tôi rất vui khi bạn đồng hành cùng sứ mệnh của chúng tôi: dịch nguồn học liệu Bitcoin sang càng nhiều ngôn ngữ càng tốt, nhằm giúp mọi người hiểu cách Bitcoin hoạt động và cách nó có thể được sử dụng trong đời sống hằng ngày.

Trước hết, việc đóng góp cho [repository công khai](https://github.com/PlanB-Network/bitcoin-educational-content) của Plan ₿ Academy cho bạn cơ hội viết hướng dẫn, hiệu đính (proofreading) nội dung hiện có, hoặc thậm chí đề xuất thêm một ngôn ngữ mới vào nền tảng. Để bắt đầu, trước tiên hãy tham gia [Nhóm Telegram](https://t.me/PlanBNetwork_ContentBuilder), sau đó viết một phần giới thiệu ngắn về bản thân và các ngôn ngữ bạn có thể sử dụng.

Hướng dẫn này dành riêng cho những người đóng góp (contributor) muốn hiệu đính nội dung. Phần lớn trong số họ chưa quen với [GitHub](https://planb.academy/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) hoặc [ngôn ngữ Markdown](https://www.markdownguide.org/basic-syntax/) mà chúng tôi sử dụng trong repository, vì vậy việc chia sẻ những điểm mấu chốt của việc này là rất cần thiết.

Dưới đây, tôi đã tổng hợp những vấn đề phổ biến mà những người hiệu đính (proofreader) thường gặp. Bạn có thể thoải mái đề xuất thêm, vì điều này có thể giúp người khác cải thiện thêm.

Trước khi đi vào chi tiết, việc đầu tiên bạn cần làm là đọc tutorial hướng dẫn các thao tác thực tế trên GitHub, bao gồm fork repository của Plan ₿ Academy, commit thay đổi và gửi Pull Request (PR):

https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017


## Hiệu đính là gì?

Hiệu đính là bước rà soát cuối cùng của một văn bản nhằm phát hiện và sửa các lỗi về ngữ pháp, chính tả, dấu câu và định dạng. Mục tiêu là đảm bảo văn bản rõ ràng, mạch lạc và không có lỗi trước khi được xuất bản.

Khi thực hiện công việc này, điều quan trọng là giữ đúng ý nghĩa của bản gốc (EN hoặc FR), đồng thời đảm bảo bản dịch cuối cùng trôi chảy và tự nhiên đối với người bản ngữ.

Hãy luôn nhớ rằng dịch thuật/hiệu đính chính là GIÁO DỤC!

Mục tiêu chung của chúng ta là giúp càng nhiều người hiểu về Bitcoin càng tốt. Vì vậy, tài liệu họ đọc phải thật rõ ràng, dễ tiếp cận. 

Nghĩa là tất cả những người đóng góp của Plan ₿ Academy đều là nhà giáo dục.

## Các bước đầu tiên trước khi hiệu đính trên Plan ₿ Academy

Trước khi bắt đầu một công việc hiệu đính mới, hãy thông báo trong [nhóm Telegram](https://t.me/PlanBNetwork_ContentBuilder) hoặc thông báo cho điều phối viên Plan ₿ Academy. Người sẽ mở một [issue](https://github.com/orgs/PlanB-Network/projects/3) tương ứng. Khi nhận được liên kết đến issue, chỉ cần **bình luận rằng bạn đang bắt đầu** với công việc hiệu đính nội dung đó.

Hệ thống này giúp người điều phối theo dõi tiến độ trong repository, đồng thời “đánh dấu” nội dung đã có người phụ trách, tránh việc nhiều người làm trùng nhau.

Trong issue đã được mở, bạn sẽ thấy các liên kết dẫn tới nội dung cần kiểm tra. Bạn có thể mở trực tiếp từ đó, hoặc tốt hơn là sử dụng bản fork của chính bạn và làm việc từ đó.

Điều đầu tiên cần nhớ: **LUÔN ĐỒNG BỘ HÓA (SYNC) repository của bạn trên nhánh "dev"**. Việc này đảm bảo nội dung luôn được cập nhật trước khi bạn bắt đầu, và tránh xung đột giữa nội dung cũ và mới. Hãy nhớ nhấn vào "Sync fork" và "Update branch".

![REVIEW](assets/en/1.webp)

Sau khi đồng bộ hóa hoàn tất, bạn có thể truy cập trực tiếp vào nội dung cần hiệu đính và commit trên một nhánh mới, như trong [hướng dẫn này](https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017). Hoặc, bạn có thể tự tạo một nhánh mới để làm việc bằng vào mục "Branches", như được hiển thị bên dưới.

![REVIEW](assets/en/2.webp)

Trong trang này, bạn sẽ thấy mục “Your Branches”, liệt kê tất cả các branch bạn đã tạo. Mục này rất hữu ích vì nó cho phép bạn quản lý các công việc đang làm. Nếu muốn tạo nhánh mới, hãy nhấn “New Branch” ở góc trên bên phải.

![REVIEW](assets/en/3.webp)

Sau đó, một cửa sổ bật lên sẽ hiện ra yêu cầu bạn nhập tên nhánh mới. Trong ví dụ bên dưới, tôi chọn đặt tên nhánh là "BTC101-FR". Bằng cách này, tôi sẽ luôn nhớ rằng nhánh này cần được sử dụng để hiệu đính khóa học BTC101 bằng tiếng Pháp, và **tôi sẽ không sử dụng nhánh này cho bất kỳ công việc nào khác**.

Cứ nhớ là: Khi có một công việc mới, hãy tạo một nhánh mới.

![REVIEW](assets/en/4.webp)

Sau khi tạo nhánh mới, hãy nhấn vào nhánh đó trong mục "Your Branches" và bắt đầu làm việc trên file *.md* tương ứng với nội dung cụ thể (trong trường hợp của tôi, tôi sẽ nhấp vào "courses" -> "BTC101" -> "fr.md"). Tất cả các commit liên quan đến nội dung đó phải nằm cùng một nhánh.


## Ngôn ngữ gốc hay bản dịch?

Khi hiệu đính nội dung, **luôn luôn kiểm tra bản gốc tiếng Anh (hoặc tiếng Pháp)**. Xin lưu ý, rằng chúng tôi sử dụng công cụ AI để dịch, nên bản dịch ban đầu có thể sẽ chưa được tự nhiên hoặc khó hiểu với người đọc cuối.

Vì vậy, bạn hoàn toàn có thể điều chỉnh câu chữ, miễn là không làm sai nghĩa gốc. Mục tiêu là tăng độ trôi chảy và dễ hiểu. Nếu không chắc về cách xử lý một từ hay khái niệm, hãy hỏi điều phối viên dịch thuật.

Các công cụ LLM có thể dịch một số thuật ngữ Bitcoin theo nghĩa đen, chẳng hạn như Lightning Network. Việc này hay xảy ra với các thuật ngữ kỹ thuật. Trong những trường hợp như vậy, nên giữ nguyên từ tiếng Anh, trừ khi ngôn ngữ của bạn bắt buộc phải dịch.

Nếu buộc phải dịch, hãy *nghiên cứu xem cộng đồng Bitcoin trong ngôn ngữ đó đã có cách dịch phổ biến hay chưa*.

Sau đây là một số gợi ý

- **Kiểm tra [BitcoinWiki](https://en.bitcoin.it/wiki/Main_Page)** bằng ngôn ngữ đích của bạn mà bạn muốn hiệu đính.

- Giữ từ tiếng Anh (EN) và thêm nghĩa bằng ngôn ngữ đích trong ngoặc: EN (VI), hoặc ngược lại là VI (EN). Ví dụ: Address (indirizzo), hoặc indirizzo (địa chỉ).

- Hoặc giữ nguyên từ EN và để liên kết tới [glossary](https://planb.academy/en/resources/glossary) của Plan ₿ Academy. Để làm điều này, bạn cần chèn từ/cụm từ trong ngoặc vuông và liên kết trong ngoặc tròn, như bạn có thể thấy trong ví dụ dưới đây:

```
[UTXO](https://planb.academy/resources/glossary/utxo)
```

Và kết quả thu được sẽ như hình bên dưới, bạn có thể nhấp vào từ/cụm từ đó và được chuyển đến glassory (bảng thuật ngữ, một danh sách các từ ngữ chuyên ngành) tương ứng.

![REVIEW](assets/en/5.webp)

Lưu ý: liên kết thuật ngữ mà bạn sẽ lấy từ trang glossary sẽ chứa mã ngôn ngữ (`en`, `fr`…), hãy xóa chúng, để hệ thống tự điều hướng theo ngôn ngữ của người đọc.

Nội dung trên repository chứa rất nhiều các siêu liên kết như trên. Giờ bạn đã hiểu ý nghĩa của chúng, **hãy nhớ là không xóa bất kỳ liên kết nào** do tác giả gốc chèn vào.

Ngoài ra:

- Luôn giữ nguyên “Plan ₿ Academy”, không dịch “Plan”, không dịch "Academy”, và không dùng mạo từ “The”. **Hãy coi đó là một thương hiệu**.

- Tương tự với ₿-CERT, BIZ SCHOOL, TECH SCHOOL.

Cuối cùng, như đã nói ở trên, chúng tôi sử dụng các công cụ AI để dịch nội dung và sau đó yêu cầu sự can thiệp của những người đóng góp để đảm bảo mọi thứ đều trôi chảy và được hiệu đính kỹ lưỡng. 

Nếu bạn sử dụng AI để hiệu đính quá nhiều, chúng tôi sẽ nhận ra. Nếu gần như toàn bộ nội dung đều do AI xử lý, phần thưởng sats có thể bị giảm một nửa.


## Cấu trúc của tiêu đề

Trong ngôn ngữ markdown, tiêu đề bắt đầu bằng ký tự `#`. Số lượng dấu thăng tương ứng với cấp độ tiêu đề. Ví dụ: tiêu đề cấp ba (H3) có ba dấu thăng trước văn bản (ví dụ: `### Tiêu đề của tôi`).

- Trong các khóa học: 
    - Phần chính sẽ dùng `#`
    - Phần phụ sẽ dùng từ `##` đến `####`

- Trong các bài hướng dẫn, thường chỉ dùng `##`

![REVIEW](assets/en/6.webp)

**KHÔNG BAO GIỜ xóa dấu thăng** trước tiêu đề.

Đồng thời, **không thay đổi** phần `chapterID` mà bạn có thể thấy trong hình ảnh trên, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` hoặc các tham chiếu video như ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.

Không cần in đậm tiêu đề, vì Markdown đã tự xử lý việc đó.

Lưu ý thêm, trong phiên bản tiếng Anh của các khóa học, **tiêu đề bắt đầu bằng một hoặc hai ký tự ``#`` sẽ viết hoa chữ cái đầu**, còn các tiêu đề bắt đầu bằng ba hoặc bốn ký tự ``#`` không cần tuân theo quy tắc này. Nếu có thể, hãy đảm bảo tiêu đề bằng ngôn ngữ đích của bạn tuân theo cấu trúc này.


## Phần mở đầu của khóa học

Ở đầu bất kỳ nội dung nào, bạn sẽ thấy các từ khóa: "name", "description", "objectives". Chúng được trang web sử dụng để giải mã nội dung và **luôn được giữ nguyên ở định dạng EN**. Do đó:

- KHÔNG dịch chúng, nếu không nội dung gặp vấn đề về đồng bộ hóa.
- Chỉ hiệu đính phần nội dung sau dấu hai chấm `:`

![REVIEW](assets/en/7.webp)

- Không thêm bất cứ thứ gì vào đầu văn bản. Ví dụ: tránh thêm "tt" trước dấu gạch ngang, như trong hình bên dưới!

![REVIEW](assets/en/8.webp)


## Xử lý hình ảnh khóa học

Trang web của chúng tôi hiện có hình ảnh đã dịch cho hầu hết mọi khóa học!

Khi hiệu đính, hãy luôn kiểm tra xem tất cả hình ảnh đã có và hiển thị chính xác chưa. Trong `code view`, nếu bạn thấy dòng `![IMAGE](assets/en/001.webp)`, điều đó có nghĩa là hình ảnh sẽ được hiển thị ở vị trí đó.

Hãy đảm bảo bạn luôn thêm một dòng mới giữa mã hình ảnh và văn bản. Ví dụ:

```
SAI:
- Để bắt đầu dịch, hãy nhấp vào nút `Dịch`: ![language](assets/08.webp)
Để lưu, hãy nhấp vào `Lưu`!


ĐÚNG:

- Để bắt đầu dịch, hãy nhấp vào nút `Dịch`:

![language](assets/08.webp)

Để lưu, hãy nhấp vào `Lưu`!
```

Ngoài ra, hãy nhớ đọc kỹ nội dung của từng hình ảnh. Nếu bạn nhận thấy bất kỳ vấn đề nào với bản dịch văn bản trong hình, hãy báo cho điều phối viên của bạn và biết đâu bạn cũng sẽ có cơ hội hiệu đính chúng!

Bạn có thể xem hình ảnh trong phần `Preview` của GitHub (hoặc trên trang web của chúng tôi, mở trong một tab khác). Sau đó, quay lại phần `code` bên cạnh để kiểm tra.

![REVIEW](assets/en/9.webp)


## Đề xuất về định dạng

Dưới đây bạn có thể tìm thấy một số ví dụ về các vấn đề định dạng cần chú ý khi hiệu đính nội dung.

- Hãy chú ý đến các dấu cụm như `\*\*\` hoặc ``**``, vì chúng có thể là ký hiệu in đậm sai. Trong hình ảnh bên dưới, bạn có thể thấy các dấu sao chỉ nằm bên phải của từ, nhìn sai sai đúng không!?

![REVIEW](assets/en/10.webp)

Vì vậy, hãy luôn kiểm tra văn bản gốc bằng tiếng Anh để xem có cần in đậm hay không. Trong trường hợp này, chỉ cần thêm hai dấu sao vào đầu của từ đó để nó hiển thị chính xác trên trang web. Thực tế, trong ngôn ngữ markdown, **để in đậm, bạn phải chèn hai dấu sao ``**`` cả trước và sau từ/câu**, ví dụ:

![REVIEW](assets/en/11.webp)

- Những vấn đề tương tự có thể xảy ra với các ký hiệu như $ và `` ` ``. Hãy nhớ kiểm tra file ngôn ngữ gốc (thường là EN hoặc FR) để xem các ký hiệu này nằm ở đâu. Bạn luôn có thể yêu cầu điều phối viên hỗ trợ về vấn đề này.

- Nếu bạn thấy có trích dẫn, hãy nhớ tìm bản dịch phù hợp với ngôn ngữ của bạn. Trích dẫn thường được chèn sau ký hiệu ``>``.

![REVIEW](assets/en/12.webp)

## Hiệu đính các bài hướng dẫn

Nếu bạn quyết định hiệu đính bài hướng dẫn, điều phối viên sẽ mở một issue riêng cho **toàn bộ phần hướng dẫn**. Khi hoàn thành công, bạn có thể ghi lại tiến độ bằng cách bình luận trong issue đó kèm theo danh sách các bài hướng dẫn đã được hiệu đính: bằng cách này, bạn sẽ tạo ra một hệ thống theo dõi rõ ràng để tham khảo trong tương lai, điều này rất quan trọng vì nội dung mới được thêm vào hàng tháng. Bạn có thể xem ví dụ về cách làm này [tại đây](https://github.com/PlanB-Network/bitcoin-educational-content/issues/3023#issuecomment-3364923190).

![REVIEW](assets/en/13.webp)

Vì các bài hướng dẫn mới được thêm vào hàng tháng, nhánh bạn đang làm việc có thể trở nên lỗi thời trong quá trình hiệu đính. Một số người hiệu đính đã giải quyết vấn đề này bằng cách đồng bộ hóa chính xác nhánh mà họ đang làm việc: **Vui lòng KHÔNG BAO GIỜ làm như vậy! Nếu bạn làm vậy, bạn có nguy cơ mất tất cả tiến độ đã đạt được!**

Thay vào đó, bạn nên hoàn thành việc hiệu đính các bài hướng dẫn trong nhánh hiện tại của mình trước. Sau đó, **đồng bộ hóa `dev`** và tạo một nhánh mới, nơi bạn tập trung vào việc hiệu đính các bài hướng dẫn mới được thêm vào (chỉ những bài còn thiếu trong nhánh trước đó).

Trong các bài hướng dẫn, có khả năng **hình ảnh có thể không được dịch**. Vì hầu hết các bài hướng dẫn **ban đầu được viết bằng tiếng Pháp hoặc tiếng Anh**, bạn có thể sẽ tìm thấy các hình ảnh chứa câu lệnh hoặc hướng dẫn bằng ngôn ngữ gốc. Hãy lấy ví dụ từ bài hướng dẫn về Sparrow bằng tiếng Hà Lan, bằng cách trình bày cả văn bản và hình ảnh liên quan.

```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Publieke server_".
```

![REVIEW](assets/en/14.webp)

Như bạn có thể thấy, hình ảnh rõ ràng chỉ đến `Public Server` bằng tiếng Anh, trong khi văn bản lại đề cập đến cụm từ `_Publieke server_`. Trong trường hợp này, có vấn đề về tính mạch lạc, vì người đọc thấy thông tin mâu thuẫn khi so sánh hình ảnh với văn bản.

Để giải quyết vấn đề này, bạn có thể chèn lệnh như trong hình (tiếng Anh hoặc tiếng Pháp), sau đó là bản dịch sang ngôn ngữ của bạn trong ngoặc đơn, ví dụ:

```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Public Server_" (Publieke server).
```

## Hiệu đính bài kiểm tra

Bạn có biết rằng bạn cũng có thể hiệu đính các câu hỏi trắc nghiệm trong mọi khóa học không? Ví dụ, nếu bạn muốn hiệu đính các bài kiểm tra cho môn BTC101 trong ngành CNTT, bạn có thể tạo một nhánh riêng và làm theo đường dẫn này: "courses" -> "BTC101" -> "quiz". Ở đó, bạn sẽ tìm thấy tất cả các thư mục dành cho mỗi câu hỏi, cùng với file ngôn ngữ liên quan ở định dạng _yml_.

Một lần nữa, hãy đảm bảo bạn đang ở trong một nhánh riêng mà bạn mở chỉ dành cho mục đích này, và luôn thông báo cho người điều phối.

Một điều quan trọng cần ghi nhớ khi hiệu đính loại file _yml_ này là tránh thêm dấu hai chấm ``:`` hoặc dấu ngoặc kép vào trong văn bản. Trên thực tế, dấu hai chấm **chỉ** được sử dụng để phân tách các cặp khóa-giá trị như "wrong_answers" với phần còn lại. Bạn có thể xem ví dụ trong hình bên dưới:

![REVIEW](assets/en/15.webp)

Sau khi kiểm tra lại các câu hỏi, hãy đảm bảo bạn đổi trạng thái của khóa "reviewed" từ "false" thành "true", như trong hình bên dưới. Hãy đảm bảo **giữ nguyên các từ chỉ trạng thái này bằng tiếng Anh**, bất kể bạn đang làm việc với ngôn ngữ nào!

![REVIEW](assets/en/16.webp)

Nếu dòng trạng thái "reviewed:true" bị thiếu, hãy nhớ **thêm dòng này vào cuối bài kiểm tra**.

## Hiệu đính thuật ngữ (glassory)

Giống như bài kiểm tra, bạn cũng có thể hiệu đính phần chú giải thuật ngữ. Bản gốc của phần chú giải thuật ngữ được viết bằng tiếng Pháp, vì vậy bạn sẽ thấy những câu như: "Trong tiếng Pháp, cụm từ này có thể được dịch thành..."

Trong những trường hợp như vậy, hãy điều chỉnh câu sang ngôn ngữ đích hoặc tiếng Việt. Ví dụ, bạn có thể viết "Trong tiếng Việt, cụm từ này...".

Nếu tiêu đề được để bằng tiếng Anh, bạn có thể điều chỉnh câu sang ngôn ngữ của mình: "Trong tiếng Swahili, thành ngữ này..."

Ngoài ra, hãy nhớ viết tiêu đề bằng CHỮ IN HOA.

![REVIEW](assets/en/17.webp)


## Tiêu đề và mô tả Pull Request (PR) của bạn

Khi bạn gửi PR, sẽ thật tuyệt nếu bạn đặt tên theo định dạng này: [PROOFREADING] TÊN NỘI DUNG - NGÔN NGỮ:

```
[PROOFREADING] BTC101 - VIETNAMESE
```

Ngoài ra, trong **phần bình luận của PR**, bạn có thể viết "closes" + số của issue mà người điều phối đã gửi cho bạn khi bạn bắt đầu nhiệm vụ hiệu đính, bắt đầu bằng ``#``.

Ví dụ, nếu bạn vừa gửi PR kèm theo bản hiệu đính của cyp201 + bài kiểm tra, bạn có thể viết "closes [#2934](https://github.com/PlanB-Network/bitcoin-educational-content/issues/2934)".

Bằng cách này, PR và issue sẽ được liên kết với nhau và bất kỳ ai khi xem repository công khai trên Github đều có thể dễ dàng tìm thấy thông tin.


## Các phương pháp hay nhất khác

- Nếu bạn cần tìm kiếm các từ cụ thể trong văn bản, bạn có thể nhấn ``CTRL+F`` và mục tìm kiếm-thay thế sẽ xuất hiện. Tính năng này rất hữu ích khi bạn cần chuyển đến một phần cụ thể của văn bản, hoặc cần thay thế hàng loạt các từ/câu cụ thể mà không cần cuộn toàn bộ nội dung.


![REVIEW](assets/en/18.webp)


Khi sử dụng chức năng "thay thế tất cả", nhớ là phải kiểm tra lại kết quả để đảm bảo các liên kết không bị thay đổi. Ví dụ: nếu bạn muốn đổi từ "Bitcoin" thành "Bitkoin" (điều này có thể cần thiết trong một số ngôn ngữ), việc sử dụng chức năng "thay thế tất cả" có thể cập nhật hiệu quả tất cả các trường hợp trong văn bản. Tuy nhiên, hãy lưu ý rằng công cụ này cũng sẽ sửa đổi bất kỳ liên kết nào chứa từ đó, có khả năng dẫn đến các vấn đề chuyển hướng trang web.

Trong ví dụ dưới đây, người hiệu đính đã sử dụng hàm trên để thay thế "satoshi" bằng "satoshi (sats)", đồng thời thay đổi liên kết đến một bài hướng dẫn có chứa từ này. Kết quả là liên kết trở nên không hợp lệ.

Luôn kiểm tra lại tất cả các siêu liên kết trong văn bản.

![REVIEW](assets/en/19.webp)


- Tiếp theo, nếu tác giả chèn liên kết đến khóa học hoặc bài hướng dẫn của Plan ₿ Academy (**không** nằm trong dấu ngoặc đơn), trang web sẽ tự động tạo một "thẻ" hiển thị hình thu nhỏ liên quan. Do đó, hãy luôn đảm bảo **thêm một dòng mới giữa văn bản và liên kết**, nếu không bạn có thể thấy lỗi sau trên trang web.


![REVIEW](assets/en/20.webp)


## Phần kết luận

Tóm lại, việc nhận biết những lỗi thường gặp của người hiệu đính có thể giúp bạn nâng cao kỹ năng kiểm tra nội dung. Chúng ta rất dễ bỏ qua những yếu tố như ngữ cảnh hoặc tính nhất quán, và việc phát hiện ra những lỗi này có thể tạo ra sự khác biệt lớn.

Hãy luôn nhớ rằng người mới bắt đầu có thể đọc các khóa học và hướng dẫn này, vì vậy chúng ta có trách nhiệm đảm bảo họ hiểu đủ và đúng. **Là người hiệu đính, bạn cũng là một nhà giáo dục!**

Bây giờ bạn đã sẵn sàng bắt đầu hiệu đính các khóa học, hướng dẫn, bài kiểm tra và thuật ngữ. Hãy tiếp tục theo dõi để hiệu đính cả bản ghi video (video transcripts) nữa nhé!

Cảm ơn bạn đã đọc hướng dẫn này và chúc bạn có một hành trình hiệu đính tuyệt vời!