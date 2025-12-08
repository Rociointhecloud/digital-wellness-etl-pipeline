###### config.py #####

import os
from pathlib import Path
from dotenv import load_dotenv

# Obtener la ruta raíz del proyecto (un nivel arriba de src/)
ROOT_DIR = Path(__file__).parent.parent

# Cargar variables de entorno desde .env en la raíz del proyecto
dotenv_path = ROOT_DIR / '.env'
load_dotenv(dotenv_path)

# === CONFIGURACIÓN DE BASE DE DATOS ===
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# === CONFIGURACIÓN DE ARCHIVOS ===
EXCEL_FILE = os.getenv('EXCEL_FILE')
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', 'output')

# === CONFIGURACIÓN DE AUTOMATIZACIÓN ===
AUTO_OPEN_EXCEL = os.getenv('AUTO_OPEN_EXCEL', 'true').lower() == 'true'