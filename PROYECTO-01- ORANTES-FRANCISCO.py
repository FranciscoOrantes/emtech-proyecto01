from lifestore_file import lifestore_products as productos
from lifestore_file import lifestore_sales as ventas
from lifestore_file import lifestore_searches as busquedas
import numpy as np
usuario = 'TheMaximusFran'
password = '22021630K'
mayoresVentas=[]
contadorMes = 1
listaIngresosMensuales=[]
ventasPorMes2=[]

def inicioSesion():
    usuarioIntroducido = input('Ingresa tu usuario:')
    passwordIntroducida = input('Ingresa tu contraseña:')
    if usuario != usuarioIntroducido:
        print('USUARIO INCORRECTO, POR FAVOR VUELVA A INGRESAR')
        inicioSesion()
    else:
        if password != passwordIntroducida:
            print('CONTRASEÑA INCORRECTA, POR FAVOR VUELVA A INGRESAR LA CONTRASEÑA')
            inicioSesion()
        else:
            print('INICIO DE SESION CORRECTO')
            ordenarMayoresVentas()


def ordenarMayoresVentas():
    contador = 0
    totalVentas = []
    for producto in productos:
        for venta in ventas:
            if producto[0]==venta[1]:
                contador+=1
        ventasFormato = [producto[1],contador]
        totalVentas.append(ventasFormato)
        contador = 0
    for i in range(len(totalVentas)):
        for j in range(len(totalVentas)):
            if totalVentas[i][1] > totalVentas[j][1]:
                tmp = totalVentas[i]
                totalVentas[i] = totalVentas[j]
                totalVentas[j] = tmp
    for m in range(0,50):
        print('El producto: ',totalVentas[m][0], ' se vendió: ', totalVentas[m][1])

    ordenarMayoresBusquedas()    


def ordenarMayoresBusquedas():
    contador = 0
    totalBusquedas = []
    for producto in productos:
        for busqueda in busquedas:
            if producto[0]==busqueda[1]:
                contador+=1
        busquedasFormato = [producto[1],contador]
        totalBusquedas.append(busquedasFormato)
        contador = 0
    for i in range(len(totalBusquedas)):
        for j in range(len(totalBusquedas)):
            if totalBusquedas[i][1] > totalBusquedas[j][1]:
                tmp = totalBusquedas[i]
                totalBusquedas[i] = totalBusquedas[j]
                totalBusquedas[j] = tmp
    print('-----------------------------------------------------------------------')
    print('\n')
    print('RESULTADOS BUSQUEDAS') 
    print('\n')           
    for m in range(0,10):
        print('El producto: ',totalBusquedas[m][0], ' se buscó: ', totalBusquedas[m][1])    



def ordenarCategorias():
    sumaVentas = 0
    categoria=''
    contador = 0
    totalVentas = []
    formatoCategorias = []
    categorias =[]
    for producto in productos:
        for venta in ventas:
            if producto[0]==venta[1]:
                contador+=1
        ventasFormato = [producto[1],producto[3],contador]
        totalVentas.append(ventasFormato)
        contador = 0
    #print(totalVentas)
    try:
        for i in range(len(totalVentas)):
            categoria = totalVentas[i][1]
            if totalVentas[i+1][1]==categoria:
                sumaVentas = sumaVentas+totalVentas[i][2]
                #print('ENTRO AL 1ER IF')
            else:
                if categoria!=totalVentas[i+1][1]:
                    
                    formatoCategorias=[categoria,sumaVentas]
                  
                    sumaVentas=0
                    categoria=totalVentas[i+1][1]
                
                categorias.append(formatoCategorias)
                   
    except:
        formatoCategorias=[categoria,sumaVentas]
        categorias.append(formatoCategorias)
        pass
    print(categorias)
    
def ordenarProductosMayoresReseñas():
    
    resenasFormato = []
    totalResenas=[]
    nombreProducto =''
    resena = 0
    devolucion = 0
    for producto in productos:
        for venta in ventas:
            if producto[0]==venta[1]:
                nombreProducto = producto[1]
                resena = venta[2]
                devolucion = venta[4]
        resenasFormato = [nombreProducto,resena,devolucion]
        totalResenas.append(resenasFormato)
        
    #print(totalResenas)
    for i in range(len(totalResenas)):
        for j in range(len(totalResenas)):
            if totalResenas[i][1] > totalResenas[j][1] and (totalResenas[i][0]!= totalResenas[j][0]):
                tmp = totalResenas[i]
                totalResenas[i] = totalResenas[j]
                totalResenas[j] = tmp
    imprimirProductosMejoresReseñas(totalResenas)            
def imprimirProductosMejoresReseñas(totalResenas):
    print('-----------------------------------------------------------------------')
    print('\n')
    print('PRODUCTOS CON MEJORES RESEÑAS') 
    print('\n')
    resenasFinales = []
    try:
        while len(resenasFinales)<20:
            for m in range(len(totalResenas)):
                if totalResenas[m][0]!=totalResenas[m+1][0]:
                    resenasFinales.append([totalResenas[m][0],totalResenas[m][1]]) 
                else:
                    pass
    except:
        pass
    for resena in range(0,20):
        print('EL PRODUCTO ',resenasFinales[resena][0], ' tiene una reseña de ', resenasFinales[resena][1])    
        
    
            
    

                   
    


       
            

#PUNTO 3    
def calculoTotalAnual():
    contador = 0
    totalVentas = []
    ingresoAnual = 0
    for producto in productos:
        for venta in ventas:
            if producto[0]==venta[1]:
                contador+=1
        ventasFormato = [producto[1],producto[2],contador]
        totalVentas.append(ventasFormato)
        contador = 0
    #INGRESOS ANUALES
    print('-----------------------------------------------------------------------')
    print('\n')
    print('TOTAL DE INGRESO ANUAL') 
    print('\n')    
    for i in totalVentas:
        ingresoAnual=ingresoAnual+(i[1]*i[2])    
    print(ingresoAnual)
#PUNTO 3 
def calculoIngresosMensuales():
    mes = ''
   
    formatoIngresosMensuales=[]
    ingresosMensuales=[]
    contador= 0
    meses = []
   
    ventasMensuales = []
 
    for producto in productos:
        for venta in ventas:
            if producto[0]==venta[1]:
                mes = venta[3][3:5]
                meses.append(mes)
                contador+=1
        formatoIngresosMensuales = [producto[1],producto[2],meses]
        ingresosMensuales.append(formatoIngresosMensuales)
        contador = 0
        meses = []
    for i in range(len(ingresosMensuales)):
        #print(len(ingresosMensuales[i][2]))
        if len(ingresosMensuales[i][2])>0:
            #print('Entro al if')
            ventasMensuales.append(ingresosMensuales[i])
    #cprint(ventasMensuales)
    ventaMensualCalculo(ventasMensuales,contadorMes)
    ventasPorMes(ventasMensuales,contadorMes)        
#PUNTO 3 
def ventaMensualCalculo(ventasMensuales,contadorMes):
    ingresoMensual = 0
    for i in range(len(ventasMensuales)):
        for mes in ventasMensuales[i][2]:
            if contadorMes<10:
                mesActual ='0'+str(contadorMes)
                if mes==mesActual:
                    ingresoMensual = ingresoMensual + ventasMensuales[i][1]   
            else:
                mesActual= str(contadorMes)
                if mes==mesActual:
                    ingresoMensual = ingresoMensual + ventasMensuales[i][1]
    listaIngresosMensuales.append([mesActual,ingresoMensual])
    contadorMes+=1
    if contadorMes<13:
        ventaMensualCalculo(ventasMensuales,contadorMes)
    else:
        #print(listaIngresosMensuales)   
        print('-----------------------------------------------------------------------')
        print('\n')
        print('TOTAL DE INGRESOS POR MES') 
        print('\n') 
        for ingresoMes in listaIngresosMensuales:
            print('EL MES: ',ingresoMes[0], ' tuvo un ingreso de: $',ingresoMes[1])    
        
def ventasPorMes(ventasMensuales,contadorMes):
    contadorVentas = 0
    for i in range(len(ventasMensuales)):
        for mes in ventasMensuales[i][2]:
            if contadorMes<10:
                mesActual ='0'+str(contadorMes)
                if mes==mesActual:
                    contadorVentas = contadorVentas + 1   
            else:
                mesActual= str(contadorMes)
                if mes==mesActual:
                    contadorVentas = contadorVentas + 1
    ventasPorMes2.append([mesActual,contadorVentas])
    contadorMes+=1
    if contadorMes<13:
        ventasPorMes(ventasMensuales,contadorMes)
    else:
        print('-----------------------------------------------------------------------')
        print('\n')
        print('TOTAL DE VENTAS POR MES') 
        print('\n') 
        for ventasMes in ventasPorMes2:
            print('EL MES: ',ventasMes[0], ' tuvo:',ventasMes[1],'ventas')
        ordenarMesesMayoresVentas(ventasPorMes2)  

def ordenarMesesMayoresVentas(ventasPorMes2):
    for i in range(len(ventasPorMes2)):
        for j in range(len(ventasPorMes2)):
            if ventasPorMes2[i][1] > ventasPorMes2[j][1]:
                tmp = ventasPorMes2[i]
                ventasPorMes2[i] = ventasPorMes2[j]
                ventasPorMes2[j] = tmp
    print('-----------------------------------------------------------------------')
    print('\n')
    print('MESES CON MAYORES VENTAS') 
    print('\n')           
    for m in range(0,6):
        print('El mes: ',ventasPorMes2[m][0], 'tuvo un total de ventas de: ', ventasPorMes2[m][1])            




    

               
            
                
            


def main():
    ordenarProductosMayoresReseñas()

if __name__ == "__main__":
    main()