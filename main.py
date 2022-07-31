import requests
from bs4 import BeautifulSoup

url = "https://www.groupon.com/?utm_source=google&utm_medium=cpc&utm_campaign=us_dt_sea_ggl_txt_naq_sr_cbp_ch1_ybr_k*groupon_m*e_d*groupon-brand_g*groupon-exact_c*535923351489_ap*&gclid=CjwKCAjwrNmWBhA4EiwAHbjEQNwEpJsVGcdBRmVAFqcUSATcGIYY7VBrL2KU8hH8bnxDxDmtf3tyshoCrI8QAvD_BwE"

# url = "https://www.groupon.com/browse/salt-lake-city?lat=40.315&lng=-111.702&query=escape&address=Orem%2C+UT+84057&division=salt-lake-city&locale=en_US"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537/6',
    'origin': url,
    'referer': url
}

page = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(page.content, "html.parser")

job_container_tags = soup.find_all("div", class_="cui-udc-details")
job_titles = soup.find_all("div", class_="cui-udc-title")
job_locations = soup.find_all("div",  class_="cui-location-name")
job_ratings = soup.find_all("div", class_="numeric-count")
job_regular_prices = soup.find_all("div", class_="cui-price-original")
job_discount_prices = soup.find_all("div", class_="cui-price-discount")
job_description = soup.find_all("div", class_="cui-udc-subtitle")


for job in job_container_tags:
    job_title = job.find("div", class_="cui-udc-title")
    job_location = job.find("div", class_="cui-location-name")
    job_rating = job.find("div", class_="numeric-count")
    job_reglar_price = job.find("div", class_="cui-price-original")
    job_discount_price = job.find("div", class_="cui-price-discount")
    job_description = job.find("div", class_="cui-udc-subtitle")
    job_urgency_price = job.find("div", class_="cui-verbose-urgency-price")

    if job_title:
        print(job_title.string.strip())
    if job_location:
        print(job_location.string.strip())
    if job_rating:
        print(job_rating.string.strip())
    if job_reglar_price:
        print(job_reglar_price.string.strip())
    if job_discount_price:
        print(job_discount_price.string.strip())
    if job_urgency_price:
        print(job_urgency_price.string.strip())
    if job_description:
        print(job_description.string.strip())
    print()
