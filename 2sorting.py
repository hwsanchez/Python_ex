#using sort witha key:
#Here a list of tuplets of the solar system planets with their radius, density and Astronomical Unit (distance from the Sun)
#The list is ordered by the AU (distance from the Sun)
planets = [
('Mercury', 2440, 5.43, 0.395),
('Venus', 6052, 5.24, 0.723),
('Earth', 6378, 5.52, 1.000),
('Mars', 3396, 3.93, 1.530),
('Jupiter', 71492, 1.33, 5.210),
('Saturn', 60268, 0.69, 9.551),
('Uranus', 25559, 1.27, 19.213),
('Neptune', 24764, 1.64, 30.070)]

# sorting by size (radius):
Name = lambda planet : planet[0]
Size = lambda planet: planet[1]
print('Planets by distance from the Sun:')
for planet in planets:
    print(Name(planet), Size(planet))
print('----------------------------------')
# sorting the list of planets by size:
planets.sort(key=Size, reverse=True)
print('Planets by size:')
for planet in planets:
    print(Name(planet), Size(planet))

print('----------------------------------')
# sorting the list of planets by density:

Density = lambda planet : planet[2]
planets.sort(key=Density, reverse=True)
print('Planets by Density:')
for planet in planets:
    print(Name(planet), Density(planet))
