from hashlib import sha256


def checkdigest(file):
    """
    Fonction qui permet de calculer le hash d'un fichier
    :param file: le fichier dont on veut calculer le hash
    :return: le hash du fichier
    """
    #ouverture du fichier (binaire)
    f = open(file, 'rb')
    #lecture du fichier
    data = f.read()
    #On renvoie le hash du fichier
    return sha256(data).hexdigest()





