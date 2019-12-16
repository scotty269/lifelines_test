import lifelines

data = pd.read_csv('my_data.csv')
T = data['T']
E = data['E']
kmf = KaplanMeierFitter().fit(T, E)
wf = WeibullFitter().fit(T, E, label='Weibull')
exf = ExponentialFitter().fit(T, E, label='Exponential')

fig, ax = plt.subplots()
kmf.plot_survival_function()
wf.plot_survival_function(ax=ax)
exf.plot_survival_function(ax=ax)
ax.set(title='Survival Function')