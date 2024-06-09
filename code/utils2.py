import pandas as pd


def complete_games_details(games_details, teams):
    """
    Function written to add new columns to games_details using also the teams dataset
    """

    def get_arena_capacity(row):
        game_id = row['GAME_ID']
        arena_capacity = row['ARENACAPACITY']
        arena_cap = None
        game_row = teams[teams['GAME_ID'] == game_id]
        
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
    merged_df = pd.merge(games_details, teams, on='GAME_ID', how='left')
    games_details.loc[:, 'LOCATION'] = merged_df.apply(get_location, axis=1)
    merged_df_season = pd.merge(games_details, teams[['GAME_ID', 'SEASON']], on='GAME_ID', how='left')
    games_details['SEASON'] = merged_df_season.apply(get_season, axis=1)

    return games_details

