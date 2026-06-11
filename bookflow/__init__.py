from django.db.backends.mysql.base import DatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

# 1. Vypneme kontrolu verze MariaDB
DatabaseWrapper.check_database_version_supported = lambda self: None

# 2. Vypneme RETURNING a SKIP LOCKED příkazy pro starší MariaDB
DatabaseFeatures.can_return_rows_from_bulk_insert = property(lambda self: False)
DatabaseFeatures.has_select_for_update_skip_locked = property(lambda self: False)