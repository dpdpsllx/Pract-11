def solve_hod_mat():
    """Решает равенство ХОД+ХОД+ХОД=МАТ, где разным буквам соответствуют разные цифры."""
    solutions = []

    for hod in range(100, 334):
        mat = 3 * hod
        hod_str = str(hod)
        mat_str = str(mat)

        if len(mat_str) != 3:
            continue

        x, o, d = map(int, hod_str)
        m, a, t = map(int, mat_str)

        digits = {x, o, d, m, a, t}
        if len(digits) == 6:
            solutions.append(f"{hod}+{hod}+{hod}={mat}")

    return solutions

for solution in solve_hod_mat():
    print(solution)
