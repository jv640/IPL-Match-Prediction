error = True
while error:
    try:
        import requests 
        from bs4 import BeautifulSoup
        import html5lib as h5l
        import pandas as pd

        X = [['ID', 'Season', 'Home', 'Away', 'TossWin', 'TossDec', 'Venue', 'Winner']]
        playing = [['ID', 'Season', 'Team 1', 'Team 2']]
        stadiums = pd.read_csv("Stadium_and_Home_Teams.csv")
        counter = 0

        webpages = ["https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2007/08;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2009;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2009/10;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2011;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2012;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2013;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2014;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2015;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2016;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2017;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2018;trophy=117;type=season",
                    "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2019;trophy=117;type=season"
                ]

        # For Match ID
        match_id = 0

        # Iterating over Given webpages of Seasonal Match
        for page in webpages:
            r = requests.get(page)
            htmlContent = r.content
            soupmain = BeautifulSoup(htmlContent, 'html.parser')    
            # print(soup)
            # print(soup.prettify)
            
            # Finding link for all Matches Summary in given Season
            links = soupmain.find_all("a", class_ = "data-link", text = "T20")
            match_id = 1

            # Iterating over Matches
            for link in links:
                # print(link['href'])
                print("https://stats.espncricinfo.com" + link['href'])
                r = requests.get("https://stats.espncricinfo.com" + link['href'])
                # r = requests.get("https://stats.espncricinfo.com/ci/engine/match/501265.html")
                htmlContent = r.content
                soup_page = BeautifulSoup(htmlContent, 'html.parser')

                #finding Season
                Season_var = soup_page.find("a", class_ = "d-block").getText()
                season = Season_var[-4:]
                # print(season)

                
                #finding Short Names of Teams
                teams = []
                T = soup_page.find_all("a", class_ = "team-name")
                for tt in T:
                    teams.append(tt.getText())

                # Finding Full Names of Teams
                full_team_names = []
                TN = soup_page.find_all("a", class_ = "team-name")
                for ttt in TN:
                    span = ttt.find("span")
                    full_team_names.append(span['title'])
                # print(full_team_names)

                # Finding Ground
                full_place = soup_page.find("td", class_ = "match-venue").getText()
                places = full_place.split(',')
                stadium_name = places[0]

                # Deciding Home Team And Away Team
                # homeTeam = ""
                # awayTeam = ""

                found = False
                home_teams = stadiums[stadiums["Stadium"] == stadium_name]
                for home_team in home_teams["HomeTeams"]:
                    if full_team_names[0] == home_team:
                        # homeTeam = homeTeam + teams[0]
                        # awayTeam = awayTeam + teams[1]
                        found = True
                
                if found == False:
                    # homeTeam = homeTeam + teams[1]
                    # awayTeam = awayTeam + teams[0]
                    swap = teams[0]
                    teams[0] = teams[1]
                    teams[1] = swap
                    swap_full = full_team_names[0]
                    full_team_names[0] = full_team_names[1]
                    full_team_names[1] = swap_full
                # print(homeTeam, awayTeam)
                
                # Toss Details
                toss_det = soup_page.find("td", text = "Toss").findNext("td").getText()
                toss_det = toss_det.split(',')
                if len(toss_det) == 2:
                    toss_det[0] = toss_det[0][:-1]
                    
                    # Toss Winner
                    toss_win = ""
                    # print(toss_det[0],len(toss_det[0]), full_team_names[0], len(full_team_names[0]))
                    if toss_det[0] == full_team_names[0]:
                        toss_win = toss_win + "Home"
                        # print(toss_det[0], full_team_names[0])
                    else:
                        toss_win = toss_win + "Away"
                        # print(toss_det[0], full_team_names[1])
                    # print(toss_win)
                    
                    # Toss Decision
                    toss_array = toss_det[1].split()
                    toss_dec = toss_array[2]
                    # print(toss_dec)
                else:
                    toss_win = "none"
                    toss_dec = "none"

                
                # Finding Winner of match
                win = ""
                winner_tag = soup_page.find("td", text = "Points")
                
                if winner_tag != None:
                    winner_tagg = winner_tag.findNext("td").getText()
                    winner_arr = winner_tagg.split(',')
                    # print(winner_arr[0])
                    # print(winner_arr[0][-1])
                    # print(winner_arr[0][:-2])
                    if int(winner_arr[0][-1]) == 1:
                        win = win + "Tie"
                        # print(winner_arr, win)
                    elif winner_arr[0][:-2] == full_team_names[0]:
                        win = win + "Home"
                        # print(winner_arr[0][:-2], full_team_names[0], win)
                    else:
                        win = win + "Away"
                        # print(winner_arr[0][:-2], full_team_names[1], win)
                else:
                    lose = soup_page.find("span", class_ = "score-run-gray")['title']
                    if lose != full_team_names[1]:
                        win = win + "Away"
                    else:
                        win = win + "Home"

                    # print(lose)
                # print(win)

        #################        Collecting Playing 11 Data         ############

                team_1 = []
                team_2 = []
                if len(toss_det) == 2:
                    batsman_tag = soup_page.find_all("table", class_ = "batsman")
                    played_player_1 = batsman_tag[0].find_all("td", class_ = "batsman-cell")
                    if len(played_player_1) != 11:
                        not_played_1 = batsman_tag[0].find("div").find_all("a")
                    for player in played_player_1:
                        name = player.find("a")['title']
                        team_1.append(name[20:])
                    if len(played_player_1) != 11:
                        for player in not_played_1:
                            r = requests.get(player['href'])
                            htmlContent = r.content
                            soup_player_name = BeautifulSoup(htmlContent, 'html.parser')
                            team_1.append(soup_player_name.find("p", class_ = "ciPlayerinformationtxt").find("span").getText())
                            del soup_player_name
                    # print(len(team_1))
                    if len(batsman_tag) == 2:
                        played_player_2 = batsman_tag[1].find_all("td", class_ = "batsman-cell")
                    else:
                        played_player_2 = soup_page.find("table", class_ = "w-100")
                    if len(played_player_2) != 11:
                        not_played_2 = batsman_tag[1].find("div").find_all("a")
                    for player in played_player_2:
                        name = player.find("a", attrs = {'title': True})
                        if name == None:
                            r = requests.get(player['href'])
                            htmlContent = r.content
                            soup3 = BeautifulSoup(htmlContent, 'html.parser')
                            team_2.append(soup3.find("p", class_ = "ciPlayerinformationtxt").find("span").getText())
                            del soup3 
                        else:   
                            name = name['title']   
                            team_2.append(name[20:])
                    if len(played_player_2) != 11:
                        for player in not_played_2:
                            r = requests.get(player['href'])
                            htmlContent = r.content
                            soup_player_name = BeautifulSoup(htmlContent, 'html.parser')
                            team_2.append(soup_player_name.find("p", class_ = "ciPlayerinformationtxt").find("span").getText())
                            del soup_player_name
                    # print(len(team_2))
                

                match = [str(season) + "_" + str(match_id), season, teams[0], teams[1], toss_win, toss_dec, stadium_name, win]
                # print(match)
                playing_11 = [str(season) + "_" + str(match_id), season, team_1, team_2]
                del season, teams, toss_win, toss_dec, stadium_name, win, team_1, team_2
                match_id = match_id + 1
                X.append(match)
                playing.append(playing_11)
                del match
                del playing_11
                counter = counter + 1
                print("Running", counter)
                del soup_page
                # time.sleep(2)
            del soupmain

        df = pd.DataFrame(X)
        df.to_csv('Matches.csv')
        df_2 = pd.DataFrame(playing)
        df_2.to_csv('playing_11.csv')
        print("Completed")
        error = False
    except :
        error = True

