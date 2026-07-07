# G2 — Primer corte: ¿es la masa del campo la masa de Hubble? (autoconsistencia)

*Objetivo: derivar la única suposición de G1 — m = ℏH₀/c² — a partir de que el campo sea la energía oscura. Comprobación ejecutable: `verify_a0_g2.py`. Resultado: el mecanismo funciona, el coeficiente exacto NO (una tensión real de ~3×, señalada y no ocultada).*

## El mecanismo
Si la energía de vacío del campo de fase **es** la energía oscura, ella impulsa la expansión. Cerrar el bucle:
- frecuencia del gap de masa del campo: ω₀ = c√Λ/ℓ₀
- densidad de energía de vacío del campo: ρ ~ E₀Λ/ℓ₀³ (la escala de energía potencial del campo)
- Friedmann (campo = energía oscura): H₀² = 8πGρ/(3c²)
- Relación TFT: G = ℓ₀c⁴/E₀

Resolver para ω₀/H₀. **Λ se cancela** — el bucle fija la *razón* del gap de masa a la tasa de Hubble independiente del valor absoluto (desconocido, ~10⁻¹²²) de Λ:

> **ω₀/H₀ = √(3/8π) = 0,3455** (confirmado numéricamente, independiente de Λ a 4 dígitos).

Así que el campo siendo la energía oscura **sí** ata su masa a la escala de Hubble — **m ≈ 0,35 × (masa de Hubble)**. Ésa es la sustancia: a₀ ~ cH₀ es una *consecuencia* del campo siendo energía oscura, no un parámetro ajustado. Y entra por Λ (el gap de masa m = √Λ/ℓ₀), exactamente como Vic recordaba.

## Lo que está DERIVADO
- **La relación m ~ ℏH₀/c**² (gap de masa atado a la tasa de Hubble) — desde autoconsistencia, **con Λ cancelándose**, así que *sin* necesidad de resolver el problema de la constante cosmológica.
- **La conexión CC:** requerir m = masa de Hubble da Λ = (ℓ₀/R_H)² = 1,5×10⁻¹²² — aterrizando en la escala observada de constante cosmológica.
- Por tanto a₀ ~ cH₀ (orden de magnitud + mecanismo + el enlace a₀↔Λ↔energía-oscura) está establecido.

## Lo que NO se resuelve — la tensión honesta
Las dos vías de derivación dan **coeficientes diferentes**:
| vía | a₀ | razón a lo empírico (g† = 1,20×10⁻¹⁰) |
|---|---|---|
| G1 geométrica (m = masa de Hubble exacta → freq. Compton = H₀/2π) | cH₀/2π = 1,08×10⁻¹⁰ | **0,90** ✓ |
| G2 dinámica (autoconsistencia → m = 0,345 × masa de Hubble) | cH₀/18,2 = 3,7×10⁻¹¹ | **0,31** ✗ |

Discrepan por **√(8π/3) = 2,89×**, y la vía dinámica queda ~3× por debajo del dato.

**Esto activa el falsador G0 #1**: el cruce sale ∝ cH₀ pero el *coeficiente* no es limpiamente 1/2π — el argumento geométrico (que coincide con los datos) y la autoconsistencia dinámica (que queda ~3× baja) discrepan. Uno de los dos porta factores O(1) sin controlar:
- la estimación de la energía de vacío ρ ~ E₀Λ/ℓ₀³ (amplitud del campo, normalización exacta del potencial) es cruda — plausiblemente equivocada por O(pocos);
- el 8π/3 de Friedmann y la identificación del cruce a₀ = c·(frec. Compton) cada uno porta factores O(1).

## Estado G2
- **DERIVADO:** el mecanismo — campo-como-energía-oscura da autoconsistentemente a₀ ~ cH₀ (Λ se cancela; atado a Λ y a la escala CC). a₀ **no es ad hoc**. Esto vindica el núcleo de la afirmación de Vic.
- **NO DERIVADO:** el coeficiente exacto / el 1/2π limpio. La vía geométrica coincide con los datos (0,90×); la dinámica queda 3× baja (0,31×). **Tensión de ~3× sin resolver.**
- **NO TOCADO:** el valor absoluto de Λ (~10⁻¹²²) — el problema de la constante cosmológica, una entrada.

## Qué debe hacer G3
Resolver los coeficientes O(1) y la discrepancia de 2,89× — controlar la normalización de la energía de vacío (amplitud del campo, potencial exacto) y el factor del cruce, y determinar si el coeficiente verdadero es 1/2π (geométrico, coincide con datos) o algo que la dinámica fuerza. Hasta entonces: **a₀ ∝ cH₀ está derivado; el 1/2π preciso no.**

*Frase honesta: el marco predice a₀ ~ cH₀ desde el campo de energía oscura (no un parámetro libre, y viene a través de Λ) — pero el factor exacto que lo hace coincidir con los datos al 10 % está, por ahora, sólo en el argumento geométrico, no en la dinámica; los dos están 3× separados y reconciliarlos es el paso abierto.*
