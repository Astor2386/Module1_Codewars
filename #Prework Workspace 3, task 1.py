#Prework Workspace 3, task 1
Friends = {
'Astor': {
'favorite_hobby': 'trading',
'favorite_food': 'pizza'
},
'Cipi': {
'favorite_hobby': 'traveling',
'favorite_food': 'teriyaki stir fry'
},
'Sigma': {
'favorite_hobby': 'plumbing',
'favorite_food': 'spaghetti'
}
}
for Friend, friend_info in Friends.items():
    print("\nFriend: " + Friend)
    favorite_hobby = friend_info['favorite_hobby']
    favorite_food= friend_info['favorite_food']
    print("favorite hobby: " + favorite_hobby)
    print("favorite food: " + favorite_food)