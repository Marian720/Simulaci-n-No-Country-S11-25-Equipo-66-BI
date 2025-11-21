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
