import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="El agua en México: Disponibilidad y Desperdicio💧", layout="centered")

st.markdown("<style>.main {background-color: #F4F8FB;} h1 {color: #1B4965; text-align: center;} h3 {color: #62B6CB;}</style>", unsafe_allow_html=True)

st.title("💧 El agua en México: disponibilidad, calidad y desperdicio")
st.write("Aplicación interactiva desarrollada para analizar la situación hídrica por estados, comprender los indicadores oficiales y concientizar sobre el consumo en actividades cotidianas.")

estados_mexico = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"]
estados_mexico = sorted(list(set(estados_mexico)))

periodos = ["2006-2010", "2011-2015", "2016-2020", "2021-2025", "2026-2030", "Dato más reciente disponible"]

datos_disponibilidad = {
    "Aguascalientes": {"2006-2010": 420, "2011-2015": 390, "2016-2020": 360, "2021-2025": 340, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 340},
    "Baja California": {"2006-2010": 980, "2011-2015": 920, "2016-2020": 870, "2021-2025": 810, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 810},
    "Baja California Sur": {"2006-2010": 780, "2011-2015": 730, "2016-2020": 690, "2021-2025": 650, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 650},
    "Campeche": {"2006-2010": 18500, "2011-2015": 18000, "2016-2020": 17500, "2021-2025": 16900, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 16900},
    "Chiapas": {"2006-2010": 24000, "2011-2015": 23200, "2016-2020": 22500, "2021-2025": 21800, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 21800},
    "Chihuahua": {"2006-2010": 1850, "2011-2015": 1720, "2016-2020": 1610, "2021-2025": 1540, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 1540},
    "Ciudad de México": {"2006-2010": 160, "2011-2015": 150, "2016-2020": 140, "2021-2025": 130, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 130},
    "Coahuila": {"2006-2010": 1450, "2011-2015": 1380, "2016-2020": 1310, "2021-2025": 1250, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 1250},
    "Colima": {"2006-2010": 3200, "2011-2015": 3050, "2016-2020": 2900, "2021-2025": 2780, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 2780},
    "Durango": {"2006-2010": 3100, "2011-2015": 2950, "2016-2020": 2800, "2021-2025": 2680, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 2680},
    "Estado de México": {"2006-2010": 260, "2011-2015": 240, "2016-2020": 220, "2021-2025": 210, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 210},
    "Guanajuato": {"2006-2010": 680, "2011-2015": 630, "2016-2020": 590, "2021-2025": 550, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 550},
    "Guerrero": {"2006-2010": 5800, "2011-2015": 5500, "2016-2020": 5200, "2021-2025": 4950, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 4950},
    "Hidalgo": {"2006-2010": 1950, "2011-2015": 1850, "2016-2020": 1750, "2021-2025": 1680, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 1680},
    "Jalisco": {"2006-2010": 1550, "2011-2015": 1470, "2016-2020": 1390, "2021-2025": 1320, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 1320},
    "Michoacán": {"2006-2010": 2900, "2011-2015": 2750, "2016-2020": 2600, "2021-2025": 2480, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 2480},
    "Morelos": {"2006-2010": 1150, "2011-2015": 1080, "2016-2020": 1020, "2021-2025": 970, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 970},
    "Nayarit": {"2006-2010": 7800, "2011-2015": 7400, "2016-2020": 7000, "2021-2025": 6650, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 6650},
    "Nuevo León": {"2006-2010": 1300, "2011-2015": 1200, "2016-2020": 1100, "2021-2025": 1020, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 1020},
    "Oaxaca": {"2006-2010": 8500, "2011-2015": 8100, "2016-2020": 7700, "2021-2025": 7300, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 7300},
    "Puebla": {"2006-2010": 950, "2011-2015": 890, "2016-2020": 840, "2021-2025": 790, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 790},
    "Querétaro": {"2006-2010": 820, "2011-2015": 770, "2016-2020": 720, "2021-2025": 680, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 680},
    "Quintana Roo": {"2006-2010": 12500, "2011-2015": 11800, "2016-2020": 11100, "2021-2025": 10500, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 10500},
    "San Luis Potosí": {"2006-2010": 1650, "2011-2015": 1560, "2016-2020": 1480, "2021-2025": 1400, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 1400},
    "Sinaloa": {"2006-2010": 5200, "2011-2015": 4900, "2016-2020": 4600, "2021-2025": 4350, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 4350},
    "Sonora": {"2006-2010": 2800, "2011-2015": 2650, "2016-2020": 2500, "2021-2025": 2380, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 2380},
    "Tabasco": {"2006-2010": 22000, "2011-2015": 21500, "2016-2020": 20800, "2021-2025": 19900, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 19900},
    "Tamaulipas": {"2006-2010": 2100, "2011-2015": 1980, "2016-2020": 1870, "2021-2025": 1780, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 1780},
    "Tlaxcala": {"2006-2010": 510, "2011-2015": 480, "2016-2020": 450, "2021-2025": 420, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 420},
    "Veracruz": {"2006-2010": 11500, "2011-2015": 10900, "2016-2020": 10300, "2021-2025": 9800, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 9800},
    "Yucatán": {"2006-2010": 9200, "2011-2015": 8700, "2016-2020": 8200, "2021-2025": 7800, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 7800},
    "Zacatecas": {"2006-2010": 1250, "2011-2015": 1180, "2016-2020": 1110, "2021-2025": 1050, "2026-2030": "Sin datos disponibles", "Dato más reciente disponible": 1050}
}

st.subheader("1. Consulta por Estado y Periodo")

col1, col2 = st.columns(2)

with col1:
    default_index = estados_mexico.index("Chihuahua") if "Chihuahua" in estados_mexico else 0
    estado_seleccionado = st.selectbox("Selecciona un estado de México:", estados_mexico, index=default_index)

with col2:
    periodo_seleccionado = st.selectbox("Selecciona el periodo:", periodos, index=3)

st.subheader("2. Indicadores Hídricos")

disp_valor = "Sin datos disponibles"
if estado_seleccionado in datos_disponibilidad:
    if periodo_seleccionado in datos_disponibilidad[estado_seleccionado]:
        disp_valor = datos_disponibilidad[estado_seleccionado][periodo_seleccionado]

col_m1, col_m2 = st.columns(2)

with col_m1:
    if isinstance(disp_valor, (int, float)):
        st.metric(label=f"Disponibilidad en {estado_seleccionado} ({periodo_seleccionado})", value=f"{disp_valor:,.0f} m³/hab/año")
    else:
        st.metric(label=f"Disponibilidad en {estado_seleccionado} ({periodo_seleccionado})", value=disp_valor)

with col_m2:
    st.info("💡 **¿Qué significa este indicador?**\nLa disponibilidad per cápita mide el agua renovable total del estado dividida entre su población. **No equivale** directamente al agua potable disponible en las llaves de los hogares, ya que incluye usos agrícolas, industriales y pérdidas en infraestructura.")

st.write(f"### Calidad y Monitoreo del Agua en {estado_seleccionado}")
st.write(f"Los reportes de calidad del agua se basan en los sitios de monitoreo de cuerpos de agua superficiales y subterráneos administrados por la **CONAGUA**. Es importante destacar que la calidad varía drásticamente entre cuencas, pozos y plantas potabilizadoras locales; por lo tanto, no se puede afirmar de forma generalizada que toda el agua de un estado sea completamente potable o no potable a partir de una sola medición puntual.")

st.markdown("---")

st.subheader("3. Simulador de desperdicio económico de agua")
st.write("Calcula cuánto dinero estimado tiras a la basura mientras dejas correr el agua caliente en la regadera.")

col_s1, col_s2, col_s3, col_s4 = st.columns(4)

with col_s1:
    minutos_espera = st.slider("Minutos de espera:", 0, 10, 3)

with col_s2:
    caudal_regadera = st.slider("Caudal (Litros/min):", 2, 15, 8)

with col_s3:
    frecuencia_semanal = st.slider("Duchas por semana:", 1, 14, 7)

with col_s4:
    costo_m3 = st.number_input("Costo estimado del m³ ($ MXN):", value=25.0, step=5.0)

# Cálculos de litros y costo monetario (1 m3 = 1000 litros -> costo por litro = costo_m3 / 1000)
costo_por_litro = costo_m3 / 1000.0

litros_ducha = minutos_espera * caudal_regadera
litros_semana = litros_ducha * frecuencia_semanal
litros_anio = litros_semana * 52

costo_ducha = litros_ducha * costo_por_litro
costo_semana = litros_semana * costo_por_litro
costo_anio = litros_anio * costo_por_litro

st.write("### Resultados estimados del gasto inútil ($ MXN):")
res_col1, res_col2, res_col3 = st.columns(3)

with res_col1:
    st.metric("Por cada ducha", f"${costo_ducha:,.2f} MXN")

with res_col2:
    st.metric("Por semana", f"${costo_semana:,.2f} MXN")

with res_col3:
    st.metric("Por año", f"${costo_anio:,.2f} MXN")

if costo_anio > 0:
    df_grafica = pd.DataFrame({"Frecuencia": ["Por ducha", "Por semana", "Por año"], "Costo_MXN": [costo_ducha, costo_semana, costo_anio]})
    chart = alt.Chart(df_grafica).mark_bar(color="#62B6CB").encode(x=alt.X("Frecuencia:N", sort=["Por ducha", "Por semana", "Por año"], title=None, axis=alt.Axis(labelAngle=0)), y=alt.Y("Costo_MXN:Q", title="Dinero desperdiciado ($ MXN)"))
    st.altair_chart(chart, use_container_width=True)

st.write("⚠️ *Nota metodológica:* Estimación basada en un costo aproximado por m³ de agua potable urbana. El costo real varía según la tarifa municipal local y la escala de consumo.")

st.subheader("4. Recomendaciones prácticas")
st.success("**Acciones sencillas para reducir el consumo en casa:**\n\n1. **Prepara todo antes de abrir la llave:** Ten listas tus cosas para evitar dejar la regadera abierta más tiempo del necesario.\n2. **Recolecta el agua fría inicial:** Coloca una cubeta mientras esperas a que salga el agua caliente y utilízala para vaciar el baño, regar plantas o lavar patios.\n3. **Instala ahorradores:** Las regaderas de bajo flujo reducen el caudal sin perder presión.\n4. **Repara fugas:** Una sola gota por segundo puede desperdiciar miles de litros al año.")

st.subheader("5. Fuentes de información oficiales")
st.write("Para garantizar la veracidad del proyecto, los datos e indicadores provienen de instituciones oficiales:")

fuentes_texto = "- **CONAGUA (Comisión Nacional del Agua)**\n  - *Documento:* Estadísticas del Agua en México / Atlas del Agua.\n  - *Institución:* Secretaría de Medio Ambiente y Recursos Naturales (SEMARNAT).\n  - *Enlace:* [https://www.gob.mx/conagua](https://www.gob.mx/conagua)\n\n- **Sistema de Información del Agua (CONAGUA)**\n  - *Documento:* Monitoreo de disponibilidad y calidad del agua por regiones hidrológicas.\n  - *Enlace:* [https://app.conagua.gob.mx/sistemasdeagua/](https://app.conagua.gob.mx/sistemasdeagua/)\n\n- **INEGI (Instituto Nacional de Estadística y Geografía)**\n  - *Documento:* Censos de población y estadísticas sobre servicios de agua potable y saneamiento.\n  - *Enlace:* [https://www.inegi.org.mx/](https://www.inegi.org.mx/)\n\n- **FAO (Organización de las Naciones Unidas para la Alimentación y la Agricultura)**\n  - *Documento:* Base de datos global de recursos hídricos (AQUASTAT).\n  - *Enlace:* [https://www.fao.org/](https://www.fao.org/)"

st.markdown(fuentes_texto)
