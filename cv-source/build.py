from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto("file://"+os.path.abspath("cv.html")); pg.wait_for_timeout(300)
    print("content bottom px:", pg.evaluate("(()=>{const pgEl=document.querySelector('.page');const r=pgEl.getBoundingClientRect();let m=0;pgEl.querySelectorAll('*').forEach(e=>{m=Math.max(m,e.getBoundingClientRect().bottom)});return [Math.round(m-r.top), Math.round(r.height)]})()"))
    pg.pdf(path="../Shuvo_Datta_CV.pdf", width="210mm", height="297mm", print_background=True, prefer_css_page_size=True)
    b.close()
