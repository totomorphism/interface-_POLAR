from flask import Flask, render_template, request, redirect, url_for, session
import cv2
import os


app = Flask(__name__) #on crée une instance de la classe Flask, représente le nom du module
app.secret_key = 'cle_secrete' #pour pouvoir utiliser les sessions


@app.route('/') #on définit une route pour la page d'accueil
def index(): #définit la fonction associée à la route, qui rend le modèle index.html
    return render_template('index.html')

@app.route('/result', methods=['POST']) #définit une route pour la page de résultats qui accepte uniquement les requêtes POST
def result():
    if request.method == 'POST': #pour plus de flexibilité si on enlève le methods=['post'] dans la route, au cas où si on veut utiliser des requetes get
        acquisitions = int(request.form['acquisitions']) #on récup les données mises en input
        exposition_time = float(request.form['exposition_time'])
        
        #ici il faudrait ajouter un chemin qui répertorie toutes les images prises par les caméras
        image_brute= 'static/index.jpeg'
      
        session['acquisitions'] = acquisitions #session pour conserver temporairement des variables et les utiliser dans dautres fonctions
        session['exposition_time'] = exposition_time
        return render_template('result.html', acquisitions=acquisitions, exposition_time=exposition_time, image_brute=image_brute)

# @app.route('/RGB')
# def RGB():

#     acquisitions = session.get('acquisitions',0)
#     exposition_time = session.get('exposition_time',0)
#     return render_template('RGB.html',acquisitions=acquisitions, exposition_time = exposition_time)

# def decompose(image_brute):
#     image_to_decompose = cv2.imread(image_brute)
#     im_R,im_G,im_B = cv2.split(image_to_decompose)
#         # Enregistrer les composantes en tant que fichiers séparés
#     base_path = os.path.dirname(image_brute)
#     decomposed_image_paths = []

#     for i, component in enumerate([im_R, im_G, im_B]):
#         component_path = os.path.join(base_path, f'component_{i}.png')
#         cv2.imwrite(component_path, component)
#         decomposed_image_paths.append(component_path)

#     return decomposed_image_paths

if __name__ == '__main__': #on s'assure que le script est exécuté en tant que main
    app.run(debug=True) #on lance l'appli flask
