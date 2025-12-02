"""
Mia on harjunud elektrihinda vaatama äpist, kus on kirjas, mitu senti maksab kilovatt-tund.

Kuna paljudes kohtades on hind näidatud eurodes megavatt-tunni kohta, siis soovib ta hinna teisendamiseks programmi
 (1 MWh = 1000 kWh).
Koostada funktsioon elektrihind, mis
võtab argumendiks elektrihinna sentides kilovatt-tunni kohta (s/kWh);
teisendab hinna eurodesse megavatt-tunni kohta (€/MWh);
tagastab hinna eurodes megavatt-tunni kohta.

Näide funktsiooni tööst
elektrihind(22.8)
228.0
Koostada põhiprogramm, mis
küsib kasutajalt elektrihinda sentides kilovatt-tunni kohta (ujukomaarv);
rakendab funktsiooni elektrihind ja väljastab ekraanile elektrihinna eurodes megavatt-tunni kohta.
Oluline on, et elektrihinna teisendamise funktsioon ise ei küsiks kasutajalt midagi ja
 see funktsioon ise ka ei väljastaks tulemust ekraanile.
 Need tegevused peab tegema põhiprogrammis väljaspool funktsiooni, funktsiooni töö on vaid arvutada ja tagastada tulemus.

NB! Funktsiooni nimi peab olema täpselt see, mis on ülesandes ette antud.

Näited programmi tööst

  Sisesta elektrihind sentides kilovatt-tunni kohta: 22.8
  22.8 s/kWh on 228.0 €/MWh

  Sisesta elektrihind sentides kilovatt-tunni kohta: 12.35
  12.35 s/kWh on 123.5 €/MWh
"""

def convert_price(price_s_kw: float) -> float:
    """
    Convert electricity price from s/kWh to €/MWh
    :param price_s_kw: price in cent per kilo watt-hour
    :return: price in euro per mega watt-hour
    """
    price_in_eur = price_s_kw / 100
    return price_in_eur * 1000


if __name__ == '__main__':
    given_price_str = input("Sisesta elektrihind sentides kilovatt-tunni kohta:")
    converted_price = convert_price(float(given_price_str))
    print(f"{given_price_str} s/kWh on {converted_price} €/MWh")
