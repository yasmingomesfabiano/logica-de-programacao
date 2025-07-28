def estado_luz(status):
    match status:
        case "luz ligada":
            return "on"
        
        case "luz desligada":
            return "off"
        
        case "luz piscando":
            return "blink"
        
        case _:
            return "Erro!"
        
estado=input("informe o estado da sua luz(luz ligada, luz desligada ou luz piscando): ")
resultado= estado_luz(estado)
print(resultado)