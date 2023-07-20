import math
from scipy.stats import norm

def black_scholes_option_pricing(S, K, r, T, sigma, option_type='call'):
    """
    Calculate the option price using the Black-Scholes formula.

    :param S: Current stock price
    :param K: Strike price
    :param r: Risk-free interest rate (annualized)
    :param T: Time to expiration (in years)
    :param sigma: Volatility of the underlying stock (annualized)
    :param option_type: 'call' for Call option, 'put' for Put option
    :return: Option price
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price

# Example usage
if __name__ == "__main__":
    current_stock_price = 100
    strike_price = 100
    risk_free_rate = 0.05
    time_to_expiration = 1
    volatility = 0.2
    option_type = 'call'

    option_price = black_scholes_option_pricing(current_stock_price, strike_price, risk_free_rate, time_to_expiration,
                                                volatility, option_type)
    print(f"The {option_type.capitalize()} option price is: {option_price:.2f}")
