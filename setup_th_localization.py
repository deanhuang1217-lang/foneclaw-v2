#!/usr/bin/env python3
from pathlib import Path
import re, ast, json, datetime, textwrap, shutil
base=Path('/home/administrator/clawfone-v2')

# 1) Thai translations
TH_TRANSLATIONS = {
 'homepage': {
  'meta_title':'FoneClaw — ผู้ช่วย AI สำหรับ Android | สั่งงานเสียง 120+ รายการ',
  'meta_desc':'FoneClaw คือผู้ช่วย AI สำหรับ Android ที่สั่งงานมือถือได้จริงด้วยเสียง รองรับงาน 120+ รายการใน 16 หมวด เช่น สถานะเครื่อง ข้อความ การตั้งค่า ภาพหน้าจอ นำทาง และงานเว็บ',
  'hero_slogan':'พูดแล้ว ให้มือถือทำ',
  'hero_lead':'สั่งงานมือถือได้ 120+ รายการด้วยเสียงครั้งเดียว ฟีเจอร์หลักใช้งานได้ฟรี FoneClaw คือผู้ช่วย AI สำหรับ Android ที่ลงมือควบคุมมือถือจริง ไม่ใช่แค่ตอบคำถาม',
  'cta_download':'ดาวน์โหลด APK','cta_copy':'ดาวน์โหลดฟรี รับเวอร์ชัน Android ล่าสุด','cta_see_features':'ดูฟีเจอร์ →',
  'scenario_title':'สามเรื่องที่มือถือควรช่วยทำแทนคุณ','scenario_desc':'FoneClaw ช่วยจัดการงานมือถือประจำวันที่กินเวลาและมักต้องกดหลายขั้นตอน',
  'scenario_1_title':'สรุปรายวัน','scenario_1_desc':'สรุป SMS การแจ้งเตือน และข้อมูลระบบตามผู้ติดต่อและเวลา เพื่อให้เห็นเรื่องสำคัญโดยไม่ต้องไล่เปิดทุกแอป',
  'scenario_2_title':'สุขภาพมือถือ','scenario_2_desc':'ตรวจแบตเตอรี่ พื้นที่เก็บข้อมูล เครือข่าย และความเสี่ยงด้านสิทธิ์ในรายงานเสียงเดียว ไม่ต้องขุดหาในเมนู Android',
  'scenario_3_title':'ทริกเกอร์อัตโนมัติ','scenario_3_desc':'เมื่อถ่ายภาพหน้าจอหรือรูปภาพในแอปใด FoneClaw ตรวจจับและเสนอคำสรุปได้ทันที โดยไม่ต้องสลับบริบท',
  'stat_categories':'หมวดฟีเจอร์','stat_actions':'การทำงานที่รองรับ','stat_free':'ฟีเจอร์หลัก','stat_android':'การทำงานระดับระบบ',
  'articles_title':'บทวิเคราะห์ FoneClaw เชิงลึก','articles_desc':'อ่านคู่มือล่าสุดเกี่ยวกับการสั่งงาน Android ด้วยเสียงและผู้ช่วย AI บนมือถือ',
  'bottom_cta_title':'120+ การทำงาน ทดลองใช้ฟรี','bottom_cta_desc':'ดาวน์โหลด FoneClaw แล้วทดสอบการทำงาน Android ที่รองรับด้วยเสียง',
  'footer_slogan':'FoneClaw คือผู้ช่วย AI สำหรับ Android ที่ลงมือควบคุมมือถือจริง ไม่ใช่แค่ตอบคำถาม'
 },
 'features': {
  'meta_title':'ฟีเจอร์ FoneClaw — ผู้ช่วย AI สำหรับ Android',
  'meta_desc':'สำรวจฟีเจอร์ FoneClaw มากกว่า 120 รายการใน 16 หมวดสำหรับ Android: สถานะมือถือ ข้อความ การตั้งค่า ภาพหน้าจอ อีเมล ปฏิทิน แผนที่ และงานเว็บ',
  'hero_title':'120+ การทำงานบนมือถือ ในคำสั่งเสียงเดียว','hero_lead':'FoneClaw แปลงความสามารถของ Android ให้เป็นคำสั่งภาษาธรรมชาติ ตั้งแต่สถานะเครื่อง ข้อความ การตั้งค่า ภาพหน้าจอ การนำทาง และอื่นๆ',
  'cta_download':'ดาวน์โหลด APK','cta_copy':'ดาวน์โหลดฟรี รับเวอร์ชัน Android ล่าสุด','cta_explore':'สำรวจฟีเจอร์'
 },
 'features_showcase': {
  'cat_title':'16 หมวดฟีเจอร์ มากกว่า 120 การทำงาน','cat_desc':'ทุกความสามารถถูกจัดตามสิ่งที่ผู้ใช้ต้องการทำบนมือถือ บางฟีเจอร์ตั้งค่าแล้วใช้ได้ทันที บางฟีเจอร์ต้องให้สิทธิ์ก่อน',
  'cmd_title':'แปดคำสั่งที่ทำให้เห็นภาพสินค้า','cmd_desc':'แต่ละคำสั่งให้ผลลัพธ์ที่มองเห็นได้บนมือถือ เช่น รายงานสถานะ สรุปข้อมูล เปลี่ยนการตั้งค่า อ่านภาพหน้าจอ ตำแหน่ง หรือการนำทาง',
  'trust_title':'สิทธิ์ การตั้งค่า และการควบคุมโดยผู้ใช้','trust_desc':'FoneClaw ใช้สิทธิ์ Android เพื่อทำงานบนมือถือจริง ความไว้วางใจและการยืนยันจึงเป็นส่วนหนึ่งของประสบการณ์',
  'faq_title':'คำถามที่พบบ่อย','bottom_cta_title':'พร้อมลองผู้ช่วยมือถือที่ลงมือทำจริงหรือยัง','bottom_cta_desc':'ดาวน์โหลด FoneClaw แล้วทดสอบการทำงาน Android 120+ รายการ พร้อมสิทธิ์ที่โปร่งใสและการยืนยันก่อนงานสำคัญ'
 },
 'features_sections': {
  'eyebrow_phone':'สถานะมือถือ','show1_title':'รู้ว่าเกิดอะไรขึ้นบนมือถือของคุณ','show1_desc':'เปลี่ยนข้อมูลสุขภาพเครื่องให้เป็นรายงานที่อ่านเข้าใจ แทนการค้นหาในหน้าตั้งค่าหลายชั้น','show1_b1':'หน่วยความจำ พื้นที่ แบตเตอรี่ และสถานะเครือข่าย','show1_b2':'ตรวจสิทธิ์แอปและสิทธิ์อ่อนไหว','show1_b3':'ตรวจสัญญาณแอปที่ทำงานและแอปที่ซ่อนอยู่',
  'eyebrow_messages':'ข้อความและการแจ้งเตือน','show2_title':'เปลี่ยนเสียงรบกวนจากมือถือเป็นสรุปรายวัน','show2_desc':'FoneClaw สรุป SMS การแจ้งเตือน และข้อมูลระบบ เพื่อไม่ให้เรื่องสำคัญจมอยู่ในหลายแอป','show2_b1':'สรุป SMS ตามผู้ติดต่อและเวลา','show2_b2':'ค้นหาข้อมูลตามหัวข้อ','show2_b3':'ดูบริบทและทำเครื่องหมายว่าเรียบร้อย',
  'eyebrow_controls':'การควบคุม','show3_title':'เปลี่ยนการตั้งค่า Android ได้เร็วขึ้น','show3_desc':'ใช้ภาษาธรรมชาติสำหรับการตั้งค่า Android ที่รองรับ แทนการกดเข้าเมนูลึก','show3_b1':'ความสว่าง ปรับสว่างอัตโนมัติ เวลาหน้าจอ และการหมุนจอ','show3_b2':'เสียงสื่อ เสียงเรียกเข้า การแจ้งเตือน นาฬิกาปลุก โทรศัพท์ และระบบ','show3_b3':'โหมดเงียบ ห้ามรบกวน ไฟฉาย และการตั้งค่าระบบ',
  'eyebrow_productivity':'งานและการนำทาง','show4_title':'จากความตั้งใจไปสู่ผลลัพธ์บนมือถือ','show4_desc':'FoneClaw จัดการอีเมลที่ตั้งค่าไว้ ปฏิทิน นาฬิกาปลุก โน้ต ตำแหน่ง การค้นหารอบตัว แผนที่ และงานเว็บ','show4_b1':'อีเมลต้องตั้งค่า IMAP/SMTP','show4_b2':'การนำทางต้องมีแอปแผนที่ติดตั้ง','show4_b3':'การเปรียบเทียบเว็บใช้ข้อมูลออนไลน์ ราคาอาจไม่เรียลไทม์',
  'eyebrow_connectivity':'การเชื่อมต่อ','show5_title':'ควบคุม Wi-Fi และ Bluetooth ด้วยเสียง','show5_desc':'จัดการการเชื่อมต่อไร้สายโดยไม่ต้องค้นหาในตั้งค่า Android: สแกน เชื่อมต่อ จับคู่ และลืมเครือข่าย','show5_b1':'Wi-Fi: สแกนเครือข่ายใกล้เคียง เชื่อมต่อ ลืม และดูเครือข่ายที่บันทึก','show5_b2':'Bluetooth: จับคู่ เชื่อมต่อ ดูอุปกรณ์ที่จับคู่และเชื่อมต่อ','show5_b3':'ใช้ได้กับหูฟัง ลำโพง รถ และอุปกรณ์สวมใส่',
  'eyebrow_passive':'ทริกเกอร์อัตโนมัติ','show6_title':'FoneClaw ทำงานได้แม้ไม่ได้เปิดแอป','show6_desc':'เมื่อคุณถ่ายภาพหน้าจอหรือรูปในแอปใด FoneClaw ตรวจจับและเสนอการสรุปเนื้อหา','show6_b1':'ตรวจจับภาพหน้าจอและสรุปอัตโนมัติ','show6_b2':'ตรวจจับรูปภาพและวิเคราะห์เนื้อหา','show6_b3':'หน้าต่างลอยไม่รบกวนการใช้งาน','show6_b4':'ต้องมีสิทธิ์ตรวจจับและแสดงทับหน้าจอ',
  'trust1_title':'สิทธิ์ที่โปร่งใส','trust1_b1':'Accessibility สำหรับอ่านหน้าจอและกดองค์ประกอบ','trust1_b2':'การเข้าถึงการแจ้งเตือนสำหรับสรุปแจ้งเตือน','trust1_b3':'รายชื่อ SMS ตำแหน่ง กล้อง Bluetooth หน้าต่างลอย และสิทธิ์ตั้งค่าระบบ','trust2_title':'ยืนยันก่อนงานสำคัญ','trust2_desc':'การโทร ส่ง SMS ส่งอีเมล ลบข้อมูล และงานอ่อนไหวอื่นต้องได้รับการยืนยันจากผู้ใช้','trust3_title':'ข้อกำหนดการตั้งค่าชัดเจน','trust3_desc':'อีเมลต้องตั้งค่า IMAP/SMTP แผนที่ต้องมีแอปนำทาง และการตรวจภาพหน้าจอต้องมีสิทธิ์หน้าต่างลอย',
  'faq1_q':'FoneClaw ควบคุมอะไรบน Android ได้บ้าง','faq1_a':'FoneClaw รองรับการทำงานบน Android มากกว่า 120 รายการใน 16 หมวด เช่น สถานะเครื่อง ข้อความ การตั้งค่า ภาพหน้าจอ อีเมล การนำทาง และงานเว็บ','faq2_q':'FoneClaw ต้องใช้สิทธิ์ Accessibility หรือไม่','faq2_a':'ต้องใช้สำหรับการอ่านหน้าจอ การกดตามโหนด การเข้าถึงแจ้งเตือน และการเปลี่ยนการตั้งค่าระบบที่รองรับ','faq3_q':'FoneClaw ส่ง SMS หรืออีเมลอัตโนมัติได้ไหม','faq3_a':'FoneClaw ช่วยเตรียมและดำเนินการตามคำสั่งที่รองรับได้ แต่งานอ่อนไหวต้องมีการยืนยันจากผู้ใช้ก่อนเสมอ','faq4_q':'ทุกฟีเจอร์ใช้ได้ทันทีโดยไม่ตั้งค่าหรือไม่','faq4_a':'ไม่ทั้งหมด อีเมลต้องตั้งค่า IMAP/SMTP แผนที่ต้องมีแอปนำทาง และการตรวจภาพหน้าจอต้องเปิดสิทธิ์หน้าต่างลอย','faq5_q':'ฟีเจอร์พร้อมใช้งานอะไรบ้าง','faq5_a':'มี 16 หมวดฟีเจอร์พร้อมการทำงาน 120+ รายการ เช่น ตรวจเครื่อง จัดการข้อความ ควบคุมการตั้งค่า วิเคราะห์ภาพหน้าจอ และอื่นๆ',
  'cmd1':'ตรวจสถานะมือถือ','cmd1_desc':'รายงานหน่วยความจำ พื้นที่ แบตเตอรี่ เครือข่าย และความเสี่ยงด้านสิทธิ์','cmd2':'สรุป SMS วันนี้','cmd2_desc':'เรื่องสำคัญ คำตอบค้าง และความเสี่ยงตามผู้ติดต่อ','cmd3':'ตั้งความสว่าง 60%','cmd3_desc':'เปลี่ยนการตั้งค่า Android ที่รองรับพร้อมผลลัพธ์ชัดเจน','cmd4':'ถ่ายภาพหน้าจอ','cmd4_desc':'จับหน้าจอปัจจุบันและสรุปสิ่งที่เห็น','cmd5':'แจ้งเตือนสำคัญมีอะไรบ้าง','cmd5_desc':'จัดลำดับแจ้งเตือนล่าสุดในมือถือ','cmd6':'เช็คอีเมล','cmd6_desc':'อ่านอีเมลล่าสุดจากบัญชี IMAP/SMTP ที่ตั้งค่าไว้','cmd7':'ตอนนี้ฉันอยู่ที่ไหน','cmd7_desc':'ส่งคืนตำแหน่ง พิกัด ความแม่นยำ แหล่งที่มา และเวลา','cmd8':'นำทางด้วยรถยนต์','cmd8_desc':'เปิดแอปแผนที่ที่ติดตั้งและเริ่มนำทาง'
 },
 'download': {
  'meta_title':'ดาวน์โหลด FoneClaw — ผู้ช่วย AI สำหรับ Android','meta_desc':'ดาวน์โหลด FoneClaw สำหรับ Android ฟีเจอร์หลักใช้งานได้ฟรี ไม่ต้องชำระเงิน รองรับคำสั่งเสียง 120+ รายการใน 16 หมวดสำหรับงานมือถือจริง',
  'hero_title':'ดาวน์โหลด FoneClaw','hero_lead':'120+ การทำงาน ทดลองใช้ฟรี ฟีเจอร์หลักใช้งานได้ฟรีในตอนนี้ ไม่ต้องชำระเงิน','hero_subtitle':'ฟีเจอร์หลักใช้งานได้ฟรี ไม่ต้องชำระเงิน','product_desc':'ผู้ช่วย AI ระดับระบบสำหรับ Android 9+ รองรับการสั่งงานด้วยเสียง การทำงานข้ามแอป การจัดการอุปกรณ์ และงานมือถือประจำวันที่สำคัญ','req_title':'ข้อกำหนดระบบ','req_desc':'ตรวจสอบว่าอุปกรณ์ของคุณตรงตามข้อกำหนดเหล่านี้','faq_title':'คำถามที่พบบ่อย','faq_free_q':'FoneClaw ฟรีจริงหรือไม่','faq_free_a':'ใช่ ฟีเจอร์หลักใช้งานได้ฟรีในตอนนี้ อาจมีแผน Pro สำหรับฟีเจอร์ขั้นสูงในอนาคต แต่ข้อความบนหน้านี้ไม่สัญญาว่าฟรีถาวร','faq_phones_q':'ใช้ได้กับมือถือ Android ทุกเครื่องไหม','faq_phones_a':'FoneClaw ต้องใช้ Android 9 ขึ้นไปและ RAM อย่างน้อย 3GB จึงเหมาะกับอุปกรณ์ Android สมัยใหม่ส่วนใหญ่','faq_data_q':'ข้อมูลของฉันปลอดภัยไหม','faq_data_a':'FoneClaw ออกแบบให้ประมวลผลงานบนอุปกรณ์และใช้สิทธิ์ Android อย่างโปร่งใส งานอ่อนไหวต้องยืนยันก่อน','faq_available_q':'พร้อมใช้งานเมื่อใด','faq_available_a':'FoneClaw มีไฟล์ Android APK ให้ดาวน์โหลด ใช้ปุ่มดาวน์โหลดด้านบนเพื่อรับเวอร์ชันล่าสุด','req_android':'Android 9.0 ขึ้นไป','req_ram':'RAM อย่างน้อย 3GB','req_storage':'พื้นที่เก็บข้อมูล 100MB','req_mic':'สิทธิ์ไมโครโฟน','req_accessibility':'สิทธิ์ Accessibility Service','cta_download':'ดาวน์โหลด APK','cta_copy':'ดาวน์โหลดฟรี รับเวอร์ชัน Android ล่าสุด'
 },
 'resources': {'meta_title':'แหล่งความรู้ — คู่มือและบทความ FoneClaw','meta_desc':'รวมคู่มือ FoneClaw ภาษาไทยเกี่ยวกับการสั่งงาน Android ด้วยเสียง การเปรียบเทียบผู้ช่วย AI บนมือถือ และคำแนะนำใช้งานจริงสำหรับผู้ใช้ Android'},
 'community': {'meta_title':'ชุมชน — ผู้ใช้และฟีดแบ็ก FoneClaw','meta_desc':'เข้าร่วมชุมชน FoneClaw บน Telegram, Discord และ X เพื่อติดตามอัปเดต แชร์ฟีดแบ็ก และพูดคุยกับผู้ใช้ที่สนใจการสั่งงาน Android ด้วยเสียง','hero_title':'เข้าร่วมชุมชน FoneClaw','hero_desc':'พบผู้ใช้คนอื่น รับข่าวอัปเดตเร็วขึ้น และช่วยออกแบบอนาคตของการสั่งงาน Android ด้วยเสียง'}
}

p=base/'_th_translations.py'
p.write_text('# Source-backed Thai translations for FoneClaw.\n\nTH_TRANSLATIONS = '+repr(TH_TRANSLATIONS)+'\n',encoding='utf-8')

# 2) Patch _i18n.py
f=base/'_i18n.py'; s=f.read_text(encoding='utf-8')
if "'th':" not in s.split('}',1)[0]:
    s=s.replace("    'ar': {'name': 'Arabic', 'native': 'العربية', 'dir': 'ar', 'hreflang': 'ar'},", "    'ar': {'name': 'Arabic', 'native': 'العربية', 'dir': 'ar', 'hreflang': 'ar'},\n    'th': {'name': 'Thai', 'native': 'ไทย', 'dir': 'th', 'hreflang': 'th'},")
if 'from _th_translations import TH_TRANSLATIONS' not in s:
    block="""\ntry:\n    from _th_translations import TH_TRANSLATIONS\n    for _page, _entries in TH_TRANSLATIONS.items():\n        for _key, _text in _entries.items():\n            TRANSLATIONS.setdefault(_page, {}).setdefault(_key, {})['th'] = _text\nexcept Exception:\n    pass\n"""
    s=s.replace('\ndef get_text(page, key, lang=\'en\'):', block+'\ndef get_text(page, key, lang=\'en\'):')
f.write_text(s,encoding='utf-8')

# 3) Patch _components.py
f=base/'_components.py'; s=f.read_text(encoding='utf-8')
if 'NAV_ITEMS_TH' not in s:
    insert="""
NAV_ITEMS_TH = [
    (0, 'หน้าแรก', '/'),
    (1, 'ฟีเจอร์', '/features.html'),
    (2, 'ดาวน์โหลด', '/download.html'),
    (3, 'แหล่งความรู้', '/resources.html'),
    (4, 'ชุมชน', '/community.html'),
]
"""
    s=s.replace('\nLANG_DIR = {', insert+'\nLANG_DIR = {')
s=s.replace("'ar': 'ar'}", "'ar': 'ar', 'th': 'th'}")
s=s.replace("('ar', 'العربية')]", "('ar', 'العربية'), ('th', 'ไทย')]")
if "elif lang == 'th':\n        items = NAV_ITEMS_TH" not in s:
    s=s.replace("    elif lang == 'ar':\n        items = NAV_ITEMS_AR", "    elif lang == 'ar':\n        items = NAV_ITEMS_AR\n    elif lang == 'th':\n        items = NAV_ITEMS_TH")
if "'th': {'index': 'https://www.foneclaw.ai/th/index.html'" not in s:
    s=s.replace("        'ar': {'index': 'https://www.foneclaw.ai/ar/index.html', 'features': 'https://www.foneclaw.ai/ar/features.html', 'download': 'https://www.foneclaw.ai/ar/download.html', 'resources': 'https://www.foneclaw.ai/ar/resources.html', 'community': 'https://www.foneclaw.ai/ar/community.html'},",
                "        'ar': {'index': 'https://www.foneclaw.ai/ar/index.html', 'features': 'https://www.foneclaw.ai/ar/features.html', 'download': 'https://www.foneclaw.ai/ar/download.html', 'resources': 'https://www.foneclaw.ai/ar/resources.html', 'community': 'https://www.foneclaw.ai/ar/community.html'},\n        'th': {'index': 'https://www.foneclaw.ai/th/index.html', 'features': 'https://www.foneclaw.ai/th/features.html', 'download': 'https://www.foneclaw.ai/th/download.html', 'resources': 'https://www.foneclaw.ai/th/resources.html', 'community': 'https://www.foneclaw.ai/th/community.html'},")
if "startswith('/th/')" not in s:
    s=s.replace("    elif normalized_path.startswith('/ar/'):\n        normalized_path = '/' + normalized_path.split('/ar/', 1)[1]", "    elif normalized_path.startswith('/ar/'):\n        normalized_path = '/' + normalized_path.split('/ar/', 1)[1]\n    elif normalized_path.startswith('/th/'):\n        normalized_path = '/' + normalized_path.split('/th/', 1)[1]")
# footer block: add simple Thai branch before else if no explicit
if "elif lang == 'th':\n        slogan =" not in s:
    s=s.replace("    elif lang == 'ar':\n        slogan = 'FoneClaw هو وكيل الذكاء الاصطناعي لأندرويد", "    elif lang == 'th':\n        slogan = 'FoneClaw คือผู้ช่วย AI สำหรับ Android ที่ลงมือควบคุมมือถือจริง ไม่ใช่แค่ตอบคำถาม'\n        ft_product = 'ผลิตภัณฑ์'; ft_topics = 'หัวข้อ'; ft_company = 'บริษัท'; ft_follow = 'ติดตาม'\n        ft_features = 'ฟีเจอร์'; ft_download = 'ดาวน์โหลด'; ft_resources = 'แหล่งความรู้'; ft_community = 'ชุมชน'\n        ft_voice = 'การสั่งงานด้วยเสียง'; ft_comp = 'เปรียบเทียบ'; ft_ai = 'AI บนมือถือ'; ft_news = 'ข่าวสาร'\n        ft_copy = 'สงวนลิขสิทธิ์'\n    elif lang == 'ar':\n        slogan = 'FoneClaw هو وكيل الذكاء الاصطناعي لأندرويد")
# JS English fallback exclusion
s=s.replace('o.value.indexOf("/ar/")===-1', 'o.value.indexOf("/ar/")===-1&&o.value.indexOf("/th/")===-1')
f.write_text(s,encoding='utf-8')

# 4) Patch _features_page.py
f=base/'_features_page.py'; s=f.read_text(encoding='utf-8')
if "if lang == 'th':\n        _eyebrow" not in s:
    s=s.replace("    if lang == 'ar':\n        _eyebrow = 'ميزات FoneClaw'", "    if lang == 'ar':\n        _eyebrow = 'ميزات FoneClaw'\n    if lang == 'th':\n        _eyebrow = 'ฟีเจอร์ FoneClaw'")
if "if lang == 'th':\n        _stat_categories" not in s:
    s=s.replace("    if lang == 'ar':\n        _stat_categories = 'فئات الميزات'\n        _stat_actions = 'الإجراءات المدعومة'", "    if lang == 'ar':\n        _stat_categories = 'فئات الميزات'\n        _stat_actions = 'الإجراءات المدعومة'\n    if lang == 'th':\n        _stat_categories = 'หมวดฟีเจอร์'\n        _stat_actions = 'การทำงานที่รองรับ'")
if "elif lang == 'th':\n        _faq_sub" not in s:
    thai_block="""    elif lang == 'th':
        _faq_sub = 'ช่วยให้เข้าใจว่า FoneClaw ทำอะไรได้ในตอนนี้ และงานใดต้องยืนยันก่อนดำเนินการ'
        _cat_phone, _cat_phone_n = 'สถานะมือถือ', '9 คำสั่ง'
        _cat_notif, _cat_notif_n = 'การแจ้งเตือน', '6 คำสั่ง'
        _cat_sms, _cat_sms_n = 'SMS', '6 คำสั่ง'
        _cat_calls, _cat_calls_n = 'การโทร', '3 คำสั่ง'
        _cat_settings, _cat_settings_n = 'การตั้งค่าระบบ', '18 คำสั่ง'
        _cat_conn, _cat_conn_n = 'Wi-Fi และ Bluetooth', '12 คำสั่ง'
        _cat_photo, _cat_photo_n = 'รูปภาพและภาพหน้าจอ', '8 คำสั่ง'
        _cat_screen, _cat_screen_n = 'การอ่านหน้าจอ', '2 คำสั่ง'
        _cat_email, _cat_email_n = 'อีเมล', '10 คำสั่ง'
        _cat_calendar, _cat_calendar_n = 'ปฏิทิน', '6 คำสั่ง'
        _cat_alarms, _cat_alarms_n = 'นาฬิกาปลุก', '2 คำสั่ง'
        _cat_notes, _cat_notes_n = 'โน้ต', '9 คำสั่ง'
        _cat_maps, _cat_maps_n = 'แผนที่และนำทาง', '8 คำสั่ง'
        _cat_web, _cat_web_n = 'เว็บ', '3 คำสั่ง'
        _cat_workflows, _cat_workflows_n = 'เวิร์กโฟลว์', '3 คำสั่ง'
        _cat_app, _cat_app_n = 'การโต้ตอบแอป', 'คำสั่งลัด'
"""
    s=s.replace("    elif lang == 'ar':\n        _faq_sub", thai_block+"    elif lang == 'ar':\n        _faq_sub")
f.write_text(s,encoding='utf-8')

# 5) Patch social share
f=base/'_social_share.py'; s=f.read_text(encoding='utf-8')
if "elif lang == 'th':" not in s:
    s=s.replace("    elif lang == 'ar':", "    elif lang == 'th':\n        labels = {'x':'แชร์บน X','telegram':'แชร์บน Telegram','linkedin':'แชร์บน LinkedIn','facebook':'แชร์บน Facebook','reddit':'แชร์บน Reddit','copy':'คัดลอกลิงก์','toast':'คัดลอกลิงก์แล้ว'}\n    elif lang == 'ar':")
f.write_text(s,encoding='utf-8')

# 6) Patch homepage minimal
f=base/'_homepage.py'; s=f.read_text(encoding='utf-8')
if 'TH_TRANSLATIONS = {' not in s:
    th_cards={
    'tasker-alternative-voice-automation':('ทางเลือก Tasker สำหรับสั่ง Android ด้วยเสียง','อัตโนมัติบน Android โดยไม่ต้อง root หรือเขียนสคริปต์','คู่มือ','9 นาที'),
    'xiaomi-ai-ecosystem-2026':('ระบบ AI ของ Xiaomi และ HyperOS ปี 2026','มอง MiMo, HyperOS และ MiClaw ผ่านงานมือถือจริง','อุตสาหกรรม','9 นาที'),
    'voice-control-visually-impaired':('สั่งงาน Android ด้วยเสียงสำหรับผู้พิการทางสายตา','คู่มือ Voice Access, TalkBack และ FoneClaw อย่างปลอดภัย','การเข้าถึง','9 นาที'),
    'gemini-intelligence-supported-devices':('อุปกรณ์ที่รองรับ Gemini Intelligence','ความเข้ากันได้ของ AI เทียบกับการทำงานจริงบน Android','อุตสาหกรรม','10 นาที'),
    'comp_vs_miclaw':('MiClaw vs FoneClaw สำหรับ Android','ระบบ Xiaomi เทียบกับการทำงาน Android ที่กว้างกว่า','เปรียบเทียบ','8 นาที'),
    'wwdc-2026-ai-do-over-phone-agent':('WWDC 2026, Siri AI และ Apple Intelligence','สิ่งที่ Apple เปลี่ยนมีความหมายอย่างไรต่อผู้ช่วยมือถือ','อุตสาหกรรม','10 นาที'),
    'agentic-ai-phone-explained':('AI Agent บนมือถือคืออะไร','จากการตอบคำถามไปสู่การลงมือทำงานบนมือถือ','คู่มือ','9 นาที'),
    'gemini-vs-foneclaw':('Gemini vs FoneClaw: เข้าใจหรือทำงาน','การเข้าใจข้อมูลเทียบกับการสั่งงาน Android จริง','เปรียบเทียบ','9 นาที'),
    'android-vs-ios-26-5-voice-control':('Android vs iOS: สั่งงานด้วยเสียง 2026','เปรียบเทียบเสียง การเข้าถึง และอัตโนมัติแบบใช้งานจริง','เปรียบเทียบ','8 นาที'),
    'voice-control-whatsapp':('สั่งงาน WhatsApp ด้วยเสียงบน Android','ข้อความ โทร และการยืนยันด้วยขอบเขตที่ชัดเจน','คู่มือ','8 นาที'),
    'gemini-intelligence-vs-siri':('Gemini Intelligence vs Siri AI 2026','กลยุทธ์ผู้ช่วย AI ของ Google และ Apple','อุตสาหกรรม','8 นาที'),
    'foneclaw-vs-apple-intelligence':('FoneClaw vs Apple Intelligence','การฝังลึกใน iOS เทียบกับการทำงานจริงบน Android','เปรียบเทียบ','8 นาที')}
    s=s.replace('\ndef _build_article_cards', '\nTH_TRANSLATIONS = '+repr(th_cards)+'\n\ndef _build_article_cards')
if "elif lang == 'th' and slug in TH_TRANSLATIONS" not in s:
    s=s.replace("        elif lang == 'ar' and slug in AR_TRANSLATIONS:\n            title, desc, cat, read_time = AR_TRANSLATIONS[slug]", "        elif lang == 'ar' and slug in AR_TRANSLATIONS:\n            title, desc, cat, read_time = AR_TRANSLATIONS[slug]\n        elif lang == 'th' and slug in TH_TRANSLATIONS:\n            title, desc, cat, read_time = TH_TRANSLATIONS[slug]")
s=s.replace("('اقرأ' if lang == 'ar' else", "('อ่าน' if lang == 'th' else ('اقرأ' if lang == 'ar' else")
s=s.replace("'Read')))))))))", "'Read'))))))))))")
s=s.replace("('/ar' if lang == 'ar' else", "('/th' if lang == 'th' else ('/ar' if lang == 'ar' else")
s=s.replace("'')))))))))", "''))))))))))")
s=s.replace("'de', 'ar')", "'de', 'ar', 'th')")
s=s.replace("'de','ar')", "'de','ar','th')")
if "th_cat =" not in s:
    s=s.replace("            ar_cat = {'Setup': 'إعداد','Industry': 'صناعة','Use Cases': 'حالات الاستخدام','Comparison': 'مقارنة','Apps': 'تطبيقات','Guide': 'دليل','Safety': 'أمان','Accessibility': 'إمكانية الوصول'}", "            ar_cat = {'Setup': 'إعداد','Industry': 'صناعة','Use Cases': 'حالات الاستخدام','Comparison': 'مقارنة','Apps': 'تطبيقات','Guide': 'دليل','Safety': 'أمان','Accessibility': 'إمكانية الوصول'}\n            th_cat = {'Setup': 'คู่มือ','Industry': 'อุตสาหกรรม','Use Cases': 'กรณีใช้งาน','Comparison': 'เปรียบเทียบ','Apps': 'แอป','Guide': 'คู่มือ','Safety': 'ความปลอดภัย','Accessibility': 'การเข้าถึง'}")
    s=s.replace("cat = (ar_cat if lang == 'ar' else", "cat = (th_cat if lang == 'th' else (ar_cat if lang == 'ar' else")
    s=s.replace("zh_cat))))))))).get(cat, cat)", "zh_cat)))))))))).get(cat, cat)")
s=s.replace("('مجاني' if lang == 'ar' else", "('ฟรี' if lang == 'th' else ('مجاني' if lang == 'ar' else")
s=s.replace("'Free')))))))))", "'Free'))))))))))")
f.write_text(s,encoding='utf-8')

# 7) Patch build_multi.py dynamically simple string additions
f=base/'build_multi.py'; s=f.read_text(encoding='utf-8')
# add th to obvious language lists
for old,new in [
    ("['zh','tw','ja','ko','es','pt','ru','fr','de','ar']", "['zh','tw','ja','ko','es','pt','ru','fr','de','ar','th']"),
    ("['zh', 'tw', 'ja', 'ko', 'es', 'pt', 'ru', 'fr', 'de', 'ar']", "['zh', 'tw', 'ja', 'ko', 'es', 'pt', 'ru', 'fr', 'de', 'ar', 'th']"),
    ("('zh','tw','ja','ko','es','pt','ru','fr','de','ar')", "('zh','tw','ja','ko','es','pt','ru','fr','de','ar','th')"),
    ("('zh', 'tw', 'ja', 'ko', 'es', 'pt', 'ru', 'fr', 'de', 'ar')", "('zh', 'tw', 'ja', 'ko', 'es', 'pt', 'ru', 'fr', 'de', 'ar', 'th')"),
]: s=s.replace(old,new)
# if explicit dirs list in sitemap with tuples, add after ar
s=s.replace("('ar', 'ar')", "('ar', 'ar'), ('th', 'th')")
f.write_text(s,encoding='utf-8')

print('setup core thai done')
