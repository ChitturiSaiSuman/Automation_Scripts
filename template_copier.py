#!/usr/bin/env python3
import os
import shutil
import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from colorama import Fore


def get_samples(problem_link: str) -> list:

    print(Fore.YELLOW + "Extracting samples for " + problem_link + " ...", end = "", flush = True)

    xpath = "//body/div[@id='ember-root']/div[@id='ember242']/div[@id='ember251']/main[@id='content-regions']/section[1]/div[1]/span[3]/pre[1]"

    xpath_prefix = "//body/div[@id='ember-root']/div[@id='ember242']/div[@id='ember251']/main[@id='content-regions']/section[1]/div[1]/span["
    xpath_suffix = "]/pre[1]"

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options = options)

    driver.get(problem_link)
    element = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.TAG_NAME, "code")))

    samples = []
    i = 1
    while True:
        absolute_xpath = xpath_prefix + str(i) + xpath_suffix
        try:
            element = driver.find_element(By.XPATH, absolute_xpath)
            samples.append(element.text)
            i += 1
        except:
            break

    driver.quit()
    print(Fore.GREEN + "Done", flush = True)
    return samples



def extract_problem_links(contest_link: str) -> list:
    print(Fore.CYAN + "Extracting problem links...", end = "", flush = True)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options = options)

    prefix = contest_link

    if "?" in contest_link:
        prefix = contest_link[:contest_link.index("?")]

    prefix += "/problems"

    driver.get(contest_link)
    element = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "dataTable")))

    all_links = driver.find_elements(By.TAG_NAME, 'a')

    problem_links = []

    for link in all_links:
        try:
            link = str(link.get_attribute('href'))
            if link.startswith(prefix):
                problem_links.append(link)
        except:
            print(Fore.RED + "Attempt to Extract failed. Retrying...", flush = True)
            return []
    
    driver.quit()
    if problem_links == []:
        print(Fore.RED + "Attempt to Extract failed. Retrying...", flush = True)
        return []
    print(Fore.GREEN + "Done", flush = True)
    return problem_links


def get_contest_name(contest_link: str) -> str:
    print(Fore.YELLOW + "Extracting contest name...", end = "", flush = True)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options = options)
    driver.get(contest_link)

    element = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "breadcrumbs")))
    element = driver.find_element(By.CLASS_NAME, 'breadcrumbs')
    inner_text = element.get_attribute('innerHTML')

    contest_name = inner_text[inner_text.rindex(";") + 1:]
    driver.quit()
    print(Fore.GREEN + "Done", flush = True)
    print(Fore.YELLOW + "Contest Name: " + Fore.GREEN + contest_name, flush = True)
    return contest_name

def get_problem_codes(problem_links: list) -> list:

    problem_codes = []
    for link in problem_links:
        code = link[link.rindex('/') + 1:]
        problem_codes.append(code)
    
    return problem_codes


def extract_meta_data(contest_link: str) -> dict:

    # Contest Code
    contest_code = ""
    if "?" in contest_link:
        contest_code = contest_link[contest_link.rindex("/") + 1: contest_link.index("?")]
    else:
        contest_code = contest_link[contest_link.rindex("/") + 1:]

    # Contest Name
    contest_name = get_contest_name(contest_link)

    # Problem links
    problem_links = []
    while problem_links == []:
        problem_links = extract_problem_links(contest_link)

    # Problem Codes
    problem_codes = get_problem_codes(problem_links)

    # Problem Samples
    problem_samples = []
    for link in problem_links:
        problem_samples.append(get_samples(link))

    # Problem Meta Data
    meta_data = {}
    meta_data['contest_code'] = contest_code
    meta_data['contest_name'] = contest_name
    meta_data['problem_links'] = problem_links
    meta_data['problem_codes'] = problem_codes
    meta_data['problem_samples'] = problem_samples

    return meta_data

def copy_default_files(path_to_workplace, path_to_templates) -> None:
    print()
    files_needed = ['Default.cpp', 'Extended.cpp', 'Generator.cpp', 'Test.cpp']
    for file in files_needed:
        print(Fore.YELLOW + "Copying " + file + "...", end = "", flush = True)
        shutil.copy(path_to_templates + "/" + file, path_to_workplace)
        print(Fore.GREEN + "Done", flush = True)
    print()

def create_problem(path_to_workplace: str, default_source: str, header: str, problem_link: str, problem_code: str, test_cases: list) -> None:
    path_to_file = path_to_workplace + "/" + problem_code + ".cpp"
    print(Fore.YELLOW + "Creating files for " + problem_code + "...", end = "", flush = True)

    with open(path_to_file, 'w') as file:
        problem_link = "Problem: " + problem_link + "\n"
        header = '/*\n' + header + problem_link + '*/\n'
        source_code = header + default_source
        file.write(source_code)

    for i in range(len(test_cases)):
        test_case = test_cases[i]
        sample_input = test_case[0]
        sample_output = test_case[1]

        input_file = path_to_workplace + "/" + problem_code + str(i) + ".in"
        with open(input_file, 'w') as file:
            file.write(sample_input)

        output_file = path_to_workplace + "/" + problem_code + str(i) + ".out"
        with open(output_file, 'w') as file:
            file.write(sample_output)
    
    
    print(Fore.GREEN + "Done", flush = True)
    

def parse_test_cases(test_cases: list, problem_code: str) -> list:
    # Given is a list of strings
    # [input0, output0, input1, output1, ...]
    # Returns list of tuples
    # With input and output zipped
    # [(input0, output0), (input1, output1), ...]
    parsed_test_cases = []
    for i in range(0, len(test_cases), 2):
        try:
            parsed_test_cases.append((test_cases[i], test_cases[i + 1]))
        except:
            print(Fore.RED + "Error in parsing test cases for " + problem_code + ".")
    return parsed_test_cases

def initialise_workplace(meta_data: dict) -> None:

    header = "Author: Chitturi Sai Suman" + "\n"
    header += "Powered by: GitHub Copilot" + "\n"
    header += "Created: " + meta_data['time'] + "\n"
    header += "Contest: " + meta_data['contest_name'] + "\n"

    path_to_workplace = '/home/suman/' + meta_data['contest_code']
    path_to_templates = '/home/suman/Desktop/Templates'

    print(Fore.YELLOW + "\nCreating workplace " + path_to_workplace + "...", end = "", flush = True)

    try:
        os.makedirs(path_to_workplace)
    except:
        pass

    copy_default_files(path_to_workplace, path_to_templates)

    default_source = ""
    with open(path_to_templates + "/Default.cpp", 'r') as file:
        default_source += file.read()

    for i in range(len(meta_data['problem_codes'])):
        problem_link = meta_data['problem_links'][i]
        problem_code = meta_data['problem_codes'][i]
        test_cases = meta_data['problem_samples'][i]
        test_cases = parse_test_cases(test_cases, problem_code)
        create_problem(path_to_workplace, default_source, header, problem_link, problem_code, test_cases)

    print()
    print(Fore.YELLOW + "Opening " + path_to_workplace + " in Code...", end = "", flush = True)
    os.system("code " + path_to_workplace)
    print(Fore.GREEN + "Done" + Fore.WHITE, flush = True)


if __name__ == '__main__':

    os.system("clear")

    now = datetime.datetime.now()
    now_str = str(now.strftime("%Y-%m-%d %H:%M:%S"))

    contest_link = input(Fore.YELLOW + "\nEnter Contest Link: " + Fore.WHITE)
    print()
    meta_data = extract_meta_data(contest_link)
    meta_data['time'] = now_str

    initialise_workplace(meta_data)
    print(Fore.YELLOW + "\nScrape time: " + Fore.GREEN + "" + str((datetime.datetime.now() - now).total_seconds()) + " seconds\n")