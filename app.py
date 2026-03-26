import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="WLF Signals Premium",
    page_icon="📈",
    layout="wide",
)

stripe_payment_link = "https://buy.stripe.com/cNieVc4d96uu13x9OvaIM00"

logo = Image.open("Logo.png")
chart_img = Image.open("SIgnsSupplyDemmand.jpg")

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(14, 95, 48, 0.18), transparent 24%),
        radial-gradient(circle at top right, rgba(196, 154, 45, 0.10), transparent 18%),
        linear-gradient(135deg, #040404 0%, #090909 40%, #101212 100%);
    color: #f5f5f5;
}

.block-container {
    max-width: 1380px;
    padding-top: 2.2rem;
    padding-bottom: 2.6rem;
}

/* Oculta bloques vacíos extraños de Streamlit */
div[data-testid="stVerticalBlock"] > div:empty,
div[data-testid="stHorizontalBlock"] > div:empty {
    display: none !important;
}

/* Tarjetas */
.clean-card {
    background: linear-gradient(145deg, rgba(16,16,16,0.95), rgba(8,8,8,0.92));
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 30px;
    padding: 36px;
    box-shadow:
        0 0 0 1px rgba(255,255,255,0.02) inset,
        0 24px 60px rgba(0,0,0,0.45);
}

/* Glow del logo */
.logo-glow {
    display: inline-block;
    padding: 14px 18px 8px 18px;
    border-radius: 24px;
    background:
        radial-gradient(circle, rgba(86,255,144,0.12) 0%, rgba(86,255,144,0.04) 40%, rgba(0,0,0,0) 72%);
    margin-bottom: 8px;
}

/* Texto debajo del logo */
.logo-subtitle {
    color: #c5ccd3;
    font-size: 1.02rem;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 26px;
}

/* Badge */
.lux-badge {
    display: inline-block;
    padding: 9px 16px;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(18,96,47,0.34), rgba(184,148,52,0.20));
    border: 1px solid rgba(212,175,55,0.16);
    color: #ececec;
    font-size: 0.90rem;
    margin-bottom: 22px;
}

/* Título */
.hero-title {
    font-size: 3.4rem;
    line-height: 1.02;
    font-weight: 800;
    margin-bottom: 18px;
    color: #f8f8f8;
}

.hero-accent {
    background: linear-gradient(90deg, #ffffff 0%, #c2ffd0 38%, #ddb968 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-text {
    color: #c7c7c7;
    font-size: 1.08rem;
    line-height: 1.85;
    margin-bottom: 26px;
    max-width: 90%;
}

/* Caja de suscripción */
.offer-box {
    background: linear-gradient(90deg, rgba(18,18,18,0.98), rgba(8,38,22,0.88));
    border: 1px solid rgba(110,255,164,0.08);
    border-radius: 20px;
    padding: 20px 22px;
    margin-bottom: 22px;
}

.offer-title {
    color: #f1f1f1;
    font-weight: 700;
    font-size: 1.12rem;
    margin-bottom: 6px;
}

.offer-text {
    color: #bbbbbb;
    font-size: 0.97rem;
    line-height: 1.7;
}

/* Botón */
div.stLinkButton > a {
    background: linear-gradient(90deg, #0d8d43 0%, #18b95d 44%, #d8ad52 100%);
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    padding: 1rem 1.2rem !important;
    font-weight: 800 !important;
    font-size: 1.03rem !important;
    box-shadow: 0 12px 30px rgba(24,185,93,0.20);
    text-decoration: none !important;
}

div.stLinkButton > a:hover {
    transform: translateY(-1px);
    box-shadow: 0 16px 34px rgba(216,173,82,0.22);
}

/* Etiqueta derecha */
.side-label {
    color: #d8ae52;
    font-size: 0.88rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 800;
    margin-bottom: 18px;
}

/* Imagen */
.chart-frame {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 14px 36px rgba(0,0,0,0.34);
    margin-bottom: 18px;
}

/* Nota */
.soft-note {
    color: #bcbcbc;
    font-size: 0.96rem;
    line-height: 1.75;
}

/* Responsive */
@media (max-width: 900px) {
    .hero-title {
        font-size: 2.4rem;
    }

    .clean-card {
        padding: 24px;
    }

    .hero-text {
        max-width: 100%;
    }
}
</style>
""", unsafe_allow_html=True)

left, right = st.columns([1.06, 0.94], gap="large")

with left:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)

    st.markdown('<div class="logo-glow">', unsafe_allow_html=True)
    st.image(logo, width=165)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="logo-subtitle">WLF TRADING</div>', unsafe_allow_html=True)
    st.markdown('<div class="lux-badge">Acceso privado • WLF Trading</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="hero-title">Señales <span class="hero-accent">Premium</span><br>con presencia, claridad y nivel.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-text">
            Accede a un servicio exclusivo de señales con una presentación cuidada,
            una identidad sólida y una experiencia pensada para transmitir seriedad
            desde el primer vistazo.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="offer-box">
            <div class="offer-title">Suscripción mensual con Stripe</div>
            <div class="offer-text">
                Acceso privado para miembros activos. Pago simple, proceso limpio y
                una experiencia premium alineada con la identidad de WLF Trading.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Desbloquear acceso premium",
        stripe_payment_link,
        type="primary",
        use_container_width=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)

    st.markdown('<div class="side-label">Ejemplo real de señal enviada</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-frame">', unsafe_allow_html=True)
    st.image(chart_img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="soft-note">
            Ejemplo del tipo de señal que se envía cuando el precio crea,
            retestea, mitiga o invalida una zona relevante dentro de la estructura operativa.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)
