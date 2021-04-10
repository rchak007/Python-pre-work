# Python-Intro to Finance

##### future_value.py present_value interest no_comp years
##### present_value.py future_value interest no_comp years

### Reading: Time Value of Money

Which would you rather have: ``10,000`` today or ``10,000`` next year? If you had to choose one, you'd probably select today, because if you did, you can take that money and invest it. By the end of a year (if you invested wisely), you'd end up with more than $10,000. This is the time value of money: there's a benefit to having money now, rather than later.

We quantify that benefit from interest rates or the expected percentage return on capital. Put it this way: Would you rather have $10,000 now, or $10,010 a year from now? The latter option doesn't sound very appealing, does it? Indeed, that's only one-tenth of a percent of return. That doesn't even beat inflation--you'd effectively be losing money! But how about this: $10,000 now, or $15,000 in a year? A 50% annual return sounds pretty appealing.

These rates, 0.10%, and 50%--are interest rates or rates of return. In a competitive market, what goes into determining a particular interest rate ultimately depends on the alternative options the borrower and lender both have. If there's a lot of money looking to be parked somewhere, and no one really interested in borrowing, interest rates will drop. If people expect inflation to be really high, they'll only lend their money out if the interest rate is high enough to compensate them for that.

There's a way to compare money today versus money tomorrow. Money today, or in the present, is called **Present Value**, or PV. **Money tomorrow**, or in the future, is called Future Value, or FV. The two are linked by the expected return each time period. For example, to find out what $10,000 is worth 5 years from now, assuming a 10% annual return and assuming that profits are reinvested annually, we use this formula:

```
FV = PV * [1+(i/n)]^(n*t)
```

Where FV is the future value, PV is the past value, i is the interest rate, n is the number of compounding periods within a year, and t is the number of years:

```
FV = $10,000 * [1+(.10/1)]^(1*5)
FV = $10,000 * (1+.10)^5
FV = $16,105
```

Here, we assumed that our returns were re-invested each year. If we put these re-invested returns to work more quickly (perhaps if we received dividend payments every quarter, reinvesting as soon as they were received), our compounding period would be shorter. Since this means we'd be investing capital earlier, a more frequent compounding period means that we'll end up with slightly more investment return in the future. Taking the same example above, returns were the same, but the returns were re-invested quarterly, instead of annually (so that the annual 10% return were received and re-invested in four equal installments each year):

```
FV = $10,000 * [1+(.10/4)]^(4*5)
FV = $10,000 * (1+.025)^20
FV = $16,386
```

The annual return was the same, but we ended up with $281 more after five years because we consistently had a bit of a head start when re-investing those returns. This is why compound returns are important.

It's important to note that if you rearrange the above formula, you can solve for present value:

```
FV = PV * [1+(i/n)]^(n*t)
-->
PV = FV / [1+(i/n)]^(n*t)
```

A lot of financial models for valuing stocks, companies, and even real estate use this formula. Consider why with a simple example: If there was a building for sale that you knew would be worth $100,000 next year, but you were only considering investments yielding at least a 10% return, what's the maximum price you'd offer to buy it for?

     Future Value: You expect it's worth $100,000
     Your Required Return: 10%
     Time Horizon: 1 year
     Compounding Period: 1 (only at the end of the year do you finally sell the building and earn any cash)
    
     Using the Formula:
     PV = FV / [1+(i/n)]^(n*t)
     PV = $100,000 / (1+.10)^1
     PV = $90,909

You'd pay no more than $90,909 to acquire the building. Anything less, and your expected return would fall below 10%.

Real estate is not the only area that uses the present value to evaluate investments. Investment bankers use present value when trying to figure out how much a company might sell for. Venture capitalists estimate present value on more established start-ups to estimate how much a given equity funding round is worth. Stock traders will use their forecasts for what a stock will be worth in the future to estimate a fair price to pay for it today. In practice, the approach is a bit more involved for each of these scenarios (for example, a stock trader would need to find not just the present value of the expected future price of the stock, but also the present value of each expected dividend received while holding it), but the basic formula and principle is exactly the same. Present value is an important and frequently used concept in finance.

