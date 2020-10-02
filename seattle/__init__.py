# encoding=utf-8
from pupa.scrape import Jurisdiction, Organization
from .events import SeattleEventScraper


class Seattle(Jurisdiction):
    division_id = "ocd-division/country:us/state:wa/place:seattle"
    classification = "executive"
    name = "Seattle"
    url = "seattle.gov"
    scrapers = {
        "events": SeattleEventScraper,
    }

    scrapers = {
        # "people": ChicagoPersonScraper,
        "events": SeattleEventScraper,
        # "bills": ChicagoBillScraper,
    }

    def get_organizations(self):
        #REQUIRED: define an organization using this format
        #where org_name is something like Seattle City Council
        #and classification is described here:
        org = Organization(name="Seattle City Council", classification="legislature")

        # OPTIONAL: add posts to your organization using this format,
        # where label is a human-readable description of the post (eg "Ward 8 councilmember")
        # and role is the position type (eg councilmember, alderman, mayor...)
        # skip entirely if you're not writing a people scraper.
        # org.add_post(label="position_description", role="position_type")

        #REQUIRED: yield the organization
        yield org
