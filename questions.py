import csv
import random

# Lecture du fichier CSV
with open('questions_reponses.csv', 'r') as file:
    reader = csv.DictReader(file)
    questions_reponses = list(reader)

# Variables pour le suivi des résultats
total_questions = 0
total_reponses_correctes = 0
correct_indices = []
incorrect_indices = []

# Boucle pour poser les questions
while total_questions < 10:  # ou le nombre souhaité de questions
    # Mélange aléatoire des questions
    random.shuffle(questions_reponses)

    for i, qr in enumerate(questions_reponses):
        question = qr['question']
        answer = input(question + ' ')
        if answer.lower() == qr['réponse'].lower():
            print('Correct !')
            total_reponses_correctes += 1
            correct_indices.append(i)  # Enregistre l'indice de la question correcte
        else:
            print('Incorrect ! La réponse correcte est :', qr['réponse'])
            incorrect_indices.append(i)  # Enregistre l'indice de la question incorrecte
        total_questions += 1

        if total_questions >= 10:
            break  # Sort de la boucle si le nombre de questions atteint le seuil souhaité

    # Vérification du nombre de questions posées
    if total_questions >= 10:
        break  # Sort de la boucle while si le nombre de questions atteint le seuil souhaité


    # Affichage des résultats partiels après chaque série de questions
    print('--- Résultats partiels ---')
    print('Nombre total de questions :', total_questions)
    print('Nombre de réponses correctes :', total_reponses_correctes)
    print('Nombre d\'erreurs :', total_questions - total_reponses_correctes)
    print('Indices des questions correctes :', correct_indices)
    print('Indices des questions incorrectes :', incorrect_indices)
    print('--------------------------')

    # Réinitialisation des indices pour la prochaine série de questions
    correct_indices = []
    incorrect_indices = []

    # Demande si l'utilisateur souhaite continuer
    response = input('Voulez-vous continuer ? (Oui/Non) ')
    if response.lower() != 'oui':
        break

# Affichage des résultats finaux
print('--- Résultats finaux ---')
print('Nombre total de questions :', total_questions)
print('Nombre de réponses correctes :', total_reponses_correctes)
print('Nombre d\'erreurs :', total_questions - total_reponses_correctes)
print('Indices des questions correctes :', correct_indices)
print('Indices des questions incorrectes :', incorrect_indices)


