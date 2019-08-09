beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
new_beer = {key:value+value*0.05 for key,value in beer.items()}
print(beer)
print(new_beer)
