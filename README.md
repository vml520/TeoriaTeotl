# Teoría del Campo Teotl (TFT)

## Convocatoria abierta a la colaboración científica

**Un marco de física fundamental con raíces filosóficas mesoamericanas,
problemas abiertos bien planteados, y código ejecutable que respalda cada
afirmación.**

-----

## Qué es esto

La Teoría del Campo Teotl (TFT) toma en serio el reloj interno de de Broglie:
si mc² = hf, entonces la masa *es* un proceso periódico real. TFT pregunta qué
estructura mínima se sigue de esa lectura, y propone un campo de fase θ con
valores en el círculo, con dos escalas primitivas (E₀, ℓ₀) y una hipótesis
central: la compacidad del tiempo.

La ontología hacia la que este trabajo se dirige es el *teotl* del pensamiento
náhuatl — la realidad como proceso generativo, no como sustancia — siguiendo la
reconstrucción filosófica de Miguel León-Portilla. Declaramos esta orientación
abiertamente, al estilo de Newton (*hypotheses non fingo*, invertido): la
ontología es dirección y motivación; las matemáticas deben sostenerse por sí
solas. Este no es un marco terminado. Es un programa de investigación que
necesita expertos, y queremos que esos expertos estén en México.

-----

## Lo que está construido y verificado

Cada resultado lleva su etiqueta epistémica: **DERIVADO** (se sigue de la
acción por cálculo, verificado numéricamente), **PROPUESTO** (identificación
motivada, aún no forzada), o **ABIERTO** (brecha conocida). Todo es
reproducible con los scripts incluidos en este repositorio.

**La acción y sus consecuencias** (`verify_derivations.py`):

> S[θ] = (E₀/ℓ₀) ∫dt ∫d³x [ (1/2c²)(∂θ/∂t)² − ½|∇θ|² − (Λ/ℓ₀²)(1 − cos θ) ]

- Masa del solitón (kink): M = 8√Λ·E₀/c² — la inercia como energía de una
  estructura de fase topológicamente protegida. **DERIVADO**, verificado con
  error relativo < 10⁻⁸.
- Ley de fuerza sobre solitones bajo tensión de fase: F = −2πf por unidad de
  enrollamiento. **DERIVADO**, verificado al ~2 %.
- Cinemática relativista exacta de los solitones (sector 1D). **DERIVADO.**
- Cuantización de la energía, E_n = nE₀, como consecuencia de la topología
  temporal compacta. **DERIVADO dada la compacidad; la compacidad misma es el
  postulado central del marco.** (Obligación de literatura previa: la Teoría de
  Ciclos Elementales de D. Dolce; el diálogo está pendiente y es bienvenido.)

**El emulador de qubit de campo** (`teotl_qc.py`):

- Oscilación de Rabi con contraste 0.995; linealidad frecuencia–amplitud con
  r = 0.997; conservación de masa < 10⁻⁵. **DERIVADO.**
- Resultado de frontera: la transición exacta entre dinámica clásica
  sincronizante (acoplamiento sin, tipo Kuramoto) y dinámica unitaria
  (acoplamiento cos ponderado por amplitud — la forma de Madelung/Bohm).

**La prueba de Bell** (`teotl_chsh.py`) — incluimos nuestro resultado negativo
con el mismo orgullo que los positivos:

- Referencia cuántica exacta con el mismo protocolo de pulsos: S = 2.8284
  (cota de Tsirelson). El instrumento funciona.
- El campo local de TFT: **S = 2.0000 exactamente** — satura la cota clásica y
  no la cruza. Una conjetura nuestra (que el campo podría realizar cómputo
  cuántico con recursos polinomiales) **fue refutada por nuestro propio
  experimento.** Lo reportamos porque esa es la disciplina que pedimos.
- El campo conectado con tiempo cíclico produce S > 2 solo con violaciones
  masivas de no-señalización — es comunicación, no violación de Bell.

**Optimización nativa de fase** (`maxcut_tft.py`):

- La dinámica de asentamiento del campo resuelve MAX-CUT: encuentra los óptimos
  conocidos exactamente en instancias estructuradas; queda 1.5–4 % por debajo
  de recocido simulado afinado en instancias aleatorias — exactamente la banda
  reportada para las máquinas de Ising de osciladores en la literatura
  (Wang & Roychowdhury). **DERIVADO/MEDIDO.**

-----

## Los problemas abiertos (la invitación real)

1. **El problema de Bell, ahora bien planteado.** Bajo tiempo compacto, la
   evolución es un problema de valores en la frontera periódico — el mismo
   territorio matemático de los modelos retrocausales, la única familia que
   evade legítimamente los supuestos de Bell. Pregunta precisa: cuando los
   ajustes de medición entran como datos de frontera sobre el ciclo S¹, ¿las
   soluciones globalmente autoconsistentes exhiben correlaciones con S > 2 y
   marginales limpios? **Criterio de aprobación, dos números: S > 2 con
   Δ_marginales ≈ 0.** Nuestro instrumento ya distingue los tres regímenes.
1. **El teorema de Derrick en 3D.** La materia puntual como solitón escalar
   estático es inestable en tres dimensiones. La ruta de escape natural del
   marco son las soluciones localizadas periódicas en el tiempo (oscilones /
   análogos del breather) — favorecida estructuralmente porque aquí la materia
   se *define* por oscilación interna.
1. **Universalidad del ciclo.** Las frecuencias de de Broglie dependen de la
   masa; una sola fibra S¹ compartida necesita dar cuenta de todas las especies
   (armónicos / números de enrollamiento como candidatos; comparar con la
   compactificación por partícula de Dolce).
1. **Invariancia de Lorentz global y cotas de discretización temporal**, frente
   a los datos de dispersión de fotones.
1. **Entropía.** Sin sector estadístico todavía; retirada de la lista de
   resultados derivados hasta que exista.

-----

## Por qué México

El fundamento filosófico de este trabajo es mesoamericano y es estructural, no
decorativo: la intuición del tiempo cíclico que permitió reconocer lo que la
ecuación de de Broglie señalaba viene del pensamiento náhuatl, estudiado
durante décadas. Si algo surge de este programa, el registro debe decir que su
raíz intelectual es de México y su desarrollo se hizo con México. Buscamos
activamente:

- **Físicos y matemáticos** (teoría de campos, fundamentos cuánticos, sistemas
  dinámicos) para atacar los problemas 1–5.
- **Revisión crítica hostil.** Los colaboradores que buscamos primero son los
  que intenten romper esto.
- **Replicación independiente** de todos los resultados numéricos (cada script
  corre en una computadora personal, sin GPU).
- **Una revisión náhuatl.** La traducción al náhuatl del ensayo de origen del
  marco busca revisión por un intelectual nahua antes de su publicación; la
  dimensión filosófica merece el mismo rigor que la física.

Lo que ofrecemos: código bajo licencia MIT, derivaciones verificadas con sus
scripts de verificación, etiquetado epistémico honesto en todo el corpus,
coautoría plena en lo que se construya conjuntamente, y un programa que ya
demostró que mata sus propias conjeturas cuando los datos lo exigen.

-----

## Cómo verificar todo lo dicho aquí (≈ 15 minutos)

```
python verify_derivations.py   # masa del kink, ley de fuerza, dispersión
python teotl_qc.py             # Rabi, linealidad, conservación
python teotl_chsh.py           # referencia 2.8284 / campo local 2.0000
python maxcut_tft.py           # optimización de fase vs recocido simulado
```

Requisitos: Python 3 + numpy. Nada más.

-----

## Contacto y participación

- Abra un *issue* en este repositorio con preguntas, objeciones o resultados
  de replicación. Las objeciones técnicas son contribuciones de primera clase.
- Publicación completa del marco: planeada para el 17 de noviembre de 2026
  (Toxiuh Molpilia), bajo licencia MIT.
- Ensayos y contexto: Teotl Dispatch (Substack).

*Tloque Nahuaque — lo que está cerca y junto a todo.*