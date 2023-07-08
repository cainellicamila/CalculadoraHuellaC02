import streamlit as st
from constantes import FACTORES

lista_factores = FACTORES

def calcula_huella(*arguments):
    """
    Esta función calcula la huella de carbono
    Parameters
    ----------
    *arguments: int
    Lista con los consumos por categoría
    """
    totalSum = 0
    for (number, factor) in zip(arguments, lista_factores):
        totalSum += number * factor
    return totalSum

def obtener_impacto_arboles(huella):
    arboles_por_tonelada = 3.67 # Cantidad promedio de árboles necesarios para compensar una tonelada de emisiones de CO2
    arboles_necesarios = huella / 1000 * arboles_por_tonelada # Convertir huella a toneladas
    return arboles_necesarios

def obtener_impacto_ejemplos():
    impacto = {
        "Impacto en el cambio climático": "La huella de carbono generada contribuye al cambio climático, aumentando la temperatura promedio del planeta.",
        "Contaminación del aire": "Las emisiones de carbono también se asocian con la contaminación del aire y problemas de salud, como enfermedades respiratorias.",
        "Escasez de recursos naturales": "El aumento de las emisiones de carbono puede agotar los recursos naturales, como el agua y los combustibles fósiles.",
        "Degradación del ecosistema": "La emisión de carbono puede afectar negativamente a los ecosistemas, provocando la pérdida de biodiversidad y daños a los hábitats naturales."
    }
    return impacto

def obtener_compensacion_ejemplos(huella):
    arboles_necesarios = obtener_impacto_arboles(huella)
    compensacion = {
        "Plantación de árboles": "Se requiere plantar aproximadamente {} árboles.".format(int(arboles_necesarios)),
        "Energías renovables": "Apoyar proyectos de energía renovable y utilizar fuentes de energía limpias.",
        "Eficiencia energética": "Mejorar la eficiencia energética en tus actividades diarias.",
        "Transporte sostenible": "Utilizar medios de transporte sostenibles y optar por vehículos eléctricos o híbridos.",
        "Compensación de carbono": "Participar en programas y proyectos de compensación de carbono."
    }
    return compensacion

st.title("Calculadora Huella de Carbono :earth_americas:")

# Efecto de la huella de carbono en el medio ambiente
st.subheader("**:blue[¿Cómo afecta la Huella de Carbono al medio ambiente?]**")

for ejemplo, mensaje in obtener_impacto_ejemplos().items():
    st.write(f"- **{ejemplo}:** {mensaje}")

# Formulario
st.subheader("**:blue[Ingresa tus datos de consumo]**")
with st.form("my_form"):
    km_auto_gas = st.number_input("KM en automóvil gasoil", min_value=0)
    km_auto_die = st.number_input("KM en automóvil diesel", min_value=0)
    km_auto_elec = st.number_input("KM en automóvil eléctrico", min_value=0)
    km_auto_gnc = st.number_input("KM en automóvil gnc", min_value=0)
    km_moto_gas = st.number_input("KM en moto gasoil", min_value=0)
    km_camion_liviano_die = st.number_input("KM en camión liviano diésel", min_value=0)
    km_colect_die = st.number_input("KM en colectivo diésel", min_value=0)
    km_colect_gas = st.number_input("KM en colectivo gasoil", min_value=0)
    km_subte = st.number_input("KM en Subte", min_value=0)

    submitted = st.form_submit_button("Calcular")
    huella = calcula_huella(km_auto_gas, km_auto_die, km_auto_elec, km_auto_gnc, km_moto_gas, km_camion_liviano_die, km_colect_gas)

if submitted:
    st.write("Tu huella de carbono es:", huella)
    impacto_arboles = obtener_impacto_arboles(huella)

    st.write("Esto equivale a la absorción de CO2 de aproximadamente", int(impacto_arboles), "árboles.")

    st.write("Este impacto de la huella de carbono se podría compensar con:")
    for ejemplo, mensaje in obtener_compensacion_ejemplos(huella).items():
        st.write(f"- {ejemplo}: {mensaje}")