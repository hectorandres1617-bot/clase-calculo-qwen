# Clase de cálculo integral con una IA local (Qwen + Ollama + Open WebUI)

Material del video de **Automátika**: una IA que corre en un computador propio (Qwen 3.8 de 27B, con Ollama y Open WebUI) da una clase de cálculo integral de menos a más. Probado el 17-nov-2026.

**Para qué sirve este repositorio:** que puedas comprobar las cuentas del video y repetir las animaciones.

## Comprobar los resultados (no necesita instalar nada)
```
python3 scripts/verificar.py
```
Calcula con el método de Simpson: área bajo 3x²+1 en [0,2] = 10; área entre y=x e y=x² = 1/6; volumen del sólido de y=√x (discos) = 8π ≈ 25,13; ∫x·ln x en [0,1] = −1/4; ∫1/x² desde 1 → 1.

## Error de la IA que encontramos
Qwen dijo que el sólido de y=√x girado «es un cono». Es un paraboloide: el cono daría 16π/3 ≈ 16,76 y el volumen correcto es 8π ≈ 25,13. Siempre hay que revisar a la IA.

## Animaciones y gráficas
```
pip install matplotlib numpy      # además necesitas ffmpeg instalado
python3 scripts/animaciones.py riemann,entre,volumen,impropia      # horizontal 1920x1080
python3 scripts/animaciones.py riemann,entre,volumen,impropia v    # vertical 1080x1920
python3 scripts/graficas.py
```
(crea antes una carpeta `anim/` y otra `capturas/`). Las gráficas las hace Python con los datos de los ejemplos; Qwen no las dibujó.

## Cómo se obtuvo la clase
`scripts/clase.py` abre Open WebUI con Playwright, elige el modelo y envía tres mensajes (nivel 1, 2 y 3). Necesita Ollama con el modelo `qwen3.8:27b`, Open WebUI en `127.0.0.1:3030` y `pip install playwright`. Los mensajes están al inicio del script.

## Aviso
Contenido educativo hecho con ayuda de IA; no es consejo profesional. Licencia MIT.
