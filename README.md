Reto 7: Gestión de accesos a instalaciones
La empresa Egibide Access Control S.L. necesita registrar qué personas pueden entrar a
determinadas zonas y dejar constancia de cada intento de acceso. No solo quiere saber
quién entró, sino también quién intentó entrar sin permiso o con autorización caducada. La
aplicación debe permitir gestionar usuarios, zonas, permisos temporales o permanentes y
registros de acceso.
14
En la base de datos, Usuario y Zona no se relacionan de forma directa simple, porque la
relación real depende del permiso concedido. Un usuario puede tener permiso para varias
zonas y una zona puede estar autorizada para muchos usuarios. Por tanto, la relación entre
Usuario y Zona es many-to-many, pero se implementa mediante la tabla Permiso. Esa tabla
no solo conecta ambas entidades, sino que añade información clave: fecha de inicio, fecha
de fin, estado, etc. Después aparece RegistroAcceso, que representa cada evento de
acceso y tiene una relación de muchos a uno tanto con Usuario como con Zona. Es decir,
un usuario puede tener muchos registros de acceso y una zona también puede aparecer en
muchos registros.
Este es otro caso muy bueno para enseñar la diferencia entre permiso estructural y evento
operativo. Permiso dice lo que está autorizado. RegistroAcceso dice lo que ocurrió
realmente. Esa separación tiene mucho valor técnico y conceptual.
Panel con listado de usuarios y zonas, gestión de permisos en tablas claras y registro de
accesos en formato log cronológico con indicadores de acceso permitido o denegado.
Información principal
- Usuario
• DNI
• Nombre
• Apellidos
• Email
• Teléfono
• Tipo de usuario
- Zona
• Código de zona
• Nombre
• Descripción
• Nivel de acceso requerido
• Ubicación
- Permiso
• Código de permiso
• Usuario asociado
• Zona asociada
• Fecha de inicio
• Fecha de fin
• Estado
- Registro de acceso
• Código de acceso
• Fecha
• Hora
• Usuario asociado
• Zona asociada
• Resultado del acceso
• Observaciones
15
Funcionalidades mínimas
• Gestión de usuarios: alta, listado, detalle, actualización y baja
• Gestión de zonas: alta, listado, detalle, actualización y baja
• Gestión de permisos: alta, listado, detalle, actualización y baja
• Registro de accesos: alta, listado y detalle
• Consulta de accesos por usuario, fecha o zona
• Validación de acceso autorizado o denegado
• Panel de accesos recientes
• Histórico de permisos caducados
