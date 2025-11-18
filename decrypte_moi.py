messages_gr3 = {
    "pseudo" : "DebugWoman",
    "messages" : ["Rendez vous au point 8 à midi", "Plan B activer en cas de problème", "Le code maître est 2345"],
    "cryptes" : ["Uhqghc yrxv dx srlqw 1 à plgl", "Sodq E dfwlyhu hq fdv gh sureoèph", " Oh frgh pdîwuh hvw 4567"]
}
def dechiffrement_cesar(chaine):
    """
    Fonction pour décoder un message en code César de déplacement de 3.
    :param chaine: la chaine à déchiffrer
    :return: la chaine déchifrée
    """
    liste_decodee = [""]
    alphabet = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
    alphabet_majuscule = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
    numero = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    caracteres = ["à", "é", "è", "î"]
    for liste in chaine:
        for lettre in chaine:
            if lettre in alphabet:
                index = alphabet.index(lettre)
                index = index - 3
                lettre = alphabet[index]
                liste_decodee.append(lettre)
            elif lettre in numero:
                index = numero.index(lettre)
                index = index - 3
                lettre = numero[index]
                liste_decodee.append(lettre)
            elif lettre in alphabet_majuscule:
                index = alphabet_majuscule.index(lettre)
                index = index - 3
                lettre = alphabet_majuscule[index]
                liste_decodee.append(lettre)
            elif lettre == " ":
                lettre = " "
                liste_decodee.append(lettre)
            elif lettre in caracteres:
                liste_decodee.append(lettre)
    liste_decodee = "".join(liste_decodee)
    return liste_decodee




ligne = (messages_gr3["cryptes"])
message_transmis = dechiffrement_cesar(ligne)
print("Accusé-réception :")
print("Attention, le 3ième message a été intercepté.")
print("Nous accusons réception des messages 1 et 2.")

