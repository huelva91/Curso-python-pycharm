# + Tabla persona
# campos: nombre, apellido, email
#
# + Insertar 3 personas
#
# + obtener solo los nombres de todas las personas
#
# + sacar toda la información de las personas que tengas un email *gmail.com
#
# + actualizais a las personas que no tengan un email de gmail con el dominio gmail.com
# sadad@correo.es sadad@gmail.com

from utils.conexiones import get_mysql_conection

try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(id, nombre, apellido, email) VALUES(%s, %s, %s, %s)"
            valores = (
                (1, "Ana", "Gomez", "email1@gmail.com"),
                (2, "Manuel", "Rodriguez", "email2@terra.es"),
                (3, "Daniel", "Castilla", "email3@gmail.com")
            )
            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')

    try:
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = "SELECT nombre FROM persona"
                cursor.execute(sentencia)
                nombres = cursor.fetchall()
                for nombre in nombres:
                    print(nombre)

    except Exception as e:
        print(f'Ocurrió un error: {e}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

    try:
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = "SELECT id, nombre, apellido, email FROM curso_python.persona WHERE email LIKE '%gmail.com'"
                cursor.execute(sentencia)
                nombres = cursor.fetchall()
                for nombre in nombres:
                    print(nombre)

    except Exception as e:
        print(f'Ocurrió un error: {e}')

    try:
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = "SELECT id, nombre, apellido, email FROM curso_python.persona WHERE email LIKE '%gmail.com'"
                cursor.execute(sentencia)
                nombres = cursor.fetchall()
                for nombre in nombres:
                    print(nombre)

    except Exception as e:
        print(f'Ocurrió un error: {e}')

