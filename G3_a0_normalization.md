# G3 — Controlando la normalización de la energía de vacío

*Objetivo: ¿sale el coeficiente en a₀ = (coef)·cH₀ igual a 1/2π cuando los factores O(1) se hacen adecuadamente? Comprobación ejecutable: `verify_a0_g3.py`. Resultado: el 2π es limpio; el residuo es un O(1) cosmológico, no una constante de primeros principios.*

## El cálculo apropiado
La densidad de energía potencial sine-Gordon es tipo axion:
> u_V(θ) = (E₀Λ/ℓ₀³)(1 − cos θ) ≡ μ⁴(1 − cos θ).

Dos cantidades distintas provienen de ella:
- **Gap de masa** (curvatura en θ=0): ω₀ = c√Λ/ℓ₀. **Fijo**, independiente de dónde se ubique el campo. Es lo que entra en a₀ = c·(frecuencia Compton) = c·ω₀/2π. **El 2π es h/ℏ = un ciclo S¹ completo — limpio, y no la fuente de ninguna discrepancia.**
- **Densidad de energía oscura** = la *altura* del potencial en la posición actual del campo θ_i: ρ_DE = μ⁴(1 − cos θ_i). Depende de **θ_i** — una cantidad cosmológica (cuán lejos ha rodado el campo ultraligero).

Friedmann H₀² = 8πGρ_DE/(3c²) con G = ℓ₀c⁴/E₀. **Λ se cancela.** El resultado:

> **a₀ = (cH₀/2π) · √( 3 / (8π(1 − cos θ_i)) ).**

El paréntesis es exactamente **ω₀/H₀** — cuán cerca está la masa del campo de la masa de Hubble.

## Lo que dice (medido, `verify_a0_g3.py`)
| θ_i | ω₀/H₀ | a₀ | a₀/emp |
|---|---|---|---|
| π/2 (O(1) genérico) | 0,345 | cH₀/18 | 0,31 |
| **0,44 rad (~25°)** | **1,12** | **cH₀/5,6 ≈ 1,2×10⁻¹⁰** | **1,01** |
| π | 0,244 | cH₀/26 | 0,22 |

Los datos (a₀ = 1,20×10⁻¹⁰) corresponden a **θ_i ≈ 0,44 rad**, es decir **ω₀ ≈ H₀ — la masa del campo ≈ la masa de Hubble.** Ésa es precisamente la condición estándar de quintaesencia «thawing»: un escalar se vuelve dinámico cuando su masa cae a la tasa de Hubble actual. Por tanto el valor preferido por los datos es *físicamente el esperado*, no un ajuste arbitrario.

## Veredicto honesto
- **El 2π está DERIVADO** — geométrico (frecuencia Compton, h/ℏ, S¹). Nunca fue el problema.
- **a₀ ∝ cH₀ está DERIVADO** — mecanismo (campo = energía oscura), Λ se cancela, atado a la escala CC.
- **El coeficiente exacto NO está unívocamente fijado.** Es ω₀/H₀ = √(3/(8π(1−cosθ_i))), un **O(1) fijado por la posición cósmica del campo θ_i**. La quintaesencia *naturalmente* pone ω₀ ~ H₀ (masa ~ masa de Hubble, volviéndose dinámica ahora), lo cual da a₀ ~ cH₀/2π y coincide con los datos. Pero un θ_i *genérico* ~ O(1) da ~3× bajo. Así que el coeficiente es **natural y consistente con los datos, no forzado desde primeros principios.**

**Esto no libera del todo G3.** Atacar la normalización no convirtió el coeficiente en una constante pura; reveló que el factor residual es **una cantidad cosmológica real** (la posición / ecuación de estado del campo de energía oscura), que los datos fijan al valor natural «m ≈ H₀». Ésa *no* es una perilla libre que ajustamos — es ω₀/H₀, físicamente ~1 para quintaesencia — pero tampoco está derivada desde la nada.

## Dónde está el programa a₀ (G1–G3)
- **a₀ ∝ cH₀** — DERIVADO. No ad hoc (contra MOND). Viene por Λ, vía el campo siendo energía oscura. ✓ (La afirmación central de Vic.)
- **El 2π** — DERIVADO (S¹/Compton), *dado que* m = masa de Hubble.
- **m = masa de Hubble** — la condición natural de quintaesencia (m ~ H₀); el coeficiente exacto porta un O(1) atado a la posición del campo, que los datos fijan al valor thawing. **Natural, consistente, no unívocamente predicho.**
- **|Λ| ~ 10⁻¹²²** — el problema de la constante cosmológica, sin tocar.

**Frase única:** a₀ ~ cH₀ con el 2π desde S¹ es real y predicho; hacer que coincida con los datos al 10 % requiere que el campo ultraligero tenga masa ≈ la tasa de Hubble actual — la condición estándar «la energía oscura volviéndose dinámica ahora» — que es natural pero es una entrada cosmológica, no una constante derivada. **Derivar a₀ exactamente = derivar por qué la energía oscura es dinámica ahora = el problema de la coincidencia.** Ése es el suelo honesto.
