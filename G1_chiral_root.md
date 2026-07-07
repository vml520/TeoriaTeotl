# G1 — La raíz quiral: ¿tiene la TFT una estructura quiral?

*Comprobación ejecutable: `verify_chiral_g1.py`. Resultado: el invariante quiral EXISTE (= helicidad de líneas de enrollamiento, las «direcciones de enrollamiento» de Vic), pero la acción mínima es CP-simétrica, así que la quiralidad neta no es forzada.*

## A. La acción mínima es CP-simétrica
Densidad de energía e = ½(∇θ)² + Λ(1−cos θ). Bajo C: θ → −θ. Tanto (∇θ)² como cos θ son invariantes → **e es CP-par** (verificado exactamente: max|e − e_flip| = 0). Así que la TFT sine-Gordon mínima produce **enrollamientos + y − iguales — materia = antimateria, cero mano neta.** La quiralidad NO es automática.

## B. El invariante quiral existe — helicidad de líneas de enrollamiento
El número de enlace (helicidad) de dos líneas de enrollamiento, integral de Gauss Lk = (1/4π)∮∮(r₁−r₂)·(dl₁×dl₂)/|r₁−r₂|³:
| configuración | Lk |
|---|---|
| enlazado, mano derecha | −1 |
| desenlazado | 0 |
| espejo (mano izquierda) | +1 |

Un invariante topológico que **distingue mano** (CP invierte su signo), no nulo **sólo cuando los enrollamientos se enlazan/torsionan**. **Ésta es la «quiralidad a partir de las direcciones de enrollamiento»** — quiralidad = helicidad del campo de enrollamiento, la correlación de las *direcciones* de enrollamiento de líneas de defecto enlazadas. (Memoria de Vic confirmada.)

## Por qué esto desbloquea el trío — un invariante, tres caras
La helicidad de líneas de enrollamiento es simultáneamente:
- **carga** de enrollamiento alrededor de la línea = **número bariónico** (bariogénesis),
- **enlace de flujo** = **helicidad magnética** (magnetogénesis),
- **signo del enlace** = **quiralidad**.

Así que la anomalía quiral (número bariónico ↔ helicidad magnética) no es un postulado extra — en la TFT es la afirmación de que son la *misma* cantidad topológica. Eso es G2.

## Veredicto
- **Estructura quiral PRESENTE** — el trío tiene un hogar topológico genuino; el programa no está muerto en la raíz.
- **NO forzada** — la acción mínima es CP-par, así que una quiralidad *neta* (el exceso real de materia / la mano preferida) es una **condición inicial** (helicidad primordial neta) o requiere una **entrada violadora de CP** (un vacío de enrollamiento / ángulo θ, un término añadido).
- **Consecuencia, señalada de antemano:** el *vínculo* (G2) es derivable; la *asimetría neta* (signo y magnitud de η) topará con una CI / desconocido profundo, como el coeficiente de a₀ y |Λ|. Mecanismo sí; número absoluto, casi seguro que no.
