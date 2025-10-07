#### Exercicio 1

Explicación  Vamos a comezar aprendendo a **utilizar un resolutor** como pode ser `dig` para resolver diferentes dominios.

1. Utiliza `dig` para resolver o nome de dominio `www.google.com`

. **Realiza capturas** da saída da execución do comando.
![image-20251007141958325](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251007141958325.png)

Utiliza `dig` para resolver o nome de dominio `www.google.es`

. **Realiza capturas** da saída da execución do comando.

![image-20251007142020988](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251007142020988.png)

Utiliza `dig` para resolver o nome de dominio `google.com`

. **Realiza capturas** da saída da execución do comando.

![image-20251007142049537](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251007142049537.png)

Utiliza `dig` para resolver o nome de dominio `xunta.gal`

. **Realiza capturas** da saída da execución do comando.

![image-20251007142150818](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251007142150818.png)

Utiliza `dig` para resolver o nome de dominio `edu.xunta.gal`

. **Realiza capturas** da saída da execución do comando.
![image-20251007142205267](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251007142205267.png)

Utiliza `dig` para resolver o nome de dominio `www.youtube.com`

1. . **Realiza capturas** da saída da execución do comando.
   ![image-20251007142247258](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251007142247258.png)

------

#### Exercicio 2

Explicación Nesta tarefa vamos a **crear o noso propio servidor DNS** para poder engadir rexistros. Para levantalo servizo utilizaremos Docker. Nos equipos da aula está instalado.

1. Descarga o seguinte [ficheiro](https://dapw-03-servizo-dns-97d5d1.gitlab.io/97tarefas/t03_01/docker-compose.yaml).
2. Sitúate no terminal no directorio onde ter almacenado dito ficheiro. Executa `docker compose up`

1. .

> Cando remates a tarefa preme `Ctrl + C`

 e a continuación ``docker compose down`. Para proseguir ca tarefa volve executar `docker compose up`. Sempre debes facelo no directorio onde se atopa o ficheiro `

> docker-compose.yaml`.

1. Nun navegador web, utiliza a URL `localhost:5380`

 para acceder a interface web que xestiona o servidor DNS.

Introduce de contrasinal de administrador `abc123.`

. O nome de usuario administrador será sempre `admin`.

Vamos a comprobar que funciona. Para iso engade no comando de `dig` `@localhost`

. Con isto estás indicando que en lugar de resolver cara o servidor DNS  que está configurado no equipo, o fas cara o servidor DNS de `localhost`. Neste caso é o servidor DNS que creamos. Polo tanto resolve o dominio de `www.google.com`

1. . **Realiza capturas** da saída da execución do comando.

Explicación  Neste último comando, pedímoslle ao noso servidor que resolvera `www.google.com`

. O noso servidor como non é un servidor autoritario da zona `google.com`

 fixo unha consulta recursiva para dar resolto dito nome. A continuación vamos **crear unha zona directa que o noso servidor poida resolver**.

1. Na interface web do servidor DNS, vaite a `Zones` e preme no botón `Add Zone`

.

Engade a zona `iniciais.gal`

1.  como zona primaria.
2. **Realiza unha captura** onde se vexa na interface web a zona creada.
3. Comezaremos creando rexistros `A` da seguinte táboa:

| nome                                         | IP         |
| -------------------------------------------- | ---------- |
| [www.iniciais.gal](https://www.iniciais.gal) | 10.0.0.101 |
| db.iniciais.gal                              | 10.0.0.102 |
| sftp.iniciais.gal                            | 10.0.0.103 |

1. Con `dig` resolve estes tres rexistros. **Realiza capturas** da saída da execución dos comandos.

Explicación Imaxinemos agora que a nosa web atópase na IP 10.0.0.101 que é onde apunta o nome `www.iniciais.gal`

. Pero queremos que tamén se poida acceder a web con outros nomes como `es.iniciais.gal` ou `en.iniciais.gal`

. Poderiamos engadir outros dous rexistros `A`. Se nalgún momento tiveramos que migrar o servidor web (algo bastante habitual) entón teriamos que modificar os tres rexistros `A` pola nova IP. Nestes casos o mellor é utilizar os **rexistros `CNAME`**.

1. Engade un rexistro `CNAME` para `es.iniciais.gal`

 e `en.iniciais.gal` que apunte a `www.iniciais.gal`

1. .
2. Fai a resolución con `dig` destes nomes de dominio. **Realiza capturas** da saída da execución dos comandos.

Explicación Xeralmente cando nun navegador web introducimos un nome de dominio,  este automaticamente mostra o contido da web. Por exemplo, se poñemos `google.com`

 este xa nolo traduce por `www.google.com`

. Vamos facer o mesmo pero para o noso dominio. Teremos que utilizar o **rexistro `ANAME`** para este caso.

1. Fai a resolución con `dig` do nome `iniciais.gal`

. Verás que non che resolve con ningunha IP. **Realiza capturas** da saída da execución dos comandos.

Engade un novo rexistro `ANAME` pero no nome escribe o símbolo `@`. Este tradúcese polo nome da zona, neste caso `iniciais.gal`

. Fai que apunte a `www.iniciais.gal`

.

Fai a resolución con `dig` do nome `iniciais.gal`

1. . **Realiza capturas** da saída da execución dos comandos.

Cando estás despregando unha aplicación web (por exemplo en Let’s Encrypt), é común que o provedor te pida engadir un rexistro `TXT` no DNS para verificar que es o propietario do dominio antes de que  permitan enlazar a túa aplicación con ese dominio. Vamos ver un exemplo  de como engadir este tipo de rexistro.

1. Engade un rexistro `TXT` para o nome `_acme-challenge.www.iniciais.gal`

 co valor `x8FsezU9-8FwGz3gABX6JcRQ8hX8K4sNzyEaD9xRZpA`

.

Resolve este nome de dominio. Recorda utilizar `dig TXT ...`

1.  para realizar a consulta deste tipo de rexistros  **Realiza capturas** da saída da execución dos comandos.

Explicación Os rexistros **`CNAME` tamén permiten resolver cara dominios de outra zona**. Isto é moi habitual. En moitos servizos de Cloud se che proporcionan  unha máquina virtual non che indican a súa IP, senón que che din o seu  nome (isto realizase para esquivar o problema de falta de IPs públicas). Polo tanto se eu levanto unha aplicación nesa máquina virtual, terei  que apuntar cara ese nome que me proporcionaron cun rexistro `CNAME`.

1. Engade un rexistro `CNAME` para `search.iniciais.gal`

 que apunte a `www.google.com`

.

Fai a resolución con `dig` destes nomes de dominio. **Realiza capturas** da saída da execución dos comandos.
