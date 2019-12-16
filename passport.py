class Passport:
    nom = ""
    prenom = ""
    nationalite = ""
    num_passport = ""
    date_naissance = ""
    date_exp = ""
    
    def __init__(self, nom, prenom, nationalite, num_passport, date_naissance, date_exp):
        self.nom = nom
        self.prenom = prenom
        self.nationalite = nationalite
        self.num_passport = num_passport
        self.date_naissance = date_naissance
        self.date_exp = date_exp
