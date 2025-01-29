import yfinance as yf
import matplotlib.pyplot as plt
import os 
from rich.console import Console
from rich.table import Table
from rich import print
import sys
import pandas as pd
from tabulate import tabulate

def stock_save(stocks):
    for i in stocks: 
        data = yf.Ticker(i).history(period="3mo").reset_index()[["Date", "Open"]]
        plt.title("STOCKS")
        plt.plot(data["Date"], data["Open"], label = i)
        plt.title("STOCKS")
        plt.legend()
        save = os.getcwd()
        plt.savefig(save + '/plot.png')

def stock_viewer(stocks):
    for i in stocks: 
        data = yf.Ticker(i).history(period="3mo").reset_index()[["Date", "Open"]]
        plt.title("STOCKS")
        plt.plot(data["Date"], data["Open"], label = i)
        plt.title("STOCKS")
        plt.legend()
    plt.show()


def get_info(stocks):
    for i in stocks: 
        info = yf.Ticker(i).history(period='1d', interval='1d')
        print(i)   
        print(tabulate(info, headers='keys', tablefmt='psql'))
    

def check(test):
    if test == "2":
        return test
    if test == "1":
        sys.exit()
    sel = ["1", "2"]
    while test not in sel:
            console.log("Please enter either 1 or 2")
            test = console.input(f"[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    return test


# Main
stocks = input("Enter the stock names followed by a space: ").upper()
stocks = stocks.split(" ")
test = ""
while test != "1":
    print()
    table = Table(title="STOCKY Commands")
    table.add_column("NUM", style="green")
    table.add_column("TASK", style="red")
    table.add_column("Description", style="blue")

    table.add_row("1", "Stock_Save", "This will save a graph of the stocks that you picked. Will be 3 months.")
    table.add_row("2", "Stock_Viewer", "This will display the Stocks graph.")
    table.add_row("3", "Get_Info", "This will show the stock info. Includes, highs, lows, open, close. ETC.")
    console = Console()
    console.print(table)
    print()
    selection = input("enter a number to execute the command: ")
    if selection == "1":
        stock_save(stocks)
    elif selection == "2":
        print()
        stock_viewer(stocks)
        print()
    elif selection == "3":
        print()
        get_info(stocks)
        print()
    else:
        console.log("[bold red]Please enter a valid choice!")
    print()
    test = console.input(f"[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    if test != "1":
        x = check(test)
        if x == "1":
            sys.exit()
