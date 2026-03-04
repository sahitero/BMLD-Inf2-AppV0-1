def calculate_gfr(krea, age, sex):
    #do werde die faktore beobachtet und gändert will zb Fraue im schnitt weniger Muskelmasse hänt und somit weniger Kreatinin im Blut
    if sex == "Weiblich":
        kappa = 0.7
        alpha = -0.329
        gender_fix = 1.018
    else:
        kappa = 0.9
        alpha = -0.411
        gender_fix = 1.0

    gfr = 141 * min(krea/kappa, 1)**alpha * max(krea/kappa, 1)**-1.209 * 0.993**age * gender_fix
    return gfr