planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Neptune']
print('Mercurys' in planets for planet in planets)
print(planets.index("Neptune"))
for planet in planets:
    if planet in planets:
        print(True)