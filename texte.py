from table import table

def run_texte(**kw: dict) -> None:
    input_file = kw.get("input", None)
    output_file = kw.get("output", None)
    ta = table('{"size": 10}')
    ta.set_value_at(0, 0, 1)
    ta.set_h_sign_at(0, 0, True)
    ta.set_h_sign_at(1, 0, True)
    ta.set_h_sign_at(0, 1, True)
    ta.set_h_sign_at(2, 3, False)
    ta.set_v_sign_at(3, 2, True)
    print(ta)
    print(ta.gen_dimacs())
    return None
