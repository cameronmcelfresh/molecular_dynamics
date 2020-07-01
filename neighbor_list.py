import random
import time

positions = []
cut_off_distance=2
num_particles = 100
total_iterations = 10000

#Create a list of random particle positions
for i in range(num_particles):
  
  while True:
    rand_pos = round(random.uniform(0, 25), 3) #make sure not to add them in the same place

    if not(rand_pos in positions):  
      positions.append(rand_pos) #pick a random position between 0-25
      break
      
##################################
## Aproach 2 - without neighbor list
##################################

#Begin "brute force" calculation of the forces
brute_start = time.perf_counter()

for iter in range(total_iterations):

  for i in range(num_particles): #loop through all particles
    for j in range(num_particles): #loop through the rest of the particles
      if i==j:
        continue #skip any self-forces

      if abs(positions[i]-positions[j])<cut_off_distance:
        F = 10/(positions[i]-positions[j]) #arbitrary stand-in of force calculation

brute_end = time.perf_counter()


##################################
## Aproach 2 - with neighbor list
##################################

neighbor_list = []

#Begin calculation of the forces using a neighbor list
neighbor_start = time.perf_counter()

for iter in range(total_iterations):

  #Update the neighbor list every 10 iterations
  if iter%10==0:
    neighbor_list = []
    for i in range(num_particles): #loop through all particles

      a_list = []

      for j in range(num_particles): #loop through the rest of the particles
        if i==j:
          continue #skip any self-forces

        if abs(positions[i]-positions[j])<cut_off_distance:
          a_list.append(j)

      neighbor_list.append(a_list.copy())

  for i in range(num_particles): #loop through all particles
    for neighbor in neighbor_list[i]: #go through each particle in its neighbor list
      F = 10/abs(positions[i]-positions[neighbor]) #arbitrary stand-in of force calculation

neighrbor_end = time.perf_counter()


print("No neighor list: " + str(round(end-start,3)) + "s")
print("Using a neighbor list: " + str(round(neighrbor_end-neighrbor_start,2)) + "s\n")

#Print some of the neighbor lists
for i in range(4):
  print("Particle " + str(i) + " neighbors: " + str(neighbor_list[i]))


