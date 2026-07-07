# G1 — Primer corte: a₀ = cH₀/2π desde la masa del campo (Λ)

*Derivación estructural. Comprobación ejecutable: `verify_a0_g1.py`. Etiquetas de estado en línea.*

## El ancla: la TFT tiene dos tasas fundamentales
Tiempo = ciclado de fase. Las dos escalas de aceleración de la gravedad son la misma idea en los extremos opuestos de la escala:
- **UV:** G = ω_P²/ρ_P, ω_P = 1/t_P la tasa de ciclado de Planck. *(Resultado de `verify_G_as_rate.py`.)*
- **IR:** a₀ = cH₀/2π, es decir a₀/c = H₀/2π, una tasa de ciclado *cosmológica*.
El 2π es el período S¹ en ambas. Derivar a₀ es el espejo IR del resultado G.

## La cadena (cada eslabón etiquetado)

**(1) Gap de masa del campo — DERIVADO.** El acoplamiento sine-Gordon Λ le da al campo un gap de masa m = √Λ/ℓ₀ (el mismo √Λ que fija la masa del kink 8√Λ y la longitud de apantallamiento Yukawa ℓ₀/√Λ). *(Establecido en sesión anterior.)*

**(2) Identificación cosmológica — ASUMIDA (éste es el nudo, → G2; y es la «α desde Λ» de Vic).**
El campo es **ultraligero**: su longitud de onda Compton reducida iguala el radio de Hubble,
> ƛ = ℏ/(mc) = c/H₀  ⟺  **m = ℏH₀/c²** (la «masa de Hubble») ⟺ **√Λ/ℓ₀ ↔ ℏH₀/c²**.
Ésta es la única entrada física aún no derivada. Ata Λ (el acoplamiento) a la cosmología (H₀). Numéricamente m = 1,5×10⁻³³ eV — exactamente la escala de la constante cosmológica / ultraligera.

**(3) Frecuencia Compton — álgebra.** La frecuencia Compton del campo es
> f = mc²/h = ℏH₀/h = **H₀/2π**.
El 2π es literalmente **h/ℏ = un ciclo S¹ completo** (longitud de onda Compton completa vs reducida). *De aquí viene el 2π — la geometría S¹, no un ajuste.*

**(4) Aceleración de cruce — el resultado.** Una aceleración a tiene una frecuencia característica a/c. Cuando a/c cae por debajo de la frecuencia Compton propia del campo H₀/2π, la aceleración es más lenta de lo que el campo puede oscilar y la respuesta tipo-sin-masa (newtoniana) falla → régimen modificado. El cruce:
> **a₀ = c·f = cH₀/2π.**

## Confirmación numérica (`verify_a0_g1.py`)
- masa del campo = ℏH₀/c² = **1,49×10⁻³³ eV** (escala Hubble/Λ) ✓
- longitud de onda Compton reducida / radio de Hubble = **1,0000** ✓
- a₀ = cH₀/2π = **1,08×10⁻¹⁰ m/s²**; RAR empírica g† = 1,20×10⁻¹⁰ ± 0,24(sist) → razón **0,90** (dentro de los sistemáticos) ✓

## Bono — esto re-explica la Etapa 2 y unifica el cuadro gravitatorio
La longitud de apantallamiento del campo = longitud de onda Compton = **radio de Hubble**, que es 10⁵× una galaxia y 10¹³× el sistema solar. Así que el *mismo campo* es **efectivamente sin masa en todas las escalas subcosmológicas** → da la **gravedad 1/r que derivamos** (por la vía Goldstone-sin-masa / Poisson), y su diminuta masa a escala Hubble sólo muerde en la aceleración a₀.
> **La Etapa 2 falló porque usó Λ ~ O(1)** — apantallamiento en el ℓ₀ microscópico. La Λ *cosmológica* es ultraligera — apantallamiento en el radio de Hubble. Misma ecuación, Λ correcta: gravedad sin masa localmente **más** un cruce MOND en a₀. La memoria de Vic de que «α cayó desde Λ» queda estructuralmente vindicada: a₀ entra por el gap de masa m = √Λ/ℓ₀.

## Estado G1
- **DERIVADO (estructural):** la *forma* a₀ = cH₀/2π, con el **2π = S¹** (ciclo Compton completo), y el enlace a₀ ↔ Λ vía el gap de masa.
- **ASUMIDO (→ G2, la puerta):** la identificación ultraligera m = ℏH₀/c² (√Λ/ℓ₀ ↔ masa de Hubble). Todo cuelga de esta única entrada.
- **ASUMIDO (→ G3):** que a₀ = c·(frecuencia Compton) es el cruce físico (necesita el mecanismo de la ecuación de campo, no sólo la coincidencia de escala).

## Qué debe hacer G2
Justificar **m = ℏH₀/c²** desde la TFT — es decir, mostrar que la masa del campo de fase queda fijada a la escala de Hubble por el propio marco (candidato: autoconsistencia, donde la energía de vacío del campo fija tanto H₀ como su masa — el sector de la constante cosmológica). Si G2 sólo puede *imponer* m = masa de Hubble en vez de derivarla, entonces a₀ = cH₀/2π es una **relación de consistencia**, no una predicción de primeros principios — un resultado honesto y aún útil, pero etiquetado como tal.
