def binomial_option_pricing(S, K, r, T, sigma, n, option_type='call'):
    """
    Calculate the option price using the Binomial model.

    :param S: Current stock price
    :param K: Strike price
    :param r: Risk-free interest rate (annualized)
    :param T: Time to expiration (in years)
    :param sigma: Volatility of the underlying stock (annualized)
    :param n: Number of time steps in the binomial tree
    :param option_type: 'call' for Call option, 'put' for Put option
    :return: Option price
    """
    dt = T / n
    u = 1 + (r * dt) + sigma * (dt ** 0.5)  # Up factor
    d = 1 + (r * dt) - sigma * (dt ** 0.5)  # Down factor

    # Probability of up and down movements
    p = (math.exp(r * dt) - d) / (u - d)

    # Initialize option value at each node of the binomial tree
    option_values = [[0 for j in range(i + 1)] for i in range(n + 1)]

    # Calculate option values at expiration (last layer of the tree)
    for j in range(n + 1):
        if option_type == 'call':
            option_values[n][j] = max(0, S * (u ** (n - j)) * (d ** j) - K)
        elif option_type == 'put':
            option_values[n][j] = max(0, K - S * (u ** (n - j)) * (d ** j))

    # Backward induction to calculate option values at earlier nodes
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            option_values[i][j] = math.exp(-r * dt) * (p * option_values[i + 1][j] + (1 - p) * option_values[i + 1][j + 1])

    # The option price is the value at the root node of the binomial tree
    option_price = option_values[0][0]

    return option_price

# Example usage
if __name__ == "__main__":
    current_stock_price = 100
    strike_price = 100
    risk_free_rate = 0.05
    time_to_expiration = 1
    volatility = 0.2
    num_time_steps = 100
    option_type = 'call'

    option_price = binomial_option_pricing(current_stock_price, strike_price, risk_free_rate, time_to_expiration,
                                           volatility, num_time_steps, option_type)
    print(f"The {option_type.capitalize()} option price is: {option_price:.2f}")
