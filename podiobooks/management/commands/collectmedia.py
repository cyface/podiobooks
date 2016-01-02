"""Copies Media from the mediaroot dir to MEDIA_ROOT"""

import os
import shutil
from django.conf import settings
from django.core.management.base import CommandError, BaseCommand


class Command(BaseCommand):
    """
        Copy media to MEDIA_ROOT (useful when MEDIA_ROOT ends up being outside the code tree, e.g. on a server)
    """
    help = "Copy media files from local storage to MEDIA_ROOT"

    def handle(self, **options):

        local_media = os.path.join(settings.BASE_DIR, 'podiobooks', 'mediaroot')

        if os.path.exists(local_media):
            if not os.path.exists(settings.MEDIA_ROOT):
                os.mkdir(settings.MEDIA_ROOT)
            self.copy_dir(local_media, settings.MEDIA_ROOT)
        else:
            raise CommandError("Local Media Path '{0}' does not exist".format(local_media))

    def copy_dir(self, source_path, dest_path):
        """
            Copy a whole directory to new path

            :param source_path: source directory path
            :param dest_path: destination directory path
        """
        for item in os.listdir(source_path):
            item_path = os.path.join(source_path, item)
            if os.path.isdir(item_path):
                try:
                    os.mkdir(os.path.join(dest_path, item))
                except:
                    pass
                self.copy_dir(item_path, os.path.join(dest_path, item))
            else:
                try:
                    shutil.copy2(os.path.join(source_path, item), os.path.join(dest_path, item))
                except (shutil.Error, IOError) as error:
                    print error
