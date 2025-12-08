# Proceso de trabajo y seguimiento Agile

Este documento recoge el seguimiento detallado del proyecto  
**Mental Wellness & Screen Time — Proyecto IV**, incluyendo:

- Organización del trabajo en sprints
- Distribución de tareas por rol
- Incidencias técnicas y su resolución
- Iteraciones de mejora post-sprint

El objetivo de este archivo es documentar el **proceso de trabajo y coordinación del equipo**,  
sin sobrecargar el README principal, que se centra en el producto final y el análisis.

---

### Enfoque de trabajo (Agile · 3 sprints)

El proyecto se desarrolló aplicando metodología **Agile**, organizado en **tres sprints iterativos** que permitieron avanzar progresivamente desde la base técnica hasta el refinamiento del dashboard final.

Este enfoque facilitó la validación temprana de decisiones, la resolución de bloqueos técnicos y la mejora continua sin reabrir el alcance del proyecto.

### MARTES · 2/12

#### ROCÍO · Product Owner

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Buscar base de datos actual que sustituya a Sakila (evitar datasets obsoletos).<br>- Verificar condición del formador: base relacional y tamaño reducido.<br>- Preparar propuesta clara para el equipo.<br>- Avanzar README (estructura general y accesibilidad).<br>- Buscar imágenes para storytelling del proyecto. |
| **DOING** | - Revisión de bases de datos recientes (2025) y evaluación de viabilidad.<br>- Documentación de decisiones técnicas y adaptación del dataset.<br>- Comunicación interna para definir roles, tiempos y enfoque.<br>- Propuesta formal de rol como Product Owner. |
| **DONE** | - Selección de dataset: Screen Time vs Mental Wellness Survey (2025).<br>- Diseño del modelo relacional.<br>- Decisión de generar tabla final de 17 filas desde el dataset completo.<br>- Validación del formador:<br>&nbsp;&nbsp;• Base de datos aprobada.<br>&nbsp;&nbsp;• Flujo aprobado: MySQL (normalización) → Python → Excel.<br>- Primer borrador del README completado.<br>- Imágenes seleccionadas y registradas. |

---

#### JAIME · Scrum Master

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Preparar proyecto en común a mis compañeras, normalzación de la base de datos, corrección de bugs con el script que teníamos para pasar de dataset a una base de datos relacional. |
| **DOING** | - Revisión de la base de datos elegida, normalización del dataset y dividision en tablas relacionales. |
| **DONE** | - Elección dataset Scren Time vs Mental Wellness Survey como base de datos relacional, elección de roles, realizar estructura del proyecto, asignación de tareas, realización del proyecto dentro de github con tablero kanban.|

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
| **TO DO** | - Compartir aprendizajes de proyectos anteriores.<br>- Aplicar buenas prácticas de repositorios Factoría F5 (Madrid).<br>- Mejorar atractivo visual y coherencia del proyecto, corrección de bug que no deja ejecutar correctamente el script. Inicio de revisión script de python|
| **DOING** | - Correción bug de script sql, revisión de script de python. |
| **DONE** | - Bug corregido de script sql para poder generar la base de datos relacional, revisión de parte de script de python (Aun falta por revisar código) |

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
| **TO DO** | - Continuar desarrollo del dashboard en Excel.<br>- Asegurar coherencia entre KPIs, tablas dinámicas y objetivos del proyecto. Revisión y modifación del código de python para que funcione correctamente, Creación de entorno virtual e imports de librerias necesarias para el proceso de ETL.|
| **DOING** | - Creación y ajuste de tablas dinámicas a partir del dataset final.<br>- Definición y validación de KPIs principales.<br>- Construcción del dashboard en Excel junto a Mariana.<br>- Revisión de estructura, filtros y lectura del dashboard. Modificación codigo python|
| **DONE** | - Dashboard funcional en Excel.<br>- KPIs definidos y conectados a tablas dinámicas.<br>- Avance sólido alineado con el README y el objetivo del proyecto. Script de python funcional, realiza la tarea que necesitamos para el proyecto.|

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
| **TO DO** | - Detectar bloqueos técnicos recurrentes.<br>- Analizar cómo anticipar incidencias similares en próximos proyectos. Confirmar pr`s pendientes y mergear ramas. Parte principal del proyecto terminado solo falta revisión y puesta en comun de ideas para modificar lo necesario|
| **DOING** | - Evaluación del flujo Kanban y del reparto de tareas.<br>- Revisión de puntos donde se concentró el trabajo técnico crítico. |
| **DONE** | - Aprendizajes identificados:<br>&nbsp;&nbsp;• Importancia del orden de ejecución y consistencia de tipos en bases de datos.<br>&nbsp;&nbsp;• Valor de atacar los bloqueos técnicos temprano para no frenar al equipo.<br>- Mejora propuesta:<br>&nbsp;&nbsp;• Añadir checkpoints técnicos intermedios antes de integrar cambios grandes.<br>- Consolidación del rol de Scrum Master como facilitador, no solo resolutor. Pull requests confrimados. Puesto en pie una reunión para terminar de confirmar todos los cambios del proyecto.|

---

#### MARIANA · Data Analyst

| Estado | Tareas |
| ------ | ------ |
| **TO DO** | - Revisar impacto real de KPIs y visualizaciones creadas.<br>- Detectar oportunidades para simplificar métricas sin perder información. |
| **DOING** | - Análisis crítico de tablas dinámicas y KPIs.<br>- Revisión de si los datos apoyan una lectura clara del problema. |
| **DONE** | - Aprendizajes:<br>&nbsp;&nbsp;• Menos métricas aportan más claridad.<br>&nbsp;&nbsp;• La validación previa de cálculos evita correcciones posteriores.<br>- Mejora propuesta:<br>&nbsp;&nbsp;• Iterar primero sobre tablas dinámicas antes de cerrar el dashboard final.<br>- Refuerzo del rol analítico orientado a decisiones, no solo a datos. |

---
### SÁBADO · Iteración de refinamiento (post-sprint)

> Trabajo de refinamiento realizado de forma asíncrona tras el cierre del sprint, orientado a mejorar la coherencia analítica, la claridad visual y la accesibilidad del dashboard final, **partiendo del trabajo ya desarrollado por el equipo**.

#### ROCÍO · Product Owner

| Estado | Tareas |
| ------ | ------ |
| **DONE** | - Unificación de criterios estadísticos (uso consistente de promedios en variables personales).<br>- Revisión del peso de KPIs numéricos y sustitución por mensajes interpretativos contextuales.<br>- Clarificación de títulos y preguntas analíticas asociadas a cada gráfico.<br>- Reducción de visualizaciones redundantes para disminuir carga cognitiva.<br>- Mejora de legibilidad (escalas, contraste y coherencia visual).<br>- Refuerzo del rol de los slicers como herramienta central de exploración. |

**Nota:**  
Esta iteración consolida y refina el dashboard construido durante el sprint, sin modificar el alcance funcional ni las métricas definidas previamente.

---

### LUNES · 8/12  
**Documentación final · Accesibilidad · Análisis estadístico**

#### ROCÍO · Product Owner

| Estado | Tareas |
|------|------|
| **TO DO** | - Revisar el README completo desde la perspectiva del lector externo.<br>- Unificar el enfoque estadístico del análisis para evitar interpretaciones erróneas.<br>- Mejorar la claridad metodológica sin añadir complejidad innecesaria.<br>- Reorganizar secciones para mejorar legibilidad y jerarquía visual. |
| **DOING** | - Redacción completa del bloque de **enfoque estadístico** (tipo de variables, medidas utilizadas y qué no se está haciendo).<br>- Revisión crítica de conclusiones para asegurar coherencia con estadística descriptiva.<br>- Ajuste del lenguaje para eliminar ambigüedades y evitar cualquier lectura causal.<br>- Integración del discurso de accesibilidad y reducción de carga cognitiva en el README. |
| **DONE** | - README actualizado con una sección de estadística clara, defendible y alineada con el dashboard.<br>- Incorporación de ejemplos de lectura estadística coherentes con los gráficos.<br>- Refuerzo explícito del enfoque ético y no causal en todo el análisis.<br>- Mejora de la estructura general del README para facilitar una lectura rápida y profunda.<br>- Verificación final de consistencia entre documentación, visualizaciones y objetivos del proyecto. |

---

### LUNES · 8/12  
**Preparación de la presentación final · Coordinación de equipo**

> Reunión de equipo a las **12:00** para revisar el estado final del proyecto y preparar la presentación del martes conforme a las indicaciones del formador.

#### TRABAJO DE EQUIPO · PRESENTACIÓN FINAL

| Estado | Tareas |
|------|------|
| **TO DO** | - Revisar en conjunto los requisitos de la presentación (10 minutos, 2–3 diapositivas, enfoque claro y conciso).<br>- Decidir el formato final de la presentación (una diapositiva tipo *canvas* como apoyo visual).<br>- Acordar qué partes del proyecto mostrar y cuáles dejar en segundo plano. |
| **DOING** | - Revisión completa del proyecto (README, repositorio y dashboard final) para asegurar coherencia.<br>- Selección de los puntos clave a presentar:<br>&nbsp;&nbsp;• Organización del equipo y roles.<br>&nbsp;&nbsp;• Herramientas utilizadas (Kanban, pipeline, Excel).<br>&nbsp;&nbsp;• Demostración del dashboard final.<br>- Distribución de los turnos de palabra para una presentación fluida y equilibrada. |
| **DONE** | - Estructura de la presentación acordada y alineada con las instrucciones del formador.<br>- Definición clara de quién presenta cada parte:<br>&nbsp;&nbsp;• Organización y metodología de trabajo.<br>&nbsp;&nbsp;• Explicación breve del pipeline y herramientas.<br>&nbsp;&nbsp;• Navegación guiada por el dashboard.<br>- Decisión de utilizar **una diapositiva tipo canvas** como soporte visual, evitando sobrecargar con slides.<br>- Mensaje común consensuado para transmitir el objetivo y valor del proyecto de forma clara y breve. |

### CONCLUSIÓN DEL EQUIPO

- El uso de Kanban facilitó visibilidad, foco y coordinación.
- La definición clara de roles evitó solapamientos.
- Detectamos que documentar, revisar y reflexionar no ralentiza el proyecto: lo hace más sólido.
- El próximo proyecto se abordará con:
  - Más validaciones tempranas.
  - Menos retrabajo.
  - Mayor intención en cada decisión visual y técnica.
---