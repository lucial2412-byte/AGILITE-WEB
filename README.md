# Agilité Pilates · Prototipo web

Prototipo funcional en HTML, CSS y JavaScript. Se abre con doble clic en
`index.html`, sin instalar ni compilar nada.

```
index.html                      la aplicación (estructura, estilos y lógica)
assets/                         logo y fotografías
agilite-pilates-completo.html   la misma app en un solo archivo, para compartir
construir-archivo-unico.py      regenera ese archivo
README.md
```

## Para compartirlo con alguien

`agilite-pilates-completo.html` es la aplicación entera en **un archivo**, con
las imágenes incrustadas. Se puede enviar por correo o WhatsApp y se abre con
doble clic, sin necesidad de la carpeta `assets` ni de internet.

Úsalo siempre que vayas a compartir. `index.html` + `assets/` es la versión
de trabajo: si abres ese sin la carpeta al lado, las fotografías no cargan.

Después de cambiar `index.html`, regenera el archivo único:

```bash
python3 construir-archivo-unico.py
```

## Qué está construido

El **home público** completo, con la estructura general que comparten todas
las pantallas:

- Header con el logo, el menú del perfil activo y el acceso a la cuenta.
  **El teléfono y el Instagram viven sólo aquí**, una vez en todo el sitio:
  en móvil son dos íconos y en escritorio el teléfono se expande y muestra
  el número. Una prueba comprueba en los tres perfiles que cada uno aparece
  exactamente una vez y que está dentro del header. Al lado va el ícono de
  WhatsApp, que abre el chat del estudio con el mensaje ya escrito. Al lado va el ícono de
  WhatsApp, que abre el chat del estudio con el mensaje ya escrito.
- Banda informativa estática con la promoción vigente, sobre fotografía con
  degradado, con enlace a la sección y botón para cerrarla. No rota.
- Banner principal a todo el ancho, con rotación cada 7 segundos. Cada
  diapositiva lleva titular, una línea y **un solo llamado a la acción**
  —«Iniciar mi experiencia», «Más información», «Contáctanos»—; el
  dato de cupos libres salió de ahí porque el estudio lo quería enfocado
  en la acción, y la disponibilidad real sigue en la sección de horarios.
  El velo no cubre toda la fotografía sino sólo la esquina donde cae el
  texto, para que el resto de la sala se vea.
- Servicios en cuadrícula de cuatro tarjetas.
- Planes con la Promo Flash aplicada y sus condiciones.
- Horarios con dos pestañas: la disponibilidad de hoy y un cuadro de toda
  la semana (cinco franjas por cinco días) con el cupo de cada clase.
- Instructoras, una por jornada.
- Testimonios de estudiantes.
- Footer en tres columnas más la línea de derechos reservados.

### Entrar (construida)

`#/entrar` es la puerta a las dos vistas con sesión. El usuario y la
contraseña de demostración —`cliente` / `0000`, en `AG.data.acceso`— vienen
ya escritos en el formulario, y dos botones deciden con qué vista entrar:
estudiante o administración. Si las credenciales no coinciden lo dice sin
recargar. Una ruta de estudiante o de administración pedida sin sesión
lleva aquí, con el nombre de la pantalla que se quería abrir.

**No es autenticación y la pantalla lo declara.** El usuario y la clave
están escritos en el archivo y en el propio formulario; el panel de al
lado los muestra a propósito, para que la demostración se pueda recorrer
sin instrucciones. Cuando el sitio se publique, cada persona tendrá su
cuenta, la verificación tiene que hacerse en un servidor y las contraseñas
guardarse cifradas.

### Vista de estudiante (construida)

- **Reservar** · su plan del mes, el horario contratado, la tira de días con
  las fechas reales de la semana y los cinco horarios con cupos. Reservar,
  cancelar, cambiar de horario puntualmente y entrar a la lista de espera
  cambian los datos de verdad y se redibuja la pantalla.
- **Mi progreso** · clases del mes, medidor del plan, fichas de dato, las
  clases por semana, el **seguimiento de medidas** y las **fotos de
  progreso**. Las medidas las registra la estudiante y el cambio se muestra
  sin metas ni colores de acierto: el estudio dice «queremos que te sientas
  bien en el cuerpo que habitas», así que la pantalla informa, no califica.
  Las fotos son opcionales y privadas; en el prototipo no salen del
  navegador —se reducen con un canvas y se pierden al recargar—, así que
  antes de publicar hay que decidir dónde se guardan y con qué
  consentimiento.
- **Mi plan** · lo contratado, condiciones, historial de pagos y cambio de
  plan con el precio de la promoción aplicado.

Las reglas del estudio se hacen cumplir: cada estudiante tiene un horario
habitual —el que eligió al inscribirse, que aparece preseleccionado— pero
**puede reagendar cualquier clase** según la disponibilidad del día, se
cancela hasta 24 horas antes del inicio, y la cuota de clases del plan no
se puede exceder. El plazo se evalúa contra el reloj
real; `cancelacion.js` lo prueba con el reloj fijado en un miércoles a las
10h15, a las 5h00, un martes a las 23h30 y un sábado, porque si la suite
corre en fin de semana la rama de día laborable no se ejercitaría nunca.

### Vista de administración (construida)

- **Panel** · lo que hay que confirmar hoy: avisos accionables, ocupación
  de cada clase, listas de espera, solicitudes de cambio e interesadas sin
  responder. Avisar a una lista de espera la vacía y queda registrado.
- **Estudiantes** · el padrón de 27, con búsqueda por nombre y filtros por
  horario y estado de pago.
- **Horarios** · capacidad, instructora, inscritas y la ocupación de la
  semana de cada clase.
- **Comunicación** · un aviso a todas de una vez, plantillas para responder
  a las interesadas y el historial de lo enviado.
- **Reportes** · ocupación media por horario, mapa de cupos por día e
  ingresos por plan, todo calculado del padrón.

### Pantallas públicas (construidas)

- **Inscripción** · tres pasos: plan (con el precio de la promoción
  aplicado), horario del mes (los llenos quedan deshabilitados y ofrecen
  lista de espera) y datos, con resumen y confirmación. Al entrar a la
  cuenta pasa a la vista de estudiante.
- **Contacto** · formulario cuyo mensaje entra en la bandeja de
  administración, más las respuestas rápidas que enlazan a cupos, planes e
  inscripción.
- **Quiénes somos** · misión, cifras del estudio e instructoras.
- **Ubicación** · dirección, enlace al mapa y horarios de atención.
- **Términos de las promociones** · redactados a partir de los datos
  reales de la promoción vigente.
- **Política de privacidad** y **Trabaja con nosotros**.

Sólo queda un marcador: «Mi cuenta».

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
3. Cada pantalla es una función registrada en `AG.views` (16 construidas):

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

Las bandas alternan blanco, rosa vivo, rosa velado y rosa neblina para
que dos secciones contiguas nunca compartan fondo.

**La paleta se corrió hacia el rosa** a pedido del estudio, que pedía menos
vino y más el rosa de la marca. El límite lo pone el contraste, no el
gusto:

| Tinta | Antes | Ahora | Por qué ahí |
| --- | --- | --- | --- |
| berry oscuro (texto y componentes) | `#6E1F33` | `#8E2F4E` | sobre el rosa neblina del pie da 4,90 : 1, el mínimo para texto pequeño; un paso más de rosa ya no alcanza |
| berry (bandas grandes y botones) | `#A62B47` | `#B84068` | con blanco encima da 5,29 : 1 |

Sobre el rosa vivo de las bandas grandes el rosa neblina sólo alcanza para
texto grande (3,29 : 1), así que los rótulos pequeños de esas bandas pasaron
a blanco. El pie dejó de ser vino: va en rosa neblina con el texto en vino
tinta (10,17 : 1) y los rótulos en berry oscuro (4,90 : 1), porque el blanco
sobre ese rosa no alcanza (1,61 : 1).

## Gráficos

Cada gráfico lleva una sola serie de datos y una sola tinta.

«Mi progreso» plotea las clases por semana en una sola
tinta de la marca, validada con el script de la guía de visualización:
barras de 24 px como máximo, extremo superior redondeado y base cuadrada,
separación de 2 px, sin caja de leyenda —el título dice qué se mira—, con
los valores etiquetados de forma selectiva y una tabla accesible para el
resto. El medidor del plan usa el relleno berry sobre una pista de la misma
tinta, más clara.

«Reportes» añade barras horizontales con el valor en la punta y un mapa de
calor de cupos por día que usa una rampa secuencial de una sola tinta
—rosa velado, neblina, dusty, berry, berry oscuro—, monótona de claro a
oscuro y con cada paso verificado contra el texto que lleva encima (de
5,29 a 10,17 : 1). El mapa trae leyenda de intensidad y tabla accesible.

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
combinaciones que se pueden calcular del CSS, con el ratio WCAG, en las
dieciséis pantallas y en los tres perfiles; y los textos que van sobre
fotografía, midiendo el fondo real en píxeles.

La segunda medición (`fotocontraste.js`) se rehízo porque la anterior
mentía de tres maneras:

1. calculaba como si todo el texto fuera blanco, cuando varios elementos
   iban en rosa neblina, que tiene bastante menos luminancia;
2. medía la caja del elemento, que incluye esquinas sin letras —la esquina
   vacía de un titular de dos líneas—, así que penalizaba zonas donde no
   hay texto; ahora mide una caja por línea, con `Range`;
3. ocultaba el bloque de texto para fotografiar el fondo, y con él se iban
   los rellenos que protegen el texto, como la píldora del dato de cupos;
   ahora las letras se vuelven transparentes y los fondos se quedan.

Con la medición corregida, los diez textos sobre fotografía cumplen. El
peor caso es **3,47 : 1 en el titular** del banner (mínimo 3,0 por ser
texto grande) y **5,77 : 1 en el párrafo** (mínimo 4,5). El titular es el
que va más justo a propósito: el estudio pidió que el banner diera luz a
la página, así que el velo no cubre toda la fotografía sino sólo la
esquina donde cae el texto.

El dusty rose sólo se usa en bordes y elementos decorativos, porque como
texto sobre fondos claros no alcanza contraste suficiente. El verde salvia
aparece
únicamente en el estado «disponible» de los cupos, en un tono algo más
oscuro cuando hace de texto sobre las tarjetas.

**Cuadro semanal usable en el celular.** Cada celda lleva sólo la cifra de
cupos libres —o un guión si está llena—: el color y la leyenda de abajo ya
dicen qué significa, así que repetir «libres» en cada casilla era
redundante. El dato sigue completo para quien usa lector de pantalla,
porque el `aria-label` del botón lo dice con palabras. Al desplazarlo
horizontalmente la columna de horas queda fija, de modo que nunca se
pierde la referencia de
qué franja se está mirando.

**Fotografías.** Las tarjetas de servicios comparten proporción 4:3. El
banner reserva la altura de la diapositiva más alta, de modo que el bloque
no cambia de tamaño al rotar. La rotación se detiene con el cursor encima o
con el foco dentro, y se respeta la preferencia de movimiento reducido del
sistema.

**Dos recortes por fotografía del banner.** Un mismo archivo no sirve para
el monitor y para el celular: en horizontal sobra alto y en vertical sobra
ancho, y el recorte automático se come el motivo. Cada fotografía del
banner tiene entonces dos archivos y el navegador elige con `<picture>`:

| Archivo | Medida | Proporción | Se usa desde |
| --- | --- | --- | --- |
| `banner-*-h.jpg` | 2400 × 1000 px | 2,4:1 | 768 px de ancho en adelante |
| `banner-*-v.jpg` | 1200 × 2000 px | 0,6:1 | por debajo de 768 px |

Van en JPG sRGB progresivo, por debajo de 300 KB cada uno. El motivo se
encuadra dentro del 80 % central en la horizontal y del 83 % central en la
vertical, porque el navegador recorta los bordes según la pantalla. El
tercio inferior izquierdo se deja despejado: ahí caen el titular, los
botones y la parte más cargada del velo. Si una diapositiva no trae
recorte vertical (`imgV`), el navegador usa el horizontal en todos los
anchos.

**El velo cambia según la pantalla.** En el celular el bloque de texto
ocupa casi todo el alto del banner, así que el velo va cargado; desde
768 px el texto se concentra a la izquierda y el velo se aligera para que
la fotografía se vea. Cuando el recorte horizontal ya muestra el letrero
del estudio en la pared, la diapositiva marca `logoEnFoto:true` y el chip
del logo se oculta en pantallas anchas para no repetir la marca; en el
celular, donde ese letrero queda debajo del texto, el chip sigue visible.

## Textos legales

Los términos de las promociones y la política de privacidad son un
**borrador** redactado a partir de la información real del estudio, y cada
página lo declara en pantalla con un aviso visible. El estudio debe
revisarlos antes de publicarlos. Los datos que citan los términos
—el 30 %, las 48 horas y el plan mínimo que entra en la promoción— se leen
de `AG.data.promo`, así que se actualizan solos si cambia la promoción.

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
