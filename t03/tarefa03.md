#  ORM
---------------

É uma técnica de desenvolvimento que usa bancos de dados relacionais para reduzir a resistência à programação orientada a objetos. As tabelas de banco de dados são representadas por classes e os registros em cada tabela são representados como instâncias da classe correspondente.

## Python Peewee
-----
Peewee é um ORM projetado para criar e gerenciar tabelas de banco de dados relacionais por meio de objetos Python. O Peewee é adequado para o pequeno porte médio e se destaca por sua simplicidade mais média em comparação com outros ORMs como SQLAlchemy. Uma analogia que os autores da API usam e que acho muito interessante é que o Peewee está para o SQLAlchemy o que o SQLite está para o PostgreSQL.
-----------------------------

# ODBC
----------
ODBC (Open Database Connectivity) é um padrão para acessar sistemas de gerenciamento de banco de dados (DBMS). O padrão define um conjunto de interfaces que permitem acessar diversos bancos de dados utilizando linguagens de programação como Visual Basic, Delphi, Visual C++, Java, etc. Capacidade de usar essas interfaces sem exigir métodos específicos de acesso ao código.

O ODBC alcança a independência do banco de dados usando o driver como a camada de tradução entre o aplicativo e o DBMS. O aplicativo utiliza funções ODBC por meio do gerenciador de driver ODBC ao qual está vinculado, e o driver passa a consulta para o SGBD.

A implementação de um aplicativo baseado em ODBC permite que você use MySQL, Access e SQL Server simultaneamente sem alterar a camada de dados. O uso dessas interfaces depende da existência de um driver ODBC específico para o banco de dados que está sendo acessado.

A maioria dos bancos de dados vem com drivers ODBC, então você provavelmente pode usar um desses drivers junto com uma interface ODBC Python para conectar seu aplicativo Python a qualquer banco de dados no mercado.
