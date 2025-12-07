#!/bin/bash

# Carpeta donde están los CSV
CSV_DIR="/mnt/c/Users/yiras/OneDrive/No Country/NC csv/datos_csv"

for file in "$CSV_DIR"/*.csv; do
    filename=$(basename "$file" .csv)
    table_name="sustainable_growth.$filename"

    echo "Importando: $filename → tabla $table_name"

    PGPASSWORD="far14426fwwhjw" psql \
      -h aws-1-us-east-1.pooler.supabase.com \
      -p 5432 \
      -U postgres.ftczzbbxrvcykefpdtnj \
      -d postgres \
      -c "\copy $table_name FROM '$file' CSV HEADER;"
done
