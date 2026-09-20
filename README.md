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

- Franja superior en berry oscuro con el teléfono y el Instagram del estudio
  (en móvil se reduce a los íconos).
- Header con el logo, el menú del perfil activo, el número de contacto y el
  acceso a la cuenta.
- Franja de promoción vigente, con enlace a la sección y botón para cerrarla.
- Banner principal de composición partida, con rotación cada 7 segundos.
- Servicios, horarios con disponibilidad y planes.
- Footer en tres columnas más la línea de derechos reservados.

Las demás pantallas ya están declaradas y son navegables: muestran un
marcador sobre la misma estructura.

## Las tres vistas

El botón **«Vista: …»**, abajo a la derecha, alterna entre los tres perfiles
para recorrer el sistema completo. Es una ayuda del prototipo, no parte del
producto.

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

## Decisiones de diseño

**Responde al diagnóstico.** La disponibilidad de los cinco horarios se ve
sin iniciar sesión y sin preguntar, que era la tarea que más estrés generaba
a la administración y la mayor dificultad para las estudiantes. El horario
de 8h00 aparece lleno con lista de espera, y la promoción vigente encabeza
la página para que nadie se entere tarde.

**Móvil primero.** El 83 % de las estudiantes gestiona sus clases desde el
celular: el diseño base es de una columna y crece hacia tablet y escritorio.

**Legibilidad.** Cuerpo de texto de 17 px, botones de 52 px de alto y áreas
de toque de 44 px como mínimo. Todas las combinaciones de texto sobre fondo
que aparecen en pantalla se verificaron con el ratio de contraste WCAG: el
valor más bajo en uso es 4,79 : 1 y la mayoría supera 7 : 1. El dusty rose
sólo se usa en bordes y elementos decorativos, porque como texto sobre
fondos claros no alcanza contraste suficiente. El verde salvia aparece
únicamente en el estado «disponible» de los cupos, en un tono algo más
oscuro cuando hace de texto sobre las tarjetas.

**Fotografías sin deformar.** En el banner la imagen se muestra completa
(`object-fit: contain`) sobre una ampliación desenfocada de sí misma; las
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
instructoras, la dirección, el correo, las redes sociales y la etiqueta
«Más elegida» del plan de tres clases por semana. La ocupación de los
horarios reproduce el diagnóstico: 27 reservas sobre 40 cupos, con el
horario de 8h00 lleno.

## Fotografías

El logo y las fotografías salen de los archivos originales del estudio; el
logo se recortó sobre fondo transparente. Las imágenes de servicios son
recortes 4:3 del mismo material, para que las cuatro tarjetas compartan
proporción.
