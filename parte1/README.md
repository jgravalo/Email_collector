## Definición de la API

**Endpoint:** `/classify-email` 

**Método:** `POST` 

**Parámetros** (enviados en el cuerpo como texto **JSON**): 

``` json
{ 
  "client_id": integer, 
  "fecha_envio": string, 
  "email_body": string 
} 
```
 

### Respuesta

### Si el cliente no tiene impagos

**Código de respuesta:** 200 

**Cuerpo** de la respuesta (formato **JSON**): 

``` json
{ 
  "exito": boolean,
  "prediccion": string 
} 
```

### Si el cliente tiene impagos

**Código de respuesta:** 200

**Cuerpo** de la respuesta (formato **JSON**): 

``` json
{ 
  "exito": false,
  "razon": "El cliente tiene impagos", 
} 
```


**Descripción**: El endpoint `/classify-email` acepta peticiones con el método `POST`. 
Se espera recibir tres parámetros en el cuerpo de la solicitud: 
`client_id`, que debe ser un número entero; `fecha_envio`, que representa la fecha y hora de envío en formato de fecha y hora 
(formato `YYYY-MM-dd hh:mm:ss`); y `email_body`, que es una cadena de texto que contiene el cuerpo del correo electrónico 
a clasificar. Si la solicitud es procesada con éxito, el endpoint devolverá un código de estado 200 y un objeto JSON 
con un campo llamado `prediccion`, que contendrá una cadena de texto con la predicción, junto con un campo
`exito`, un booleano que tendrá valor `true`.

En caso de que el cliente figure entre los impagados, el endpoint devolverá un código de estado 200 y un objeto JSON
con un campo `exito` con valor `false` y un campo `razon` con el mensaje "El cliente tiene impagos".