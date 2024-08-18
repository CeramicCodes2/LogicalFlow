from ...ports.drivens.for_messageLogging import ForMessageLogging
from colorama import Fore,Back,Init


Init()
class MessageLogging(ForMessageLogging):
    def checkStatusMessage(self,status):
        dctStatus = {
            'info':{'fore':Fore.YELLOW,'back':Back.BLUE},
            'error':{'fore':Back.RED,'back':Back.RESET},
            'system':{'fore':Fore.CYAN,'back':Back.BLUE}
        }
        if not(status in dctStatus):
            print(f'[{dctStatus["error"]['back']}] {dctStatus["error"]['fore']} ERROR UNIKOWN STATUS')
            return dctStatus["error"]
        return dctStatus[status]
       
    def log(self,message: str, status: str) -> None:
        statusAlert = self.checkStatusMessage(status)
        
        print(f"[{statusAlert['fore']}{status}]: {statusAlert['Back']}{message}")
    def logFromList(self,messages: list, status: str) -> None:
        
        alert = self.checkStatusMessage(status)
        for message in messages:
            print(f"[{alert['fore']}{status}]: {alert['Back']}{message}")