1. Inicia a máquina virtual `dapw_iniciais_server_01` e conéctate por SSH dende o Visual Studio Code.
2. Sitúate no directorio `home` de `dadmin` e executa o seguinte comando para borrar todo o contido: `rm -R * -f`.

Comezaremos **clonando o respositorio** que contén o proxecto de PHP e **instalaremos as libreíras** necesarias para o correcto funcionamento **do proxecto**.

1. Clona o repositorio `iniciaist0201_1`. A continuación abre o directorio do repositorio en Visual Studio Code.

2. Comproba que non temos o directorio `vendor`. **Realiza unha captura** desta comprobación.

   ![image-20250930140026826](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930140026826.png)

3. Utilizando `Composer` instala tódolos paquetes que necesita o proxecto para funcionar.

4. **Realiza unha captura** do contido do directorio `vendor`.
   ![image-20250930140609682](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930140609682.png)

Se nos fixamos no ficheiro `composer.json` podemos observar que sempre se instalará unha versión maior se existe a que se indica no ficheiro. Realizaremos unhas modificacións pertinentes para que sempre se instale a mesma versión e non ter problemas nun  futuro con incompatibilidades.

1. Elimina o directorio `vendor`. Deste xeito borraremos tódalas librerías instaladas.

2. Modifica o ficheiro `composer.json` para que instale unha versión concreta dos paquetes instalados. **Realiza unha captura** do contido deste ficheiro.
   ![image-20250930140742094](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930140742094.png)

3. Instala tódolos paquetes que se indica no ficheiro `composer.json`. Deberíache saír unha mensaxe similar a seguinte:

   ```txt
   Verifying lock file contents can be installed on current platform.
   Warning: The lock file is not up to date with the latest changes in composer.json. You may be getting outdated dependencies. It is recommended that you run `composer update` or `composer update <package name>`.
   ```

4. Esta mensaxe indícanos que `composer.json` e `composer.lock` non están sincronizados. Se queremos sincronizalos teremos que executar o comando `composer update`.

5. Executa o *script* co seguinte comando `php xerar_alumnos.php` para ver que todo funciona correctamente. **Realiza unha captura** do ficheiro creado por este *script*.
   ![image-20250930140927212](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930140927212.png)

Para evitarnos futuros problemas, **no momento de instalar liberías podemos indicar a versión concreta que desexamos**. Neste caso vamos instalar unha versión antiga do paquete `friendsofphp/php-cs-fixer`. Este paquete é unha ferramenta para formatar e corrixir o estilo do código PHP automaticamente. Ademais é un **paquete de desenvolvemento**, polo que so nese contorno debe ser instalado (nunca se debe instalar nun contorno de produción).

1. Vai a páxina web de `Composer`: https://getcomposer.org/ . Preme en `Browse Packages`. E busca por `php-cs-fixer`. Entra na páxina do paquete que desexamos instalar.
2. Na parte dereita da web, poderedes observar as versións dispoñibles. Instala a penúltima versión. **Realiza unha captura** do comando utilizado para realizar esta instalación. Recorda utilizar a opción `--dev` para que só se instale nun contorno de desenvolvemento.
   `composer require --dev friendsofphp/php-cs-fixer`
3. **Realiza unha captura** do contido do contido do ficheiro `composer.json`.
   ![image-20250930141447955](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930141447955.png)
4. Realiza un `commit` e un `push` para subir o repositorio a GitLab.com.
5. **Realiza unha captura** do repositorio en GitLab.com que se vexa o contido deste.
   ![image-20250930141605882](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930141605882.png)

------

#### Exercicio 2: Reprodución de contorno de desenvolvemento con NPM

Neste exercicio faremos algo similiar ao realizado no exercicio anterior, pero esta vez utilizando `npm` en lugar de `Composer`.

1. Clona o repositorio `iniciaist0201_2`. A continuación abre o directorio do repositorio en Visual Studio Code.
2. Comproba que non temos o directorio `node_modules`. **Realiza unha captura** desta comprobación.
   ![image-20250930141749904](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930141749904.png)
3. Utilizando `npm` instala tódolos paquetes que necesita o proxecto para funcionar.
4. **Realiza unha captura** do contido do directorio `node_modules`.
   ![image-20250930141913062](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930141913062.png)

Se comprobas o ficheiro `package.json` verás que non se indica unha versión concreta dos paquetes. Vamos modificar isto.

1. Borra o directorio `node_modules`. Así eliminamos todos os módulos instalados.
2. Modifica o ficheiro `package.json` para que se instale unha versión concreta. **Realiza unha captura** do contido deste ficheiro.
   ![image-20250930142011207](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930142011207.png)
3. Instala os paquetes que se indican no ficheiro `package.json`.
4. Executa o comando `node index.js` para ver que todo funciona correctamente. **Realiza capturas** da saída da execución do *script*.
   ![image-20250930142040898](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930142040898.png)

Para finalizar veremos como se **instala un paquete de desenvolvemento** nunha versión concreta. Neste caso vamos instalar o paquete `eslint`. Esta é unha ferramenta para analizar e corrixir automaticamente o estilo e os erros potenciais no teu código JavaScript

1. Vai a páxina de `npm` (https://www.npmjs.com/ ). Busca o paquete `eslint` e vaite a súa páxina en `npm`. Preme na lapela de `versions`.
2. Instala a penúltima versión do paquete en modo desenvolvemento. **Realiza captura** do comando utilizado.
   `$ npm install eslint@9.35.0 --save-dev`
3. **Realiza unha captura** do contido do ficheiro `packages.json`.
   ![image-20250930142351688](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930142351688.png)
4. Realiza un `commit` e un `push` para subir o repositorio a GitLab.com.
5. **Realiza unha captura** do repositorio en GitLab.com que se vexa o contido deste.
   ![image-20250930142501640](/home/sanclemente.local/a25davidvm/.config/Typora/typora-user-images/image-20250930142501640.png)
