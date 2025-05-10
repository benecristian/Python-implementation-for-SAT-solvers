def resolve(clause1, clause2):
    resolvents = []
    for lit in clause1:
        if -lit in clause2:
            new_clause = set(clause1 + clause2)
            new_clause.discard(lit)
            new_clause.discard(-lit)
            resolvents.append(list(new_clause))
    return resolvents

def resolution_solver(cnf):
    clauses = [set(clause) for clause in cnf]
    new = set()
    while True:
        pairs = [(clauses[i], clauses[j]) for i in range(len(clauses)) for j in range(i+1, len(clauses))]
        for (ci, cj) in pairs:
            resolvents = resolve(list(ci), list(cj))
            for res in resolvents:
                if not res:
                    return False  # empty clause found => UNSAT
                new_clause = frozenset(res)
                if new_clause not in new:
                    new.add(new_clause)
        if new.issubset(set(map(frozenset, clauses))):
            return True  # no new clauses => SAT
        for c in new:
            if c not in map(frozenset, clauses):
                clauses.append(set(c))
