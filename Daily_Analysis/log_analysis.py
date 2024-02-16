class Loger:
    
    def menu(): ### <<<< Loger Menu:
           print(""" 

                1. **Scan all logos**
                
                 

        Info: 
                 
                1. Syslog: A general log file about system processes and events.
                2. Dpkg.log: Provides information about packages installed and removed by the package manager (apt).
                3. Auth.log: Provides information about authentication and user login operations.
                4. History.log: APT package operations log.
                5. Kern.log: Records kernel-level operations, errors, and warnings.

    
                 """)
    def entry():   ### <<<< Entry and Input
           entry_log = input("------> Please enter the required number:\t ")
           if entry_log.isdigit():
                  return int(entry_log)
           else:
                print("Invalid input. Please enter a number.")
                return None
        
    def select_log(entry): ## The Select Log analysis
        for _ in range(5):

            if entry == 1:
                entry_loger = input("-------> Enter the log path to scan:\t")
                keyword = 'error'

                with open(entry_loger, 'r+') as file:
                    for num , line in enumerate(file ,1):
                        if keyword.lower() in line.lower():
                            print(f"line {num:4};  {line.strip()}")
                            
                            break 
                        


if __name__ == '__main__':  ## The all Class scan
    Loger.menu()
    entry = Loger.entry()
    if entry is not None:
        Loger.select_log(entry)