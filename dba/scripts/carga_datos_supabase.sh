#!/bin/bash

# Carpeta donde están los CSV
CSV_DIR="/ruta/a/tus/csv"

for file in "$CSV_DIR"/*.csv; do
    filename=$(basename "$file" .csv)
    table_name="nombre_schema.$filename"

    echo "Importando: $filename → tabla $table_name"

    PGPASSWORD="TU_PASSWORD" psql \
      -h TU_HOST \
      -p TU_PUERTO \
      -U TU_USUARIO \
      -d TU_BASE_DE_DATOS \
      -c "\copy $table_name FROM '$file' CSV HEADER;"
done
