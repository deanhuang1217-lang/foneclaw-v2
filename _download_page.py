"""Download page generation - synced from upload_download_version_check_20260610_170222."""


def generate_download_page(full_page, base, lang='en'):
    from _i18n import get_text, generate_hreflang_tags
    t = lambda key: get_text('download', key, lang)
    _ht = t('hero_title'); _hs = t('hero_subtitle'); _pd = t('product_desc')
    _rt = t('req_title'); _rd = t('req_desc'); _ft = t('faq_title')
    _fq1q = t('faq_free_q'); _fq1a = t('faq_free_a')
    _fq2q = t('faq_phones_q'); _fq2a = t('faq_phones_a')
    _fq3q = t('faq_data_q'); _fq3a = t('faq_data_a')
    _fq4q = t('faq_available_q'); _fq4a = t('faq_available_a')
    _ra = t('req_android'); _rr = t('req_ram'); _rs = t('req_storage')
    _rm = t('req_mic'); _rac = t('req_accessibility')
    """Generate the download page using full_page()."""

    body = f'''
<section style="padding:120px 0 50px;text-align:center;background:linear-gradient(180deg,#080c18 0%,#0b1a3a 50%,#080c18 100%)">
<div class="wrap">
<h1 style="font-size:clamp(32px,5vw,48px);font-weight:700;line-height:1.15;margin-bottom:14px">{_ht}</h1>
<p style="font-size:17px;color:#8b949e;max-width:480px;margin:0 auto">{_hs}</p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;max-width:760px;margin:40px auto 0">
<div style="background:#0d1117;border:1px solid #1a2332;border-radius:16px;padding:36px 24px;text-align:center">
<div style="text-align:center;margin-bottom:14px;height:48px;display:flex;align-items:center;justify-content:center"><img src="/favicon.png" alt="FoneClaw" style="width:48px;height:48px"></div>
<h2 style="font-size:20px;margin-bottom:6px;height:28px;display:flex;align-items:center;justify-content:center">FoneClaw</h2>
<p style="color:#8b949e;font-size:14px;margin-bottom:20px;line-height:1.6">{_pd}</p>
<div data-foneclaw-apk-cta></div>
</div>
<div style="background:#0d1117;border:1px solid #1a2332;border-radius:16px;padding:36px 24px;text-align:center">
<div style="text-align:center;margin-bottom:14px;height:48px;display:flex;align-items:center;justify-content:center;font-size:48px">\u2699\ufe0f</div>
<h2 style="font-size:20px;margin-bottom:6px;height:28px;display:flex;align-items:center;justify-content:center">{_rt}</h2>
<p style="color:#8b949e;font-size:14px;margin-bottom:20px;line-height:1.6">{_rd}</p>
<div style="text-align:left;padding:0 8px">
<div style="display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid #1a2332"><span style="color:#3fb950;font-size:14px">\u2713</span><span style="color:#c9d1d9;font-size:14px">{_ra}</span></div>
<div style="display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid #1a2332"><span style="color:#3fb950;font-size:14px">\u2713</span><span style="color:#c9d1d9;font-size:14px">{_rr}</span></div>
<div style="display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid #1a2332"><span style="color:#3fb950;font-size:14px">\u2713</span><span style="color:#c9d1d9;font-size:14px">{_rs}</span></div>
<div style="display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid #1a2332"><span style="color:#3fb950;font-size:14px">\u2713</span><span style="color:#c9d1d9;font-size:14px">{_rm}</span></div>
<div style="display:flex;align-items:center;gap:10px;padding:9px 0"><span style="color:#3fb950;font-size:14px">\u2713</span><span style="color:#c9d1d9;font-size:14px">{_rac}</span></div>
</div>
</div>
</div>
</div>
</section>
<section style="padding:60px 0 50px"><div class="wrap" style="max-width:680px">
<h2 style="font-size:24px;text-align:center;margin-bottom:28px">{_ft}</h2>
<details style="margin-bottom:10px;background:#0d1117;border:1px solid #1a2332;border-radius:10px;overflow:hidden"><summary style="padding:15px 18px;cursor:pointer;font-family:Space Grotesk,sans-serif;font-weight:600;color:#f0f4f8;font-size:15px;list-style:none;display:flex;justify-content:space-between;align-items:center">{_fq1q}<span style="color:#6e7681;font-size:18px">+</span></summary><div style="padding:0 18px 15px;color:#8b949e;font-size:14px;line-height:1.7">{_fq1a}</div></details>
<details style="margin-bottom:10px;background:#0d1117;border:1px solid #1a2332;border-radius:10px;overflow:hidden"><summary style="padding:15px 18px;cursor:pointer;font-family:Space Grotesk,sans-serif;font-weight:600;color:#f0f4f8;font-size:15px;list-style:none;display:flex;justify-content:space-between;align-items:center">{_fq2q}<span style="color:#6e7681;font-size:18px">+</span></summary><div style="padding:0 18px 15px;color:#8b949e;font-size:14px;line-height:1.7">{_fq2a}</div></details>
<details style="margin-bottom:10px;background:#0d1117;border:1px solid #1a2332;border-radius:10px;overflow:hidden"><summary style="padding:15px 18px;cursor:pointer;font-family:Space Grotesk,sans-serif;font-weight:600;color:#f0f4f8;font-size:15px;list-style:none;display:flex;justify-content:space-between;align-items:center">{_fq3q}<span style="color:#6e7681;font-size:18px">+</span></summary><div style="padding:0 18px 15px;color:#8b949e;font-size:14px;line-height:1.7">{_fq3a}</div></details>
<details style="margin-bottom:10px;background:#0d1117;border:1px solid #1a2332;border-radius:10px;overflow:hidden"><summary style="padding:15px 18px;cursor:pointer;font-family:Space Grotesk,sans-serif;font-weight:600;color:#f0f4f8;font-size:15px;list-style:none;display:flex;justify-content:space-between;align-items:center">{_fq4q}<span style="color:#6e7681;font-size:18px">+</span></summary><div style="padding:0 18px 15px;color:#8b949e;font-size:14px;line-height:1.7">{_fq4a}</div></details>
</div></section>
'''

    hreflang = generate_hreflang_tags('/download.html', lang)
    return full_page(
        t('meta_title'),
        t('meta_desc'),
        '/download.html' if lang == 'en' else f'/{lang}/download.html',
        2,
        body,
        og_image='https://www.foneclaw.ai/images/og-download.jpg',
        lang=lang,
        hreflang_tags=hreflang)
