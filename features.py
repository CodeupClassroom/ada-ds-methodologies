import pandas as pd

def new_features(df):
    df['bedandbath'] = df.bathroomcnt + df.bedroomcnt
    df['structure_dollarpersqft'] = df.structuretaxvaluedollarcnt//df.calculatedfinishedsquarefeet
    df['land_dollarpersqft'] = df.landtaxvaluedollarcnt/df.lotsizesquarefeet
    df['acres'] = df.lotsizesquarefeet/43560
    df['livingsqft'] = df.calculatedfinishedsquarefeet - (df.bathroomcnt*25 + df.bedroomcnt*120)
    df['logerror'] = df.logerror + 5
    df['taxvalue'] = df.landtaxvaluedollarcnt + df.structuretaxvaluedollarcnt
    return df

def bin_feature(df, col, newcol, bin_cuts=[]):
    labs = list(range(len(bin_cuts)))[1:]
    df[newcol] = pd.cut(df[col], bin_cuts, labels=labs, include_lowest=False)
    return df