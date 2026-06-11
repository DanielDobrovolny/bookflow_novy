from django.db.backends.mysql.base import DatabaseWrapper as MysqlWrapper
from django.db.backends.mysql.features import DatabaseFeatures

class OpraveneFeatures(DatabaseFeatures):
    # KLÍČOVÁ OPRAVA: Tyto dva řádky kompletně zakážou klauzuli RETURNING v Django 6
    can_return_columns_from_insert = False
    can_return_rows_from_bulk_insert = False
    
    @property
    def has_select_for_update_skip_locked(self):
        return False

class DatabaseWrapper(MysqlWrapper):
    features_class = OpraveneFeatures

    # Ignorujeme starou verzi MariaDB v XAMPPu při startu
    def check_database_version_supported(self):
        pass