from scipy.integrate import quad


class Solow:
    """
        Implements the Solow growth model with update rule

            k_{t+1} = [(s z k^α_t) + (1 - δ)k_t] /(1 + n)

    """

    def __init__(self, n=0.05,  # population growth rate
                 s=0.25,  # savings rate
                 sigma=0.1,  # depreciation rate
                 alpha=0.3,  # share of labor
                 z=2.0,  # productivity
                 k=1.0):  # current capital stock
        self.n, self.s, self.sigma, self.alpha, self.z = n, s, sigma, alpha, z
        self.k = k

    def h(self):
        # Evalúa la función h
        # Llamar a las constantes
        n, s, sigma, alpha, z = self.n, self.s, self.sigma, self.alpha, self.z
        return (s * z * self.k ** alpha + (1 - sigma) * self.k) / (1 + n)

    def update(self):
        # Actualiza el estado actual (the capital stock)
        self.k = self.h()

    def steady_state(self):
        # Estado de equilibrio
        # Llamar a las constantes
        n, s, sigma, alpha, z = self.n, self.s, self.sigma, self.alpha, self.z
        return ((s * z) / (n + sigma)) ** (1 / (1 - alpha))

    def generate_sequence(self, t):
        # Genera y devuelve una serie de tiempo de largo t
        path = []
        for i in range(t):
            path.append(self.k)
            self.update()
        return path


class Market:

    def __init__(self, ad, bd, az, bz, tax):
        """
        Set up market parameters.  All parameters are scalars.  See
        https://lectures.quantecon.org/py/python_oop.html for interpretation.

        """
        self.ad, self.bd, self.az, self.bz, self.tax = ad, bd, az, bz, tax
        if ad < az:
            raise ValueError('Demanda Insuficiente.')

    def price(self):
        """
        Return equilibrium price
        """
        return (self.ad - self.az + self.bz * self.tax) / (self.bd + self.bz)

    def quantity(self):
        """
        Calcula el punto de equilibrio
        :return: ad-bd*price
        """
        return self.ad - self.bd * self.price()

    def consumer_surp(self):
        "Compute consumer surplus"
        # == Compute area under inverse demand function == #
        integrand = lambda x: (self.ad / self.bd) - (1 / self.bd) * x
        area, error = quad(integrand, 0, self.quantity())
        return area - self.price() * self.quantity()

    def producer_surp(self):
        "Compute producer surplus"
        # == Compute area above inverse supply curve, excluyendo impuestos == #
        integrand = lambda x: -(self.az / self.bz) + (1 / self.bz) * x
        area, error = quad(integrand, 0, self.quantity())
        return (self.price() - self.tax) * self.quantity() - area

    def taxrev(self):
        # Calcula el máxim
        return self.tax * self.quantity()

    def inverse_demand(self, x):
        """inversa de la demanda"""
        return self.ad / self.bd - (1 / self.bd) * x

    def inverse_supply(self, x):
        """Calcula la curva inversa de la oferta"""
        return -(self.az / self.bz) + (1 / self.bz) * x + self.tax

    def inverse_supply_no_tax(self, x):
        """Calcula la inversa de la curva de oferta sin impuestos"""
        return -(self.az / self.bz) + (1 / self.bz) * x


def deadw(m):
    """Calcula la pérdida del peso muerto para el mercado m"""
    # Crear mercado análogo pero sin impuestos
    m_no_tax = Market(m.ad, m.bd, m.az, m.bz, 0)
    # Comparar surplus, retornar diferencia
    surp1 = m_no_tax.consumer_surp() + m_no_tax.producer_surp()
    surp2 = m.consumer_surp() + m.producer_surp() + m.taxrev()
    return surp1 - surp2


class Chaos:
    """
    Modelo de sistema dinámico con: x_{t+1} = r*x_t*(1-x_t)
    """

    def __init__(self, x0, r):
        """
        Inicialización de variables
        :param x0:
        :param r:
        """
        self.x, self.r = x0, r

    def update(self):
        """
        Actualiza el valor del lado derecho de la ecuación
        """
        self.x = self.r * self.x * (1 - self.x)

    def generate_sequence(self, n):
        """
        Genera y devuelve la secuencia de largo n.
        :param n: Largo de la secuencia
        :return: path
        """
        path = []
        for i in range(n):
            path.append(self.x)
            self.update()
        return path


class ECDF:
    """
    The empirical cumulative distribution function (ecdf)
    """

    def __init__(self, observations):
        """
        Instanciación del objeto
        """
        self.observations = observations

    def __call__(self, x):
        suma = 0.0
        for obs in self.observations:
            if obs <= x:
                suma += 1
        return suma / len(self.observations)
