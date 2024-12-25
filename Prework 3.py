#Prework 3
Friends = {
'Astor': {
'first': 'John',
'last': 'Astor',
'favorite_hobby': 'trading',
'favorite_food': 'pizza'
},
'Cipi': {
'first': 'Cipi',
'last': 'Chang',
'favorite_hobby': 'traveling',
'favorite_food': 'teriyaki stir fry'
},
'Sigma': {
'first': 'Chad',
'last': 'Smith',
'favorite_hobby': 'plumbing',
'favorite_food': 'spaghetti'
}
}
for Friend, friend_info in Friends.items():
    print("\nFriend: " + Friend)
    full_name = friend_info['first'] + " " + friend_info['last']
    favorite_hobby = friend_info['favorite_hobby']
    favorite_food= friend_info['favorite_food']
    print("\tFull name: " + full_name.title())
    print("\tfavorite hobby: " + favorite_hobby)
    print("\tfavorite food: " + favorite_food )
