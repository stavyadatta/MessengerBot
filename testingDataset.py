import pandas as pd


def testing_data_country_wise(alpha_3_country, nameOfCountry):
    url = 'https://raw.githubusercontent.com' \
          '/owid/covid-19-data/master/public/data/testing/covid-testing-latest-data-source-details.csv'
    print(alpha_3_country)

    df = pd.read_csv(url, error_bad_lines=False)
    country_df = df.loc[df['ISO code'] == alpha_3_country]
    lists_of_entities = []
    replace_text = f"{nameOfCountry} -"
    # finding the cumulative count of tests
    for index, entity in country_df.iterrows():
        cumulative_count = commaNumber(float(entity["Cumulative total"]))
        entity_name = str(entity["Entity"]).replace(replace_text, "")
        daily_count = commaNumber(float(entity["Daily change in cumulative total"]))
        lists_of_entities.append((entity_name.capitalize(), cumulative_count, daily_count))
    return lists_of_entities


def commaNumber(number):
    return "{:,}".format(number)
