import secrets
import string

def main():
    paramettre = input('Quelle taille voulait vous qu\'il fait ?')
    if not paramettre:
        print("Aucune taille")
        return
    try:
        taille = int(paramettre)
    except ValueError:
        print("Taille invalide")
        return
    if taille < 1:
        print("Taille invalide")
        return
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = ''.join(secrets.choice(chars) for _ in range(taille))
    print(password)
if __name__ == "__main__":
    main()