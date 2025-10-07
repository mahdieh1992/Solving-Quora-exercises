#رنگ‌آمیزی مکعب
def coloring(cube: list[list[list[int]]]) -> None:
    for index_out,cub in enumerate(cube):
        for index_mid,group in enumerate(cub):
            for index_inner,element in enumerate(group):
                cube[index_out][index_mid][index_inner] = 0
                if (index_out == 0 or index_out == len(cube) - 1) or (index_mid == 0 or index_mid == len(cub) - 1) or (index_inner == 0 or index_inner == len(group) - 1):
                   cube[index_out][index_mid][index_inner] = 1

matrix = [
    [
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5]
    ],
    [
       
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5]
    ],
    [
       
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5],
        [5, 5, 5, 5, 5,5]
    ]
]

coloring(matrix)

for i in range(len(matrix)):
    print(f"\nlayer {i + 1}:")
    for group in matrix[i]:
        for element in group:
            print(element,end=" ")
        print()