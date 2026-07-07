# Teoría del Campo Teotl — Demostraciones computacionales

Código complementario de *⟨título del artículo⟩* (V. Luna, ⟨año⟩). Cada programa es una comprobación pequeña
y autocontenida que cualquiera puede ejecutar en pocos segundos.

> **Qué son.** Demostraciones y comprobaciones de consistencia — **no pruebas.** Muestran que los
> mecanismos del marco producen el comportamiento indicado, y que reproducen la física conocida donde
> corresponde. Cada resultado abajo lleva una etiqueta que dice qué establece. Nada aquí reclama
> unicidad ni prueba la teoría; para eso está el experimento. El marco está **en desarrollo**; esto es
> lo que hace hasta ahora.

Todo se apoya en cuatro escalas (**E₀, ℓ₀, τ₀, α₀**) y tres ecuaciones
(**mc² = hf**, *el tiempo = el giro de la fase*, *la fuerza = la pendiente de la fase*) — véase el artículo.
Estos programas ejercitan esas pocas piezas a lo largo de cinco órdenes de magnitud en escala:
**partícula → planeta → galaxia → cosmos.**

**¿Recién llegado?** Lee primero [`WHAT_TFT_IS.md`](WHAT_TFT_IS.md) — una lectura matemática breve de lo
que *es* el marco (un campo de fase con valores en un círculo, y por qué buena parte de la física
estándar resulta ser su geometría y topología).

## Ejecución

```bash
pip install numpy
python3 verify_conservative_1d.py      # o cualquier archivo abajo — cada uno imprime su resultado
```

Requisitos: Python 3.8+ y NumPy. Sin otras dependencias. Cada archivo es autocontenido.

## Las demostraciones, por escala

Etiquetas: **[derivado]** se sigue del marco · **[consistencia]** reproduce un resultado conocido,
no una predicción única · **[entrada]** un valor que el marco aún no fija.

### A. El sustrato y sus partículas
| archivo | qué muestra | estado |
|---|---|---|
| `verify_conservative_1d.py`, `verify_force_law_sign.py` | la masa en reposo de una partícula = 8√Λ·E₀ (con precisión de 1e-9); obedece F = Ma | **[derivado]** |
| `verify_breather_1d.py` | una partícula como onda estacionaria — la masa está enteramente en el movimiento | **[derivado]** (exacto en 1D) |
| `verify_oscillon_3d.py`, `verify_qball_3d.py` | una fase aislada no puede sostener una partícula 3D; una carga conservada (Q-ball) sí | **[derivado]** (aislamiento carga-vs-alternativa no completo) |

### B. Las dos fuerzas, a partir de una distinción
| archivo | qué muestra | estado |
|---|---|---|
| `verify_goldstone_1r2.py`, `verify_force_sign.py` | electromagnetismo: una fuerza de Coulomb 1/r², cargas iguales se repelen | **[derivado]** |
| `verify_poisson_metric.py`, `verify_gravity_coupling.py` | gravedad a partir de la energía: atracción universal 1/r; la materia y la antimateria caen igual (cf. CERN ALPHA-g 2023) | **[derivado]**, coincide con el experimento |
| `verify_G_as_rate.py` | la G de Newton leída como (ritmo del tiempo)² / densidad | reencuadre, no un valor |

### C. El mundo clásico
| archivo | qué muestra | estado |
|---|---|---|
| `tft_solar_system.py`, `stage3_orbits.py`, `stage5_mercury.py` | un sistema solar a partir de una única calibración: 8 períodos a <0,1 %, la tercera ley de Kepler, Mercurio 42,9″/siglo | **[consistencia]** (órbitas cerradas por construcción; Mercurio es el valor GR estándar, no único) |

### D. La escala cósmica — galaxias sin materia oscura
| archivo | qué muestra | estado |
|---|---|---|
| `verify_a0_g1.py` … `g5.py` | la escala galáctica de aceleración α₀ = cH₀/2π — fijada por la expansión del universo, no ajustada | escala **[derivada]**; coeficiente exacto = el problema de la coincidencia («¿por qué ahora?») |
| `milkyway_rotation.py` | curva de rotación de la Vía Láctea al ~3 %, sólo bariones; sigue la relación de aceleración de 175 galaxias | **[ajusta]** (forma de transición dependiente del modelo, como en MOND) |
| `verify_a0_g4.py` | el exponente masa-rotación (Tully–Fisher) = exactamente 4 (observado 3,85 ± 0,09) | **[derivado]**, sin parámetros libres |

### E. Materia, campos y quiralidad — un solo objeto topológico
| archivo | qué muestra | estado |
|---|---|---|
| `verify_chiral_g1.py`, `verify_chiral_g2.py` | número bariónico, magnetismo y quiralidad son tres lecturas de una única cantidad topológica (enrollamiento + enlace); su vínculo anómalo es automático | **[vínculo derivado]**; el *tamaño* del desbalance materia-antimateria es una condición inicial |

## Un compendio más amplio

`DERIVED_SUMMARY.md` — un resumen escala por escala de lo que está derivado, lo que se reproduce por
construcción y lo que queda como entrada abierta (con cada número abierto nombrado: G, la constante
cosmológica, el problema de la coincidencia, la asimetría bariónica).

## El único patrón honesto

En todos los resultados: el marco deriva **mecanismos y relaciones de escala** sin parámetros libres,
y carga **una constante de calibración por cada escala absoluta**. Los números absolutos restantes
(G, |Λ|, el coeficiente exacto de α₀, la asimetría bariónica) se reducen cada uno a un problema
abierto en *cualquier* marco — no una laguna exclusiva de éste.

## Cómo citar

Si usas este código, por favor cita la versión archivada:
`https://doi.org/10.5281/zenodo.⟨ID⟩`

## Licencia

⟨elegir una — p. ej. MIT para el código, CC-BY para el texto⟩
