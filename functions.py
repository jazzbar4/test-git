def znesek_odplacila(mesecna_anuiteta, stevilo_mesecev):
    return mesecna_anuiteta + stevilo_mesecev

def EOM_navadni (G, p):
    d = 365 * 2
    o = ((G * p * d) / (365 * 100))
    return o