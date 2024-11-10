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
