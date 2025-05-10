def dpll(clauses, assignment={}):
    def unit_propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                if len(clause) == 1:
                    unit = clause[0]
                    assignment[abs(unit)] = unit > 0
                    new_clauses = []
                    for c in clauses:
                        if unit in c:
                            continue
                        if -unit in c:
                            c = [x for x in c if x != -unit]
                        new_clauses.append(c)
                    clauses = new_clauses
                    changed = True
                    break
        return clauses, assignment

    clauses, assignment = unit_propagate(clauses, assignment)
    if [] in clauses:
        return False
    if not clauses:
        return True
    for clause in clauses:
        for lit in clause:
            var = abs(lit)
            if var not in assignment:
                break
        break
    for value in [True, False]:
        local_assignment = assignment.copy()
        local_assignment[var] = value
        simplified = []
        for c in clauses:
            if (var if value else -var) in c:
                continue
            simplified.append([l for l in c if l != (-var if value else var)])
        if dpll(simplified, local_assignment):
            return True
    return False
