import pandas as pd
import send_text

def main():

    teams = 'Chicago','New York','Portland','Miami', 'Cleveland', '\n'
    'LA Clippers', 'Dallas', 'Denver', 'Brooklyn', 'Toronto', 'Milwaukee', 'Golden State', '\n'
    'Seattle', 'San Antonio', 'Detroit', 'Minnesota', 'Los angeles', 'Boston', 'Houston', '\n'
    'Washington', 'Philadelphia', 'Utah', 'Oklahoma', 'Denver', 'Sacramento', 'Orlando', '\n'
    'New Orleans','Indiana','Charlotte', 'Memphis'

    for t in teams:
    
        scraper = pd.read_html('https://scores.nbcsports.com/nba/scoreboard.asp?meta=true', match= t)
        row = pd.concat(scraper)
        new = row.head(4)
        neww = new.tail(2)
        team1 = neww.iloc[0,5]
        new1 = neww.iloc[1,5]
        
        frames = [float(team1), float(new1)]
        
        
        score1 = frames[0]
        score2 = frames[1]
        margin = score1 - score2
        margin = abs(margin)
        print(margin)
        if margin > 18:
            send_text()
            break

if __name__ == "__main__":
    main()



