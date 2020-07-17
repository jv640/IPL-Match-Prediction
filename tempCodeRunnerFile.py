if len(played_player_1) != 11:
            #     # not_played_1 = batsman_tag[0].find("div").find_all("a")
            #     print(played_player_1)
            # for player in played_player_1:
            #     name = player.find("a", attrs = {'title': True})
            #     if name == None:
            #         r = requests.get(player['href'])
            #         htmlContent = r.content
            #         soup3 = BeautifulSoup(htmlContent, 'html.parser')
            #         team_1.append(soup3.find("p", class_ = "ciPlayerinformationtxt").find("span").getText())
            #         del soup3 
            #     else:   
            #         name = name['title']   
            #         team_1.append(name[20:])
            # if len(played_player_1) != 11:
            #     for player in not_played_1:
            #         r = requests.get(player['href'])
            #         htmlContent = r.content
            #         soup_player_name = BeautifulSoup(htmlContent, 'html.parser')
            #         team_1.append(soup_player_name.find("p", class_ = "ciPlayerinformationtxt").find("span").getText())
            #         del soup_player_name
            # # print(len(team_1))
            # if len(batsman_tag) == 2:
            #     played_player_2 = batsman_tag[1].find_all("td", class_ = "batsman-cell")
            #     if(played_player_2 == None):
            #         played_player_2 = batsman_tag[1].find_all("tr")
            # else:
            #     played_player_2 = soup_page.find("table", class_ = "w-100").find_all("a")
            # if len(played_player_2) != 11:
            #     not_played_2 = batsman_tag[1].find("div").find_all("a")
            # for player in played_player_2:
            #     name = player.find("a", attrs = {'title': True})
            #     if name == None:
            #         r = requests.get(player['href'])
            #         htmlContent = r.content
            #         soup3 = BeautifulSoup(htmlContent, 'html.parser')
            #         team_2.append(soup3.find("p", class_ = "ciPlayerinformationtxt").find("span").getText())
            #         del soup3 
            #     else:   
            #         name = name['title']   
            #         team_2.append(name[20:])
            # if len(played_player_2) != 11:
            #     for player in not_played_2:
            #         r = requests.get(player['href'])
            #         htmlContent = r.content
            #         soup_player_name = BeautifulSoup(htmlContent, 'html.parser')
            #         team_2.append(soup_player_name.find("p", class_ = "ciPlayerinformationtxt").find("span").getText())
            #         del soup_player_name
            # # print(len(team_2))
        
