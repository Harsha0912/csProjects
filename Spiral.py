#  File: Spiral.py
#  Student Name: Alejandro Zamudio
#  St
        # This loops through all of the touching points and adds them to count
        try:
            k = (point[0]+i[0])
            j = (point[1]+i[1])
            if k >= 0 and j >= 0:
                # Makes sure that the point is positive to avoid negative indexes
                count += spiral[k][j]
        except:
            # If the index is out of range just skip it
            continue
        
    return count


                



# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)

    # use following line for debugging only
    # print_spiral(spiral)


    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
