#### Archivo BD_ETL #####

# ETL PROCESS screen_time_wellness
import pandas as pd
from sqlalchemy import create_engine
import os
from config import *

def bd_conect():
    """Build SQLAlchemy engine from environment variables."""
    if not DB_USER or not DB_PASSWORD:
        raise ValueError("DB_USER or DB_PASSWORD not set in .env")
    url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(url)

def data_extract(engine):
    query = """
        SELECT
            p.user_id,
            p.age,
            p.gender,
            p.occupation,
            p.work_mode,
            d.screen_time_hours,
            d.work_screen_hours,
            d.leisure_screen_hours,
            d.exercise_minutes_per_week,
            d.social_hours_per_week,
            w.sleep_hours,
            w.sleep_quality_1_5,
            w.stress_level_0_10,
            w.productivity_0_100,
            w.mental_wellness_index_0_100
        FROM participant p
        JOIN digital_habits d ON p.user_id = d.user_id
        JOIN wellness w ON p.user_id = w.user_id
        ORDER BY p.user_id
        """

    try:
        # try sample table
        df = pd.read_sql(query, con=engine)
        print(f"Fetched mental_wellness_sample ({len(df)} rows).")
        return df
    except Exception:
       	print(f"Something gone wrong:")

def transform_data(df):

    print("Transforming data...")

    # Cast numeric columns
    num_cols = [
        'age', 'screen_time_hours', 'work_screen_hours', 'leisure_screen_hours',
        'exercise_minutes_per_week', 'social_hours_per_week', 'sleep_hours',
        'sleep_quality_1_5', 'stress_level_0_10', 'productivity_0_100',
        'mental_wellness_index_0_100'
    ]
    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    # Basic missing value handling: keep rows but mark missingness
    missing_summary = df[num_cols].isna().sum()
    print("Missing values summary (numeric cols):")
    print(missing_summary.to_dict())
    
    # Delete nulls
    df.dropna()

    # Create age_group
    if 'age' in df.columns:
        bins = [0, 17, 24, 34, 44, 54, 64, 120]
        labels = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
        df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

    # Create a digital_balance score (interpretable, explain in README)
    # Normalize scales: productivity and wellness are 0-100, stress 0-10 -> scale stress to 0-100
    if {'productivity_0_100', 'mental_wellness_index_0_100', 'stress_level_0_10'}.issubset(df.columns):
        df['stress_scaled_0_100'] = df['stress_level_0_10'] * 10
        df['digital_balance'] = (
            df['productivity_0_100'].fillna(50) * 0.4 +
            df['mental_wellness_index_0_100'].fillna(50) * 0.4 -
            df['stress_scaled_0_100'].fillna(50) * 0.2
        )
        # keep score bounded 0-100
        df['digital_balance'] = df['digital_balance'].clip(lower=0, upper=100).round(1)

    # Create simple flags
    if 'screen_time_hours' in df.columns:
        df['high_screen_time'] = df['screen_time_hours'] > 8  # boolean
    if 'sleep_hours' in df.columns:
        df['short_sleep'] = df['sleep_hours'] < 6  # boolean

    # Select and order columns for final CSV (keep descriptive order)
    preferred_cols = [
        'user_id', 'age', 'age_group', 'gender', 'occupation', 'work_mode',
        'screen_time_hours', 'work_screen_hours', 'leisure_screen_hours',
        'exercise_minutes_per_week', 'social_hours_per_week',
        'sleep_hours', 'sleep_quality_1_5', 'short_sleep',
        'stress_level_0_10', 'productivity_0_100', 'mental_wellness_index_0_100',
        'digital_balance', 'high_screen_time'
    ]
    final_cols = [c for c in preferred_cols if c in df.columns]
    final_df = df[final_cols]

    print("Transformation complete.")
    return final_df

def load_data(df):

    print("💾 saving CSV...")

    # Guardar CSV
    df.to_csv(f'{OUTPUT_FOLDER}/datos_digital_wellness_sample_2025.csv', index=False, encoding='utf-8-sig')

    print(f"✓ CSV save in '{OUTPUT_FOLDER}/datos_digital_wellness_sample_2025.csv'")

    return True

def execute_etl():

    """Ejecutar proceso ETL completo"""
    try:
        # Conect to database
        engine = bd_conect()
        
        # Extraer
        df = data_extract(engine)
        
        # Transformar
        df_transformado = transform_data(df)
        
        # Guardar CSV principal
        load_data(df_transformado)
        
        # Retornar dataset para el dashboard
        return {
            'datos_principales': df_transformado
        }
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    
if __name__ == "__main__":
        execute_etl()
