-- ================================================================
--  Proyecto: Sustainable Growth Monitor
-- ================================================================

-- ================================================================
--  1. DIMENSIÓN: dim_tiempo 
-- ================================================================

CREATE TABLE IF NOT EXISTS pubic.dim_tiempo (
    id_fecha INT PRIMARY KEY,
    fecha DATE NOT NULL,
    anio INT NOT NULL,
    trimestre SMALLINT NOT NULL,
    mes SMALLINT NOT NULL,
    mes_nombre VARCHAR(20) NOT NULL,
    dia_semana_nombre VARCHAR(20) NOT NULL
);

-- ================================================================
--  2. FACT: fact_finanzas 
-- ================================================================

CREATE TABLE IF NOT EXISTS public.fact_finanzas (
    id_finanza SERIAL PRIMARY KEY,
    id_fecha INT NOT NULL,
    ingresos NUMERIC(10,2),      
    costos NUMERIC(10,2) NOT NULL,
    CONSTRAINT fk_finanzas_fecha
        FOREIGN KEY (id_fecha)
        REFERENCES public.dim_tiempo(id_fecha)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- ================================================================
--  3. FACT: fact_ambiental 
-- ================================================================

CREATE TABLE IF NOT EXISTS public.fact_ambiental (
    id_ambiental SERIAL PRIMARY KEY,
    id_fecha INT NOT NULL,
    consumo_kwh NUMERIC(10,2) NOT NULL,
    consumo_agua_litros NUMERIC(10,2),        
    residuos_totales_kg NUMERIC(10,2) NOT NULL,
    residuos_reciclados_kg NUMERIC(10,2) NOT NULL,
    huella_carbono_tCO2e NUMERIC(10,2),       
    CONSTRAINT fk_ambiental_fecha
        FOREIGN KEY (id_fecha)
        REFERENCES public.dim_tiempo(id_fecha)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- ================================================================
--  4. FACT: fact_rrhh 
-- ================================================================

CREATE TABLE IF NOT EXISTS public.fact_rrhh (
    id_rrhh SERIAL PRIMARY KEY,
    id_fecha INT NOT NULL,
    total_empleados INT NOT NULL,
    empleados_nuevos INT NOT NULL,
    empleados_baja INT NOT NULL,
    liderazgo_femenino INT NOT NULL,
    liderazgo_masculino INT NOT NULL,
    satisfaccion_empleados NUMERIC(3,1),      
    CONSTRAINT fk_rrhh_fecha
        FOREIGN KEY (id_fecha)
        REFERENCES public.dim_tiempo(id_fecha)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- ================================================================
--  5. FACT TRIMESTRAL: fact_gobernanza_trimestral 
-- ================================================================

CREATE TABLE IF NOT EXISTS public.fact_gobernanza_trimestral (
    id_gobernanza SERIAL PRIMARY KEY,
    id_fecha INT NOT NULL,
    pct_capacitacion_etica NUMERIC(4,1),    
    nro_auditorias_internas INT NOT NULL,
    canal_denuncias_activo BOOLEAN NOT NULL,
    CONSTRAINT fk_gobernanza_fecha
        FOREIGN KEY (id_fecha)
        REFERENCES public.dim_tiempo(id_fecha)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- ================================================================
--  6. DIMENSIÓN: objetivos_esg 
-- ================================================================

CREATE TABLE IF NOT EXISTS public.objetivos_esg (
    id_objetivo SERIAL PRIMARY KEY,
    categoria_esg VARCHAR(20) NOT NULL,
    kpi_nombre VARCHAR(50) NOT NULL,
    descripcion_objetivo VARCHAR(255),
    unidad_medida VARCHAR(20),
    valor_objetivo NUMERIC(10,2) NOT NULL,
    anio_objetivo INT NOT NULL,
    valor_ejemplo VARCHAR(50)
);

-- ================================================================
--  ÍNDICES
-- ================================================================

CREATE INDEX IF NOT EXISTS idx_finanzas_fecha 
    ON public.fact_finanzas(id_fecha);

CREATE INDEX IF NOT EXISTS idx_ambiental_fecha 
    ON public.fact_ambiental(id_fecha);

CREATE INDEX IF NOT EXISTS idx_rrhh_fecha 
    ON public.fact_rrhh(id_fecha);

CREATE INDEX IF NOT EXISTS idx_gobernanza_fecha 
    ON public.fact_gobernanza_trimestral(id_fecha);
