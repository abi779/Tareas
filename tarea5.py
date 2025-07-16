from datetime import date

objeto = {
    "nombre": "abigail",
    "edad": 18,
    "ciudad": "buenos aires",
}
objeto["cumple"]=date(2007,3,5)
hoy = date.today()
objeto["edad"] = (
    hoy.year - objeto["cumple"].year
)
def cumpleHoy(fechaDeHoy,
              fechaDeNacimiento):
    mismoMes = (
        fechaDeHoy.month 
        == fechaDeNacimiento.month
    )
    mismoDia = (fechaDeHoy.day 
                == fechaDeNacimiento.day
    )
    return mismoMes and mismoDia

objeto2 = dict(nombre = "abigail", 
               edad = 18, 
               ciudad = "buenos aires",
               cumple = date(2007,3,5))
listaDeDiccionarios = [
    objeto,
    objeto2,
    {
        "nombre":"abigail",
        "edad":18,
        "ciudad":"buenos aires",
        "cumple":date(2007,3,5),
    
    }
]
print("quien es el primer elemento?",
      listaDeDiccionarios[0]["nombre"])