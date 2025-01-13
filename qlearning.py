
import random

def click_btn():
    pass

def click_link():
    pass

def input_text():
    pass

# Définir une liste d'états, dans notre cas, une liste d'adresses cibles par exemple
states = ['http://127.0.0.1:5000/', 'http://127.0.0.1:5000/welcome', 'http://127.0.0.1:5000/welcome?identifier=ds']
# Définir une liste d'actions possibles, dans notre cas, cliquer sur un bouton donné, ou cliquer sur un lien
actions = [click_btn, click_link, input_text]
# Pour chaque état obtenu, affecter une récompense. Si on cherche à atteindre une page en particulier, donner un nombre de points positifs, et pour les autres adresses, des points négatifs
rewards = {states[0]: 0, states[1]: 0, states[2]: 10}

# Initialiser le dictionnaire avec uniquement des zéros
# Dans ce dicitionnaire, pour chaque état, pour chaque action, un score est associé, ici tous les scores sont à zéro.
Q = {}
for state in states:
    score_actions = {action.__name__:0 for action in actions}
    Q[state] = score_actions

print(Q)

# Définir les hyperparamètres suivants
alpha = 0.1 # taux d'apprentissage
gamma = 0.9 # rapprocher gamma de 1 si nous avons beaucoup d'états, sinon, le rapprocher de 0
epsilon = 0.2 # exploration probability compris entre 0 et 1
num_episodes = 30

exit()

# Créer une fonction dont l'objectif est de choisir une action en suivant la stratégie epsilon-greedy
# choisir une valeur aléatoire comprise entre 0 et 1
# si < epsilon, se lancer dans l'exploration, c'est à dire à choisir une action au hasard
# si >= epsilon, se lancer dans l'exploitation, c'est à dire choisir l'action avec le plus grand score dans la Q-Table pour l'état en cours
# cette fonction renvoie donc une action
def choose_action(state):
    next_action = None
    destiny = random.random()
    if destiny < epsilon:
        next_action = random.choice(actions)
    else:
        next_action = max(Q[state], key=lambda item: item.get) # choisir l'action permettant d'obtenir le meilleur score
    return next_action

# créer une fonction qui va renvoyer l'état attendu pour une action donné
# créer un comportement par défaut qui choisit un état au hasard si l'action ne correspond à aucune prévue
# renvoyer un tuple prochain_état, récompense
def step(state, action):
    pass

# Définir une fonction qui doit mettre à jour la Q-Table selon l'équation dite de Bellman
# L'équation de Bellman permet de mettre à jour pour une action et un état donné en paramètre son nouveau suivant la formule : (1 - alpha) * Q_s-1 + alpha * (reward + gamma * max(Q_s))
def update_Q(state, action, reward, next_state):
    pass

# Run the Q-learning algorithm for a fixed number of episodes
# Pour terminer, entrainer notre Q-Table sur un nombre fixe d'épisodes
for _ in range(0):
    pass
    # Initialiser la navigation à un état aléatoire

    # Réaliser autant d'itérations tant que l'état cible n'est pas atteint
    # A chaque itération
    ## choisir une action avec la fonction choose_action
    ## obtenir la prochaine étape et la récompense de l'état en cours avec la fonction step
    # mettre à jour la Q-Table avec toutes ces valeurs récupérées
    #driver.quit()


# Utiliser ensuite la Q-Table obtenue pour prendre des décisions dans les futures interactions avec la page web
# Pour une interaction donnée, toujours choisir l'action avec la Q-Value la plus élevée
