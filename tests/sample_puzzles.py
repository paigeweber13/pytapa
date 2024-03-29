valid_sample_puzzles = [
    {
        'start': [[-1,-1,11,-1,-1,-1],
                  [-1,4,21,-1,-1,31],
                  [-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1],
                  [5,-1,-1,311,6,-1],
                  [-1,-1,-1,11,-1,-1]],
        'solution': [[-2,-2,11,-1,-2,-2],
                     [-2,4,21,-2,-2,31],
                     [-2,-1,-1,-2,-1,-2],
                     [-2,-2,-2,-2,-2,-2],
                     [5,-2,-1,311,6,-2],
                     [-2,-2,-2,11,-2,-2]]
    },
    {
        'start': [[-1,-1,-1,21,-1,-1,3,11,-1,-1],
                  [-1,7,-1,-1,-1,-1,-1,-1,6,-1],
                  [21,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [3,-1,-1,32,221,-1,221,-1,-1,4],
                  [-1,-1,-1,-1,-1,-1,41,-1,-1,-1],
                  [-1,-1,-1,221,-1,-1,-1,-1,-1,-1],
                  [5,-1,-1,31,-1,5,22,-1,-1,3],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
                  [-1,51,-1,-1,-1,-1,-1,-1,6,-1],
                  [-1,-1,21,4,-1,-1,4,-1,-1,-1]],
        'solution': [[-2,-2,-2,21,-1,-2,3,11,-2,-2],
                     [-2,7,-2,-1,-2,-2,-2,-1,6,-2],
                     [21,-2,-2,-2,-2,-1,-2,-2,-2,-2],
                     [3,-2,-1,32,221,-2,221,-1,-2,4],
                     [-1,-2,-2,-2,-1,-2,41,-2,-2,-1],
                     [-2,-2,-1,221,-2,-2,-2,-1,-2,-2],
                     [5,-2,-2,31,-2,5,22,-2,-2,3],
                     [-2,-2,-1,-1,-2,-1,-1,-2,-1,11],
                     [-2,51,-2,-2,-2,-2,-2,-2,6,-2],
                     [-2,-2,21,4,-2,-1,4,-2,-2,-2]],
    },
    # demoing each hint
    {
        'start': [[-1,-1,-1],
                  [-1,8,-1],
                  [-1,-1,-1]],
        'solution': [[-2,-2,-2],
                     [-2,8,-2],
                     [-2,-2,-2]],
    },
    {
        'start': [[-1,-1,-1],
                  [-1,7,-1],
                  [-1,-1,-1]],
        'solution': [[-2,-1,-2],
                     [-2,7,-2],
                     [-2,-2,-2]],
    },
]

invalid_sample_puzzles = [
    {
        # invalid because has a 2x2 square of 1s
        'solution': [[-2,-2,-1],
                     [-2,-2,-1],
                     [-1,-1,-1]]
    },
    {
        # invalid because has a 2x2 square of 1s
        # more difficult to catch than previous example
        'solution': [[-2,-1,-1,-1,-1,-1],
                     [-2,-2,-1,-2,1,-2],
                     [-1,-2,1,-1,-2,-2],
                     [-2,-1,-2,1,-2,-1],
                     [-2,-2,1,-1,-1,-1],
                     [-2,-1,-1,-1,-1,-1]]
    },
    {
        # invalid because solution is not a continuous line
        'solution': [[-2,-1,-1],
                     [-2,-1,-2],
                     [-1,-1,-2]]
    },
    {
        # invalid because hint 8 is not satisfied
        'solution': [[-2,-1,-1],
                     [-2,8,-2],
                     [-1,-1,-2]]
    },
    {
        # invalid because hint 11 in row -1 is not satisfied
        'solution': [[-2,-1,11,-1,-2,-2],
                     [-2,4,21,-2,1,31],
                     [-2,-1,-1,-2,-1,-2],
                     [-2,-2,1,-2,1,-2],
                     [5,-2,-1,311,6,-2],
                     [-2,-2,1,11,-2,-2]]
    },
    {
        # invalid because of 31 hint in row -1
        'solution': [[-2,-2,1,31,-1,-2,3,11,-2,-2],
                     [-2,7,-2,-1,-2,1,-2,-1,6,-2],
                     [21,-2,1,-2,1,-1,-2,1,-2,-2],
                     [3,-2,-1,32,221,-2,221,-1,-2,4],
                     [-1,-2,1,-2,-1,-2,41,-2,1,-1],
                     [-2,-2,-1,221,-2,1,-2,-1,-2,-2],
                     [5,-2,1,31,-2,5,22,-2,1,3],
                     [-2,-2,-1,-1,-2,-1,-1,-2,-1,11],
                     [-2,51,-2,1,-2,1,-2,1,6,-2],
                     [-2,-2,21,4,-2,-1,4,-2,1,-2]],
    }
]
