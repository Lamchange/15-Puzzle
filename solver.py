from search import a_star_search, ida_star_search
from time import perf_counter

def solved_state(size):
    lst = [x for x in range(1, size * size)]
    lst.append(0)
    return tuple(lst)


def pretty_print_steps(steps, size):
    width = len(str(size * size))
    decor = "-"
    for n in range(len(steps)):
        if n == 0:
            print(f"--[initial state]{4*decor}")
        else:
            print(f"--[step {n:2d}]{10*decor}")
        print()
        for i in range(size):
            for j in range(size):
                tile = str(steps[n][i * size + j])
                if tile == "0":
                    tile = "-" * width
                print(f" {tile:>{width}}", end="")
            print()
        print()
    print(f"{20*decor}")


def solve(puzzle):
    size = 4
    solved = solved_state(4)

    t_start = perf_counter()
    res = a_star_search(puzzle, solved, size, 1)
    t_delta = perf_counter() - t_start

    print("search duration:" + f" {t_delta:.4f} second(s)")
    success, steps, complexity = res
    num_evaluated = complexity["time"]
    time_per_node = t_delta / max(num_evaluated, 1)
    print(f"{num_evaluated} {'evaluated nodes'} ", end="")
    print(f"{time_per_node:.8f} {'second(s) per node'}")
    if success:
        print("length of solution:", max(len(steps) - 1, 0))
        print("initial state and solution steps:")
        pretty_print_steps(steps, size)

    else:
        print("solution not found")
        
    print("space complexity:", complexity["space"], "nodes in memory")
    print("time complexity:", complexity["time"], "evaluated nodes")
    
    return steps
    
    
def solve_ida(puzzle):
    size = 4
    solved = solved_state(4)

    t_start = perf_counter()
    res = ida_star_search(puzzle, solved, size, 1)
    t_delta = perf_counter() - t_start

    print("search duration:" + f" {t_delta:.4f} second(s)")
    success, steps, complexity = res
    num_evaluated = complexity["time"]
    time_per_node = t_delta / max(num_evaluated, 1)
    print(f"{num_evaluated} {'evaluated nodes'} ", end="")
    print(f"{time_per_node:.8f} {'second(s) per node'}")
    if success:
        print("length of solution:", max(len(steps) - 1, 0))
        print("initial state and solution steps:")
        pretty_print_steps(steps, size)

    else:
        print("solution not found")
        
    print("space complexity:", complexity["space"], "nodes in memory")
    print("time complexity:", complexity["time"], "evaluated nodes")
    
    return steps