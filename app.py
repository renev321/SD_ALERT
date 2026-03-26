import base64
import streamlit as st

st.set_page_config(
    page_title="WLF Signals Premium",
    page_icon="📈",
    layout="wide",
)

# -----------------------------
# Helpers
# -----------------------------
def get_base64(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_path = "Logo.png"
chart_path = "SIgnsSupplyDemmand.jpg"

logo_b64 = get_base64(logo_path)
chart_b64 = get_base64(chart_path)

stripe_payment_link = "https://buy.stripe.com/cNieVc4d96uu13x9OvaIM00"

# -----------------------------
# Premium CSS
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(20,90,40,0.22), transparent 28%),
            radial-gradient(circle at top right, rgba(180,140,40,0.16), transparent 22%),
            linear-gradient(135deg, #050505 0%, #0a0a0a 35%, #101313 100%);
        color: #f5f5f5;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1350px;
    }

    .hero-card {
        background: linear-gradient(145deg, rgba(18,18,18,0.92), rgba(10,10,10,0.86));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 28px;
        padding: 36px 38px;
        box-shadow:
            0 0 0 1px rgba(255,255,255,0.02) inset,
            0 20px 60px rgba(0,0,0,0.45);
        backdrop-filter: blur(10px);
    }

    .chart-card {
        background: linear-gradient(145deg, rgba(15,15,15,0.96), rgba(8,8,8,0.92));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 28px;
        padding: 20px;
        box-shadow:
            0 0 0 1px rgba(255,255,255,0.02) inset,
            0 20px 60px rgba(0,0,0,0.45);
    }

    .mini-badge {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: linear-gradient(90deg, rgba(18,96,47,0.32), rgba(184,148,52,0.22));
        border: 1px solid rgba(212,175,55,0.18);
        color: #d8d8d8;
        font-size: 0.88rem;
        letter-spacing: 0.4px;
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 3.4rem;
        line-height: 1.02;
        font-weight: 800;
        margin: 0 0 14px 0;
        color: #f7f7f7;
    }

    .hero-title .accent {
        background: linear-gradient(90deg, #ffffff 0%, #b7ffca 35%, #d6b25e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-sub {
        font-size: 1.12rem;
        color: #bcbcbc;
        line-height: 1.75;
        margin-bottom: 26px;
        max-width: 780px;
    }

    .benefit-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 14px;
        margin-top: 20px;
        margin-bottom: 28px;
    }

    .benefit-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.03), rgba(255,255,255,0.015));
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 16px 18px;
    }

    .benefit-title {
        font-weight: 700;
        font-size: 1rem;
        color: #f3f3f3;
        margin-bottom: 6px;
    }

    .benefit-text {
        font-size: 0.95rem;
        color: #b5b5b5;
        line-height: 1.55;
    }

    .price-box {
        margin-top: 12px;
        margin-bottom: 24px;
        padding: 18px 20px;
        border-radius: 18px;
        background: linear-gradient(90deg, rgba(20,20,20,0.95), rgba(14,36,22,0.82));
        border: 1px solid rgba(119,255,169,0.10);
    }

    .price-main {
        font-size: 1.1rem;
        color: #e8e8e8;
        font-weight: 700;
    }

    .price-sub {
        color: #aaaaaa;
        margin-top: 6px;
        font-size: 0.95rem;
    }

    .premium-note {
        margin-top: 18px;
        color: #c2c2c2;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .chart-image {
        width: 100%;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.05);
        box-shadow: 0 12px 36px rgba(0,0,0,0.35);
    }

    .logo-wrap {
        margin-bottom: 22px;
    }

    .logo-wrap img {
        width: 240px;
        max-width: 100%;
        display: block;
    }

    .section-label {
        color: #d3a84a;
        font-size: 0.86rem;
        text-transform: uppercase;
        letter-spacing: 1.4px;
        font-weight: 700;
        margin-bottom: 14px;
    }

    div.stLinkButton > a {
        background: linear-gradient(90deg, #0c8f43 0%, #16b85a 45%, #d4a94b 100%);
        color: white !important;
        border: none !important;
        border-radius: 18px !important;
        padding: 0.95rem 1.2rem !important;
        font-weight: 800 !important;
        font-size: 1.02rem !important;
        box-shadow: 0 10px 28px rgba(22,184,90,0.22);
        transition: all 0.2s ease-in-out;
    }

    div.stLinkButton > a:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 36px rgba(212,169,75,0.22);
    }

    .footer-box {
        margin-top: 22px;
        padding: 16px 18px;
        border-radius: 16px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        color: #bdbdbd;
        line-height: 1.65;
        font-size: 0.93rem;
    }

    @media (max-width: 900px) {
        .hero-title {
            font-size: 2.4rem;
        }

        .benefit-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([1.08, 0.92], gap="large")

with left:
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="logo-wrap">
            <img src="data:image/png;base64,{logo_b64}">
        </div>

        <div class="mini-badge">Entrega Exclusiva • WLF Trading</div>

        <div class="hero-title">
            Señales <span class="accent">Premium</span><br>
            con una experiencia de alto nivel.
        </div>

        <div class="hero-sub">
            Únete a la experiencia premium de WLF Trading y recibe señales de trading
            de alta calidad a través de un flujo exclusivo para suscriptores, diseñado
            para transmitir seriedad, elegancia y profesionalismo desde el primer momento.
        </div>

        <div class="price-box">
            <div class="price-main">Acceso premium mensual mediante suscripción con Stripe</div>
            <div class="price-sub">Pago simple. Acceso exclusivo para suscriptores. Flujo profesional y privado.</div>
        </div>

        <div class="benefit-grid">
            <div class="benefit-card">
                <div class="benefit-title">Entrega Precisa</div>
                <div class="benefit-text">Recibe señales claras con entradas, stop loss y objetivos bien estructurados.</div>
            </div>
            <div class="benefit-card">
                <div class="benefit-title">Acceso Exclusivo</div>
                <div class="benefit-text">Las señales están reservadas únicamente para miembros suscritos dentro de una experiencia más selecta.</div>
            </div>
            <div class="benefit-card">
                <div class="benefit-title">Identidad WLF</div>
                <div class="benefit-text">Una presentación visual pulida que refleja tu marca de trading y tu profesionalismo.</div>
            </div>
            <div class="benefit-card">
                <div class="benefit-title">Preparado para Escalar</div>
                <div class="benefit-text">Este frontend está listo para conectarse más adelante con Telegram y validación automática de suscripción.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "Desbloquear Acceso Premium",
        stripe_payment_link,
        type="primary",
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="premium-note">
            Después de suscribirse, el usuario pasará al siguiente paso del proceso para conectar su canal privado de recepción de señales.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="footer-box">
            Esta página es tu punto de entrada premium. La siguiente etapa conectará la validación del pago con la entrega privada de señales únicamente para suscriptores activos.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Vista previa de señales WLF</div>', unsafe_allow_html=True)
    st.markdown(
        f'<img class="chart-image" src="data:image/jpeg;base64,{chart_b64}">',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
