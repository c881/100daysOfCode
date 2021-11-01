years = [2010, 2011, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370 ]

def annual_births_average(inp_years, inp_births):
    total = 0
    result = []
    for index, (year, birth) in enumerate(zip(years, births), start=1):
        total += birth
        yield (year, birth, round(total / index))
    # return result

print(*annual_births_average(years, births),sep='\n')