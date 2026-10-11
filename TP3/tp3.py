import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    
    # Expressão regular combinada com grupos nomeados para cada token da linguagem
    pattern = re.compile(
        r'(?P<COMENTARIO>#.*)|'
        r'(?P<VARIAVEL>\?[a-zA-Z0-9_]+)|'
        r'(?P<LINGUA>@[a-zA-Z]{2,})|'
        r'(?P<STRING>"[^"]*")|'
        r'(?P<RESERVADA>\bLIMIT\b)|'
        r'(?P<NUMERO>\d+)|'
        r'(?P<CONCEITO>[a-zA-Z_][a-zA-Z0-9_:]*)|'
        r'(?P<DELIM>[\{\}\.])|'
        r'(?P<SKIP>[ \t\r]+)|'
        r'(?P<NEWLINE>\n)|'
        r'(?P<ERRO>.)'
    )
    
    for m in pattern.finditer(input_string):
        tipo = m.lastgroup
        valor = m.group(tipo)
        
        if tipo == 'NEWLINE':
            t = ("NEWLINE", valor, linha, m.span())
            linha += 1
        elif tipo == 'SKIP':
            continue  # Ignorar espaços e tabulações
        elif tipo == 'COMENTARIO':
            continue  # Ignorar comentários
        else:
            t = (tipo, valor, linha, m.span())
            
        reconhecidos.append(t)
        
    return reconhecidos

if __name__ == '__main__':
    query_exemplo = """# Cinema: Filmes de Christopher Nolan
select ?titulo ?ano
where {
?f a dbo:Film .
?f dbo:director ?d .
?d foaf:name "Christopher Nolan"@en .
?f foaf:name ?titulo .
?f dbo:releaseDate ?ano
}
LIMIT 500"""

    for tok in tokenize(query_exemplo):
        print(tok)
