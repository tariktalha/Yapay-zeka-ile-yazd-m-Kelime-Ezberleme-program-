import random
from english_words import english_words
from turkish_words import turkish_words

def main():
    correct_count = 0
    wrong_count = 0
    question_number = 0

    # Kullanıcıya hangi dili soracağını seçtirme
    while True:
        choice = input("Hangi dili sormak istersiniz? (İngilizce için 'e', Türkçe için 't' girin): ").lower()
        if choice in ['e', 't']:
            break
        else:
            print("Geçersiz seçim. Lütfen 'e' veya 't' girin.")

    # Kelimelerin indekslerini karıştırın
    indices = list(range(len(english_words)))
    random.shuffle(indices)

    num_questions = len(indices)

    for i in indices:
        question_number += 1
        english_word = english_words[i]
        turkish_word = turkish_words[i]

        print(f"\nSoru {question_number}/{num_questions}:")
        if choice == 'e':
            print(f"'{english_word}' kelimesinin Türkçe karşılığı nedir?")
            user_answer = input("Türkçe karşılığını giriniz: ")

            if user_answer.lower() == turkish_word.lower():
                print("Doğru!")
                correct_count += 1
            else:
                print(f"Yanlış! Doğru cevap '{turkish_word}' olacaktı.")
                wrong_count += 1
        else:
            print(f"'{turkish_word}' kelimesinin İngilizce karşılığı nedir?")
            user_answer = input("İngilizce karşılığını giriniz: ")

            if user_answer.lower() == english_word.lower():
                print("Doğru!")
                correct_count += 1
            else:
                print(f"Yanlış! Doğru cevap '{english_word}' olacaktı.")
                wrong_count += 1

    print("\nİstatistikler:")
    print(f"Doğru cevap sayısı: {correct_count}")
    print(f"Yanlış cevap sayısı: {wrong_count}")
    print(f"Toplam soru sayısı: {num_questions}")

if __name__ == "__main__":
    main()

