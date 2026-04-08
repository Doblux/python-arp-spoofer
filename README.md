> [!IMPORTANT]
> **hay que usar iptables y alterar una ruta del sistema para poder aceptar paquetes entrantes para luego redirigirlos devuelta**

```sh
iptables --policy FORWARD ACCEPT
```
> [!IMPORTANT]
> **tiene que decir 1**
```sh
cat /proc/sys/net/ipv4/ip_forward
```

```sh
echo "1" > /proc/sys/net/ipv4/ip_forward
```
