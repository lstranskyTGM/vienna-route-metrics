"""
Vienna Route Metrics - Main Streamlit Application
TU Wien | Denkweisen der Informatik
"""

import streamlit as st
from config import MODE_LABELS

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="Vienna Route Metrics",
    page_icon="🚇",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CUSTOM CSS
# =============================================================================
st.markdown("""
    <style>
    /* ===== SIDEBAR STYLES ===== */
    [data-testid="stSidebar"] .stMarkdown hr {
        margin: 0.75rem 0;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.75rem;
    }

    /* ===== BUTTON STYLES ===== */
    .stButton > button[kind="primary"] {
        background-color: #0D9488;
        border-color: #0D9488;
        color: white;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #0F766E;
        border-color: #0F766E;
        color: white;
    }

    .stButton > button[kind="primary"]:focus {
        box-shadow: 0 0 0 0.2rem rgba(13, 148, 136, 0.4);
    }

    .stButton > button[kind="primary"]:active {
        background-color: #115E59;
        border-color: #115E59;
    }

    /* ===== MAP PLACEHOLDER STYLES ===== */
    .map-placeholder {
        width: 100%;
        height: 400px;
        background-color: #E5E7EB;
        border: 2px dashed #9CA3AF;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #6B7280;
        font-size: 1.1rem;
    }

    /* ===== FOOTER STYLES ===== */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #1A1F2C;
        padding: 10px;
        text-align: center;
        font-size: 0.8rem;
        color: #6B7280;
    }
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# SIDEBAR - INPUT SECTION
# =============================================================================
with st.sidebar:
    st.header("Route eingeben")
    st.markdown("---")

    start_address = st.text_input(
        label="Startadresse",
        placeholder="z.B. Stephansplatz, Wien",
    )

    destination_address = st.text_input(
        label="Zieladresse",
        placeholder="z.B. TU Wien Hauptgebäude",
    )

    st.markdown("---")

    compare_button = st.button(
        label="🔍 Routen vergleichen",
        type="primary",
        use_container_width=True
    )

# =============================================================================
# MAIN CONTENT AREA
# =============================================================================
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("📊 Vergleichsergebnisse")
    results_placeholder = st.empty()

with col_right:
    st.subheader("🗺️ Routenkarte")
    map_placeholder = st.empty()

# =============================================================================
# BUTTON CLICK HANDLER
# =============================================================================
if compare_button:
    if not start_address or not destination_address:
        st.sidebar.error("⚠️ Bitte geben Sie Start- und Zieladresse ein.")
    else:
        with st.spinner("Routen werden berechnet..."):
            # Placeholder for results table
            with results_placeholder.container():
                st.info(
                    f"🔄 **Route wird berechnet...**\n\n"
                    f"**Von:** {start_address}\n\n"
                    f"**Nach:** {destination_address}"
                )

                st.markdown("#### Vorschau der Ergebnistabelle (Platzhalter)")

                import pandas as pd
                placeholder_data = {
                    "Verkehrsmittel": [MODE_LABELS['driving'], MODE_LABELS['transit'],
                                       MODE_LABELS['bicycling'], MODE_LABELS['walking']],
                    "Dauer": ["-- min", "-- min", "-- min", "-- min"],
                    "Distanz": ["-- km", "-- km", "-- km", "-- km"],
                    "CO₂":  ["-- g", "-- g", "-- g", "-- g"],
                    "Kosten":  ["-- €", "-- €", "-- €", "-- €"]
                }
                placeholder_df = pd.DataFrame(placeholder_data)
                st.table(placeholder_df)

                st.warning("**API-Integration ausstehend**")

            # Placeholder for map
            with map_placeholder.container():
                st.info("**Kartenansicht (Platzhalter)**")
                st.markdown(
                    '<div class="map-placeholder">Karte wird hier angezeigt</div>',
                    unsafe_allow_html=True
                )
else:
    with results_placeholder.container():
        st.info(
            "Geben Sie Start- und Zieladresse in der Seitenleiste ein "
            "und klicken Sie auf **'Routen vergleichen'**."
        )

    with map_placeholder.container():
        st.info(
            "Nach der Routenberechnung wird hier eine interaktive Karte "
            "mit allen Routen angezeigt."
        )

# =============================================================================
# FOOTER
# =============================================================================
st.markdown(
    '<div class="footer"><strong>TU Wien</strong> | Denkweisen der Informatik</div>',
    unsafe_allow_html=True
)