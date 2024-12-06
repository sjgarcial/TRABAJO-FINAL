# from fastapi import FastAPI
# from pydantic import BaseModel
# import random

# app = FastAPI()


# # Diccionario de categorías con palabras clave y respuestas
# categorias = {
#     "saludo": {
#         "palabras_claves": ["hola", "buenos dias", "buenas tardes", "buenas noches"],
#         "respuestas": {
#             "hola": "Hola, ¿qué tal?",
#             "buenos dias": "Buenos días, un gusto saludarte",
#             "buenas tardes": "Buenas tardes, un gusto saludarte",
#             "buenas noches": "Buenas noches, un placer tenerte en esta noche tan maravillosa"
#         }
#     },
#     "Información de contacto": {
#         "palabras_claves": ["¿como puedo contactarlos?", "¿Cuál es el número de teléfono?", "¿Cuál es la dirección?", "¿Cuál es el correo electronico?"],
#         "respuestas": {
#             "¿como puedo contactarlos?": "Tenemos medios de comunicacion vitual y sedes fisicas",
#             "¿Cuál es el número de teléfono?": "El numero de telefono es: 3113458596",
#             "¿Cuál es la dirección?": "La dirección es: calle 70 # 45-08 Sabaneta-Antioquia",
#             "¿Cuál es el correo electronico?": "La direccion de correo electronico es macbro246@gmail.com"
#         }
#     },
#     "Horario de atención": {
#         "palabras_claves": ["¿Cuál es el horario de atención?", "¿En qué días están abiertos?", "¿Cuál es el horario de atención virtual?"],
#         "respuestas": {
#             "¿Cuál es el horario de atención?": "Nuestro horario de atención es de lunes a viernes de 8:00 a.m. a 6:00 p.m., y sábados de 9:00 a.m. a 2:00 p.m.",
#             "¿En qué días están abiertos?": "Estamos abiertos de lunes a sábado. Los domingos y festivos permanecemos cerrados.",
#             "¿Cuál es el horario de atención virtual?": "Atendemos virtualmente de lunes a viernes de 8:00 a.m. a 8:00 p.m. a través de nuestro chat en línea y correo electrónico."
#         }
#     },
#     "Política de devolución": {
#         "palabras_claves": ["¿Cuál es la política de devoluciones?", "¿Puedo devolver el producto?"],
#         "respuestas": {
#             "¿Cuál es la política de devoluciones?": "Nuestra política de devoluciones permite realizar cambios o devoluciones dentro de los 15 días posteriores a la compra, siempre que el producto esté en su estado original y cuente con la factura.",
#             "¿Puedo devolver el producto?": "Sí, puedes devolver el producto si presenta defectos de fábrica o si no cumple con tus expectativas, siguiendo nuestra política de devoluciones."
#         }
#     },
#     "Soporte técnico": {
#         "palabras_claves": ["Tengo un problema técnico", "¿Cómo puedo solucionar un error?"],
#         "respuestas": {
#             "Tengo un problema técnico": "Lamentamos el inconveniente. Por favor, contacta a nuestro soporte técnico al correo soporte@empresa.com o llama al 3113458596 para recibir asistencia.",
#             "¿Cómo puedo solucionar un error?": "Puedes intentar reiniciar el dispositivo o verificar las instrucciones del manual. Si el problema persiste, comunícate con nuestro equipo de soporte técnico."
#         }
#     },
#     "despedida": {
#         "palabras_claves": ["adios", "chao", "hasta luego", "nos vemos", "bye"],
#         "respuestas": {
#             "adios": "Gracias por su visita",
#             "chao": "Un gusto atenderlo",
#             "hasta luego": "Que tenga un buen día",
#             "nos vemos": "Nos vemos pronto",
#             "bye": "Nos vemos pronto"
#         }
#     },
#     "precio": {
#         "palabras_claves": ["precio", "cuánto cuesta", "cuánto vale", "cuánto es", "valor"],
#         "respuestas": {
#             "precio": "El precio depende del modelo del celular. ¿Cuál te interesa?",
#             "cuánto cuesta": "El precio depende del modelo del celular. ¿Cuál te interesa?",
#             "cuánto vale": "El precio depende del modelo del celular. ¿Cuál te interesa?",
#             "cuánto es": "El precio depende del modelo del celular. ¿Cuál te interesa?",
#             "valor": "El valor es de 500.000 pesos "
#         }
#     },
#     "Métodos de pago": {
#         "palabras_claves": ["¿Qué métodos de pago aceptan?", "¿Aceptan tarjeta de crédito?", "¿Puedo pagar en efectivo?", "¿Tienen pago contra entrega?", "¿Aceptan transferencias bancarias?"],
#         "respuestas": {
#             "¿Qué métodos de pago aceptan?": "Aceptamos tarjeta de crédito, débito, transferencias bancarias y pagos en efectivo.",
#             "¿Aceptan tarjeta de crédito?": "Sí, aceptamos todas las tarjetas de crédito principales.",
#             "¿Puedo pagar en efectivo?": "Sí, puedes pagar en efectivo en nuestras tiendas físicas o contra entrega.",
#             "¿Tienen pago contra entrega?": "Sí, ofrecemos pago contra entrega en ciertas áreas. Por favor, consulta disponibilidad.",
#             "¿Aceptan transferencias bancarias?": "Sí, puedes realizar transferencias bancarias a nuestra cuenta. Te enviaremos los datos al confirmar tu pedido."
#         }
#     },
#     "Productos disponibles": {
#         "palabras_claves": ["¿Qué productos tienen?", "¿Tienen productos nuevos?", "¿Qué modelos de celulares venden?", "¿Tienen promociones?"],
#         "respuestas": {
#             "¿Qué productos tienen?": "Ofrecemos celulares, accesorios y servicios técnicos especializados.",
#             "¿Tienen productos nuevos?": "Sí, actualizamos nuestro catálogo regularmente con los últimos modelos.",
#             "¿Qué modelos de celulares venden?": "Trabajamos con las marcas más reconocidas como Samsung, iPhone y Xiaomi.",
#             "¿Tienen promociones?": "¡Claro! Tenemos descuentos cada semana. Consulta nuestras ofertas vigentes."
#         }
#     },
#     "Garantías": {
#         "palabras_claves": ["¿Ofrecen garantía?", "¿Qué cubre la garantía?", "¿Cuánto tiempo dura la garantía?", "¿Cómo puedo reclamar la garantía?"],
#         "respuestas": {
#             "¿Ofrecen garantía?": "Sí, todos nuestros productos cuentan con garantía.",
#             "¿Qué cubre la garantía?": "La garantía cubre defectos de fábrica y fallos técnicos no provocados por el usuario.",
#             "¿Cuánto tiempo dura la garantía?": "La duración de la garantía varía según el producto, generalmente entre 6 meses y 1 año.",
#             "¿Cómo puedo reclamar la garantía?": "Para reclamar la garantía, por favor trae tu factura y el producto a nuestra tienda."
#         }
#     },
#     "Envíos": {
#         "palabras_claves": ["¿Hacen envíos?", "¿Cuánto cuesta el envío?", "¿Cuánto tarda el envío?", "¿Puedo hacer seguimiento al envío?"],
#         "respuestas": {
#             "¿Hacen envíos?": "Sí, hacemos envíos a todo el país.",
#             "¿Cuánto cuesta el envío?": "El costo del envío depende de la ubicación. Consulta con nuestro asesor.",
#             "¿Cuánto tarda el envío?": "Los envíos tardan entre 2 y 5 días hábiles, dependiendo de tu ubicación.",
#             "¿Puedo hacer seguimiento al envío?": "Sí, te proporcionaremos un número de seguimiento al despachar tu pedido."
#         }
#     },
#     "Problemas con el pedido": {
#         "palabras_claves": ["No llegó mi pedido", "Recibí un producto equivocado", "Mi pedido llegó dañado", "¿Qué hago si tengo un problema con el pedido?"],
#         "respuestas": {
#             "No llegó mi pedido": "Lamentamos la demora. Por favor, comunícate con nuestro servicio al cliente para resolver el problema.",
#             "Recibí un producto equivocado": "Pedimos disculpas. Por favor, contáctanos para gestionar el cambio de producto.",
#             "Mi pedido llegó dañado": "¡Lo sentimos! Puedes hacer uso de la garantía o devolverlo según nuestra política.",
#             "¿Qué hago si tengo un problema con el pedido?": "Contáctanos de inmediato a través de nuestros canales de atención al cliente."
#         }
#     },
#     "Cuidados y mantenimiento": {
#         "palabras_claves": ["¿Cómo cuido mi celular?", "¿Qué debo hacer para prolongar la vida de la batería?", "¿Cómo limpiar mi celular?"],
#         "respuestas": {
#             "¿Cómo cuido mi celular?": "Utiliza siempre una funda protectora y un protector de pantalla. Evita exponerlo a altas temperaturas.",
#             "¿Qué debo hacer para prolongar la vida de la batería?": "Evita que la batería llegue al 0% y usa cargadores originales.",
#             "¿Cómo limpiar mi celular?": "Limpia la pantalla con un paño de microfibra y evita el uso de líquidos directamente sobre el dispositivo."
#         }
#     },
#     "Promociones y descuentos": {
#         "palabras_claves": ["¿Tienen descuentos?", "¿Qué promociones están vigentes?", "¿Cómo puedo acceder a un descuento?"],
#         "respuestas": {
#             "¿Tienen descuentos?": "Sí, contamos con descuentos especiales cada mes. ¡Consulta nuestras redes sociales para más información!",
#             "¿Qué promociones están vigentes?": "Actualmente tenemos un 20% de descuento en accesorios y envío gratis en compras superiores a 200,000 pesos.",
#             "¿Cómo puedo acceder a un descuento?": "Puedes acceder a los descuentos aplicando los cupones promocionales en nuestra tienda en línea o visitando nuestras sucursales."
#         }
#     },
#     "Tiempo de entrega": {
#         "palabras_claves": ["¿Cuánto tarda en llegar mi pedido?", "¿Pueden entregar el mismo día?", "¿Cuánto es el tiempo de espera para envíos?"],
#         "respuestas": {
#             "¿Cuánto tarda en llegar mi pedido?": "El tiempo de entrega varía según tu ubicación, pero generalmente toma entre 2 y 5 días hábiles.",
#             "¿Pueden entregar el mismo día?": "Sí, contamos con servicio de entrega el mismo día en áreas seleccionadas. Consulta disponibilidad con nuestro equipo.",
#             "¿Cuánto es el tiempo de espera para envíos?": "Los envíos regulares tardan de 2 a 5 días hábiles. Los envíos exprés pueden llegar en 1 día hábil en ciudades principales."
#         }
#     },
#     "Compatibilidad de productos": {
#         "palabras_claves": ["¿Este accesorio es compatible con mi celular?", "¿Puedo usar este cargador con mi dispositivo?", "¿Cómo sé si un producto es compatible con mi modelo?"],
#         "respuestas": {
#             "¿Este accesorio es compatible con mi celular?": "Por favor, verifica las especificaciones del producto en nuestra página web o consulta con un asesor.",
#             "¿Puedo usar este cargador con mi dispositivo?": "Recomendamos utilizar cargadores compatibles y originales para evitar problemas. Contáctanos si tienes dudas sobre un modelo específico.",
#             "¿Cómo sé si un producto es compatible con mi modelo?": "Puedes buscar tu modelo en nuestra página de productos o consultar con nuestro equipo de soporte para asegurarte."
#         }
#     },
#     "Estado de los productos": {
#         "palabras_claves": ["¿Son nuevos los productos?", "¿Venden productos reacondicionados?", "¿Los productos tienen garantía de calidad?"],
#         "respuestas": {
#             "¿Son nuevos los productos?": "Sí, todos nuestros productos son nuevos y cuentan con garantía de fábrica.",
#             "¿Venden productos reacondicionados?": "Sí, ofrecemos productos reacondicionados a precios más accesibles, con garantía incluida.",
#             "¿Los productos tienen garantía de calidad?": "Sí, todos nuestros productos son revisados y cumplen con altos estándares de calidad."
#         }
#     },
#     "Cuentas y registro": {
#         "palabras_claves": ["¿Necesito una cuenta para comprar?", "¿Cómo creo una cuenta?", "Olvidé mi contraseña, ¿qué hago?"],
#         "respuestas": {
#             "¿Necesito una cuenta para comprar?": "No es obligatorio, pero tener una cuenta te permite acceder a beneficios como historial de pedidos y descuentos exclusivos.",
#             "¿Cómo creo una cuenta?": "Puedes registrarte fácilmente en nuestra página web llenando el formulario de registro con tus datos básicos.",
#             "Olvidé mi contraseña, ¿qué hago?": "No te preocupes, puedes restablecer tu contraseña haciendo clic en '¿Olvidaste tu contraseña?' en la página de inicio de sesión."
#         }
#     },
#     "Ubicación de tiendas": {
#         "palabras_claves": ["¿Dónde están ubicados?", "¿Tienen tiendas físicas?", "¿Cuál es la dirección de su tienda principal?"],
#         "respuestas": {
#             "¿Dónde están ubicados?": "Tenemos varias sucursales en todo el país. Consulta nuestra página web para encontrar la más cercana.",
#             "¿Tienen tiendas físicas?": "Sí, contamos con tiendas físicas en diferentes ciudades. ¡Te esperamos!",
#             "¿Cuál es la dirección de su tienda principal?": "Nuestra tienda principal está ubicada en calle 70 # 45-08 Sabaneta-Antioquia."
#         }
#     }
# }

# # Clasificador de categorías con palabra clave
# def clasificar_categoria(frase):
#     frase = frase.lower()  # Convierte en minúsculas
#     for categoria, data in categorias.items():
#         for palabra_clave in data["palabras_claves"]:
#             if palabra_clave.lower() in frase:  # Coincidencia exacta o parcial
#                 return categoria, palabra_clave
#     return "desconocido", None

# # # Clasificador de categorías con palabra clave
# # def clasificar_categoria(frase):
# #     frase = frase.lower()  # Convierte en minúsculas
# #     for categoria, data in categorias.items(): 
# #         if any(palabra_clave in frase for palabra_clave in data["palabras_claves"]):
# #             return categoria
# #     return "desconocido"

# # Chatbot
# def chatbot(frase_usuario):
#     categoria, palabra_clave = clasificar_categoria(frase_usuario)
#     if categoria == "desconocido":
#         return "Lo siento, no entendí tu pregunta. Por favor, sea más específico."
#     # Devuelve la respuesta correspondiente a la palabra clave
#     return categorias[categoria]["respuestas"].get(palabra_clave, "Lo siento, no tengo una respuesta para eso.")

# # Modelo para entrada de datos
# class FraseEntrada(BaseModel):
#     frase: str

# # Endpoint del chatbot
# @app.post("/chatbot/")
# def obtener_respuesta(entrada: FraseEntrada):
#     respuesta = chatbot(entrada.frase)
#     return {"respuesta": respuesta}


# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List, Dict

# app = FastAPI()

# # Base de datos simulada en memoria
# usuarios_db = []  # Lista que actuará como base de datos

# # Modelo para los datos del cliente
# class Usuario(BaseModel):
#     nombre: str
#     edad: int
#     enfermedades: List[str]

# # Endpoint para agregar o verificar usuarios
# @app.post("/registro/")
# def registro_usuario(usuario: Usuario):
#     # Verificar si el usuario ya existe
#     for registrado in usuarios_db:
#         if registrado['nombre'].lower() == usuario.nombre.lower():
#             return {
#                 "mensaje": f"El cliente '{usuario.nombre}' ya se encuentra registrado.",
#                 "datos": registrado
#             }
#     # Si no existe, registrar al usuario
#     nuevo_usuario = {
#         "nombre": usuario.nombre,
#         "edad": usuario.edad,
#         "enfermedades": usuario.enfermedades
#     }
#     usuarios_db.append(nuevo_usuario)
#     return {
#         "mensaje": f"El cliente '{usuario.nombre}' ha sido registrado exitosamente.",
#         "datos": nuevo_usuario
#     }

# # Endpoint para mostrar todos los usuarios registrados
# @app.get("/usuarios/")
# def listar_usuarios():
#     if not usuarios_db:
#         return {"mensaje": "No hay usuarios registrados."}
#     return {"usuarios": usuarios_db}

# # Endpoint interactivo para el chatbot
# @app.post("/chatbot/")
# def chatbot(pregunta: str):
#     if "registrar" in pregunta.lower():
#         # return {"mensaje": "Por favor, proporcione su nombre, edad y enfermedades para registrarse."}
#         return registro_usuario()
#     elif "listar" in pregunta.lower():
#         return listar_usuarios()
#         # return {"mensaje": "Puede ver todos los usuarios registrados en el sistema usando el endpoint '/usuarios/'."}
#     else:
#         return {"mensaje": "¿En qué más puedo ayudarte? Puede registrarse o listar usuarios."}

# import pandas as pd
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# # Ruta del archivo Excel donde se guardarán los datos
# DATABASE_PATH = "usuarios_db.xlsx"

# # Modelo de datos del usuario
# class Usuario(BaseModel):
#     nombre: str
#     edad: int
#     enfermedades: List[str]

# # Función para cargar datos desde Excel
# def cargar_datos():
#     try:
#         # Leer el archivo Excel
#         return pd.read_excel(DATABASE_PATH)
#     except FileNotFoundError:
#         # Si el archivo no existe, crear un DataFrame vacío
#         return pd.DataFrame(columns=["nombre", "edad", "enfermedades"])

# # Función para guardar datos en Excel
# def guardar_datos(data):
#     data.to_excel(DATABASE_PATH, index=False)

# # Cargar la base de datos al iniciar la aplicación
# usuarios_df = cargar_datos()

# # Endpoint para registrar o verificar usuarios
# @app.post("/registro/")
# def registro_usuario(usuario: Usuario):
#     global usuarios_df

#     # Verificar si el usuario ya existe en el DataFrame
#     if not usuarios_df.empty and usuario.nombre.lower() in usuarios_df['nombre'].str.lower().values:
#         # Si el usuario existe, devolver un mensaje
#         datos_existentes = usuarios_df[usuarios_df['nombre'].str.lower() == usuario.nombre.lower()]
#         return {
#             "mensaje": f"El cliente '{usuario.nombre}' ya se encuentra registrado.",
#             "datos": datos_existentes.to_dict(orient="records")
#         }

#     # Si el usuario no existe, agregarlo al DataFrame
#     nuevo_usuario = {
#         "nombre": usuario.nombre,
#         "edad": usuario.edad,
#         "enfermedades": ",".join(usuario.enfermedades)  # Convertir la lista en una cadena separada por comas
#     }
#     # Usar concat() para agregar el nuevo usuario al DataFrame
#     usuarios_df = pd.concat([usuarios_df, pd.DataFrame([nuevo_usuario])], ignore_index=True)
#     guardar_datos(usuarios_df)  # Guardar los datos en el archivo Excel
#     return {
#         "mensaje": f"El cliente '{usuario.nombre}' ha sido registrado exitosamente.",
#         "datos": nuevo_usuario
#     }

# # Endpoint para listar todos los usuarios registrados
# @app.get("/usuarios/")
# def listar_usuarios():
#     if usuarios_df.empty:  # Si el DataFrame está vacío
#         return {"mensaje": "No hay usuarios registrados."}
    
#     # Convertir el DataFrame a una lista de diccionarios
#     usuarios = usuarios_df.to_dict(orient="records")
    
#     # Convertir la cadena de enfermedades de nuevo en lista
#     for usuario in usuarios:
#         usuario["enfermedades"] = usuario["enfermedades"].split(",")  # Convertir cadena de enfermedades a lista
    
#     return {"usuarios": usuarios}

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# import pandas as pd
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Configurar CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Permitir todos los orígenes
#     allow_credentials=True,
#     allow_methods=["*"],  # Permitir todos los métodos
#     allow_headers=["*"],  # Permitir todos los encabezados
# )

# # Rutas de los archivos Excel
# DATABASE_PATH = "usuarios_db.xlsx"  # Usuarios
# FOOD_DATABASE_PATH = "Alimentos y propiedades.xlsx"  # Alimentos

# # Modelo de datos para usuarios
# class Usuario(BaseModel):
#     nombre: str
#     edad: int
#     enfermedades: List[str]

# # Modelo de datos para alimentos
# class Food(BaseModel):
#     Alimento: str
#     Propiedades: str
#     Calorias:int 
#     Beneficios: str
#     Impacto_Cuerpo: str
#     Enfermedades: List[str]

# # Función para cargar datos desde Excel
# def cargar_datos(ruta, columnas):
#     try:
#         return pd.read_excel(ruta)
#     except FileNotFoundError:
#         return pd.DataFrame(columns=columnas)

# # Función para guardar datos en Excel
# def guardar_datos(data, ruta):
#     data.to_excel(ruta, index=False)

# # Cargar las bases de datos al iniciar la aplicación
# usuarios_df = cargar_datos(DATABASE_PATH, ["nombre", "edad", "enfermedades"])
# foods_df = cargar_datos(FOOD_DATABASE_PATH,["Alimento","Propiedades","Calorias","Beneficios","Impacto_Cuerpo","Enfermedades"])

# # Endpoints para usuarios
# @app.post("/registro/")
# def registro_usuario(usuario: Usuario):
#     global usuarios_df

#     # Verificar si el usuario ya existe
#     if not usuarios_df.empty and usuario.nombre.lower() in usuarios_df['nombre'].str.lower().values:
#         datos_existentes = usuarios_df[usuarios_df['nombre'].str.lower() == usuario.nombre.lower()]
#         return {
#             "mensaje": f"El cliente '{usuario.nombre}' ya se encuentra registrado.",
#             "datos": datos_existentes.to_dict(orient="records")
#         }

#     # Si no existe, agregar el usuario
#     nuevo_usuario = {
#         "nombre": usuario.nombre,
#         "edad": usuario.edad,
#         "enfermedades": ",".join(usuario.enfermedades)
#     }
#     usuarios_df = pd.concat([usuarios_df, pd.DataFrame([nuevo_usuario])], ignore_index=True)
#     guardar_datos(usuarios_df, DATABASE_PATH)

#     return {
#         "mensaje": f"El cliente '{usuario.nombre}' ha sido registrado exitosamente.",
#         "datos": nuevo_usuario
#     }

# @app.get("/usuarios/")
# def listar_usuarios():
#     if usuarios_df.empty:
#         return {"mensaje": "No hay usuarios registrados."}
    
#     # Convertir el DataFrame a una lista de diccionarios
#     usuarios = usuarios_df.to_dict(orient="records")
    
#     # Convertir la cadena de enfermedades de nuevo en lista
#     for usuario in usuarios:
#         usuario["enfermedades"] = usuario["enfermedades"].split(",")
    
#     return {"usuarios": usuarios}

# # Endpoints para alimentos
# @app.post("/foods/")
# def agregar_alimento(food: Food):
#     global foods_df

#     # Crear un diccionario con los datos del alimento
#     nuevo_alimento = {
#         "Alimento": food.Alimento,
#         "Propiedades": food.Propiedades,
#         "Calorias": food.Calorias,
#         "Beneficios": food.Beneficios,
#         "Impacto_Cuerpo": food.Impacto_Cuerpo,
#         "Enfermedades": ",".join(food.Enfermedades)
#     }

#     # Agregar el nuevo alimento al DataFrame
#     foods_df = pd.concat([foods_df, pd.DataFrame([nuevo_alimento])], ignore_index=True)
#     guardar_datos(foods_df, FOOD_DATABASE_PATH)
#     return {
#         "mensaje": f"El alimento '{food.Alimento}' ha sido agregado exitosamente.",
#         "datos": nuevo_alimento
#     }

# @app.get("/foods/")
# def listar_alimentos():
#     if foods_df.empty:
#         return {"mensaje": "No hay alimentos registrados."}
    
#     # Convertir el DataFrame a una lista de diccionarios
#     alimentos = foods_df.to_dict(orient="records")
#     return {"alimentos": alimentos} 

# @app.get("/Recomendaciones/{usuario_nombre}")
# def recomendaciones(usuario_nombre: str):
#     global usuarios_df, foods_df

#     # Verificar si el usuario existe
#     if usuarios_df.empty or usuario_nombre.lower() not in usuarios_df['nombre'].str.lower().values:
#         return {"mensaje": f"No se encontró el usuario '{usuario_nombre}'."}

#     # Obtener las enfermedades del usuario
#     usuario = usuarios_df[usuarios_df['nombre'].str.lower() == usuario_nombre.lower()].iloc[0]
#     enfermedades_usuario = usuario["enfermedades"].split(",")

#     # Buscar alimentos relacionados con las enfermedades del usuario
#     if foods_df.empty:
#         return {"mensaje": "No hay alimentos registrados para hacer recomendaciones."}

#     alimentos_recomendados = []
#     for _, alimento in foods_df.iterrows():
#         enfermedades_alimento = alimento["Enfermedades"].split(",")
#         if any(enf in enfermedades_usuario for enf in enfermedades_alimento):
#             alimentos_recomendados.append({
#                 "Alimento": alimento["Alimento"],
#                 "Propiedades": alimento["Propiedades"],
#                 "Calorias": f"""{alimento["Calorias"]} calorias por 100 gramos de peso""",
#                 "Beneficios": f"""Algunos beneficios son: '{alimento["Beneficios"]}'""",
#                 "Impacto_Cuerpo": alimento["Impacto_Cuerpo"],
#                 "Enfermedades": enfermedades_alimento
#             })

#     if not alimentos_recomendados:
#         return {"mensaje": f"No se encontraron alimentos relacionados con las enfermedades de '{usuario_nombre}'."}

#     return {
#         "mensaje": f"Recomendaciones de alimentos para el usuario '{usuario_nombre}':",
#         "recomendaciones": alimentos_recomendados
#     }


# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# import pandas as pd
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Configurar CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Permitir todos los orígenes
#     allow_credentials=True,
#     allow_methods=["*"],  # Permitir todos los métodos
#     allow_headers=["*"],  # Permitir todos los encabezados
# )

# # Rutas de los archivos Excel
# DATABASE_PATH = "usuarios_db.xlsx"  # Usuarios

# # Modelo de datos para usuarios
# class Usuario(BaseModel):
#     nombre: str
#     edad: int
#     enfermedades: List[str]

# # Modelo de datos para alimentos
# class Food(BaseModel):
#     Alimento: str
#     Propiedades: str
#     Calorias:int 
#     Beneficios: str
#     Impacto_Cuerpo: str
#     Enfermedades: List[str]

# # Función para cargar datos desde una hoja específica de Excel
# def cargar_datos(ruta: str, columnas: List[str], hoja: str):
#     try:
#         # Leer los datos de la hoja especificada
#         return pd.read_excel(ruta, sheet_name=hoja)
#     except FileNotFoundError:
#         # Si el archivo no existe, devuelve un DataFrame vacío con las columnas proporcionadas
#         return pd.DataFrame(columns=columnas)
#     except ValueError:
#         # Si la hoja no existe, devuelve un DataFrame vacío con las columnas proporcionadas
#         return pd.DataFrame(columns=columnas)

# # Función para guardar datos en Excel
# def guardar_datos_hojas(data: pd.DataFrame, ruta: str, hoja: str):
#     try:
#         # Abrir el archivo existente y agregar o sobrescribir la hoja correspondiente
#         with pd.ExcelWriter(ruta, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
#             data.to_excel(writer, index=False, sheet_name=hoja)
#     except FileNotFoundError:
#         # Si el archivo no existe, crearlo
#         with pd.ExcelWriter(ruta, engine="openpyxl") as writer:
#             data.to_excel(writer, index=False, sheet_name=hoja)

# # Cargar las bases de datos al iniciar la aplicación
# usuarios_df = cargar_datos(DATABASE_PATH, ["nombre", "edad", "enfermedades"], "Usuarios")
# foods_df = cargar_datos(DATABASE_PATH, ["Alimento", "Propiedades", "Calorias", "Beneficios", "Impacto_Cuerpo", "Enfermedades"], "Alimentos")

# # Endpoints para usuarios
# @app.post("/registro/")
# def registro_usuario(usuario: Usuario):
#     global usuarios_df

#     # Verificar si el usuario ya existe
#     if not usuarios_df.empty and usuario.nombre.lower() in usuarios_df['nombre'].str.lower().values:
#         datos_existentes = usuarios_df[usuarios_df['nombre'].str.lower() == usuario.nombre.lower()]
#         return {
#             "mensaje": f"El cliente '{usuario.nombre}' ya se encuentra registrado.",
#             "datos": datos_existentes.to_dict(orient="records")
#         }

#     # Si no existe, agregar el usuario
#     nuevo_usuario = {
#         "nombre": usuario.nombre,
#         "edad": usuario.edad,
#         "enfermedades": ",".join(usuario.enfermedades)
#     }
#     usuarios_df = pd.concat([usuarios_df, pd.DataFrame([nuevo_usuario])], ignore_index=True)
    
#     # Guardar en la hoja "Usuarios"
#     guardar_datos_hojas(usuarios_df, DATABASE_PATH, "Usuarios")

#     return {
#         "mensaje": f"El cliente '{usuario.nombre}' ha sido registrado exitosamente.",
#         "datos": nuevo_usuario
#     }

# @app.get("/usuarios/")
# def listar_usuarios():
#     if usuarios_df.empty:
#         return {"mensaje": "No hay usuarios registrados."}
    
#     # Convertir el DataFrame a una lista de diccionarios
#     usuarios = usuarios_df.to_dict(orient="records")
    
#     # Convertir la cadena de enfermedades de nuevo en lista
#     for usuario in usuarios:
#         usuario["enfermedades"] = usuario["enfermedades"].split(",")
    
#     return {"usuarios": usuarios}

# # Endpoints para alimentos
# @app.post("/foods/")
# def agregar_alimento(food: Food):
#     global foods_df

#     # Crear un diccionario con los datos del alimento
#     nuevo_alimento = {
#         "Alimento": food.Alimento,
#         "Propiedades": food.Propiedades,
#         "Calorias": food.Calorias,
#         "Beneficios": food.Beneficios,
#         "Impacto_Cuerpo": food.Impacto_Cuerpo,
#         "Enfermedades": ",".join(food.Enfermedades)
#     }

#     # Agregar el nuevo alimento al DataFrame
#     foods_df = pd.concat([foods_df, pd.DataFrame([nuevo_alimento])], ignore_index=True)
    
#     # Guardar en la hoja "Alimentos"
#     guardar_datos_hojas(foods_df, DATABASE_PATH, "Alimentos")
    
#     return {
#         "mensaje": f"El alimento '{food.Alimento}' ha sido agregado exitosamente.",
#         "datos": nuevo_alimento
#     }

# @app.get("/foods/")
# def listar_alimentos():
#     if foods_df.empty:
#         return {"mensaje": "No hay alimentos registrados."}
    
#     # Convertir el DataFrame a una lista de diccionarios
#     alimentos = foods_df.to_dict(orient="records")
#     return {"alimentos": alimentos} 

# @app.get("/Recomendaciones/{usuario_nombre}")
# def recomendaciones(usuario_nombre: str):
#     global usuarios_df, foods_df

#     # Verificar si el usuario existe
#     if usuarios_df.empty or usuario_nombre.lower() not in usuarios_df['nombre'].str.lower().values:
#         return {"mensaje": f"No se encontró el usuario '{usuario_nombre}'."}

#     # Obtener las enfermedades del usuario
#     usuario = usuarios_df[usuarios_df['nombre'].str.lower() == usuario_nombre.lower()].iloc[0]
#     enfermedades_usuario = usuario["enfermedades"].split(",")

#     # Buscar alimentos relacionados con las enfermedades del usuario
#     if foods_df.empty:
#         return {"mensaje": "No hay alimentos registrados para hacer recomendaciones."}

#     alimentos_recomendados = []
#     for _, alimento in foods_df.iterrows():
#         enfermedades_alimento = alimento["Enfermedades"].split(",")
#         if any(enf in enfermedades_usuario for enf in enfermedades_alimento):
#             alimentos_recomendados.append({
#                 "Alimento": alimento["Alimento"],
#                 "Propiedades": alimento["Propiedades"],
#                 "Calorias": f"""{alimento["Calorias"]} calorias por 100 gramos de peso""",
#                 "Beneficios": f"""Algunos beneficios son: '{alimento["Beneficios"]}'""",
#                 "Impacto_Cuerpo": alimento["Impacto_Cuerpo"],
#                 "Enfermedades": enfermedades_alimento
#             })

#     if not alimentos_recomendados:
#         return {"mensaje": f"No se encontraron alimentos relacionados con las enfermedades de '{usuario_nombre}'."}

#     return {
#         "mensaje": f"Recomendaciones de alimentos para el usuario '{usuario_nombre}':",
#         "recomendaciones": alimentos_recomendados
#     }


# se importan las librerias
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Configurar CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Ruta de los archivos Excel
DATABASE_PATH = "usuarios_db.xlsx"  # Ruta del archivo de usuarios

# Modelo de datos para los usuarios
class Usuario(BaseModel):
    nombre: str  # Nombre del usuario
    edad: int  # Edad del usuario
    enfermedades: List[str]  # Lista de enfermedades del usuario

# Modelo de datos para los alimentos
class Food(BaseModel):
    Alimento: str  # Nombre del alimento
    Propiedades: str  # Propiedades del alimento
    Calorias: int  # Calorías por 100 gramos
    Beneficios: str  # Beneficios del alimento
    Impacto_Cuerpo: str  # Impacto en el cuerpo
    Enfermedades: List[str]  # Enfermedades asociadas con el alimento

# Función para cargar datos desde una hoja específica de Excel
def cargar_datos(ruta: str, columnas: List[str], hoja: str):
    try:
        # Leer los datos de la hoja especificada
        return pd.read_excel(ruta, sheet_name=hoja)
    except FileNotFoundError:
        # Si el archivo no existe, devuelve un DataFrame vacío con las columnas proporcionadas
        return pd.DataFrame(columns=columnas)
    except ValueError:
        # Si la hoja no existe, devuelve un DataFrame vacío con las columnas proporcionadas
        return pd.DataFrame(columns=columnas)

# Función para guardar datos en Excel
def guardar_datos_hojas(data: pd.DataFrame, ruta: str, hoja: str):
    try:
        # Abrir el archivo existente y agregar o sobrescribir la hoja correspondiente
        with pd.ExcelWriter(ruta, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            data.to_excel(writer, index=False, sheet_name=hoja)
    except FileNotFoundError:
        # Si el archivo no existe, crearlo
        with pd.ExcelWriter(ruta, engine="openpyxl") as writer:
            data.to_excel(writer, index=False, sheet_name=hoja)

# Cargar las bases de datos al iniciar la aplicación
usuarios_df = cargar_datos(DATABASE_PATH, ["nombre", "edad", "enfermedades"], "Usuarios")
foods_df = cargar_datos(DATABASE_PATH, ["Alimento", "Propiedades", "Calorias", "Beneficios", "Impacto_Cuerpo", "Enfermedades"], "Alimentos")

# Endpoint para registrar un nuevo usuario
@app.post("/registro/")
def registro_usuario(usuario: Usuario):
    global usuarios_df

    # Verificar si el usuario ya existe
    if not usuarios_df.empty and usuario.nombre.lower() in usuarios_df['nombre'].str.lower().values:
        datos_existentes = usuarios_df[usuarios_df['nombre'].str.lower() == usuario.nombre.lower()]
        return {
            "mensaje": f"El cliente '{usuario.nombre}' ya se encuentra registrado.",
            "datos": datos_existentes.to_dict(orient="records")
        }

    # Si no existe, agregar el usuario
    nuevo_usuario = {
        "nombre": usuario.nombre,
        "edad": usuario.edad,
        "enfermedades": ",".join(usuario.enfermedades)
    }
    # Añadir el nuevo usuario al DataFrame
    usuarios_df = pd.concat([usuarios_df, pd.DataFrame([nuevo_usuario])], ignore_index=True)
    
    # Guardar los datos en la hoja "Usuarios"
    guardar_datos_hojas(usuarios_df, DATABASE_PATH, "Usuarios")

    return {
        "mensaje": f"El cliente '{usuario.nombre}' ha sido registrado exitosamente.",
        "datos": nuevo_usuario
    }

# Endpoint para listar todos los usuarios registrados
@app.get("/usuarios/")
def listar_usuarios():
    if usuarios_df.empty:
        return {"mensaje": "No hay usuarios registrados."}
    
    # Convertir el DataFrame a una lista de diccionarios
    usuarios = usuarios_df.to_dict(orient="records")
    
    # Convertir la cadena de enfermedades de nuevo en lista
    for usuario in usuarios:
        usuario["enfermedades"] = usuario["enfermedades"].split(",")
    
    return {"usuarios": usuarios}

# Endpoint para agregar un nuevo alimento
@app.post("/foods/") 
def agregar_alimento(food: Food):
    global foods_df

    # Crear un diccionario con los datos del alimento
    nuevo_alimento = {
        "Alimento": food.Alimento,
        "Propiedades": food.Propiedades,
        "Calorias": food.Calorias,
        "Beneficios": food.Beneficios,
        "Impacto_Cuerpo": food.Impacto_Cuerpo,
        "Enfermedades": ",".join(food.Enfermedades)
    }

    # Agregar el nuevo alimento al DataFrame
    foods_df = pd.concat([foods_df, pd.DataFrame([nuevo_alimento])], ignore_index=True)
    
    # Guardar los datos en la hoja "Alimentos"
    guardar_datos_hojas(foods_df, DATABASE_PATH, "Alimentos")
    
    return {
        "mensaje": f"El alimento '{food.Alimento}' ha sido agregado exitosamente.",
        "datos": nuevo_alimento
    }

# Endpoint para listar todos los alimentos registrados
@app.get("/foods/") 
def listar_alimentos():
    if foods_df.empty:
        return {"mensaje": "No hay alimentos registrados."}
    
    # Convertir el DataFrame a una lista de diccionarios
    alimentos = foods_df.to_dict(orient="records")
    return {"alimentos": alimentos} 

# Endpoint para obtener recomendaciones de alimentos según las enfermedades del usuario
@app.post("/Recomendaciones/{usuario_nombre}")
def recomendaciones(usuario_nombre: str):
    global usuarios_df, foods_df

    # Verificar si el usuario existe
    if usuarios_df.empty or usuario_nombre.lower() not in usuarios_df['nombre'].str.lower().values:
        return {"mensaje": f"No se encontró el usuario '{usuario_nombre}'."}

    # Obtener las enfermedades del usuario
    usuario = usuarios_df[usuarios_df['nombre'].str.lower() == usuario_nombre.lower()].iloc[0]
    enfermedades_usuario = usuario["enfermedades"].split(",")

    # Buscar alimentos relacionados con las enfermedades del usuario
    if foods_df.empty:
        return {"mensaje": "No hay alimentos registrados para hacer recomendaciones."}

    alimentos_recomendados = []
    for _, alimento in foods_df.iterrows():
        enfermedades_alimento = alimento["Enfermedades"].split(",")
        # Verificar si alguna de las enfermedades del usuario se encuentra en el alimento
        if any(enf in enfermedades_usuario for enf in enfermedades_alimento):
            alimentos_recomendados.append({
                "Alimento": alimento["Alimento"],
                "Propiedades": alimento["Propiedades"],
                "Calorias": f"""{alimento["Calorias"]} calorías por 100 gramos de peso""",
                "Beneficios": f"""Algunos beneficios son: '{alimento["Beneficios"]}'""",
                "Impacto_Cuerpo": alimento["Impacto_Cuerpo"],
                "Enfermedades": enfermedades_alimento
            })

    if not alimentos_recomendados:
        return {"mensaje": f"No se encontraron alimentos relacionados con las enfermedades de '{usuario_nombre}'."}

    return {
        "mensaje": f"Recomendaciones de alimentos para el usuario '{usuario_nombre}':",
        "recomendaciones": alimentos_recomendados
    }
