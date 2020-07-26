import logging
import time

from sys import exit
from textblob import Word
from rich import print as rich_print
from rich.console import Console 

from helper import clean_text
from constants import FAQS, STOP_WORDS

logging.basicConfig(filename='amaq.log', level=logging.DEBUG)

class amaq(object):
    def __init__(self, *args, **kwargs):
        self.name = 'Amaq'
        self.console = Console()

    def __str__(self):
        self.name = 'Amaq'

    def amaq_queries(self):
        logging.info('Running Amaq ' + time.asctime(time.localtime(time.time())))

        rich_print("[bold blue]Hello, I\'m Amaq[/bold blue]")
        rich_print("[bold blue]Let\'s get to the business.[\bold blue]")

        while True:
            text = self.console.input('[red]>>>[/red] ')
            if text.strip() == '':
                continue

            logging.info('User input: ' + text)
            user_in = Word(clean_text(text))

            if user_in in STOP_WORDS:
                self.quit()

            if FAQS.get(user_in):
                logging.info('User asked about question')
                rich_print(FAQS.get(user_in))
                continue

            meanings = self.meaning_check(user_in)

            req = meanings[0]
            logging.info(f'Writing the result onto the output screen for {req}')
            del(meanings[0])

            if not meanings:
                rich_print('[yellow]Sorry, I didn\'t found any match.[/yellow]')
                logging.info(f'Amaq failed to find any match for {req}')
                continue
            
            rich_print(f'[blue]{req.capitalize()}[/blue] stands for : \n')
            for meaning in meanings:
                rich_print(f'[green]*** {meaning}[/green]')

    def meaning_check(self,text):
        # spell checking  and output of text
        text = Word(text)

        if text.correct() != text:
            while True:
                rich_print('''
                    [bold yellow]Are you certain this is the right word?
                    If not, I have a correction for you.
                    Would you like me to correct?
                    Press Y for Yes and N for No.[/bold yellow]
                ''')
                choice = self.console.input('[red]>>>[\red] ')

                if choice.lower() not in ('y', 'n'):
                    rich_print('[yellow]Valid options are:[/yellow] [bold red]Y[/bold red] and [bold red]N[/bold red] only.')
                    continue

                if choice.lower() == 'y':
                    text = text.correct()

                break

        res = [ text ]
        if text.definitions:
            res.extend(text.definitions)

        return res

    def quit(self):
        rich_print('[bold blue]Bye Bye![/bold blue]')
        logging.info(f'Terminating script at {time.asctime(time.localtime(time.time()))}')
        exit()


if __name__=='__main__':
    a = amaq()
    a.amaq_queries()
