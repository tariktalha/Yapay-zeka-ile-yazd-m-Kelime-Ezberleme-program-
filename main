# main.py

import random
from english_words import english_words
from turkish_words import turkish_words

def main():
    correct_count = 0
    wrong_count = 0
    question_number = 0

    # Kelimelerin indekslerini karıştırın
    indices = list(range(len(english_words)))
    random.shuffle(indices)

    num_questions = len(indices)

    for i in indices:
        question_number += 1
        english_word = english_words[i]
        turkish_word = turkish_words[i]

        print(f"\nSoru {question_number}/{num_questions}:")
        print(f"'{english_word}' kelimesinin Türkçe karşılığı nedir?")
        user_answer = input("Türkçe karşılığını giriniz: ")

        if user_answer.lower() == turkish_word.lower():
            print("Doğru!")
            correct_count += 1
        else:
            print(f"Yanlış! Doğru cevap '{turkish_word}' olacaktı.")
            wrong_count += 1

    print("\nİstatistikler:")
    print(f"Doğru cevap sayısı: {correct_count}")
    print(f"Yanlış cevap sayısı: {wrong_count}")
    print(f"Toplam soru sayısı: {num_questions}")

if __name__ == "__main__":
    main()
