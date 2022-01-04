import logging

from django.core.management.base import BaseCommand


LOG_FORMAT = "%(asctime)s %(levelname)s %(module)s.%(funcName)s: %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

LOG = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Citrix API Build Helper Command"

    def handle(self, *args, **kwargs):
        LOG.info("Citrix API Test start ...")
