"""
TECHFAM Software Agency Website
app.py — Main Streamlit Application
"""

import streamlit as st
import base64
from pathlib import Path
from data.content import (
    SERVICES, PROJECTS, TESTIMONIALS, FAQS,
    PRICING, TECHNOLOGIES, STATS, PROCESS, WHY_US, SOCIAL_LINKS
)

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="TECHFAM — We Build Solutions. You Get Results.",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ── Asset Helpers ──────────────────────────────────────────────────────────────
def img_to_b64(path: str) -> str:
    try:
        data = Path(path).read_bytes()
        return base64.b64encode(data).decode()
    except Exception:
        return ""


# Optimized assets are used for web display (originals preserved untouched in assets/
# for brand archival — see assets/logo.png and assets/founder.png for source files).
LOGO_B64 = img_to_b64("assets/logo_optimized.png")
FOUNDER_B64 = img_to_b64("assets/founder_optimized.jpg")
FOUNDER_THUMB_B64 = img_to_b64("assets/founder_thumb.jpg")


# ── Global CSS ─────────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
<style>
/* ── Reset & Base ─────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --black:    #0A0A0A;
  --charcoal: #1A1A1A;
  --blue:     #00BFFF;
  --blue-dim: #0090CC;
  --white:    #FFFFFF;
  --gray:     #CFCFCF;
  --gray-dim: #888888;
  --purple:   #7C3AED;
  --green:    #10B981;
  --card-bg:  rgba(26,26,26,0.85);
  --border:   rgba(0,191,255,0.18);
  --glow:     0 0 30px rgba(0,191,255,0.25);
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stAppViewContainer"] {
  background: var(--black);
  font-family: 'Inter', sans-serif;
  color: var(--white);
}
[data-testid="stVerticalBlock"] { gap: 0 !important; }
section[data-testid="stSidebar"] { display: none; }
.stMarkdown p { margin: 0; }

/* ── Scrollbar ─────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--charcoal); }
::-webkit-scrollbar-thumb { background: var(--blue); border-radius: 3px; }

/* ── Navbar ────────────────────────────────────────────────────────── */
.tf-nav {
  position: sticky; top: 0; z-index: 1000;
  background: rgba(10,10,10,0.92);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 0 5% ;
  display: flex; align-items: center; justify-content: space-between;
  height: 72px;
}
.tf-nav-logo img { height: 44px; }
.tf-nav-links { display: flex; gap: 2rem; list-style: none; }
.tf-nav-links a {
  color: var(--gray); text-decoration: none; font-size: .9rem;
  font-weight: 500; transition: color .2s;
  letter-spacing: .3px;
}
.tf-nav-links a:hover { color: var(--blue); }
.tf-nav-cta {
  background: var(--blue); color: var(--black);
  border: none; padding: .55rem 1.4rem; border-radius: 8px;
  font-weight: 700; font-size: .88rem; cursor: pointer;
  transition: all .2s; text-decoration: none;
  letter-spacing: .3px;
}
.tf-nav-cta:hover { background: #00d4ff; transform: translateY(-1px); box-shadow: var(--glow); }

/* ── Hero ──────────────────────────────────────────────────────────── */
.tf-hero {
  min-height: 100vh;
  display: grid; grid-template-columns: 1fr 1fr;
  align-items: center; gap: 4rem;
  padding: 6rem 8% 4rem;
  position: relative; overflow: hidden;
  background: var(--black);
}
.tf-hero::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 80% 80% at 70% 50%, rgba(0,191,255,.07) 0%, transparent 60%),
              radial-gradient(ellipse 40% 60% at 10% 80%, rgba(124,58,237,.05) 0%, transparent 50%);
  pointer-events: none;
}
.tf-hero-grid {
  position: absolute; inset: 0;
  background-image: linear-gradient(rgba(0,191,255,.04) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0,191,255,.04) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
}
.tf-hero-badge {
  display: inline-flex; align-items: center; gap: .5rem;
  background: rgba(0,191,255,.1); border: 1px solid rgba(0,191,255,.3);
  color: var(--blue); padding: .4rem 1rem; border-radius: 100px;
  font-size: .8rem; font-weight: 600; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 1.5rem;
}
.tf-hero-badge::before { content: '●'; font-size: .5rem; animation: pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.3} }

.tf-hero h1 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: clamp(2.4rem, 4.5vw, 4rem);
  font-weight: 800; line-height: 1.1;
  letter-spacing: -1.5px; margin-bottom: 1.5rem;
}
.tf-hero h1 .accent { color: var(--blue); }
.tf-hero-sub {
  font-size: 1.1rem; color: var(--gray);
  line-height: 1.7; margin-bottom: 2.5rem; max-width: 520px;
}
.tf-hero-btns { display: flex; gap: 1rem; flex-wrap: wrap; }
.btn-primary {
  background: var(--blue); color: var(--black);
  padding: .85rem 2rem; border-radius: 10px; font-weight: 700;
  font-size: .95rem; text-decoration: none; transition: all .25s;
  display: inline-flex; align-items: center; gap: .5rem;
  letter-spacing: .2px;
}
.btn-primary:hover { background: #00d4ff; transform: translateY(-2px); box-shadow: 0 8px 30px rgba(0,191,255,.4); }
.btn-secondary {
  background: transparent; color: var(--white);
  padding: .85rem 2rem; border-radius: 10px; font-weight: 600;
  font-size: .95rem; text-decoration: none; transition: all .25s;
  border: 1px solid rgba(255,255,255,.2);
  display: inline-flex; align-items: center; gap: .5rem;
}
.btn-secondary:hover { border-color: var(--blue); color: var(--blue); transform: translateY(-2px); }
.btn-ghost {
  background: transparent; color: var(--gray);
  padding: .85rem 2rem; border-radius: 10px; font-weight: 600;
  font-size: .95rem; text-decoration: none; transition: all .25s;
  border: 1px solid rgba(255,255,255,.1);
  display: inline-flex; align-items: center; gap: .5rem;
}
.btn-ghost:hover { border-color: var(--blue); color: var(--blue); }

/* Hero image */
.tf-hero-img-wrap {
  position: relative; display: flex;
  justify-content: center; align-items: flex-end;
}
.tf-hero-img-glow {
  position: absolute; bottom: 0; left: 50%; transform: translateX(-50%);
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(0,191,255,.2) 0%, transparent 70%);
  border-radius: 50%;
}
.tf-hero-img {
  position: relative; z-index: 1;
  width: 100%; max-width: 440px;
  border-radius: 20px;
  filter: drop-shadow(0 30px 60px rgba(0,191,255,.2));
}
.tf-hero-stats {
  display: flex; gap: 2rem; margin-top: 2.5rem; flex-wrap: wrap;
}
.tf-hero-stat { text-align: center; }
.tf-hero-stat-val {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.8rem; font-weight: 800; color: var(--blue);
}
.tf-hero-stat-lbl { font-size: .78rem; color: var(--gray-dim); text-transform: uppercase; letter-spacing: .5px; }

/* Floating tech pills */
.tf-float-pills {
  display: flex; flex-wrap: wrap; gap: .6rem; margin-top: 2rem;
}
.tf-pill {
  background: rgba(0,191,255,.08); border: 1px solid rgba(0,191,255,.2);
  color: var(--blue); padding: .3rem .8rem; border-radius: 100px;
  font-size: .78rem; font-weight: 600; animation: floatpill 4s ease-in-out infinite;
}
.tf-pill:nth-child(2) { animation-delay: .5s; }
.tf-pill:nth-child(3) { animation-delay: 1s; }
.tf-pill:nth-child(4) { animation-delay: 1.5s; }
.tf-pill:nth-child(5) { animation-delay: 2s; }
@keyframes floatpill { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }

/* ── Section Wrapper ───────────────────────────────────────────────── */
.tf-section {
  padding: 6rem 8%;
  position: relative;
}
.tf-section-alt { background: rgba(26,26,26,.5); }
.tf-section-header { text-align: center; margin-bottom: 4rem; }
.tf-eyebrow {
  display: inline-block; color: var(--blue);
  font-size: .8rem; font-weight: 700; letter-spacing: 2px;
  text-transform: uppercase; margin-bottom: .75rem;
}
.tf-section-title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 800; line-height: 1.2; letter-spacing: -1px;
  margin-bottom: 1rem;
}
.tf-section-sub {
  color: var(--gray-dim); font-size: 1.05rem; max-width: 560px; margin: 0 auto;
  line-height: 1.7;
}

/* ── Stats ─────────────────────────────────────────────────────────── */
.tf-stats-grid {
  display: grid; grid-template-columns: repeat(5, 1fr); gap: 1.5rem;
}
.tf-stat-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 16px; padding: 2rem 1rem; text-align: center;
  backdrop-filter: blur(10px);
  transition: all .3s;
}
.tf-stat-card:hover { border-color: var(--blue); transform: translateY(-4px); box-shadow: var(--glow); }
.tf-stat-icon { font-size: 2rem; margin-bottom: .75rem; }
.tf-stat-val {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.4rem; font-weight: 800; color: var(--blue);
}
.tf-stat-lbl { color: var(--gray-dim); font-size: .85rem; margin-top: .25rem; }

/* ── Service Cards ─────────────────────────────────────────────────── */
.tf-services-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem;
}
.tf-service-card {
  background: var(--card-bg);
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 16px; padding: 2rem;
  backdrop-filter: blur(10px);
  transition: all .3s; position: relative; overflow: hidden;
}
.tf-service-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0;
  height: 2px; background: linear-gradient(90deg, var(--blue), transparent);
  opacity: 0; transition: opacity .3s;
}
.tf-service-card:hover { border-color: var(--border); transform: translateY(-6px); box-shadow: var(--glow); }
.tf-service-card:hover::before { opacity: 1; }
.tf-service-icon { font-size: 2.2rem; margin-bottom: 1rem; }
.tf-service-title { font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: .6rem; }
.tf-service-desc { color: var(--gray-dim); font-size: .88rem; line-height: 1.65; }

/* ── Project Cards ─────────────────────────────────────────────────── */
.tf-projects-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 1.5rem;
}
.tf-project-card {
  background: var(--card-bg);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 20px; overflow: hidden;
  transition: all .3s; position: relative;
}
.tf-project-card:hover { transform: translateY(-8px); box-shadow: 0 20px 60px rgba(0,0,0,.5); }
.tf-project-top {
  padding: 2rem 2rem 1.5rem;
  border-bottom: 1px solid rgba(255,255,255,.06);
}
.tf-project-emoji-wrap {
  width: 60px; height: 60px; border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.8rem; margin-bottom: 1rem;
}
.tf-project-title { font-family: 'Space Grotesk', sans-serif; font-size: 1.2rem; font-weight: 700; margin-bottom: .5rem; }
.tf-project-desc { color: var(--gray-dim); font-size: .87rem; line-height: 1.6; }
.tf-project-bottom { padding: 1.5rem 2rem; }
.tf-project-tech { display: flex; flex-wrap: wrap; gap: .4rem; margin-bottom: 1rem; }
.tf-tech-tag {
  background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.1);
  color: var(--gray); padding: .2rem .7rem; border-radius: 6px; font-size: .75rem; font-weight: 500;
}
.tf-project-status {
  display: inline-flex; align-items: center; gap: .4rem;
  padding: .25rem .75rem; border-radius: 100px; font-size: .75rem; font-weight: 700;
}
.tf-status-live {
  background: rgba(16,185,129,.15); color: #10B981; border: 1px solid rgba(16,185,129,.3);
}
.tf-status-progress {
  background: rgba(0,191,255,.12); color: var(--blue); border: 1px solid var(--border);
}
.tf-project-features { list-style: none; margin-top: .75rem; }
.tf-project-features li {
  color: var(--gray-dim); font-size: .82rem; padding: .2rem 0;
  display: flex; align-items: center; gap: .4rem;
}
.tf-project-features li::before { content: '→'; color: var(--blue); font-weight: 700; }

/* ── Why Us ────────────────────────────────────────────────────────── */
.tf-whyus-grid {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem;
}
.tf-why-card {
  background: var(--card-bg); border: 1px solid rgba(255,255,255,.06);
  border-radius: 16px; padding: 1.75rem;
  transition: all .3s; text-align: center;
}
.tf-why-card:hover { border-color: var(--border); transform: translateY(-4px); box-shadow: var(--glow); }
.tf-why-icon { font-size: 2rem; margin-bottom: .75rem; }
.tf-why-title { font-weight: 700; margin-bottom: .4rem; font-size: .95rem; }
.tf-why-desc { color: var(--gray-dim); font-size: .83rem; }

/* ── Testimonials ──────────────────────────────────────────────────── */
.tf-testi-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;
}
.tf-testi-card {
  background: var(--card-bg); border: 1px solid rgba(255,255,255,.07);
  border-radius: 20px; padding: 2rem;
  backdrop-filter: blur(10px); transition: all .3s;
}
.tf-testi-card:hover { border-color: var(--border); transform: translateY(-4px); box-shadow: var(--glow); }
.tf-testi-stars { color: #F59E0B; font-size: 1rem; margin-bottom: 1rem; }
.tf-testi-text { color: var(--gray); font-size: .9rem; line-height: 1.7; margin-bottom: 1.5rem; font-style: italic; }
.tf-testi-author { display: flex; align-items: center; gap: .75rem; }
.tf-testi-avatar {
  width: 44px; height: 44px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: .85rem; color: var(--black);
  flex-shrink: 0;
}
.tf-testi-name { font-weight: 700; font-size: .9rem; }
.tf-testi-role { color: var(--gray-dim); font-size: .78rem; }

/* ── Pricing ───────────────────────────────────────────────────────── */
.tf-pricing-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; align-items: start;
}
.tf-price-card {
  background: var(--card-bg); border: 1px solid rgba(255,255,255,.08);
  border-radius: 24px; padding: 2.5rem;
  transition: all .3s; position: relative;
}
.tf-price-card.featured {
  border-color: var(--blue);
  box-shadow: 0 0 40px rgba(0,191,255,.15);
  transform: scale(1.03);
}
.tf-price-badge {
  position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
  background: var(--blue); color: var(--black);
  padding: .3rem 1.2rem; border-radius: 100px; font-size: .75rem; font-weight: 800;
  text-transform: uppercase; letter-spacing: .5px; white-space: nowrap;
}
.tf-price-name { font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; font-weight: 700; margin-bottom: .4rem; }
.tf-price-desc { color: var(--gray-dim); font-size: .85rem; margin-bottom: 1.5rem; }
.tf-price-amount {
  font-family: 'Space Grotesk', sans-serif; font-size: 2.6rem; font-weight: 800;
  margin-bottom: .25rem;
}
.tf-price-usd { color: var(--gray-dim); font-size: .85rem; margin-bottom: 2rem; }
.tf-price-features { list-style: none; }
.tf-price-features li { font-size: .88rem; padding: .5rem 0; border-bottom: 1px solid rgba(255,255,255,.05); color: var(--gray); }
.tf-price-features li:last-child { border-bottom: none; }
.tf-price-btn {
  width: 100%; margin-top: 2rem; padding: .85rem; border-radius: 10px;
  font-weight: 700; font-size: .95rem; cursor: pointer;
  border: none; transition: all .25s; text-align: center;
}
.tf-price-btn-primary { background: var(--blue); color: var(--black); }
.tf-price-btn-primary:hover { background: #00d4ff; box-shadow: var(--glow); }
.tf-price-btn-outline { background: transparent; color: var(--white); border: 1px solid rgba(255,255,255,.2) !important; }
.tf-price-btn-outline:hover { border-color: var(--blue) !important; color: var(--blue); }

/* ── Tech Grid ─────────────────────────────────────────────────────── */
.tf-tech-grid {
  display: grid; grid-template-columns: repeat(6, 1fr); gap: 1rem;
}
.tf-tech-item {
  background: var(--card-bg); border: 1px solid rgba(255,255,255,.06);
  border-radius: 12px; padding: 1.25rem .75rem; text-align: center;
  transition: all .25s;
}
.tf-tech-item:hover { border-color: var(--border); transform: translateY(-4px); box-shadow: var(--glow); }
.tf-tech-emoji { font-size: 1.75rem; margin-bottom: .5rem; }
.tf-tech-name { font-size: .78rem; color: var(--gray-dim); font-weight: 500; }

/* ── Process Timeline ──────────────────────────────────────────────── */
.tf-process-grid {
  display: grid; grid-template-columns: repeat(7, 1fr); gap: .75rem; position: relative;
}
.tf-process-grid::before {
  content: ''; position: absolute; top: 2.5rem; left: 5%; right: 5%;
  height: 1px; background: linear-gradient(90deg, transparent, var(--border), transparent);
}
.tf-process-step { text-align: center; position: relative; padding-top: .5rem; }
.tf-process-num {
  width: 48px; height: 48px; border-radius: 50%;
  background: var(--card-bg); border: 2px solid var(--blue);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Space Grotesk', sans-serif; font-weight: 800; color: var(--blue);
  font-size: .85rem; margin: 0 auto 1rem;
  box-shadow: 0 0 20px rgba(0,191,255,.2);
}
.tf-process-icon { font-size: 1.2rem; margin-bottom: .5rem; }
.tf-process-title { font-weight: 700; font-size: .88rem; margin-bottom: .35rem; }
.tf-process-desc { color: var(--gray-dim); font-size: .76rem; line-height: 1.5; }

/* ── FAQ ───────────────────────────────────────────────────────────── */
.tf-faq-item {
  background: var(--card-bg); border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px; margin-bottom: .75rem; overflow: hidden;
  transition: border-color .2s;
}
.tf-faq-item:hover { border-color: var(--border); }
.tf-faq-q {
  padding: 1.2rem 1.5rem; font-weight: 600; font-size: .95rem;
  cursor: pointer; display: flex; justify-content: space-between; align-items: center;
}
.tf-faq-a {
  padding: 0 1.5rem 1.2rem; color: var(--gray-dim);
  font-size: .88rem; line-height: 1.7;
}

/* ── Contact ───────────────────────────────────────────────────────── */
.tf-contact-grid {
  display: grid; grid-template-columns: 1fr 1.4fr; gap: 4rem; align-items: start;
}
.tf-contact-info h3 {
  font-family: 'Space Grotesk', sans-serif; font-size: 1.8rem; font-weight: 800;
  margin-bottom: 1rem;
}
.tf-contact-info p { color: var(--gray-dim); line-height: 1.7; margin-bottom: 2rem; }
.tf-contact-link {
  display: flex; align-items: center; gap: .75rem;
  color: var(--gray); text-decoration: none; padding: .75rem 0;
  border-bottom: 1px solid rgba(255,255,255,.05); font-size: .9rem;
  transition: color .2s;
}
.tf-contact-link:hover { color: var(--blue); }
.tf-contact-link-icon { font-size: 1.2rem; }
.tf-contact-founder {
  margin-top: 2rem;
  border-radius: 16px; overflow: hidden;
  border: 1px solid var(--border);
  max-width: 260px;
}
.tf-contact-founder img { width: 100%; display: block; }

/* ── About ─────────────────────────────────────────────────────────── */
.tf-about-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: center;
}
.tf-about-img-wrap { position: relative; }
.tf-about-img {
  width: 100%; border-radius: 20px;
  box-shadow: 0 30px 80px rgba(0,0,0,.5);
  filter: brightness(.95) saturate(1.05);
}
.tf-about-img-overlay {
  position: absolute; bottom: 1.5rem; left: 1.5rem; right: 1.5rem;
  background: rgba(10,10,10,.85); backdrop-filter: blur(20px);
  border: 1px solid var(--border); border-radius: 12px; padding: 1.25rem 1.5rem;
  display: flex; gap: 1.5rem;
}
.tf-about-metric { text-align: center; }
.tf-about-metric-val {
  font-family: 'Space Grotesk', sans-serif; font-size: 1.6rem;
  font-weight: 800; color: var(--blue);
}
.tf-about-metric-lbl { font-size: .75rem; color: var(--gray-dim); }
.tf-about-text h2 {
  font-family: 'Space Grotesk', sans-serif; font-size: clamp(1.8rem, 3vw, 2.5rem);
  font-weight: 800; line-height: 1.2; letter-spacing: -1px; margin-bottom: 1.25rem;
}
.tf-about-text p { color: var(--gray-dim); line-height: 1.8; margin-bottom: 1rem; font-size: .95rem; }
.tf-about-tags { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1.5rem; }
.tf-tag {
  background: rgba(0,191,255,.1); border: 1px solid rgba(0,191,255,.25);
  color: var(--blue); padding: .35rem .9rem; border-radius: 8px;
  font-size: .8rem; font-weight: 600;
}

/* ── CTA Banner ────────────────────────────────────────────────────── */
.tf-cta {
  background: linear-gradient(135deg, rgba(0,191,255,.1) 0%, rgba(124,58,237,.1) 100%);
  border: 1px solid rgba(0,191,255,.2); border-radius: 24px;
  padding: 4rem; text-align: center; position: relative; overflow: hidden;
  margin: 0 8% 6rem;
}
.tf-cta::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 60% 80% at 50% 50%, rgba(0,191,255,.06) 0%, transparent 70%);
}
.tf-cta h2 {
  font-family: 'Space Grotesk', sans-serif; font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 800; letter-spacing: -1px; margin-bottom: 1rem; position: relative;
}
.tf-cta p { color: var(--gray-dim); font-size: 1.05rem; margin-bottom: 2rem; position: relative; }
.tf-cta-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; position: relative; }

/* ── Footer ────────────────────────────────────────────────────────── */
.tf-footer {
  background: var(--charcoal); border-top: 1px solid rgba(255,255,255,.07);
  padding: 4rem 8% 2rem;
}
.tf-footer-grid {
  display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; margin-bottom: 3rem;
}
.tf-footer-brand p { color: var(--gray-dim); font-size: .88rem; line-height: 1.7; margin-top: .75rem; max-width: 280px; }
.tf-footer-col h4 { font-weight: 700; margin-bottom: 1rem; font-size: .95rem; }
.tf-footer-col ul { list-style: none; }
.tf-footer-col ul li { margin-bottom: .5rem; }
.tf-footer-col ul li a { color: var(--gray-dim); text-decoration: none; font-size: .85rem; transition: color .2s; }
.tf-footer-col ul li a:hover { color: var(--blue); }
.tf-footer-social { display: flex; gap: .75rem; flex-wrap: wrap; margin-top: .75rem; }
.tf-social-btn {
  width: 38px; height: 38px; border-radius: 9px;
  background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.08);
  display: flex; align-items: center; justify-content: center;
  font-size: 1rem; text-decoration: none; transition: all .2s;
}
.tf-social-btn:hover { background: rgba(0,191,255,.15); border-color: var(--border); transform: translateY(-2px); }
.tf-footer-bottom {
  border-top: 1px solid rgba(255,255,255,.06); padding-top: 1.5rem;
  display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;
}
.tf-footer-copy { color: var(--gray-dim); font-size: .83rem; }

/* ── Forms (Streamlit overrides) ───────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
  background: rgba(26,26,26,.9) !important;
  border: 1px solid rgba(255,255,255,.12) !important;
  border-radius: 10px !important; color: var(--white) !important;
  font-family: 'Inter', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
  border-color: var(--blue) !important;
  box-shadow: 0 0 0 2px rgba(0,191,255,.15) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label,
.stFileUploader label { color: var(--gray) !important; font-size: .9rem !important; font-weight: 500 !important; }
.stButton > button {
  background: var(--blue) !important; color: var(--black) !important;
  border: none !important; border-radius: 10px !important;
  font-weight: 700 !important; font-size: .95rem !important;
  padding: .75rem 2rem !important; transition: all .25s !important;
  width: 100% !important;
}
.stButton > button:hover { background: #00d4ff !important; box-shadow: var(--glow) !important; }
.stSuccess > div { background: rgba(16,185,129,.1) !important; border-color: rgba(16,185,129,.3) !important; color: #10B981 !important; }

/* ── Divider ───────────────────────────────────────────────────────── */
.tf-divider {
  height: 1px; background: linear-gradient(90deg, transparent, var(--border), transparent);
  margin: 0 8%;
}

/* ── Responsive ────────────────────────────────────────────────────── */
@media (max-width: 1024px) {
  .tf-hero { grid-template-columns: 1fr; padding: 5rem 6% 3rem; }
  .tf-hero-img-wrap { display: none; }
  .tf-stats-grid { grid-template-columns: repeat(3, 1fr); }
  .tf-whyus-grid { grid-template-columns: repeat(2, 1fr); }
  .tf-testi-grid { grid-template-columns: repeat(2, 1fr); }
  .tf-pricing-grid { grid-template-columns: 1fr; }
  .tf-price-card.featured { transform: scale(1); }
  .tf-about-grid { grid-template-columns: 1fr; }
  .tf-contact-grid { grid-template-columns: 1fr; }
  .tf-footer-grid { grid-template-columns: 1fr 1fr; }
  .tf-tech-grid { grid-template-columns: repeat(4, 1fr); }
  .tf-process-grid { grid-template-columns: repeat(4, 1fr); }
}
@media (max-width: 768px) {
  .tf-section { padding: 4rem 5%; }
  .tf-stats-grid { grid-template-columns: repeat(2, 1fr); }
  .tf-testi-grid { grid-template-columns: 1fr; }
  .tf-projects-grid { grid-template-columns: 1fr; }
  .tf-tech-grid { grid-template-columns: repeat(3, 1fr); }
  .tf-process-grid { grid-template-columns: repeat(2, 1fr); }
  .tf-footer-grid { grid-template-columns: 1fr; }
  .tf-whyus-grid { grid-template-columns: repeat(2, 1fr); }
  .tf-cta { margin: 0 5% 4rem; padding: 2.5rem 1.5rem; }
  .tf-nav-links { display: none; }
}
</style>
""", unsafe_allow_html=True)


# ── Components ─────────────────────────────────────────────────────────────────

def render_navbar():
    logo_src = f"data:image/png;base64,{LOGO_B64}" if LOGO_B64 else ""
    logo_html = f'<img src="{logo_src}" alt="TECHFAM">' if logo_src else '<span style="font-family:Space Grotesk;font-weight:800;font-size:1.4rem;color:#00BFFF;">TECHFAM</span>'

    st.markdown(f"""
<nav class="tf-nav">
  <div class="tf-nav-logo">{logo_html}</div>
  <ul class="tf-nav-links">
    <li><a href="#services">Services</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#testimonials">Testimonials</a></li>
    <li><a href="#pricing">Pricing</a></li>
    <li><a href="#faq">FAQ</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <a class="tf-nav-cta" href="#contact">⚡ Hire Us</a>
</nav>
""", unsafe_allow_html=True)


def render_hero():
    founder_src = f"data:image/jpeg;base64,{FOUNDER_B64}" if FOUNDER_B64 else ""
    founder_html = f'<img src="{founder_src}" alt="TECHFAM Founder" class="tf-hero-img">' if founder_src else ""

    st.markdown(f"""
<section class="tf-hero" id="home">
  <div class="tf-hero-grid"></div>

  <div class="tf-hero-content">
    <div class="tf-hero-badge">🇳🇬 Nigeria · Serving Clients Worldwide</div>

    <h1>We Build <span class="accent">Solutions.</span><br>You Get Results.</h1>

    <p class="tf-hero-sub">
      We design modern software, AI applications, business systems, and websites
      that help students, startups, entrepreneurs, and businesses succeed.
      <strong style="color:#fff;">100% remote. Always delivered.</strong>
    </p>

    <div class="tf-hero-btns">
      <a class="btn-primary" href="#contact">⚡ Hire Us</a>
      <a class="btn-secondary" href="#projects">🚀 View Projects</a>
      <a class="btn-ghost" href="#contact">💬 Free Consultation</a>
    </div>

    <div class="tf-hero-stats">
      <div class="tf-hero-stat">
        <div class="tf-hero-stat-val">120+</div>
        <div class="tf-hero-stat-lbl">Projects Done</div>
      </div>
      <div class="tf-hero-stat">
        <div class="tf-hero-stat-val">95+</div>
        <div class="tf-hero-stat-lbl">Happy Clients</div>
      </div>
      <div class="tf-hero-stat">
        <div class="tf-hero-stat-val">3+</div>
        <div class="tf-hero-stat-lbl">Years Active</div>
      </div>
    </div>

    <div class="tf-float-pills">
      <span class="tf-pill">🤖 AI & ML</span>
      <span class="tf-pill">🐍 Python</span>
      <span class="tf-pill">🌐 Web Dev</span>
      <span class="tf-pill">☁️ Cloud</span>
      <span class="tf-pill">🎓 Final-Year Projects</span>
    </div>
  </div>

  <div class="tf-hero-img-wrap">
    <div class="tf-hero-img-glow"></div>
    {founder_html}
  </div>
</section>
""", unsafe_allow_html=True)


def render_stats():
    cards = "".join([f"""
<div class="tf-stat-card">
  <div class="tf-stat-icon">{s['icon']}</div>
  <div class="tf-stat-val">{s['value']}{s['suffix']}</div>
  <div class="tf-stat-lbl">{s['label']}</div>
</div>""" for s in STATS])

    st.markdown(f"""
<section class="tf-section tf-section-alt" id="stats">
  <div class="tf-stats-grid">{cards}</div>
</section>
""", unsafe_allow_html=True)


def render_services():
    cards = "".join([f"""
<div class="tf-service-card">
  <div class="tf-service-icon">{s['icon']}</div>
  <div class="tf-service-title">{s['title']}</div>
  <div class="tf-service-desc">{s['desc']}</div>
</div>""" for s in SERVICES])

    st.markdown(f"""
<section class="tf-section" id="services">
  <div class="tf-section-header">
    <span class="tf-eyebrow">What We Do</span>
    <h2 class="tf-section-title">Services Built for <span style="color:#00BFFF;">Real Results</span></h2>
    <p class="tf-section-sub">From AI-powered applications to final-year projects — we build software that works, scales, and impresses.</p>
  </div>
  <div class="tf-services-grid">{cards}</div>
</section>
""", unsafe_allow_html=True)


def render_projects():
    cards = ""
    for p in PROJECTS:
        tech_tags = "".join([f'<span class="tf-tech-tag">{t}</span>' for t in p["tech"]])
        features = "".join([f'<li>{f}</li>' for f in p["features"]])
        status_class = "tf-status-live" if p["status"] == "Live" else "tf-status-progress"
        status_dot = "🟢" if p["status"] == "Live" else "🔵"
        cards += f"""
<div class="tf-project-card">
  <div class="tf-project-top">
    <div class="tf-project-emoji-wrap" style="background:rgba(0,0,0,.3);border:1px solid {p['color']}33;">
      {p['emoji']}
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:.6rem;">
      <div class="tf-project-title">{p['title']}</div>
      <span class="tf-project-status {status_class}">{status_dot} {p['status']}</span>
    </div>
    <div class="tf-project-desc">{p['desc']}</div>
  </div>
  <div class="tf-project-bottom">
    <div class="tf-project-tech">{tech_tags}</div>
    <ul class="tf-project-features">{features}</ul>
  </div>
</div>"""

    st.markdown(f"""
<section class="tf-section tf-section-alt" id="projects">
  <div class="tf-section-header">
    <span class="tf-eyebrow">Our Work</span>
    <h2 class="tf-section-title">Projects That <span style="color:#00BFFF;">Speak for Themselves</span></h2>
    <p class="tf-section-sub">Real systems. Real clients. Real results. Every project is production-ready and fully documented.</p>
  </div>
  <div class="tf-projects-grid">{cards}</div>
</section>
""", unsafe_allow_html=True)


def render_about():
    founder_src = f"data:image/jpeg;base64,{FOUNDER_B64}" if FOUNDER_B64 else ""
    img_html = f'<img src="{founder_src}" alt="TECHFAM Founder" class="tf-about-img">' if founder_src else ""

    tags = "".join([f'<span class="tf-tag">{t}</span>' for t in
                    ["Python Expert", "AI Engineer", "Full-Stack Dev", "Nigeria 🇳🇬",
                     "100% Remote", "Final-Year Specialist", "3+ Years Experience"]])

    st.markdown(f"""
<section class="tf-section" id="about">
  <div class="tf-about-grid">
    <div class="tf-about-img-wrap">
      {img_html}
      <div class="tf-about-img-overlay">
        <div class="tf-about-metric">
          <div class="tf-about-metric-val">120+</div>
          <div class="tf-about-metric-lbl">Projects</div>
        </div>
        <div class="tf-about-metric">
          <div class="tf-about-metric-val">95+</div>
          <div class="tf-about-metric-lbl">Clients</div>
        </div>
        <div class="tf-about-metric">
          <div class="tf-about-metric-val">100%</div>
          <div class="tf-about-metric-lbl">Remote</div>
        </div>
      </div>
    </div>
    <div class="tf-about-text">
      <span class="tf-eyebrow">About TECHFAM</span>
      <h2>Built in Nigeria.<br>Trusted <span style="color:#00BFFF;">Worldwide.</span></h2>
      <p>TECHFAM is a software development agency founded with one mission: deliver world-class software at accessible prices. We specialize in Python applications, AI systems, web development, and complete final-year projects.</p>
      <p>We work 100% remotely with clients across Nigeria, Ghana, UK, USA, Canada, and beyond — delivering production-ready systems that actually work and impress.</p>
      <p>Whether you're a student needing a final-year project, a startup building an MVP, or an enterprise automating workflows — TECHFAM has you covered.</p>
      <div class="tf-about-tags">{tags}</div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)


def render_why_us():
    cards = "".join([f"""
<div class="tf-why-card">
  <div class="tf-why-icon">{w['icon']}</div>
  <div class="tf-why-title">{w['title']}</div>
  <div class="tf-why-desc">{w['desc']}</div>
</div>""" for w in WHY_US])

    st.markdown(f"""
<section class="tf-section tf-section-alt" id="why">
  <div class="tf-section-header">
    <span class="tf-eyebrow">Why TECHFAM</span>
    <h2 class="tf-section-title">Why 95+ Clients <span style="color:#00BFFF;">Choose Us</span></h2>
    <p class="tf-section-sub">We're not just coders. We're partners invested in your success.</p>
  </div>
  <div class="tf-whyus-grid">{cards}</div>
</section>
""", unsafe_allow_html=True)


def render_testimonials():
    cards = "".join([f"""
<div class="tf-testi-card">
  <div class="tf-testi-stars">{'★' * t['rating']}</div>
  <p class="tf-testi-text">"{t['text']}"</p>
  <div class="tf-testi-author">
    <div class="tf-testi-avatar" style="background:{t['color']};">{t['avatar']}</div>
    <div>
      <div class="tf-testi-name">{t['name']}</div>
      <div class="tf-testi-role">{t['role']}</div>
    </div>
  </div>
</div>""" for t in TESTIMONIALS])

    st.markdown(f"""
<section class="tf-section" id="testimonials">
  <div class="tf-section-header">
    <span class="tf-eyebrow">Testimonials</span>
    <h2 class="tf-section-title">What Our <span style="color:#00BFFF;">Clients Say</span></h2>
    <p class="tf-section-sub">Don't take our word for it. Here's what clients across Africa and beyond say about working with TECHFAM.</p>
  </div>
  <div class="tf-testi-grid">{cards}</div>
</section>
""", unsafe_allow_html=True)


def render_pricing():
    cards = ""
    for p in PRICING:
        badge = '<div class="tf-price-badge">⭐ Most Popular</div>' if p["featured"] else ""
        featured_class = "featured" if p["featured"] else ""
        btn_class = "tf-price-btn-primary" if p["featured"] else "tf-price-btn-outline"
        color = p["color"]
        features = "".join([f'<li>{f}</li>' for f in p["features"]])
        cards += f"""
<div class="tf-price-card {featured_class}" style="border-color:{'var(--blue)' if p['featured'] else 'rgba(255,255,255,.08)'};">
  {badge}
  <div class="tf-price-name" style="color:{color};">{p['name']}</div>
  <div class="tf-price-desc">{p['desc']}</div>
  <div class="tf-price-amount">{p['price']}</div>
  <div class="tf-price-usd">{p['usd']}</div>
  <ul class="tf-price-features">{features}</ul>
  <button class="tf-price-btn {btn_class}">Get Started →</button>
</div>"""

    st.markdown(f"""
<section class="tf-section tf-section-alt" id="pricing">
  <div class="tf-section-header">
    <span class="tf-eyebrow">Pricing</span>
    <h2 class="tf-section-title">Transparent <span style="color:#00BFFF;">Pricing</span></h2>
    <p class="tf-section-sub">World-class software at fair prices. No hidden fees, no surprises.</p>
  </div>
  <div class="tf-pricing-grid">{cards}</div>
</section>
""", unsafe_allow_html=True)


def render_technologies():
    items = "".join([f"""
<div class="tf-tech-item">
  <div class="tf-tech-emoji">{t['icon']}</div>
  <div class="tf-tech-name">{t['name']}</div>
</div>""" for t in TECHNOLOGIES])

    st.markdown(f"""
<section class="tf-section" id="tech">
  <div class="tf-section-header">
    <span class="tf-eyebrow">Tech Stack</span>
    <h2 class="tf-section-title">Technologies We <span style="color:#00BFFF;">Master</span></h2>
    <p class="tf-section-sub">We stay current with the tools that power modern software — from AI to deployment.</p>
  </div>
  <div class="tf-tech-grid">{items}</div>
</section>
""", unsafe_allow_html=True)


def render_process():
    steps = "".join([f"""
<div class="tf-process-step">
  <div class="tf-process-num">{s['step']}</div>
  <div class="tf-process-icon">{s['icon']}</div>
  <div class="tf-process-title">{s['title']}</div>
  <div class="tf-process-desc">{s['desc']}</div>
</div>""" for s in PROCESS])

    st.markdown(f"""
<section class="tf-section tf-section-alt" id="process">
  <div class="tf-section-header">
    <span class="tf-eyebrow">How We Work</span>
    <h2 class="tf-section-title">Our <span style="color:#00BFFF;">Process</span></h2>
    <p class="tf-section-sub">A clear, structured process that keeps you informed and in control at every step.</p>
  </div>
  <div class="tf-process-grid">{steps}</div>
</section>
""", unsafe_allow_html=True)


def render_faq():
    items = ""
    for i, (q, a) in enumerate(FAQS):
        items += f"""
<div class="tf-faq-item">
  <div class="tf-faq-q">
    <span>{q}</span>
    <span style="color:#00BFFF;font-size:1.2rem;">+</span>
  </div>
  <div class="tf-faq-a">{a}</div>
</div>"""

    st.markdown(f"""
<section class="tf-section" id="faq">
  <div class="tf-section-header">
    <span class="tf-eyebrow">FAQ</span>
    <h2 class="tf-section-title">Common <span style="color:#00BFFF;">Questions</span></h2>
    <p class="tf-section-sub">Everything you need to know before working with us.</p>
  </div>
  <div style="max-width:780px;margin:0 auto;">{items}</div>
</section>
""", unsafe_allow_html=True)


def render_contact():
    founder_thumb_src = f"data:image/jpeg;base64,{FOUNDER_THUMB_B64}" if FOUNDER_THUMB_B64 else ""

    social_links = "".join([
        f'<a class="tf-contact-link" href="{v["url"]}" target="_blank"><span class="tf-contact-link-icon">{v["icon"]}</span>{k}</a>'
        for k, v in SOCIAL_LINKS.items()
    ])

    founder_card = f"""
<div class="tf-contact-founder">
  <img src="{founder_thumb_src}" alt="Founder">
</div>""" if founder_thumb_src else ""

    st.markdown(f"""
<section class="tf-section tf-section-alt" id="contact">
  <div class="tf-section-header">
    <span class="tf-eyebrow">Get In Touch</span>
    <h2 class="tf-section-title">Let's Build <span style="color:#00BFFF;">Something Great</span></h2>
    <p class="tf-section-sub">Tell us about your project and we'll respond within 2 hours with a free consultation.</p>
  </div>
  <div class="tf-contact-grid">
    <div class="tf-contact-info">
      <h3>Talk to us.<br>We don't bite. 😄</h3>
      <p>Whether you have a rough idea or a detailed spec — reach out. We'll help you figure out the best path forward, for free, with no commitment required.</p>
      {social_links}
      {founder_card}
    </div>
""", unsafe_allow_html=True)

    # Streamlit form
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name *", placeholder="John Doe")
        with col2:
            email = st.text_input("Email Address *", placeholder="john@example.com")

        col3, col4 = st.columns(2)
        with col3:
            telegram = st.text_input("Telegram Username", placeholder="@johndoe")
        with col4:
            phone = st.text_input("Phone Number", placeholder="+234 800 000 0000")

        col5, col6 = st.columns(2)
        with col5:
            project_type = st.selectbox("Project Type", [
                "— Select Project Type —",
                "Final-Year Project", "Web Application", "AI Chatbot",
                "Business Software", "Mobile App", "Automation Script",
                "API Development", "Database Design", "Other"
            ])
        with col6:
            budget = st.selectbox("Budget Range", [
                "— Select Budget —",
                "Under ₦50,000", "₦50,000 – ₦150,000",
                "₦150,000 – ₦500,000", "₦500,000+", "Custom / Let's discuss"
            ])

        deadline = st.text_input("Deadline / Timeline", placeholder="e.g. 2 weeks, ASAP, by December 2025")
        description = st.text_area("Project Description *", placeholder="Describe your project in detail. What does it need to do? Who will use it? Any special requirements?", height=140)
        uploaded = st.file_uploader("Attach File (optional — brief, mockup, dataset)", type=["pdf", "docx", "png", "jpg", "zip", "csv"])

        submitted = st.form_submit_button("⚡ Send Message — Get Free Consultation")

        if submitted:
            if not name or not email or not description:
                st.error("Please fill in your name, email, and project description.")
            else:
                st.success(f"""
✅ **Message received, {name.split()[0]}!**

We'll review your project and respond to **{email}** within 2 hours.

For urgent projects, message us directly on Telegram: **@techfam**

Thank you for choosing TECHFAM! 🚀
""")

    st.markdown("</div></section>", unsafe_allow_html=True)


def render_cta():
    st.markdown("""
<div class="tf-cta">
  <h2>Ready to Build Something <span style="color:#00BFFF;">Amazing?</span></h2>
  <p>Join 95+ clients who trusted TECHFAM to turn their ideas into reality. First consultation is always free.</p>
  <div class="tf-cta-btns">
    <a class="btn-primary" href="#contact">⚡ Start Your Project</a>
    <a class="btn-secondary" href="#projects">🚀 See Our Work</a>
  </div>
</div>
""", unsafe_allow_html=True)


def render_footer():
    logo_src = f"data:image/png;base64,{LOGO_B64}" if LOGO_B64 else ""
    logo_html = f'<img src="{logo_src}" style="height:38px;" alt="TECHFAM">' if logo_src else '<span style="font-family:Space Grotesk;font-weight:800;font-size:1.4rem;color:#00BFFF;">TECHFAM</span>'

    socials = "".join([
        f'<a class="tf-social-btn" href="{v["url"]}" target="_blank" title="{k}">{v["icon"]}</a>'
        for k, v in SOCIAL_LINKS.items()
    ])

    st.markdown(f"""
<footer class="tf-footer" id="footer">
  <div class="tf-footer-grid">
    <div class="tf-footer-brand">
      {logo_html}
      <p>Nigeria's premium software development agency. We build AI apps, web platforms, business systems, and final-year projects that actually work.</p>
      <div class="tf-footer-social" style="margin-top:1.25rem;">{socials}</div>
    </div>
    <div class="tf-footer-col">
      <h4>Services</h4>
      <ul>
        <li><a href="#services">AI Chatbots</a></li>
        <li><a href="#services">Web Development</a></li>
        <li><a href="#services">Python Apps</a></li>
        <li><a href="#services">Final-Year Projects</a></li>
        <li><a href="#services">Machine Learning</a></li>
        <li><a href="#services">API Development</a></li>
      </ul>
    </div>
    <div class="tf-footer-col">
      <h4>Company</h4>
      <ul>
        <li><a href="#about">About Us</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#testimonials">Testimonials</a></li>
        <li><a href="#process">Our Process</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </div>
    <div class="tf-footer-col">
      <h4>Contact</h4>
      <ul>
        <li><a href="https://t.me/techfam">📱 Telegram</a></li>
        <li><a href="https://wa.me/2348000000000">💬 WhatsApp</a></li>
        <li><a href="mailto:hello@techfam.dev">📧 Email Us</a></li>
        <li><a href="#faq">❓ FAQ</a></li>
      </ul>
    </div>
  </div>
  <div class="tf-footer-bottom">
    <span class="tf-footer-copy">© 2025 TECHFAM. All rights reserved. Built in Nigeria 🇳🇬 for the world.</span>
    <span class="tf-footer-copy">We Build Solutions. You Get Results.</span>
  </div>
</footer>
""", unsafe_allow_html=True)


# ── Main App ───────────────────────────────────────────────────────────────────
def main():
    inject_css()
    render_navbar()
    render_hero()
    render_stats()
    render_services()
    render_projects()
    render_about()
    render_why_us()
    render_testimonials()
    render_pricing()
    render_technologies()
    render_process()
    render_faq()
    render_contact()
    render_cta()
    render_footer()


if __name__ == "__main__":
    main()
