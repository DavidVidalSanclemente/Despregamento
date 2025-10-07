# T02.03 Servidor de base de datos nun contorno de desenvolvemento

### Presentación da tarefa

Nesta tarefa vamos a **implantar un servidor de base de datos de desenvolvemento**.

Ademais de realizar toda a configuración crearemos tanto un usuario de desenvolvemento como a súa respectiva base de datos.

Por último veremos un **cliente gráfico** co que realizar operacións sobre a base de datos.

### Exercicios

#### Exercicio 1: Instalación do SXBD MariaDB con base de datos de desenvolvemento

> O ideal sería realizar esta mesma tarefa noutra máquina e que esa  máquina funcionara tan só como servidor de base de datos. Se queres  facer unha nova máquina que teña por nome `dapw_iniciais_server_01c` e como nome interno da máquina `iniciais_server_01c`.

1. Inicia a máquina virtual `dapw_iniciais_server_01` e conéctate por SSH dende o Visual Studio Code.

Nos seguintes pasos vamos a **instalar e configurar MariaDB**.

1. Instala na máquina o servidor e cliente de MariaDB.
2. Realiza a configuración de seguridade. A `root` ponlle o contrasinal `abc123.`.
3. Modifica a configuración de MariaDB para poder acceder dende calquera equipo.

Por último vamos crear unha base de datos de proba xunto a un usuario de desenvolvemento:

1. Inicia sesión co cliente de MariaDB co usuario `root`.
2. Crea a base de datos de nome `proba` e dálle acceso ao usuario `iniciais` con contrasinal `abc123.`.
3. Proba dende o terminal da propia máquina virtual a conexión a base de datos. **Realiza capturas** do correcto inicio de sesión con este usuario.
   ![image-20251003090928422](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251003090928422.png)

------

#### Exercicio 2: Configuración de cliente de base de datos en VSC

A continuación imos utilizar un **cliente gráfico**  de  MariaDB para comprobar que temos acceso dende fora da máquina virtual a  base de datos. O noso cliente será unha extensión de Visual Studio Code.

1. Cerra o Visual Studio Code conectado a máquina virtual, pero esta non a apagues.

2. Nun Visual Studio Code no anfitrión, instala a extensión `SQLTools` e `SQLTools MySQL/MariaDB/TiDB Driver`. A primeira é o cliente e a segunda é o *driver* para conectarnos a MariaDB. Se queremos conectarnos a outro sistema  xestor de base de datos, tan só debemos instalar o seu driver. A  primeira extensión funciona do mesmo xeito.

3. Preme na icona da barra esquerda de `SQLTools`.

4. Preme en `Add New Connection` e realiza a conexión. **Realiza capturas** da configuración que realizas

   ![image-20251003091615472](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251003091615472.png)

    para a conexión. Podes probar se está todo correcto premendo en `Test Connection` (para iso pedirá o contrasinal do usuario). Deberás indicar os seguintes datos:

   - Indicar un nome.
   - En `Server address` indicas a dirección IP onde se atopa a base de datos.
   - En `Database` indica o nome da base de datos.
   - En `usernmae` o nome de usuario de desenvolvemento con acceso a base de datos.

5. Garda a conexión premendo en `Save Connection`.

6. No menú da esquerda de `SQLTools` aparecera a nova conexión co nome que indicamos. Preme nela para conectarte.

7. Unha vez conectado, nas iconas do apartado `Connections`, preme no de `New SQL File`. Abrirase un ficheiro no que podemos executar SQL.

8. Crea a táboa `usuarios` co campo `id` como clave primaria e co campo `nome` que sexa texto.

9. Engade un usuario calquera.

10. No apartado de `Connections` preme na conexión co botón dereito e preme en `Refresh`.

11. Preme no despregable da conexión para ver todas as táboas. Sobre a táboa `usuarios` preme no icona da lupa se pasas por encima co rato.

12. **Realiza unha captura** do contido da táboa.
    ![image-20251003093431247](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20251003093431247.png)

13. Pecha a conexión.