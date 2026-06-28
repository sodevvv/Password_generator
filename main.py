import secrets
import string

def main():
    paramettre = input("Quelle taille voulez-vous ? ")
    if not paramettre:
        print("Aucune taille")
        input("Appuie sur Entrée pour quitter...")
        return
    try:
        taille = int(paramettre)
    except ValueError:
        print("Taille invalide")
        input("Appuie sur Entrée pour quitter...")
        return
    if taille < 1:
        print("Taille invalide")
        input("Appuie sur Entrée pour quitter...")
        return

    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = ''.join(secrets.choice(chars) for _ in range(taille))
    print("Mot de passe :", password)
    input("Appuie sur Entrée pour quitter...")
if __name__ == "__main__":
    main()
