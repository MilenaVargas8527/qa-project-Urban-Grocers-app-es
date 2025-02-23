# Proyecto Urban Grocers

Soy Milena Vargas y este es el proyecto del Sprint 7 de Tripleten

Proyecto de Pruebas Automatizadas para Urban Grocers

Descripción General
Este proyecto contiene pruebas automatizadas para la aplicación Urban Grocers, enfocadas en la validación de su API, la creación de un usuario en su campo “name” y la creación de un KIT de productos. Las pruebas están diseñadas para verificar el correcto comportamiento del sistema, detectar posibles errores y asegurar la calidad del software.

Estructura del Proyecto
• tests/ → Contiene los archivos de prueba automatizados.
• sender_stand_request.py → Módulo para enviar solicitudes a la API.
• data.py → Contiene datos de prueba.
• configuration.py → Configuración del servicio (URLs, variables, etc.).

Se utiliza Python junto con pytest para la ejecución de pruebas funcionales y de API.
Instalación y Configuración
Para ejecutar este proyecto en un entorno local, sigue estos pasos:

Clonar el repositorio:
git clone https://github.com/MilenaVargas8527/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es

Instalar las librerías necesarias:
pip install pip pytest requests
Ejecución de Pruebas
Para ejecutar todas las pruebas desde la terminal, usa el siguiente comando:
pytest
Si deseas ejecutar pruebas específicas, puedes hacerlo con:
pytest tests/nombre_de_la_prueba.py

Casos de Prueba Implementados

Se han implementado pruebas para la validación del parámetro name en la creación de usuario y la creación de un KIT de productos. Se realizaron:
• Pruebas de aserción positiva (positive assert): Validaciones cuando se ingresan datos correctos.
• Pruebas de aserción negativa (negative assert): Identificación de errores cuando se ingresan datos inválidos.
Durante las pruebas, se identificaron varios bugs, los cuales han sido documentados.

Requisitos Previos
Para más información sobre los requisitos y especificaciones de la API de Urban Grocers, consulta la documentación en el siguiente enlace: API Urban Grocers
