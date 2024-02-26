# Computational Finance with Python

## Simple Returns (Arithmetic Returns)
Simple returns represent the percentage change in a financial asset's price over a specific period.

### Simple Return Formula:
For a single-period simple return, the formula is:
\[ R_t = \frac{P_t - P_{t-1}}{P_{t-1}} \]

Where:
- \( R_t \) is the simple return at time \( t \).
- \( P_t \) is the asset price at time \( t \).
- \( P_{t-1} \) is the asset price at the previous time \( t-1 \).

### Interpretation:
If \( R_t \) is positive, it indicates a profit, whereas a negative \( R_t \) suggests a loss for that period.

## Holding Period Returns (HPR)
The Holding Period Return (HPR) represents the total return on an investment over a given period.

### Holding Period Return Formula:
The formula for the holding period return is:
\[ HPR = \frac{P_t + D - P_{t-1}}{P_{t-1}} \]

Where:
- \( HPR \) is the holding period return.
- \( P_t \) is the ending price of the asset.
- \( P_{t-1} \) is the beginning (or purchase) price of the asset.
- \( D \) is the cash dividend or cash flow received during the holding period.

### Interpretation:
A positive \( HPR \) indicates a profit over the holding period, and a negative \( HPR \) suggests a loss.

## Annualized Returns
Annualized return expresses an investment's return on an annual basis.

### Annualized Return Formula:
For investments held over multiple years:
\[ \text{Annualized Return} = \left(1 + HPR\right)^\frac{1}{n} - 1 \]

Where:
- \( HPR \) is the total holding period return.
- \( n \) is the number of years of the holding period.

### Interpretation:
The annualized return provides an average yearly return rate.

## Log Returns (Continuously Compounded Returns)
Log returns measure returns useful for mathematical and statistical analyses.

### Log Return Formula:
The log return for a single period is:
\[ r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) \]

Where:
- \( r_t \) is the log return at time \( t \).
- \( P_t \) is the asset price at time \( t \).
- \( P_{t-1} \) is the asset price at the previous time.

### Interpretation:
Log returns can be additive across time. They simplify certain mathematical and statistical operations.

## Annualized Log Returns (Continuously Compounded Annual Returns)

While log returns give the return of an asset over a specific period (like a day or month), it's often useful to know what the return would be over a standard time period, like a year. This helps in comparing returns across different assets or investments. Annualized log returns allow us to express returns on a standardized yearly basis.

### Annualized Log Return Formula:

Given a log return \( r \) over a period \( t \) and assuming \( n \) such periods make up a year, the annualized log return is calculated using:

\[ R_a = n \times r \]

Where:
- \( R_a \) is the annualized log return.
- \( r \) is the average log return for the given period.
- \( n \) is the number of periods in a year (e.g., if you're working with daily returns, and assuming 252 trading days in a year, \( n = 252 \)).

### Interpretation:

- Annualized log returns provide a way to compare the performance of assets over equivalent yearly periods.
- This method of annualizing assumes the return compounds in a continuously compounded manner over the course of the year.

### Example:

Assuming you have a daily log return (for a trading day) of 0.001 and there are 252 trading days in a year, the annualized log return would be:

\[ R_a = 252 \times 0.001 = 0.252 \]

This translates to an annualized log return of 25.2%.

### Note:

It's essential to use the correct number of periods for \( n \) depending on the data frequency (daily, monthly, quarterly, etc.) to get accurate annualized returns.

## Adjusting Returns for Dividends

When analyzing the returns of a stock or another asset, dividends play an essential role. Total return accounts for both price appreciation and dividends (or other distributions). If dividends aren't reinvested, you might simply add the dividend yield to the price return. If dividends are reinvested, the computation is slightly more involved.

### Simple Returns with Dividends:

When calculating simple returns with dividends, consider both the change in price and the dividend received.

\[ r_t = \frac{P_t + D_t - P_{t-1}}{P_{t-1}} \]

Where:
- \( r_t \) is the return at time \( t \).
- \( P_t \) is the price at time \( t \).
- \( P_{t-1} \) is the price at time \( t-1 \).
- \( D_t \) is the dividend received at time \( t \).

### Log Returns with Dividends:

When dividends are reinvested, log returns can be adjusted for dividends as follows:

\[ r_t = \ln\left(\frac{P_t + D_t}{P_{t-1}}\right) \]

Where:
- \( r_t \) is the log return at time \( t \).
- \( P_t \) is the price at time \( t \).
- \( P_{t-1} \) is the price at time \( t-1 \).
- \( D_t \) is the dividend received at time \( t \).

### Notes:

- Adjusting for dividends gives a clearer picture of the true return an investor would receive.
- For stocks with significant dividend distributions, this adjustment can make a material difference in understanding the total returns.
- When dividends are reinvested, they contribute to the compounding effect, which can significantly impact long-term returns.


## Adjusting Returns for an Entire Portfolio

The return of a portfolio is determined by the returns of its constituent assets and their respective weights in the portfolio. To calculate the portfolio return, you'll want to take a weighted average of the returns of the individual assets.

### Portfolio Simple Returns:

The simple return for a portfolio, \( r_p \), is given by:

\[ r_p = \sum_{i=1}^{n} w_i r_i \]

Where:
- \( r_p \) is the portfolio return.
- \( w_i \) is the weight of asset \( i \) in the portfolio.
- \( r_i \) is the return of asset \( i \).
- \( n \) is the number of assets in the portfolio.

### Portfolio Log Returns:

For log returns, the process isn't as straightforward due to the nature of logarithms. You cannot directly weight the log returns. Instead, you'd use the asset weights with the simple returns to compute the portfolio's overall return and then compute its log return.

### Notes:

- It's crucial to periodically review and rebalance your portfolio. The actual asset weights can drift over time due to the varying performance of the underlying assets.
- Portfolio diversification can help reduce risk. By holding a mix of assets, negative returns from one asset can potentially be offset by positive returns from another.
- Always consider transaction costs and taxes when rebalancing a portfolio, as they can erode returns.

## Excess Returns

Excess returns, often denoted as \( \alpha \) (alpha), refer to the returns of an investment or portfolio above a benchmark or risk-free rate. It helps in assessing how much additional return the investment or strategy has generated relative to a passive benchmark or the return one could have earned without taking any risk.

### Equation for Excess Return:

The excess return for an investment or portfolio is given by:

\[ \alpha = r_i - r_b \]

Where:
- \( \alpha \) is the excess return.
- \( r_i \) is the return of the investment or portfolio.
- \( r_b \) is the return of the benchmark or the risk-free rate.

### Notes:

- Positive excess returns indicate that the investment or strategy outperformed the benchmark or earned more than the risk-free rate.
- Negative excess returns imply underperformance relative to the benchmark or that the investment earned less than what could have been earned by investing in a risk-free asset.
- It's essential to use an appropriate benchmark that reflects the risk and investment style of the asset or strategy being evaluated.

## Random Variables

A **random variable** (often denoted as \(X, Y, Z,\) etc.) is a function that maps the outcomes of unpredictable processes to numerical values. They can be either discrete (having specific, separate values) or continuous (having any value in a range).

### Discrete Random Variable:

A discrete random variable has a countable number of possible values. The probability of a discrete random variable \(X\) taking on a particular value \(x\) is given by \(P(X = x)\).

**Probability Mass Function (PMF)**:

The PMF gives the probability that a discrete random variable is exactly equal to some value. It's given by:

\[ p(x) = P(X = x) \]

For all \(x\), \(0 \leq p(x) \leq 1\), and the sum of \(p(x)\) over all possible values of \(x\) is 1.

### Continuous Random Variable:

A continuous random variable can take any value in a range. It's described not by a PMF, but by a **probability density function (PDF)**.

**Probability Density Function (PDF)**:

While the value of the PDF at any given \(x\) does not give the probability \(P(X = x)\) (because for continuous variables this is always 0), the area under the PDF curve between two points gives the probability that \(X\) falls between those values.

Mathematically, the probability that \(X\) is between \(a\) and \(b\) is:

\[ P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx \]

For all \(x\), \(f(x) \geq 0\), and the integral of \(f(x)\) over all possible values of \(x\) is 1.

**Cumulative Distribution Function (CDF)**:

For both discrete and continuous random variables, the CDF gives the probability that the random variable is less than or equal to a certain possible value \(x\).

\[ F(x) = P(X \leq x) \]

### Notes:

- For discrete random variables, the CDF is found by summing up the probabilities.
- For continuous random variables, the CDF at \(x\) is the area to the left of \(x\) under the PDF curve.

## Discrete vs Continuous Random Variables

Random variables can be classified into two main types: discrete and continuous. These classifications are based on the type of values the random variable can assume.

### Discrete Random Variables:

- **Definition**: A random variable is said to be discrete if it can take on a finite or countably infinite set of values.
- **Examples**: Number of heads in three coin flips, number of defective items in a sample, etc.

**Probability Mass Function (PMF)**:

- The PMF is used to specify the probability distribution of a discrete random variable.
- Denoted as \( p(x) \) for a value \( x \), the PMF is:

\[ p(x) = P(X = x) \]

This means that the probability \( X \) takes on the value \( x \) is \( p(x) \).

**Properties**:

1. For every \( x \):

\[ 0 \leq p(x) \leq 1 \]

2. The sum of all probabilities is 1:

\[ \sum_{all \ x} p(x) = 1 \]

### Continuous Random Variables:

- **Definition**: A random variable is said to be continuous if it can take on an infinite number of values in a given range.
- **Examples**: Height of individuals in a group, time it takes for a light bulb to burn out, etc.

**Probability Density Function (PDF)**:

- The PDF is used to specify the probability distribution of a continuous random variable.
- Unlike PMF, the value of the PDF at a particular point doesn't represent the actual probability. Instead, it represents the relative likelihood.

Given a PDF \( f(x) \):

\[ P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx \]

This means the probability that \( X \) falls between \( a \) and \( b \) is the area under the curve of \( f(x) \) from \( a \) to \( b \).

**Properties**:

1. For every \( x \):

\[ f(x) \geq 0 \]

2. The integral of \( f(x) \) over all possible values is 1:

\[ \int_{-\infty}^{\infty} f(x) \, dx = 1 \]

### Conclusion:

- **Discrete** random variables have specific, countable outcomes with corresponding probabilities defined by the PMF.
- **Continuous** random variables can take on any value within a range, and their probabilities are described by the PDF.

## Bernoulli Distribution

The Bernoulli distribution is a discrete probability distribution for a random variable which can take one of two possible outcomes, often labeled 0 and 1. It represents the probability distribution of any single experiment that asks a yes–no question. Such an experiment is called a Bernoulli trial.

### Parameters:
- \( p \): The probability of success (where the outcome is 1).

### Random Variable:
The random variable \( X \) following a Bernoulli distribution can take on the values 0 and 1. 
- \( X = 1 \) with probability \( p \)
- \( X = 0 \) with probability \( 1 - p \)

### Probability Mass Function (PMF):

The PMF of a Bernoulli-distributed random variable is:

\[ P(X = k) = p^k (1-p)^{1-k} \]

for \( k \in \{0,1\} \).

### Expected Value and Variance:

- **Expected Value**: \( E[X] = p \)
- **Variance**: \( Var(X) = p(1-p) \)

### Properties:

1. The Bernoulli distribution is a special case of the binomial distribution where \( n = 1 \).
2. If \( X \) has a Bernoulli distribution with parameter \( p \), then \( 1-X \) has a Bernoulli distribution with parameter \( 1-p \).

### Usage:

Bernoulli distributions are often used to model experiments with binary outcomes: success/failure, yes/no, 1/0, etc.


## Uniform Distribution

The Uniform distribution is a probability distribution where all outcomes are equally likely. It can be either discrete or continuous, but the continuous version is more common. In this explanation, we'll primarily focus on the continuous version.

### Continuous Uniform Distribution:

#### Definition:
A random variable \( X \) is said to be uniformly distributed over the interval \([a, b]\) if its probability density function (pdf) is:

\[ f(x) = \begin{cases} 
\frac{1}{b-a} & \text{for } a \leq x \leq b \\
0 & \text{otherwise}
\end{cases} \]

#### Parameters:
- \( a \): Start of the interval.
- \( b \): End of the interval.

#### Expected Value and Variance:

- **Expected Value**: \( E[X] = \frac{a+b}{2} \)
- **Variance**: \( Var(X) = \frac{(b-a)^2}{12} \)

### Discrete Uniform Distribution:

#### Definition:
If each of the \( n \) values in a finite set is equally likely, the variable has a discrete uniform distribution. The probability for each value \( x_i \) is:

\[ P(X = x_i) = \frac{1}{n} \]

#### Parameters:
- \( n \): Number of equally likely outcomes.

#### Expected Value and Variance:

- **Expected Value**: \( E[X] = \frac{n+1}{2} \) (if the outcomes are numbered 1, 2, ..., n)
- **Variance**: \( Var(X) = \frac{n^2-1}{12} \)

### Properties:

1. The continuous uniform distribution is flat, meaning all intervals of the same length are equally probable.
2. Both the continuous and discrete uniform distributions are symmetric.

### Usage:

The uniform distribution is often used in computer simulations to generate "random" numbers between a specified range.

## Normal Distribution

The Normal distribution, also known as the Gaussian distribution, is one of the most widely known and used probability distributions in statistics and in nature.

### Definition:

A random variable \( X \) follows a normal distribution if its probability density function (pdf) is given by:

\[ f(x|\mu,\sigma^2) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \]

where:
- \( \mu \) is the mean or expected value of the distribution.
- \( \sigma^2 \) is the variance.
- \( \sigma \) is the standard deviation.

### Parameters:

- \( \mu \): Mean of the distribution.
- \( \sigma^2 \): Variance of the distribution.

### Properties:

1. **Symmetry**: The normal distribution is symmetric about its mean.
2. **Bell Curve**: The shape of the normal distribution is known as a bell curve.
3. **Empirical Rule**: For a normal distribution:
   - Approximately 68% of the data falls within one standard deviation of the mean (\( \mu \pm \sigma \)).
   - Approximately 95% falls within two standard deviations (\( \mu \pm 2\sigma \)).
   - Approximately 99.7% falls within three standard deviations (\( \mu \pm 3\sigma \)).

### Cumulative Distribution Function (CDF):

The CDF of a normal random variable \( X \) is given by:

\[ F(x) = \int_{-\infty}^{x} f(u) \, du \]

However, this integral doesn't have a closed-form expression in elementary functions and is usually computed using numerical methods or looked up in tables. It's often represented as \( \Phi(x) \) or by using error functions.

### Standard Normal Distribution:

A normal distribution with \( \mu = 0 \) and \( \sigma = 1 \) is called a standard normal distribution. The variable used is often denoted as \( Z \). Any normal variable can be transformed into a standard normal variable using:

\[ Z = \frac{X - \mu}{\sigma} \]

### Applications:

The normal distribution is foundational in statistics and is used in the Central Limit Theorem, hypothesis testing, confidence intervals, and more. Many natural phenomena are approximately normally distributed, making it a vital tool in many fields.


## Student’s t-distribution

The Student's t-distribution (or simply "t-distribution") arises when estimating the mean of a normally distributed population in situations where the sample size is small and the population variance is unknown. It resembles the normal distribution but has heavier tails.

### Definition:

The probability density function (pdf) of the t-distribution is:

\[ f(t|v) = \frac{\Gamma\left(\frac{v + 1}{2}\right)}{\sqrt{v\pi} \cdot \Gamma\left(\frac{v}{2}\right)} \left(1 + \frac{t^2}{v}\right)^{-\left(\frac{v + 1}{2}\right)} \]

where:
- \( t \) is the value on the x-axis.
- \( v \) is the degrees of freedom (often based on sample size).
- \( \Gamma \) is the gamma function.

### Parameters:

- \( v \): Degrees of freedom. Typically \( v = n - 1 \) where \( n \) is the sample size.

### Properties:

1. **Symmetry**: The t-distribution is symmetric about 0.
2. **Heavier Tails**: Compared to the normal distribution, the t-distribution has heavier tails. This accounts for the increased variability when working with smaller samples and unknown population variance.
3. **Converges to Normal**: As \( v \to \infty \), the t-distribution approaches the standard normal distribution.

### Cumulative Distribution Function (CDF):

The CDF for the t-distribution, like the normal distribution, doesn't have an elementary closed-form expression. It's typically computed using special functions or looked up in t-tables.

### t-Score:

The t-score is a standardized score that tells how much a sample mean deviates from the population mean in terms of estimated standard errors. It's given by:

\[ t = \frac{\bar{x} - \mu}{s/\sqrt{n}} \]

where:
- \( \bar{x} \) is the sample mean.
- \( \mu \) is the population mean (or hypothesized value).
- \( s \) is the sample standard deviation.
- \( n \) is the sample size.

### Applications:

The t-distribution is frequently used in hypothesis testing (specifically, the t-test) and in constructing confidence intervals for small sample sizes when the population variance is unknown.

## Expected Value (E)

The expected value is a fundamental concept in probability theory and statistics, representing the average or mean value of a random variable. It provides a measure of the "center" of a probability distribution.

### Definition:

For a **discrete random variable** \( X \) with possible outcomes \( x_i \) and associated probabilities \( p(x_i) \), the expected value \( E(X) \) is given by:

\[ E(X) = \sum_i x_i \times p(x_i) \]

For a **continuous random variable** with probability density function \( f(x) \):

\[ E(X) = \int x \times f(x) \, dx \]

### Intuition:

The expected value can be thought of as the "weighted average" of all possible values that the random variable can assume. Each value is weighted by its probability of occurrence.

### Properties:

1. **Linearity**: \( E(aX + bY) = aE(X) + bE(Y) \) where \( a \) and \( b \) are constants, and \( X \) and \( Y \) are random variables.
2. \( E(c) = c \) where \( c \) is a constant.
3. If \( X \) and \( Y \) are independent, then \( E(XY) = E(X)E(Y) \).

### Applications:

Expected value is foundational in many areas of mathematics, economics, and finance. For example:
- In finance, the expected value can help determine the expected return on an investment.
- In decision theory, expected value can be used to choose between different strategies based on their anticipated outcomes.

## Variance, Skewness, and Kurtosis

### Variance (\( \sigma^2 \))

Variance measures the spread or dispersion of a set of data points. It gives a sense of how much individual data points differ from the mean.

#### Equation:
For a random variable \( X \) with mean \( \mu \):
\[ \sigma^2 = E[(X - \mu)^2] \]

For a sample:
\[ s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2 \]

where \( \bar{x} \) is the sample mean.

---

### Skewness

Skewness quantifies the asymmetry of the probability distribution of a real-valued random variable about its mean. 

- **Positive skewness** indicates that the distribution tail is skewed to the right of the mean.
- **Negative skewness** indicates the distribution tail is skewed to the left.

#### Equation:
\[ \text{Skewness} = E\left[ \left( \frac{X - \mu}{\sigma} \right)^3 \right] \]

For a sample:
\[ \text{Sample Skewness} = \frac{n}{(n-1)(n-2)} \sum_{i=1}^{n} \left( \frac{x_i - \bar{x}}{s} \right)^3 \]

where \( s \) is the sample standard deviation.

---

### Kurtosis

Kurtosis quantifies the shape of the distribution's tails in relation to its overall shape. 

- **Leptokurtic** (> 3 for a normal standardized distribution): Distributions with "heavy tails" or "fat tails".
- **Platykurtic** (< 3 for a normal standardized distribution): Distributions with "light tails" or "thin tails".
- **Mesokurtic** (= 3 for a normal standardized distribution): Normal distribution shape.

#### Equation:
\[ \text{Kurtosis} = E\left[ \left( \frac{X - \mu}{\sigma} \right)^4 \right] \]

For a sample:
\[ \text{Sample Kurtosis} = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum_{i=1}^{n} \left( \frac{x_i - \bar{x}}{s} \right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)} \]

## Covariance

Covariance is a measure of the relationship between two random variables. It indicates the direction of the linear relationship between the variables. 

- **Positive covariance** implies that as one variable increases, the other tends to increase as well.
- **Negative covariance** implies that as one variable increases, the other tends to decrease.

However, covariance does not indicate the strength of the relationship, nor is it standardized. Therefore, it can take any value between negative infinity and positive infinity, which makes it difficult to interpret on its own.

### Equation:
For two random variables \( X \) and \( Y \) with means \( \mu_X \) and \( \mu_Y \) respectively:
\[ \text{Cov}(X,Y) = E[(X - \mu_X)(Y - \mu_Y)] \]

For samples:
\[ \text{Cov}(X,Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \]

where \( \bar{x} \) and \( \bar{y} \) are the sample means of \( X \) and \( Y \) respectively.

Note: The covariance of a variable with itself is its variance, i.e., \( \text{Cov}(X,X) = \sigma^2_X \).


## Variance of Sums of Random Variables

When adding two random variables, the variance of the sum is not just the sum of their individual variances unless the variables are independent. 

### Equation:

For two random variables \( X \) and \( Y \):

1. **If \( X \) and \( Y \) are independent**:
\[ \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) \]

2. **If \( X \) and \( Y \) are not independent**:
\[ \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y) \]

Where \( \text{Var} \) denotes variance and \( \text{Cov} \) denotes the covariance between \( X \) and \( Y \).

### General Formula:

For \( n \) random variables \( X_1, X_2, ... , X_n \):

\[ \text{Var}\left( \sum_{i=1}^{n} X_i \right) = \sum_{i=1}^{n} \text{Var}(X_i) + 2\sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \text{Cov}(X_i, X_j) \]

Note: The double summation accounts for all pairwise covariance terms among the \( n \) random variables.

## Exponential Growth Model in Finance

In finance, exponential growth often refers to the process by which an amount of money grows at a rate that is proportionate to the amount already present. This is the fundamental concept behind compound interest. 

### Compound Interest Formula:

The exponential model for compound interest can be represented as:

\[ A = P(1 + r/n)^{nt} \]

Where:
- \( A \) is the future value of the investment/loan, including interest.
- \( P \) is the principal investment/loan amount (initial deposit or loan amount).
- \( r \) is the annual interest rate (decimal form).
- \( n \) is the number of times interest is compounded per year.
- \( t \) is the number of years the money is invested/borrowed for.

### Continuous Compounding:

When interest is compounded continuously, the formula becomes:

\[ A = Pe^{rt} \]

Where:
- \( e \) is Euler's number (approximately equal to 2.71828).

### Interpretation:

The exponential growth model is fundamental in finance, especially in the context of savings, investments, and loans. It explains why small differences in interest rates can lead to significant differences in end values over time, especially when the compounding frequency is high or the investment horizon is long.

## Log Prices in Finance

In finance, log prices refer to the natural logarithm of asset prices. Using log prices can make certain calculations, especially those involving compound returns, more straightforward.

### Formula:

Given an asset with a price \( P \), the log price \( L \) is defined as:

\[ L = \ln(P) \]

Where:
- \( \ln \) is the natural logarithm.

### Advantages of Using Log Prices:

1. **Returns Calculation**: The difference between the log prices of an asset at two different times gives the continuously compounded return over that period.
    \[ r = \ln(P_t) - \ln(P_{t-1}) \]
   
2. **Additivity**: Continuous returns (log returns) are additive across time. This is useful when aggregating returns over non-overlapping periods.
    \[ r_{total} = \ln(P_t) - \ln(P_0) = \sum_{i=1}^{t} r_i \]

3. **Statistical Properties**: Log returns are often more amenable to statistical analyses than simple returns, as they're often more closely normally distributed.

### Example:

Consider a stock whose price increased from $100 to $110 over a month. Using log prices, the continuously compounded monthly return is:

\[ r = \ln(110) - \ln(100) \]

This would give you the continuously compounded return for the month.

### Log Returns

Log returns are calculated using the natural logarithm of the price relative (i.e., the ratio of subsequent prices). Given two consecutive prices \( P_t \) and \( P_{t-1} \), the log return \( r_t \) at time \( t \) is computed as:

\[ r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) \]

### Dividend Discount Model

The basic formula for the DDM is:

\[ P_0 = \frac{D_1}{r - g} \]

Where:

- \( P_0 \) is the current stock price.
- \( D_1 \) is the expected dividend next period.
- \( r \) is the discount rate or required rate of return.
- \( g \) is the growth rate of the dividends.

If dividends are expected to be constant forever (zero growth), the DDM simplifies to the Perpetuity formula:

\[ P_0 = \frac{D}{r} \]

Where:

- \( D \) is the constant dividend amount.

For the multi-stage DDM, where dividend growth might change, the valuation is the sum of the present values of each stage.

#### 1. Current Yield (CY)

\[ \text{Current Yield (CY)} = \frac{\text{Annual Interest Payment (Coupon Payment)}}{\text{Current Bond Price}} \]

### Leptokurtosis in Financial Distributions

Leptokurtosis refers to the kurtosis of a distribution that exceeds the kurtosis of a normal distribution, which is 3.

#### Kurtosis

\[ \text{Kurtosis} = E\left[\left(\frac{X - \mu}{\sigma}\right)^4\right] \]

Where:
- \( X \) is the random variable.
- \( \mu \) is the mean of the distribution.
- \( \sigma \) is the standard deviation of the distribution.
- \( E[\cdot] \) represents the expected value.

#### Excess Kurtosis

\[ \text{Excess Kurtosis} = \text{Kurtosis} - 3 \]

A positive excess kurtosis value indicates leptokurtosis. 

### Summary Statistics in Finance

1. **Mean (Average)**
   \[ \mu = \frac{1}{n} \sum_{i=1}^{n} x_i \]

2. **Median**
   - Middle value when sorted.

3. **Mode**
   - Most frequent value.

4. **Variance**
   \[ \sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2 \]

5. **Standard Deviation**
   \[ \sigma = \sqrt{\sigma^2} \]

6. **Skewness**
   \[ \text{Skewness} = E\left[ \left( \frac{x - \mu}{\sigma} \right)^3 \right] \]

7. **Kurtosis**
   \[ \text{Kurtosis} = E\left[ \left( \frac{x - \mu}{\sigma} \right)^4 \right] \]

8. **Minimum and Maximum**
   - Smallest and largest values.

9. **Range**
   \[ \text{Range} = \text{Maximum} - \text{Minimum} \]

10. **Quantiles**
   - Partitions based on data points (e.g., Quartiles, Deciles).

### Volatility in Finance

**Volatility** refers to the degree of variation of a financial instrument's price over time. It's typically measured using the standard deviation or variance of returns.

1. **Daily Return**:
   \[ r_t = \frac{P_t - P_{t-1}}{P_{t-1}} \]
   Where:
   - \( r_t \) is the return on day \( t \)
   - \( P_t \) is the price on day \( t \)
   - \( P_{t-1} \) is the price on the previous day

2. **Variance of Returns**:
   \[ \sigma^2 = \frac{1}{n-1} \sum_{i=1}^{n} (r_i - \bar{r})^2 \]
   Where:
   - \( \sigma^2 \) is the variance
   - \( n \) is the number of observations
   - \( r_i \) is the return of the ith observation
   - \( \bar{r} \) is the mean return

3. **Standard Deviation (Volatility)**:
   \[ \sigma = \sqrt{\sigma^2} \]
   The standard deviation (\( \sigma \)) is the most commonly used measure of volatility in finance.

4. **Annualized Volatility**:
   \[ \sigma_{annual} = \sigma_{daily} \times \sqrt{252} \]
   Where 252 is typically used as the number of trading days in a year.

### Bivariate Descriptive Statistics in Finance

**Bivariate descriptive statistics** help in understanding the relationship between two financial variables.

1. **Scatter Plot**:
   A scatter plot graphically displays the relationship between two variables.

2. **Covariance**:
   It measures the degree to which two variables move together.
   
   \[ \text{Cov}(X, Y) = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{n-1} \]
   
   Where:
   - \( X_i \) and \( Y_i \) are data points for the variables \( X \) and \( Y \) respectively
   - \( \bar{X} \) and \( \bar{Y} \) are the means of \( X \) and \( Y \) respectively
   - \( n \) is the number of data points

3. **Correlation Coefficient (Pearson's \( r \))**:
   This measures the strength and direction of a linear relationship between two variables.
   
   \[ r_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} \]
   
   Where:
   - \( \sigma_X \) and \( \sigma_Y \) are the standard deviations of \( X \) and \( Y \) respectively
   - \( r_{XY} \) is the correlation coefficient between \( X \) and \( Y \)

### Value-at-Risk (VaR) in Finance

**Value-at-Risk (VaR)** provides an estimate of the potential loss an investment portfolio might face over a specific time period for a set confidence level.

#### 1. **Parametric (Variance-Covariance) VaR**:
   Using the normal distribution, VaR is calculated by:

   \[ \text{VaR}_{\alpha} = \mu - Z_{\alpha} \sigma \]

   Where:
   - \( \mu \) is the expected return.
   - \( \sigma \) is the standard deviation of the returns.
   - \( Z_{\alpha} \) is the Z-score corresponding to the desired confidence level \( \alpha \).

#### 2. **Historical Simulation VaR**:
   Arrange all returns from worst to best and find the return at the \( (1-\alpha) \) percentile.

#### 3. **Monte Carlo Simulation VaR**:
   Use random sampling to generate a large number of potential future return paths and then find the \( (1-\alpha) \) percentile return for the simulated returns.

### Value-at-Risk (VaR) Computation in Finance

**Value-at-Risk (VaR)** aims to quantify the potential loss an investment portfolio could face over a specific period for a given confidence level.

#### 1. **Parametric (Variance-Covariance) VaR**:

Given that returns are normally distributed, the VaR can be computed as:

\[ \text{VaR}_{\alpha} = \mu \times t + Z_{\alpha} \times \sigma \times \sqrt{t} \]

Where:
- \( \mu \) = Expected return over time \( t \)
- \( \sigma \) = Standard deviation of the returns
- \( Z_{\alpha} \) = Z-score corresponding to the desired confidence level \( \alpha \)
- \( t \) = Time horizon

#### 2. **Historical Simulation VaR**:

For this method:
- Collect a set of historical returns.
- Rank the returns from worst to best.
- Identify the return at the \( (1-\alpha) \) percentile.

The result is your VaR at the \( \alpha \) confidence level.

#### 3. **Monte Carlo Simulation VaR**:

This involves:
- Modeling the behavior of individual risk factors using stochastic processes.
- Simulating a large number of potential future scenarios.
- Calculating portfolio returns for each scenario.
- Ranking the simulated returns and determining the \( (1-\alpha) \) percentile return.

### Autocorrelation in Returns in Finance

**Autocorrelation** describes the relationship between a series and a lagged version of itself. It is defined as:

\[ \rho_k = \frac{\sum_{t=k+1}^{T} (r_t - \bar{r})(r_{t-k} - \bar{r})}{\sum_{t=1}^{T} (r_t - \bar{r})^2} \]

Where:
- \( \rho_k \) = Autocorrelation of the series at lag \( k \)
- \( r_t \) = Return at time \( t \)
- \( \bar{r} \) = Mean return over the sample
- \( T \) = Length of the time series

Autocorrelation can be tested using the Ljung-Box test, Durbin-Watson test, and others to check for randomness in returns.

### Variance Ratio in Finance

The **Variance Ratio** (\( VR \)) for \( k \)-period returns is defined as:

\[ VR(k) = \frac{\text{Var}[k \cdot r_t]}{k \cdot \text{Var}[r_t]} \]

Where:
- \( VR(k) \) = Variance ratio for \( k \)-period returns.
- \( r_t \) = 1-period return.
- \( \text{Var}[k \cdot r_t] \) = Variance of the aggregated \( k \)-period returns.
- \( \text{Var}[r_t] \) = Variance of 1-period returns.

If \( VR(k) = 1 \), it suggests that price changes are random. If \( VR(k) > 1 \), it indicates positive autocorrelation, and if \( VR(k) < 1 \), it indicates negative autocorrelation.

### Capital Asset Pricing Model (CAPM)

The equation for the CAPM is:

\[ E(R_i) = R_f + \beta_i (E(R_m) - R_f) \]

Where:

- \( E(R_i) \) = Expected return on the asset.
- \( R_f \) = Risk-free rate.
- \( \beta_i \) = Beta of the asset (how much the asset's returns move relative to the market's returns).
- \( E(R_m) \) = Expected return on the market.
- \( E(R_m) - R_f \) = Market risk premium (the additional return over the risk-free rate required by investors to hold the market portfolio).

In the CAPM, the expected return of an asset is composed of the risk-free rate and a premium for the risk (beta) the asset adds to a diversified portfolio.

### Decomposing Different Kinds of Risk

1. **Total Risk**:
    The total variability in returns of an asset or a portfolio.

    \[ \sigma^2(Total) = \sigma^2(Systematic) + \sigma^2(Unsystematic) \]

2. **Systematic Risk (or Market Risk)**:
    This is the risk inherent to the entire market or market segment. It cannot be diversified away. It's affected by factors like changes in interest rates, inflation rates, and overall economic cycles.

    \[ \sigma^2(Systematic) = \beta^2 \times \sigma^2(Market) \]
   
    Where:
    - \( \beta \) = Beta of the asset or portfolio (measures sensitivity to the market).
    - \( \sigma^2(Market) \) = Variance of the market.

3. **Unsystematic Risk (or Idiosyncratic Risk or Diversifiable Risk)**:
    This is the risk specific to individual assets and can be diversified away as one adds more assets to the portfolio. It includes risks like business risk, financial risk, etc.

    \[ \sigma^2(Unsystematic) = \sigma^2(Total) - \sigma^2(Systematic) \]

### Multifactor CAPM

The equation for the multifactor model can be represented as:

\[ R_i - R_f = \alpha_i + \beta_{iM} (R_M - R_f) + \beta_{i1} F_1 + \beta_{i2} F_2 + \dots + \beta_{ik} F_k + \epsilon_i \]

Where:

- \( R_i \) = Expected return on the asset or portfolio `i`.
- \( R_f \) = Risk-free rate.
- \( \alpha_i \) = Asset's alpha, which represents the unique return of the asset not explained by the systematic risks.
- \( \beta_{iM} \) = Sensitivity of the asset or portfolio's returns to the market return.
- \( R_M \) = Expected return on the market.
- \( \beta_{i1}, \beta_{i2}, \dots, \beta_{ik} \) = Sensitivities of the asset or portfolio's returns to factor 1, factor 2, ..., factor k, respectively.
- \( F_1, F_2, \dots, F_k \) = Factor 1, factor 2, ..., factor k's risk premiums.
- \( \epsilon_i \) = Error term or idiosyncratic risk of the asset.

### Coefficient of Determination (\( R^2 \))

The equation for \( R^2 \) in the context of a simple linear regression is:

\[ R^2 = 1 - \frac{SS_{res}}{SS_{tot}} \]

Where:

- \( SS_{res} \) = Sum of squares of residuals = \(\sum (y_i - \hat{y}_i)^2\)
- \( SS_{tot} \) = Total sum of squares = \(\sum (y_i - \bar{y})^2\)
- \( y_i \) = Actual value of the dependent variable.
- \( \hat{y}_i \) = Predicted value of the dependent variable from the regression.
- \( \bar{y} \) = Mean value of the dependent variable.

### Adjusted Coefficient of Determination (\( R^2_{adj} \))

The equation for \( R^2_{adj} \) is:

\[ R^2_{adj} = 1 - \left( \frac{1 - R^2}{n - k - 1} \right) \]

Where:

- \( R^2 \) = Coefficient of determination.
- \( n \) = Total number of observations.
- \( k \) = Number of predictors (not including the constant term).

### Joint Parameter Test (F-test)

The hypothesis tested is:
\[ H_0: \beta_1 = \beta_2 = \dots = \beta_k = 0 \]
\[ H_a: \text{at least one of } \beta \text{ is not } 0 \]

The F-statistic is given by:
\[ F = \frac{(R^2 / k)}{(1 - R^2) / (n - k - 1)} \]

Where:

- \( R^2 \) is the coefficient of determination of the regression.
- \( k \) is the number of predictors.
- \( n \) is the total number of observations.

The F-statistic follows an F-distribution with \( k \) and \( n - k - 1 \) degrees of freedom. A large F-statistic indicates that at least one of the predictors is significant.

### Disturbance Diagnostics

1. **Linearity**
The relationship between the independent variables and the dependent variable should be linear.

2. **Independence**
Residuals should be independent of each other.

*Test for Autocorrelation*: Durbin-Watson test
\[ DW = \sum_{t=2}^{n} (e_t - e_{t-1})^2 / \sum_{t=1}^{n} e_t^2 \]

3. **Homoscedasticity**
The variance of the residuals should remain constant.

*Tests for Heteroscedasticity*: Breusch-Pagan test, White test, etc.

4. **Normality of Errors**
The residuals should be normally distributed.

*Tests for Normality*: Jarque-Bera test, Shapiro-Wilk test, etc.

5. **No Multicollinearity**
The independent variables should not be highly correlated.

*Test for Multicollinearity*: Variance Inflation Factor (VIF)
\[ VIF_j = 1 / (1 - R^2_j) \]

### ARCH Model

Given a time series of returns \( r_t \), the ARCH model is given by:

1. Mean equation:
\[ r_t = \mu + \epsilon_t \]
Where \( r_t \) is the return at time \( t \) and \( \epsilon_t \) is the disturbance at time \( t \).

2. Variance equation:
\[ \epsilon_t = \sigma_t z_t \]
\[ \sigma_t^2 = \alpha_0 + \alpha_1 \epsilon_{t-1}^2 \]

Where:
- \( \sigma_t \) is the conditional standard deviation at time \( t \).
- \( z_t \) is a white noise error term.
- \( \alpha_0 \) and \( \alpha_1 \) are parameters.

For ARCH(q):
\[ \sigma_t^2 = \alpha_0 + \alpha_1 \epsilon_{t-1}^2 + ... + \alpha_q \epsilon_{t-q}^2 \]


### Nonstationarity

A time series is said to be stationary if it has constant mean, variance, and autocorrelation over time. Nonstationarity implies that one or more of these properties change over time.

The most common form of nonstationarity is the **unit root**. For a time series \( Y_t \):

\[ Y_t = Y_{t-1} + \epsilon_t \]
where \( \epsilon_t \) is a white noise error term, implies \( Y_t \) has a unit root and is nonstationary.

The general representation is:
\[ \Delta Y_t = \alpha + \beta t + \rho Y_{t-1} + \epsilon_t \]
If \( |\rho| = 1 \), then \( Y_t \) is nonstationary.

### Testing for Nonstationarity

The **Dickey-Fuller** test is commonly used to detect unit roots. The Augmented Dickey-Fuller (ADF) test extends this to handle autocorrelated residuals. The ADF tests the null hypothesis that a unit root is present.

### Dickey-Fuller Tests

The Dickey-Fuller tests are used to test for the presence of a unit root in a time series, suggesting nonstationarity.

#### 1. Basic Dickey-Fuller Test

The regression equation for this test is:
\[ \Delta Y_t = \alpha + \beta t + \gamma Y_{t-1} + \epsilon_t \]
Where:
- \( \Delta Y_t \) is the difference in the series at time \( t \)
- \( \alpha \) is a constant
- \( \beta t \) is a trend term
- \( \gamma Y_{t-1} \) is the lagged level of the series
- \( \epsilon_t \) is the error term

The null hypothesis for the test is \( \gamma = 0 \), indicating nonstationarity.

#### 2. Augmented Dickey-Fuller (ADF) Test

The ADF test equation is:
\[ \Delta Y_t = \alpha + \beta t + \gamma Y_{t-1} + \delta_1 \Delta Y_{t-1} + \delta_2 \Delta Y_{t-2} + ... + \delta_p \Delta Y_{t-p} + \epsilon_t \]
Where:
- \( \delta_1, \delta_2, ... \) are the coefficients of the lagged differences of the series to account for autocorrelation.

Again, the null hypothesis is \( \gamma = 0 \).

### KPSS (Kwiatkowski-Phillips-Schmidt-Shin) Test

The KPSS test is used to test for stationarity in a time series.

#### 1. Level Stationarity

Model:
\[ Y_t = \mu + u_t \]
Where:
\[ u_t = \rho u_{t-1} + \epsilon_t \]
And:
\[ \epsilon_t \sim WN(0, \sigma^2) \]

Test Statistic:
\[ LM_{level} = \frac{\sum_{t=1}^{T}S^2_t}{\sigma^2} \]
Where:
\[ S_t = \sum_{i=1}^{t}u_i \]

#### 2. Trend Stationarity

Model:
\[ Y_t = \mu + \lambda t + u_t \]

Test Statistic:
\[ LM_{trend} = \frac{\sum_{t=1}^{T}S^2_t}{\sigma^2} \]

For both versions of the test, if the LM statistic exceeds the critical value, the null hypothesis of stationarity is rejected.

### Equity Shock

In finance, an "equity shock" refers to a sudden and significant event impacting stock values. 

#### Model

Given:
- \( r_t \): Return of a stock at time \( t \).
- \( s_t \): Shock at time \( t \).

The impact of a shock on returns can be modeled as:
\[ r_t = \alpha + \beta s_t + \epsilon_t \]

Where:
- \( \alpha \) is the constant term.
- \( \beta \) represents the sensitivity of the stock return to the shock.
- \( \epsilon_t \) is the error term.

If \( \beta \) is significantly different from zero, it suggests that the stock return is affected by the shock.

### Dividend Shock

In finance, a "dividend shock" pertains to unexpected changes in a company's dividend payout, which can significantly impact stock valuations.

#### Model

Given:
- \( P_t \): Stock price at time \( t \).
- \( D_t \): Dividend payout at time \( t \).
- \( DS_t \): Dividend shock at time \( t \).

The impact of a dividend shock on stock prices can be represented as:
\[ P_t = \alpha + \beta D_t + \gamma DS_t + \epsilon_t \]

Where:
- \( \alpha \) is the constant term.
- \( \beta \) captures the sensitivity of the stock price to dividend payouts.
- \( \gamma \) represents the sensitivity of the stock price to dividend shocks.
- \( \epsilon_t \) is the error term.

A significant value of \( \gamma \) implies that the stock price reacts notably to dividend shocks.


### Variance Decomposition

In finance, variance decomposition assesses how individual assets in a portfolio contribute to the portfolio's overall risk or variance.

#### Two-Asset Portfolio

For a portfolio comprised of two assets with weights \( w_1 \) and \( w_2 \), the variance (\( \sigma^2 \)) of the portfolio can be expressed as:

\[ \sigma^2_{\text{portfolio}} = w_1^2 \sigma^2_1 + w_2^2 \sigma^2_2 + 2 w_1 w_2 \sigma_{1,2} \]

Where:
- \( \sigma^2_1 \) represents the variance of asset 1.
- \( \sigma^2_2 \) denotes the variance of asset 2.
- \( \sigma_{1,2} \) is the covariance between the two assets.

This equation illustrates how each asset, as well as the interaction between them (covariance), contributes to the total portfolio variance.


### Brownian Motion (Wiener Process)

Brownian motion, often referred to as the Wiener process in finance, is a cornerstone of modern financial mathematics, especially in the domain of option pricing.

**Properties:**

1. The process starts at zero: \( W_0 = 0 \).
2. The increments are normally distributed: for any \( s < t \), \( W_t - W_s \) is distributed as \( N(0, t - s) \).
3. The increments are independent: for any \( s < t \) and \( u < v \), the increments \( W_t - W_s \) and \( W_v - W_u \) are independent.

The differential form of the Wiener process can be expressed as:

\[ dW_t \sim N(0, dt) \]

This indicates the distribution of small changes in the process over an infinitesimal time interval \( dt \).

### Geometric Brownian Motion (GBM)

Geometric Brownian Motion is a stochastic process used to model stock prices in various financial applications, notably in the Black-Scholes option pricing model. The key assumption is that the logarithm of the stock price follows a Brownian motion with a constant drift and volatility.

**Stochastic Differential Equation:**

\[ dS_t = \mu S_t dt + \sigma S_t dW_t \]

**Parameters:**
- \( S_t \): Stock price at time \( t \).
- \( \mu \): Expected return (drift) of the stock.
- \( \sigma \): Volatility of the stock.
- \( dW_t \): Increment of a standard Wiener process (Brownian motion).

**Solution:**

Given an initial stock price \( S_0 \), the stock price at time \( t \) is:

\[ S_t = S_0 e^{(\mu - \frac{\sigma^2}{2})t + \sigma W_t} \]

### Binomial Model

The binomial option pricing model is a method used for valuing American options. The model divides the time to expiration into intervals and calculates the option price based on a tree of stock prices. Each node represents a possible stock price, and the option price is derived by working backward from the end of the period to the present.

**One-step Binomial Model**:

**Parameters**:
- \( S \): Current stock price.
- \( u \): Factor by which stock price increases.
- \( d \): Factor by which stock price decreases.
- \( r \): Risk-free interest rate per period.
- \( \Delta t \): Length of the time step.

**Possible stock prices at the end of one period**:
\[ S_u = S \times u \]
\[ S_d = S \times d \]

**Option values at the end of the period**:
\[ C_u \] (for the up state)
\[ C_d \] (for the down state)

**Present value of the option (risk-neutral pricing)**:
\[ C = \frac{1}{1+r} \left( p C_u + (1-p) C_d \right) \]

**Risk-neutral probability**:
\[ p = \frac{e^{r \Delta t} - d}{u - d} \]



## Granger Causality

Granger causality is a statistical concept used to determine whether one time series can predict another time series. It was developed by Clive Granger, who was awarded the Nobel Prize in Economics in 2003 for his work. Despite the term "causality" in its name, Granger causality doesn't imply a causal relationship in the traditional sense, but rather a predictive one.

### Basic Breakdown:

1. **Two Time Series**: Granger causality typically deals with two time series, \(X\) and \(Y\).
2. **Prediction**: The fundamental question Granger causality asks is whether past values of \(X\) provide information that helps predict \(Y\), above and beyond the information provided by past values of \(Y\) itself.
3. **Lagged Values**: To determine this, a statistical model is used that includes lagged (i.e., past) values of \(X\) and \(Y\).
4. **Comparison**: The predictive power of a model that uses lagged values of both \(X\) and \(Y\) to predict \(Y\) is compared to a model that uses only lagged values of \(Y\).
5. **Result**: If the inclusion of lagged values of \(X\) significantly improves the prediction of \(Y\), then \(X\) is said to "Granger-cause" \(Y\).

### Key Points:

- **Not Causal in Traditional Sense**: Just because \(X\) Granger-causes \(Y\) doesn't mean \(X\) is the underlying cause of changes in \(Y\). It simply means there's a consistent pattern where changes in \(X\) precede changes in \(Y\).
- **Bi-directionality**: It's possible for \(X\) to Granger-cause \(Y\) and for \(Y\) to Granger-cause \(X\). This would indicate a bi-directional predictive relationship.
- **Limitations**: The concept is based on linear models, and the results might not hold in non-linear systems. Also, if the lag structure or model is misspecified, it could lead to incorrect conclusions.

Granger causality tests are widely used in econometrics, neuroscience, and other fields where time series data are available, and researchers are interested in understanding potential predictive relationships between variables.
