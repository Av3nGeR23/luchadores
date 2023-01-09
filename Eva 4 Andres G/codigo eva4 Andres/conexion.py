#--------------------------------------------------------Modulo: Conexión

import mysql.connector

def conex():
    try:
        myconn = mysql.connector.connect(host="localhost", user="AndresG", passwd="Andres23$%", database="luchadores")
        
    except:
        # registrar un log...1
        print("Error")
    return myconn

#--------------------------------------------------------modulo: Clase gladiador

class gladiador():
    Vida = ''

    def Lucha(self, pelea):
        self.p = pelea

        return """EL gladiador {} puede Luchar""".format(self.p)

    def modificar_atributos(self, valor1):
        self.v = valor1
        gladiador.Vida = self.v

        return valor1


#pe = gladiador()
#print(pe.Lucha('Sí'))
#print('El atributo inicial de la clase es: ',pe.Vida)
#print('El atributo modificado de la clase es: ',pe.modificar_atributos(100))



#--------------------------------------------------------Modulo CRUD
import traceback

def insertarBD(Vida, Lucha):

    sql = 'insert into gladiador (Vida, Lucha) values (%s, %s)'

    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql,(Vida,Lucha))
        conexion.commit()
        fila = cursor.rowcount
        if fila>0:
            print('Datos ingresados OK')
        else:
            print('No se insertan valores')    

    except:
        print(traceback.print_exc())


def listar():

    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute('select Vida, Lucha from gladiador ')
        result = cursor.fetchall()
        conexion.close()

    except:
        print('Error')
    
    return result

def eliminar(Vida):
    sql_eliminar = "delete from gladiador where Vida = %s"
    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql_eliminar,(Vida,))
        conexion.commit()
        filas = cursor.rowcount
        conexion.close()
        
        if filas > 0:
            return filas
        else:
            return print('No hay registros con ese peleador')

    except:
        print("Error")


#--------------------------------------------------------Modulo: Login

import hashlib
import pwinput
class Encoder:

    def encode(self, string):

        result = hashlib.md5(string.encode())
        return result.hexdigest()

    def decode(self, string, claveMD5):

        if hashlib.md5(string.encode()).hexdigest() == claveMD5:
            return True
        else:
            return False

def ingresarUsuario():
    sql = "insert into usuarios (user, password) values (%s,%s)"
    conexregistro = conex()
    try:
        user = input('Registre un usuario: ')
        clave = pwinput.pwinput('Ingrese password: ')
        clave = Encoder().encode(clave)
        cursor = conexregistro.cursor()
        cursor.execute(sql,(user, clave))
        conexregistro.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Datos ingresados OK")
        else:
            print("no hubo cambios")
    except:
        print(traceback.print_exc())
    

def validarLogin():
    username = input("Ingrese nombre de usuario : ")
    clave = pwinput.pwinput('Ingrese password: ')
    resultado = buscarUsuarioClave(username, clave)
    print(resultado)
    return resultado
    


def buscarUsuarioClave(username, clave):
        clave = Encoder().encode(clave)
        sql = "select user, password from usuarios where user = %s and password = %s"
        resultado = None
        conexionuser = conex()
        try:
            cursor = conexionuser.cursor()
            cursor.execute(sql, (username, clave))
            resultado = cursor.fetchone()

        except:
            print(traceback.print_exc())
        
        return resultado

def inicioSesion():
    intentos = 1
    print("Bienvenido al sistema de Eva 3")
    while intentos <= 3:
        resu = validarLogin()
        if resu is not None:
            print(f"Bienvenido(a) Sr(a). : {resu[0]}")
            
            break
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1

#--------------------------------------------------------Modulo de los JSON
import json

def prepararExportarJson():
        lista = []
        lista2 = []
        dic={}
        c = conex()

        try:
            cursor = c.cursor()
            cursor.execute("select Vida, Lucha from gladiador")
            result = cursor.fetchall()
            ## convierte filas en objetos

            for u in result:
                gladiador = (u[0],u[1])
                lista.append(gladiador)
            
            for w in lista:
                lista2.append({'Vida':w[0], 'Lucha':w[1]})
                dic['Datos'] = lista2                
            
            print("Exportación OK")

            exportargladiadores("gladiadores2.json", dic)
            #datos_json = json.dumps(lista)
            #print('esto contiene',datos_json)    

        except Exception as ex:
            # connection.myconn.rollback()
            print(ex)
        #print('prepararExportarJson')    
        return lista

#print(prepararExportarJson())

def exportargladiadores(archivo, obj):
    resu={}
    try:
        out_file = open(archivo, "w", encoding="utf-8")
        json.dump(obj, out_file, indent=4)
        out_file.close()
        resu["mensaje"] = "Datos exportados satisfactoriamente"

    except Exception as ex:
        resu["Error"] = ex

#exportargladiadores('gladiadores.json',prepararExportarJson())

#####Importar
def leerJson():
    ruta2 = 'gladiadores2.json'
    with open(ruta2) as file:
        data = json.load(file)
        #print(data)
        
        for y in data['Datos']:
            print(y)

#leerJson()

def importargladiadoresJson():
    lista=[]
    
    try:
        ruta2 = 'gladiadores2.json'
        with open(ruta2) as file:
            data = json.load(file)
        #print(data)
        
        for x in data['Datos']:
            lista.append((x["Vida"],x["Lucha"]))       
                
        sql = "insert into gladiador (Vida, Lucha) values (%s,%s)"
        conexion = conex()
        cursor = conexion.cursor()
        cursor.executemany(sql, lista)
        conexion.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Datos agregados satisfactoriamente")

        else:
            print("No se realizaron cambios")

    except Exception:
        print("Error al insertar json")

#--------------------------------------------------------Modulo: Menú

class Menu():
    op= int(input('''Ingrese opcion :
                    1- Registrar Usuario
                    2- Login
                    '''))
    if op == 1:
        ingresarUsuario()
        inicioSesion()
    elif op==2:
        inicioSesion()

    while True:
        print('')
        print('****** MENU GLADIADORES ******')
        print('')
        print('Opcion 1 Agregar gladiadores')
        print('Opcion 2 Listar datos')
        print('Opcion 3 Eliminar')
        print('Opcion 4 Leer Archivos Json')
        print('Opcion 5 Importar a Json')
        print('Opcion 6 Exportar a Json')    
        print('Opcion 0 Para Salir')

        opcion = input('\ningrese la opcion:')
        print('')

        if opcion == '1':
            print('Se agregaran gladiadores')
            v = int(input('Ingrese la Vida del gladiador: '))
            r = input('puede Luchar? ')
            p = gladiador()
            p.modificar_atributos(v)
            p.Lucha(r)
            insertarBD(p.modificar_atributos(v),p.Lucha(r))
        
        elif opcion == '2':
            print('Se listarán los gladiadores')

            for p in listar():
                print(p)

        elif opcion == '3':
            print('Eliminar gladiadores')
            a = input('Ingrese la Vida del gladiador que quiere eliminar: ')
            p = gladiador()
            p.Lucha(a)
            eliminar(p.Lucha(a))
        
        elif opcion == '4':
            print('Leer datos de JSON existentes')
            leerJson()

        elif opcion == '5':
            print('Vamos a importar desde un JSON hacia la BD')
            importargladiadoresJson()

        elif opcion == '6':
            print('Vamos a exportar a JSON')
            prepararExportarJson()
        
        elif opcion == '0':
            print('Hasta pronto')
            break
            
        else:
            print('Opción no válida')
        
        


