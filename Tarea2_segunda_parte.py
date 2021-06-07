import math

class Grafo:
    def _init_(self):
        self.vertices = []
        self.matriz = []


    def estan_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def l(self, v):
        if self.estan_vertices(v):
            return False

        self.vertices.append(v)

        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1)]

        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        self.matriz = matriz_aux
        return True
            

    def arista(self, inicio, fin, valor, dirijida):
        if not(self.estan_vertices(inicio)) or not(self.estan_vertices(fin)):
            return False
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor


        if not dirijida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = valor
        return True

    def imprimir(self, m):
        cadena = "\n"

        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])

        cadena += "\n " + ("   -" * len(m))

        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                    if f == c and (m[f][c] is None or m[f][c] == 0):
                        cadena += "\t" + "\\"
                    else:
                        if m[f][c] is None:
                            cadena += "\t" + "X"
                        elif math.isinf(m[f][c]):
                            cadena += "\t"  + "m"  
                        else:
                            cadena += "\t" + str(m[f][c])

        cadena += "\n"
        print(cadena)


def main():


    g = Grafo()

    g.l("0") 
    g.l("1") 
    g.l("2") 
    g.l("3") 
    g.l("4") 
    g.l("5") 
    g.l("6")


    g.arista("0", "5", 5, True)
    g.arista("0", "2", 4, True)
    g.arista("1", "3", 2, True)
    g.arista("2", "0", 1, True)
    g.arista("2", "4", 1, True)
    g.arista("2", "3", 5, True)
    g.arista("3", "2", 3, True)
    g.arista("3", "4", 3, True)
    g.arista("3", "1", 4, True)
    g.arista("4", "2", 8, True)
    g.arista("4", "5", 8, True)
    g.arista("4", "3", 8, True) 
    g.arista("5", "0", 8, True)
    g.arista("5", "6", 8, True)
    g.arista("5", "4", 8, True)
    g.arista("6", "5", 8, True)


    g.imprimir(g.matriz)

main()