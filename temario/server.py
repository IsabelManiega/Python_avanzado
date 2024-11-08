# server.py

import socket
 
# Instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Puerto y servidor que debe escuchar
ser.bind(("", 8050))
 
# Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(1)
 
# Instanciamos un objeto cli (socket cliente) para recibir datos
cli, addr = ser.accept()

while True:
    # Recibimos el mensaje, con el metodo recv recibimos datos. Por parametro la cantidad de bytes para recibir
    data = cli.recv(10000)
    # Imprimimos el mensaje que en nos envia el cliente.
    print(data)
    # Si no hay datos que se pare el servidor
    if not data: 
        # Cerramos la instancia del socket cliente y servidor
        cli.close()
        ser.close()        
        print("Conexiones cerradas")
    # Devolvemos el mensaje al cliente
    cli.sendall(b'mensaje recibido')
