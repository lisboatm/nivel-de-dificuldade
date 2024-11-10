## Desafio - O Quão Fácil é...

### Descrição do Problema
O TopCoder decidiu automatizar o processo de atribuição de níveis de dificuldade para problemas de programação. A dificuldade de um problema é determinada apenas com base no comprimento médio das palavras presentes em seu enunciado.

A classificação da dificuldade é baseada na média dos comprimentos das palavras válidas:
- Comprimento médio **≤ 3** → dificuldade de **250 pontos**
- Comprimento médio entre **4 e 5** → dificuldade de **500 pontos**
- Comprimento médio **≥ 6** → dificuldade de **1000 pontos**

#### Definições:
- **Símbolo**: Um conjunto de caracteres delimitado por espaços, ou pelo início ou fim da linha.
- **Palavra**: Um símbolo que contém apenas letras (`a-z`, `A-Z`) e pode terminar com um único ponto (`.`). O ponto, se presente, não é contado no comprimento da palavra.

**Exemplos de palavras válidas**: `"AB"`, `"ab."`

**Exemplos de palavras inválidas**: `"a.b"`, `"a2b."`, `"."`, `"ab.."`

#### Cálculo do Comprimento Médio:
O comprimento médio das palavras é obtido somando o comprimento de todas as palavras válidas e dividindo esse total pelo número de palavras válidas. A divisão é feita como uma divisão inteira. Se não houver palavras válidas, a média é considerada **0**.

### Entrada
A entrada consiste em várias linhas, cada uma contendo o enunciado de um problema (uma string com até 50 caracteres). A entrada termina com o fim de arquivo (EOF).

**Restrições**:
- Cada linha contém entre **1 e 50 caracteres**, incluindo letras (`A-Z`, `a-z`), dígitos (`0-9`), espaços (` `) e pontos (`.`).

### Saída
Para cada linha de entrada, imprima um único número indicando a dificuldade do problema:
- **250** se o comprimento médio das palavras for **≤ 3**
- **500** se o comprimento médio das palavras estiver entre **4 e 5**
- **1000** se o comprimento médio das palavras for **≥ 6**

### Exemplo de Entrada e Saída

#### Entrada:
```
This is a problem statement
523hi.
Implement a class H5 which contains some method.
 no9 . wor7ds he8re. hj..
```

#### Saída:
```
500
250
500
250
```

### Como a Solução Funciona

1. **Dividir a entrada em palavras** usando espaços como delimitadores.
2. **Verificar se cada palavra é válida**:
   - A palavra pode conter apenas letras (`a-z`, `A-Z`) e, opcionalmente, pode terminar com um único ponto (`.`).
3. **Calcular o comprimento total** das palavras válidas e contar o número de palavras.
4. **Calcular o comprimento médio**:
   - Se não houver palavras válidas, a média é zero.
   - Caso contrário, dividir o comprimento total pelo número de palavras válidas (divisão inteira).
5. **Classificar a dificuldade** com base no comprimento médio e imprimir o resultado.

### Implementação em Python

```python
import sys

def is_valid_word(word):
    # Verificar se a palavra contém apenas letras ou termina com um único ponto
    if word.endswith('.'):
        word = word[:-1]  # Remover o ponto final para validação
    return word.isalpha()

def compute_difficulty(sentence):
    words = sentence.split()
    total_length = 0
    valid_words_count = 0

    for word in words:
        if is_valid_word(word):
            valid_words_count += 1
            # Remover o ponto final, se houver, para calcular o comprimento
            if word.endswith('.'):
                total_length += len(word) - 1
            else:
                total_length += len(word)

    # Calcular o comprimento médio (divisão inteira)
    if valid_words_count == 0:
        avg_length = 0
    else:
        avg_length = total_length // valid_words_count

    # Classificar de acordo com o comprimento médio
    if avg_length <= 3:
        return 250
    elif 4 <= avg_length <= 5:
        return 500
    else:
        return 1000

def main():
    for line in sys.stdin:
        line = line.strip()
        if line:
            difficulty = compute_difficulty(line)
            print(difficulty)

if __name__ == "__main__":
    main()
```

### Como Executar
1. Salve o código em um arquivo, por exemplo, `dificuldade.py`.
2. Para testar localmente, crie um arquivo de entrada (`input.txt`) com várias linhas e use o comando:
   ```bash
   python3 dificuldade.py < input.txt
   ```
3. Para submeter ao Beecrowd, certifique-se de que está utilizando o Python 3.11, pois ele é compatível com a plataforma.

### Possíveis Problemas
- **Presentation Error**: Certifique-se de que não há espaços extras ou quebras de linha na saída.
- **Runtime Error**: Verifique se há manipulação correta de strings e divisões por zero.

### Autor
Esse problema foi criado por **TopCoder** e adaptado para o Beecrowd por **Jeferson T.**
