# FUNCIÓN 1. de creación de una población con alelos al azar

import scipy 

""""se obtiene un modulo para lo numeros al azar """
def build_population(N, p):
    
    """Con la primera funcion se obtendra una poblacion de N= 500 y una propabilidad de ocurrencia de aleleos ("A" or "a"), la cual se     podria obtener
    por medio de una revision en la literatura, este valor tiene un rango de 1- p"""
    
    population = [] 
    """se crea lista vacia para ir agregando lo resultdos de la funcion"""
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:#si la probabilida es mayor sera el dominante/ (p)probabalidad de ocurencia 
            """si la propabilidad de ocurencia es mayor al numero obtenido del modulo spipy sera mas propable
        tener una poblacion con una ocurencia alelica dominante o si no sera recesivo"""
        allele1 = "a"
        allele2 = "A" #o si no es mayor 
        if scipy.random.rand() > p:
            allele2 = "a"
        """se hace la misma funcion pero para el alelo 2"""
        population.append((allele1, allele2))
        """por ultimo se usa la funcion append para ir añadiendo a la lista previamente creada """
    return population
""" y con la funcion return me da la lista creada """

 # FUNCIÓN 2. Conteo de pares de alelos
def compute_frequencies(population):
    """ se cuenta la frecuencia de los areglos alelicos"""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})
# FUNCIÓN 3. Creación de nueva población

def reproduce_population(population):
    """se crea diferentes generaciones a partir de una poblacion original, claramente tomando en cuenta los alelos de cada padre"""
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2) # UNO DE LOS DOS CROMOSOMAS DEBE DE SER EL DE LA MADRE  0 O 1
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom]) # HIJOS 
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation

