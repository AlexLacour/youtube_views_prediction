from ml import view_prediction

features = {"channelid": "UC_yP2DpIgs5Y1uWC0T03Chw", "channelname": "Joueur Du Grenier", "datepublished": "2018-02-17", "description": "MERCI DE LIRE ! Nouvel \u00e9pisode de Joueur du grenier sur les jeux vid\u00e9os Harry Potter ! Cet \u00e9pisode a mis beaucoup de temps arriver parce qu'il est assez diff...", "dislikes": 2937, "duration": 2222, "familyfriendly": "True",
            "genre": "Gaming", "imageurl": "https://i.ytimg.com/vi/Ugs9HASX4rA/maxresdefault.jpg", "likes": 318929, "subscribers": 3360000, "tags": ["Joueur du grenier", "bazar du grenier", "Harry potter", "Playstation", "chambre des secret", "Ordre du ph\u00e9nix", "Ecole des sorcier", "Test", "retro gaming"], "title": "Joueur du grenier - HARRY POTTER", "uploaddate": "2018-02-17", "views": 9043229}
data_url = '../data.json'

print(view_prediction(features, data_url))
