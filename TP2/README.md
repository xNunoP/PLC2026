# Manifesto: TP2 - Conversor de MarkDown para HTML
## Autor
* **Nome:** Nuno Rei de Sousa Pinto
* **Identificador:** A110326
* **Fotografia:**
  <br>
  <img src="https://github.com/user-attachments/assets/4bc9b049-eb44-406d-8fad-c5599ae38f16" width="150" alt="Fotografia do Autor">


---

## Resumo
Este script em Python converte sintaxe básica de Markdown para HTML utilizando Expressões Regulares. 

As transformações foram implementadas com padrões específicos para evitar conflitos:
*   **Cabeçalhos:** Uma função dinâmica conta os `#` e gera a tag correta (ex: `<h1>`, `<h2>`).
*   **Bold e Itálico:** Uso de quantificadores preguiçosos (`.*?`) para capturar apenas o texto necessário.
*   **Imagens e Links:** Captura do texto alternativo e URL com grupos (`\1`, `\2`).
*   **Listas Numeradas:** Feito em duas etapas com a flag `(?m)` (multiline):
    1. Transforma as linhas com números em `<li>`.
    2. Agrupa blocos consecutivos de `<li>` dentro de uma tag `<ol>`.
---



## Lista de resultados
*  [Resolução e Casos de Teste em Python (tp2.py)](./tp2.py)
