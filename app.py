
# app.py
import streamlit as st
from pathlib import Path

# ---- CONFIGURACIÓN BÁSICA ----
st.set_page_config(
    page_title="Tesis PCA - Dashboard Interactivo",
    page_icon="📊",
    layout="wide"
)

RUTA_BASE = Path(__file__).parent
DIR_HTML = RUTA_BASE / "html"
DIR_PNG = RUTA_BASE / "png"
DIR_EXCEL = RUTA_BASE / "excel"

st.markdown("""
# Reporte de Tesis Doctoral
**Propensión Conductual al Ahorro y Sesgos Cognitivos**

> Esta versión en Streamlit integra los interactivos (Plotly HTML), imágenes y descargas de Excel.
""")

# ---- PANEL LATERAL ----
st.sidebar.header("📁 Navegación")
opcion = st.sidebar.radio(
    "Selecciona una vista",
    [
        "1) Network de Sesgos",
        "2) Sankey de Flujos",
        "3) Radar Comparativo",
        "4) Hexbin PCA vs PSE",
        "5) Violin + Swarm",
        "6) Coordenadas Paralelas",
        "7) Treemap Jerárquico",
        "8) Ridgeline",
        "9) Matriz de Correlación",
        "10) PCA Biplot",
        "11) Scatter Matrix",
        "12) Heatmap Cuadrantes × Sesgos",
        "13) Boxplots Comparativos",
        "14) Dashboard Estadístico",
        "Descargas"
    ]
)

# Utilidad: incrustar un HTML interactivo de Plotly
def mostrar_html_interactivo(nombre_archivo_html: str, altura: int = 800):
    ruta = DIR_HTML / nombre_archivo_html
    if not ruta.exists():
        st.error(f"No se encontró el interactivo: {ruta}")
        return
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
    st.components.v1.html(contenido, height=altura, scrolling=True)

# Utilidad: mostrar una imagen PNG (como respaldo estático)
def mostrar_png(nombre_png: str, caption: str = None):
    ruta = DIR_PNG / nombre_png
    if not ruta.exists():
        st.warning(f"No se encontró la imagen: {ruta}")
        return
    st.image(str(ruta), caption=caption, use_column_width=True)

# ---- RUTAS por opción seleccionada ----
if opcion == "1) Network de Sesgos":
    st.subheader("1) Network de Sesgos")
    mostrar_html_interactivo("01_network_sesgos.html", altura=800)
    st.divider()
    mostrar_png("01_network_sesgos.png", "Versión estática (PNG)")

elif opcion == "2) Sankey de Flujos":
    st.subheader("2) Sankey de Flujos")
    mostrar_html_interactivo("02_sankey_flujos.html", altura=800)
    st.divider()
    mostrar_png("02_sankey_flujos.png")

elif opcion == "3) Radar Comparativo":
    st.subheader("3) Radar Comparativo")
    mostrar_html_interactivo("03_radar_comparativo.html", altura=800)
    st.divider()
    mostrar_png("03_radar_comparativo.png")

elif opcion == "4) Hexbin PCA vs PSE":
    st.subheader("4) Hexbin PCA vs PSE")
    mostrar_png("04_hexbin_densidad.png")

elif opcion == "5) Violin + Swarm":
    st.subheader("5) Violin + Swarm")
    mostrar_png("05_violin_swarm.png")

elif opcion == "6) Coordenadas Paralelas":
    st.subheader("6) Coordenadas Paralelas (Plotly Parcoords)")
    mostrar_html_interactivo("06_parallel_coordinates.html", altura=800)
    st.divider()
    mostrar_png("06_parallel_coordinates.png")

elif opcion == "7) Treemap Jerárquico":
    st.subheader("7) Treemap Jerárquico")
    mostrar_html_interactivo("07_treemap_jerarquico.html", altura=800)
    st.divider()
    mostrar_png("07_treemap_jerarquico.png")

elif opcion == "8) Ridgeline":
    st.subheader("8) Ridgeline")
    mostrar_png("08_ridgeline_plot.png")

elif opcion == "9) Matriz de Correlación":
    st.subheader("9) Matriz de Correlación avanzada")
    mostrar_png("09_matriz_correlacion_avanzada.png")

elif opcion == "10) PCA Biplot":
    st.subheader("10) PCA Biplot")
    mostrar_png("10_pca_biplot.png")

elif opcion == "11) Scatter Matrix":
    st.subheader("11) Scatter Matrix")
    mostrar_html_interactivo("11_scatter_matrix.html", altura=900)
    st.divider()
    mostrar_png("11_scatter_matrix.png")

elif opcion == "12) Heatmap Cuadrantes × Sesgos":
    st.subheader("12) Heatmap Cuadrantes × Sesgos")
    mostrar_png("12_heatmap_cuadrantes_sesgos.png")

elif opcion == "13) Boxplots Comparativos":
    st.subheader("13) Boxplots Comparativos (Mann-Whitney)")
    mostrar_png("13_boxplot_comparativo.png")

elif opcion == "14) Dashboard Estadístico":
    st.subheader("14) Dashboard Estadístico Consolidado")
    mostrar_html_interactivo("14_dashboard_estadistico.html", altura=900)
    st.divider()
    mostrar_png("14_dashboard_estadistico.png")

elif opcion == "Descargas":
    st.subheader("📥 Descargas (Excel)")
    # Ofrece los archivos Excel de tu carpeta `excel/` como download buttons
    excels = sorted(DIR_EXCEL.glob("*.xlsx"))
    if not excels:
        st.info("No se encontraron archivos Excel en la carpeta 'excel/'.")
    else:
        for ruta in excels:
            with open(ruta, "rb") as f:
                st.download_button(
                    label=f"Descargar {ruta.name}",
                    data=f.read(),
                    file_name=ruta.name,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

st.caption("© Tesis Doctoral — PCA y Sesgos Cognitivos | Streamlit")

