# Qué es la TFT — una lectura matemática

*Prefacio conceptual a las demostraciones. En lenguaje llano, pero preciso. El marco está **en desarrollo**; esto describe lo que es, no una afirmación de que esté terminado o sea único.*

## El objeto

Matemáticamente, la TFT es la teoría de **un solo campo con valores en el círculo**:

$$\theta:\ \mathbb{R}^3\times S^1 \longrightarrow S^1, \qquad \text{o equivalentemente un campo complejo } \psi = \rho\, e^{i\theta}.$$

Un campo cuyo *valor es una fase*. Ésa es toda la ontología. Casi todo lo que se demuestra en este repositorio no es maquinaria extra atornillada por encima — es la geometría y la topología que **cualquier** campo así arrastra automáticamente. Cuatro piezas de matemática estándar aparecen gratis en cuanto uno se compromete con ese único objeto.

### 1. El blanco es un círculo → enteros gratis
El círculo tiene grupo fundamental $\pi_1(S^1)=\mathbb{Z}$: un campo de fase puede enrollarse un número entero de veces, y ese entero no puede cambiar continuamente. Ese único hecho topológico *es* la cuantización de la carga, *es* el número bariónico — el «¿por qué la carga es un entero?» que el Modelo Estándar inserta a mano. Es topología, no dinámica. (Linaje Skyrme / solitón topológico.)
→ `verify_charge_quantization.py`

### 2. Una fase viene con una conexión → el electromagnetismo ya está ahí
El gradiente $\nabla\theta$ se comporta como un potencial de gauge $A$; su rotacional es un flujo magnético; el flujo se cuantiza en unidades de $2\pi\times(\text{enrollamiento})$. Ésta es la matemática de un fibrado $U(1)$ y su curvatura — la misma matemática que la cuantización del flujo en un superconductor. El electromagnetismo no se añade; es la geometría de una fase.
→ `verify_goldstone_1r2.py`, `verify_force_sign.py`

### 3. Noether te entrega dos corrientes, de carácter opuesto
Un campo con estas simetrías produce dos cantidades conservadas: la corriente de simetría interna $j^\mu=\rho^2\partial^\mu\theta$ (por $\theta\to\theta+\text{const}$), y el tensor de energía–momento $T^{\mu\nu}$ (por las traslaciones espacio-temporales).
- $j^\mu$ es **lineal y con signo** → una fuerza que puede atraer *o* repeler = Coulomb / electromagnetismo.
- $T^{\mu\nu}$ es **cuadrático y no negativo** → un acoplamiento *siempre* atractivo = gravedad.

Así, que las dos fuerzas de largo alcance tengan *personalidades opuestas* no es una elección — el teorema de Noether lo fuerza. Ésta es tal vez la «puerta trasera» más limpia del marco.
→ `verify_poisson_metric.py`, `verify_gravity_coupling.py`

### 4. El tiempo es fase; la gravedad es la geometría del sustrato
Leer $mc^2 = hf$ literalmente — el reloj *es* el giro de la fase, $d\tau = \hbar\,d\theta/E$ — es tomar en serio la fase de un estado cuántico como tiempo (la lectura de de Broglie). Y dejar que la densidad de energía alimente una métrica mediante una ecuación de Poisson, $\nabla^2\Phi = (\text{fuente positiva}) \to 1/r$, es la matemática de Sakharov–Jacobson de la «gravedad como elasticidad emergente de un sustrato»: se obtiene *la forma y el signo* de la gravedad sin elegir una ley de fuerza.
→ `verify_G_as_rate.py`, `tft_solar_system.py`

## El paso, en términos claros

El paso es un **cambio de variables más un único postulado**: *asumir que el objeto fundamental es una fase $U(1)$, y negarse a insertar nada a mano.* Cuando uno hace eso, las partes de la física que en secreto son «geometría de fase» — la cuantización entera, la estructura de gauge, las dos corrientes de Noether, la gravedad de métrica emergente, la fase-como-tiempo — se reensamblan sin ser postuladas por separado.

Incluso el resultado galáctico es «la misma ecuación, con una longitud desplazada»: el gap de masa de la fase $m=\sqrt{\Lambda}/\ell_0$ se ubica en la escala microscópica (apantallamiento ordinario) o en la escala de Hubble (→ una ley tipo MOND con $a_0 = cH_0/2\pi$). Una perilla, dos regímenes.

Por eso puede sentirse como *una puerta trasera hacia lo que ya estaba ahí* — porque en gran medida **lo es**: teorema de Noether, homotopía de $S^1$, fibrados $U(1)$, gravedad emergente de Sakharov — rederivados desde una sola entrada en lugar de ensamblarse a partir de postulados separados. Descubrir que muchas cosas son una misma cosa disfrazada es lo que significa **unificación**.

## Los bordes honestos

Al ser una recodificación, hereda ambos lados — declarados en claro para que la afirmación sea defendible:

- **Fortaleza.** La estructura viene gratis y con *menos* insumos: el marco carga aproximadamente una constante de calibración por escala absoluta, en vez de una tabla de postulados.
- **Límite 1 — una re-descripción no calcula lo que el original no podía.** Los números que quedan abiertos (la $G$ de Newton, $|\Lambda|$, las masas leptónicas, la asimetría bariónica $\eta$) son exactamente los que esta puerta no puede fijar — nunca estuvieron codificados en la topología de un solo círculo. Cada uno es un problema abierto en *todo* marco, no una laguna exclusiva de éste.
- **Límite 2 — no se demuestra unicidad.** «Este sustrato *produce* la estructura» no es «éste es el *único* sustrato que podría hacerlo». Otros puntos de partida dan la misma geometría $U(1)$.

## La prueba que importa

La prueba real no es la reorganización, por económica que sea — es si la puerta revela **una habitación que no se veía desde el frente**. Una recodificación que sólo reetiqueta física conocida es elegante pero aún no es física nueva; una que *fuerza una conexión que nadie construyó en los originales* sí lo es.

El candidato aquí es el **vínculo $a_0$–energía oscura**: como la misma fase ultraligera fija tanto la escala galáctica de aceleración como la densidad de energía oscura, las curvas de rotación galácticas y la ecuación de estado de la energía oscura quedan forzadas a ser el mismo campo — una predicción entre observables cruzados (coincidente con el $w_0$ de DESI, falsable en $w_a$) que ni MOND ni $\Lambda$CDM hacen. Véase `PREDICTIONS.md`.

---

**En una línea:** *Una cantidad notable de física es la geometría diferencial y la topología de un solo campo con valores en el círculo — y la TFT es la única puerta por la que hay que pasar para verlo.*
