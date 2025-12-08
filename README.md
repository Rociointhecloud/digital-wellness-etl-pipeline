<h1 align="center">Mental Wellness & Screen Time — Proyecto IV</h1>
<p align="center"><em>Dashboard de análisis sobre hábitos digitales y bienestar</em></p>

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/24fc67ef-0db5-4459-bd36-74bd0770a639"
    width="45%"
    alt="Personas usando el móvil de forma continua, como invitación visual a reflexionar sobre la necesidad de una pausa digital"
  >
</p>

## MySQL → Python → Excel  
Pipeline automatizado · Accesibilidad · Análisis de bienestar digital

### Equipo de trabajo
- **Scrum Master:** Jaime Amuedo  
- **Data Analyst:** Mariana Moreno Henao  
- **Product Owner:** Rocío Pérez López  

El proyecto se ha desarrollado siguiendo un enfoque **Agile**, con una definición clara de roles.  
Rocío actúa como Product Owner, priorizando tareas y asegurando la coherencia entre objetivos, análisis y resultados. Jaime desempeña el rol de Scrum Master, facilitando el flujo de trabajo y resolviendo bloqueos técnicos. Mariana participa como Data Analyst, encargándose de la ejecución técnica y del análisis de los datos. Todo el equipo comparte la responsabilidad de cumplir los objetivos dentro del plazo establecido.

El trabajo se ha organizado mediante un **backlog priorizado** y un **tablero Kanban** con los estados *Backlog → Ready → In progress → In review → Done*, lo que ha permitido gestionar el avance de forma visual, transparente y colaborativa.  
Cada decisión relevante se ha documentado en este README y se han realizado sincronizaciones periódicas para asegurar un avance alineado y sostenido.

El desarrollo del proyecto se organizó en **tres sprints**. El primero se centró en sentar la base técnica: selección y validación del dataset, diseño del modelo relacional y definición del pipeline MySQL → Python → Excel. El segundo sprint abordó la **automatización y la visualización**, normalizando los datos, generando el CSV y construyendo las primeras tablas dinámicas y gráficos en Excel. En el tercer sprint el foco estuvo en el **análisis y el refinamiento**, revisando métricas, unificando criterios estadísticos, mejorando la accesibilidad y ajustando el dashboard y la documentación final.

# Objetivos del Proyecto
1.	Construir una base de datos relacional a partir del dataset Screen Time vs Mental Wellness Survey 2025.
2.	Automatizar la extracción de datos desde MySQL usando Python.
3.	Generar un archivo CSV actualizado que se conecta directamente al dashboard de Excel.
4.	Crear un dashboard accesible siguiendo principios WCAG 2.2, con una paleta apta para daltonismo y baja carga cognitiva.
5.	Analizar de forma crítica la relación entre sueño, estrés, tiempo de pantalla y bienestar social.
6.	Documentar el proceso con claridad, para que cualquier persona pueda reproducirlo y comprenderlo sin barreras.

---

# Arquitectura del Pipeline

```
MySQL (modelo relacional)
        ↓
Python (pandas, SQLAlchemy, etc)
        ↓
CSV generado automáticamente
        ↓
Excel (Dashboard dinámico y accesible)
```
---

# Estructura del Repositorio

```
📦 p4-da-project-data-automation-grupo5/
 ┣ 📁 dashboard/
 │   ┗ digital_wellness.xlsx 
 ┣ 📁 output/
 │   ┗ mental_wellness_sample_2025.csv  
 ┣ 📁 script_sql/
 │   ┗ creacion_bd.sql  
 ┣ 📁 src/
 │   ┣ __init__.py
 │   ┣ BD_ETL.py
 │   ┗ config.py
 ┣ 📁 docs/
 │   ┗ proceso_agile.md
 ┣ 📄 .env.example
 ┣ 📄 .gitignore
 ┣ 📄 main.py
 ┣ 📄 README.md
 ┗ 📄 requirements.txt

 ```
---

# Tecnologías y Librerías
- ![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas) - Manipulación y análisis de datos
- ![sqlalchemy](https://img.shields.io/badge/SQLAlchemy-306998?logo=python&logoColor=white) - Conexión a base de datos
- ![mysql-connector-python](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) - Driver MySQL
- ![openpyxl](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) - Generación y manipulación de archivos Excel
- ![python-dotenv](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  Gestión de variables de entorno
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) (modelo relacional, claves foráneas, normalización)
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) (pandas, SQLAlchemy, mysql-connector, python-dotenv)
- ![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white) (Tablas dinámicas, gráficos accesibles, slicers)
- ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) (herramienta de control de versiones)
- ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) (herramieta de control de versiones)
---

# 🧹 Proceso de Limpieza y Normalización

## 1. **Creación del modelo relacional**
El dataset original se normalizó en 3 tablas:

- **participant** — información de usuario  
- **digital_habits** — horas de pantalla, socialización, trabajo y ejercicio  
- **wellness** — estrés, sueño y productividad  

## 2. **Transformaciones principales**
- Conversión de tipos (enteros, floats, booleanos)
- Normalización de strings (trim + lower)
- Conversión de horas a valores numéricos  
- Eliminación de registros inconsistentes  
- Creación de una tabla para uso en Excel  
- Integración final mediante **JOINS SQL**

---

# Dataset Final

El archivo **mental_wellness_sample_2025.csv**:

- Se genera automáticamente con `main.py`  
- Es la fuente directa del dashboard  

## 📈 Dashboard

## Dashboard de Análisis — Bienestar Digital y Uso de Pantallas

Este dashboard se ha diseñado para explorar la relación entre hábitos digitales y bienestar personal desde una perspectiva analítica, accesible y sin juicios. El objetivo no es establecer causalidades, sino facilitar una lectura crítica de patrones y tendencias a partir de los datos.

La navegación está estructurada en cuatro bloques temáticos, que pueden analizarse de forma independiente o combinada a través de filtros interactivos (edad, género, modo de trabajo, ocupación y calidad del sueño).

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/38149303-5b27-4d73-90b3-82b821559a8a"
    width="90%"
    alt="Vista general del dashboard con los cuatro bloques temáticos sobre tiempo de pantalla, sueño, productividad y bienestar"
  >
</p>

---

### 1. Tiempo de pantalla y distribución del uso — estrés como variable asociada

Este bloque muestra cómo se distribuye el tiempo de pantalla entre usuarios con niveles altos y bajos de uso, así como su peso relativo dentro del conjunto analizado.

Se han incluido tanto gráficos de proporción como de volumen para diferenciar entre:
- **Distribución relativa de usuarios**, que indica qué porcentaje pertenece a cada nivel de uso.
- **Carga acumulada de tiempo de pantalla**, que ayuda a contextualizar el impacto global del uso intensivo.

El uso de filtros permite observar cómo estos patrones cambian según edad, género o modalidad laboral, reforzando la idea de que el uso digital no es homogéneo ni universal.

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/09dca4ea-055d-4d46-8d4b-2b46627cda1e"
    width="90%"
    alt="Bloque del dashboard centrado en tiempo de pantalla y distribución del uso, con segmentación por edad, género y modo de trabajo"
  >
</p>

---

### 2. Horas de sueño y calidad del descanso

Este bloque analiza la relación entre:
- Duración media del sueño  
- Calidad percibida del descanso  
- Nivel medio de estrés  

Todos los valores mostrados corresponden a **promedios**, evitando sumas agregadas que podrían distorsionar la interpretación por tamaño de grupo.

Los gráficos permiten observar una asociación consistente entre mejor calidad del descanso, mayor duración del sueño y menores niveles de estrés, sin asumir relaciones causales directas.

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/2080f276-04a8-4371-ad4e-dc9d54974de2"
    width="90%"
    alt="Bloque del dashboard sobre horas de sueño, calidad del descanso y niveles de estrés, con filtros por edad y género"
  >
</p>

---

### 3. Productividad percibida según modo de trabajo

Aquí se explora cómo varían las horas de pantalla y la productividad autopercibida en función de la modalidad laboral (presencial, híbrida y remota).

El análisis pone de manifiesto que:
- El trabajo remoto tiende a concentrar mayores horas de uso de pantallas.
- Este aumento no siempre se traduce en un incremento proporcional de la productividad percibida.

Esto sugiere una relación no lineal entre ambas variables y refuerza la importancia de considerar el contexto laboral en cualquier análisis sobre bienestar digital.

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/5d1e3ee3-370d-4aed-92d6-20a38f3e97d7"
    width="90%"
    alt="Bloque del dashboard que compara productividad percibida y horas de pantalla según modo de trabajo"
  >
</p>

---

### 4. Horas sociales y bienestar general

Este bloque cruza el uso de pantallas con indicadores de bienestar general por grupo de edad.

Se combinan:
- Una visualización de la distribución relativa del tiempo de pantalla.
- Un gráfico comparativo de promedios de horas de pantalla y bienestar percibido.

El objetivo es ofrecer una lectura contextual, observando variaciones entre grupos sin establecer juicios normativos sobre el uso tecnológico.

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/5aba7a2d-aaf4-4cc9-acf9-85d3921f3593"
    width="90%"
    alt="Bloque del dashboard que analiza la relación entre horas sociales, tiempo de pantalla y bienestar general por grupo de edad"
  >
</p>

## Decisiones de análisis y diseño

El dashboard no es el resultado de una única iteración, sino de un proceso de selección consciente orientado a mejorar la **coherencia analítica**, la **interpretabilidad** y la **accesibilidad** de los datos.

### 🔹 Elección de métricas
Las variables relacionadas con bienestar, estrés, sueño y uso de pantallas se representan mediante **promedios**, y no mediante sumas agregadas.  
Esta decisión evita que las diferencias observadas estén condicionadas por el tamaño de los grupos y permite comparaciones más coherentes entre perfiles.

### 🔹 Uso intencional de visualizaciones
El uso de gráficos circulares se ha limitado a funciones estrictamente descriptivas (distribución relativa), evitando su empleo para comparaciones directas entre variables.  
Las relaciones entre indicadores se analizan principalmente mediante **gráficos de barras** y **comparativas de promedios**, más adecuadas para este propósito.

### 🔹 Reducción de KPIs tradicionales
En lugar de indicadores sintéticos únicos, se optó por incorporar **mensajes interpretativos contextuales**, dependientes de los filtros activos.  
Este enfoque evita simplificaciones excesivas y favorece una lectura más reflexiva de los datos.

### 🔹 Diseño basado en exploración
Los *slicers* no se conciben como elementos auxiliares, sino como **herramientas centrales del análisis**.  
El dashboard está diseñado para explorar perfiles concretos y contrastar patrones entre grupos, sin conducir a una única conclusión predeterminada.

### 🔹 Enfoque ético y no causal
Dado el contexto de salud mental, todas las visualizaciones incluyen referencias explícitas a su carácter descriptivo.  
Las asociaciones observadas deben interpretarse como **tendencias generales**, no como relaciones causales directas.

---

## Accesibilidad y decisiones de diseño

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/c956728a-7ff2-4714-9197-b7f5320dfa82"
    width="35%"
    alt="Sobrecarga cognitiva y multitarea digital"
  >
</p>

<sub>Imagen conceptual sobre sobrecarga informativa que guía las decisiones de accesibilidad y reducción de carga cognitiva del dashboard.</sub>

El diseño del dashboard sigue principios básicos de **accesibilidad** y **claridad visual**:

- Paleta de colores coherente y con contraste suficiente.
- Uso consistente de escalas y métricas (promedios en lugar de sumas para variables personales).
- Textos explicativos breves que sustituyen a KPIs rígidos, favoreciendo una lectura reflexiva.
- Estructura modular que reduce la carga cognitiva y permite explorar los datos paso a paso.

Todos los elementos interactivos están pensados para **apoyar la exploración**, no para dirigir conclusiones cerradas.

---

## Nota metodológica

Los resultados mostrados deben interpretarse como **tendencias observadas en una muestra concreta**.  
Las diferencias entre grupos reflejan **patrones agregados** y no implican relaciones causales ni diagnósticos individuales.

Este enfoque busca respetar la complejidad del bienestar digital y evitar simplificaciones excesivas en un ámbito claramente multifactorial.
---

## Enfoque estadístico del análisis

El dashboard trabaja con **estadística descriptiva** a partir de la muestra del estudio *Screen Time vs Mental Wellness 2025*. No se realizan inferencias ni tests de hipótesis: el objetivo es retratar patrones dentro de esta muestra, no generalizar a toda la población.

### Tipo de variables

- **Nominales:** género, modo de trabajo, ocupación.  
- **Ordinales:** calidad del sueño, nivel de estrés, calidad del bienestar.  
- **De razón:** horas de pantalla, horas de sueño, horas sociales.

### Medidas utilizadas

- Para variables cuantitativas personales (sueño, estrés, bienestar, productividad) se utilizan **medias** y **porcentajes**, evitando sumas que solo reflejarían el tamaño del grupo.  
- Para distribuciones por segmentos (edad, nivel de uso, modalidad laboral) se muestran **frecuencias relativas** (porcentajes) para ver cómo se concentra el uso y detectar posibles asimetrías en los patrones.

### Qué no estamos haciendo

- No se calculan **intervalos de confianza** ni **contrastes de hipótesis**.  
- No se habla de **causalidad**, solo de asociaciones descriptivas observadas en esta muestra.

---

## Ejemplos de lectura estadística del dashboard

A continuación se resumen algunas conclusiones que pueden extraerse del dashboard usando herramientas de estadística descriptiva, sin ir más allá de lo que los datos permiten.

### Bloque 1 · Tiempo de pantalla y distribución del uso

- En la muestra, una parte de la población concentra la mayoría de las horas de pantalla: el grupo de **alto uso** reúne la mayor parte del tiempo total, aunque no representa la totalidad de las personas usuarias.  
- Al comparar **porcentaje de personas** y **porcentaje de horas**, el dashboard diferencia entre:
  - Frecuencia relativa (cuánta gente hay en alto/bajo uso).  
  - Peso en la carga total de uso (quién acumula más horas).  
- Cuando se filtra por edad o modo de trabajo, aparecen segmentos donde ambos porcentajes (usuarios de alto uso y horas totales) se disparan a la vez, lo que apunta a perfiles más expuestos a un uso intensivo de pantallas, sin afirmar que esto cause más estrés.

### Bloque 2 · Horas de sueño y calidad del descanso

- La muestra está desequilibrada: la mayoría de registros se agrupan en **buen descanso**, y un grupo mucho menor en **mal descanso**, algo importante al interpretar medias de grupos pequeños.  
- Las medias muestran un patrón consistente:
  - Quienes declaran buen descanso duermen **más horas** y presentan **menor nivel medio de estrés**.  
  - Quienes declaran mal descanso concentran **menos horas de sueño** y **más estrés medio**.  
- La diferencia entre grupos es más marcada en estrés que en horas de sueño, lo que sugiere que la **calidad percibida del descanso** recoge algo más que “cuántas horas duermo” (rutina, continuidad, despertares, etc.).

### Bloque 3 · Productividad percibida según modo de trabajo

- La modalidad **remota** presenta las mayores medias de horas de pantalla, pero la **productividad percibida** no aumenta en la misma proporción. No se observa una relación lineal simple del tipo “más pantalla = más productividad”.  
- Al comparar medias entre remoto, híbrido y presencial, las diferencias en productividad son moderadas frente a las diferencias en horas de pantalla, lo que apunta a una **correlación débil** entre ambas variables en esta muestra.  
- El dashboard funciona como una tabla de medias segmentadas: permite ver si hay cambios relevantes por modalidad sin necesidad de entrar en modelos de regresión.

### Bloque 4 · Horas sociales y bienestar general

- El reparto de horas de pantalla por edad es claramente **asimétrico**: los grupos de **25–34** y **35–44** años concentran la mayor parte del uso total, mientras que los extremos de edad aportan muchas menos horas.  
- Al cruzar **promedio de horas de pantalla** y **promedio de bienestar**, no aparece un patrón único del tipo “a más pantalla, peor bienestar” en todos los grupos. Algunos segmentos con muchas horas muestran niveles de bienestar similares a otros con menos pantalla.  
- Esto sugiere que la relación entre uso de pantallas y bienestar es **multifactorial** y que conviene leerla siempre junto con sueño y socialización. El texto lateral del dashboard recuerda que cada barra representa una **media de grupo**, no la realidad individual de cada persona.


# Análisis y Preguntas Clave

<p>
  <img 
    src="https://github.com/user-attachments/assets/7ce82c68-916e-4d95-8970-5dc6dadc152a"
    width="30%"
    alt="Diagrama conceptual que representa cómo la atención de una persona se reparte entre varias pantallas y contenidos digitales"
  >
</p>

- ¿Más horas de pantalla implican mayor estrés?  
- ¿El sueño modera el impacto del tiempo de pantalla?  
- ¿La socialización mejora el bienestar general?  
- ¿El modo de trabajo influye en la productividad percibida?  

---

# Cómo Ejecutar el Proyecto

| Paso | Acción | Detalle |
|------|--------|---------|
| **1** | Crear la base de datos en MySQL | Ejecutar el archivo `setup_mental_wellness.sql` en MySQL Workbench. Este script creará las tablas, cargará los datos y generará la tabla reducida `mental_wellness_sample`. |
| **2** | Configurar el archivo `.env` | Definir las variables de entorno con las credenciales de acceso a la base de datos:<br><br>`DB_HOST=localhost`<br>`DB_PORT=3306`<br>`DB_NAME=screen_time_wellness`<br>`DB_USER=usuario`<br>`DB_PASSWORD=contraseña` |
| **3** | Instalar dependencias | Instalar las librerías necesarias ejecutando:<br><br>`pip install -r requirements.txt` |
| **4** | Ejecutar el script de automatización | Ejecutar el pipeline completo con:<br><br>`python main.py`<br><br>Este paso generará automáticamente el archivo `output/mental_wellness_sample.csv`. |
| **5** | Actualizar el dashboard en Excel | Abrir el archivo de Excel y actualizar las conexiones para refrescar todas las tablas dinámicas, gráficos y KPIs. |

## Referencias

### Datos
- Screen Time vs Mental Wellness Survey 2025 (Kaggle)

### Documentación técnica
- pandas — documentación oficial  
- SQLAlchemy — documentación oficial  
- MySQL — documentación oficial  

### Accesibilidad digital
- WCAG 2.2 — Web Content Accessibility Guidelines  
- Ley 11/2023 sobre accesibilidad digital  

### Formación y contexto
- Factoría F5 — Madrid  
- Factoria-F5-madrid repositories  

### Recursos audiovisuales
- YouTube: *5 Reglas de Oro que debe cumplir un Dashboard*  
  https://www.youtube.com/watch?v=15BTK340OLo 

---

# Conclusiones del Proyecto

<p>
  <img 
    src="https://github.com/user-attachments/assets/4af33795-94d6-4718-a264-705ad3b94e3b"
    width="35%"
    alt="Personas utilizando el teléfono móvil durante un trayecto en transporte público, representando el uso cotidiano y normalizado de la tecnología digital"
  >
</p>

Los principales hallazgos del análisis ponen de relieve que el bienestar digital no puede explicarse a partir de una única variable, sino como el resultado de la interacción entre distintos factores personales y sociales:

- El tiempo de pantalla, por sí solo, no explica el malestar.  
  Los patrones emergen cuando se incorporan variables relacionadas con el sueño y la socialización.

- La calidad del sueño actúa como un mediador clave, con mayor peso que el número total de horas dormidas.

- Las horas dedicadas a la socialización mejoran de forma significativa el índice de bienestar, incluso en personas con un uso elevado de pantallas.

- El modo de trabajo influye en la productividad percibida, aunque no siempre guarda una relación directa con el nivel de estrés.

- El bienestar digital debe entenderse como un equilibrio, y no como un juicio moral sobre el uso de la tecnología.

- El análisis confirma que los hábitos digitales conforman un fenómeno complejo, en el que múltiples variables interactúan y se condicionan mutuamente.

Para ilustrar cómo estas conclusiones se manifiestan en segmentos concretos de la población, el dashboard permite explorar el comportamiento del uso digital en función de variables como edad, género y modo de trabajo:
Como ejemplo concreto, cuando filtramos el dashboard por hombres de 35-44 años que trabajan en remoto, casi todo el uso se concentra en niveles altos: el 95 % del tiempo registrado corresponde a “alto tiempo de pantalla” y solo el 5 % a “bajo”. En este mismo segmento, aproximadamente 7 de cada 10 usuarios (69 %) se sitúan en el grupo de alto uso, lo que sugiere un colectivo especialmente expuesto a un desequilibrio digital si no hay buenas rutinas de descanso y desconexión.

**Ejemplo de segmento en riesgo**

- Segmento: hombres, 35–44 años, trabajo remoto  
- % de usuarios con alto tiempo de pantalla: **69 %**  
- % del tiempo total que corresponde a alto uso: **95 %**  
- % del tiempo total con bajo uso: **5 %**

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/1624b471-3c50-4324-8bd0-d9b72bbb483e"
    width="70%"
    alt="Vista del dashboard filtrado por hombres de 35 a 44 años en modalidad remota, mostrando una alta concentración de tiempo de pantalla frente a un bajo peso del uso reducido"
  >
</p>

# Gracias por leer este proyecto

Este proyecto nace de la intención de mirar el bienestar digital con un poco más de calma. Utiliza los datos como punto de partida para reflexionar, no para juzgar, y asume que la relación entre tecnología y salud mental es compleja y llena de matices.

Las cifras no buscan señalar comportamientos “correctos” o “incorrectos”, sino abrir preguntas y ayudar a tomar decisiones más conscientes.

Si quieres mejorar tu propio pipeline, desarrollar un dashboard accesible o explorar este tema desde tus propios datos, estaremos encantados de ayudarte.

---

# 👩‍💻 Contribuyentes

| Nombre           | GitHub | LinkedIn |
|------------------|--------|----------|
| Jaime Amuedo     | [![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JaimeAmuedoJAH) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jaime-amuedo-a432bb354/) |
| Rocío Pérez López | [![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Rociointhecloud) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rocio-perez-lopez-a59259178/) |
| Mariana Moreno    | [![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MarianaMH1195) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariana-moreno-henao-70305a16b) |

---






