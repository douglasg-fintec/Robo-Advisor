
 ## return investment recommendation based on the selected risk level
def return_recommended_portfolio(risk):

    risk = risk.lower()
    investment_portfolio={
    'none': "100% bonds (AGG), 0% equities (SPY)",
    'low': "60% bonds (AGG), 40% equities (SPY)",
    'medium': "40% bonds (AGG), 60% equities (SPY)",
    'high': "20% bonds (AGG), 80% equities (SPY)"
     }
    return investment_portfolio.get(risk)

investment_recommendation =return_recommended_portfolio('High')

print(investment_recommendation)