import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="WLF Signals Premium",
    page_icon="📈",
    layout="wide",
)

# -----------------------------
# CONFIG
# -----------------------------
stripe_payment_link = "https://buy.stripe.com/cNieVc4d96uu13x9OvaIM00"

logo = Image.open("Logo.png")
chart_img = Image.open("SIgnsSupplyDemmand.jpg")

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
/* Fondo general */
.stApp {
    background:
        radial-gradient(circle at top left, rgba(14, 85, 45, 0.22), transparent 28%),
        radial-gradient(circle at top right, rgba(180, 145, 50, 0.14), transparent 22%),
        linear-gradient(135deg, #050505 0%, #090909 38%, #101313 100%);
    color: #f5f5f5;
}

/* Contenedor principal */
.block-container {
    max-width: 1380px;
    padding-top: 2.2rem;
    padding-bottom: 2.5rem;
}

/* Más aire arriba entre bloques */
div[data-testid="stVerticalBlock"] > div:has(div.section-card) {
    margin-bottom: 1rem;
}

/* Tarjetas premium */
.section-card {
    background: linear-gradient(145deg, rgba(18,18,18,0.94), rgba(9,9,9,0.90));
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 28px;
    padding: 34px 34px 30px 34px;
    box-shadow:
        0 0 0 1px rgba(255,255,255,0.02) inset,
        0 22px 55px rgba(0,0,0,0.42);
}

/* Badge */
.badge {
    display: inline-block;
    padding: 9px 16px;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(17,94,48,0.34), rgba(183,147,53,0.22));
    border: 1px solid rgba(212,175,55,0.18);
    color: #e7e7e7;
    font-size: 0.90rem;
    letter-spacing: 0.3px;
    margin-bottom: 20px;
}

/* Título */
.hero-title {
    font-size: 3.35rem;
    line-height: 1.02;
    font-weight: 800;
    margin-bottom: 18px;
    color: #f7f7f7;
}

.hero-accent {
    background: linear-gradient(90deg, #ffffff 0%, #bfffcf 38%, #d7b462 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Párrafos */
.hero-text {
    color: #c7c7c7;
    font-size: 1.10rem;
    line-height: 1.8;
    margin-bottom: 26px;
}

/* Caja de precio */
.price-box {
    background: linear-gradient(90deg, rgba(20,20,20,0.96), rgba(11,34,20,0.90));
    border: 1px solid rgba(110, 255, 164, 0.10);
    border-radius: 18px;
    padding: 18px 20px;
    margin-bottom: 26px;
}

.price-title {
    color: #f0f0f0;
    font-weight: 700;
    font-size: 1.15rem;
    margin-bottom: 6px;
}

.price-text {
    color: #b9b9b9;
    font-size: 0.97rem;
    line-height: 1.6;
}

/* Grid de beneficios */
.benefit-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
    margin-top: 10px;
    margin-bottom: 28px;
}

.benefit-item {
    background: linear-gradient(145deg, rgba(255,255,255,0.03), rgba(255,255,255,0.015));
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 18px;
}

.benefit-item-title {
    color: #f3f3f3;
    font-size: 1.02rem;
    font-weight: 700;
    margin-bottom: 8px;
}

.benefit-item-text {
    color: #b7b7b7;
    font-size: 0.95rem;
    line-height: 1.65;
}

/* Título lateral derecho */
.side-label {
    color: #d8ae52;
    font-size: 0.88rem;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    font-weight: 800;
    margin-bottom: 16px;
}

/* Botón */
div.stLinkButton > a {
    background: linear-gradient(90deg, #0d8d43 0%, #18b95d 42%, #d8ad52 100%);
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    padding: 0.95rem 1.2rem !important;
    font-weight: 800 !important;
    font-size: 1.03rem !important;
    box-shadow: 0 12px 30px rgba(24,185,93,0.20);
    text-decoration: none !important;
}

div.stLinkButton > a:hover {
    box-shadow: 0 15px 34px rgba(216,173,82,0.22);
    transform: translateY(-1px);
}

/* Notas */
.note-box {
    margin-top: 18px;
    padding: 16px 18px;
    border-radius: 16px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.05);
    color: #c0c0c0;
    line-height: 1.7;
    font-size: 0.95rem;
}

/* Ajustes de imágenes */
.logo-wrapper {
    margin-bottom: 10px;
}

.logo-subtitle {
    color: #8f949a;
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 0.6px;
    margin-top: 2px;
    margin-bottom: 26px;
    text-shadow: 0 0 10px rgba(255,255,255,0.04);
}

.chart-frame {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0 14px 36px rgba(0,0,0,0.34);
}

/* Responsive */
@media (max-width: 900px) {
    .hero-title {
        font-size: 2.35rem;
    }

    .benefit-grid {
        grid-template-columns: 1fr;
    }

    .section-card {
        padding: 24px 22px;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LAYOUT
# -----------------------------
left, right = st.columns([1.08, 0.92], gap="large")

with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.image(logo, width=165)
    st.markdown('<div class="logo-subtitle">WLF TRADING</div>', unsafe_allow_html=True)

    st.markdown('<div class="badge">Entrega Exclusiva • WLF Trading</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="hero-title">Señales <span class="hero-accent">Premium</span><br>con una experiencia de alto nivel.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-text">
            Únete a la experiencia premium de WLF Trading y recibe señales de trading
            de alta calidad a través de un flujo exclusivo para suscriptores, diseñado
            para transmitir seriedad, elegancia y profesionalismo desde el primer momento.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="price-box">
            <div class="price-title">Acceso premium mensual mediante suscripción con Stripe</div>
            <div class="price-text">
                Pago simple, acceso exclusivo para suscriptores y una experiencia privada
                orientada a una entrega más profesional.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="benefit-grid">
            <div class="benefit-item">
                <div class="benefit-item-title">Entrega Precisa</div>
                <div class="benefit-item-text">Recibe señales claras con entradas, stop loss y objetivos bien estructurados.</div>
            </div>
            <div class="benefit-item">
                <div class="benefit-item-title">Acceso Exclusivo</div>
                <div class="benefit-item-text">Las señales están reservadas únicamente para miembros activos dentro de una experiencia más selecta.</div>
            </div>
            <div class="benefit-item">
                <div class="benefit-item-title">Identidad WLF</div>
                <div class="benefit-item-text">Una presentación visual premium que transmite marca, presencia y profesionalismo.</div>
            </div>
            <div class="benefit-item">
                <div class="benefit-item-title">Preparado para Escalar</div>
                <div class="benefit-item-text">Este frontend está listo para conectar después la validación de pago y la entrega privada.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Desbloquear Acceso Premium",
        stripe_payment_link,
        type="primary",
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="note-box">
            Después de suscribirse, el usuario podrá pasar al siguiente paso para conectar
            su canal privado de recepción de señales.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown('<div class="side-label">Ejemplo real de señal operativa</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-frame">', unsafe_allow_html=True)
    st.image(chart_img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="note-box">
            Ejemplo del tipo de señal que se envía cuando el precio crea, retestea,
            mitiga o invalida una zona relevante dentro de la estructura operativa.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)
