def unit_propagate(clauses, assignment):
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            if len(clause) == 1:
                lit = clause[0]
                assignment[abs(lit)] = lit > 0
                new_clauses = []
                for c in clauses:
                    if lit in c:
                        continue
                    if -lit in c:
                        c = [x for x in c if x != -lit]
                    new_clauses.append(c)
                clauses = new_clauses
                changed = True
                break
    return clauses, assignment

def pure_literal_assign(clauses, assignment):
    counts = {}
    for clause in clauses:
        for lit in clause:
            counts[lit] = counts.get(lit, 0) + 1
    for lit in counts:
        if -lit not in counts:
            assignment[abs(lit)] = lit > 0
            clauses = [c for c in clauses if lit not in c]
    return clauses, assignment

def dp_solver(clauses):
    assignment = {}
    clauses, assignment = unit_propagate(clauses, assignment)
    clauses, assignment = pure_literal_assign(clauses, assignment)
    if [] in clauses:
        return False
    if not clauses:
        return True
    var = abs(clauses[0][0])
    new_clauses = []
    for clause in clauses:
        if var in clause:
            continue
        new_clauses.append([x for x in clause if x != -var])
    return dp_solver(new_clauses)
