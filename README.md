# 📈 PROYECTO SUSTAINABLE GROWTH MONITOR
**Simulación Laboral No Country | Cohorte S11-25 | Equipo 66-BI**

---

## 📋 Contexto del Proyecto (Consigna)

### Necesidad del Cliente
Las PyMEs actuales enfrentan el desafío de monitorear su impacto ambiental sin descuidar su rentabilidad financiera. Actualmente, buscan una solución para monitorear **impacto ambiental, rentabilidad y métricas ESG** en un solo panel unificado.

### 🎯 Objetivo General
Diseñar un panel de inteligencia empresarial que integre indicadores financieros, de impacto ambiental y de sostenibilidad (ESG) para que las PyMEs puedan monitorear su desempeño integral y tomar decisiones más conscientes y rentables.

### ✅ Requerimientos Principales
* **Identificación de métricas clave:** Financieras y ESG.
* **Visualización integrada:** Tableros que combinen rentabilidad con sostenibilidad.
* **Alertas:** Detección de desviaciones respecto a objetivos.
* **Correlaciones:** Identificar relaciones (ej: impacto del ahorro energético en el margen neto).

---

## 🚀 Solución Propuesta (Entregable 1)

**Estado:** Entregado ✅
**Fecha:** 21/11/2025

### 1. Introducción y Propuesta de Valor

El objetivo principal de este proyecto es diseñar un sistema de inteligencia de negocios que permita a las PyMEs monitorear su desempeño integral. Actualmente, la información financiera, operativa y de recursos humanos reside en silos desconectados.

Nuestra propuesta de valor consiste en **integrar estos indicadores** para demostrar que la sostenibilidad no es un centro de costos, sino una palanca de rentabilidad.

El dashboard resultante permitirá responder preguntas clave como:
* ¿Cómo impacta la eficiencia energética en el margen neto?
* ¿Qué relación existe entre la satisfacción del empleado y los costos de rotación?

### 2. Definición de Métricas e Indicadores (KPIs)

A continuación, se detallan los indicadores seleccionados para cubrir los requerimientos financieros y ESG (Ambiental, Social y Gobernanza), junto con su lógica de cálculo y objetivos.

#### 2.1 Métricas Financieras
*Objetivo: Medir la rentabilidad y salud económica del negocio.*

| Indicador / KPI | Definición / Fórmula | Propósito de Negocio |
| :--- | :--- | :--- |
| **Ingresos Totales** | `SUM(ingresos)` | Medir el volumen de ventas facturado. |
| **Costos Operativos** | `SUM(costos)` | Controlar el gasto total de la operación. |
| **Rentabilidad (Margen Neto)** | `SUM(ingresos) - SUM(costos)` | Medir la ganancia real en dinero. |
| **Margen Porcentual** | `([Margen Neto] / SUM(ingresos) )` | Evaluar la eficiencia y rentabilidad relativa del negocio. |
| **Crecimiento de Ingresos** | `([Ingresos Actuales] - [Ingresos Periodo Anterior]) / [Ingresos Periodo Anterior]` | Monitorear la expansión del negocio año contra año. |

#### 2.2 Métricas Ambientales (E)
*Objetivo: Monitorear el impacto ecológico y la eficiencia de recursos.*

| Indicador / KPI | Definición / Fórmula | Propósito de Negocio | Meta Sugerida |
| :--- | :--- | :--- | :--- |
| **Consumo Energético** | `AVERAGE(consumo_kwh)` | Detectar picos de ineficiencia energética. | < 1800 kWh/día |
| **Huella de Carbono** | `AVERAGE(huella_carbono_tCO2e)` | Medir el impacto ambiental directo. | Reducción 10% anual |
| **Consumo de Agua** | `AVERAGE(consumo_agua_litros)` | Controlar el uso de recursos hídricos. | Reducción 5% anual |
| **Tasa de Reciclaje** | `SUM(residuos_reciclados_kg) / SUM(residuos_totales_kg)` | Verificar el compromiso con la economía circular. | > 40% |

#### 2.3 Métricas Sociales (S)
*Objetivo: Evaluar el capital humano, la equidad y el clima laboral.*

| Indicador / KPI | Definición / Fórmula | Propósito de Negocio | Meta Sugerida |
| :--- | :--- | :--- | :--- |
| **Tasa de Rotación** | `( SUM(empleados_baja) / AVERAGE(total_empleados) )` | Medir la estabilidad de la fuerza laboral y costos asociados. | < 15% anual |
| **Equidad de Género** | `AVERAGE(mujeres_liderazgo)` | Monitorear la diversidad en puestos de decisión. | > 10 puestos clave |
| **Satisfacción Empleado** | `AVERAGE(satisfaccion_empleados)` | Evaluar el clima laboral y su impacto en la productividad. | > 7.5 puntos |

#### 2.4 Métricas de Gobernanza (G)
*Objetivo: Asegurar la transparencia, ética y cumplimiento normativo.*

| Indicador / KPI | Definición / Fórmula | Propósito de Negocio | Meta Sugerida |
| :--- | :--- | :--- | :--- |
| **Capacitación Ética** | `AVERAGE(pct_capacitacion_etica)` | Mitigar riesgos legales y de reputación. | > 95% |
| **Auditorías Internas** | `AVERAGE(nro_auditorias_internas)` | Medir el control interno promedio por trimestre. | >= 2 por trimestre |
| **Canal de Denuncias** | `LASTNONBLANK(canal_denuncias_activo, 1)` | Garantizar mecanismos de transparencia activos. | 100% Operativo |

### 3. Estrategia de Alertas y Objetivos

Para cumplir con el requerimiento funcional de "detectar desviaciones", el sistema no solo medirá el valor actual, sino que lo comparará contra **Objetivos Anuales Definidos**.

* **Mecanismo:** Cada métrica listada anteriormente tendrá asociado un "Valor Meta" para el año en curso.
* **Visualización:** El dashboard resaltará automáticamente (en rojo/verde) cuando un KPI se desvíe de su meta establecida (ej. si la Tasa de Reciclaje cae por debajo del 40%).

---

# 4\. Arquitectura del Modelo de Datos

El modelo de datos del proyecto Sustainable Growth Monitor se diseñó siguiendo un enfoque estrella (Star Schema), optimizado para análisis de Business Intelligence. La arquitectura está compuesta por:

## 4.1. Una dimensión temporal limpia (dim_tiempo)

Proporciona la granularidad diaria y los atributos necesarios para realizar:

- agregaciones por trimestre,
- análisis por año, mes o día,
- cálculo de correlaciones temporales.

La clave primaria **id_fecha** se utiliza como punto de unión entre todas las tablas de hechos. Esta dimensión **no permite valores nulos en ninguno de sus campos**, ya que la estructura temporal debe ser completamente consistente para evitar errores en correlaciones y cálculos derivados.

## 4.2. Cuatro tablas de hechos operativas

Cada área del negocio se modela de forma independiente según su naturaleza:

**• fact_finanzas**

Registra ingresos y costos diarios. Permite datos incompletos porque simula escenarios reales donde la información financiera puede contener errores o ausencias de valores.

**Campos que permiten nulos:**

- **ingresos**: se habilitó para representar registros contables faltantes o inconsistencias operativas.
- **costos**: _no_ admite nulos para garantizar un mínimo de completitud en la información financiera.

**• fact_ambiental**

Contiene consumo energético, agua, residuos y huella de carbono. También admite nulos, reflejando la variabilidad y calidad irregular típica de mediciones ambientales.

**Campos que permiten nulos:**

- **consumo_agua_litros**: simula sensores fuera de línea o fallas en medición.
- **huella_carbono_tCO2e**: permite nulos para reflejar cálculos incompletos o no reportados.

Los demás campos son obligatorios para asegurar un mínimo de coherencia ambiental diaria.

**• fact_rrhh**

Integra indicadores sociales: total de empleados, entradas, salidas, liderazgo y satisfacción. Representa el componente "S" de ESG.

**Campos que permiten nulos:**

- **satisfaccion_empleados**: se permite para simular encuestas no respondidas o periodos sin medición.

Todos los demás campos son obligatorios para reflejar consistencia en las métricas de personal.

**• fact_gobernanza_trimestral**

Modelada con granularidad trimestral, dado que las prácticas de gobernanza no ocurren diariamente. Su unión a _dim_tiempo_ se hace mediante una fecha representativa del trimestre (por ejemplo, el último día del trimestre).

**Campos que permiten nulos:**

- **pct_capacitacion_etica**: puede faltar en algunos trimestres para simular reportes incompletos.

Los demás campos son obligatorios porque su ausencia comprometería la interpretación de auditorías y del estado del canal de denuncias.

## 4.3. Una tabla de catálogo independiente (objetivos_esg)

Esta tabla no forma parte del modelo relacional analítico, sino que funciona como un repositorio descriptivo de KPIs:

- Nombre del indicador
- Unidad de medida
- Definición
- Valor objetivo
- Año objetivo
- Ejemplo de valor típico

No requiere relaciones físicas, ya que su uso es conceptual y su contenido permite que se consuma desde la capa BI para comparar valores reales vs metas.

**Campos que permiten nulos:**

- **descripcion_objetivo**, **unidad_medida** y **valor_ejemplo**, ya que algunos objetivos pueden no requerir detalles adicionales o formatos específicos.

Existe como tabla independiente porque no participa en joins operativos, sino en la interpretación de KPIs.

## 4.4. Justificación de la arquitectura

Este diseño:

- Mantiene el modelo simple y entendible para analistas.
- Facilita cálculos temporales y correlaciones.
- Permite cargar datos imperfectos para simular ambientes reales.
- Reduce la rigidez del esquema permitiendo nulos en las tablas de hechos solo en campos donde los errores son realistas.
- Ofrece una tabla auxiliar (_objetivos_esg_) que sirve a la capa BI sin sobrecargar el esquema relacional.


