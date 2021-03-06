"""Module Gobblet

Attributes:
    GOBBLET_REPRÉSENTATION (dict): Constante représentant les gobblet des joueurs.

Functions:
    * interpréteur_de_commande - Génère un interpréteur de commande.
    * formater_un_gobblet - Formater la représentation graphique d'un Gobblet.
    * formater_un_joueur - Formater la représentation graphique d'un joueur et de ses piles.
    * formater_plateau - Formater la représentation graphique d'un plateau.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
from argparse import ArgumentParser

# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: ["▫", "◇", "◯", "□"],
    2: ["▪", "◆", "●", "■"],
}


def interpréteur_de_commande():
    """Interpreteur de commande

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut IDUL représentant l'idul du joueur
                   et l'attribut lister qui est un booléen True/False.
    """
    parser = ArgumentParser(description="prend l'IDUL du joueur")

    parser.add_argument('-l','--lister', dest='IDUL', type=int, help="Lister les parties existantes")

    return parser.parse_args()


def formater_un_gobblet(gobblet):
    """Formater un Gobblet

    Args:
        gobblet (list): liste vide ou de 2 entier [x, y] représentant le Gobblet

    Returns:
        str: Représentation du Gobblet pour le bon joueur
    """
    if not gobblet:
        return '   '

    return (f' {GOBBLET_REPRÉSENTATION[gobblet[0]][gobblet[1]]} ')


def formater_un_joueur(joueur):
    """Formater un joueur

    Args:
        joueur (dict): dictionnaire contenant le nom du joueurs et ses piles de Gobblet

    Returns:
        str: Représentation du joueur et de ses piles de Gobblet
    """
    return (f'{joueur["nom"]}: {formater_un_gobblet(joueur["piles"][0])} {formater_un_gobblet(joueur["piles"][1])} {formater_un_gobblet(joueur["piles"][2])}')


def formater_plateau(plateau):
    """Formater un plateau

    Args:
        plateau (list): plateau de jeu 4 x 4

    Returns:
        str: Représentation du plateau avec ses Gobblet
    """
    return (
        f"3{formater_un_gobblet(plateau[0][0])}|{formater_un_gobblet(plateau[0][1])}|{formater_un_gobblet(plateau[0][2])}|{formater_un_gobblet(plateau[0][3])}\n"
        f" ───┼───┼───┼───\n"
        f"2{formater_un_gobblet(plateau[1][0])}|{formater_un_gobblet(plateau[1][1])}|{formater_un_gobblet(plateau[1][2])}|{formater_un_gobblet(plateau[1][3])}\n"
        f" ───┼───┼───┼───\n"
        f"1{formater_un_gobblet(plateau[2][0])}|{formater_un_gobblet(plateau[2][1])}|{formater_un_gobblet(plateau[2][2])}|{formater_un_gobblet(plateau[2][3])}\n"
        f" ───┼───┼───┼───\n"
        f"0{formater_un_gobblet(plateau[3][0])}|{formater_un_gobblet(plateau[3][1])}|{formater_un_gobblet(plateau[3][2])}|{formater_un_gobblet(plateau[3][3])}\n"
        f"  0   1   2   3 ")


def formater_jeu(plateau, joueurs):
    """Formater un jeu

    Args:
        plateau (list): plateau de jeu 4 x 4
        joueurs (list): list de dictionnaire contenant le nom du joueurs et ses piles de Gobblet

    Returns:
        str: Représentation du jeu
    """
    a = max(len(joueurs[0]["nom"]) + 13, len(joueurs[1]["nom"]) + 13)
    
    return ("0   1   2 ".rjust(a) + "\n"
            + formater_un_joueur(joueurs[0]).rjust(a) + "\n"
            + formater_un_joueur(joueurs[1]).rjust(a) + "\n\n"
            + formater_plateau(plateau))


def formater_les_parties(parties):
    """Formater une liste de parties

    L'ordre doit être exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """
    res = ""
    j = 1
    for i in parties:
        res += f"{j} : {i['date']}, {i['joueurs'][0]} vs {i['joueurs'][1]}\n"
        j += 1

    return (res)


def récupérer_le_coup():
    """Récupérer le coup

    Returns:
        tuple: Un tuple composé d'un origine et de la destination.
               L'origine est soit un entier représentant le numéro de la pile du joueur
               ou une liste de 2 entier [x, y] représentant le Gobblet sur le plateau
               La destination estune liste de 2 entier [x, y] représentant le Gobblet
               sur le plateau

    Examples:
        Quel Gobblet voulez-vous déplacer:
        Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 0
        Où voulez-vous placer votre Gobblet (x,y): 0,1

        Quel Gobblet voulez-vous déplacer:
        Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 2,3
        Où voulez-vous placer votre Gobblet (x,y): 0,1
    """
    coup = [tuple(input("Donnez le numéro de la pile (p) ou la position sur le plateau (x,y):")), tuple(input("Où voulez-vous placer votre gobelet (x,y):"))]
    return coup
