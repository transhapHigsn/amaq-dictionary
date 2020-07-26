import logging
import time

from sys import exit
from textblob import Word

from helper import clean_text
import welcome as w

logging.basicConfig(filename='amaq.log', level=logging.DEBUG)

class amaq(object):
    def __str__(self):
        self.name = 'Amaq'

    def amaq_queries(self):
        logging.info('Running Amaq ' + time.asctime(time.localtime(time.time())))
        print("Hello, I\'m Amaq")
        print("Let\'s get to the business.")
        while True:
            text = input('>>> ')
            logging.info('User input: ' + text)
            user_in = Word(clean_text(text))

            if user_in in w.STOP_WORDS:
                self.quit()

            if w.FAQS.get(user_in):
                logging.info('User asked about question')
                print (w.FAQS.get(user_in))
                continue

            meanings = self.meaning_check(user_in)
            logging.info('Writing the result onto the output screen for ' + meanings[0])
            print(f'{meanings[0].capitalize()} stands for : \n')
            temp = meanings[0]
            del(meanings[0])
            
            for meaning in meanings:
                print(f'*** {meaning}')

            else:
                print('Sorry, I didn\'t found any match.')
                logging.info('Amaq failed to find any match for ' + temp)

    def meaning_check(self,text):
        # spell checking  and output of text
        text = Word(text)

        if text.correct() != text:
            print('''
                Are you certain this is the right word?
                If not, I have a correction for you.
                Would you like me to correct?
                Press Y for Yes and N for No.
            ''')
            choice = input('>>> ')

            if choice.lower() == 'y':
                text = text.correct()

        res = [ text ]
        if text.definitions:
            res.extend(text.definitions)

        return res

    def quit(self):
        print('Bye Bye!')
        logging.info(f'Terminating script at {time.asctime(time.localtime(time.time()))}')
        exit()


if __name__=='__main__':
    a = amaq()
    a.amaq_queries()
