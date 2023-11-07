dl=float(input("Presión del neumático delantero izquierdo (bar): "))
dr=float(input("Presión del neumático delantero derecho (bar): "))
bl=float(input("Presión del neumático delantero izquierdo (bar): "))
br=float(input("Presión del neumático delantero derecho (bar): "))

presion=2.5
margen=0.2

if dl<presion-margen:
    print("EL NEUMÁTICO DELANTERO IZQUIERDO TIENE LA PRESIÓN BAJA")
elif dl>presion+margen:
    print("EL NEUMÁTICO DELANTERO IZQUIERDO TIENE LA PRESIÓN ALTA")

if dr<presion-margen:
    print("EL NEUMÁTICO DELANTERO DERECHO TIENE LA PRESIÓN BAJA")
elif dr>presion+margen:
    print("EL NEUMÁTICO DELANTERO DERECHO TIENE LA PRESIÓN ALTA")

if bl<presion-margen:
    print("EL NEUMÁTICO TRASERO IZQUIERDO TIENE LA PRESIÓN BAJA")
elif bl>presion+margen:
    print("EL NEUMÁTICO TRASERO IZQUIERDO TIENE LA PRESIÓN ALTA")

if bl<presion-margen:
    print("EL NEUMÁTICO TRASERO DERECHO TIENE LA PRESIÓN BAJA")
elif bl>presion+margen:
    print("EL NEUMÁTICO TRASERO DERECHO TIENE LA PRESIÓN ALTA")
