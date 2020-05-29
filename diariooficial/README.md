![Scrapy](http://scrapy.org/img/scrapylogo.png)

Essa POC tem como objetivo testar, avaliar e documentar os recursos do framework para scraping e crawler chamada `scrapy`.

## Sobre o framework

Scrapy é um framework desenvolvido para uso em python e mantido por [ScrapingHub](https://scrapinghub.com/).
Possui uma estrutura preparada para **`Crawler`** e **`Scraping`**, desta maneira facilita bastante a vida do desenvolvedor.

## Detalhes da POC

Para realização da `POC` foi escolhido realizar o scraping do `Diário Oficial de SP` (`DOSP`).
Para tanto foi utilizado o site do [JusBrasil](https://www.jusbrasil.com.br) para ter acesso aos cadernos do diário.

Foram identificados alguns problemas durante o processo de acesso às páginas, sendo eles:

* Conteúdo do site gerado por javascript dinâmico;
* Bloqueio de acesso para **`Bots`** pelo arquivo Robots.txt do site.

Para resolver o problema de acesso, foi necessário o uso da biblioteca Selenium como **middleware** de acesso às páginas. 
Como o mesmo faz uso de browsers em modo headless (sem interface gráfica) que imita um ser usuário no acesso.
Essa abordagem permitiu o acesso às páginas, mas sacrificou um pouco o desempenho do processamento.

## Fluxo

* O crawler vai percorrer todos os cadernos e páginas de cada caderno;  
* O Spider vai extrair todo o texto de cada página;  
* Após a extração de cada item, o mesmo é armazenado em um banco de dados `MongoDB`.


## Ambiente

Foi utilizado o python3 para desenvolvimento e build em ambiente Linux (**Ubuntu**).   

Também será necessária a instalação do **`Geckodriver (Firefox)`** seguindo os passos abaixo:

1. Faça o download [aqui](https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz).
2. Extrair o conteúdo do pacote. 
`$ sudo tar -xvf geckodriver-v0.21.0-linux64.tar.gz`
3. Mover o arquivo para `/usr/local/bin` com o comando `$ sudo mv geckodriver /usr/local/bin`

Agora abra o terminal na pasta do projeto e execute os comandos abaixo para restaurar as dependências do projeto:
```shell script
$ pip install -r requirements.txt
```

Não esqueça de estar com o ambiente ativado na pasta do projeto!

## Estrutura

Scrapy segue a seguinte arquitetura de projeto:

![](https://doc.scrapy.org/en/latest/_images/scrapy_architecture_02.png)
_Diagrama de arquitetura. Documentação [scrapy.org](https://doc.scrapy.org/en/latest/topics/architecture.html)_

O template de projeto tem a seguinte estrutura de arquivos:

--pasta principal  
----projeto  
------spiders  
--------spider.py   
------\_\_init__.py   
------items.py  
------middlewares.py  
------pipelines.py  
------settings.py  
--scrapy.cfg

Para mais detalhes acessa a documentação oficial do [scrapy](https://doc.scrapy.org/en/latest/index.html)
