# Blog em Django

Este é um projeto de blog simples desenvolvido em Django. O objetivo deste projeto é fornecer uma plataforma básica para a criação e visualização de posts.

## Tecnologias Utilizadas

- **Django**: Um framework web de alto nível que incentiva o desenvolvimento rápido e limpo.
- **SQLite**: Um banco de dados leve e embutido que é usado como o sistema de gerenciamento de banco de dados padrão do Django.
- **HTML/CSS**: Para a estruturação e estilização das páginas do blog.
- **Taildcss**: Ajudando na estilização mais rápida
- **Jazzmin**: Para personalizar o admin de maneira rápida

## Pré-requisitos

Antes de começar, você precisará ter o Python pipenv instalados em sua máquina. Você pode verificar se o Python está instalado executando:

```bash
python --version
```

E para verificar a instalação do Django:

```bash
pipenv --version
```

Se você não tiver o pipenv instalado, pode instalá-lo usando pip:

```bash
pip install pipenv
```

Como Rodar o Projeto
Siga os passos abaixo para rodar o projeto localmente:

Clone o repositório:
```bash

git clone https://github.com/patrikrufino/full_blog-exemplo-django
cd full_blog-exemplo-django
cd back-django
```
Instale as dependências:
```bash
pipenv shell
pipenv install
```

Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

Acesse o blog: Abra seu navegador e vá para http://127.0.0.1:8000/ para ver o blog em funcionamento.

## Endpoinsts:

**Painel Administrativo - (Usuário e senhas: admin):**

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Posts
[http://127.0.0.1:8000/blog](http://127.0.0.1:8000/blog)

Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a MIT License.

Contato
Para mais informações, entre em contato com [patrik.rufino@gmail.com].

# Screenshots:
![image](https://github.com/user-attachments/assets/06985239-0946-4f7e-b4fa-3f09eb9858f3)
![image](https://github.com/user-attachments/assets/1b08df00-be04-41f4-8cb0-e097704d0736)
![image](https://github.com/user-attachments/assets/a0c878c5-3eae-4508-a577-ae31308402e3)


