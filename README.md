# Agilité Pilates · Prototipo web

Prototipo funcional en HTML, CSS y JavaScript. Se abre con doble clic en
`index.html`, sin instalar ni compilar nada.

```
index.html      toda la aplicación (estructura, estilos y lógica)
assets/         logo y fotografías
README.md
```

## Qué está construido

El **home público** completo, con la estructura general que comparten todas
las pantallas:

- Header con el logo, el menú del perfil activo y el acceso a la cuenta.
  **El teléfono y el Instagram viven sólo aquí**, una vez en todo el sitio:
  en móvil son dos íconos y en escritorio el teléfono se expande y muestra
  el número. Una prueba comprueba en los tres perfiles que cada uno aparece
  exactamente una vez y que está dentro del header.
- Banda informativa estática con la promoción vigente, sobre fotografía con
  degradado, con enlace a la sección y botón para cerrarla. No rota.
- Banner principal a todo el ancho, con rotación cada 7 segundos.
- Servicios en cuadrícula de cuatro tarjetas.
- Banda de cifras del estudio.
- Horarios con dos pestañas: la disponibilidad de hoy y un cuadro de toda
  la semana (cinco franjas por cinco días) con el cupo de cada clase.
- Instructoras, una por jornada.
- Planes con la Promo Flash aplicada y sus condiciones.
- Testimonios de estudiantes.
- Footer en tres columnas más la línea de derechos reservados.

### Vista de estudiante (construida)

- **Reservar** · su plan del mes, el horario contratado, la tira de días con
  las fechas reales de la semana y los cinco horarios con cupos. Reservar,
  cancelar, cambiar de horario puntualmente y entrar a la lista de espera
  cambian los datos de verdad y se redibuja la pantalla.
- **Mi progreso** · clases del mes, medidor del plan, fichas de dato y las
  clases por semana.
- **Mi plan** · lo contratado, condiciones, historial de pagos y cambio de
  plan con el precio de la promoción aplicado.

Las reglas del estudio se hacen cumplir: el horario contratado es el mismo
todo el mes (un cambio de horario es puntual, sólo para ese día, y no altera
el del mes), se cancela hasta 4 horas antes del inicio, y la cuota de clases
del plan no se puede exceder.

Las pantallas de administración y las públicas ya están declaradas y son
navegables: muestran un marcador sobre la misma estructura.

## Las tres vistas

La **franja de demostración**, arriba de todo, alterna entre los tres
perfiles para recorrer el sistema completo. Es andamiaje del prototipo, no
parte del producto: en el sitio publicado no existe, porque cada persona
entra con su sesión y ve sólo su menú. Se elimina quitando el bloque
`.demobar` del marcado y `pintarSelectorVista()`.

| Perfil | Menú |
|---|---|
| Visitante (sin sesión) | Inicio · Horarios y planes · Contacto, más iniciar sesión e inscríbete |
| Estudiante (con sesión) | Reservar · Mi progreso · Mi plan, más el acceso a su cuenta |
| Administración (con sesión) | Panel · Estudiantes · Horarios · Comunicación · Reportes |

La estructura del header, la franja superior y el footer es la misma en las
tres; sólo cambian el menú y el bloque de cuenta.

## Cómo agregar una pantalla

1. Los datos simulados viven en `AG.data` (estudio, promoción, banner,
   servicios, horarios, planes y sesiones).
2. Las rutas de cada perfil están en `AG.perfiles`.
3. Cada pantalla es una función registrada en `AG.views`:

```js
AG.views['#/reservar'] = function (contenedor) {
  contenedor.innerHTML = '…';
};
```

Registrar la función reemplaza automáticamente el marcador. El enrutador
devuelve al inicio del perfil activo cualquier ruta que no le corresponda.

## Dirección visual

La composición sigue la maqueta de referencia entregada por el estudio:
secciones a todo el ancho, fotografía con degradado oscuro encima,
titulares en Jost mayúscula con una palabra en Cormorant itálica de acento,
bandas oscuras con cifras en serif, píldoras en mayúscula espaciada y
tarjetas de esquina muy redondeada. La paleta es la de la marca, no la de
la maqueta, y el código es propio: no se copió el de la plantilla.

Las bandas alternan blanco, berry oscuro, rosa velado y rosa neblina para
que dos secciones contiguas nunca compartan fondo.

## Gráficos

«Mi progreso» lleva una sola serie de datos (clases por semana) en una sola
tinta de la marca, validada con el script de la guía de visualización:
barras de 24 px como máximo, extremo superior redondeado y base cuadrada,
separación de 2 px, sin caja de leyenda —el título dice qué se mira—, con
los valores etiquetados de forma selectiva y una tabla accesible para el
resto. El medidor del plan usa el relleno berry sobre una pista de la misma
tinta, más clara.

## Decisiones de diseño

**Responde al diagnóstico.** La disponibilidad de los cinco horarios se ve
sin iniciar sesión y sin preguntar, que era la tarea que más estrés generaba
a la administración y la mayor dificultad para las estudiantes. El horario
de 8h00 aparece lleno con lista de espera, y la promoción vigente encabeza
la página para que nadie se entere tarde.

**Móvil primero.** El 83 % de las estudiantes gestiona sus clases desde el
celular: el diseño base es de una columna y crece hacia tablet y escritorio.

**Legibilidad.** Cuerpo de texto de 17 px, botones de 52 px de alto y áreas
de toque de 44 px como mínimo. El contraste se verificó de dos maneras: las
combinaciones que se pueden calcular del CSS, con el ratio WCAG; y los
textos que van sobre fotografía —banner, tarjetas de servicio y banda
informativa— midiendo el píxel más claro del fondo real en escritorio y
móvil, en las tres diapositivas. El peor caso en uso es 5,12 : 1 para texto
grande y 5,62 : 1 para texto normal. El dusty rose
sólo se usa en bordes y elementos decorativos, porque como texto sobre
fondos claros no alcanza contraste suficiente. El verde salvia aparece
únicamente en el estado «disponible» de los cupos, en un tono algo más
oscuro cuando hace de texto sobre las tarjetas.

**Cuadro semanal usable en el celular.** Al desplazarlo horizontalmente la
columna de horas queda fija, de modo que nunca se pierde la referencia de
qué franja se está mirando.

**Fotografías.** El banner es a todo el ancho, así que las verticales
originales se recortaron a 16:9 encuadrando el motivo (la fachada, por
ejemplo, quedó centrada en el interior iluminado y no en el letrero). Las
tarjetas de servicios comparten proporción 4:3. El banner reserva la altura
de la diapositiva más alta, de modo que el bloque no cambia de tamaño al
rotar. La rotación se detiene con el cursor encima o con el foco dentro, y
se respeta la preferencia de movimiento reducido del sistema.

## Datos reales y supuestos

Son reales, tomados de los materiales del estudio: los cuatro planes con
sus precios ($60, $85, $100 y $120), las condiciones de los planes, los
cinco horarios de lunes a viernes, la Promo Flash vigente (30 % de
descuento en los planes desde tres clases por semana, cupos limitados,
48 horas) y el teléfono de contacto.

La Promo Flash está conectada con las tarjetas de planes: `AG.data.promo`
lleva `descuento` y `aplicaDesdeClases`, y cada tarjeta que entra en la
promoción calcula su precio, muestra el anterior tachado y una etiqueta.
Al poner `promo.activa` en `false` desaparecen la franja, las etiquetas y
los descuentos, y vuelven los precios de lista.

Siguen siendo inventados, porque no había material: los nombres de las
instructoras, la dirección, el correo y la etiqueta «Más elegida» del plan
de tres clases por semana. Los **testimonios son de ejemplo** y cada
tarjeta se muestra marcada como tal; sirven de borrador del tono hasta que
el estudio entregue los reales. Vaciar `AG.data.testimonios` oculta la
sección completa. La ocupación de los
horarios reproduce el diagnóstico: 27 reservas sobre 40 cupos, con el
horario de 8h00 lleno.

## Fotografías

El logo y las fotografías salen de los archivos originales del estudio; el
logo se recortó sobre fondo transparente. Las imágenes de servicios son
recortes 4:3 del mismo material, para que las cuatro tarjetas compartan
proporción.
