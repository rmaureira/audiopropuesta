# Propuesta de Nueva Constitución en Audio

En este repositorio podrán encontrar la Propuesta de Nueva Constitución, preparada por la Convención Constitucional, y publicada en su sitio [web](https://chileconvencion.cl), en formatos adicionales (Audio, Texto plano)

## Archivos

En la carpeta [txt/](txt/) podrán encontrar el texto completo de la propuesta, así como todos los artículos en formato TXT.

En la carpeta [mp3/](mp3/) encontrarán todos los artículos en formato MP3 v2 (32 kbps, 24 kHZ, mono) 

En la carpeta [scripts/](scripts/) está el script en Python que usé para convertir los textos en audio, usando la API [Text to Speech](https://cloud.google.com/text-to-speech) de Google Cloud

## Podcast
Los audios por capítulo, en formato podcast se pueden encontrar en:

[RSS.com](https://rss.com/podcasts/audiopropuesta/)

[Spotify](https://open.spotify.com/show/3DzXhzLwD8AT1jvxzBvcm8)

[Apple Podcasts](https://podcasts.apple.com/us/podcast/la-nueva-constitución-en-audio/id1633122737)

[Amazon Music](https://music.amazon.com/podcasts/6c0a5687-1061-4c99-99d5-48d59fc8bb36/la-nueva-constituci%C3%B3n-en-audio)

## TO DO
- ~~Agregar archivos de audio por capítulo completo~~
- Agregar duración de cada audio
- ~~Publicar los audios como podcast (?)~~

### Comentarios
Si encuentran algún error en los archivos, por favor, reportarlo como issue en este repositorio.

Existe una pequeña diferencia entre el texto oficial, y el texto que está en los archivos, y es la adición de muchos puntos (.) adicionales, esto para forzar pausas en el audio, pues el algoritmo de TTS usa los puntos para generar pausas naturales durante la generación.

Las voces que usé son del tipo [WaveNet](https://www.deepmind.com/blog/wavenet-a-generative-model-for-raw-audio), pues suenan un poco más naturales que las estándar. Los nombres de archivo contienen el identificador de las 2 voces usadas.

Si quieren recrear los audios en calidad distinta, u otra API, lo mejor es usar los archivos individuales de texto, pues estos ya están preparados para ese fin.

El script está sacado de los ejemplos del cliente de Python para las API de Google Cloud, los cuales están [acá](https://github.com/googleapis/python-texttospeech/tree/main/samples). Es mejor usar eso como ejemplo, y no mi versión.

La motivación para hacer esto, es por un lado la accesibilidad, el PDF publicado no es muy accesible, en especial para quienes deban usar lectores de pantalla, como las personas de visión reducida, o carentes de ella. Pero por otro lado, porque personalmente, tener el texto en formato audio me podría dar la oportunidad de escucharlo durante traslados en transporte.

¿Se puede hacer mejor? Sí, siempre, pero esto es solo una forma de ofrecer una solución rápida.
