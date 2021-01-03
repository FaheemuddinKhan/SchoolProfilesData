import scrapy
import json
from ..items import NtschoolsItem


class NTschools(scrapy.Spider):
    name = "ntschools"
    start_urls = [
        'https://directory.ntschools.net/#/schools'
    ]

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US, en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "directory.ntschools.net",
        "Pragma": "no-cache",
        "Referer": "https://directory.ntschools.net/",
        "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-Requested-With": "Fetch"
    }

    def parse(self, response):
        base_url = "https://directory.ntschools.net/api/System/GetAllSchools"
        yield scrapy.Request(base_url, callback=self.parse_school_codes, headers=self.headers)

    def parse_school_codes(self, response):
        base_url = "https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="
        schools = json.loads(response.body)
        for school_data in schools:
            school_code = school_data["itSchoolCode"]
            school_url = base_url + school_code
            yield scrapy.Request(school_url, callback=self.parse_school, headers=self.headers)

    def parse_school(self,response):
        item = NtschoolsItem()
        school_data = json.loads(response.body)
        item["Name"] = school_data["name"]
        item["PhysicalAddress"] = school_data["physicalAddress"]["displayAddress"]
        item["PostalAddress"] = school_data["postalAddress"]["displayAddress"]
        item["Email"] = school_data["mail"]
        item["Phone"] = school_data["telephoneNumber"]

        yield item

