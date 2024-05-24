from InitCube import face1, face2, face3, face4, face5, face6

def algo_face1():
    face = 1
    face1[0].set_compass(nord=(5, 3), sud=(face, 4), ouest=(2, 1), est=(face, 2))
    face1[1].set_compass(nord=(5, 2), sud=(face, 5), ouest=(face, 1), est=(face, 3))
    face1[2].set_compass(nord=(5, 1), sud=(face, 6), ouest=(face, 2), est=(4, 3))

    face1[3].set_compass(nord=(face, 1), sud=(face, 7), ouest=(2, 2), est=(face, 5))
    face1[4].set_compass(nord=(face, 2), sud=(face, 8), ouest=(face, 4), est=(face, 6))
    face1[5].set_compass(nord=(face, 3), sud=(face, 9), ouest=(face, 5), est=(4, 2))

    face1[6].set_compass(nord=(face, 4), sud=(3, 1), ouest=(2, 3), est=(face, 8))
    face1[7].set_compass(nord=(face, 5), sud=(3, 2), ouest=(face, 7), est=(face, 9))
    face1[8].set_compass(nord=(face, 6), sud=(3, 3), ouest=(face, 8), est=(4, 1))

def algo_face2():
    face = 2
    face2[0].set_compass(nord=(1, 1), sud=(face, 4), ouest=(5, 3), est=(face, 2))
    face2[1].set_compass(nord=(1, 4), sud=(face, 5), ouest=(face, 1), est=(face, 3))
    face2[2].set_compass(nord=(1, 7), sud=(face, 6), ouest=(face, 2), est=(3, 1))

    face2[3].set_compass(nord=(face, 1), sud=(face, 7), ouest=(5, 6), est=(face, 5))
    face2[4].set_compass(nord=(face, 2), sud=(face, 8), ouest=(face, 4), est=(face, 6))
    face2[5].set_compass(nord=(face, 3), sud=(face, 9), ouest=(face, 5), est=(3, 2))

    face2[6].set_compass(nord=(face, 4), sud=(6, 7), ouest=(5, 9), est=(face, 8))
    face2[7].set_compass(nord=(face, 5), sud=(6, 4), ouest=(face, 7), est=(face, 9))
    face2[8].set_compass(nord=(face, 6), sud=(6, 1), ouest=(face, 8), est=(3, 7))

def algo_face3():
    face = 3
    face3[0].set_compass(nord=(1, 7), sud=(face, 4), ouest=(2, 3), est=(face, 2))
    face3[1].set_compass(nord=(1, 8), sud=(face, 5), ouest=(face, 1), est=(face, 3))
    face3[2].set_compass(nord=(1, 9), sud=(face, 6), ouest=(face, 2), est=(4, 1))

    face3[3].set_compass(nord=(face, 1), sud=(face, 7), ouest=(2, 6), est=(face, 5))
    face3[4].set_compass(nord=(face, 2), sud=(face, 8), ouest=(face, 4), est=(face, 6))
    face3[5].set_compass(nord=(face, 3), sud=(face, 9), ouest=(face, 5), est=(4, 4))

    face3[6].set_compass(nord=(face, 4), sud=(6, 1), ouest=(2, 9), est=(face, 8))
    face3[7].set_compass(nord=(face, 5), sud=(6, 2), ouest=(face, 7), est=(face, 9))
    face3[8].set_compass(nord=(face, 6), sud=(6, 3), ouest=(face, 8), est=(4, 7))
    
def algo_face4():
    face = 4
    face4[0].set_compass(nord=(1, 9), sud=(face, 4), ouest=(3, 6), est=(face, 2))
    face4[1].set_compass(nord=(1, 6), sud=(face, 5), ouest=(face, 1), est=(face, 3))
    face4[2].set_compass(nord=(1, 3), sud=(face, 6), ouest=(face, 2), est=(5, 1))

    face4[3].set_compass(nord=(face, 1), sud=(face, 7), ouest=(3, 6), est=(face, 5))
    face4[4].set_compass(nord=(face, 2), sud=(face, 8), ouest=(face, 4), est=(face, 6))
    face4[5].set_compass(nord=(face, 3), sud=(face, 9), ouest=(face, 5), est=(5, 4))

    face4[6].set_compass(nord=(face, 4), sud=(6, 3), ouest=(3, 9), est=(face, 8))
    face4[7].set_compass(nord=(face, 5), sud=(6, 6), ouest=(face, 7), est=(face, 9))
    face4[8].set_compass(nord=(face, 6), sud=(6, 9), ouest=(face, 8), est=(5, 7))


def algo_face5():
    face = 5
    face5[0].set_compass(nord=(1, 3), sud=(face, 4), ouest=(4, 3), est=(face, 2))
    face5[1].set_compass(nord=(1, 2), sud=(face, 5), ouest=(face, 1), est=(face, 3))
    face5[2].set_compass(nord=(1, 1), sud=(face, 6), ouest=(face, 2), est=(2, 1))

    face5[3].set_compass(nord=(face, 1), sud=(face, 7), ouest=(4, 6), est=(face, 5))
    face5[4].set_compass(nord=(face, 2), sud=(face, 8), ouest=(face, 4), est=(face, 6))
    face5[5].set_compass(nord=(face, 3), sud=(face, 9), ouest=(face, 5), est=(2, 4))

    face5[6].set_compass(nord=(face, 4), sud=(6, 9), ouest=(4, 9), est=(face, 8))
    face5[7].set_compass(nord=(face, 5), sud=(6, 8), ouest=(face, 7), est=(face, 9))
    face5[8].set_compass(nord=(face, 6), sud=(6, 7), ouest=(face, 8), est=(2, 7))

def algo_face6():
    face = 6
    face6[0].set_compass(nord=(3, 7), sud=(face, 4), ouest=(2, 3), est=(face, 2))
    face6[1].set_compass(nord=(3, 8), sud=(face, 5), ouest=(face, 1), est=(face, 3))
    face6[2].set_compass(nord=(3, 9), sud=(face, 6), ouest=(face, 2), est=(4, 7))

    face6[3].set_compass(nord=(face, 1), sud=(face, 7), ouest=(2, 6), est=(face, 5))
    face6[4].set_compass(nord=(face, 2), sud=(face, 8), ouest=(face, 4), est=(face, 6))
    face6[5].set_compass(nord=(face, 3), sud=(face, 9), ouest=(face, 5), est=(4, 8))

    face6[6].set_compass(nord=(face, 4), sud=(5, 9), ouest=(2, 9), est=(face, 8))
    face6[7].set_compass(nord=(face, 5), sud=(5, 8), ouest=(face, 7), est=(face, 9))
    face6[8].set_compass(nord=(face, 6), sud=(5, 7), ouest=(face, 8), est=(4, 9))