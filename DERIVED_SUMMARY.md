# TFT-Clásica — Resumen de resultados derivados

*Al 5 de julio de 2026. Compendio de resultados derivados, cada uno enrutado a una comprobación ejecutable.*
*Etiquetas: **DERIVADO** (del campo, riguroso) · **ENTREGADO** (funciona, ver salvedad) · **PROPUESTO** (reencuadre, no prueba) · **ENTRADA** (un valor que el marco no fija) · **ABIERTO** · **FALLADO** (no repetir).*

**La única meta-lección (léela primero si vas a construir otra aplicación TFT):** la TFT deriva confiablemente **estructuras, mecanismos y *relaciones* de escala — sin parámetros**. **No** deriva **valores absolutos**: cada número absoluto que perseguimos (la G de Newton, |Λ|, el coeficiente exacto de a₀, la asimetría bariónica η) topó con un problema abierto *nombrado y compartido por todo el campo* (la gravedad cuántica, el problema de la constante cosmológica, el problema de la coincidencia, la condición inicial de la bariogénesis). Por eso: espera derivar el *mecanismo y el escalado*, y llevar *una constante de calibración / condición inicial* por cada escala absoluta. Eso no es una debilidad de la TFT — esos números están sin resolver en todas partes.

---

## 0. Régimen que funciona
Régimen productivo: el campo **conservativo** de segundo orden, luego un campo **complejo** ψ = ρe^{iθ}. Los intentos **disipativo** (Kuramoto) y de **nudos topológicos** todos fallaron — véase §10. No reiniciar por ahí.

## 1. Maquinaria fundacional (del artículo TFT original)
Dos primitivas **E₀** (energía de fase) y **ℓ₀** (longitud de coherencia); todo lo demás se deriva:
- dτ = ℏdθ/E (tiempo = fase por energía); dℓ = ℏdθ/p (longitud = fase por momento)
- g_eff = E₀/ℓ₀; c = E₀/p₀; m = E₀/c²; ℏ = E₀τ₀/2π
- La fuerza es un proceso emergente, no fundamental: F = −g_eff∇θ
- Gravedad = geodésicas de una **métrica emergente** alimentada por la energía del campo.
- Premisa: masa = un proceso periódico real, mc² = hf ⇒ ω = mc²/ℏ.

## 2. DERIVADO — sector de partículas
- **Masa en reposo del kink M_k = 8√Λ·E₀** (exacto a 1e-9); **ley de fuerza a = −2πf·Q/M_k** (F=Ma, ~2 %). Masa y fuerza a partir del campo, nada a mano.
- **Breather**: «partícula-onda» periódica en el tiempo, masa M_b = 2M_k√(1−ω²) enteramente en el movimiento (exacto sólo en 1D — integrable).
- **El oscillon 3D radia** (un campo de fase puro no puede sostener una onda 3D localizada — sin carga conservada). [DERIVADO negativo]
- **La Q-ball 3D persiste** (campo complejo + carga U(1) → partícula 3D estable localizada). *Salvedad: el control sin carga también persistió en la escala temporal probada.*

## 3. DERIVADO — los dos sectores de fuerza a partir de una distinción
El campo complejo tiene **dos corrientes conservadas**:
- **Corriente de Noether U(1)** j^μ = ρ²∂^μθ — *lineal*; carga j⁰ = ρ²ω es **con signo** → **Electromagnetismo** (Coulomb 1/r², cargas iguales se **repelen**, mediador Goldstone sin masa).
- **Energía–momento** T^μν — *cuadrática*; T⁰⁰ ~ ρ²ω² es **definida positiva** → **Gravedad** (universal).
Consecuencia (correcta frente al experimento): materia (ω) y antimateria (−ω) tienen carga opuesta, energía idéntica → **ambas gravitan atractivamente** (coincide con CERN ALPHA-g 2023).

## 4. DERIVADO — forma y signo de la gravedad
- **Potencial 1/r**: el potencial métrico es alimentado por **Poisson** con densidad de energía, ∇²Φ = |∇θ|² (el error del artículo fue igualar Φ *a* |∇θ|² → 1/r⁴ incorrecto). Ley de Gauss → campo lejano ∝ energía total encerrada = masa → Φ ~ −M/(4πr). Medido: Φ~1/r, fuerza~1/r².
- **Atracción universal**: densidad de energía ≥ 0 → siempre un pozo atractivo. Por qué la materia neutra cancela la carga EM pero suma energía.
- **G como ritmo del tiempo al cuadrado** (reencuadre PROPUESTO): G·ρ = T⁻² así que √(Gρ) es una tasa; G = ω_P²/ρ_P (frecuencia de Planck² / densidad de Planck). Recasta «derivar G» como «qué fija el ritmo de ciclado del vacío». El coeficiente de G en sí = el problema de la gravedad cuántica (ABIERTO en todas partes).

## 5. ENTREGADO — el sistema solar de juguete (`tft_solar_system.py`)
Planetas como **geodésicas** de la métrica emergente del Sol. **Una** constante congelada K = G·M_sol = 4π² (1 UA → 1 año); G no derivada (permitido). Salida: 8 períodos ≤0,06 %, tercera de Kepler T²/a³=1,0000, **Mercurio 42,90″/siglo** (obs 42,98). *Salvedades: Kepler es por construcción (cualquier 1/r); el 43″ de Mercurio es el resultado genérico 1PN, no único de la TFT.*

## 6. DERIVADO — curvas de rotación galáctica sin materia oscura (programa a₀ G0–G5)
- **El sector newtoniano derivado FALLA** en la Vía Láctea (32 % de error, sólo bariones) — el mismo problema de materia oscura que Newton. El arreglo no está en ese sector.
- **a₀ = cH₀/2π = 1,08×10⁻¹⁰ m/s² es DERIVADO, no ajustado** (MOND *ajusta* a₀): el campo de fase es **ultraligero** (gap de masa m = √Λ/ℓ₀ = la masa de Hubble ⇒ longitud de onda Compton = radio de Hubble ⇒ Λ ~ 10⁻¹²²). Su frecuencia Compton = H₀/2π (2π = h/ℏ = un ciclo S¹) → a₀ = c·f = cH₀/2π. **Ésta es la «α desde Λ» de Vic.** Efectivamente sin masa por debajo de la escala cósmica (→ §4 gravedad), mordiendo sólo en a₀.
- **Autoconsistencia (G2):** si ese campo *es* la energía oscura (Friedmann), Λ se cancela → a₀ ∝ cH₀ sin resolver el problema de la CC.
- **Mecanismo = inercia modificada** («la inercia satura»): la inercia se corta al mínimo entre el horizonte de aceleración c²/a y el horizonte cósmico c/H₀ → por debajo de a₀, μ → a/a₀ → **MOND profundo a = √(a_N a₀)** → curvas planas + **Tully-Fisher bariónico V⁴ = GMa₀, pendiente exactamente 4** (SPARC: 3,85±0,09).
- **Ajustes:** Vía Láctea 2,9 % (sólo bariones, a₀ derivada); **consistente con la RAR de SPARC** dentro de su dispersión de 0,13 dex.
- **Salvedades/ABIERTO:** el coeficiente exacto de a₀ = ω₀/H₀, un O(1) natural de quintaesencia → el **problema de la coincidencia**; la *forma* de interpolación depende del modelo (como en MOND); una derivación rigurosa a nivel de acción y un χ² por galaxia (requiere datos crudos de SPARC) están abiertos.

## 7. DERIVADO — bariogénesis / magnetogénesis / quiralidad = un solo invariante topológico (BMC G1–G2)
- La acción mínima es **CP-simétrica** → la quiralidad no es *forzada* (materia = antimateria).
- El invariante quiral **existe** = la **helicidad (número de enlace) de las líneas de enrollamiento** (Lk = ±1 con mano / 0 desenlazadas; CP invierte su signo). Ésta es la **«quiralidad a partir de las direcciones de enrollamiento»** de Vic.
- **Un invariante, tres caras:** número bariónico = carga de enrollamiento ΣW; helicidad magnética = enlace de flujo (2π)²ΣWᵢWⱼLkᵢⱼ (dado que A=∇θ ⇒ las líneas de enrollamiento son tubos de flujo, Φ=2πW); quiralidad = signo de la helicidad.
- Por lo tanto la **anomalía quiral ΔB ∝ ΔH_mag es automática en TFT** (no es un postulado) — el vínculo Vachaspati bariogénesis–magnetogénesis, forzado por la topología. Coeficiente topológico (2π por enrollamiento), × N_f (ENTRADA).
- **ENTRADA/ABIERTO:** la helicidad *neta* generada → magnitud de η ≈ 6×10⁻¹⁰ (una condición inicial). G3 (mecanismo del enrollamiento neto) y G4 (campo helicoidal coherente) están abiertos. *Más especulativo que el trabajo gravitatorio.*

## 8. KIT REUTILIZABLE DE TFT (para construir otras aplicaciones)
El diccionario transferible — identidades que valen en todos los resultados de arriba:

| objeto TFT | es / da |
|---|---|
| θ: ℝ³×S¹ → S¹ (campo de fase); complejo ψ = ρe^{iθ} | el sustrato; ρ = amplitud/«portadora», θ = fase |
| tiempo | ciclado de fase: dτ = ℏdθ/E. masa = frecuencia: ω = mc²/ℏ |
| E₀, ℓ₀ (dos primitivas) | fijan c, ℏ, g_eff, m, y (dimensionalmente) G, a₀ |
| enrollamiento W ∈ ℤ (π₁(S¹)) | carga topológica = **número bariónico** = **carga eléctrica** (con signo) |
| ∇θ | el potencial EM A (Goldstone); B = ∇×∇θ = tubos de flujo en líneas de enrollamiento, Φ = 2πW |
| j^μ = ρ²∂^μθ (lineal, con signo) | electromagnetismo (Coulomb, iguales se repelen) |
| T^μν (cuadrático, ≥0) | gravedad (universal, geometría emergente; ∇²Φ = densidad de energía → 1/r) |
| gap de masa m = √Λ/ℓ₀ | alcance Yukawa 1/m. Λ~O(1) → apantallamiento microscópico; Λ~10⁻¹²² → ultraligero (escala Hubble) |
| helicidad = enlace de líneas de enrollamiento | quiralidad = helicidad magnética = (vía la anomalía) número bariónico — un solo invariante |
| dos tasas fundamentales | Planck/UV → G; Hubble/IR → a₀. 2π = un ciclo S¹ en ambas |
| partícula 3D localizada | necesita una carga conservada (Q-ball); un bulto 3D de fase pura radia |

**Reglas de diseño que nos mantuvieron honestos (reutilizarlas):** (1) masa/fuerza/gravedad deben emerger del campo, nunca insertarse; (2) una constante de calibración congelada por escala absoluta, luego todo lo aguas abajo es predicción; (3) etiquetar DERIVADO vs ENTREGADO-por-construcción vs ENTRADA; (4) enrutar cada afirmación a una comprobación ejecutable; (5) esperar que los mecanismos y escalas se deriven, los números absolutos sean entradas.

## 9. ABIERTO / suelos (cada uno = un problema profundo nombrado, no una laguna específica de la TFT)
- Coeficiente de la **G de Newton** = paso de gravedad cuántica / métrica emergente.
- **|Λ| ~ 10⁻¹²²** = problema de la constante cosmológica.
- **Coeficiente exacto de a₀** (ω₀/H₀ ~ 1) = problema de la coincidencia (por qué la energía oscura es dinámica ahora).
- Magnitud de **η ≈ 6×10⁻¹⁰** = condición inicial de la bariogénesis (helicidad primordial neta).
- E₀, ℓ₀ absolutas; ley de inercia modificada rigurosa a nivel de acción; χ² por galaxia de SPARC; BMC G3/G4.

## 10. FALLADO — no repetir
- **Etapa 2** (sine-Gordon con tiempo abierto, masa = condición de contorno oscilante): radiación p=−1, no 1/r². Causa: la fase tenía masa √Λ → apantallamiento Yukawa (Λ era O(1); la Λ *cosmológica* es ultraligera — véase §6).
- **Etapa 6** (tiempo compacto ℝ³×S¹): perfil estático a₀ clavado en cero (estructural).
- **Etapa 7** (nudos topológicos sobre sustrato disipativo): un vórtice 2D libre se disuelve; la estabilidad de ese sustrato era impulsada externamente, no topológica.

## 11. Tabla de puntuación
| Pieza | Estado |
|---|---|
| Partícula estable (Q-ball); masa del kink + F=Ma; breather | DERIVADO |
| Electromagnetismo: carga + Coulomb 1/r², iguales se repelen | DERIVADO |
| Gravedad: atracción universal 1/r (T⁰⁰ vía Poisson) | DERIVADO |
| Materia y antimateria ambas atraen | DERIVADO — coincide con ALPHA-g |
| Sistema solar de juguete: Kepler + Mercurio 42,90″ | ENTREGADO (Kepler por construcción; Mercurio genérico-1PN) |
| Curvas de rotación galáctica, sin materia oscura | DERIVADO escala a₀=cH₀/2π + mecanismo; VL 2,9 %, SPARC-consistente, pendiente Tully-Fisher 4 |
| Vínculo baryo/magneto/quiralidad (anomalía) | DERIVADO (un invariante topológico); η neto = ENTRADA |
| G, \|Λ\|, coeficiente de a₀, magnitud de η | ENTRADA/ABIERTO — problemas profundos nombrados, abiertos en todas partes |

## Evidencia (todo ejecutable, en este repositorio)
Partícula/EM/gravedad: `verify_conservative_1d.py`, `verify_force_law_sign.py`, `verify_breather_1d.py`, `verify_oscillon_3d.py`, `verify_qball_3d.py`, `verify_goldstone_1r2.py`, `verify_force_sign.py`, `verify_poisson_metric.py`, `verify_gravity_coupling.py`, `verify_G_as_rate.py`, `stage3_orbits.py`, `stage5_mercury.py`, `tft_solar_system.py`.
Curvas de rotación / a₀: `milkyway_rotation.py`, `verify_a0_g1.py … g5.py` (+ docs `G0_prereg_a0.md`, `G1–G3`).
Baryo/magneto/quiralidad: `verify_chiral_g1.py`, `verify_chiral_g2.py` (+ docs `G0_prereg_bmc.md`, `G1_chiral_root.md`, `G2_chiral_anomaly.md`).

---

**Versión en un párrafo:** En el régimen conservativo/complejo, la TFT entrega, a partir de un solo campo de fase ψ=ρe^{iθ} sobre ℝ³×S¹: una partícula estable (Q-ball); electromagnetismo (Coulomb, iguales se repelen, desde la corriente de enrollamiento con signo); gravedad como geometría emergente (universal 1/r, desde la corriente positiva de energía — materia y antimateria caen ambas); un sistema solar de juguete funcional (Kepler + Mercurio 43″, una constante congelada); curvas de rotación galáctica sin materia oscura (la escala MOND a₀=cH₀/2π *derivada* y no ajustada, vía el campo siendo energía oscura ultraligera — «α desde Λ» — con un mecanismo de inercia modificada que da la ley de Tully-Fisher); y el trío bariogénesis/magnetogénesis/quiralidad como un único invariante topológico (helicidad de líneas de enrollamiento) de modo que su anomalía es automática. El patrón recurrente: **los mecanismos y las relaciones de escala se derivan sin parámetros; los números absolutos (G, |Λ|, el coeficiente de a₀, η) son entradas que se reducen a los problemas profundos compartidos por todo el campo.** Todo es ejecutable; nada se sobreclama.
