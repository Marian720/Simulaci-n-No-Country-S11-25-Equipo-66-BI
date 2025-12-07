import pandas as pd
import numpy as np
import os

# ============================================
#   0. CONFIGURACIÓN DE RUTAS
# ============================================

base_path = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(base_path, "datos_csv")
os.makedirs(output_folder, exist_ok=True)

print(f"Los archivos CSV se guardarán en: {output_folder}\n")

# ============================================
#   1. DIM_Tiempo
# ============================================

print("1/6 Generando dim_tiempo.csv...")

fechas = pd.date_range(start='2023-01-01', end='2025-12-31', freq='D')
num_dias = len(fechas)

dim_tiempo = pd.DataFrame({
    'fecha': fechas,
    'id_fecha': fechas.strftime('%Y%m%d').astype(int),
    'anio': fechas.year,
    'trimestre': fechas.quarter,
    'mes': fechas.month,
    'mes_nombre': fechas.strftime('%B'),
    'dia_semana_nombre': fechas.strftime('%A')
})

dim_tiempo = dim_tiempo[['id_fecha', 'fecha', 'anio', 'trimestre', 'mes', 'mes_nombre', 'dia_semana_nombre']]
dim_tiempo.to_csv(os.path.join(output_folder, 'dim_tiempo.csv'), index=False)

print("✔ dim_tiempo.csv creado.\n")

# ============================================
#   2. fact_finanzas
# ============================================

print("2/6 Generando fact_finanzas.csv...")

fact_finanzas = pd.DataFrame({
    'id_fecha': dim_tiempo['id_fecha'],
    'ingresos': np.random.uniform(10000, 50000, num_dias).round(2),
    'costos': np.random.uniform(5000, 25000, num_dias).round(2)
})

# Ensuciar
fact_finanzas.loc[fact_finanzas.sample(n=30).index, 'ingresos'] = np.nan
fact_finanzas.loc[fact_finanzas.sample(n=3).index, 'ingresos'] = 9999999.00
fact_finanzas = pd.concat([fact_finanzas, fact_finanzas.sample(n=10)], ignore_index=True)

fact_finanzas['id_finanza'] = range(1, len(fact_finanzas) + 1)
fact_finanzas = fact_finanzas[['id_finanza', 'id_fecha', 'ingresos', 'costos']]
fact_finanzas.to_csv(os.path.join(output_folder, 'fact_finanzas.csv'), index=False)

print("✔ fact_finanzas.csv creado.\n")

# ============================================
#   3. fact_ambiental
# ============================================

print("3/6 Generando fact_ambiental.csv...")

fact_ambiental = pd.DataFrame()
fact_ambiental['id_fecha'] = dim_tiempo['id_fecha']
fact_ambiental['consumo_kwh'] = np.random.uniform(1000, 3000, num_dias).round(2)
fact_ambiental['consumo_agua_litros'] = np.random.uniform(500, 1500, num_dias).round(2)
fact_ambiental['residuos_totales_kg'] = np.random.uniform(50, 200, num_dias).round(2)

fact_ambiental['residuos_reciclados_kg'] = (
    fact_ambiental['residuos_totales_kg'] *
    np.random.uniform(0.1, 0.7, num_dias)
).round(2)

fact_ambiental['huella_carbono_tCO2e'] = (
    fact_ambiental['consumo_kwh'] * 0.45 +
    np.random.uniform(10, 50, num_dias)
).round(2)

# Ensuciar
fact_ambiental.loc[fact_ambiental.sample(n=25).index, 'consumo_agua_litros'] = np.nan
fact_ambiental.loc[fact_ambiental.sample(n=10).index, 'huella_carbono_tCO2e'] = np.nan

fact_ambiental['id_ambiental'] = range(1, len(fact_ambiental) + 1)
fact_ambiental = fact_ambiental[['id_ambiental', 'id_fecha', 'consumo_kwh',
                                 'consumo_agua_litros', 'residuos_totales_kg',
                                 'residuos_reciclados_kg', 'huella_carbono_tCO2e']]

fact_ambiental.to_csv(os.path.join(output_folder, 'fact_ambiental.csv'), index=False)

print("✔ fact_ambiental.csv creado.\n")

# ============================================
#   4. fact_rrhh
# ============================================

print("4/6 Generando fact_rrhh.csv...")

fact_rrhh = pd.DataFrame()
fact_rrhh['id_fecha'] = dim_tiempo['id_fecha']
fact_rrhh['total_empleados'] = np.random.randint(40, 60, num_dias)
fact_rrhh['empleados_nuevos'] = np.random.randint(0, 3, num_dias)
fact_rrhh['empleados_baja'] = np.random.randint(0, 2, num_dias)
fact_rrhh['liderazgo_femenino'] = np.random.randint(5, 15, num_dias)
fact_rrhh['liderazgo_masculino'] = np.random.randint(5, 15, num_dias)
fact_rrhh['satisfaccion_empleados'] = np.random.uniform(6.5, 8.5, num_dias).round(1)

# Ensuciar
fact_rrhh.loc[fact_rrhh.sample(n=30).index, 'satisfaccion_empleados'] = np.nan
fact_rrhh = pd.concat([fact_rrhh, fact_rrhh.sample(n=15)], ignore_index=True)

fact_rrhh['id_rrhh'] = range(1, len(fact_rrhh) + 1)

fact_rrhh = fact_rrhh[['id_rrhh', 'id_fecha', 'total_empleados', 'empleados_nuevos',
                       'empleados_baja', 'liderazgo_femenino',
                       'liderazgo_masculino', 'satisfaccion_empleados']]

fact_rrhh.to_csv(os.path.join(output_folder, 'fact_rrhh.csv'), index=False)

print("✔ fact_rrhh.csv creado.\n")

# ============================================
#   5. fact_gobernanza_trimestral
# ============================================

print("5/6 Generando fact_gobernanza_trimestral.csv...")

quarterly_dates = dim_tiempo.groupby(['anio', 'trimestre'])['id_fecha'].max().reset_index()
num_quarters = len(quarterly_dates)

fact_gobernanza = pd.DataFrame()
fact_gobernanza['id_fecha'] = quarterly_dates['id_fecha']
fact_gobernanza['pct_capacitacion_etica'] = np.random.uniform(70, 95, num_quarters).round(1)
fact_gobernanza['nro_auditorias_internas'] = np.random.randint(1, 3, num_quarters)
fact_gobernanza['canal_denuncias_activo'] = np.random.randint(0, 2, num_quarters)

# Ensuciar
fact_gobernanza.loc[fact_gobernanza.sample(n=2).index, 'pct_capacitacion_etica'] = np.nan

fact_gobernanza['id_gobernanza'] = range(1, num_quarters + 1)

fact_gobernanza = fact_gobernanza[['id_gobernanza', 'id_fecha',
                                   'pct_capacitacion_etica',
                                   'nro_auditorias_internas',
                                   'canal_denuncias_activo']]

fact_gobernanza.to_csv(os.path.join(output_folder, 'fact_gobernanza_trimestral.csv'), index=False)

print("✔ fact_gobernanza_trimestral.csv creado.\n")

# ============================================
#   6. objetivos_esg (con valor_ejemplo)
# ============================================

print("6/6 Generando objetivos_esg.csv...")

data_objetivos = [
    [2023, 'Ambiental', 'Tasa Reciclaje', '% residuos reciclados', '%', 0.30],
    [2023, 'Ambiental', 'Huella Carbono', 'Toneladas CO2e promedio diario', 'tCO2e', 20.00],
    [2023, 'Social', 'Rotación', 'Tasa de rotación anual máxima', '%', 0.15],
    [2023, 'Social', 'Equidad', 'Mujeres en liderazgo', 'Cantidad', 8.00],
    [2023, 'Gobernanza', 'Capacitación Ética', 'Porcentaje empleados capacitados', '%', 80.00],
    [2023, 'Financiero', 'Margen Neto', 'Margen neto objetivo', '%', 0.25],

    [2024, 'Ambiental', 'Tasa Reciclaje', '% residuos reciclados', '%', 0.40],
    [2024, 'Ambiental', 'Huella Carbono', 'Toneladas CO2e promedio diario', 'tCO2e', 18.00],
    [2024, 'Social', 'Rotación', 'Máxima rotación anual', '%', 0.12],
    [2024, 'Social', 'Equidad', 'Mujeres en liderazgo', 'Cantidad', 10.00],
    [2024, 'Gobernanza', 'Capacitación Ética', 'Porcentaje empleados capacitados', '%', 90.00],
    [2024, 'Financiero', 'Margen Neto', 'Margen objetivo', '%', 0.30],

    [2025, 'Ambiental', 'Tasa Reciclaje', '% residuos reciclados', '%', 0.50],
    [2025, 'Ambiental', 'Huella Carbono', 'Toneladas CO2e promedio diario', 'tCO2e', 15.00],
    [2025, 'Social', 'Rotación', 'Rotación anual máxima', '%', 0.10],
    [2025, 'Social', 'Equidad', 'Mujeres en liderazgo', 'Cantidad', 12.00],
    [2025, 'Gobernanza', 'Capacitación Ética', 'Porcentaje capacitados', '%', 95.00],
    [2025, 'Financiero', 'Margen Neto', 'Meta de margen neto', '%', 0.35],
]

objetivos_esg = pd.DataFrame(data_objetivos, columns=[
    'anio_objetivo', 'categoria_esg', 'kpi_nombre',
    'descripcion_objetivo', 'unidad_medida', 'valor_objetivo'
])

valor_ejemplo = []

for _, row in objetivos_esg.iterrows():
    objetivo = row['valor_objetivo']
    unidad = row['unidad_medida']

    if unidad == '%':
        ejemplo = round(np.random.uniform(0, objetivo), 3)
    elif unidad.lower() in ['cantidad', 'unidades']:
        ejemplo = int(np.random.uniform(objetivo * 0.8, objetivo * 1.2))
    elif unidad.lower() == 'tco2e':
        ejemplo = round(np.random.uniform(objetivo * 0.9, objetivo * 1.1), 2)
    else:
        ejemplo = round(np.random.uniform(objetivo * 0.8, objetivo * 1.2), 3)

    valor_ejemplo.append(str(ejemplo))

objetivos_esg['valor_ejemplo'] = valor_ejemplo
objetivos_esg['id_objetivo'] = range(1, len(objetivos_esg) + 1)

objetivos_esg = objetivos_esg[['id_objetivo', 'categoria_esg', 'kpi_nombre',
                               'descripcion_objetivo', 'unidad_medida',
                               'valor_objetivo', 'anio_objetivo', 'valor_ejemplo']]

objetivos_esg.to_csv(os.path.join(output_folder, "objetivos_esg.csv"), index=False)

print("\n✔ ¡Proceso completado! Todos los CSV fueron generados correctamente.\n")
