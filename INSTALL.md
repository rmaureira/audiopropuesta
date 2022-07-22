# Conversión de archivos

A continuación detallo los pasos para poder utilizar el API de [Text-to-Speech](https://cloud.google.com/text-to-speech/?hl=es_419) de Google Cloud.

## Paso 1

Instalar Google Cloud SDK, las instrucciones se encuentran [acá](https://cloud.google.com/sdk/docs/install)

## Paso 2

Crear un proyecto nuevo en Google Cloud usando la herramienta ```gcloud```

```gcloud projects create $PROJECT_ID```

Opcionalmente se puede usar la opción ```--set-as-default``` para configurar el proyecto como default para los siguientes comandos

Si el proyecto ya lo tienen, pueden marcar el proyecto como default con el comando

```gcloud config set project $PROJECT_ID```

## Paso 3

Habilitar la API de Text-to-Speech

```gcloud services enable texttospeech.googleapis.com```

Inicializar la autenticación usando las credenciales por default, existen otros mecanismos que se pueden revisar en la [documentación](https://cloud.google.com/sdk/gcloud/reference/auth/application-default)

```gcloud auth application-default login```

## Paso 4

Instalar módulos de Python necesarios

```pip3 install google-cloud-texttospeech```

## Paso 5

Ejecutar el script, pasando el archivo con texto como argumento

```python3 scripts/tts.py archivo.txt```