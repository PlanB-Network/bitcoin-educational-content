import os

# --- Configuración ---
# Directorio donde se encuentran los subdirectorios (usamos '.' para el directorio actual)
directorio_base = "." 
# El número del primer subdirectorio que fue ELIMINADO (044)
inicio_hueco = 44 
# El número del último subdirectorio que fue ELIMINADO (048)
fin_hueco = 48
# Número del subdirectorio más alto que existía (110)
limite_superior = 110

# La cantidad de carpetas eliminadas (48 - 44 + 1 = 5)
desplazamiento = fin_hueco - inicio_hueco + 1

# --- Lógica del Renombrado ---
print(f"Iniciando el renombrado de carpetas en: {os.path.abspath(directorio_base)}\n")
print(f"El desplazamiento (hueco a cubrir) es de: {desplazamiento} carpetas.")

# Recorrer las carpetas desde el límite superior hacia abajo
# Esto es CRUCIAL para evitar sobrescribir carpetas antes de renombrarlas
for i in range(limite_superior, inicio_hueco - 1, -1):
    # Formato de tres dígitos (ej: 049)
    nombre_antiguo = f"{i:03d}" 
    
    # Nuevo número (ej: 049 - 5 = 044, ¡pero el hueco empieza en 44!)
    # Si i=49, el nuevo número debe ser 45 (porque 44-48 se eliminaron).
    # i - desplazamiento = 49 - 5 = 44. ¡Incorrecto! 
    # El primer nuevo número debe ser inicio_hueco (44) y corresponde al 49.
    
    # La lógica es: si el índice actual (i) es mayor que el último eliminado (fin_hueco),
    # el nuevo índice será i - desplazamiento.
    if i > fin_hueco:
        nuevo_numero = i - desplazamiento
        nombre_nuevo = f"{nuevo_numero:03d}"
        
        ruta_antigua = os.path.join(directorio_base, nombre_antiguo)
        ruta_nueva = os.path.join(directorio_base, nombre_nuevo)

        # Verificar si la carpeta antigua existe antes de intentar renombrar
        if os.path.isdir(ruta_antigua):
            try:
                os.rename(ruta_antigua, ruta_nueva)
                print(f"✅ Renombrado: '{nombre_antiguo}' -> '{nombre_nuevo}'")
            except OSError as e:
                print(f"❌ ERROR al renombrar {nombre_antiguo}: {e}")
        else:
            # Esto puede ser normal si i corresponde a una de las carpetas eliminadas,
            # pero el bucle solo va desde 110 hasta 44. Si 44-48 no existen, esto es correcto.
            if i > fin_hueco:
                print(f"⚠️ Advertencia: La carpeta '{nombre_antiguo}' no existe. Omitiendo.")

print("\n✨ Proceso de renombrado completado.")