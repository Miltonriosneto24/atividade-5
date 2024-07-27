from flask import Flask,jsonify,request
app = Flask (__name__)
livros =  [
    {
        'id': 1,
        'nome': 'O Pequeno Príncipe',
        'escritor': 'Antoine de Saint-Exupéry',
        'ano': 1999,
        'valor': 30
    },
    {
        'id': 2,
        'nome': 'Romeu E Julieta',
        'escritor': 'William Shakespeare',
        'ano': 1996,
        'valor': 120
    },
    {
        'id': 3,
        'nome': 'Dom Quixote De La mancha',
        'escritor':  'Miguel de Cervantes',
        'ano': 1995,
        'valor': 190
    },
    {
        'id': 4,
        'nome': 'A Cabana',
        'escritor':  'William P.',
        'ano': 1994,
        'valor': 111
    },
]   
@app.route ('/livros',methods= ['GET'])
def consultar_livros ():
     return jsonify (livros)

@app.route('/livros/<int:id>',methods=['GET'])
def consultar_livro_por_id(id):
    for livros in livros:
        if livros.get('id')==id:
            return jsonify(livros)
app.run()