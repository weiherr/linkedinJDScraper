from bs4 import BeautifulSoup
import requests
import os

jd_extractor_ori_dir = os.getcwd()

### input your fixed location within the '' signs
fixed_jd_dir = (r'C:\Users\ooiwe\OneDrive\Job\Application (Companies)\UK 2022_23\JD')

### request directory input if none is given. suggest a fixed directory given above to reduce repeatable step.
if len(fixed_jd_dir) == 0:
    input_jd_dir = input('What is the directory in which the new folders are to be created in? \n')
    jd_folder = input_jd_dir
elif len(fixed_jd_dir) > 0:
    jd_folder = fixed_jd_dir
    
## debugging to see whether the jd_folder string is printed correctly
# print(jd_folder)

## debugging to see whether the files within the directory is listed correctly
# os.chdir(jd_folder)
# os.listdir()

### get job link and convert HTML text to BeautifuLSoup Object for easy HTML element searching and data extraction
link = input('What is the LinkedIn job link that you want to copy the JD from? \n')
html_text = requests.get(link).text
soup = BeautifulSoup(html_text, "html.parser")
# print(soup)

### get necessary data
job_company = soup.find('div', class_="topcard__flavor-row").a.text.strip()
job_title = soup.find('h1').text
job_description = soup.find('div', class_="show-more-less-html__markup show-more-less-html__markup--clamp-after-5 relative overflow-hidden")

## debugging of previous code on all the text extracted
# print(job_company)
# print(job_title)
# print(job_description)

### beautify the HTML formatting of the JD extracted in step above
html = job_description.prettify('utf-8')
## debugging of the method above
# print(html)

### get folder name and create folder
folder_name = (job_company + " - " + job_title).replace(r'/', ',')
## debugging of folder name
# print(folder_name)
path = os.path.join(jd_folder, folder_name)
## debugging joining of the variables to form full path for directory creation
# print(path)
split_path = path.split("\\")
shortened_path = split_path[-2] + '\\' + split_path[-1]
## debugging
# print(shortened_path)
## create new folder, can comment out if want to debug
try:
    os.mkdir(path)
except FileExistsError:
    print("Folder exists. Check on directory.")
else:
    ## debug to check what is the active directory, seems like mkdir will not change the active directory.
    # os.listdir()
    # print(os.getcwd())
    os.chdir(path)

    ### write HTML file into newly created folder
    jd_filename = 'JD.html'
    with open(jd_filename, "wb") as file:
        file.write(html)

    print(f'JD has been successfully created in {shortened_path}!')

    ### ----------------------- FILE OPEN (NO CHOICE) --------------------------- ###
    ### code to open file after saved
    written_jd = os.path.join(path, jd_filename)
    ## debugging join
    # print(written_jd)
    import webbrowser
    webbrowser.open_new_tab(written_jd)

    ### ----------------------- FILE OPEN (CHOICE) --------------------------- ###
    ### code to open file by choice
    # open_file_choice = input('Do you want to open the file? (Y/N)')
    # if open_file_choice == 'Y':
    #     written_jd = os.path.join(path, jd_filename)
    #     ## debugging join
    # #     print(written_jd)
    #     import webbrowser
    #     webbrowser.open_new_tab(written_jd)
