def IPovrsinu():
    if oblik == "pravougaonik":
        print("povrsina pravougaonika je a*b")
        print("obim pravougaonika je a*2 + b*2")
    elif oblik == "kvadrat":
        print("povrsina kvadrata je a*a")
        print("obim kvadrata je 4*a ")
    elif oblik == "trougao":
        print("povrsina trougla je a*b/2")
        print("obim trougla je a + b + c")
    else:
        print("tog oblika nema")
oblik = (input("unesite neki oblik(pravougaonik, kvadrat, trougao): "))
IPovrsinu()