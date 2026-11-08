"""Lịch nghĩa vụ định kỳ của phòng HCNS và xuất file .ics (nhập Google Calendar, Outlook, điện thoại)."""
import os
import uuid
from datetime import date, datetime, timedelta

from . import lich_vn

# (tháng, ngày, tên, căn cứ, ghi chú, nhãn) – hạn "trước ngày X" lưu ngày X-1
NGHIA_VU_NAM = [
    (1, 9, "Báo cáo công tác an toàn, vệ sinh lao động năm trước", "Luật ATVSLĐ 2015 và văn bản hướng dẫn",
     "Hạn thường gặp: trước 10/01 – đối chiếu hướng dẫn hiện hành", "Cần kiểm tra"),
    (3, 31, "Quyết toán thuế TNCN thay người lao động (phối hợp kế toán)", "Luật Quản lý thuế",
     "Ngày cuối tháng thứ 3 sau năm; trùng ngày nghỉ lùi sang ngày làm việc tiếp theo", "Chắc chắn"),
    (6, 4, "Báo cáo tình hình thay đổi lao động 6 tháng đầu năm (Mẫu 01/PLI)", "Khoản 2 Điều 4 NĐ 145/2020",
     "Nộp trước 05/6 qua Cổng Dịch vụ công quốc gia → Sở Nội vụ", "Chắc chắn"),
    (12, 4, "Báo cáo tình hình thay đổi lao động năm (Mẫu 01/PLI)", "Khoản 2 Điều 4 NĐ 145/2020",
     "Nộp trước 05/12 qua Cổng Dịch vụ công quốc gia → Sở Nội vụ", "Chắc chắn"),
]

NHAC_NOI_BO = [
    (1, 15, "Chốt phương án nghỉ Tết âm lịch và thông báo NLĐ (trước ít nhất 30 ngày)", "NĐ 145/2020"),
    (2, 28, "Rà soát HĐLĐ hết hạn trong quý II – thông báo trước 15 ngày nếu không gia hạn", "Điều 45 BLLĐ 2019"),
    (3, 15, "Tổ chức hội nghị người lao động / đối thoại định kỳ năm", "Điều 63 BLLĐ 2019"),
    (5, 31, "Rà soát HĐLĐ hết hạn trong quý III", "Điều 45 BLLĐ 2019"),
    (6, 20, "Chuẩn bị mức đóng BHXH mới nếu lương cơ sở/lương tối thiểu thay đổi từ 01/7", "Luật BHXH 2024"),
    (8, 31, "Rà soát HĐLĐ hết hạn trong quý IV", "Điều 45 BLLĐ 2019"),
    (11, 15, "Lập kế hoạch khám sức khỏe định kỳ, huấn luyện ATVSLĐ năm sau", "Luật ATVSLĐ 2015"),
    (11, 30, "Rà soát HĐLĐ hết hạn trong quý I năm sau; rà nội quy, quy chế theo luật mới", "Điều 45 BLLĐ 2019"),
    (12, 15, "Cập nhật lịch nghỉ lễ Tết năm sau; phương án nghỉ Tết", "Điều 112 BLLĐ 2019"),
]


def _lui_ngay_lam_viec(d, nghi_thu_bay=True):
    nghi_tuan = (5, 6) if nghi_thu_bay else (6,)
    nghi, lam_bu = lich_vn.tap_ngay_nghi(d.year, d.year, nghi_tuan)
    while not lich_vn.la_ngay_lam_viec(d, nghi, lam_bu, nghi_tuan):
        d += timedelta(days=1)
    return d


def _ics(su_kien, ten_lich):
    def esc(s):
        return str(s).replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")
    dong = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//hanhchinh-nhansu//VI", "CALSCALE:GREGORIAN",
            f"X-WR-CALNAME:{esc(ten_lich)}", "X-WR-TIMEZONE:Asia/Ho_Chi_Minh"]
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    for s in su_kien:
        d = lich_vn._ngay(s["ngay"])
        dong += ["BEGIN:VEVENT", f"UID:{uuid.uuid4()}@hcns", f"DTSTAMP:{stamp}",
                 f"DTSTART;VALUE=DATE:{d.strftime('%Y%m%d')}",
                 f"DTEND;VALUE=DATE:{(d + timedelta(days=1)).strftime('%Y%m%d')}",
                 f"SUMMARY:{esc(s['ten'])}", f"DESCRIPTION:{esc(s.get('mo_ta', ''))}"]
        for truoc in s.get("nhac_truoc_ngay", [7, 1]):
            dong += ["BEGIN:VALARM", "ACTION:DISPLAY", f"DESCRIPTION:{esc(s['ten'])}",
                     f"TRIGGER:-P{int(truoc)}D", "END:VALARM"]
        dong.append("END:VEVENT")
    dong.append("END:VCALENDAR")
    return "\r\n".join(_gap(x) for x in dong) + "\r\n"


def _gap(dong, toi_da=75):
    """Gấp dòng dài theo RFC 5545 (≤ 75 byte/dòng, dòng tiếp bắt đầu bằng dấu cách), không cắt giữa ký tự UTF-8."""
    if len(dong.encode("utf-8")) <= toi_da:
        return dong
    phan, hien_tai = [], ""
    for ch in dong:
        gioi_han = toi_da if not phan else toi_da - 1
        if len((hien_tai + ch).encode("utf-8")) > gioi_han:
            phan.append(hien_tai)
            hien_tai = ch
        else:
            hien_tai += ch
    phan.append(hien_tai)
    return "\r\n ".join(phan)


def lich_tuan_thu_hcns(nam, nghi_thu_bay=True, them_nhac_noi_bo=True, su_kien_them=None, xuat_ics=""):
    nam = int(nam)
    ds = []
    for th, ng, ten, can_cu, ghi_chu, nhan in NGHIA_VU_NAM:
        d0 = date(nam, th, ng)
        d = _lui_ngay_lam_viec(d0, nghi_thu_bay) if "Quyết toán" in ten else d0
        ds.append({"ngay": d.isoformat(), "ten": ten, "loai": "Nghĩa vụ pháp lý",
                   "mo_ta": f"{ghi_chu}. Căn cứ: {can_cu}. [{nhan}]"})
    le, bu = lich_vn.ngay_le(nam, nghi_tuan=(5, 6) if nghi_thu_bay else (6,))
    for d, t in le + bu:
        ds.append({"ngay": d.isoformat(), "ten": f"Nghỉ: {t}", "loai": "Ngày nghỉ", "mo_ta": "Điều 112 BLLĐ 2019",
                   "nhac_truoc_ngay": [14]})
    if them_nhac_noi_bo:
        for th, ng, ten, can_cu in NHAC_NOI_BO:
            ds.append({"ngay": date(nam, th, ng).isoformat(), "ten": ten, "loai": "Nhắc việc nội bộ",
                       "mo_ta": f"Căn cứ: {can_cu}"})
    for s in su_kien_them or []:
        ds.append({"ngay": lich_vn._ngay(s["ngay"]).isoformat(), "ten": s["ten"], "loai": s.get("loai", "Thêm"),
                   "mo_ta": s.get("mo_ta", "")})
    ds.sort(key=lambda x: x["ngay"])
    kq = {"nam": nam, "so_su_kien": len(ds),
          "lich": [{"ngay": lich_vn._fmt(lich_vn._ngay(x["ngay"])), "viec": x["ten"], "loai": x["loai"], "ghi_chu": x["mo_ta"]}
                   for x in ds],
          "luu_y": "BHXH báo tăng/giảm phát sinh hằng tháng; HĐLĐ hết hạn tính theo danh sách nhân viên – thêm qua su_kien_them."}
    if xuat_ics:
        os.makedirs(os.path.dirname(os.path.abspath(xuat_ics)), exist_ok=True)
        with open(xuat_ics, "w", encoding="utf-8", newline="") as f:
            f.write(_ics(ds, f"Lịch tuân thủ HCNS {nam}"))
        kq["file_ics"] = os.path.abspath(xuat_ics)
    return kq


def tao_file_ics(duong_dan_ra, su_kien, ten_lich="Lịch công việc"):
    with open(duong_dan_ra, "w", encoding="utf-8", newline="") as f:
        f.write(_ics(su_kien, ten_lich))
    return {"da_tao": os.path.abspath(duong_dan_ra), "so_su_kien": len(su_kien),
            "huong_dan": "Google Calendar: Cài đặt → Nhập và xuất → Nhập. Outlook: File → Open & Export → Import/Export."}


TOOLS = [
    {"name": "lich_tuan_thu_hcns", "fn": lich_tuan_thu_hcns,
     "description": "Lập lịch nghĩa vụ định kỳ cả năm của phòng HCNS (báo cáo tình hình lao động 05/6, 05/12; báo cáo ATVSLĐ; "
                    "quyết toán TNCN; ngày nghỉ lễ Tết; nhắc rà HĐLĐ hết hạn, đối thoại định kỳ...) và xuất file .ics có nhắc trước.",
     "schema": {"type": "object", "required": ["nam"], "properties": {
         "nam": {"type": "integer"}, "nghi_thu_bay": {"type": "boolean"}, "them_nhac_noi_bo": {"type": "boolean"},
         "su_kien_them": {"type": "array", "items": {"type": "object", "properties": {
             "ngay": {"type": "string"}, "ten": {"type": "string"}, "mo_ta": {"type": "string"}}}},
         "xuat_ics": {"type": "string", "description": "Đường dẫn file .ics cần tạo"}}}},
    {"name": "tao_file_ics", "fn": tao_file_ics,
     "description": "Tạo file lịch .ics từ danh sách sự kiện (ngày, tên, mô tả, số ngày nhắc trước) – ví dụ hạn HĐLĐ, lịch phỏng vấn, "
                    "kết luận cuộc họp – để nhập vào Google Calendar/Outlook.",
     "schema": {"type": "object", "required": ["duong_dan_ra", "su_kien"], "properties": {
         "duong_dan_ra": {"type": "string"}, "ten_lich": {"type": "string"},
         "su_kien": {"type": "array", "items": {"type": "object", "required": ["ngay", "ten"], "properties": {
             "ngay": {"type": "string"}, "ten": {"type": "string"}, "mo_ta": {"type": "string"},
             "nhac_truoc_ngay": {"type": "array", "items": {"type": "integer"}}}}}}}},
]
