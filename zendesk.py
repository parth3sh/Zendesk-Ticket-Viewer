import requests
import json
import datetime
from requests.auth import HTTPBasicAuth

#relevent URLS
url = 'https://zcc8848.zendesk.com'
getTicketsUrl = 'https://zcc8848.zendesk.com/api/v2/tickets'

#returns json with all of my tickets
def getTickets():
    getTickets = requests.get(getTicketsUrl , headers={"Authorization": "Basic %s" % 'cGFydGhlc2hrcGF0ZWxAZ21haWwuY29tOk15bmFtZWlzZG9uNQ=='})
    if(getTickets.status_code != 200):
        print("Unfortunately, there seems to be an issue connecting to the API. Thus, Zendesk Ticket Viewer is unavaliable at this time. Please try again in the future.")
        exit()
    ticketJson = getTickets.json()
    return ticketJson

def displayMenu():
    print("")
    print("Menu:")
    print("* Enter 'display' to display all tickets")
    print("* Enter 'info' to display information for a single ticket")
    print("* Enter 'help' to see menu options")
    print("* Enter 'exit' to end script")
    print("")

def displayLargeAmts(allTickets, start):
    length = len(allTickets)
    print("")
    for x in range (start, min(length-1, start + 25)):
        date = allTickets[x].get('created_at')[:10]
        date = str(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y'))
        print("Ticket ID: " + str(allTickets[x].get('id')) + " | " + "Ticket Subject: " + "'"+allTickets[x].get('subject')+"'" + " | " + "Date Created: " + date)
    inList = True
    print("")
    while inList:
        if(start == 0):
            userChoice = input("Enter 'F' to move forwards in the list. Enter 'Q' to return to the main menu.")
        elif(length-1 < start + 25):
            userChoice = input("No more tickets remain. Enter 'B' to move backwards in the list. Enter 'Q' to return to the main menu.")
        else:
            userChoice = input("Enter 'B' to move backwards in the list. Enter 'F' to move forwards in the list. Enter 'Q' to return to the main menu.")
        if(userChoice == "B"):
            inList = False
            displayLargeAmts(allTickets, start-25)
        elif(userChoice == "F"):
            inList = False
            displayLargeAmts(allTickets, start+25)
        elif(userChoice == "Q"):
            inList = False
        else:
            print("There seems to be an error with your input.")

    
        
def run():
    running = True
    while running:
        print("")
        userInput = input("What can I do for you? ")
        if (userInput != 'display' and userInput != 'info' and userInput!= "help" and userInput != 'exit'):
            print("There seems to be an issue with your request. Type help to see valid commands")
        #help displays menu
        elif (userInput == "help"):
            displayMenu()
        #display prints all tickets... will send to helper function when len > 25 for page thru
        elif (userInput == "display"):
            tickets = getTickets()
            if (len(tickets.get('tickets'))>25):
                displayLargeAmts(tickets.get('tickets'), 0)
            else:
                allTickets = tickets.get('tickets')
                for x in range(len(tickets.get('tickets'))):
                    date = allTickets[x].get('created_at')[:10]
                    date = str(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y'))
                    print("Ticket ID: " + str(allTickets[x].get('id')) + " | " + "Ticket Subject: " + "'"+allTickets[x].get('subject')+"'" + " | " + "Date Created: " + date)
       #asks for ticket id and prints information
        elif(userInput == "info"):
            tickets = getTickets()
            allTickets = tickets.get('tickets')
            print("")
            requestedTicket = input("Please enter id of ticket you would like the information for: ")
            found = False
            for x in range(len(tickets.get('tickets'))):
                if(str(allTickets[x].get('id')) == requestedTicket):
                    date = allTickets[x].get('created_at')[:10]
                    date = str(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y'))
                    print("")
                    print("Information for ticket with ID: " + str(allTickets[x].get('id')) + " | " + "Ticket Subject: " + "'"+allTickets[x].get('subject')+"'" + " | " + "Date Created: " + date + " | " + "Description: " + allTickets[x].get('description'))
                    found = True
            if(not found):
                print("No ticket with the input id was found.")
       #exits script
        elif (userInput == "exit"):
            exit()


if __name__ == "__main__":
    print("Hello and welcome to the Zendesk Ticket Viewer!")
    displayMenu()
    run()
