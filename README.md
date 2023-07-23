# LinkedIn JD Scraper
**Skills Showcased:** Python, Web Scraping, HTML

## Background
As a job seeker, it is frustrating to apply for jobs on pages like LinkedIn, and not to have any JD as reference a few weeks / months after the application as the application page was taken down, or that you have forgotten where you've applied. What I would have done to circumvent this issue is to copy and paste the JD into a word document and save it into a folder named as with the company and the job title (e.g. Coca-cola - Business Analyst). This was a multi-step process and takes roughly a minute or two. The time adds up when application number increases.

## Project Objective
This webscraping project is to automate these tasks to reduce time for each job application.

## Project Details
The project utilizes the BeautifulSoup library, which is a library that works by assessing the data within the HTML of a page. One can further specify the section by searching for the HTML elements' tag and class to get a specific data. This is reflected in the project as I extracted the job company, job title and job description from different elements.

As the JD for each company is built differently with different formattings, I chose to save the JD as a HTML file to maintain its format structure. Then, with the extracted Company Name and Job Title, a folder is created in the specified path given earlier in the code for the HTML file to be written. It is then a 3-step process.

  1. Copy the LinkedIn job posting link.
  2. Run the code.
  3. Paste the link into the input pop-up.

Simple and effective! Hope this will help other job seekers who looks to do the same too!
