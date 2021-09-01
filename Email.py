import win32com.client as client
outlook =client.Dispatch("Outlook.Application")
message=outlook.CreateItem(0)
message.Display()
message.To = "Bhagyashree.Shinde@genre.com"
message.CC = "Bhagyashree.Shinde@genre.com"
message.Subject="Execution Report"
message.Body ="Hi Team,PFA copy of executio report"
message.Save()
message.Send()

def main():
    main()

if __name__ == "__main__":
    main()
