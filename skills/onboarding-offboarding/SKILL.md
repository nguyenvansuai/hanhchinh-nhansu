---
name: onboarding-offboarding
description: Tiếp nhận nhân viên mới và làm thủ tục nghỉ việc trọn gói cho phòng HCNS doanh nghiệp Việt Nam — danh mục hồ sơ cá nhân (không giữ bản gốc giấy tờ), mã số thuế cá nhân theo số định danh, đăng ký người phụ thuộc, báo tăng BHXH, cấp tài khoản – tài sản – thẻ, lịch hội nhập tuần đầu và mục tiêu 30-60-90 ngày, người kèm cặp; khi nghỉ việc: tính ngày nghỉ hợp lệ theo thời hạn báo trước, biên bản bàn giao công việc – tài sản – tài khoản, thu hồi quyền truy cập, thanh toán lương – phép chưa nghỉ – trợ cấp thôi việc trong 14 ngày làm việc, báo giảm và chốt sổ BHXH, chứng từ khấu trừ thuế TNCN, phỏng vấn nghỉ việc. Dùng khi người dùng nói "nhân viên mới vào làm cần chuẩn bị gì", "checklist onboarding", "kế hoạch hội nhập", "nhân viên xin nghỉ việc", "thủ tục nghỉ việc", "biên bản bàn giao", "chốt sổ bảo hiểm", "tính tiền cho người nghỉ việc".
---

# Onboarding – Offboarding

Đọc trước: `references/nguyen-tac-chung.md`, `references/quy-dinh-lao-dong-2026.md`, `references/checklist-vao-ra.md`.

## A. Onboarding (nhân viên mới)

**1. Trước ngày đầu (T-7 → T-1)** – checklist `references/checklist-vao-ra.md` mục A. Lập bảng việc theo người phụ trách (HCNS, IT, quản lý trực tiếp, kế toán).

**2. Hồ sơ nhân viên**
- Nhận **bản sao** CCCD, văn bằng; **không giữ bản chính** (Điều 17 BLLĐ).
- Mã số thuế cá nhân: dùng số định danh cá nhân (số CCCD) thay MST [Chắc chắn – từ 01/7/2025]; mã số BHXH gắn với số định danh [Cần kiểm tra thủ tục cụ thể].
- Người phụ thuộc: hướng dẫn đăng ký giảm trừ (bộ kế toán xử lý tờ khai).
- Xin đồng ý xử lý dữ liệu cá nhân (điều khoản trong HĐLĐ hoặc văn bản riêng).

**3. Ngày đầu & tuần đầu** – lịch hội nhập (mẫu mục B): giới thiệu, nội quy, an toàn lao động (huấn luyện ATVSLĐ bắt buộc với NLĐ mới theo Luật ATVSLĐ), công cụ, buổi 1-1 với quản lý.

**4. Mục tiêu 30-60-90 ngày** – 2–4 mục tiêu đo được cho mỗi mốc, gắn với JD; mốc đánh giá thử việc trùng ngày kết thúc thử việc (tính bằng `ngay_lam_viec`/`cong_ngay_lich`).

**5. Thủ tục**: ký HĐLĐ (skill `hop-dong-lao-dong`), báo tăng BHXH trong tháng, cập nhật sổ quản lý lao động.

## B. Offboarding (nghỉ việc)

**1. Xác định trường hợp** → căn cứ và giấy tờ khác nhau: NLĐ xin nghỉ (Điều 35) · thỏa thuận chấm dứt (Điều 34.3) · hết hạn HĐ (Điều 34.1) · NSDLĐ chấm dứt (Điều 36) · sa thải (kỷ luật). Trường hợp có tranh chấp/sa thải → skill `cham-dut-hop-dong`, `ky-luat-lao-dong`.

**2. Ngày nghỉ hợp lệ** – `thoi_han_bao_truoc` (ben=nguoi_lao_dong, loại HĐ, ngày nộp đơn). Nghỉ sớm hơn mà công ty đồng ý → ghi rõ "thỏa thuận chấm dứt".

**3. Bàn giao** – biên bản (mẫu mục C): công việc dở dang, tài liệu, tài sản (mã), tài khoản (chỉ ghi tên tài khoản – **không ghi mật khẩu** vào biên bản), khách hàng/đối tác đang phụ trách.

**4. Thu hồi quyền truy cập** ngay ngày làm việc cuối: email, phần mềm, Drive, chữ ký số được ủy quyền, thẻ ra vào; chuyển tiếp email theo quy chế.

**5. Thanh toán trong 14 ngày làm việc** kể từ ngày chấm dứt (tối đa 30 ngày khi luật định – Điều 48):
- Lương đến ngày nghỉ; phép năm chưa nghỉ (số ngày bằng `phep_nam`, trừ ngày đã nghỉ) × lương ngày.
- Trợ cấp thôi việc (nếu thuộc diện): `tro_cap_thoi_viec` – thường chỉ phát sinh với thời gian chưa đóng BHTN (thử việc, giai đoạn trước 2009...).
- Các khoản khấu trừ hợp pháp (tạm ứng, bồi thường theo quy trình) – không khấu trừ quá 30% lương tháng nếu khấu trừ vào lương.
- Ngày thanh toán chậm nhất: `ngay_lam_viec` (so_ngay=14 từ ngày chấm dứt).

**6. BHXH & thuế**: báo giảm lao động; hoàn thành thủ tục xác nhận thời gian đóng BHXH và trả lại giấy tờ bản chính đã giữ (nếu có) cho NLĐ (Điều 48); cấp chứng từ khấu trừ thuế TNCN nếu NLĐ yêu cầu (kế toán). Hướng dẫn NLĐ nộp hồ sơ trợ cấp thất nghiệp trong **03 tháng** kể từ ngày chấm dứt HĐ (Luật Việc làm 2025) [Chắc chắn].

**7. Quyết định/thỏa thuận chấm dứt** – mẫu trong skill `cham-dut-hop-dong`.

**8. Phỏng vấn nghỉ việc** – 6–8 câu hỏi (mục D); tổng hợp lý do nghỉ theo quý.

## Đầu ra
Checklist có người phụ trách + hạn · lịch hội nhập · mục tiêu 30-60-90 · biên bản bàn giao · bảng tính thanh toán khi nghỉ (kèm căn cứ) · nhắc hạn BHXH.

<!-- KET-NOI:BAT-DAU (sinh tự động từ scripts/ket_noi.json – sửa ở đó rồi chạy build) -->
## Kết nối ứng dụng

Connector dùng cho skill này: **Google Calendar** · **Gmail** · **Google Drive** · **Slack** · **Microsoft 365 (Outlook, OneDrive/SharePoint, Teams)**. Đọc quy tắc trong `references/ket-noi.md` trước khi dùng.

1. Nhân viên mới: tạo lịch hội nhập tuần đầu (gặp quản lý, đào tạo, nhận thiết bị) trên lịch các bên – sau khi xác nhận.
2. Tạo nháp email chào mừng, thư thông báo cho IT, kế toán cấp tài khoản, thiết bị; lập thư mục hồ sơ nhân viên trên Drive.
3. Đăng tin chào mừng lên kênh chung (Slack/Teams) sau khi xác nhận nội dung.
4. Nghỉ việc: tạo nhắc hạn thanh toán trong 14 ngày làm việc, nháp email biên bản bàn giao, xác nhận thu hồi tài khoản.

**Khi chưa kết nối:** làm đủ phần soạn thảo, tính toán; đưa nội dung sẵn để người dùng tự dán vào email, lịch, thư mục; nhắc **một lần** cách bật connector, không dừng việc chỉ vì chưa kết nối.
<!-- KET-NOI:KET-THUC -->
