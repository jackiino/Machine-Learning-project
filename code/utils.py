import pandas as pd


def ratio_missing_values_column(df, column):
    """
    Function taking as input a dataframe and a column key, returning the ratio between the number of missing values and the column size and printing it in percentage
    """
    nan_count = df[column].isna().sum()
    ratio = nan_count/df.shape[0]
    print(f"{ratio*100}% of the values of the column {column} are missing.")
    return ratio


def ratio_missing_values_df(df):
    """
    Function taking as input a dataframe, returning the ratio between the number of rows containing at least a missing value and the size of the column and printing it in percentage
    """
    num_missing_rows = df.isna().any(axis=1).sum()
    ratio = num_missing_rows/df.shape[0]
    print(f"{ratio*100}%")
    return ratio


def complete_games_details(games_details, games):
    """
    Function written to add new columns to games_details using also the games dataset
    """

    def get_opposing_team_id(row):
        game_id = row['GAME_ID']
        team_id = row['TEAM_ID']
        opposing_team_id = None
        game_row = games[games['GAME_ID'] == game_id]
        
        if team_id == game_row['HOME_TEAM_ID'].values[0]:
            opposing_team_id = game_row['VISITOR_TEAM_ID'].values[0]
        else:
            opposing_team_id = game_row['HOME_TEAM_ID'].values[0]
        
        return opposing_team_id

    def get_location(row):
        if row['TEAM_ID'] == row['HOME_TEAM_ID']:
            return 'Home'
        elif row['TEAM_ID'] == row['VISITOR_TEAM_ID']:
            return 'Away'
        else:
            return 'Unknown'

    def get_season(row):
        return row['SEASON']
        
    games_details.loc[:, 'OPPOSING_TEAM_ID'] = games_details.apply(get_opposing_team_id, axis=1)
    merged_df = pd.merge(games_details, games, on='GAME_ID', how='left')
    games_details.loc[:, 'LOCATION'] = merged_df.apply(get_location, axis=1)
    merged_df_season = pd.merge(games_details, games[['GAME_ID', 'SEASON']], on='GAME_ID', how='left')
    games_details['SEASON'] = merged_df_season.apply(get_season, axis=1)

    return games_details