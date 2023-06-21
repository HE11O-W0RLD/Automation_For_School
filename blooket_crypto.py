from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import re

class Blooket_Crypto_Auto_Solver:
    
    def click_12_buttons(self):
        container = self.driver.find_element(By.CSS_SELECTOR, 'div.styles__buttonContainer___3XYeN-camelCase')#<div class="styles__buttonContainer___3XYeN-camelCase">
        count = 0

        while count < 12:
            button = container.find_element(By.CSS_SELECTOR, 'div.styles__button___C94Th-camelCase[style*="opacity: 1;"]')#<div class="styles__button___C94Th-camelCase" role="button" tabindex="0" style="opacity: 1;">
            if button is None:
                no_click_button = container.find_element(By.CSS_SELECTOR, 'div.styles__button___C94Th-camelCase.styles__noClick___39ylx-camelCase')#<div class="styles__button___C94Th-camelCase styles__noClick___39ylx-camelCase" role="button" tabindex="0" style="opacity: 0;">
                if no_click_button is None:
                    self.check_if_game_ended()
                    time.sleep(0.2)
                    continue

            button.click()
            count += 1
            button = None
    
    def repeat_the_pattern(self):
        button_container = self.driver.find_element(By.CSS_SELECTOR, 'div.styles__buttonContainer___3XYeN-camelCase')
        while True:
            buttons = button_container.find_elements(By.CSS_SELECTOR, 'div.styles__button___C94Th-camelCase[role="button"]')
            for button in buttons:
                if 'styles__chosen___3pT3X-camelCase' in button.get_attribute('class'):
                    continue
                button.click()
                time.sleep(0.1)
                # Check if puzzle solved
                if self.driver.find_elements(By.CSS_SELECTOR, 'div.arts__modal___VpEAD-camelCase'):
                    return

    def make_all_same_color(self):
        pass
    
    def wait_until_hack_is_gone(self):
        while True:
            hack_element = self.driver.find_elements(By.CSS_SELECTOR, 'div.arts__modal___VpEAD-camelCase')#<div class="arts__modal___VpEAD-camelCase">
            if hack_element:
                time.sleep(0.1)
                continue
            else:
                break
    
    def get_hack_type(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'div.styles__desc___1Mg77-camelCase')#<div class="styles__desc___1Mg77-camelCase">Click 3 Buttons</div>
        return element.text
        
    def solving_hacks(self):
        hack_type= self.get_hack_type()
        match hack_type:
            case "Click 12 Buttons":
                self.click_12_buttons()
            case "Repeat the pattern":
                self.repeat_the_pattern()
            case "Make all buttons the same color":
                self.make_all_same_color()
            case "Find the matching cards":
                self.find_matching_cards()
            case re.match(r'Set the temperature to (\d+°)', argument) as match:
                temperature = match.group(1)
                self.set_the_temperature(temperature)
            case "Complete the upload":
                self.complete_the_upload()
            case "Click the numbers from 1 to 10":
                self.click_the_numbers()
            case "Reorder the right colors to match left (click to swap right colors)":
                self.reorder_the_colors()
            case _:
                raise Exception("Unknown hack found: Cannot solve")
        self.wait_until_hack_is_gone()
    
    def check_if_game_ended(self):
        end_of_game_element = self.driver.find_elements(By.CSS_SELECTOR, 'a.styles__headerRight___nPb83-camelCase[href="https://play.blooket.com/play"]') #The element searched here: <a class="styles__headerRight___nPb83-camelCase" href="https://play.blooket.com/play">Play Again</a>
            
        if end_of_game_element:
            time.sleep(5)
            raise Exception("Game ended")
    
    def check_if_something_wrong(self):
        while True:
            
            self.check_if_game_ended()
            
            hack_element = self.driver.find_elements(By.CSS_SELECTOR, 'div.arts__modal___VpEAD-camelCase') #The element searched here: <div class="arts__modal___VpEAD-camelCase">
            
            if not hack_element:
                if self.hacked:
                    self.repeat_loop=True
                else:
                    self.repeat_loop=False
                self.hacked=False
                break
            else:
                self.hacked=True
                self.solving_hacks()
                
            time.sleep(1)
    
    def repeat(self):
        if self.repeat_loop:
            self.repeat_loop=False
            return True
        else:
            return False
    
    def retrieve_user_input(self):
        self.name = input("Name: ")
        while True:
            try:
                id = int(input("ID: "))
                break
            except:
                print("Invalid ID")

        self.link = rf"https://play.blooket.com/play?id={id}"
        
    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)
    
    def join_game(self):
        # Wait for the input field and submit button to be available
        while True:
            try:
                name_input = self.driver.find_element(By.CSS_SELECTOR, 'input.styles__nameInput___20VdG-camelCase') #<input class="styles__nameInput___20VdG-camelCase" placeholder="Nickname" type="text" maxlength="15" value="" wfd-id="id0">
                submit_button = self.driver.find_element(By.CSS_SELECTOR, 'div.styles__joinButton___2upCU-camelCase') #<div type="submit" role="button" class="styles__joinButton___2upCU-camelCase" tabindex="0"><i class="styles__joinIcon___2ctgb-camelCase fas fa-arrow-right" aria-hidden="true"></i></div>
                self.check_if_game_ended()
                break
            except NoSuchElementException:
                time.sleep(0.5)
                self.check_if_game_ended()
        
        # Input the name into the input field
        name_input.send_keys(self.name)
        
        # Click the submit button
        submit_button.click()

    def choose_password(self):
        # Continuously check if the button container exists
        while True:
            button_container = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__buttonContainer___3yX9w-camelCase') #<div class="styles__buttonContainer___3yX9w-camelCase"><div class="styles__button___2OOoS-camelCase" role="button" tabindex="0">&gt;_&gt;</div><div class="styles__button___2OOoS-camelCase" role="button" tabindex="0">iAm10KING</div><div class="styles__button___2OOoS-camelCase" role="button" tabindex="0">unicorn345739</div><div class="styles__button___2OOoS-camelCase" role="button" tabindex="0">eggsToast&amp;Bacon-pls</div><div class="styles__button___2OOoS-camelCase" role="button" tabindex="0">_MoNkEy</div></div>
            if button_container:
                # Click a random button if the container exists
                buttons = button_container[0].find_elements(By.CLASS_NAME, 'styles__button___2OOoS-camelCase') 
                if buttons:
                    random_button = random.choice(buttons)
                    random_button.click()
                    self.check_if_something_wrong()
                    if self.repeat():
                        continue
                    break  # Exit the loop after successfully clicking a button
            else:
                time.sleep(0.3)
                self.check_if_something_wrong()

    def check_if_question_exists(self):
    # Check if the question element exists dynamically
        while True:
            question_element = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__questionText___2MlSZ-camelCase')#<div class="styles__questionText___2MlSZ-camelCase" style="color: rgb(255, 255, 255); font-size: 44px;"><div style="display: block;">???1</div></div>
            if question_element:
                self.question = question_element[0].text
                time.sleep(0.3)
                break
            else:
                self.check_if_something_wrong()
                time.sleep(0.5)

    def init_variables(self):
        self.answers= {}
        self.password_attempts= {}
        self.correct_passwords= {}
        self.link = None
        self.driver= None
        self.name= None
        self.question= None
        self.answer_is_random= None
        self.question_type_is_text= None
        self.returned_answer= None
        self.right= None
        self.reward_text= None
        self.victim= None
        self.returned_pass= None
        self.hacked= None
        self.repeat_loop= None
        self.pass_is_random= None
        self.pass_correct= None
        
    def choose_random_answer(self):
        self.answer_is_random = True
        if self.question_type_is_text:
            self.returned_answer = "a"
        else:
            while True:
                answer_options = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__answerText___2eIBw-camelCase') #<div class="styles__answersHolder___3LYNs-camelCase"><div class="styles__answerWrapper___51Q0g-camelCase" id="answer0"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True3</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer1"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">False1</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer2"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True1</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer3"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True2</div></div></div></div></div></div>
                if answer_options:
                    random_answer = random.choice(answer_options)
                    self.returned_answer = random_answer.text
                    break
                else:
                    self.check_if_something_wrong()
                    time.sleep(0.2)
                
    def retrieve_question_answer(self):
        if self.question not in self.answers:
            self.answers[self.question] = None
            self.choose_random_answer()
        else:
            self.returned_answer = self.answers[self.question]
            self.answer_is_random = False
    
    def retrieve_question_type(self):
        while True:
            input_element = self.driver.find_elements(By.CSS_SELECTOR, 'input.styles__typingAnswerInput___2wQ3I-camelCase')#<input class="styles__typingAnswerInput___2wQ3I-camelCase" placeholder="Type answer here" type="text" autocomplete="new-password" autocapitalize="none" autocorrect="off" spellcheck="false" value="">
            div_element = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__answersHolder___3LYNs-camelCase')#<div class="styles__answersHolder___3LYNs-camelCase"><div class="styles__answerWrapper___51Q0g-camelCase" id="answer0"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True3</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer1"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">False1</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer2"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True1</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer3"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True2</div></div></div></div></div></div>
            if input_element:
                self.question_type_is_text = True
                break
            elif div_element:
                self.question_type_is_text = False
                break
            else:
                self.check_if_something_wrong()
                time.sleep(0.5)
        
    def enter_answer(self):
        while True:
            if self.question_type_is_text:
                input_element = self.driver.find_elements(By.CSS_SELECTOR, 'input.styles__typingAnswerInput___2wQ3I-camelCase')#<input class="styles__typingAnswerInput___2wQ3I-camelCase" placeholder="Type answer here" type="text" autocomplete="new-password" autocapitalize="none" autocorrect="off" spellcheck="false" value="">
                submit_button = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__typingAnswerButton___1WnK5-camelCase')#<div class="styles__typingAnswerButton___1WnK5-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);">Submit</div>
                if input_element and submit_button:
                    input_element[0].send_keys(self.returned_answer)
                    submit_button[0].click()
                    self.check_if_something_wrong()
                    if self.repeat():
                        continue
                    break
            else:
                answer_options = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__answersHolder___3LYNs-camelCase div.styles__answerWrapper___51Q0g-camelCase')#<div class="styles__answersHolder___3LYNs-camelCase"><div class="styles__answerWrapper___51Q0g-camelCase" id="answer0"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True2</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer1"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True1</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer2"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">True3</div></div></div></div></div><div class="styles__answerWrapper___51Q0g-camelCase" id="answer3"><div class="styles__answerContainer___3WS-k-camelCase" role="button" tabindex="0" style="background-color: rgba(128, 255, 128, 0.8);"><div class="styles__answerTextContainer___3YgCT-camelCase"><div class="styles__answerText___2eIBw-camelCase" style="color: rgb(0, 0, 0); font-size: 36px;"><div style="display: block;">False1</div></div></div></div></div></div>
                if answer_options:
                    for answer_option in answer_options:
                        if self.returned_answer in answer_option.text:
                            answer_option.click()
                            break
                    self.check_if_something_wrong()
                    if self.repeat():
                        continue
                    break
            self.check_if_something_wrong()
            time.sleep(0.5)

    def check_if_right(self):
        while True:
            header_element = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__header___2daxi-camelCase')
            if header_element:
                correctness_status = header_element[0].text
                if correctness_status == "INCORRECT":#<div class="styles__header___2daxi-camelCase">INCORRECT</div>
                    self.right = False
                    break
                elif correctness_status == "CORRECT":#<div class="styles__header___2daxi-camelCase">CORRECT</div>
                    self.right = True
                    break
            self.check_if_something_wrong()
            time.sleep(0.4)

    def answer_was_wrong(self):
        while True:
            correct_answer_element = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__correctAnswers___2G7Wf-camelCase')#<div class="styles__correctAnswers___2G7Wf-camelCase">Correct Answer: <div style="display: flex; align-items: center; margin: 0px 5px;"><span>Tru</span></div></div>
            if correct_answer_element:
                correct_answer_text = correct_answer_element[0].find_element(By.CSS_SELECTOR, 'span').text
                self.answers[self.question] = correct_answer_text
                break
            self.check_if_something_wrong()
            time.sleep(0.4)

        element_to_be_found=None
        while True:
            while True:
                feedback_button = self.driver.find_elements(By.CSS_SELECTOR, 'div.arts__regularBody___1TM6E-camelCase.styles__background___2GulD-camelCase') #<div class="arts__regularBody___1TM6E-camelCase styles__background___2GulD-camelCase" id="feedbackButton" role="button" tabindex="0" style="background-color: rgb(196, 58, 53); cursor: pointer;">
                if feedback_button:
                    feedback_button[0].click()
                    self.check_if_something_wrong()
                    if self.repeat():
                        continue
                    break
                self.check_if_something_wrong()
                time.sleep(0.2)
            element_to_be_found = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__questionText___2MlSZ-camelCase')
            if element_to_be_found:
                break
            self.check_if_something_wrong()
            time.sleep(0.2)
    
    def check_if_answer_is_random_right(self):
        if self.answer_is_random:
            self.answers[self.question] = self.returned_answer
    
    def click_reward(self):
        element_to_be_found= None
        while True:
            while True:
                feedback_button = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__header___2daxi-camelCase')#<div class="arts__regularBody___1TM6E-camelCase styles__background___2GulD-camelCase" id="feedbackButton" role="button" tabindex="0" style="background-color: rgb(75, 194, 46); cursor: pointer;">
                if feedback_button:
                    feedback_button[0].click()
                    self.check_if_something_wrong()
                    if self.repeat():
                        continue
                    break
                self.check_if_something_wrong()
                time.sleep(0.1)
            element_to_be_found = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__choice___1aMOz-camelCase.styles__choice1___fVE10-camelCase')
            if element_to_be_found:
                break
            self.check_if_something_wrong()
            time.sleep(0.2)

        while True:
            choice_element = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__choice___1aMOz-camelCase.styles__choice1___fVE10-camelCase')#<div class="styles__choice___1aMOz-camelCase styles__choice1___fVE10-camelCase" role="button" tabindex="0">
            if choice_element:
                choice_element[0].click()
                self.check_if_something_wrong()
                if self.repeat():
                    continue
                break
            self.check_if_something_wrong()
            time.sleep(0.5)

        while True:
            reward_element = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__choiceText___1YwWe-camelCase')#<div class="styles__choiceText___1YwWe-camelCase">+ 50 Crypto</div>
            if reward_element:
                self.reward_text = reward_element[0].text
                break
            self.check_if_something_wrong()
            time.sleep(0.5)
    
    def answer_was_true_reward_proceed(self, line_of_code_for_element_to_be_found):
        element_to_be_found = None
        while True:
            while True:
                feedback_container = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__feedbackContainer___7PzgR-camelCase')#<div class="styles__feedbackContainer___7PzgR-camelCase" role="button" tabindex="0" style="outline: none; cursor: pointer;">
                if feedback_container:
                    feedback_container[0].click()
                    self.check_if_something_wrong()
                    if self.repeat():
                        continue
                    break
                self.check_if_something_wrong()
                time.sleep(0.1)
            exec(line_of_code_for_element_to_be_found)
            if element_to_be_found:
                break
            self.check_if_something_wrong()
            time.sleep(0.2)
            
    def get_victim_name(self):
        while True:
            time.sleep(0.4)
            element = self.driver.find_element(By.CSS_SELECTOR, 'div.styles__introHeader___Dzfym-camelCase')#<div class="styles__introHeader___Dzfym-camelCase" style="animation-delay: 0ms; animation-duration: 1000ms;">HACKING <span style="color: rgb(255, 255, 255);">B</span></div>
            if element:
                span_element = element.find_element(By.TAG_NAME, 'span')#<span style="color: rgb(255, 255, 255);">B</span>
                if span_element:
                    self.victim = span_element.text
                    break
            self.check_if_something_wrong()
            time.sleep(0.3)
    
    def create_keys_for_victims(self):
        if self.victim not in self.password_attempts:
            self.password_attempts[self.victim] = []
        if self.victim not in self.correct_passwords:
            self.correct_passwords[self.victim] = None

    def choose_random_pass(self):
        self.pass_is_random = True
        retrieved_passwords = self.password_attempts.get(self.victim, [])
        while True:
            pass_options = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__button___2OOoS-camelCase[role="button"]')#<div class="styles__buttonContainer___3yX9w-camelCase" style="animation-delay: 2500ms;"><div class="styles__button___2OOoS-camelCase" role="button" tabindex="0">Az@yU</div><div class="styles__button___2OOoS-camelCase" role="button" tabindex="0">kingOfMyHeart2000</div><div class="styles__button___2OOoS-camelCase" role="button" tabindex="0">(づ｡◕‿‿◕｡)づ</div></div>
            if pass_options:
                available_passwords = [pass_option.text for pass_option in pass_options]
                remaining_passwords = [password for password in available_passwords if password not in retrieved_passwords]
                if remaining_passwords:
                    random_pass = random.choice(remaining_passwords)
                    self.returned_pass = random_pass
                    break
                else:
                    random_pass = random.choice(available_passwords)
                    self.returned_pass = random_pass
                    break
            else:
                self.check_if_something_wrong()
                time.sleep(0.2)
    
    def choose_dict_pass(self):
        if self.victim in self.correct_passwords and self.correct_passwords[self.victim] is not None:
            self.returned_pass = self.correct_passwords[self.victim]
            self.pass_is_random = False
            return True
        else:
            return False

    def click_pass(self):
        while True:
            pass_container = self.driver.find_element(By.CSS_SELECTOR, 'div.styles__buttonContainer___3yX9w-camelCase')
            if pass_container:
                pass_buttons = pass_container.find_elements(By.CSS_SELECTOR, 'div.styles__button___2OOoS-camelCase[role="button"]')
                if pass_buttons:
                    target_button = None
                    for button in pass_buttons:
                        if button.text == self.returned_pass:
                            target_button = button
                            break
                    if not target_button:
                        # If no button with self.returned_pass is found, choose a random button
                        target_button = random.choice(pass_buttons)
                        self.returned_pass = target_button.text

                    target_button.click()
                    self.check_if_something_wrong()
                    if self.repeat():
                        continue
                    break
            self.check_if_something_wrong()
            time.sleep(0.3)
    
    def choose_pass(self):
        if self.choose_dict_pass():
            pass
        else:
            self.choose_random_pass()
    
    def check_if_pass_right(self):
        while True:
            correct_element = self.driver.find_element(By.XPATH, '//div[@class="styles__introHeader___Dzfym-camelCase" and text()="CORRECT"]')#<div class="styles__introHeader___Dzfym-camelCase" style="animation-delay: 2500ms; animation-duration: 1000ms;">CORRECT</div>
            incorrect_element = self.driver.find_element(By.XPATH, '//div[@class="styles__introHeader___Dzfym-camelCase" and text()="INCORRECT"]')#<div class="styles__introHeader___Dzfym-camelCase" style="animation-delay: 2500ms; animation-duration:1000ms; color:rgb(255, 51, 51);">INCORRECT</div>

            if correct_element.is_displayed():
                self.pass_correct = True
                break
            elif incorrect_element.is_displayed():
                self.pass_correct = False
                break
            self.check_if_something_wrong()
            time.sleep(0.3)
    
    def pass_was_random_right(self):
        if self.pass_is_random and self.pass_correct:
            self.correct_passwords[self.victim] = self.returned_pass
    
    def pass_is_wrong(self):
        if not self.pass_correct:
            if self.victim in self.password_attempts:
                self.password_attempts[self.victim].append(self.returned_pass)
            else:
                self.password_attempts[self.victim] = [self.returned_pass]

    def hacking(self):
        while True:
            if self.answer_was_true_reward_proceed("element_to_be_found = self.driver.find_element(By.CSS_SELECTOR, 'div.styles__introHeader___Dzfym-camelCase')"):
                break
        self.get_victim_name()
        self.create_keys_for_victims()
        self.choose_pass()
        self.click_pass()
        self.check_if_pass_right()
        self.pass_was_random_right()
        self.pass_is_wrong()
                        
    def answer_was_right(self):
        self.check_if_answer_is_random_right()
        self.click_reward()
        if self.reward_text != "HACK":
            self.answer_was_true_reward_proceed("element_to_be_found = self.driver.find_elements(By.CSS_SELECTOR, 'div.styles__questionText___2MlSZ-camelCase')")
        elif self.reward_text == "HACK":
            self.hacking()
            
    def answer_afterward(self):
        if not self.right:
            self.answer_was_wrong()
        elif self.right:
            self.answer_was_right()

    def initializing_action(self):
        self.init_variables()
        self.retrieve_user_input()
        self.init_driver()
        self.join_game()
        self.choose_password()
    
    def repetitive_action(self):
        while True:
            self.check_if_question_exists()
            self.retrieve_question_type()
            self.retrieve_question_answer()
            self.enter_answer()
            self.check_if_right()
            self.answer_afterward()
    
    def mainloop(self):
        try:
            self.initializing_action()
            self.repetitive_action()
        except Exception as e:
            e= str(e)
            if e== "Game ended":
                print(f'Expected exception in "{self.__class__.__name__}" instance of "Blooket_Crypto_Auto_Solver" class: Game Ended')
            else:
                print(f'Unexpected exception in "{self.__class__.__name__}" instance of "Blooket_Crypto_Auto_Solver" class: {e}')
        finally:
            self.driver.quit()

Crypto= Blooket_Crypto_Auto_Solver()
Crypto.mainloop()


#doesnt proceed after right