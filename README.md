# Mental Wellness & Screen Time — Proyecto IIII  

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
 │   ┣ digital_welness.xlsx 
 ┣ 📁 output/
 │   ┗ datos_mental_wellness_sample_2025.csv  
 ┣ 📁 script_sql/
 │   ┗ creacion_bd.sql  
 ┣ 📁 src/
 │   ┣ init.py
 │   ┣ BD_ETL.py
 │   ┗ config.py
 ┣ 📄 .env.example
 ┣ 📄 .gitignore
 ┣ 📄 main.py
 ┣ 📄 README.md
 ┗ 📄 requirements.txt
 ```
---

## Gestión del trabajo y avance del proyecto (Kanban · Agile)

---

### MARTES · 2/12

#### ROCÍO · Product Owner

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Buscar base de datos actual que sustituya a Sakila (evitar datasets obsoletos).<br>- Verificar condición del formador: base relacional y tamaño reducido (~17 filas).<br>- Preparar propuesta clara para el equipo.<br>- Avanzar README (estructura general y accesibilidad).<br>- Buscar imágenes para storytelling del proyecto. |
| **DOING** | - Revisión de bases de datos recientes (2025) y evaluación de viabilidad.<br>- Documentación de decisiones técnicas y adaptación del dataset.<br>- Comunicación interna para definir roles, tiempos y enfoque.<br>- Propuesta formal de rol como Product Owner. |
| **DONE** | - Selección de dataset: Screen Time vs Mental Wellness Survey (2025).<br>- Diseño del modelo relacional.<br>- Decisión de generar tabla final de 17 filas desde el dataset completo.<br>- Validación del formador:<br>&nbsp;&nbsp;• Base de datos aprobada.<br>&nbsp;&nbsp;• Flujo aprobado: MySQL (normalización) → Python → Excel.<br>- Primer borrador del README completado.<br>- Imágenes seleccionadas y registradas. |

---

#### JAIME · Scrum Master

| Estado | Tareas |
| ------ | ------ |
| **TO DO** |  |
| **DOING** |  |
| **DONE** |  |

---

#### MARIANA · Data Analyst

| Estado | Tareas |
| ------ | ------ |
| **TO DO** |  |
| **DOING** |  |
| **DONE** |  |

---

### MIÉRCOLES · 3/12

#### ROCÍO · Product Owner

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Analizar integración del video compartido (YouTube).<br>- Enviar README al formador.<br>- Añadir en README:<br>&nbsp;&nbsp;• “Para quién es este dashboard”.<br>&nbsp;&nbsp;• Mapa del dashboard y cómo leerlo.<br>&nbsp;&nbsp;• “Qué decisiones permite tomar”.<br>&nbsp;&nbsp;• Bloque inicial “En 20 segundos”.<br>- Redefinir paleta de colores con propósito.<br>- Revisar estructura del dashboard.<br>- Verificar que cada gráfico responde a una sola pregunta.<br>- Ajustar textos para reducir carga cognitiva. |
| **DOING** | - Integración de reglas del video en la documentación.<br>- Revisión de saturación de KPIs.<br>- Ajustes de layout según retícula. |
| **DONE** | - Resumen del video realizado.<br>- Aplicación conceptual de reglas al proyecto.<br>- Identificación de mejoras en dashboard y README. |

---

#### TRABAJO CONJUNTO · ROCÍO + JAIME  
**Horario:** 11:30 – 14:00

**Incidencias detectadas**

- Unknown table en DROP / INSERT.
- Tipos incompatibles en `user_id`.
- Errores de sintaxis SQL (1064).
- Bloqueos por claves foráneas.
- Incompatibilidad FK / PK.
- Bloqueo por `secure-file-priv`.
- Advertencias `utf8` / `utf8mb3`.

**Acciones realizadas**

- Corrección del orden de ejecución de scripts.
- Homogeneización de `user_id` como INT.
- Ajuste de engines a InnoDB.
- Carga de datos vía Python (`pandas → to_sql`).
- Corrección de sintaxis SQL.
- Verificación de tablas y registros.
- Limpieza de CSV y encoding previo a inserción.

**Resultado**

- 400 registros cargados en `mental_wellness_raw`.
- Tablas normalizadas correctamente.
- Tabla final de muestra creada (17 filas).
- Flujo MySQL → Python → CSV operativo.
- Output listo: `mental_wellness_sample.csv`.

**Estado:** Resuelto.

---

#### MARIANA · Data Analyst  

> Nota: Mariana avisó previamente al equipo de que no podría estar presente durante la jornada.

| Estado | Tareas |
| ------ | ------ |
| **TO DO** |  |
| **DOING** |  |
| **DONE** |  |

---

#### JAIME · Scrum Master (miércoles)

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Compartir aprendizajes de proyectos anteriores.<br>- Aplicar buenas prácticas de repositorios Factoría F5 (Madrid).<br>- Mejorar atractivo visual y coherencia del proyecto. |
| **DOING** |  |
| **DONE** |  |

---

#### MARIANA · Data Analyst

| Estado | Tareas |
| ------ | ------ |
| **TO DO** |  |
| **DOING** |  |
| **DONE** |  |

---

### JUEVES

#### ROCÍO · Product Owner (ausente)  

> Nota: Rocío avisó previamente de que no podría asistir y no estuvo presente durante la jornada.

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Solicitar actualización del estado del proyecto al equipo.<br>- Revisar avances de Excel, tablas dinámicas, KPIs y dashboard más adelante.<br>- Mantener seguimiento asíncrono del progreso. |
| **DOING** | - Comunicación asíncrona con el equipo para conocer el estado del trabajo.<br>- Revisión posterior del README ya compartido como guía de trabajo. |
| **DONE** | - Aviso previo de ausencia al equipo.<br>- Alineación previa del alcance y criterios del dashboard a través del README.<br>- Coordinación asíncrona para asegurar continuidad del proyecto. |

---

#### JAIME · Scrum Master

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Continuar desarrollo del dashboard en Excel.<br>- Asegurar coherencia entre KPIs, tablas dinámicas y objetivos del proyecto. |
| **DOING** | - Creación y ajuste de tablas dinámicas a partir del dataset final.<br>- Definición y validación de KPIs principales.<br>- Construcción del dashboard en Excel junto a Mariana.<br>- Revisión de estructura, filtros y lectura del dashboard. |
| **DONE** | - Dashboard funcional en Excel.<br>- KPIs definidos y conectados a tablas dinámicas.<br>- Avance sólido alineado con el README y el objetivo del proyecto. |

---

#### MARIANA · Data Analyst

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Preparar datos para visualización en Excel.<br>- Apoyar definición de métricas clave. |
| **DOING** | - Limpieza y preparación de datos para Excel.<br>- Creación de tablas dinámicas.<br>- Apoyo en la definición de KPIs.<br>- Colaboración directa en la construcción del dashboard.<br>- Validación de cálculos y consistencia de datos. |
| **DONE** | - Datos listos para análisis en Excel.<br>- Tablas dinámicas correctamente configuradas.<br>- Métricas y KPIs validados.<br>- Contribución directa al dashboard final. |

---

### VIERNES · 5/12  
**Cierre de sprint · Reflexión y mejora continua**

#### ROCÍO · Product Owner

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Identificar puntos de fricción en el flujo de trabajo.<br>- Priorizar mejoras de comunicación y documentación para futuros proyectos.<br>- Revisar si los objetivos iniciales se tradujeron claramente en el dashboard final. |
| **DOING** | - Revisión crítica del backlog ejecutado vs. backlog inicial.<br>- Reflexión sobre claridad de requisitos, tiempos y dependencias.<br>- Recogida de feedback del equipo para mejorar la coordinación. |
| **DONE** | - Identificación de aprendizajes clave:<br>&nbsp;&nbsp;• La documentación temprana (README) acelera el trabajo técnico.<br>&nbsp;&nbsp;• La definición clara de “qué decisión responde cada gráfico” evita retrabajo.<br>- Refuerzo del rol de Product Owner como eje de alineación entre técnica y negocio.<br>- Propuesta de mejora: dedicar más tiempo inicial a validar visualizaciones antes de construirlas. |

---

#### JAIME · Scrum Master

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Detectar bloqueos técnicos recurrentes.<br>- Analizar cómo anticipar incidencias similares en próximos proyectos. |
| **DOING** | - Evaluación del flujo Kanban y del reparto de tareas.<br>- Revisión de puntos donde se concentró el trabajo técnico crítico. |
| **DONE** | - Aprendizajes identificados:<br>&nbsp;&nbsp;• Importancia del orden de ejecución y consistencia de tipos en bases de datos.<br>&nbsp;&nbsp;• Valor de atacar los bloqueos técnicos temprano para no frenar al equipo.<br>- Mejora propuesta:<br>&nbsp;&nbsp;• Añadir checkpoints técnicos intermedios antes de integrar cambios grandes.<br>- Consolidación del rol de Scrum Master como facilitador, no solo resolutor. |

---

#### MARIANA · Data Analyst

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Revisar impacto real de KPIs y visualizaciones creadas.<br>- Detectar oportunidades para simplificar métricas sin perder información. |
| **DOING** | - Análisis crítico de tablas dinámicas y KPIs.<br>- Revisión de si los datos apoyan una lectura clara del problema. |
| **DONE** | - Aprendizajes:<br>&nbsp;&nbsp;• Menos métricas aportan más claridad.<br>&nbsp;&nbsp;• La validación previa de cálculos evita correcciones posteriores.<br>- Mejora propuesta:<br>&nbsp;&nbsp;• Iterar primero sobre tablas dinámicas antes de cerrar el dashboard final.<br>- Refuerzo del rol analítico orientado a decisiones, no solo a datos. |

---

### CONCLUSIÓN DEL EQUIPO

- El uso de Kanban facilitó visibilidad, foco y coordinación.
- La definición clara de roles evitó solapamientos.
- Detectamos que documentar, revisar y reflexionar no ralentiza el proyecto: lo hace más sólido.
- El próximo proyecto se abordará con:
  - Más validaciones tempranas.
  - Menos retrabajo.
  - Mayor intención en cada decisión visual y técnica.


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

El dashboard no es el resultado de una única iteración, sino de un proceso de selección consciente orientado a mejorar la coherencia analítica, la interpretabilidad y la accesibilidad de los datos.

### Elección de métricas
Las variables relacionadas con bienestar, estrés, sueño y uso de pantallas se representan mediante **promedios**, y no sumas agregadas. Esta decisión evita que las diferencias observadas estén condicionadas por el tamaño de los grupos y permite comparaciones más coherentes entre perfiles.

### Uso intencional de visualizaciones
Se ha limitado el uso de gráficos circulares a funciones estrictamente descriptivas (distribución relativa), evitando su empleo para comparaciones directas entre variables. Las relaciones entre indicadores se analizan principalmente mediante gráficos de barras y comparativas de promedios, más adecuadas para este propósito.

### Reducción de KPIs tradicionales
En lugar de indicadores sintéticos únicos, se optó por incorporar **mensajes interpretativos contextuales**, dependientes de los filtros activos. Este enfoque evita simplificaciones excesivas y favorece una lectura más reflexiva de los datos.

### Diseño basado en exploración
Los slicers no se conciben como elementos auxiliares, sino como herramientas centrales del análisis. El dashboard está diseñado para explorar perfiles concretos y contrastar patrones entre grupos, sin conducir a una única conclusión predeterminada.

### Enfoque ético y no causal
Dado el contexto de salud mental, todas las visualizaciones incluyen referencias explícitas a su carácter descriptivo. Las asociaciones observadas deben interpretarse como tendencias generales y no como relaciones causales directas.

---

## Accesibilidad y decisiones de diseño

El diseño del dashboard sigue principios básicos de accesibilidad y claridad visual:

- Paleta de colores coherente y con contraste suficiente.
- Uso consistente de escalas y métricas (promedios en lugar de sumas para variables personales).
- Textos explicativos breves que sustituyen a KPIs rígidos, favoreciendo una lectura reflexiva.
- Estructura modular que reduce la carga cognitiva y permite explorar los datos paso a paso.

Además, todos los elementos interactivos están pensados para apoyar la exploración, no para dirigir conclusiones cerradas.
---

## Nota metodológica

Los resultados mostrados deben interpretarse como **tendencias observadas en una muestra concreta**. Las diferencias entre grupos reflejan patrones agregados y no implican relaciones causales ni diagnósticos individuales.

Este enfoque busca respetar la complejidad del bienestar digital y evitar simplificaciones excesivas en un ámbito claramente multifactorial.

---


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
