# Manifesto: TP1 - Validador de Binários sem "011"
## Autor
* **Nome:** Nuno Rei de Sousa Pinto
* **Identificador:** A110326
* **Fotografia:**
  <img src="https://github.com/user-attachments/assets/4bc9b049-eb44-406d-8fad-c5599ae38f16" width="150" alt="Fotografia do Autor">


---

## Resumo
Trabalho prático focado no desenvolvimento de uma Expressão Regular para validar cadeias binárias que não contêm a substring "011".

A Expressão Regular concebida e utilizada foi `^1*(0|01)*$`:
* `^1*`: Permite qualquer quantidade de `1`s no início da string.
* `(0|01)*$`: Garante que, a partir do primeiro `0`, cada bloco só pode conter no máximo um `1` isolado antes de surgir outro `0` ou a string terminar.

---



## Lista de resultados
*  [Resolução e Casos de Teste em Python (tp1.py)](./tp1.py)
