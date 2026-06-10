import sqlite3

# ==========================
# CRIAR BANCO
# ==========================

def criar_banco():

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    # USUÁRIOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # FUNCIONÁRIOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # EMPRÉSTIMOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        livro TEXT,
        autor TEXT,
        ano TEXT,
        data_emprestimo TEXT,
        data_entrega TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


# ==========================
# USUÁRIOS
# ==========================

def add_user(username, password):

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, password)
    )

    conn.commit()
    conn.close()


def validate_user(username, password):

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    usuario = cursor.fetchone()

    conn.close()

    return usuario


def listar_usuarios():

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username FROM users"
    )

    dados = cursor.fetchall()

    conn.close()

    return dados


# ==========================
# FUNCIONÁRIOS
# ==========================

def add_funcionario(username, password):

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO funcionarios(username,password) VALUES(?,?)",
        (username, password)
    )

    conn.commit()
    conn.close()


def validate_funcionario(username, password):

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM funcionarios WHERE username=? AND password=?",
        (username, password)
    )

    funcionario = cursor.fetchone()

    conn.close()

    return funcionario


# ==========================
# EMPRÉSTIMOS
# ==========================

def cadastrar_emprestimo(
    usuario_id,
    livro,
    autor,
    ano,
    data_emprestimo,
    data_entrega
):

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emprestimos(
        usuario_id,
        livro,
        autor,
        ano,
        data_emprestimo,
        data_entrega,
        status
    )
    VALUES(?,?,?,?,?,?,?)
    """,
    (
        usuario_id,
        livro,
        autor,
        ano,
        data_emprestimo,
        data_entrega,
        "ATIVO"
    ))

    conn.commit()
    conn.close()


def listar_emprestimos_usuario(usuario_id):

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    livro,
    autor,
    ano,
    data_emprestimo,
    data_entrega,
    status
    FROM emprestimos
    WHERE usuario_id=?
    """,
    (usuario_id,)
    )

    dados = cursor.fetchall()

    conn.close()

    return dados


def listar_todos_emprestimos():

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    emprestimos.id,
    users.username,
    emprestimos.livro,
    emprestimos.autor,
    emprestimos.data_entrega,
    emprestimos.status
    FROM emprestimos
    JOIN users
    ON users.id = emprestimos.usuario_id
    """)

    dados = cursor.fetchall()

    conn.close()

    return dados


def registrar_devolucao(id_emprestimo):

    conn = sqlite3.connect("bookflow.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE emprestimos
        SET status='DEVOLVIDO'
        WHERE id=?
        """,
        (id_emprestimo,)
    )

    conn.commit()
    conn.close()


criar_banco()