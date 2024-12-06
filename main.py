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
        if any(enf.lower() in (e.lower() for e in enfermedades_alimento) for enf in enfermedades_usuario):
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
