USE atc;

CREATE TABLE IF NOT EXISTS clientes (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS impagos (
    id INT NOT NULL AUTO_INCREMENT,
    client_id INT NOT NULL,
    fecha_impago DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (client_id) REFERENCES clientes(id)
);

CREATE TABLE IF NOT EXISTS emails (
    id INT NOT NULL AUTO_INCREMENT,
    fecha_envio DATETIME NOT NULL,
    client_id INT NOT NULL,
    email VARCHAR(4000) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (client_id) REFERENCES clientes(id)
);


-- INSERTS en la tabla 'clientes'
INSERT INTO clientes (nombre, email)
VALUES 
('Juan', 'juan@test.com'),
('Pedro', 'pedro@test.com'),
('Maria', 'maria@test.com'),
('Jose', 'jose@test.com'),
('Pepe', 'pepe@test.com'),
('Pablo', 'pablo@test.com'),
('Hugo', 'hugo@test.com'),
('Arnau', 'arnau@test.com'),
('Berta', 'berta@test.com'),
('Juana', 'juana@test.com'),
('Clara', 'clara@test.com'),
('Sergio', 'sergio@test.com'),
('Laura', 'laura@test.com'),
('Adriana', 'adriana@test.com'),
('Rafael', 'rafael@test.com'),
('Miguel', 'miguel@test.com'),
('Lucia', 'lucia@test.com'),
('Carlos', 'carlos@test.com'),
('Elena', 'elena@test.com'),
('Fernando', 'fernando@test.com'),
('Isabel', 'isabel@test.com'),
('Javier', 'javier@test.com'),
('Natalia', 'natalia@test.com'),
('Diego', 'diego@test.com'),
('Andrea', 'andrea@test.com'),
('Manuel', 'manuel@test.com'),
('Sofia', 'sofia@test.com'),
('Luis', 'luis@test.com'),
('Marta', 'marta@test.com'),
('Alberto', 'alberto@test.com'),
('Cristina', 'cristina@test.com'),
('David', 'david@test.com'),
('Patricia', 'patricia@test.com'),
('Alejandro', 'alejandro@test.com'),
('Sandra', 'sandra@test.com'),
('Enrique', 'enrique@test.com'),
('Monica', 'monica@test.com'),
('Pilar', 'pilar@test.com'),
('Antonio', 'antonio@test.com'),
('Beatriz', 'beatriz@test.com'),
('Francisco', 'francisco@test.com'),
('Veronica', 'veronica@test.com'),
('Raul', 'raul@test.com'),
('Yolanda', 'yolanda@test.com'),
('Gonzalo', 'gonzalo@test.com'),
('Leticia', 'leticia@test.com'),
('Cliente47', 'cliente47@test.com'),
('Cliente48', 'cliente48@test.com'),
('Cliente49', 'cliente49@test.com'),
('Cliente50', 'cliente50@test.com');

-- INSERTS en la tabla 'impagos'
INSERT INTO impagos (client_id, fecha_impago)
VALUES 
(1, '2021-01-01'),
(1, '2021-02-01'),
(8, '2021-01-01'),
(8, '2021-02-01'),
(8, '2021-03-01'),
(2, '2023-07-12'),
(15, '2023-07-05'),
(16, '2023-08-15'),
(29, '2023-10-30'),
(30, '2023-11-05'),
(41, '2023-02-08'),
(50, '2023-11-05');

-- INSERTS en la tabla 'emails'
INSERT INTO emails (fecha_envio, client_id, email)
VALUES
('2022-06-12 06:23:15', 1, 'Hola
Soy cliente pero no puedo acceder a mi factura online y tampoco me puedo registrar como cliente porque siempre me sale una ventana que me dice "error del servidor"
¿Me pueden decir si hay alguna forma de consultar mis facturas?
Podrían ponerlo un poco más fácil...
Atentamente
'),
('2022-08-12 19:15:39', 2, 'Hola, buenos días. Necesito que alguien me ayude para poder ver mi factura. No me deja crear correo. Gracias. Cuando puedan, ayúdenme.
'),
('2022-05-11 06:26:11', 3, '¿Cada cuánto facturas el gas? Llevo con vosotros desde el 10 de febrero y no me ha llegado ninguna factura.
Enviado desde
Outlook para Android
'),
('2022-04-15 19:13:26', 4, 'Buenos días,
No consigo ver la siguiente factura. Por favor enviarlo adjunto, gracias
Factura
Fecha
Cups
Importe
Ver
F-23-XXXXXXX
21/03/2023
ES00000054053403
490,90 €
'),
('2022-04-07 19:25:24', 5, '
Hola buenas tardes,
Seguimos desde que realizaron cambios en su web,
sin poder conectarnos y por tanto sin obtener nuestras facturas ni
tampoco adjuntar las lecturas mensuales.

Hemos solicitado en repetidas ocasiones y por diferentes medios que solventen el problema y todavía no tenemos
acceso y no hemos recibido ninguna contestación al respecto.

De nuevo nos vemos obligados a enviarles nuestras lecturas de GAS y LUZ por correo electrónico y solicitamos de nuevo
las dos facturas (en pdf) que ya han sido pagadas por nuestra entidad bancaria y que no tenemos.

FACTURAS : GAS por importe de 11,82 € y LUZ por importe de 153,49 €.

Así mismo adjuntamos nuestras lecturas tanto de gas como de luz, para la confección de nuestra factura de marzo.

Saludos

Admin
'),
('2022-02-18 19:29:31', 6, '
¿Por qué motivo no puedo visualizar mi contrato después de firmar? Soy el firmante Antonio Mel Lema, con DNI 12345678Z. ¿Me lo pueden enviar por correo electrónico? Gracias
'),
('2022-05-12 20:01:26', 7, 'Me ha entrado la factura, o sea, me ha entrado la factura, no, me ha llegado el cargo al banco de la luz y sin embargo no tengo las facturas. A ver si me las pueden mandar por correo, por favor. Vale, gracias a Dios.
'),
('2022-05-08 08:54:34', 8,
        'Hola, buenos días. Mira que me habéis cobrado las facturas de la luz y el gas, pero no me habéis mandado la factura. ¿Vale? Gracias.'),
('2022-05-23 19:11:41', 9, '

Buenos días, nos ponemos en contacto con ustedes para solicitar documentación necesaria para la central:

TITULAR : XXXX PRUEBA
NIF B123456789

REF CONTRATO :XXXXXXXX

Contrato de electricidad vigente, Facturas de energía de los últimos 12 meses, Curvas de consumo del último año
Quedamos a la espera, ¡saludos!
'),
('2022-08-08 20:42:46', 2, '
Buenos días, quería saber si tengo con vosotros contratado el gas.
Gracias 
'),
('2022-01-25 19:57:15', 2, '
No he recibido el contrato 
'),
('2022-08-12 08:52:39', 1, '
Buenos días
He borrado sin querer mis contratos de luz y gas...
¿Podrían volver a mandármelos?
Luis XXX
454135456P

Muchas gracias y perdonen las molestias

Enviado desde mi iPhone
'),
('2022-11-09 20:40:38', 3, '
Hola buenas tardes, necesito que me envíen el contrato  de electricidad y gas. Nunca me lo han enviado 
'),
('2022-04-18 07:11:29', 4, '
Hola, yo llamaba porque quiero darme de baja del servicio de gas. Entonces parece que he llegado un poco tarde, por eso es las seis y media. El teléfono mío es 6666666666. Si puede mañana me llamo. Gracias.

'),
('2022-01-05 06:49:43', 5, '
Señores:
Adjunto la documentación requerida para el cambio de titularidad del contrato de suministro de electricidad (nº ZXXXXXX), actualmente a nombre del Sr. Salvador, relativo al local sito en Barcelona, c/. Prueba.

Atentamente,
'),
('2022-03-15 08:38:44', 6, '
Buenas tardes,
Necesito que me enviéis las facturas de gas y luz del mes de abril, por favor. Me tengo que ir del piso en el que vivo y el propietario las necesita para hacer cambio de titularidad.
Gracias 
'),
('2022-08-18 20:57:43', 7, 'Buenos días. Solicitamos nos envíen la factura XXXXXX de importe XX€ emitida a nuestra empresa Panaderías XXXXX S.L.'),
('2022-08-13 06:56:49', 8,
        'Buenos días, necesitamos que nos envíen la factura del mes de septiembre del siguiente cliente: XXXXXX'),
('2022-09-15 06:19:16', 9,
        'Buenos días. Soy Pepito Grillo. Llevo dos días intentando conseguir mis facturas por mail o por teléfono y no me es posible. Por favor, ¿se pueden poner en contacto conmigo? Gracias'),
('2022-08-08 19:22:27', 8, 'Buenos días. Quisiera que me enviaran también las siguientes facturas:

- Recibida 18/07/2023, importe XX€
- Recibida 18/07/2023, importe YY€
- Recibida 18/08/2023, importe ZZ€'),
('2022-07-13 18:21:44', 1, 'Necesito hablar con un operador que es urgente, necesito ver las facturas que tengo de luz.'),
('2022-03-13 07:24:42', 2, 'Buenas tardes. Estoy pidiendo la factura que me habéis cargado el 25 de septiembre con importe de XX€. Mi empresa es Panadería González S.L. Por favor, enviadme la factura, que me urge.'),
('2022-06-17 06:07:44', 3, 'Hola, llamo porque he llamado antes, pero me ha atendido una operadora, pero se me ha cortado. Para que me digan la factura de este mes, ¿cuánto es? ¿Cuánto es? Mi número de teléfono lo tienen ustedes ahí. Bueno, tienen el móvil y el de casa, así que si pueden me llaman, gracias, para saber lo que tengo que pagar este mes, ¿vale? Gracias.'),
('2023-02-15 08:30:45', 11, 'Buenos días, solicito las facturas de los últimos tres meses. Gracias.'),
('2023-03-20 09:45:22', 12, 'Hola, necesito un duplicado de mi contrato de luz. Por favor, envíenlo a este correo.'),
('2023-05-01 14:30:10', 13, 'Buenas tardes, tengo problemas para acceder a mi cuenta y necesito las facturas de abril.'),
('2023-06-10 07:50:33', 14, 'Hola, no he recibido ninguna comunicación sobre mis facturas. ¿Podrían enviarlas? Gracias.'),
('2023-07-15 19:20:45', 15, 'Buenos días, solicito un desglose de los cargos de este mes. Quedo a la espera.'),
('2023-08-05 11:15:00', 16, 'Hola, me han cobrado un importe erróneo. Necesito una revisión urgente. Gracias.'),
('2023-09-10 16:45:12', 17, 'Buenas tardes, por favor envíenme las facturas pendientes de los meses de junio y julio.'),
('2023-10-01 18:30:45', 18, 'Hola, no puedo descargar mis facturas desde la web. Por favor, mándenmelas por correo electrónico.'),
('2023-11-05 20:00:00', 19, 'Buenas noches, necesito saber el importe exacto de la factura de este mes.'),
('2023-12-01 10:15:55', 20, 'Hola, ¿podrían actualizar mi información de contacto en su sistema? Gracias.'),
('2023-01-12 09:25:30', 21, 'Buenos días, deseo dar de baja mi contrato de gas. Indíquenme los pasos a seguir.'),
('2023-02-18 15:40:50', 22, 'Hola, necesito cambiar la cuenta bancaria asociada a mi contrato. ¿Cómo puedo hacerlo?'),
('2023-03-22 12:35:20', 23, 'Buenas tardes, tengo dudas sobre los cargos en mi última factura. Por favor, contáctenme.'),
('2023-04-28 17:50:05', 24, 'Hola, quiero contratar un nuevo servicio de gas para mi domicilio. ¿Qué debo hacer?'),
('2023-05-30 08:15:15', 25, 'Buenos días, he recibido un aviso de impago y deseo regularizar mi situación.'),
('2023-06-25 14:45:55', 26, 'Hola, por favor envíenme el historial de consumo de los últimos 6 meses.'),
('2023-07-18 19:05:40', 27, 'Buenas tardes, necesito asistencia para entender mi factura de este mes.'),
('2023-08-22 07:30:25', 28, 'Hola, ¿podrían confirmar si mi último pago ha sido recibido? Gracias.'),
('2023-09-27 13:20:35', 29, 'Buenas, quisiera conocer las tarifas actuales para nuevos clientes.'),
('2023-10-30 16:55:50', 30, 'Hola, tengo problemas para acceder a mi cuenta en línea. ¿Podrían ayudarme?'),
('2023-11-15 11:10:05', 31, 'Buenos días, deseo saber cómo puedo cambiar la potencia contratada.'),
('2023-12-20 18:25:15', 32, 'Hola, necesito información sobre promociones vigentes.'),
('2023-01-05 20:40:25', 33, 'Buenas noches, he olvidado mi contraseña y no puedo acceder a mi cuenta.'),
('2023-02-10 09:55:35', 34, 'Hola, ¿podrían enviarme una copia del contrato firmado?'),
('2023-03-15 15:15:45', 35, 'Buenas tardes, tengo un cargo duplicado en mi cuenta bancaria. Necesito aclararlo.'),
('2023-04-20 10:30:55', 36, 'Hola, quisiera saber si ofrecen planes de energía renovable.'),
('2023-05-25 16:45:05', 37, 'Buenas, necesito actualizar mis datos personales. ¿Cómo procedo?'),
('2023-06-30 12:00:15', 38, 'Hola, ¿hay algún descuento por pago anual anticipado?'),
('2023-07-05 17:15:25', 39, 'Buenos días, deseo reportar una incidencia en el suministro eléctrico.'),
('2023-08-10 08:30:35', 40, 'Hola, ¿pueden facilitarme mi número de cliente? Lo he extraviado.'),
('2023-09-15 13:45:45', 41, 'Buenas tardes, sigo sin poder acceder a mis facturas en línea. Necesito ayuda.'),
('2023-10-20 18:00:55', 42, 'Hola, he cambiado de domicilio. ¿Cómo actualizo mi dirección en el contrato?'),
('2023-11-25 09:15:05', 43, 'Buenos días, deseo contratar un servicio adicional de mantenimiento.'),
('2023-12-30 14:30:15', 44, 'Hola, me gustaría saber si hay cortes programados en mi zona.'),
('2023-01-04 19:45:25', 45, 'Buenas noches, tengo problemas con la factura electrónica. ¿Pueden enviármela en papel?'),
('2023-02-09 10:00:35', 46, 'Hola, necesito asistencia técnica para mi contador de luz.'),
('2023-03-14 15:15:45', 47, 'Buenas tardes, he recibido una factura con un importe muy elevado. ¿Podrían revisarla?'),
('2023-04-19 20:30:55', 48, 'Hola, quiero dar de alta un nuevo punto de suministro en otra vivienda.'),
('2023-05-24 11:45:05', 49, 'Buenos días, ¿cómo puedo activar la facturación electrónica?'),
('2023-06-29 17:00:15', 50, 'Hola, he recibido una oferta de otra compañía. ¿Pueden mejorar mi tarifa actual?');
