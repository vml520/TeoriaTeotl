# Apéndice: demostraciones computacionales

*Código complementario de ⟨título del artículo⟩ (V. Luna, ⟨año⟩). Cada programa es autocontenido (Python 3 + NumPy), imprime su propio resultado, y corre en segundos.*

> **Qué son.** Demostraciones y comprobaciones de consistencia — **no pruebas.** Etiquetas: **[derivado]** se sigue del marco · **[consistencia]** reproduce física conocida, no una predicción única · **[entrada]** un valor que el marco no fija · **[abierto]** intentado, no resuelto. Nada aquí reclama unicidad ni prueba la teoría; para eso está el experimento. El marco está **en desarrollo** — esto es lo que hace hasta ahora. En conjunto los programas cubren **cinco órdenes de magnitud — partícula → planeta → galaxia → cosmos — desde un campo y un conjunto de ecuaciones.**

**Repositorio:** `https://github.com/vml520/TeoriaTeotl` · **Archivado (citar esto):** `https://doi.org/10.5281/zenodo.⟨ID⟩`

---

## A. El sustrato y sus partículas
| archivo | qué muestra | estado |
|---|---|---|
| `verify_conservative_1d.py`, `verify_force_law_sign.py` | la masa en reposo de una partícula = 8√Λ·E₀ (con precisión de 1 parte en 10⁹) y obedece F = Ma — masa y fuerza a partir del campo, no insertadas | **[derivado]** |
| `verify_breather_1d.py` | una partícula como onda estacionaria: localizada, periódica en el tiempo, masa enteramente en el movimiento | **[derivado]** |
| `verify_oscillon_3d.py`, `verify_qball_3d.py` | una fase aislada no puede sostener una partícula 3D (radia); una carga conservada (Q-ball) sí puede | **[derivado]** |

## B. Las dos fuerzas, a partir de una distinción
| archivo | qué muestra | estado |
|---|---|---|
| `verify_goldstone_1r2.py`, `verify_force_sign.py` | electromagnetismo: una fuerza de Coulomb 1/r², cargas iguales se repelen (a partir de la corriente de carga del campo) | **[derivado]** |
| `verify_poisson_metric.py` | gravedad: la densidad de energía alimenta un potencial 1/r (Poisson), así que toda masa atrae | **[derivado]** |
| `verify_gravity_coupling.py` | materia y antimateria portan carga opuesta pero energía idéntica → ambas caen igual | **[derivado — coincide con CERN ALPHA-g 2023]** |
| `verify_G_as_rate.py` | la G de Newton leída como (ritmo del tiempo)² / densidad | [reencuadre, no un valor] |

## C. El mundo clásico
| archivo | qué muestra | estado |
|---|---|---|
| `tft_solar_system.py`, `stage3_orbits.py`, `stage5_mercury.py` | un sistema solar a partir de una única calibración: 8 períodos planetarios a <0,1 %, la tercera ley de Kepler, los 42,9″/siglo de Mercurio | **[consistencia]** — las órbitas cerradas son por construcción; Mercurio es el valor relativista estándar, no único |

## D. Galaxias sin materia oscura
| archivo | qué muestra | estado |
|---|---|---|
| `verify_a0_g1.py`…`g3.py` | la escala galáctica de aceleración α₀ = cH₀/2π ≈ 1,1×10⁻¹⁰ m/s², fijada por la expansión cósmica — no ajustada | escala **[derivada]**; coeficiente exacto = el problema de la coincidencia |
| `verify_a0_g4.py`, `milkyway_rotation.py` | inercia modificada → límite MOND profundo; curva de la Vía Láctea al ~3 % (sólo bariones); **exponente Tully–Fisher exactamente 4** (obs 3,85±0,09) | mecanismo + pendiente-4 **[derivado]**; forma de interpolación [abierta] |
| `verify_a0_g5.py` | la ley TFT sigue la relación de aceleración de 175 galaxias SPARC dentro de su dispersión | **[consistencia con SPARC]** |

## E. Energía oscura — y la predicción central del artículo
| archivo | qué muestra | estado |
|---|---|---|
| `verify_dark_sectors.py` | materia oscura y energía oscura son un solo campo: la escala galáctica = la escala de energía oscura (tres números independientes dentro de ~1,8×) | **[derivado]** |
| `verify_dynamical_de.py` | la energía oscura es dinámica (quintaesencia thawing): w sube de −1 a **w₀ = −0,88** hoy — coincide con la firma de DESI 2024 y con w₀ | firma + w₀ **[derivados]**; wₐ verificable |
| `verify_a0_de_consistency.py` | **⭐ el campo fijado por la rotación galáctica *predice* el w₀ de la energía oscura (= −0,83, coincide con DESI), y pronostica wₐ ≈ −0,2 a −0,3** — un vínculo entre observables cruzados que ningún otro marco establece | **[predicción]** — w₀ confirmada; wₐ es una tensión de ~1,7σ, falsable por DESI DR2 / Euclid |

## F. Materia, campos y quiralidad — un solo objeto topológico
| archivo | qué muestra | estado |
|---|---|---|
| `verify_chiral_g1.py`, `verify_chiral_g2.py` | número bariónico, helicidad magnética y quiralidad son tres lecturas de una única cantidad topológica (enrollamiento + enlace) — de modo que su vínculo anómalo es automático, y los campos primordiales deben ser helicoidales | vínculo **[derivado]**; el *tamaño* de la asimetría materia–antimateria es una [entrada] |

## G. Sector cuántico — propiedades de partícula desde la dinámica de campo
| archivo | qué muestra | estado |
|---|---|---|
| `verify_charge_quantization.py` | la «carga» es el número de enrollamiento del campo — un entero exacto por topología; la masa es energía de campo; antipartícula = enrollamiento opuesto, masa idéntica. Las propiedades son configuraciones, no etiquetas intrínsecas | principio **[derivado]**; el *espectro* de partículas es [abierto] |
| `verify_koide_generations.py`, `verify_koide_sqrt2.py` | tres generaciones como tres fases a 120° una de otra = la **relación de Koide**, que predice la masa del tau desde el electrón y el muon con precisión de **0,006 %**; su coeficiente se reduce a una autodualidad de 45° del vector de masa | **[consistencia, no derivado]** — Koide es empírico; la TFT lo *expresa* |
| `verify_selfdual_attempt.py` | intento de derivar esa autodualidad: la condición queda clavada exactamente, y el principio obvio (equipartición) queda descartado | **[abierto]** — no derivado; un objetivo bien planteado |

---

**Reproducción.** Cada archivo es autocontenido (Python 3.8+, sólo NumPy) e imprime su resultado con `python3 <archivo>.py`. Un árbitro puede verificar cualquier afirmación individual en segundos.

**Lo que *no* se reclama.** Unicidad; las constantes absolutas (la G de Newton, la constante cosmológica, el coeficiente exacto de a₀, la asimetría bariónica, las masas leptónicas); ni que nada de esto pruebe la teoría. El patrón recurrente y honesto: **el marco deriva mecanismos y relaciones de escala sin parámetros libres, y carga una constante de calibración (o un número abierto) por cada escala absoluta — y cada uno de esos números abiertos es un problema que está abierto en *todos* los marcos, no una laguna exclusiva de éste.**
