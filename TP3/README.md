# Manifesto: TP3 - Analisador léxico para uma liguagem de query
## Autor
* **Nome:** Nuno Rei de Sousa Pinto
* **Identificador:** A110326
* **Fotografia:**
  <br>
  <img src="https://github.com/user-attachments/assets/4bc9b049-eb44-406d-8fad-c5599ae38f16" width="150" alt="Fotografia do Autor">


---

## Resumo
Este trabalho consiste no desenvolvimento de um analisador léxico (*lexer*) em Python para uma linguagem de queries. O analisador utiliza a função `re.finditer` e grupos nomeados de expressões regulares para identificar e transformar o texto de entrada numa sequência estruturada de tokens.

## Tokens Reconhecidos

O lexer reconhece os seguintes tipos de tokens:

* **COMENTARIO**: Linhas de comentário iniciadas por `#`, que são ignoradas pelo analisador.
* **VARIAVEL**: Identificadores iniciados por `?`, como `?titulo`.
* **LINGUA**: Identificadores de idioma iniciados por `@`, como `@en`.
* **STRING**: Valores textuais delimitados por aspas duplas (`"`).
* **RESERVADA**: Palavras-chave da linguagem, como `LIMIT`.
* **NUMERO**: Valores numéricos inteiros.
* **CONCEITO**: Identificadores de ontologias e termos, como `dbo:Film`.
* **DELIM**: Delimitadores estruturais, como `{`, `}` e `.`.
* **SKIP / NEWLINE**: Espaços em branco e quebras de linha, tratados de acordo com as regras de processamento do lexer.

---



## Lista de resultados
*  [Resolução e Casos de Teste em Python (tp3.py)](./tp3.py)
