import numpy as np
import time
def findCells(points, bounds):
    # make sure points is n by 2 (pool.map might send us 1D arrays)
    points = points.reshape((-1,2))

    # check for each point if all coordinates are in bounds
    # dimension 0 is bound
    # dimension 1 is is point
    allInBounds = (points[:,0] > bounds[:,None,0])
    allInBounds &= (points[:,1] > bounds[:,None,1])
    allInBounds &= (points[:,0] < bounds[:,None,2])
    allInBounds &= (points[:,1] < bounds[:,None,3])


    # now find out the positions of all nonzero (i.e. true) values
    # nz[0] contains the indices along dim 0 (bound)
    # nz[1] contains the indices along dim 1 (point)
    nz = np.nonzero(allInBounds)

    # initialize the result with all nan
    r = np.full(points.shape[0], np.nan)
    # now use nz[1] to index point position and nz[0] to tell which cell the
    # point belongs to
    r[nz[1]] = nz[0]
    return r

def findCellsParallel(points, bounds, chunksize=100):
    import multiprocessing as mp
    from functools import partial

    func = partial(findCells, bounds=bounds)

    # using python3 you could also do 'with mp.Pool() as p:'
    p = mp.Pool()
    try:
        return np.hstack(p.map(func, points, chunksize))
    finally:
        p.close()

def main():
    nPoints = int(1e6)
    nBounds = int(1e4)

    # points = np.array([[ 1.5, 1.5],
    #                    [ 1.1, 1.1],
    #                    [ 2.2, 2.2],
    #                    [ 1.3, 1.3],
    #                    [ 3.4, 1.4],
    #                    [ 2. , 1.5]])

    points = np.random.random([nPoints, 2])

    # bounds = np.array([[0,0,2,2],
    #                    [2,2,3,3]])

    # bounds = np.array([[0,0,1.4,1.4],
    #                    [1.4,1.4,2,2],
    #                    [2,2,3,3]])

    bounds = np.sort(np.random.random([nBounds, 2, 2]), 1).reshape(nBounds, 4)

    t0 = time.time()
    r = findCellsParallel(points, bounds)
    t1 = time.time() - t0
    print("time required to execute findCellsParallel:",t1)
    print(points[:10])
    for bIdx in np.unique(r[:10]):
        if np.isnan(bIdx):
            continue
        bIdx = int(bIdx)
        print("{}: {}".format(bIdx, bounds[bIdx]))
    print(r[:10])

if __name__ == "__main__":
    main()
