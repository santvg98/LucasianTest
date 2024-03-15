'''
Un restaurante que se está sistematizando completamente quiere que se le elabore un programa que le imprima una factura de cobro para sus 
clientes teniendo en cuenta que por compras iguales o mayores a $200.000 se le otorgara un descuento del 15%, por compras iguales o superiores a 
$50.000 será un descuento del 2%, por compras iguales o superiores a $20.000 un descuento del 1.5% y por compras inferiores no habrá descuento,
la factura debe llevar el valor del bono de descuento el total a pagar y un agradecimiento al comprador el cual debe ingresar su nombre. 
'''

nombre = input("Por favor, ingrese su nombre: ")
valor_compra = float(input("Por favor, ingrese el valor de su compra: "))


if valor_compra >= 200000:
    descuento = valor_compra * 0.15
elif valor_compra >= 50000:
    descuento = valor_compra * 0.02
elif valor_compra >= 20000:
    descuento = valor_compra * 0.015
else:
    descuento = 0

total_pagar = valor_compra - descuento


print(f"\nFactura de Compra")
print(f"Nombre del comprador: {nombre}")
print(f"Valor de la compra: ${valor_compra}")
print(f"Descuento: ${descuento}")
print(f"Total a pagar: ${total_pagar}")
print("Gracias por su compra!")
