# Proceso de ETL para la base de datos Sakila
import pandas as pd
from sqlalchemy import create_engine
import os
from config import *

def conectar_bd():

    url = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(url)
    return engine

def extraer_datos():

    print("Conectando a la base de datos...")
    
    engine = conectar_bd()

    # Query para análisis de clientes
    query = """
        --------------- AÑADIR CONSULTA SELECT ---------------
    """   
    df = pd.read_sql(query, engine)
    print(f"✓ {len(df)} registros extraídos")
    return df

def transformar_datos(df):

    print("Transformando datos...")
    
    ### Transformar datos adaptados a la nueva BD, dejo los antiguos para tenerlos de ejemplo.
    ### Antes hacer push eliminar comentarios que no sean necesarios o descriptivos del proyecto.
    
    # df['monto'] = df['monto'].astype(float)
    # df['fecha_renta'] = pd.to_datetime(df['fecha_renta'])
    # df['fecha_devolucion'] = pd.to_datetime(df['fecha_devolucion'])
    # df['fecha_pago'] = pd.to_datetime(df['fecha_pago'])
    # df['año_renta'] = pd.to_datetime(df['fecha_renta']).dt.year
    # df['mes_renta'] = pd.to_datetime(df['fecha_renta']).dt.month
    # df['dia_semana'] = pd.to_datetime(df['fecha_renta']).dt.day_name()
    # df['estado_cliente'] = df['active'].map({1: 'Activo', 0: 'Inactivo'})
    # df['mes_año'] = pd.to_datetime(df['fecha_renta']).dt.to_period('M').astype(str)

    print("✓ Transformación completada")

    return df

def cargar_datos(df):

    print("💾 Guardando CSV...")


    # Guardar CSV
    df.to_csv(f'{OUTPUT_FOLDER}/datos_NOMBREBD.csv', index=False, encoding='utf-8-sig')

    print(f"✓ CSV guardado en '{OUTPUT_FOLDER}/datos_NOMBREBD.csv'")

    return True

def ejecutar_etl():

    """Ejecutar proceso ETL completo"""
    try:
        # Extraer
        df = extraer_datos()
        
        # Transformar
        df_transformado = transformar_datos(df)
        
        # Guardar CSV principal
        cargar_datos(df_transformado)
        
        # Retornar dataset para el dashboard
        return {
            'datos_principales': df_transformado
        }
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    
if __name__ == "__main__":
        ejecutar_etl()


