from flask import Flask, make_response, jsonify, request

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


class Personagem:
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador


personagens = []


@app.route("/characters", methods=["GET"])
def get_personagem():
    response = [vars(personagem) for personagem in personagens]
    # a função 'vars()' puxa apenas os atributos/variaveis. É muito recente.
    return make_response(jsonify(response))


@app.route("/characters", methods=["POST"])
def criar_personagem():
    personagem = Personagem(
        nome=request.json["nome"],
        descricao=request.json["descricao"],
        link_imagem=request.json["link_imagem"],
        programa=request.json["programa"],
        animador=request.json["animador"],
    )
    personagens.append(personagem)

    return vars(personagem)


app.run()
