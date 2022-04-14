import pickle
class Arquivo(object):
    def __init__(self, modelo):
        self.modelo = modelo
        print("Criando objeto para salvar e carregar objeto python com pickle.")

    def save_model(self, nome_do_arquivo: str):
        with open(nome_do_arquivo + ".pkl", "wb") as arquivo:
            pickle.dump(self.modelo, arquivo)
        print("Salvando o modelo em um arquivo pickle.")

    def load_model(self, nome_do_arquivo: str):
        with open(nome_do_arquivo + ".pkl", "rb") as arquivo:
            modelo = pickle.load(arquivo)
        print("Carregando o modelo de um arquivo pickle.")
        return modelo